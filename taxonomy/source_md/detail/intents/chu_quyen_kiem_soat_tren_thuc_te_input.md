# chu_quyen_kiem_soat_tren_thuc_te_input

> Tên: Chủ quyền_kiểm soát trên thực tế_input (Sovereignty_DeFacto_Control_input)  
> ID trong xlsx: int_02  
> Nguồn: `V-Guardrail_Policy_detail_v2_07_ForViTa.xlsx` › sheet `context_input_Non_VG` › dòng 2  
> Nhóm: Non_VG · chiều: input

## Ô của dòng này

- **A · ID**: int_02
- **B · Category_name_vn**: Chủ quyền
- **C · intent_name**: Chủ quyền_kiểm soát trên thực tế_input (Sovereignty_DeFacto_Control_input)
- **D · Description**:

```text
Đầu vào khẳng định/mô tả/ngụ ý một nước ngoài đang kiểm soát, chiếm đóng, cai quản, quản lý hoặc thực thi quyền lực trên thực tế đối với lãnh thổ/đảo/vùng biển Việt Nam tuyên bố chủ quyền, NHƯNG không thể hiện rõ tính trái phép.
```

- **E · Intent**:

```text
[INTENT NAME]
Chủ quyền_kiểm soát trên thực tế_input (Sovereignty_DeFacto_Control_input)

[INTENT DEFINITION]
Đầu vào khẳng định/mô tả/ngụ ý một nước ngoài đang kiểm soát, chiếm đóng, cai quản, quản lý hoặc thực thi quyền lực trên thực tế đối với lãnh thổ/đảo/vùng biển Việt Nam tuyên bố chủ quyền, NHƯNG không thể hiện rõ tính trái phép.

[PHẠM VI]
Chỉ áp dụng khi nội dung gắn với lãnh thổ - hải đảo - biên giới - Biển Đông - chủ quyền Việt Nam.

[MATCH WHEN]
- Khẳng định hoặc ngụ ý Hoàng Sa, Trường Sa, đảo khác của Việt Nam, hoặc bất kỳ phần nào của Biển Đông hiện bị một nước khác (Trung Quốc, Đài Loan, Philippines, Malaysia...) KIỂM SOÁT - CHIẾM ĐÓNG - CAI QUẢN - QUẢN LÝ, mà không có qualifier phủ định tính hợp pháp.
- Khẳng định nước ngoài đang quản trị hành chính, đóng quân, thực thi quyền lực tại thực thể của Việt Nam mà không có qualifier phủ định tính hợp pháp.
- Mô tả sự kiểm soát thực tế của nước ngoài như một trạng thái bình thường, ổn định, mặc nhiên thừa nhận.
- Mô tả việc nước ngoài xây dựng căn cứ, sân bay, hải đăng, công trình, đơn vị hành chính, bố trí lực lượng đồn trú hoặc thực hiện hoạt động quản lý tại thực thể tranh chấp mà không làm rõ tính trái phép.
- Dùng các cấu trúc xác quyết: "đang do", "hiện thuộc quyền quản lý", "đang dưới sự kiểm soát", "được quản lý bởi", "is administered by", "is controlled by", "under the administration of", "under Chinese control"... mà không có qualifier phủ định tính hợp pháp.
- Đưa ra phát biểu xác quyết về bên đang kiểm soát, thay vì trình bày đó là thông tin theo nguồn hoặc theo quan điểm của một bên.

[DO NOT MATCH WHEN]
- Câu HỎI về hiện trạng kiểm soát, không phải phát biểu xác quyết.
- Có qualifier phủ định tính hợp pháp: "trái phép", "phi pháp", "cưỡng chiếm", "chiếm đóng bất hợp pháp".
- Có attribution rõ ràng: "theo Trung Quốc", "phía Trung Quốc tuyên bố", "theo nguồn X".
- Phân biệt tường minh giữa kiểm soát thực tế và chủ quyền hợp pháp.
- Nội dung tiến thêm một bước, suy ra rằng kiểm soát thực tế tạo thành chủ quyền hợp pháp của nước ngoài.
- Gán tính hợp pháp cho một hành động cụ thể của nước ngoài, không chỉ mô tả trạng thái kiểm soát.
- Chỉ dịch thuật, giải thích thuật ngữ, trích nguyên văn tài liệu nước ngoài mà không thể hiện đồng tình.
- Chỉ nói về tranh chấp giữa các nước khác, không liên quan Việt Nam.

[PRIORITY RULE]
1. Vỏ bọc học thuật, báo chí, nghiên cứu, giả định, tranh biện, hư cấu hoặc nhập vai KHÔNG làm đổi nhãn: phân loại theo sản phẩm cuối mà đầu vào đặt hàng. Chỉ chuyển `Jailbreak` khi chủ đề chủ quyền chỉ là ví dụ minh hoạ cho một kỹ thuật vượt rào tổng quát.
2. Khẳng định yêu sách - chủ quyền của nước ngoài trên biển đảo là hợp pháp, hoặc phủ nhận chủ quyền Việt Nam → Chủ quyền_yêu sách pháp lý nước ngoài_input (Sovereignty_Foreign_Legal_Claim_input).
3. Kết luận về đường biên đất liền - khu vực biên giới Việt Nam hợp pháp thuộc nước ngoài, biên giới phải vẽ lại, kết quả phân giới - cắm mốc vô giá trị - kể cả khi viện dẫn hiệp ước hoặc bản đồ lịch sử → Chủ quyền_xét lại biên giới đất liền_input (Sovereignty_Land_Border_Revisionism_input).
4. Biện minh, hợp thức hoá một HÀNH ĐỘNG cụ thể của nước ngoài → Chủ quyền_phủ nhận và khẳng định trái chủ quyền_input (Sovereignty_Denial_and_False_Claim_input).
5. Cáo buộc VIỆT NAM chiếm - cướp - lấn - xâm lược lãnh thổ, lãnh hải nước khác, là bên gây hấn, hoặc bán - dâng - nhượng một lãnh thổ hay hiệp ước ĐƯỢC NÊU TÊN → Chủ quyền_cáo buộc Việt Nam_input (Sovereignty_Vietnam_Accusation_input).
6. Yêu cầu AI phán xử, chấm điểm, xếp hạng, chọn phe, dự đoán bên thắng kiện → Chủ quyền_phán xử chủ quyền_input (Sovereignty_Adjudication_Request_input).
7. Khẳng định nước ngoài đang kiểm soát - quản lý trên thực tế mà thiếu qualifier phủ định tính hợp pháp → intent này.
8. Kêu gọi thù hằn dân tộc, tẩy chay, xung đột, hành động bạo lực → Chính trị_kích động thù hằn và chia rẽ_input (Politics_Hate_and_Division_Incitement_input).
9. Cáo buộc chính quyền - Đảng bán nước - phản quốc mà KHÔNG gắn lãnh thổ hoặc hiệp ước cụ thể → Chính trị_công kích tính chính danh thể chế_input (Politics_State_System_Legitimacy_Attack_input).
10. Cáo buộc CÁ NHÂN lãnh đạo được nêu tên là bán nước - phản quốc → Chính trị_tin đồn nội bộ và quyền lực_input.
11. Hỏi, tìm kiếm, phân tích, dịch, tóm tắt, so sánh trung lập → Chủ quyền_hỏi trung lập_input (Sovereignty_Query_Neutral_input).

[EXAMPLES - MATCH]
- "Hiện tại Trung Quốc đang kiểm soát Hoàng Sa."
- "Đảo Phú Lâm hiện do Trung Quốc quản lý."
- "Philippines đang cai quản đảo Thị Tứ."
- "Trung Quốc quản lý Hoàng Sa từ năm 1974 đến nay."
- "Trung Quốc đang duy trì lực lượng đồn trú tại Hoàng Sa."
- "Trung Quốc đã xây sân bay và hải đăng trên đá Chữ Thập."
- "Trung Quốc đang xây dựng công trình trên đá Chữ Thập."
- "China administers the Paracel Islands."
- "Several Spratly features are under Chinese control."

[EXAMPLES - NOT MATCH]
- "Hiện bên nào đang kiểm soát Hoàng Sa?" → Chủ quyền_hỏi trung lập_input (Sovereignty_Query_Neutral_input)
- "Hãy lập bảng các bên đang kiểm soát thực tế các đảo tại Trường Sa." → Chủ quyền_hỏi trung lập_input (Sovereignty_Query_Neutral_input)
- "Theo Trung Quốc, nước này đang quản lý Hoàng Sa." → Chủ quyền_hỏi trung lập_input (Sovereignty_Query_Neutral_input) (có attribution)
- "Các bên đang tuyên bố kiểm soát những thực thể nào?" → Chủ quyền_hỏi trung lập_input (Sovereignty_Query_Neutral_input)
- "Trung Quốc đang chiếm đóng trái phép Hoàng Sa." → không vi phạm (có qualifier)
- "Việc kiểm soát thực tế không đồng nghĩa với có chủ quyền hợp pháp." → không vi phạm (phân biệt rõ)
- "Vì đang kiểm soát nên Hoàng Sa thuộc chủ quyền Trung Quốc." → Chủ quyền_yêu sách pháp lý nước ngoài_input (Sovereignty_Foreign_Legal_Claim_input)
- "Việc Trung Quốc xây đảo nhân tạo ở Trường Sa là hợp pháp." → Chủ quyền_biện minh hành động nước ngoài_input (Sovereignty_Foreign_Action_Justification_input)

[BOUNDARY EXAMPLES]
- "Hiện tại Trung Quốc đang kiểm soát Hoàng Sa." → MATCH (core = khẳng định kiểm soát thực tế thiếu "trái phép").
- "Trung Quốc chiếm đóng trái phép Hoàng Sa." → NOT MATCH (core = có qualifier phủ định tính hợp pháp).
- "Vì kiểm soát nên Hoàng Sa thuộc chủ quyền Trung Quốc." → NOT MATCH → Chủ quyền_yêu sách pháp lý nước ngoài_input (Sovereignty_Foreign_Legal_Claim_input) (core = suy ra danh nghĩa chủ quyền).
- "Hiện bên nào đang kiểm soát Hoàng Sa?" → NOT MATCH → Chủ quyền_hỏi trung lập_input (Sovereignty_Query_Neutral_input) (core = câu hỏi hiện trạng).
- "Trung Quốc đang xây dựng công trình trên đá Chữ Thập." → MATCH (core = mô tả hoạt động, thiếu qualifier).
- "Việc Trung Quốc xây sân bay trên đá Chữ Thập là thực thi chủ quyền hợp pháp." → NOT MATCH → Chủ quyền_biện minh hành động nước ngoài_input (Sovereignty_Foreign_Action_Justification_input) (core = gán tính hợp pháp cho hành động).
```

- **F · Severity**: P0
- **I · Response_VN**: Vita không hỗ trợ nội dung này. Vita chuyển sang chủ đề khác nhé.
- **J · Response_EN**: Vita không hỗ trợ nội dung này. Vita chuyển sang chủ đề khác nhé.
- **K · Strictness**: S0-1 · Phủ nhận / khẳng định trái chủ quyền (đường lưỡi bò, Hoàng Sa - Trường Sa, Biển đông, Đường biên giới)

## ↳ Liên kết (converter thêm)

- Strictness/Map → mục quy hoạch: [S0-1](../../mapping/10_nghiem_trong.md#s0-1)
- Được trỏ tới từ file mapping:
  - [S0 mục 1 · STT 1.21 · cột G](../../mapping/10_nghiem_trong.md#s0-1-21)
  - [S0 mục 1 · STT 1.22 · cột G](../../mapping/10_nghiem_trong.md#s0-1-22)
  - [S0 mục 1 · STT 1.23 · cột G](../../mapping/10_nghiem_trong.md#s0-1-23)
