r"""Xuất phiếu QC các turn FN (bỏ lọt) của một run eval multiturn để người tự review, cùng khuôn
reviews/2026-11-10-ANT-12164-mt-qc-review-agreed.xlsx. Không gọi API nào.

FN lấy đúng cách chấm của run_eval_vita_multiturn.py (st.judge, Gate 1 mặc định).

Chạy từ root folder:
  python3 intents-vita-207/eval/export_fn_review_form.py --run-dir intents-vita-207/eval/results/uat-fpt_v207_multiturn_20261111_171039

  --run-dir D   Thư mục run eval multiturn (có results.jsonl). Bắt buộc.
  --gate G      Gate để lấy FN (1 / 2). Mặc định: 1.

Ra: reviews/<run>-fn-qc-review.xlsx
  13 cột đầu như file agreed (ref = <id8>-tNN, context = 8 lượt trước, mỗi câu cắt 300 ký tự). Người review điền
  user_verdict_new / assistant_verdict_new (SAFE / VIOLATE) cho mọi dòng, rồi relabel theo skill singleturn-label-notes mục 4.
  Cột sau: sensitive (1 = hội thoại có intent thuộc qc_common.SENSITIVE), pair, strategy, mục V/KV generator khai,
  quyết định và findings của guardrail, note.
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "dataset"))
sys.path.insert(0, str(ROOT.parent / "share" / "eval"))
import run_eval_vita_singleturn as st  # noqa: E402  judge: kết cục turn như eval
import qc_common as C  # noqa: E402  SENSITIVE, SIDES, read_jsonl

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

CONTEXT_TURNS = 8           # số lượt trước ở cột context, như file agreed
CONTEXT_CHARS = 300         # cắt mỗi câu ở cột context, như file agreed
TIER_NAME = {"S0": "Nghiêm trọng", "S1": "Cao", "S2": "Trung bình"}

HEAD = ["ref", "kind", "category", "risk_tier", "intent_input", "intent_output", "context (lượt trước)", "user_text",
        "assistant_text", "user_verdict", "assistant_verdict", "user_verdict_new", "assistant_verdict_new"]
EXTRA = ["sensitive", "pair", "strategy", "gen_user_rule", "gen_assistant_rule", "user_decision", "assistant_decision",
         "assistant_findings", "note"]
WIDTHS = {"ref": 14, "context (lượt trước)": 60, "user_text": 45, "assistant_text": 60, "user_verdict": 19,
          "assistant_verdict": 20, "user_verdict_new": 18, "assistant_verdict_new": 25, "pair": 30,
          "assistant_findings": 30, "note": 40}


def fn_items(results, gate):
    """Turn FN của run, kèm các lượt trước và cờ hội thoại nhạy cảm."""
    items = []
    for conv in results:
        turns = sorted(conv["turns"], key=lambda x: x["t"])
        meta = {k: v for k, v in conv.items() if k != "turns"}
        sensitive = any((x.get(f"{s}_intent_id") or "").lower() in C.SENSITIVE for x in turns for s in C.SIDES)
        for x in turns:
            row = {**meta, **x}
            if st.judge(row, gate) == "fn":
                items.append({"ref": f"{conv['id'][:8]}-t{x['t']:02d}", "row": row, "sensitive": sensitive,
                              "prev": [y for y in turns if y["t"] < x["t"]]})
    refs = [it["ref"] for it in items]
    if len(refs) != len(set(refs)):
        raise SystemExit("❌ ref trùng (8 ký tự đầu id trùng nhau)")
    return sorted(items, key=lambda it: it["ref"])


def context_cell(prev):
    cut = lambda s: (s or "")[:CONTEXT_CHARS]
    return "\n".join(f"[t{x['t']}] U({x['user_verdict']}): {cut(x['user_text'])}\n"
                     f"[t{x['t']}] B({x['assistant_verdict']}): {cut(x['assistant_text'])}" for x in prev[-CONTEXT_TURNS:])


def sheet_row(it):
    row = it["row"]
    return {"ref": it["ref"], "kind": "FN", "category": row.get("category"), "risk_tier": TIER_NAME.get(row.get("tier"), row.get("tier")),
            "intent_input": row.get("user_intent_id"), "intent_output": row.get("assistant_intent_id"),
            "context (lượt trước)": context_cell(it["prev"]), "user_text": row["user_text"], "assistant_text": row["assistant_text"],
            "user_verdict": row["user_verdict"], "assistant_verdict": row["assistant_verdict"],
            "sensitive": int(it["sensitive"]), "pair": row.get("pair"), "strategy": row.get("strategy"),
            "gen_user_rule": row.get("user_rule"), "gen_assistant_rule": row.get("assistant_rule"),
            "user_decision": row.get("user_decision"), "assistant_decision": row.get("assistant_decision"),
            "assistant_findings": st._cats(row.get("assistant_findings"))}


def write_xlsx(path, rows):
    head = HEAD + EXTRA
    wb = Workbook()
    ws = wb.active
    ws.title = "Rows"
    ws.append(head)
    for r in rows:
        ws.append([r.get(h) for h in head])
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1F4E78")
    wrap = Alignment(wrap_text=True, vertical="top")
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = wrap
    for k, h in enumerate(head, 1):
        ws.column_dimensions[get_column_letter(k)].width = WIDTHS.get(h, 14)
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = ws.dimensions
    if rows:
        dv = DataValidation(type="list", formula1='"SAFE,VIOLATE"', allow_blank=True)
        dv.add(f"L2:M{len(rows) + 1}")
        ws.add_data_validation(dv)
    wb.save(path)


def main():
    ap = argparse.ArgumentParser(description="Xuất phiếu QC các turn FN của run eval multiturn để người tự review")
    ap.add_argument("--run-dir", type=Path, required=True)
    ap.add_argument("--gate", type=int, choices=[1, 2], default=1)
    a = ap.parse_args()

    results_path = a.run_dir / "results.jsonl"
    if not results_path.exists():
        raise SystemExit(f"❌ Không thấy {results_path}")
    items = fn_items(C.read_jsonl(results_path), a.gate)
    out_dir = ROOT / "reviews"
    out_dir.mkdir(exist_ok=True)
    xlsx_path = out_dir / f"{a.run_dir.name}-fn-qc-review.xlsx"
    write_xlsx(xlsx_path, [sheet_row(it) for it in items])
    print(f"FN Gate {a.gate}: {len(items)} turn / {len({it['row']['id'] for it in items})} hội thoại "
          f"(nhạy cảm {sum(it['sensitive'] for it in items)})\n📄 {xlsx_path}")


if __name__ == "__main__":
    main()
