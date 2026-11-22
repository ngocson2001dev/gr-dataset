"""Phần dùng chung của các bước hậu kiểm (inspect_dataset, jev_check, review_check, import_decisions, report_dataset).

Một lần chạy = một thư mục dataset/<STAMP>/:
  raw/      file raw theo ô (generator ghi, hậu kiểm không sửa)
  merged/   V207_<STAMP>_pairs.jsonl (generator ghi, hậu kiểm không sửa)
  check/    jev.jsonl, review.jsonl, report.md, V207_<STAMP>_final.jsonl, V207_<STAMP>_rejected.jsonl
  check/work/  file làm việc: inspect.md/.xlsx, jev.md/.xlsx, review.md, review_todo.xlsx (phiếu cho người), decisions.jsonl

Bản sửa của người (sửa text, đổi nhãn, loại) nằm trong check/work/decisions.jsonl và được "phủ" lên merged khi đọc
(load_rows), nên raw/merged giữ nguyên bản sinh ra. Mỗi kết quả chấm (Jev, model ngoài) lưu kèm mã băm text `h`:
text đổi thì kết quả cũ tự hết hiệu lực và câu đó được chấm lại.
"""
import hashlib
import json
import re
from pathlib import Path

DATASET = Path(__file__).resolve().parent
PREFIX = "V207"
SIDES = ("user", "assistant")
SENSITIVE = {   # 7 intent nhạy cảm cao: chỉ người (chủ dataset) đọc; Claude không đọc
    "humanity_weapon_explosive_device_input", "humanity_weapon_explosive_device_output",
    "illegal_csam_input", "illegal_csam_output",
    "humanity_cbrn_massdestruction_input", "humanity_cbrn_massdestruction_output",
    "humanity_harmtool_incapacitation_input",
}
DECISIONS = ("keep", "relabel", "fix_text", "drop", "boundary")


def run_dir(arg):
    """STAMP, đường dẫn thư mục lần chạy, hoặc đường dẫn file merged → thư mục lần chạy."""
    p = Path(arg)
    if p.is_file():
        p = p.parent.parent
    elif not p.is_dir():
        p = DATASET / arg
    if not (p / "merged").is_dir():
        raise SystemExit(f"Không phải thư mục lần chạy (thiếu merged/): {p}")
    return p.resolve()


class Paths:
    def __init__(self, run):
        self.run = run
        self.stamp = run.name
        self.merged = run / "merged" / f"{PREFIX}_{self.stamp}_pairs.jsonl"
        self.check = run / "check"
        self.work = self.check / "work"
        self.jev = self.check / "jev.jsonl"
        self.review = self.check / "review.jsonl"
        self.report = self.check / "report.md"
        self.final = self.check / f"{PREFIX}_{self.stamp}_final.jsonl"
        self.rejected = self.check / f"{PREFIX}_{self.stamp}_rejected.jsonl"
        self.decisions = self.work / "decisions.jsonl"
        self.todo = self.work / "review_todo.xlsx"
        self.work.mkdir(parents=True, exist_ok=True)


def text_hash(text):
    return hashlib.sha1((text or "").encode("utf-8")).hexdigest()[:12]


def read_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def write_jsonl(path, rows):
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    tmp.replace(path)


def load_decisions(paths):
    """key → quyết định đã gộp (bản ghi sau ghi đè trường của bản trước)."""
    out = {}
    for d in read_jsonl(paths.decisions):
        out.setdefault(d["key"], {}).update({k: v for k, v in d.items() if v not in (None, "")})
    return out


def load_rows(paths, apply_decisions=True):
    """Dòng merged, đã phủ bản sửa text / đổi nhãn trong decisions. Trả (rows, decisions).
    Quyết định chỉ áp khi `base_h` khớp text gốc trong merged (merged sinh lại thì quyết định cũ bỏ qua)."""
    rows = read_jsonl(paths.merged)
    dec = load_decisions(paths) if apply_decisions else {}
    stale = 0
    for r in rows:
        for side in SIDES:
            d = dec.get(f"{r['id']}:{side}")
            if not d:
                continue
            if d.get("base_h") != text_hash(r[f"{side}_text"]):
                stale += 1
                continue
            if d.get("new_text"):
                r[f"{side}_text"] = d["new_text"]
            if d.get("new_label"):
                r[f"{side}_verdict"] = d["new_label"]
    if stale:
        print(f"⚠ {stale} quyết định không khớp text gốc trong merged (merged đã sinh lại?) → bỏ qua")
    return rows, dec


def items_of(rows):
    """Mỗi dòng merged → 2 câu (user, assistant)."""
    out = []
    for r in rows:
        for side in SIDES:
            t = r[f"{side}_text"]
            out.append(dict(key=f"{r['id']}:{side}", id=r["id"], side=side, intent=r[f"{side}_intent_id"], text=t,
                            assigned=r[f"{side}_verdict"], h=text_hash(t), meta=r))
    return out


def attach_context(items, rows):
    """Câu scope=context (generator multiturn khai `<phía>_scope`): gắn `context` = các lượt trước trong cùng hội thoại (với câu trợ lý
    thì thêm câu user cùng lượt), để model chấm lại hiểu mật danh, mảnh ghép, vai đã dựng. Jev vẫn chấm riêng từng câu."""
    by_conv = {}
    for r in rows:
        by_conv.setdefault(r.get("conversation_id"), []).append(r)
    for it in items:
        m = it["meta"]
        if m.get(f"{it['side']}_scope") != "context":
            continue
        prev = sorted((r for r in by_conv.get(m.get("conversation_id"), []) if r["turn"] < m["turn"]), key=lambda r: r["turn"])
        ctx = [(side, r[f"{side}_text"]) for r in prev for side in SIDES]
        if it["side"] == "assistant":
            ctx.append(("user", m["user_text"]))
        it["context"] = ctx
    return items


def load_results(path, items):
    """Kết quả chấm còn hiệu lực: bản ghi mới nhất của mỗi key, bỏ bản lỗi, bỏ bản có `h` khác text hiện tại."""
    cur = {it["key"]: it["h"] for it in items}
    out = {}
    for d in read_jsonl(path):
        if "error" in d:
            out.pop(d["key"], None)
        elif cur.get(d["key"]) == d.get("h"):
            out[d["key"]] = d
    return out


def zones(items, jev, threshold):
    """key → 'green' / 'yellow' / 'red' theo Jev (câu chưa có kết quả Jev thì không có vùng)."""
    z = {}
    for it in items:
        j = jev.get(it["key"])
        if not j:
            continue
        if j["label"] != it["assigned"]:
            z[it["key"]] = "red"
        elif j["prob"] < threshold or not j["stable"]:
            z[it["key"]] = "yellow"
        else:
            z[it["key"]] = "green"
    return z


def green_sample(items, zone, rate, seed):
    """Mẫu kiểm tra vùng xanh: chia tầng theo cặp × phía × nhãn (để mọi cặp, cả user lẫn trợ lý, đều được kiểm),
    mỗi tầng lấy max(1, round(rate × n)) câu có băm (seed, key) nhỏ nhất. Ổn định giữa các lần chạy: cùng tập xanh → cùng mẫu."""
    strata = {}
    for it in items:
        if zone.get(it["key"]) == "green":
            strata.setdefault((it["meta"]["pair"], it["side"], it["assigned"]), []).append(it["key"])
    out = set()
    for keys in strata.values():
        keys.sort(key=lambda k: hashlib.sha1(f"{seed}:{k}".encode()).hexdigest())
        out.update(keys[:max(1, round(rate * len(keys)))])
    return out


def codes(xs):
    """Mã mục hợp lệ (VP/KV kèm số) trong danh sách model chấm trả về, bỏ trùng, giữ thứ tự."""
    return list(dict.fromkeys(x.strip().upper() for x in xs if isinstance(x, str) and re.fullmatch(r"\s*(VP|KV)\d+\s*", x, re.I)))


def derive_verdict(matched, partial, on_topic):
    """Nhãn model chấm, suy từ mục khớp rõ (matched), khớp một phần (partial) và có thuộc chủ đề không (on_topic):
    VIOLATE = khớp rõ VP, không dính KV · SAFE = khớp rõ KV, không dính VP · WRONG_SUBJECT = không dính mục nào và lệch chủ đề ·
    UNCLEAR = còn lại (dính cả hai, chỉ khớp một phần, hoặc đúng chủ đề mà không khớp mục nào)."""
    has = lambda xs, p: any(x.startswith(p) for x in xs)
    if has(matched, "VP") and not has(matched + partial, "KV"):
        return "VIOLATE"
    if has(matched, "KV") and not has(matched + partial, "VP"):
        return "SAFE"
    if not matched and not partial and on_topic is False:
        return "WRONG_SUBJECT"
    return "UNCLEAR"


def verdict_of(rv):
    """Nhãn model chấm của một bản ghi; kết quả cũ (prompt r1–r3) có BOUNDARY → UNCLEAR."""
    return "UNCLEAR" if rv["verdict"] == "BOUNDARY" else rv["verdict"]


def review_action(it, zone, rv):
    """Gợi ý từ kết quả model ngoài → (hành động, nguyên nhân).
    A = sinh nhầm loại mẫu, B = subprompt mơ hồ, C = text lỗi, D = Jev sai."""
    v = verdict_of(rv)
    if rv.get("text_broken"):
        return "fix_text", "C"
    if v == "WRONG_SUBJECT":
        return "wrong_subject", "A"
    if v == "UNCLEAR":
        return "unclear", "B"
    if v == it["assigned"]:
        return "keep", ("D" if zone == "red" else "")
    if rv.get("confidence") == "low":     # chỉ kết quả cũ (prompt r1–r3) có confidence
        return "manual_check", "B"
    return ("relabel" if zone == "red" else "manual_check"), "A"


def auto_trusted(zone, action, sampled):
    """Câu được tin mà không cần người: xanh (không vào mẫu, hoặc vào mẫu và model ngoài đồng ý), vàng mà model ngoài đồng ý."""
    if zone == "green":
        return action in (None, "keep")
    return zone == "yellow" and action == "keep"
