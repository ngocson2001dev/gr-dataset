r"""Bước 2 của hậu kiểm: model ngoài (chat) chấm MÙ lại các câu, theo lô cùng intent (tối đa 10 câu), rồi lập phiếu cho người (bước 3).

Câu được chấm (theo kết quả Jev ở check/jev.jsonl):
  đỏ  = Jev lệch nhãn gán;  vàng = Jev khớp nhãn gán nhưng xác suất < ngưỡng hoặc không ổn định;
  mẫu xanh = --sample-rate câu vùng xanh, chia tầng theo cặp × phía (user/assistant) × nhãn (VIOLATE/SAFE), mỗi tầng ít nhất 1 câu, ổn định giữa các lần chạy.
Model không thấy nhãn gán và kết quả Jev; script tự so sánh rồi suy ra gợi ý và nguyên nhân (qc_common.review_action).
Prompt nằm ở dataset/review_prompt.md (sửa ở đó, không sửa trong code).

Chạy từ root folder:
  python3 intents-vita-207/dataset/review_check.py 20261006_231257 --dry-run
  python3 intents-vita-207/dataset/review_check.py 20261006_231257

  <run>             STAMP của lần chạy hoặc đường dẫn thư mục đó (bắt buộc).
  --model M         Model chấm: 'hãng/model' (OpenRouter) hoặc tên trần (Vertex MaaS, xem share/llm/llm_vertex_ai.py).
                    Mặc định: gemini-3.5-flash (khác họ với model sinh deepseek; so trên 81 câu đỏ 20261009_161300
                    khớp nhãn người chấm 89%, qwen3-235b và glm-5.2 68%).
  --dry-run         Chỉ đếm số câu, số lô, ước lượng token; KHÔNG gọi API (vẫn lập lại phiếu từ kết quả đã có).
  --threshold T     Ngưỡng vùng xanh của Jev. Mặc định: 0.85.
  --sample-rate R   Tỉ lệ mẫu kiểm tra vùng xanh. Mặc định: 0.05.
  --seed S          Seed chọn mẫu xanh. Mặc định: 207.
  --batch K         Số câu một lô (tối đa 10). Mặc định: 10.
  --workers W       Số request song song. Mặc định: 4.
  --xlsx            Ghi thêm phiếu cho người check/work/review_todo.xlsx. Mặc định: tắt.

Ra:
  check/review.jsonl         kết quả từng câu (key, h, verdict, matched, partial, on_topic, text_broken, reason, model).
                             verdict do code suy ra từ matched/partial/on_topic (C.derive_verdict), không do model chọn
  check/work/review.md       thống kê gợi ý theo vùng, nguyên nhân theo ô và intent; mục V/KV generator khai (`<phía>_rule`)
                             so với `matched` của model chấm: các mục hay bị sinh lệch (cột gen_rule trong phiếu)
  check/work/review_todo.xlsx  (chỉ khi --xlsx) phiếu cho người: câu cần quyết định (gợi ý ≠ giữ ở đỏ/vàng/mẫu xanh, và câu có lỗi ERROR của
                             inspect_dataset). Điền cột decision (keep / relabel / fix_text / drop / boundary), new_label, new_text,
                             note rồi chạy import_decisions.py. Quyết định đã có được điền sẵn. Cột sensitive = 1 là 7 intent nhạy cảm.
                             Sheet gate_dropped (nếu generator chạy có cổng lọc): câu cổng đã loại lúc sinh, chỉ để xem nhanh.

Nhãn model chấm: VIOLATE (khớp rõ VP, không dính KV) · SAFE (khớp rõ KV, không dính VP) · WRONG_SUBJECT (không dính mục nào,
lệch chủ đề) · UNCLEAR (còn lại). Kết quả cũ (prompt r1–r2) có BOUNDARY, được đọc như UNCLEAR.
Gợi ý: keep (người chấm = nhãn gán; ở vùng đỏ là Jev sai) · relabel (người chấm và Jev cùng lệch nhãn gán) ·
manual_check (bất đồng ở vùng vàng/xanh) · wrong_subject (lệch chủ đề) · unclear (không phân định được) · fix_text (câu hỏng) ·
qc (lỗi inspect). Cổng lọc của generator loại câu relabel, wrong_subject, unclear, fix_text.
Nguyên nhân: A = sinh nhầm loại mẫu, B = subprompt mơ hồ, C = text lỗi, D = Jev sai.
Thứ tự xử lý khuyến nghị: sửa text cho khớp nhãn gán > đổi nhãn (khi cặp user/trợ lý vẫn hợp lý) > loại.
"""
import argparse
import collections
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "share" / "llm"))
import jev_check as JC  # noqa: E402  KEY_OF_INTENT, criteria_of
import inspect_dataset as INS  # noqa: E402  inspect_rows, errors_by_key
import qc_common as C  # noqa: E402
import llm_core  # noqa: E402  build_auth: 'hãng/model' → OpenRouter, tên trần (deepseek-v3.2-maas) → Vertex MaaS

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

PROMPT = (HERE / "review_prompt.md").read_text(encoding="utf-8")
DEFAULT_REVIEW_MODEL = "gemini-3.5-flash"   # chọn 2026-10-09, xem --model trong docstring
PROMPT_VERSION = "r5"   # r5 = câu scope=context kèm các lượt trước (cổng lọc multiturn); r4 = model trả matched/partial/on_topic, code suy nhãn (4 nhãn); r3 = thêm Lưu ý riêng; r2 = matched, reason trước verdict; r1 = verdict trước
ORDER = {"relabel": 0, "manual_check": 1, "wrong_subject": 2, "unclear": 3, "fix_text": 4, "qc": 5, "keep": 6, None: 7}
ACTIONS = ["keep", "relabel", "manual_check", "wrong_subject", "unclear", "fix_text", "chưa chấm"]


def bullets(prefix, lines):
    return "\n".join(f"- {prefix}{k + 1}: {t}" for k, t in enumerate(lines))


def cau_of(k, it):
    """Một câu trong prompt; câu có `context` (qc_common.attach_context) kèm các lượt trước để hiểu câu, nhưng chỉ chấm câu cuối."""
    if not it.get("context"):
        return f"[c{k}] {it['text']}"
    who = {"user": "Người dùng", "assistant": "AI"}
    ctx = "\n".join(f"    {who[s]}: {t}" for s, t in it["context"])
    return f"[c{k}] Ngữ cảnh (các lượt trước, chỉ để hiểu câu, KHÔNG chấm):\n{ctx}\n  Câu cần chấm: {it['text']}"


def build_prompt(group):
    from generate import load_sub  # noqa: E402
    s = load_sub(JC.KEY_OF_INTENT[group[0]["intent"]])
    cau = "\n".join(cau_of(k, it) for k, it in enumerate(group))
    kind = "câu người dùng gửi cho AI (input)" if group[0]["intent"].endswith("_input") else "câu trả lời của AI (output)"
    return (PROMPT.replace("{{CHU_DE}}", s["topic"]).replace("{{LOAI_CAU}}", kind).replace("{{VI_PHAM}}", bullets("VP", s["violates"]))
            .replace("{{KHONG_VI_PHAM}}", bullets("KV", s["not_violates"]))
            .replace("{{LUU_Y}}", "\n".join(f"- {t}" for t in s["notes"]) or "- (không có)").replace("{{CAC_CAU}}", cau))


def run(model, todo, path, size, workers):
    f = path.open("a", encoding="utf-8", newline="\n")
    auth = llm_core.build_auth(model)
    cost = [0.0]

    def call(lot):
        res, meta = auth.call_batch(model, build_prompt(lot))
        cost[0] += meta.get("cost_usd", 0) or 0
        if meta.get("error") or len(res) != len(lot):
            return None, meta.get("error") or f"trả {len(res)}/{len(lot)} phần tử"
        out = []
        for k, it in enumerate(lot):
            r = res[k]
            if (not isinstance(r, dict) or r.get("id") != f"c{k}" or not isinstance(r.get("on_topic"), bool)
                    or not all(isinstance(r.get(f), list) for f in ("matched", "partial"))):
                return None, f"phần tử c{k} sai định dạng"
            matched, partial = C.codes(r["matched"]), [x for x in C.codes(r["partial"]) if x not in r["matched"]]
            out.append({"key": it["key"], "h": it["h"], "verdict": C.derive_verdict(matched, partial, r["on_topic"]),
                        "matched": matched, "partial": partial, "on_topic": r["on_topic"], "text_broken": bool(r.get("text_broken")),
                        "reason": r.get("reason", ""), "model": model, "prompt": PROMPT_VERSION})
        return out, ""

    def process(its, sz, label):
        lots, _ = JC.lots_of(its, sz)
        print(f"[{model}] {label}: {sum(len(l) for l in lots)} câu trong {len(lots)} lô")
        failed = []
        with ThreadPoolExecutor(workers) as ex:
            for lot, (out, why) in zip(lots, ex.map(call, lots)):
                if out is None:
                    failed += [(it, why) for it in lot]
                    continue
                for d in out:
                    f.write(json.dumps(d, ensure_ascii=False) + "\n")
                f.flush()
        return failed

    failed = process(todo, size, "lượt 1")
    if failed and size > 1:
        failed = process([it for it, _ in failed], 1, "thử lại từng câu")
    for it, why in failed:
        f.write(json.dumps({"key": it["key"], "h": it["h"], "error": why}, ensure_ascii=False) + "\n")
    f.close()
    print(f"[{model}] còn lỗi {len(failed)} câu; chi phí thật ≈ ${cost[0]:.4f} (Vertex không trả chi phí → 0)")


def write_todo(P, rows_todo):
    head = ["key", "sensitive", "zone", "suggestion", "cause", "intent", "side", "assigned_label", "jev_label", "jev_prob",
            "reviewer_verdict", "gen_rule", "matched", "partial", "reason", "qc_errors", "text", "partner_text",
            "decision", "new_label", "new_text", "note"]
    wb = Workbook()
    ws = wb.active
    ws.title = "todo"
    ws.append(head)
    for x in rows_todo:
        ws.append([x.get(h, "") for h in head])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="305496" if c.column <= head.index("decision") else "C2410C")
    widths = {"key": 36, "intent": 30, "reviewer_verdict": 14, "reason": 36, "qc_errors": 20, "text": 70, "partner_text": 50,
              "decision": 12, "new_text": 60, "note": 30}
    for k, h in enumerate(head, 1):
        ws.column_dimensions[get_column_letter(k)].width = widths.get(h, 10)
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    # tô màu các cột nhãn theo giá trị cho dễ so: đỏ VIOLATE, xanh SAFE, vàng UNCLEAR/UNSURE, tím WRONG_SUBJECT
    label_fill = {"VIOLATE": "F8CBAD", "SAFE": "C6EFCE", "UNCLEAR": "FFEB9C", "BOUNDARY": "FFEB9C", "UNSURE": "FFEB9C", "WRONG_SUBJECT": "D9D2E9"}
    for col in ("assigned_label", "jev_label", "reviewer_verdict"):
        for c in ws[get_column_letter(head.index(col) + 1)][1:]:
            if c.value in label_fill:
                c.fill = PatternFill("solid", fgColor=label_fill[c.value])
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = ws.dimensions
    # dropdown cho cột người điền: giá trị hợp lệ theo import_decisions.py
    last = max(ws.max_row, 2)
    for col, values, tip in (("decision", C.DECISIONS, "keep: giữ nhãn gán · relabel: đảo nhãn gán · fix_text: sửa text "
                              "(điền new_text) · drop: loại · boundary: ranh giới"),
                             ("new_label", ("VIOLATE", "SAFE"), "Chỉ dùng khi fix_text cần đổi nhãn. keep / relabel bỏ qua cột này")):
        dv = DataValidation(type="list", formula1='"' + ",".join(values) + '"', allow_blank=True,
                            showErrorMessage=True, errorTitle="Giá trị không hợp lệ", error="Chọn trong danh sách: " + ", ".join(values),
                            showInputMessage=True, promptTitle=col, prompt=tip[:255])
        letter = get_column_letter(head.index(col) + 1)
        dv.add(f"{letter}2:{letter}{last}")
        ws.add_data_validation(dv)
    write_gate_sheet(wb, P, label_fill)
    wb.save(P.todo)


def write_gate_sheet(wb, P, label_fill):
    """Sheet 'gate_dropped': câu cổng lọc của generator đã loại (raw/..._dropped.jsonl, reason gate_*). Chỉ để xem nhanh
    xem cổng có loại nhầm câu khó không; không cần điền, không nhập."""
    rows = [d for d in C.read_jsonl(P.run / "raw" / f"{C.PREFIX}_{P.stamp}_dropped.jsonl") if str(d.get("reason", "")).startswith("gate")]
    if not rows:
        return
    head = ["sensitive", "reason", "pair", "cell", "intent_id", "style", "surface", "hard", "zone", "jev_label", "jev_prob",
            "review_verdict", "review_matched", "review_partial", "review_reason", "text"]
    ws = wb.create_sheet("gate_dropped")
    ws.append(head)
    rows.sort(key=lambda d: (d["intent_id"] in C.SENSITIVE, d["pair"], d["cell"]))
    for d in rows:
        x = dict(d, sensitive=int(d["intent_id"] in C.SENSITIVE), review_matched=",".join(d.get("review_matched") or []),
                 review_partial=",".join(d.get("review_partial") or []))
        ws.append([x.get(h, "") if x.get(h) is not None else "" for h in head])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="305496")
    widths = {"reason": 16, "pair": 28, "cell": 16, "intent_id": 30, "surface": 18, "review_reason": 40, "text": 80}
    for k, h in enumerate(head, 1):
        ws.column_dimensions[get_column_letter(k)].width = widths.get(h, 10)
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    for col in ("jev_label", "review_verdict"):
        for c in ws[get_column_letter(head.index(col) + 1)][1:]:
            if c.value in label_fill:
                c.fill = PatternFill("solid", fgColor=label_fill[c.value])
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions


def rule_agreement(items, have):
    """So mã mục V/KV generator khai (meta `<phía>_rule`) với `matched` của model chấm, trên các câu đã chấm.
    Lưu ý: tập đã chấm lệch về vùng đỏ/vàng nên tỉ lệ ở đây thấp hơn toàn dataset; dùng để tìm mục hay bị sinh lệch."""
    rows = []
    for it in items:
        r = have.get(it["key"])
        rule = it["meta"].get(f"{it['side']}_rule")
        if r and rule:
            rows.append((it, rule, r))
    if not rows:
        return []
    hit = sum(rule in (r.get("matched") or []) for _, rule, r in rows)
    md = ["", "## Mục V/KV generator khai so với model chấm", f"- {len(rows)} câu đã chấm có mã; model chấm có khớp đúng mục đó: "
          f"{hit} ({100 * hit / len(rows):.1f}%). Tập đã chấm lệch về vùng đỏ/vàng, nên chỉ dùng để tìm mục hay bị sinh lệch.", "",
          "| intent | phía | mục khai | số câu | model chấm khớp mục | model chấm đổi nhãn | model chấm thấy thay |", "|---|---|---|---|---|---|---|"]
    g = collections.defaultdict(list)
    for it, rule, r in rows:
        g[(it["intent"], it["side"], rule)].append((it, r))
    def rkey(x):
        return (x[0], x[1], x[2][:2], int(x[2][2:]) if x[2][2:].isdigit() else 0)
    for k in sorted(g, key=rkey):
        xs = g[k]
        miss = [(it, r) for it, r in xs if k[2] not in (r.get("matched") or [])]
        if not miss:
            continue
        flip = sum(C.verdict_of(r) != it["assigned"] for it, r in xs)
        other = collections.Counter(m for _, r in miss for m in (r.get("matched") or []))
        md.append(f"| {k[0]} | {k[1]} | {k[2]} | {len(xs)} | {len(xs) - len(miss)} | {flip} | "
                  f"{', '.join(f'{m}×{n}' for m, n in other.most_common(3)) or '–'} |")
    return md


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--model", default=DEFAULT_REVIEW_MODEL)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--threshold", type=float, default=0.85)
    ap.add_argument("--sample-rate", type=float, default=0.05)
    ap.add_argument("--seed", type=int, default=207)
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--xlsx", action="store_true")
    a = ap.parse_args()
    a.batch = min(a.batch, 10)

    P = C.Paths(C.run_dir(a.run))
    rows, dec = C.load_rows(P)
    items = C.items_of(rows)
    by_key = {it["key"]: it for it in items}
    jev = C.load_results(P.jev, items)
    if not jev:
        raise SystemExit(f"Chưa có kết quả Jev ({P.jev}) — chạy jev_check.py trước")
    zone = C.zones(items, jev, a.threshold)
    sample = C.green_sample(items, zone, a.sample_rate, a.seed)
    cand = [it for it in items if zone.get(it["key"]) in ("red", "yellow") or it["key"] in sample]
    cand_keys = {it["key"] for it in cand}
    have = C.load_results(P.review, items)
    todo = [it for it in cand if it["key"] not in have]
    zc = collections.Counter(zone[it["key"]] for it in cand)
    lots, _ = JC.lots_of(todo, a.batch)
    print(f"{P.stamp}: chấm {len(cand)} câu (đỏ {zc['red']}, vàng {zc['yellow']}, mẫu xanh {len(sample)}/"
          f"{sum(z == 'green' for z in zone.values())}); đã có {len(cand) - len(todo)}, cần chấm {len(todo)} trong {len(lots)} lô")
    if todo:
        print(f"  ước lượng ~{sum(len(build_prompt(l)) for l in lots) // 3:,} token vào, ~{len(todo) * 70:,} token ra")
        if not a.dry_run:
            run(a.model, todo, P.review, a.batch, a.workers)
            have = C.load_results(P.review, items)

    # gợi ý cho từng câu đã chấm + lỗi inspect
    qc = INS.errors_by_key(INS.inspect_rows(rows)[0])
    todo_rows, stats = [], []
    for it in items:
        k = it["key"]
        z = zone.get(k)
        r = have.get(k)
        act, cause = (C.review_action(it, z, r) if r else (None, ""))
        if z in ("red", "yellow") or k in sample:
            stats.append(dict(it=it, zone="green_sample" if z == "green" else z, act=act or "chưa chấm", cause=cause))
        need = (r is not None and not C.auto_trusted(z, act, k in sample)) or (z == "red" and r is None) or k in qc
        if not need and k not in dec:
            continue
        if not need:      # đã có quyết định nhưng không còn cần người → vẫn hiện để đối chiếu
            act = act or "keep"
        d = dec.get(k, {})
        j = jev.get(k, {})
        m = it["meta"]
        todo_rows.append(dict(
            key=k, sensitive=int(it["intent"] in C.SENSITIVE), zone=("green_sample" if z == "green" and k in sample else z or ""),
            suggestion=("qc" if k in qc and act in (None, "keep") else act or ""), cause=cause, intent=it["intent"], side=it["side"],
            assigned_label=it["assigned"], jev_label=j.get("label", ""), jev_prob=j.get("prob", ""),
            reviewer_verdict=C.verdict_of(r) if r else "",
            gen_rule=m.get(f"{it['side']}_rule") or "", matched=",".join((r or {}).get("matched", [])),
            partial=",".join((r or {}).get("partial", [])), reason=(r or {}).get("reason", ""), qc_errors="; ".join(qc.get(k, [])), text=it["text"],
            partner_text=m["assistant_text" if it["side"] == "user" else "user_text"],
            decision=d.get("decision", ""), new_label=d.get("new_label", ""), new_text=d.get("new_text", ""), note=d.get("note", "")))
    todo_rows.sort(key=lambda x: (x["sensitive"], ORDER.get(x["suggestion"] or None, 6), x["intent"], x["key"]))
    if a.xlsx:
        write_todo(P, todo_rows)

    md = [f"# Review {P.stamp}", f"- model: {', '.join(sorted({d.get('model', '?') for d in have.values()})) or '–'}; "
          f"ngưỡng Jev {a.threshold}; mẫu xanh {a.sample_rate:.0%} (seed chọn mẫu {a.seed}, khác seed generator)", "",
          "## Gợi ý theo vùng", "| vùng | " + " | ".join(ACTIONS) + " |", "|---|" + "---|" * len(ACTIONS)]
    for z in ("red", "yellow", "green_sample"):
        c = collections.Counter(x["act"] for x in stats if x["zone"] == z)
        md.append(f"| {z} | " + " | ".join(str(c[k]) for k in ACTIONS) + " |")
    md += ["", "## Nguyên nhân theo ô (A sinh nhầm, B subprompt mơ hồ, C text lỗi, D Jev sai)", "| ô | số câu | A | B | C | D |",
           "|---|---|---|---|---|---|"]
    for cell in sorted({(x["it"]["side"], x["it"]["assigned"]) for x in stats}):
        sub = [x for x in stats if (x["it"]["side"], x["it"]["assigned"]) == cell]
        c = collections.Counter(x["cause"] for x in sub)
        md.append(f"| {cell[0]}/{cell[1]} | {len(sub)} | {c['A']} | {c['B']} | {c['C']} | {c['D']} |")
    md += rule_agreement(items, have)
    (P.work / "review.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Cần người xem: {len(todo_rows)} câu ({sum(x['sensitive'] for x in todo_rows)} thuộc 7 intent nhạy cảm)"
          + (f" → {P.todo}" if a.xlsx else "  (thêm --xlsx để ghi phiếu review_todo.xlsx)"))


if __name__ == "__main__":
    main()
