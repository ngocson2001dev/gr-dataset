# taxonomy v2.07 (ViTa)

Bản đồ các thư mục. Đọc theo thứ tự từ nguồn gốc đến sản phẩm cuối.

| Thư mục / file | Vai trò | Sửa được? |
|---|---|---|
| `V-Guardrail_Mapping_Quy hoạch 1.02 với Chính sách chi tiết.xlsx`, `V-Guardrail_Policy_detail_v2_07_ForViTa.xlsx` | Hai file Excel nguồn (1.02 là base, 2.07 là chi tiết) | Không (tài liệu gốc) |
| `V-Guardrail_Policy_detail_v2_08_AI Robot.xlsx` | Policy detail 2.08; chỉ lấy 2 intent mới (bí mật quốc phòng), bản Markdown nằm ở `intent_taxonomy/new_intents/` | Không (tài liệu gốc) |
| `source_md/` | Bản Markdown convert từ hai file Excel nguồn (`mapping/`, `detail/`) | **Chỉ đọc** |
| `intent_taxonomy/` | Taxonomy đã chốt: `taxonomy.json` (máy đọc), `TAXONOMY.md` (bản đọc cho người), `pairs.json` (cặp input ↔ output), `new_intents/` (intent mới: 4 dựng từ 1.02, 2 lấy từ Policy detail 2.08) | Có, theo quy trình duyệt |
| `subprompts/` | Subprompt viết tay, một file `<intent_key>.md` cho mỗi intent, dùng để sinh data | Có |
| `review/` | `RULES.md` (quy tắc viết subprompt), `export_review.py` (xuất Excel để review) | Có |

## Quy ước

- `intent_key` = tên tiếng Việt không dấu, nối bằng `_`, là khóa duy nhất của một intent (`taxonomy.json` → `intents`).
- **Nguồn duy nhất cho metadata** (tier, danh mục, mức rủi ro, trạng thái, id gốc `name_en`) là `taxonomy.json`. `pairs.json` chỉ chứa cấu trúc cặp (`pair`, `input`, `output`, `extra_output`); khi cần metadata của cặp, lấy qua intent input trong `taxonomy.json`. Không chép metadata sang `pairs.json`.
- 1.02 là base: xung đột với 2.07 thì 1.02 thắng.
- Mỗi intent một subprompt; hiện **82/82 file có sẵn**. Các cặp thiếu subprompt được generator tự bỏ qua và `export_review.py` đánh dấu "chưa có file".

## Dùng ở đâu

- `generator/generate.py` đọc `pairs.json`, `taxonomy.json` và `subprompts/` để dựng prompt sinh data (xem `../generator/README.md`).
- `review/export_review.py` xuất file Excel để người review đọc subprompt (xem `review/README.md`).
