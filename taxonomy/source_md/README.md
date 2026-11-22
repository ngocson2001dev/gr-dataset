# source_md — bản Markdown của 2 file xlsx nguồn v2.07

Convert một lần từ 2 file xlsx (2026-10-04); script convert không được giữ lại. Thư mục
này **chỉ đọc**: không sửa, không thêm file làm việc vào đây — ghi chú/quyết định nằm ở
`../review/`, sub-prompt ở `../subprompts/`. Chỉ đổi định dạng; mọi ô không rỗng của xlsx
có mặt nguyên văn ở đây (đã kiểm round-trip lúc convert: 2486/2486 ô).

## Nguồn
- `V-Guardrail_Mapping_Quy hoạch 1.02 với Chính sách chi tiết.xlsx` → `mapping/`
- `V-Guardrail_Policy_detail_v2_07_ForViTa.xlsx` → `detail/`

## Cấu trúc
```
mapping/
  00_tieu_chi_chap_nhan.md   tiêu chí chấp nhận 3 mức rủi ro
  10_nghiem_trong.md         tầng S0 — mục 1..15, STT chi tiết 1.1..
  20_cao.md                  tầng S1
  30_trung_binh.md           tầng S2
  40_danh_sach_thuc_the.md   danh sách đối tượng được bảo vệ
  50_han_che.md              danh mục hạn chế (y tế, pháp lý, đầu tư)
  60_tham_chieu.md           căn cứ pháp luật
detail/
  INDEX.md                   bảng mọi intent: ID, tên, Severity, Strictness, link
  intents/<intent_key>.md    một file một dòng intent (toàn bộ ô của dòng đó)
  keyword_toxic.md, keyword_general.md, summary_intent.md
```

## Quy ước
- `- **F · Mô tả**: …` — ô cột F, sau dấu `·` là tiêu đề cột. Ô ngắn 1 dòng ghi inline;
  ô dài/nhiều dòng nằm trong khối ```text … ``` (nguyên văn, kể cả khoảng trắng).
- `_ô gộp A4:A26 — áp cho STT 1.1–1.23_` — ô gộp; nội dung in MỘT lần ở cấp cao nhất nó phủ.
- `⟦đỏ⟧…⟦/đỏ⟧` — đoạn chữ đỏ bên trong ô (rich text). Marker không có trong xlsx.
- `_công thức; giá trị đã tính: …_` — ô công thức (chỉ sheet summary intent). Ô của cột
  Intent Output KHÔNG có dòng này là ô gõ tay đè lên công thức.
- Đã lược bỏ (không mang nội dung): màu nền/màu chữ của ô, ô chỉ chứa khoảng trắng,
  định dạng chữ, độ rộng cột, dropdown của cột "Trạng thái rà soát".
- `↳` — liên kết DO CONVERTER THÊM, không phải nội dung gốc:
  - mapping cột G/H → file intent (khớp theo ID + chiều + nhóm VG/Non_VG/JB);
    `⚠️ tên … khác` khi tên intent trong ô mapping không khớp tên ở file chi tiết;
  - file intent → mục quy hoạch theo mã Strictness/Map (`S0-11` → `10_nghiem_trong.md#s0-11`),
    và danh sách các dòng mapping trỏ ngược tới intent;
  - summary intent: công thức `=sheet!C2` → file intent của dòng đó.
- Anchor: `#s0-11` (mục 11 tầng S0), `#s0-11-2` (STT chi tiết 11.2).

## Khóa intent
- `intent_key` = tên tiếng Việt ở cột `intent_name` (phần trước ngoặc), bỏ dấu, chữ thường,
  nối `_`: "Chủ quyền_kiểm soát trên thực tế_input (…)" -> `chu_quyen_kiem_soat_tren_thuc_te_input`.
  Đã kiểm lúc convert: 77/77 khóa duy nhất. Đây là định danh dùng ở mọi nơi trong v2.07.
- KHÔNG dùng `int_XX` làm định danh: không duy nhất (`int_48`, `int_49` có ở cả input VG và
  input Non_VG; nhiều số trùng giữa input và output; 2 dòng không có ID). `int_XX` chỉ còn
  xuất hiện vì là nội dung gốc của ô (vd cột G/H của mapping).
