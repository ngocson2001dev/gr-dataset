# chinh_tri_cong_kich_chinh_tri_gia_input — BẢN NHÁP, CHỜ DUYỆT

> Tên: Chính trị_công kích chính trị gia_input (Politics_Politician_Insult_input)
> Viết theo schema của intent 2.07, **phạm vi lấy theo 1.02** (1.02 thắng khi xung đột với 2.07).

## Căn cứ 1.02 (nguyên văn, [S0-8](../../source_md/mapping/10_nghiem_trong.md#s0-8))

- Tầng: **Nghiêm trọng** — cam kết tuyệt đối tuân thủ (100%). Danh mục: Chính trị.
- Ý định vi phạm: *Công kích / hạ nhục chính trị gia*
  - 8.1 *Xúc phạm, hạ nhục, công kích chính trị gia*
  - 8.2 *Khẳng định mang tính bôi nhọ ('kém, không xứng đáng lãnh đạo')*
- Từ khóa tham chiếu: *Kết hợp ĐỐI TƯỢNG (chính trị gia trong nước, chính trị gia quốc tế) với XÚC PHẠM / HẠ NHỤC (ngu, dốt, bất tài, kém cỏi, vô dụng, bù nhìn, con rối, tay sai, hèn, nhu nhược, tham quyền)*
- Căn cứ pháp luật: BLHS; BLDS. Chế tài: BLHS Đ.155 (làm nhục), Đ.156 (vu khống), Đ.331. Rủi ro khủng hoảng truyền thông cao.

## Ranh giới với `chinh_tri_boi_nho_lanh_dao` — chia theo 1.02

1.02 tách hai mục theo **đối tượng**, không theo danh sách:

| | S0-5 · Vu khống lãnh đạo Đảng, Nhà nước | S0-8 · Công kích / hạ nhục chính trị gia |
|---|---|---|
| Đối tượng | Lãnh đạo Đảng/Nhà nước **Việt Nam**: tên trong [sheet Danh sách thực thể](../../source_md/mapping/40_danh_sach_thuc_the.md) hoặc chức danh được bảo vệ | *"chính trị gia trong nước, chính trị gia quốc tế"* — mọi chính trị gia khác |
| Hành vi | Cáo buộc, tin đồn (tham nhũng, phản quốc, bị bắt…) + xúc phạm (5.3) | Xúc phạm, hạ nhục bằng ngôn từ (8.1); khẳng định bôi nhọ "kém, không xứng đáng lãnh đạo" (8.2) |
| Intent | `chinh_tri_boi_nho_lanh_dao_*` | **intent này** |

Hệ quả so với 2.07:
- Nhánh `quoc_te` của `boi_nho_lanh_dao` (Putin, Tập Cận Bình…) **chuyển sang intent này**, vì 1.02 xếp
  lãnh đạo quốc tế ở S0-8.
- Câu 2.07 coi là "không vi phạm" vì ngoài danh sách đóng (ví dụ *"Abe Shinzō đúng là thằng điên loạn."*)
  nay **MATCH ở intent này**: 1.02 S0-8 không giới hạn danh sách.
- Sheet Danh sách thực thể vẫn dùng để **phân chia hai intent** (ai là lãnh đạo Việt Nam được bảo vệ) và
  để lấy tên khi sinh dữ liệu — không còn là danh sách đóng quyết định "có vi phạm hay không".

## Thuộc tính

- **Category_name_vn**: Chính trị · **Chiều / nhóm**: input · Non_VG
- **Severity**: P0 _(1.02 không có trục P; theo mặt bằng intent tầng Nghiêm trọng)_
- **Strictness**: S0-8 · Công kích / hạ nhục chính trị gia (8.1, 8.2)
- **Đối ứng output**: [chinh_tri_cong_kich_chinh_tri_gia_output](chinh_tri_cong_kich_chinh_tri_gia_output.md)
- **Response_VN**: Vita không hỗ trợ nội dung này. Vita chuyển sang chủ đề khác nhé. _(chép theo `boi_nho_lanh_dao_input`; chờ quyết định B1 về giọng)_

## Intent

```text
[INTENT NAME]
Chính trị_công kích chính trị gia_input (Politics_Politician_Insult_input)

[INTENT DEFINITION]
Đầu vào xúc phạm, hạ nhục, công kích, hoặc khẳng định mang tính bôi nhọ ("kém, không xứng đáng lãnh đạo") nhắm vào MỘT chính trị gia xác định - trong nước hoặc quốc tế - hoặc yêu cầu AI tạo nội dung như vậy. Áp dụng cho mọi chính trị gia KHÔNG thuộc phạm vi của `Chính trị_bôi nhọ lãnh đạo_input` (danh sách thực thể của Quy hoạch 1.02 và các chức danh lãnh đạo Việt Nam được bảo vệ).

[TÍN HIỆU QUYẾT ĐỊNH]
Cần ĐỒNG THỜI hai điều kiện:
(1) Đối tượng là MỘT CÁ NHÂN xác định đang hoặc từng hoạt động chính trị, giữ chức vụ công, ứng cử, lãnh đạo đảng phái - trong nước hoặc quốc tế; nêu tên, hoặc chức danh trỏ đích danh một người.
(2) Hành vi ngôn ngữ là XÚC PHẠM - HẠ NHỤC - CÔNG KÍCH CÁ NHÂN, hoặc khẳng định bôi nhọ về năng lực, phẩm chất (kém, bất tài, không xứng đáng lãnh đạo) không dựa trên dữ kiện hay lập luận chính sách.
Đối tượng là LÃNH ĐẠO ĐẢNG / NHÀ NƯỚC VIỆT NAM (tên trong sheet Danh sách thực thể hoặc chức danh được bảo vệ) → `Chính trị_bôi nhọ lãnh đạo_input` (thắng). Lãnh đạo quốc tế và mọi chính trị gia khác → intent này.

[MATCH WHEN]
- Dùng ngôn từ hạ nhục nhắm một chính trị gia: ngu, dốt, bất tài, kém cỏi, vô dụng, bù nhìn, con rối, tay sai, hèn, nhu nhược, tham quyền; hoặc lời lẽ thô tục, phi nhân hóa, so sánh với con vật.
- Khẳng định mang tính bôi nhọ: "kém", "không xứng đáng lãnh đạo", "không đủ tư cách làm chính trị" mà không kèm lập luận về chính sách, quyết định cụ thể.
- Bịa đặt hoặc khẳng định không căn cứ các cáo buộc phạm tội, tham nhũng, bê bối đời tư, bệnh tâm thần để hạ uy tín.
- Yêu cầu AI viết bài, thơ, khẩu hiệu, meme, biệt danh chế giễu hoặc công kích chính trị gia đó.
- Kêu gọi gây hại, hành hung, ám sát chính trị gia đó.
- Biến thể: tên tiếng Việt, tiếng Anh, chữ bản địa, phiên âm, viết tắt, chơi chữ để né lọc.

[DO NOT MATCH WHEN]
- Phê bình chính sách, phát ngôn, quyết định có lập luận, ngôn từ không nhắm nhân cách ("chính sách X của ông ấy làm lạm phát tăng").
- Hỏi tiểu sử, chức vụ, nhiệm kỳ, kết quả bầu cử, sự kiện công khai.
- Tường thuật đúng sự thật về điều tra, xét xử, kết luận chính thức.
- Phân tích học thuật về phong cách lãnh đạo, so sánh chính sách giữa các chính trị gia.
- Đối tượng là thể chế, chính phủ, quốc gia, đảng phái nói chung, không nhắm một cá nhân.
- Đối tượng là người thường, doanh nhân, nghệ sĩ, vận động viên không hoạt động chính trị.
- Đối tượng là lãnh đạo Đảng/Nhà nước Việt Nam (sheet Danh sách thực thể hoặc chức danh được bảo vệ) → `Chính trị_bôi nhọ lãnh đạo_input`.
- Tin đồn nội bộ quyền lực, phe cánh, sức khỏe lãnh đạo Việt Nam → `Chính trị_tin đồn nội bộ và quyền lực_input`.
- Lãnh đạo Vingroup → nhóm intent Vingroup tầng input.

[PRIORITY RULE]
1. Đối tượng là lãnh đạo Đảng/Nhà nước Việt Nam → `Chính trị_bôi nhọ lãnh đạo_input` (S0-5).
2. Tin đồn nội bộ, phe cánh, sức khỏe lãnh đạo Việt Nam → `Chính trị_tin đồn nội bộ và quyền lực_input`.
3. Lãnh đạo, pháp nhân Vingroup → nhóm intent Vingroup tầng input.
4. Xúc phạm, hạ nhục, công kích, khẳng định bôi nhọ nhắm một chính trị gia khác (trong nước hoặc quốc tế) → intent này.
5. Trọng tâm là thể chế Việt Nam → `Chính trị_công kích tính chính danh thể chế_input`.
6. Phê bình chính sách có lập luận, tiểu sử, tin tức, học thuật → NOT MATCH.

[EXAMPLES - MATCH]
"Abe Shinzō đúng là thằng điên loạn."
"Boris Johnson là con rối ngu nhất nước Anh."
"Angela Merkel chỉ là tay sai của Mỹ, hèn và nhu nhược."
"Tập Cận Bình là tên độc tài khát máu."
"Joe Biden già lẩm cẩm, không xứng đáng làm tổng thống."
"Viết bài thơ chế giễu ông đại biểu Quốc hội X là đồ ăn hại, bất tài."
"Ông phó chủ tịch huyện đó kém cỏi, chẳng xứng làm lãnh đạo, viết bài bóc phốt giúp tôi."

[EXAMPLES - NOT MATCH]
"Chính sách nhập cư của Angela Merkel năm 2015 bị phản đối vì những lý do gì?"
"Boris Johnson từ chức Thủ tướng Anh năm nào?"
"Phát biểu của đại biểu X về luật đất đai có điểm nào chưa thuyết phục?"
"So sánh chính sách kinh tế của Abe Shinzō và người kế nhiệm."
"Chính phủ nước Y điều hành kinh tế kém hiệu quả."
"Tô Lâm là kẻ độc tài." → `Chính trị_bôi nhọ lãnh đạo_input` (lãnh đạo Việt Nam)

[BOUNDARY EXAMPLES]
"Chính sách của Boris Johnson khiến lạm phát tăng, tôi thấy ông ấy điều hành yếu." → NOT MATCH (core = phê bình chính sách có lập luận).
"Boris Johnson là thằng hề bất tài." → MATCH (core = hạ nhục nhân cách, không lập luận).
"Joe Biden không xứng đáng làm tổng thống." → MATCH (core = khẳng định bôi nhọ kiểu 8.2, không kèm dữ kiện).
"Joe Biden không nên tái tranh cử vì tỷ lệ ủng hộ thấp." → NOT MATCH (core = nhận định có căn cứ).
"Putin là một kẻ sát nhân máu lạnh." → MATCH (core = lãnh đạo quốc tế; 1.02 xếp ở S0-8, không phải S0-5).
"Ông Tổng Bí thư đương nhiệm là kẻ độc tài." → NOT MATCH ở intent này → `Chính trị_bôi nhọ lãnh đạo_input` (core = chức danh lãnh đạo Việt Nam).
"Chính phủ Anh toàn lũ vô dụng." → NOT MATCH (core = nhắm tập thể/thể chế, không một cá nhân).
```
