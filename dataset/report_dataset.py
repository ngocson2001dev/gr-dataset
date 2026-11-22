r"""Bước 4 (cuối) của hậu kiểm: gộp kết quả mọi bước → trạng thái từng câu, tách dataset cuối / bị loại, và báo cáo thống kê.
Chỉ đọc kết quả đã có, KHÔNG gọi model (chạy lại bao nhiêu lần cũng được).

Đầu vào (trong dataset/<STAMP>/): merged/, check/jev.jsonl, check/review.jsonl, check/work/decisions.jsonl; lỗi inspect_dataset
được tính lại tại chỗ (tất định).

Trạng thái mỗi câu (theo thứ tự ưu tiên):
  quyết định của người  → reviewed_keep / fixed_text / relabeled / dropped / boundary
  lỗi ERROR của inspect → pending_qc
  chưa có kết quả Jev    → unchecked
  xanh (ngoài mẫu, hoặc trong mẫu và model ngoài đồng ý) → trusted_auto
  vàng và model ngoài đồng ý nhãn gán                  → trusted_model
  còn lại (đỏ, vàng/mẫu xanh mà model ngoài không đồng ý, chưa chấm) → pending_review
Một dòng (cặp user, trợ lý) vào dataset cuối khi CẢ HAI câu thuộc: trusted_auto, trusted_model, reviewed_keep, fixed_text, relabeled.

Chạy từ root folder (Windows):
  python intents-vita-207/dataset/report_dataset.py 20261006_231257

  <run>             STAMP của lần chạy hoặc đường dẫn thư mục đó (bắt buộc).
  --threshold T     Ngưỡng vùng xanh của Jev (phải khớp bước 2). Mặc định: 0.85.
  --sample-rate R   Tỉ lệ mẫu xanh (phải khớp bước 2). Mặc định: 0.05.
  --seed S          Seed mẫu xanh (phải khớp bước 2). Mặc định: 207.
  --min-n N         Số câu tối thiểu của một giá trị thuộc tính để tính lift. Mặc định: 30.

Ra (trong check/):
  report.md                    báo cáo cuối
  V207_<STAMP>_final.jsonl     dataset đã hậu kiểm (dòng merged đã phủ bản sửa + trường qc = trạng thái 2 câu)
  V207_<STAMP>_rejected.jsonl  dòng bị loại hoặc còn chờ (thêm trường reject_reasons)
"""
import argparse
import collections
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import qc_common as C  # noqa: E402
import inspect_dataset as INS  # noqa: E402

KEPT = ("trusted_auto", "trusted_model", "reviewed_keep", "fixed_text", "relabeled")
CLEAN = ("trusted_auto", "trusted_model", "reviewed_keep")          # không có vấn đề gì
STATUSES = KEPT + ("dropped", "boundary", "pending_review", "pending_qc", "unchecked")
USER_ATTRS = ("user_style", "user_surface", "user_obf", "user_hard", "user_aspect", "tier", "category")
ASSIST_ATTRS = ("assistant_style", "assistant_hard", "assistant_aspect", "tier", "category")


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "–"


def wilson(x, n, z=1.96):
    if not n:
        return "–"
    p = x / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return f"{100 * max(0, c - h) / d:.1f}% – {100 * (c + h) / d:.1f}%"


def table(head, rows):
    return ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--threshold", type=float, default=0.85)
    ap.add_argument("--sample-rate", type=float, default=0.05)
    ap.add_argument("--seed", type=int, default=207)
    ap.add_argument("--min-n", type=int, default=30)
    a = ap.parse_args()
    P = C.Paths(C.run_dir(a.run))

    base, _ = C.load_rows(P, apply_decisions=False)
    base_by = {r["id"]: r for r in base}
    rows, dec_all = C.load_rows(P)
    base_h = {f"{r['id']}:{s}": C.text_hash(r[f"{s}_text"]) for r in base for s in C.SIDES}
    dec = {k: d for k, d in dec_all.items() if d.get("base_h") == base_h.get(k)}
    items = C.items_of(rows)
    jev = C.load_results(P.jev, items)
    rv = C.load_results(P.review, items)
    zone = C.zones(items, jev, a.threshold)
    sample = C.green_sample(items, zone, a.sample_rate, a.seed)
    qc = INS.errors_by_key(INS.inspect_rows(rows)[0])

    # ---- trạng thái từng câu
    st, cause, act_of = {}, {}, {}
    for it in items:
        k, z, r = it["key"], zone.get(it["key"]), rv.get(it["key"])
        act, cz = C.review_action(it, z, r) if (r and z) else (None, "")
        act_of[k], cause[k] = act, cz
        d = dec.get(k)
        if d:
            orig = base_by[it["id"]][f"{it['side']}_verdict"]
            st[k] = {"drop": "dropped", "boundary": "boundary"}.get(d["decision"]) or (
                "fixed_text" if d.get("new_text") else "relabeled" if d.get("new_label", orig) != orig else "reviewed_keep")
        elif k in qc:
            st[k] = "pending_qc"
        elif z is None:
            st[k] = "unchecked"
        elif z == "green" and act in (None, "keep"):   # xanh: tin trừ khi model ngoài đã chấm và không đồng ý (kể cả câu ngoài mẫu hiện tại)
            st[k] = "trusted_auto"
        elif z == "yellow" and act == "keep":
            st[k] = "trusted_model"
        else:
            st[k] = "pending_review"

    # ---- tách file
    final, rejected = [], []
    for r in rows:
        s = {side: st[f"{r['id']}:{side}"] for side in C.SIDES}
        out = dict(r, qc=s)
        if all(v in KEPT for v in s.values()):
            final.append(out)
        else:
            out["reject_reasons"] = [f"{side}:{v}" for side, v in s.items() if v not in KEPT]
            rejected.append(out)
    C.write_jsonl(P.final, final)
    C.write_jsonl(P.rejected, rejected)

    # ---- báo cáo
    manifest = json.loads((P.run / "raw" / f"{C.PREFIX}_{P.stamp}_run.json").read_text(encoding="utf-8")) \
        if (P.run / "raw" / f"{C.PREFIX}_{P.stamp}_run.json").exists() else {}
    models = lambda res: ", ".join(f"{m} ({n})" for m, n in collections.Counter(f"{d.get('model', '?')}/{d.get('prompt', '?')}" for d in res.values()).most_common()) or "–"
    md = [f"# Báo cáo hậu kiểm {P.stamp}", "",
          f"- Sinh: model {manifest.get('model', '?')}, kênh {manifest.get('channel', '?')}; {len(rows)} dòng cặp = {len(items)} câu",
          f"- Bước 1 Jev: {models(jev)}; ngưỡng vùng xanh {a.threshold}",
          f"- Bước 2 model ngoài: {models(rv)}; mẫu xanh {a.sample_rate:.0%} (seed chọn mẫu {a.seed}, khác seed generator; {len(sample)} câu)",
          f"- Bước 3 quyết định của người: {len(dec)} câu" + (f" ({len(dec_all) - len(dec)} quyết định cũ không khớp text gốc, bỏ qua)" if len(dec_all) > len(dec) else ""),
          f"- Lỗi inspect (ERROR) chưa xử lý được tính là pending_qc", ""]

    # 1. tổng kết
    md += ["## 1. Tổng kết", "",
           f"- **Dataset cuối: {len(final)}/{len(rows)} dòng ({pct(len(final), len(rows))})** → `{P.final.name}`",
           f"- **Bị loại / còn chờ: {len(rejected)} dòng** → `{P.rejected.name}`", ""]
    cells = sorted({(it["side"], base_by[it["id"]][f"{it['side']}_verdict"]) for it in items})
    by_cell = collections.defaultdict(collections.Counter)
    for it in items:
        by_cell[(it["side"], base_by[it["id"]][f"{it['side']}_verdict"])][st[it["key"]]] += 1
    tot = collections.Counter(st.values())
    md += ["Trạng thái câu theo ô (nhãn gán gốc):", ""]
    md += table(["trạng thái"] + [f"{s}/{v}" for s, v in cells] + ["tổng"],
                [[x] + [by_cell[c][x] for c in cells] + [tot[x]] for x in STATUSES if tot[x]])
    rr = collections.Counter(reason for r in rejected for reason in r["reject_reasons"])
    md += ["", "Lý do loại (theo câu gây loại; một dòng có thể có 2 lý do):", ""]
    md += table(["lý do", "số câu"], rr.most_common())
    combo = lambda rs: collections.Counter(r["user_verdict"][0] + r["assistant_verdict"][0] for r in rs)
    cb, cf = combo(base), combo(final)
    md += ["", "Loại cặp (user→trợ lý): sinh ra → giữ lại", ""] + table(["combo", "sinh", "giữ", "tỉ lệ giữ"],
                                                                       [[c, cb[c], cf[c], pct(cf[c], cb[c])] for c in sorted(cb)])
    changed = sum(1 for r in final if r["user_verdict"] != base_by[r["id"]]["user_verdict"] or r["assistant_verdict"] != base_by[r["id"]]["assistant_verdict"])
    if changed:
        md.append(f"\n{changed} dòng trong dataset cuối đã đổi nhãn so với bản sinh (loại cặp đổi theo).")

    # 2. độ tin cậy
    md += ["", "## 2. Độ tin cậy", ""]
    s_rev = [k for k in sample if k in rv]
    s_dis = [k for k in s_rev if act_of[k] != "keep"]
    s_dec = [k for k in s_dis if k in dec]
    s_err = [k for k in s_dec if st[k] not in ("reviewed_keep",)]
    md += [f"- Mẫu xanh: {len(sample)} câu, model ngoài đã chấm {len(s_rev)}, không đồng ý nhãn gán {len(s_dis)}, "
           f"người đã quyết {len(s_dec)}, xác nhận lỗi {len(s_err)}.",
           f"  - Cận trên tỉ lệ lỗi vùng xanh (model ngoài không đồng ý, chưa ai xác nhận): {len(s_dis)}/{len(s_rev)} = "
           f"{pct(len(s_dis), len(s_rev))}, KTC 95% {wilson(len(s_dis), len(s_rev))}. Các câu này không vào dataset cuối.",
           f"  - Lỗi đã được người xác nhận: {len(s_err)}/{len(s_dec)} câu đã quyết" if s_dec else
           "  - Chưa có người xác nhận (chế độ tự động): lỗi thật nằm giữa 0 và cận trên trên; lỗi mà cả Jev lẫn model ngoài cùng bỏ sót không đo được."]
    both = [k for k in dec if k in rv and dec[k]["decision"] in ("keep", "relabel", "fix_text")]
    final_label = {it["key"]: it["assigned"] for it in items}
    ok_rv = sum(rv[k]["verdict"] == final_label[k] for k in both)
    ok_j = sum(jev[k]["label"] == final_label[k] for k in both if k in jev)
    md += [f"- Trên {len(both)} câu người đã quyết (keep / relabel / fix_text): model ngoài khớp nhãn cuối {pct(ok_rv, len(both))}, "
           f"Jev khớp {pct(ok_j, len(both))} (tập khó, không đại diện cả dataset).",
           f"- Câu đã sửa text: {sum(1 for k, v in st.items() if v == 'fixed_text')}; trong đó Jev chấm lại khớp nhãn "
           f"{sum(1 for k, v in st.items() if v == 'fixed_text' and k in jev and jev[k]['label'] == final_label[k])}, chưa chấm lại "
           f"{sum(1 for k, v in st.items() if v == 'fixed_text' and k not in jev)}."]

    # 3. theo intent × ô
    md += ["", "## 3. Theo intent × ô (sắp theo tỉ lệ có vấn đề)", "",
           "có vấn đề = không thuộc trusted_auto / trusted_model / reviewed_keep. A sinh nhầm loại mẫu, B subprompt mơ hồ, D Jev sai.", ""]
    grp = collections.defaultdict(list)
    for it in items:
        grp[(it["intent"], base_by[it["id"]][f"{it['side']}_verdict"])].append(it)
    lines = []
    for (intent, lab), its in grp.items():
        c = collections.Counter(st[it["key"]] for it in its)
        cz = collections.Counter(cause[it["key"]] for it in its)
        bad = sum(v for k, v in c.items() if k not in CLEAN)
        lines.append((bad / len(its), [intent + (" 🔒" if intent in C.SENSITIVE else ""), lab, len(its), f"{bad} ({pct(bad, len(its))})",
                                       sum(c[k] for k in KEPT), c["fixed_text"] + c["relabeled"], c["dropped"] + c["boundary"],
                                       c["pending_review"] + c["pending_qc"] + c["unchecked"], cz["A"], cz["B"], cz["D"]]))
    lines.sort(key=lambda x: -x[0])
    md += table(["intent", "nhãn gán", "câu", "có vấn đề", "giữ", "đã cứu", "loại", "chờ", "A", "B", "D"],
                [l for _, l in lines if l[3][0] != "0"])

    # 4. thuộc tính: lift
    md += ["", "## 4. Thuộc tính của câu có vấn đề (lift)", "",
           f"lift = tỉ lệ câu có vấn đề của giá trị đó ÷ tỉ lệ chung của cùng phía. > 1.5 là đáng xem. Chỉ giá trị có ≥ {a.min_n} câu.", ""]
    for side, attrs in (("user", USER_ATTRS), ("assistant", ASSIST_ATTRS)):
        its = [it for it in items if it["side"] == side]
        base_rate = sum(st[it["key"]] not in CLEAN for it in its) / len(its)
        lines = []
        for attr in attrs:
            vals = collections.defaultdict(list)
            for it in its:
                vals[str(it["meta"][attr])].append(it)
            for v, sub in vals.items():
                if len(sub) < a.min_n:
                    continue
                bad = sum(st[it["key"]] not in CLEAN for it in sub)
                lift = (bad / len(sub)) / base_rate if base_rate else 0
                lines.append((lift, [attr, v, len(sub), f"{bad} ({pct(bad, len(sub))})", f"{lift:.2f}" + (" ⚠" if lift > 1.5 else "")]))
        lines.sort(key=lambda x: -x[0])
        md += [f"### Câu {side} (tỉ lệ chung {100 * base_rate:.1f}%)", ""]
        md += table(["thuộc tính", "giá trị", "câu", "có vấn đề", "lift"], [l for _, l in lines[:20]]) + [""]

    # 5. lỗi hình thức
    md += ["## 5. Lỗi hình thức (inspect, ERROR) chưa xử lý", ""]
    md += table(["mã", "số câu"], collections.Counter(c for k, cs in qc.items() if st[k] == "pending_qc" for c in cs).most_common()) + [""]

    # 6. thiếu hụt
    md += ["## 6. Thiếu hụt so với số câu sinh ra (intent × ô, giữ < 90%)", ""]
    short = []
    for (intent, lab), its in grp.items():
        kept = sum(st[it["key"]] in KEPT for it in its)
        if kept < 0.9 * len(its):
            short.append((kept / len(its), [intent, lab, len(its), kept, len(its) - kept]))
    short.sort(key=lambda x: x[0])
    md += table(["intent", "nhãn gán", "sinh", "giữ", "thiếu"], [l for _, l in short]) if short else ["Không có."]

    # 7. hành động
    md += ["", "## 7. Gợi ý hành động", ""]
    a_top = sorted(((sum(cause[it["key"]] == "A" for it in its), intent, lab) for (intent, lab), its in grp.items()), reverse=True)[:8]
    b_top = sorted(((sum(cause[it["key"]] == "B" or st[it["key"]] == "boundary" for it in its), intent, lab) for (intent, lab), its in grp.items()), reverse=True)[:8]
    md += ["- **Sửa prompt sinh** (nhiều câu sinh nhầm loại mẫu, A): " + ", ".join(f"{i}/{l} ({n})" for n, i, l in a_top if n),
           "- **Sửa subprompt** (nhiều câu ranh giới, B): " + ", ".join(f"{i}/{l} ({n})" for n, i, l in b_top if n),
           f"- **Còn chờ người**: {tot['pending_review']} câu pending_review, {tot['pending_qc']} câu pending_qc → phiếu `work/review_todo.xlsx`",
           f"- **Chưa có kết quả Jev**: {tot['unchecked']} câu → chạy jev_check.py" if tot["unchecked"] else ""]
    P.report.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Dataset cuối {len(final)}/{len(rows)} dòng, bị loại/chờ {len(rejected)} → {P.report}")


if __name__ == "__main__":
    main()
