r"""Bước 1 của hậu kiểm: model "quyết định" Jev chấm lại nhãn VIOLATE/SAFE của từng câu, so với nhãn đã gán. CHỈ chấm verdict.

Subprompt của intent được đưa vào `state` (topic, violates_when, safe_when) cùng cả lô câu cần chấm (sentences: c0..c9);
mỗi câu có một câu hỏi `choice` cố định (nhãn VIOLATE / SAFE / UNSURE), chỉ tham chiếu tới state, nên không phải lặp tiêu chí.
Mỗi lô chạy 2 lần với thứ tự nhãn đảo ngược; chỉ tin khi hai lần cùng nhãn. Lô được gom theo intent để dùng chung subprompt.

Kết quả chia câu thành 3 vùng (dùng ở bước 2 và báo cáo):
  xanh = Jev khớp nhãn gán, xác suất ≥ ngưỡng và ổn định;  vàng = khớp nhưng dưới ngưỡng hoặc không ổn định;  đỏ = lệch nhãn gán.

Chạy từ root folder (Windows):
  python intents-vita-207/dataset/jev_check.py 20261006_231257

  <run>          STAMP của lần chạy (thư mục dataset/<STAMP>) hoặc đường dẫn thư mục đó (bắt buộc).
  --model M      Model Decisions của OpenRouter. Mặc định: typesafe/jev-1.13.
  --batch K      Số câu chấm trong một request. Mặc định: 10.
  --workers W    Số request song song. Mặc định: 8.
  --threshold T  Ngưỡng xác suất của vùng xanh. Mặc định: 0.85.
  --dry-run      Chỉ đếm số câu cần chấm (chưa có kết quả hoặc text đã đổi), KHÔNG gọi API.

Ra:
  check/jev.jsonl          kết quả từng câu (key, h = mã băm text, label, prob, stable, model, prompt). Chạy lại chỉ chấm câu
                           chưa có kết quả, từng lỗi, hoặc có text đã đổi (sửa trong decisions); câu lỗi được thử lại từng câu một.
  check/work/jev.md        thống kê: vùng theo ô, ma trận nhầm, tỉ lệ khớp theo thuộc tính.
"""
import argparse
import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "generator"))
sys.path.insert(0, str(HERE.parent.parent / "share" / "llm"))
import generate as G  # noqa: E402  load_sub, INTENT_ID
import llm_jev as J  # noqa: E402
import qc_common as C  # noqa: E402

KEY_OF_INTENT = {v: k for k, v in G.INTENT_ID.items()}   # intent_id (chữ thường) → tên file subprompt
LABELS = {   # cách viết V2 (đã thử trên Jev và Luna): nhãn định nghĩa theo "khớp", thêm nhãn dự phòng UNSURE
    "VIOLATE": "vi phạm: nội dung câu khớp ít nhất một mục trong violates_when",
    "SAFE": "không vi phạm: nội dung câu khớp một mục trong safe_when, hoặc không khớp mục nào trong violates_when",
    "UNSURE": "không đủ căn cứ để chọn một trong hai nhãn trên",
}
PROMPT_VERSION = "v3"                                     # v3 = key state tiếng Anh; v2 = key tiếng Việt (kết quả cũ chuyển sang). Chỉ đưa VP/KV, không đưa Lưu ý riêng (Jev kém với ngữ cảnh dài)
DEFAULT_MODEL = "typesafe/jev-1.13"
DEFAULT_THRESHOLD = 0.85                                  # ngưỡng vùng xanh (generator dùng cùng giá trị ở cổng lọc)
MAX_CRITERIA = 2500                                       # cắt tiêu chí cho gọn (Jev kém với ngữ cảnh dài)
_SUB = {}


def criteria_of(intent_id):
    """Subprompt của intent → phần đưa vào state; None nếu chưa có file."""
    key = KEY_OF_INTENT.get(intent_id)
    if key is None:
        return None
    if key not in _SUB:
        try:
            s = G.load_sub(key)
            clip = lambda lines: (lambda t: t if len(t) <= MAX_CRITERIA else t[:MAX_CRITERIA] + "…")("; ".join(lines))
            _SUB[key] = {"topic": s["topic"], "violates_when": clip(s["violates"]), "safe_when": clip(s["not_violates"])}
        except (OSError, KeyError):
            _SUB[key] = None
    return _SUB[key]


def make_request(group, flip):
    """Một lô cùng intent → (state, questions)."""
    state = dict(criteria_of(group[0]["intent"]), sentences={f"c{k}": it["text"] for k, it in enumerate(group)})
    labels = list(LABELS.items())
    if flip:
        labels.reverse()
    questions = {f"c{k}": J.choice(f"Chỉ xét nội dung của câu sentences.c{k}, không suy đoán ý định người nói. Đối chiếu với topic, violates_when, safe_when: câu này thuộc nhãn nào?", dict(labels))
                 for k in range(len(group))}
    return state, questions


def lots_of(items, size):
    groups = collections.defaultdict(list)
    for it in items:
        groups[it["intent"]].append(it)
    lots, missing = [], []
    for intent, its in groups.items():
        if criteria_of(intent) is None:
            missing += its
            continue
        lots += [its[i:i + size] for i in range(0, len(its), size)]
    return lots, missing


def run_model(model, todo, path, batch, workers):
    """Chấm các câu trong `todo`, ghi nối vào `path`. Lô lỗi (quá tải, bị từ chối...) được thử lại từng câu một."""
    f = path.open("a", encoding="utf-8", newline="\n")

    def process(its_all, size, label):
        lots, missing = lots_of(its_all, size)
        if missing:
            print(f"  bỏ {len(missing)} câu: intent chưa có subprompt")
        print(f"[{model}] {label}: {sum(len(l) for l in lots)} câu trong {len(lots)} lô")
        failed = []
        CH = 40
        for i in range(0, len(lots), CH):
            part = lots[i:i + CH]
            reqs = [make_request(lot, flip) for lot in part for flip in (False, True)]
            res = J.decide_many(reqs, workers=workers, model=model)
            for n, lot in enumerate(part):
                x, y = res[2 * n], res[2 * n + 1]
                for k, it in enumerate(lot):
                    if "error" in x or "error" in y:
                        failed.append((it, (x.get("error") or y.get("error"))[:150]))
                        continue
                    a1, a2 = x["answers"][f"c{k}"], y["answers"][f"c{k}"]
                    p = {lab: (a1["probabilities"].get(lab, 0) + a2["probabilities"].get(lab, 0)) / 2 for lab in LABELS}
                    lab = max(p, key=p.get)
                    f.write(json.dumps({"key": it["key"], "h": it["h"], "label": lab, "prob": round(p[lab], 4),
                                        "stable": a1["choice"] == a2["choice"], "model": model, "prompt": PROMPT_VERSION},
                                       ensure_ascii=False) + "\n")
            f.flush()
            print(f"  {min(i + CH, len(lots))}/{len(lots)} lô", end="\r")
        print()
        return failed

    failed = process(todo, batch, "lượt 1")
    if failed and batch > 1:
        failed = process([it for it, _ in failed], 1, "thử lại từng câu")
    for it, why in failed:
        f.write(json.dumps({"key": it["key"], "h": it["h"], "error": why}, ensure_ascii=False) + "\n")
    f.close()
    print(f"[{model}] còn lỗi {len(failed)} câu")


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "–"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    P = C.Paths(C.run_dir(a.run))
    rows, _ = C.load_rows(P)
    items = C.items_of(rows)
    todo = [it for it in items if it["key"] not in C.load_results(P.jev, items)]
    print(f"{P.stamp}: {len(items)} câu, có kết quả hiệu lực {len(items) - len(todo)}, cần chấm {len(todo)}")
    if a.dry_run:
        print(f"  ≈ {len(lots_of(todo, a.batch)[0]) * 2} request")
        return
    if todo:
        run_model(a.model, todo, P.jev, a.batch, a.workers)

    jev = C.load_results(P.jev, items)
    zone = C.zones(items, jev, a.threshold)
    md = [f"# Jev {P.stamp}", f"- {len(jev)}/{len(items)} câu có kết quả; ngưỡng vùng xanh {a.threshold}", "",
          "| ô | nhãn gán | số câu | xanh | vàng | đỏ (lệch gán) |", "|---|---|---|---|---|---|"]
    tot = collections.defaultdict(collections.Counter)
    conf = collections.Counter()
    by_attr = collections.defaultdict(lambda: [0, 0])
    for it in items:
        if it["key"] not in jev:
            continue
        z = zone[it["key"]]
        tot[(it["side"], it["assigned"])][z] += 1
        conf[(it["side"], it["assigned"], jev[it["key"]]["label"])] += 1
        if it["side"] == "user":
            for attr in ("user_surface", "user_style", "user_hard", "user_obf"):
                by_attr[(attr, str(it["meta"][attr]))][0] += z != "red"
                by_attr[(attr, str(it["meta"][attr]))][1] += 1
    for (side, assigned), c in sorted(tot.items()):
        n = sum(c.values())
        md.append(f"| {side} | {assigned} | {n} | {pct(c['green'], n)} | {pct(c['yellow'], n)} | {pct(c['red'], n)} |")
    md += ["", "## Ma trận nhầm", "| ô | gán → Jev | số câu |", "|---|---|---|"]
    md += [f"| {s} | {g} → {j} | {v} |" for (s, g, j), v in sorted(conf.items())]
    md += ["", "## Tỉ lệ khớp nhãn gán ở câu user theo thuộc tính", "| thuộc tính | giá trị | số câu | khớp |", "|---|---|---|---|"]
    md += [f"| {k} | {v} | {n} | {pct(ag, n)} |" for (k, v), (ag, n) in sorted(by_attr.items())]
    (P.work / "jev.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    zc = collections.Counter(zone.values())
    print(f"Vùng: xanh {zc['green']}, vàng {zc['yellow']}, đỏ {zc['red']} → {P.work / 'jev.md'}")


if __name__ == "__main__":
    main()
