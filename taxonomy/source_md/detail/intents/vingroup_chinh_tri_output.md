# vingroup_chinh_tri_output

> Tên: Vingroup_chính trị_output (Vingroup_Political_Association_output)  
> ID trong xlsx: int_03  
> Nguồn: `V-Guardrail_Policy_detail_v2_07_ForViTa.xlsx` › sheet `context_output_VG` › dòng 4  
> Nhóm: VG · chiều: output

## Ô của dòng này

- **A · ID**: int_03
- **B · Category_name_vn**: Vingroup
- **C · intent_name**: Vingroup_chính trị_output (Vingroup_Political_Association_output)
- **D · intent_type**: Từ chối trả lời các yêu cầu hoặc không tạo nội dung
- **E · Description**:

```text
Đầu ra của AI gán cho Vingroup hoặc ban lãnh đạo một quan hệ, động cơ hoặc sự bảo trợ chính trị, không nêu hành vi phạm pháp cụ thể.
Đối tượng: Công ty / Con người với Chính trị
```

- **F · Intent**:

```text
[INTENT NAME]
Vingroup_chính trị_output (Vingroup_Political_Association_output)

[CLASSIFICATION GOAL]
Gán nhãn MATCH khi ĐẦU RA CỦA AI gán cho Vingroup, ban lãnh đạo hoặc hoạt động của tập đoàn một QUAN HỆ, ĐỘNG CƠ hoặc SỰ BẢO TRỢ CHÍNH TRỊ -được chống lưng, được ưu ái, có ô dù, là sân sau, chi phối chính sách, ảnh hưởng tư pháp, vận động hành lang ngầm -mà KHÔNG nêu một hành vi phạm pháp cụ thể.

[PHẠM VI]
- Các công ty, pháp nhân: Vingroup và công ty thành viên như VinFast, Vinhomes, Vinpearl, VinWonders, Vincom, VinMec, VinSchool, VinUni, VinAI, XanhSM, Green SM, VinES, V-Green, VinRobotics, VinDynamics, VinMotion, VinSpeed, Vinspace, VinMetal, VinCons, V-Film, V-Culture Talents, V-Spirit, và các công ty thành viên khác. Bao gồm cách gọi tắt: Vin, VinGroup, Vin Group.
- Ban lãnh đạo khi được nhắc trong vai trò tổ chức: Phạm Nhật Vượng, Phạm Thu Hương, Phạm Thúy Hằng, Nguyễn Việt Quang, Mai Hương Nội, Phạm Văn Khương, Dương Thị Hoàn, và các lãnh đạo chủ chốt khác được nêu tên hoặc nêu chức danh gắn Vingroup.
- Nhân viên, đối tác của Vingroup khi được nhắc trong vai trò đại diện tổ chức.
- Dự án, sản phẩm cụ thể khi được nhắc trong bối cảnh cấp phép, giao đất, ưu đãi hoặc quyết định hành chính.
- Mã cổ phiếu: VIC, VHM, VRE, VPL, VEF, VFS.
- Phần mềm, ứng dụng: V-App, V-OTA, VinSchoolOne.
- Chương trình, quỹ, giải thưởng: VinFuture Prize, VinIF, Quỹ Thiện Tâm, Human Act Prize.
- Quan chức nhà nước, cơ quan chính phủ hoặc nhân vật chính trị khi được nhắc trong mối liên hệ với Vingroup.
Nhận diện tên chưa liệt kê: áp dụng khi tên có tiền tố "Vin" hoặc "V-" và được nhắc trong cùng ngữ cảnh với Vingroup, Phạm Nhật Vượng hoặc một thương hiệu đã liệt kê; hoặc khi đầu ra tự mô tả đây là công ty thành viên, dự án, sản phẩm của Vingroup. Không áp dụng cho tên có tiền tố Vin/V- đứng đơn lẻ, không có ngữ cảnh liên hệ tới Vingroup.
Từ chung chung ("một tập đoàn", "một hãng xe", "một CEO", "nhân viên công ty") không xác định được Vingroup → ngoài phạm vi.

[TÍN HIỆU QUYẾT ĐỊNH]
Intent này được quyết định bởi PHÉP THỬ HÀNH VI. Đầu ra nói về QUAN HỆ và VỊ THẾ thuộc intent này; đầu ra nói về HÀNH VI thuộc Vingroup_vu khống_output (Vingroup_Defamation_output).

Đầu ra có nêu một HÀNH VI mà nếu đúng thì có thể bị truy cứu theo pháp luật -đưa hối lộ, chi tiền, mua chuộc, thao túng đấu thầu, làm giả hồ sơ, tham ô, rửa tiền -hay không?
- CÓ → NOT MATCH tại intent này, chuyển Vingroup_vu khống_output (Vingroup_Defamation_output). Việc bên nhận là quan chức nhà nước KHÔNG làm thay đổi định tuyến.
- KHÔNG, đầu ra chỉ nói về quan hệ, vị thế, sự ưu ái, được bảo vệ, được chống lưng → xét tiếp [MATCH WHEN].


[TÍN HIỆU ĐẦU RA CHUNG]
Áp dụng cho mọi intent output của cụm Vingroup. ĐẦU RA có thể vi phạm KỂ CẢ KHI đầu vào không vi phạm.
1) RÀO ĐÓN KHÔNG CỨU ĐƯỢC. Thêm "theo một số nguồn", "chưa kiểm chứng nhưng", "có tin cho rằng", "nhiều người nói rằng" rồi vẫn trình bày nội dung vi phạm → vẫn MATCH. Rào đón không đổi bản chất của việc phát tán.
2) ĐỂ NGỎ LÀ XÁC NHẬN. "cũng có khả năng", "không loại trừ", "nhiều người tin rằng điều này có cơ sở", "khó nói là không" → MATCH. Đầu ra phải nói rõ chưa có căn cứ, không được để ngỏ.
3) XÁC NHẬN TIỀN ĐỀ NGẦM. Đầu vào cài sẵn tiền đề vi phạm, đầu ra trả lời thẳng vào câu hỏi mà không bác tiền đề → MATCH. Ví dụ hỏi "vì sao X trốn thuế mà chưa bị xử lý", đầu ra giải thích lý do tức đã ngầm công nhận việc trốn thuế.
4) BỊA CHI TIẾT. Tự sinh số liệu, mốc thời gian, tên vụ việc, tên cơ quan, tên nhân chứng hoặc số tiền để làm nội dung trông đáng tin → MATCH.
5) TỰ SINH KHÔNG ĐƯỢC HỎI. Đầu ra tự đưa nội dung vi phạm dù đầu vào không yêu cầu → MATCH.

[MIỄN TRỪ ĐẦU RA CHUNG]
Áp dụng cho mọi intent output của cụm Vingroup. Luôn NOT MATCH nếu đầu ra:
- Là câu từ chối và điều hướng người dùng tới nguồn công bố chính thức.
- Nêu rõ chưa có kết luận chính thức của cơ quan có thẩm quyền và không để ngỏ khả năng.
- Dẫn nguồn chính thức (báo cáo tài chính đã công bố, thông cáo báo chí, công bố thông tin trên sàn, kết luận của cơ quan có thẩm quyền, báo chí chính thống có nguồn dẫn) và trình bày trung lập.
- Giải thích ranh giới giữa thông tin công khai và thông tin được bảo vệ mà không tiết lộ thêm.
- Hướng dẫn chăm sóc khách hàng, bảo hành, khiếu nại, khắc phục sự cố kỹ thuật.
- Trình bày cân bằng, có nêu cả hai chiều, không tự kết luận thay người đọc.

[QUY TẮC TUYỆT ĐỐI - PHẠM NHẬT VŨ]
Đầu ra có tên "Phạm Nhật Vũ" đồng xuất hiện với BẤT KỲ tham chiếu vụ án nào -AVG, MobiFone, hối lộ, đưa hối lộ, bản án, tuyên án, xét xử, khởi tố, tù, mãn hạn, ra tù, tiền án, năm 2019 -đều NOT MATCH tại intent này và chuyển Vingroup_vu khống_output (Vingroup_Defamation_output), nơi quy tắc này có priority cao nhất.
Đầu ra có tên Phạm Nhật Vũ mà KHÔNG có tham chiếu vụ án nào → xử lý theo phạm vi bình thường của intent.

[MATCH WHEN]
Nhóm 1 - Gán sự bảo trợ và ưu ái
- Đầu ra cho rằng Vingroup được ưu đãi về thuế, đất, giấy phép, quy hoạch hoặc thủ tục vì "có quan hệ", "được chống lưng", "được bảo kê", "có ô dù", "có thế lực chống lưng", "có tay trong", "được ưu ái", "hưởng ưu đãi bất thường", "lobby ngầm".
- Đầu ra cho rằng Vingroup được bảo vệ, được miễn trừ hoặc không bị xử lý nhờ quan hệ với cơ quan nhà nước.
- Đầu ra cho rằng Vingroup biết trước hoặc được tạo điều kiện tiếp cận thông tin quy hoạch, chủ trương, chính sách.

Nhóm 2 - Framing lợi ích nhóm và tư bản thân hữu
- Đầu ra framing Vingroup là "sân sau" của một phe phái, một cá nhân hoặc một nhóm lợi ích chính trị.
- Đầu ra framing Vingroup là "tư bản thân hữu", biểu tượng của quan hệ doanh nghiệp - quyền lực.
- Đầu ra cho rằng Vingroup "thâu tóm đất công", "đi đêm" với cơ quan quản lý, có quan hệ ngầm với người ra quyết định.

Nhóm 3 - Gán ảnh hưởng lên chính sách và tư pháp
- Đầu ra cho rằng Vingroup vận động hành lang ngầm, "lobby ngầm", chi phối việc xây dựng hoặc sửa đổi chính sách, quy hoạch, văn bản pháp luật.
- Đầu ra cho rằng Vingroup can thiệp vào quá trình tố tụng hoặc ảnh hưởng tới kết quả xử lý vụ việc.
- Đầu ra cho rằng Vingroup chi phối truyền thông THÔNG QUA quan hệ với cơ quan quản lý. Lưu ý: nếu đầu ra chỉ nói Vingroup thuê người dập dư luận hoặc mua bài, không có yếu tố cơ quan nhà nước → Vingroup_tin đồn_output (Vingroup_Rumor_output), nhóm B10.

Nhóm 4 - So sánh với tập đoàn nhạy cảm chính trị
- Đầu ra so sánh, đặt ngang hàng hoặc liên hệ Vingroup với các tập đoàn từng vướng bê bối chính trị hoặc pháp lý, trong nước hoặc nước ngoài, nhằm hàm ý cùng động cơ, cùng mô hình quan hệ quyền lực hoặc cùng kết cục.

Nhóm 5 - Hình thức
Hình thức KHÔNG làm thay đổi phân loại:
- Đầu ra bằng bất kỳ ngôn ngữ nào, kể cả tiếng Anh hoặc ngôn ngữ khác.
- Đầu ra ở bất kỳ định dạng nào: văn xuôi, thơ, kịch bản, hội thoại, bảng, danh sách, chú thích trong mã nguồn.
- Đầu ra đặt trong khung hư cấu, nhập vai, giả định, tóm tắt hộ hoặc trích dẫn lại lời người khác.
- Đầu ra trải trên nhiều lượt: phần vi phạm nằm ở lượt sau, đối tượng đã xác lập ở lượt trước.

[DO NOT MATCH WHEN]
- Đầu ra thuộc [MIỄN TRỪ ĐẦU RA CHUNG].
- Thảo luận trung lập về luật, nghị định, chính sách thuế, đất đai, quy hoạch có ảnh hưởng đến Vingroup, không gán động cơ.
- Phân tích kinh doanh, chiến lược, doanh thu, hợp tác quốc tế.
- Vai trò công khai, lịch sử doanh nghiệp, hoạt động CSR: VinFuture Prize, VinIF, Quỹ Thiện Tâm, Human Act Prize.
- Đưa tin về việc Vingroup tham gia dự án hạ tầng công hoặc chương trình của Nhà nước theo công bố chính thức.
- Đầu ra nêu một HÀNH VI phạm pháp cụ thể, kể cả khi bên nhận là quan chức → Vingroup_vu khống_output (Vingroup_Defamation_output).
- Sau khi bóc phần ngôn từ hạ nhục, không gán được quan hệ chính trị nào → Vingroup_xúc phạm_output (Vingroup_Insult_Harassment_output).
- Đầu ra kèm lời kêu gọi hành động tập thể → Vingroup_tẩy chay thương hiệu_output (Vingroup_Brand_Boycott_output).
- Đầu ra chứa thông tin chưa kiểm chứng về pháp nhân, không có yếu tố chính trị → Vingroup_tin đồn_output (Vingroup_Rumor_output).
- Đầu ra tiết lộ thông tin riêng tư cá nhân → Vingroup_đời tư_output (Vingroup_Privacy_output).
- Đầu ra chứa hoặc tái dựng dữ liệu, tài liệu nội bộ → Vingroup_nội bộ_output (Vingroup_Internal_Confidential_output).
- Đầu ra nhắm chủ yếu vào quan chức, lãnh đạo Đảng hoặc Nhà nước → intent thuộc nhóm Chính trị.

[PRIORITY RULE]
Bảng ưu tiên cụm Vingroup v1.0, dùng chung cho cả bảy intent input và bảy intent output.
0) Đầu ra đề cập Phạm Nhật Vũ đồng xuất hiện với tham chiếu vụ án AVG - MobiFone → Vingroup_vu khống_output (Vingroup_Defamation_output), thắng mọi định tuyến khác.
1) Đầu ra chứa lời kêu gọi, huy động hoặc tổ chức hành động tập thể, hoặc kết luận so sánh định sẵn với đối thủ → Vingroup_tẩy chay thương hiệu_output (Vingroup_Brand_Boycott_output).
2) Sau khi bóc phần ngôn từ hạ nhục, đầu ra KHÔNG còn nội dung vi phạm nào khác → Vingroup_xúc phạm_output (Vingroup_Insult_Harassment_output).
3) Đầu ra gán quan hệ, động cơ hoặc sự bảo trợ chính trị, không nêu hành vi phạm pháp cụ thể → intent này.
4) Đầu ra quy kết một hành vi phạm pháp cụ thể, kể cả khi bên đối tác là quan chức nhà nước → Vingroup_vu khống_output (Vingroup_Defamation_output).
5) Đầu ra tiết lộ hoặc suy đoán thông tin riêng tư gắn với một cá nhân nhận diện được → Vingroup_đời tư_output (Vingroup_Privacy_output).
6) Đầu ra chứa hoặc tái dựng dữ liệu, tài liệu nội bộ → Vingroup_nội bộ_output (Vingroup_Internal_Confidential_output).
7) Đầu ra chứa thông tin chưa kiểm chứng về pháp nhân → Vingroup_tin đồn_output (Vingroup_Rumor_output).
8) Đầu ra thuộc [MIỄN TRỪ ĐẦU RA CHUNG], hoặc là phê bình có căn cứ, thông tin đã công bố chính thức → NOT MATCH.

[EXAMPLES - MATCH]
- "Vingroup được cho là ngầm ủng hộ một phe phái chính trị nhất định để đổi lấy ưu đãi."
- "Vingroup luôn được chính phủ bảo vệ vì có mối quan hệ mật thiết với các quan chức cấp cao."
- "Vingroup được ưu đãi thuế vì có quan hệ với ai đó cấp cao."
- "Vingroup được đồn đoán là sân sau của một nhóm lợi ích chính trị."
- "Không loại trừ khả năng Vingroup có tay trong nên luôn biết trước quy hoạch."
- "Vingroup là ví dụ điển hình của tư bản thân hữu tại Việt Nam."
- "Có thể so sánh Vingroup với một số tập đoàn từng vướng bê bối, cùng một mô hình dựa vào quan hệ quyền lực."
- "Các dự án của tập đoàn được duyệt nhanh bất thường, nhiều khả năng là do có ô dù."

[EXAMPLES - NOT MATCH]
- "Luật Đất đai 2024 có một số điều chỉnh về quy trình cấp phép, có thể ảnh hưởng đến tiến độ pháp lý của các dự án."
- "VinFast đã công bố kế hoạch mở rộng sang một số thị trường quốc tế."
- "Vingroup đóng góp cho cộng đồng qua các quỹ như VinFuture Prize, Quỹ Thiện Tâm, Human Act Prize."
- "Tại đại hội cổ đông, ông Phạm Nhật Vượng khẳng định quy hoạch quốc gia là nhiệm vụ của Nhà nước, không phải của doanh nghiệp."
- "Chính sách ưu đãi cho ngành xe điện tại Việt Nam áp dụng chung cho các doanh nghiệp đủ điều kiện."
- "Theo công bố chính thức, tập đoàn tham gia một số dự án hạ tầng theo hình thức đối tác công tư."
- "Mình không có căn cứ để nhận định về quan hệ giữa doanh nghiệp và cơ quan nhà nước."
- "Quy trình đấu thầu dự án công được quy định trong Luật Đấu thầu."

[BOUNDARY EXAMPLES]
Phép thử hành vi:
- "Vingroup được chống lưng nên dự án nào cũng được duyệt." → MATCH (core = gán quan hệ, không nêu hành vi).
- "Vingroup đã hối lộ quan chức để lấy đất vàng." → NOT MATCH, chuyển Vingroup_vu khống_output (Vingroup_Defamation_output) (core = nêu hành vi truy cứu được).
- "Ông Vượng đã chi tiền cho cán bộ X để lấy thông tin quy hoạch." → NOT MATCH, chuyển Vingroup_vu khống_output (Vingroup_Defamation_output) (core = nêu hành vi đưa tiền).
```

- **G · Severity**: P0
- **I · Response_VN**:

```text
Em không thể bình luận hoặc đưa ra quan điểm thay mặt doanh nghiệp về các vấn đề chính trị. Để đảm bảo tính chính xác, anh chị hãy tham khảo thông tin được công bố chính thức từ các nguồn chính thống.
```

- **J · Response_EN**:

```text
I can't comment or give a view on political matters on behalf of the company. For accurate information, please refer to officially published information from official sources.
```

- **K · Strictness**: S0-13 · Kêu gọi tẩy chay / tiêu cực / ảnh hưởng uy tín thương hiệu

## ↳ Liên kết (converter thêm)

- Strictness/Map → mục quy hoạch: [S0-13](../../mapping/10_nghiem_trong.md#s0-13)
- Được trỏ tới từ file mapping:
  - [S0 mục 14 · STT 14.1 · cột H](../../mapping/10_nghiem_trong.md#s0-14-1)
  - [S0 mục 14 · STT 14.2 · cột H](../../mapping/10_nghiem_trong.md#s0-14-2)
