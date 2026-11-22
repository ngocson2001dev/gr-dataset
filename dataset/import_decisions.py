r"""Bước 3 (tuỳ chọn) của hậu kiểm: nhập quyết định của người từ phiếu review_todo.xlsx (sinh bằng review_check.py --xlsx) vào check/work/decisions.jsonl.

Mỗi dòng phiếu có cột decision khác rỗng được nhập (dòng trống bỏ qua). Giá trị decision:
  keep      giữ nguyên nhãn gán (model chấm sai); bỏ qua new_label
  fix_text  sửa text cho khớp nhãn gán: điền new_text (ưu tiên cách này để giữ cặp user/trợ lý và phân bố ô)
  relabel   đảo nhãn gán gốc (VIOLATE ↔ SAFE), bỏ qua new_label; chỉ dùng khi cặp user/trợ lý vẫn hợp lý
  drop      loại câu (cả dòng cặp sẽ vào file bị loại)
  boundary  câu ranh giới, tiêu chí không phân định (vào file bị loại, đếm riêng trong báo cáo để sửa subprompt)
fix_text có thể kèm đổi nhãn: điền cả new_text lẫn new_label.

decisions.jsonl chỉ nối thêm (không xoá dòng cũ); bản ghi sau ghi đè trường của bản trước. Mỗi bản ghi lưu `base_h` = mã băm
text gốc trong merged: merged sinh lại thì quyết định cũ tự bỏ qua. raw/merged không bị sửa; bản sửa được phủ lên khi đọc.
Sau khi nhập, câu có text mới sẽ được Jev và model ngoài chấm lại ở lần chạy sau (để xác minh bản sửa).

Chạy từ root folder (Windows):
  python intents-vita-207/dataset/import_decisions.py 20261006_231257
  python intents-vita-207/dataset/import_decisions.py 20261006_231257 --xlsx ~/Downloads/phieu_da_dien.xlsx --by huy

  <run>          STAMP của lần chạy hoặc đường dẫn thư mục đó (bắt buộc).
  --xlsx FILE    Phiếu đã điền. Mặc định: check/work/review_todo.xlsx.
  --by NAME      Tên người quyết định ghi vào bản ghi. Mặc định: human.
"""
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qc_common as C  # noqa: E402

from openpyxl import load_workbook


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--xlsx")
    ap.add_argument("--by", default="human")
    a = ap.parse_args()
    P = C.Paths(C.run_dir(a.run))
    xlsx = Path(a.xlsx) if a.xlsx else P.todo

    base, _ = C.load_rows(P, apply_decisions=False)
    base_h = {f"{r['id']}:{s}": C.text_hash(r[f"{s}_text"]) for r in base for s in C.SIDES}
    base_label = {f"{r['id']}:{s}": r[f"{s}_verdict"] for r in base for s in C.SIDES}
    dec = C.load_decisions(P)

    ws = load_workbook(xlsx, read_only=True).active
    it = ws.iter_rows(values_only=True)
    head = [str(h) for h in next(it)]
    col = {h: i for i, h in enumerate(head)}
    for need in ("key", "decision", "new_label", "new_text", "note"):
        if need not in col:
            raise SystemExit(f"Phiếu thiếu cột {need}")

    now = datetime.now().isoformat(timespec="seconds")
    out, errors, same = [], [], 0
    for n, row in enumerate(it, 2):
        get = lambda h: (row[col[h]] if col[h] < len(row) and row[col[h]] is not None else "")
        key, decision = str(get("key")).strip(), str(get("decision")).strip().lower()
        if not key or not decision:
            continue
        if key not in base_h:
            errors.append(f"dòng {n}: key không có trong merged: {key}")
            continue
        if decision not in C.DECISIONS:
            errors.append(f"dòng {n}: decision '{decision}' không hợp lệ (dùng {', '.join(C.DECISIONS)})")
            continue
        new_text = str(get("new_text")).strip()
        new_label = str(get("new_label")).strip().upper()
        if decision == "fix_text" and not new_text:
            errors.append(f"dòng {n}: fix_text cần new_text")
            continue
        if decision == "keep":   # keep / relabel: nhãn lấy theo decision, bỏ qua cột new_label
            new_label = ""
        elif decision == "relabel":
            new_label = "SAFE" if base_label[key] == "VIOLATE" else "VIOLATE"
        if new_label and new_label not in ("VIOLATE", "SAFE"):
            errors.append(f"dòng {n}: new_label '{new_label}' không hợp lệ")
            continue
        rec = {"key": key, "base_h": base_h[key], "decision": decision, "new_label": new_label or None,
               "new_text": new_text or None, "note": str(get("note")).strip() or None, "by": a.by, "time": now}
        old = dec.get(key, {})
        if all(old.get(k) == rec[k] for k in ("decision", "new_label", "new_text", "note") if rec[k] is not None):
            same += 1
            continue
        out.append({k: v for k, v in rec.items() if v is not None})

    for e in errors:
        print("✗", e)
    if out:
        with open(P.decisions, "a", encoding="utf-8", newline="\n") as f:
            for r in out:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Nhập {len(out)} quyết định mới, {same} không đổi, {len(errors)} lỗi → {P.decisions}")
    if out:
        print("Tiếp theo: chạy lại jev_check.py và review_check.py (chấm lại câu có text mới), rồi report_dataset.py")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
