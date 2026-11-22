# Dataset v2.07 và hậu kiểm

Mỗi lần sinh (generator/generate.py) có một thư mục `dataset/<STAMP>/`:

```
<STAMP>/
  raw/      file raw theo ô + run.json (generator ghi, hậu kiểm không sửa)
  merged/   V207_<STAMP>_pairs.jsonl, mỗi dòng một cặp (câu user, câu trợ lý)
  check/
    jev.jsonl                    kết quả Jev (bước 1)
    review.jsonl                 kết quả model ngoài (bước 2)
    report.md                    báo cáo cuối (bước 4)
    V207_<STAMP>_final.jsonl     dataset đã hậu kiểm: chỉ dòng có cả 2 câu đúng hoặc đã sửa
    V207_<STAMP>_rejected.jsonl  dòng bị loại hoặc còn chờ, kèm lý do
    work/                        inspect.md, jev.md, review.md, decisions.jsonl; tuỳ chọn: inspect.xlsx (--xlsx), review_todo.xlsx (--xlsx)
```

## Quy trình (chạy từ thư mục gốc repo)

Generator in sẵn các lệnh này khi sinh xong.

| Bước | Lệnh `python3 intents-vita-207/dataset/…` | Tốn tiền |
|---|---|---|
| 0. Lỗi hình thức (tất định) | `inspect_dataset.py <STAMP>` (`--xlsx`: danh sách dòng bị cờ) | không |
| 1. Jev chấm mọi câu, chia vùng | `jev_check.py <STAMP>` | ít |
| 2. Model ngoài chấm đỏ + vàng + 5% xanh, lập phiếu | `review_check.py <STAMP> --xlsx` (model mặc định `gemini-3.5-flash`, đổi bằng `--model`) | có |
| 3. (tuỳ chọn) Người điền `check/work/review_todo.xlsx` rồi nhập | `import_decisions.py <STAMP>` | không |
| 3'. Có câu sửa text: chấm lại | chạy lại bước 1 và 2 (chỉ chấm câu có text mới) | ít |
| 4. Tách dataset cuối / bị loại, báo cáo | `report_dataset.py <STAMP>` | không |

- Bước 1 và 2 có `--dry-run` để đếm số câu, ước lượng trước khi chạy.
- `--xlsx` ghi đè phiếu. Phiếu điền sẵn các quyết định đã nhập, nên **nhập phiếu đang điền (bước 3) trước** khi chạy lại bước 2 với `--xlsx`.
- Cột `decision` của phiếu: `keep` (giữ nhãn gán) · `relabel` (đảo nhãn) · `fix_text` (điền `new_text`, kèm `new_label` nếu đổi nhãn) · `drop` · `boundary` (loại, đếm riêng để sửa subprompt).

**Vùng Jev** (so với nhãn gán): đỏ = Jev chấm khác nhãn gán (kể cả UNSURE) · vàng = cùng nhãn nhưng xác suất < 0.85 hoặc hai lần chấm không cùng nhãn · xanh = còn lại, được tin.

**Nhãn model ngoài:** model ghi mục khớp rõ (`matched`), khớp một phần (`partial`) và câu có thuộc chủ đề không (`on_topic`); code suy nhãn:

| Nhãn | Điều kiện | Gợi ý |
|---|---|---|
| VIOLATE / SAFE | khớp rõ VP (hay KV), không dính mục nào của danh sách kia | trùng nhãn gán → `keep`; ngược → `relabel` (đỏ) / `manual_check` (vàng, xanh) |
| WRONG_SUBJECT | không dính mục nào, lệch chủ đề | `wrong_subject` |
| UNCLEAR | còn lại | `unclear` |

Kết quả cũ (prompt r1–r3) có BOUNDARY, được đọc như UNCLEAR.

**Khi generator chạy có cổng lọc (mặc định):** bước 1 và phần đỏ + vàng của bước 2 đã chấm lúc sinh, nên ở đây chỉ còn chấm mẫu xanh. Câu có gợi ý `relabel`, `wrong_subject`, `unclear`, `fix_text` đã bị loại và sinh bù lúc sinh. Phiếu còn: câu đỏ mà model ngoài đồng ý nhãn gán (Jev sai, người xác nhận), câu vàng bị model ngoài phản đối, mẫu xanh bị phản đối, lỗi ERROR. Sheet `gate_dropped` liệt kê câu cổng đã loại để xem nhanh (không cần điền). Chi tiết cổng lọc: `generator/README.md` mục 7.

## Nguyên tắc

- **raw và merged giữ nguyên bản sinh.** Mọi bản sửa (sửa text, đổi nhãn, loại) nằm ở `check/work/decisions.jsonl` và được phủ lên khi đọc.
- **Kết quả chấm gắn mã băm text.** Text đổi thì kết quả cũ hết hiệu lực, câu đó tự được chấm lại ở lần chạy sau.
- **Thứ tự cứu mẫu:** sửa text cho khớp nhãn gán > đổi nhãn (khi cặp user/trợ lý vẫn hợp lý) > loại.
- **7 intent nhạy cảm** (cột `sensitive` = 1 trong phiếu) chỉ chủ dataset đọc và quyết định.
- **Câu có lỗi ERROR của bước 0** không vào dataset cuối cho tới khi được sửa hoặc người chọn `keep`.
