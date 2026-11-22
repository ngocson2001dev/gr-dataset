# review: quy tắc, danh sách cặp và file Excel review

Quy tắc tạo subprompt: [RULES.md](RULES.md) (đọc trước khi viết).

Subprompt nằm ở `../subprompts/`, mỗi intent một file `<intent_key>.md` (intent_key trong `../intent_taxonomy/taxonomy.json`), suy ra từ `../source_md` rồi kiểm 2 vòng (đối chiếu 1.02; cắt gọn cho LLM ngoài). Phần mục (header `##`) mà `generator/generate.py` đọc:

`Chủ đề` (trung lập, gộp cả mô tả; không có mục Định nghĩa) · `Vi phạm khi` · `Không vi phạm khi` · `Ca sát ranh giới` · `Lưu ý riêng` (phạm vi, routing sang chủ đề khác, điều kiện, phép thử; `Vi phạm khi` / `Không vi phạm khi` chỉ chứa định nghĩa tự đủ) · `Lưu ý mẫu vi phạm` · `Lưu ý mẫu an toàn` · `Mẫu vi phạm - mức khó` · `Mẫu an toàn - mức khó` · `Khía cạnh vi phạm` · `Khía cạnh an toàn` (dạng `- A1: mô tả`).

`../intent_taxonomy/pairs.json`: danh sách 41 cặp input ↔ output (chỉ cấu trúc; tier, danh mục, mức rủi ro, trạng thái nằm ở `taxonomy.json`), `generator/generate.py` đọc file này.

File Excel review sinh từ các subprompt bằng `python3 export_review.py` (thêm `--force` để ghi đè khi Excel hiện tại đã có quyết định chưa áp dụng).
