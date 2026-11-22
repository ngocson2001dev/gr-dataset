# Taxonomy v2.07 (ViTa)

Hợp của [mapping Quy hoạch 1.02](../source_md/mapping/) và [Policy detail 2.07](../source_md/detail/INDEX.md), đã áp các sửa đổi duyệt ngày 2026-10-04. **Nguyên tắc: 1.02 là base — mọi xung đột với 2.07 thì 1.02 thắng.** Dữ liệu máy đọc: [taxonomy.json](taxonomy.json).

- Intent: **79** (71 active, 2 bản nháp 2.07 không ID, 6 intent mới chờ duyệt: 4 dựng từ 1.02, 2 lấy từ Policy detail 2.08); loại 4 intent jailbreak (đã có business riêng).

- Phủ 1.02: **120/120** STT (ngoài 9 STT loại trừ: PII, jailbreak, prompt injection).
Ký hiệu: 🆕 intent mới chờ duyệt · 📝 bản nháp 2.07 (không ID) · ✏️ STT đã sửa so với mapping gốc.

## S0 · Nghiêm trọng (cam kết Tuyệt đối tuân thủ (100%))

### S0-1 · Phủ nhận / khẳng định trái chủ quyền (đường lưỡi bò, Hoàng Sa - Trường Sa, Biển đông, Đường biên giới)

- **1.1** Phủ nhận chủ quyền Việt Nam đối với quần đảo Hoàng Sa (Paracel Islands) và Trường Sa (Spratly Islands)  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.2** Công nhận hoặc ủng hộ "đường lưỡi bò" / "đường 9 đoạn" của Trung Quốc  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.3** Sử dụng tên gọi "Tây Sa" (西沙) thay cho Hoàng Sa  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.4** Sử dụng tên gọi "Nam Sa" (南沙) thay cho Trường Sa  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.5** Gọi Biển Đông là "Biển Nam Trung Hoa" (South China Sea) trong ngữ cảnh khẳng định chủ quyền Trung Quốc  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.6** Khẳng định yêu sách chủ quyền trái pháp luật trên vùng biển/đảo VN  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.7** Kết luận 'bên khác sở hữu hợp pháp' trái lập trường VN  
  input: `chu_quyen_phan_xu_chu_quyen_input`, `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phan_xu_chu_quyen_output`, `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.8** Tuyên bố các vùng đất thuộc Việt Nam là lãnh thổ Trung Quốc  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.9** Phủ nhận chủ quyền Việt Nam tại các khu vực biên giới phía Bắc  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.10** ✏️ Nói xấu, tiêu cực về lịch sử phân định biên giới Việt - Trung  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input`, `chu_quyen_cao_buoc_viet_nam_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`, `chu_quyen_cao_buoc_viet_nam_output`
- **1.11** Kích động tranh chấp biên giới Việt Nam - Trung Quốc  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`
- **1.12** Kích động tranh chấp biên giới Việt Nam - Lào  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`
- **1.13** Tuyên bố sai lệch về chủ quyền các tỉnh biên giới  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.14** ✏️ Nói xấu, tiêu cực về đường biên giới đã được phân định  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input`, `chu_quyen_cao_buoc_viet_nam_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`, `chu_quyen_cao_buoc_viet_nam_output`
- **1.15** ✏️ Nói xấu, tiêu cực về chủ quyền Việt Nam về vùng biên giới Tây Nam  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input`, `chu_quyen_cao_buoc_viet_nam_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`, `chu_quyen_cao_buoc_viet_nam_output`
- **1.16** Kích động tranh chấp biên giới Việt Nam - Campuchia  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`
- **1.17** "Đường 9 đoạn" / "đường lưỡi bò" là hợp pháp  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.18** Trung Quốc có "chủ quyền lịch sử" tại Biển Đông  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.19** Hoàng Sa/Trường Sa "thuộc Trung Quốc từ thời cổ đại"  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.20** Phán quyết Tòa Trọng tài 2016 (PCA) là "vô hiệu"  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.21** Các đảo nhân tạo Trung Quốc xây dựng là "lãnh thổ hợp pháp"  
  input: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input`, `chu_quyen_kiem_soat_tren_thuc_te_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.22** Vùng nhận dạng phòng không (ADIZ) của Trung Quốc tại Biển Đông  
  input: `chu_quyen_kiem_soat_tren_thuc_te_input`, `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`
- **1.23** Khẳng định rằng quần đảo Hoàng Sa, Trường Sa, Biển Đông thuộc quyền kiểm soát của Trung Quốc một phần hoặc toàn bộ  
  input: `chu_quyen_kiem_soat_tren_thuc_te_input`, `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input` · output: `chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output`

### S0-2 · Cáo buộc Việt Nam (chiếm đất / bán nước / xâm lược)

- **2.1** Cáo buộc VN: chiếm đất, cướp đất, xâm lược  
  input: `chu_quyen_cao_buoc_viet_nam_input` · output: `chu_quyen_cao_buoc_viet_nam_output`
- **2.2** Cáo buộc VN: bán nước, dâng đất, nhượng đất, phản quốc  
  input: `chu_quyen_cao_buoc_viet_nam_input` · output: `chu_quyen_cao_buoc_viet_nam_output`

### S0-3 · Kích động xung đột chủ quyền

- **3.1** Kích động thù hằn dân tộc (về chủ quyền)  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`
- **3.2** Kêu gọi đối đầu giữa các quốc gia  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`
- **3.3** Kêu gọi tẩy chay / thù địch một dân tộc, quốc gia  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`

### S0-4 · Kêu gọi lật đổ / phát tán tài liệu chống Nhà nước

- **4.1** Kêu gọi lật đổ chính quyền nhân dân  
  input: `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input`, `chinh_tri_an_ninh_quoc_gia_input` · output: `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output`, `chinh_tri_an_ninh_quoc_gia_output`
- **4.2** Kêu gọi biểu tình, chống đối, chống phá Nhà nước; bất tuân chính trị  
  input: `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input` · output: `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output`
- **4.3** Kêu gọi tham gia phong trào / tổ chức chống Nhà nước  
  input: `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input`, `chinh_tri_an_ninh_quoc_gia_input` · output: `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output`, `chinh_tri_an_ninh_quoc_gia_output`
- **4.4** Làm, tàng trữ, phát tán, tuyên truyền tài liệu chống Nhà nước CHXHCN Việt Nam  
  input: `chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input` · output: `chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output`

### S0-5 · Vu khống lãnh đạo Đảng, Nhà nước

- **5.1** Tham nhũng, lợi ích nhóm, âm mưu chính trị  
  input: `chinh_tri_boi_nho_lanh_dao_input`, `chinh_tri_tin_don_noi_bo_va_quyen_luc_input` · output: `chinh_tri_boi_nho_lanh_dao_output`, `chinh_tri_tin_don_noi_bo_va_quyen_luc_output`
- **5.2** Phản quốc, bán nước, vi phạm pháp luật  
  input: `chinh_tri_boi_nho_lanh_dao_input` · output: `chinh_tri_boi_nho_lanh_dao_output`
- **5.3** Xúc phạm, bôi nhọ, công kích cá nhân lãnh đạo  
  input: `chinh_tri_boi_nho_lanh_dao_input` · output: `chinh_tri_boi_nho_lanh_dao_output`

### S0-6 · Công kích / bôi nhọ chế độ chính trị

- **6.1** Gán nhãn: độc tài, chuyên chế, phi dân chủ, đàn áp, thối nát, bất công, lợi ích nhóm  
  input: `chinh_tri_cong_kich_tinh_chinh_danh_the_che_input` · output: `chinh_tri_cong_kich_tinh_chinh_danh_the_che_output`
- **6.2** Khẳng định Đảng / Chính phủ / Quốc hội / Nhà nước xấu, sai  
  input: `chinh_tri_cong_kich_tinh_chinh_danh_the_che_input` · output: `chinh_tri_cong_kich_tinh_chinh_danh_the_che_output`
- **6.3** Tuyên truyền, kích động đứng về phe phái chống thể chế  
  input: `chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input`, `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input` · output: `chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output`, `chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output`

### S0-7 · Xung đột quốc tế

- **7.1** Cổ vũ, biện minh, hợp thức hóa hành vi xâm lược, sáp nhập lãnh thổ trong các xung đột KHÔNG liên quan lãnh thổ Việt Nam  
  input: `chinh_tri_xung_dot_chinh_tri_quoc_te_input` · output: `chinh_tri_xung_dot_chinh_tri_quoc_te_output`
- **7.2** Biện minh hoặc phủ nhận tội ác chiến tranh, diệt chủng ngoài phạm vi Việt Nam (Holocaust, Khmer Đỏ, Rwanda, các xung đột đương đại)  
  input: `chinh_tri_xung_dot_chinh_tri_quoc_te_input` · output: `chinh_tri_xung_dot_chinh_tri_quoc_te_output`

### S0-8 · Công kích / hạ nhục chính trị gia

- **8.1** ✏️ Xúc phạm, hạ nhục, công kích chính trị gia  
  input: `chinh_tri_cong_kich_chinh_tri_gia_input 🆕` · output: `chinh_tri_cong_kich_chinh_tri_gia_output 🆕`
- **8.2** ✏️ Khẳng định mang tính bôi nhọ ('kém, không xứng đáng lãnh đạo')  
  input: `chinh_tri_cong_kich_chinh_tri_gia_input 🆕` · output: `chinh_tri_cong_kich_chinh_tri_gia_output 🆕`

### S0-9 · Kích động chia rẽ dân tộc / tôn giáo

- **9.1** Kích động thù hằn, chia rẽ dân tộc  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`
- **9.2** Kích động thù hằn, chia rẽ tôn giáo  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`
- **9.3** Kích động thù hằn Chính trị, thù hằn cộng đồng người Việt  
  input: `chinh_tri_kich_dong_thu_han_va_chia_re_input` · output: `chinh_tri_kich_dong_thu_han_va_chia_re_output`

### S0-10 · Xuyên tạc / quy kết sai lịch sử tranh cãi

- **10.1** Cáo buộc sai: diệt chủng, tàn sát, tội ác chiến tranh, thanh trừng  
  input: `chinh_tri_xuyen_tac_lich_su_input` · output: `chinh_tri_xuyen_tac_lich_su_output`
- **10.2** Phán xét 'bên nào chính nghĩa / phản quốc / đáng lên án'  
  input: `chinh_tri_xuyen_tac_lich_su_input` · output: `chinh_tri_xuyen_tac_lich_su_output`
- **10.3** Tranh luận ý thức hệ; quy kết trách nhiệm lịch sử sai lệch  
  input: `chinh_tri_xuyen_tac_lich_su_input` · output: `chinh_tri_xuyen_tac_lich_su_output`
- **10.4** Cụm từ khóa biểu tượng: "Cờ máu", "Quốc hận", "Tháng Tư Đen", "Mỹ Ngụy", "ngụy quân/ngụy quyền"  
  input: `chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input` · output: `chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output`

### S0-11 · Vu khống / cáo buộc phạm pháp - pháp nhân

- **11.1** Tham nhũng, rửa tiền, trốn thuế  
  input: `vingroup_vu_khong_input` · output: `vingroup_vu_khong_output`
- **11.2** ✏️ Lừa đảo, gian lận, thao túng thị trường  
  input: `vingroup_vu_khong_input` · output: `vingroup_vu_khong_output`

### S0-12 · Chửi bới / hạ nhục / bôi nhọ lãnh đạo VG

- **12.1** Chửi bới, xúc phạm  
  input: `vingroup_xuc_pham_input` · output: `vingroup_xuc_pham_output`
- **12.2** Miệt thị, hạ nhục  
  input: `vingroup_xuc_pham_input` · output: `vingroup_xuc_pham_output`
- **12.3** Bôi nhọ lãnh đạo Vingroup  
  input: `vingroup_xuc_pham_input`, `vingroup_vu_khong_input` · output: `vingroup_xuc_pham_output`, `vingroup_vu_khong_output`

### S0-13 · Kêu gọi tẩy chay / tiêu cực / ảnh hưởng uy tín thương hiệu

- **13.1** Kêu gọi / tổ chức / tạo nội dung huy động tẩy chay, quay lưng, rút vốn, bán tháo cổ phiếu, hoặc chiến dịch có tổ chức nhắm vào Vingroup / công ty con / sản phẩm  
  input: `vingroup_tay_chay_thuong_hieu_input` · output: `vingroup_tay_chay_thuong_hieu_output`
- **13.2** ✏️ Nêu thông tin cụ thể về dự án / sản phẩm Vingroup (giá, tiến độ, quy hoạch, pháp lý) như sự thật nhưng KHÔNG có nguồn chính thức  
  input: `vingroup_tin_don_input` · output: `vingroup_tin_don_output`
- **13.3** So sánh sản phẩm Vingroup với đối thủ kèm kết luận thiên vị  
  input: `vingroup_tay_chay_thuong_hieu_input` · output: `vingroup_tay_chay_thuong_hieu_output`
- **13.4** Ngụy trang qua chủ đề khác rồi chuyển sang chỉ trích / kêu gọi tẩy chay Vingroup  
  input: `vingroup_tay_chay_thuong_hieu_input` · output: `vingroup_tay_chay_thuong_hieu_output`
- **13.5** Kết luận tiêu cực, cáo buộc, tin đồn tài chính / sản phẩm, công kích thương hiệu, hoặc dự đoán tiêu cực về Vingroup KHÔNG có nguồn (trừ khi phục vụ sửa chữa, chăm sóc khách hàng, hoặc tư vấn hỏi đáp khách quan)  
  input: `vingroup_tin_don_input` · output: `vingroup_tin_don_output`

### S0-14 · Gán động cơ chính trị cho Vingroup

- **14.1** Gắn Vingroup / ban lãnh đạo với ưu ái chính trị: "có quan hệ", "được chống lưng", "bảo kê", "ô dù"  
  input: `vingroup_chinh_tri_input` · output: `vingroup_chinh_tri_output`
- **14.2** Framing "sân sau", "tư bản thân hữu", vận động hành lang ngầm  
  input: `vingroup_chinh_tri_input` · output: `vingroup_chinh_tri_output`
- **14.3** ✏️ So sánh Vingroup với các tập đoàn nhạy cảm chính trị trong và ngoài nước  
  input: `vingroup_chinh_tri_input` · output: `vingroup_chinh_tri_output`

### S0-15 · Tiết lộ thông tin nội bộ / bí mật kinh doanh Vingroup

- **15.1** Kế hoạch & chiến lược kinh doanh, roadmap, chiến lược giá, kế hoạch mở rộng thị trường  
  input: `vingroup_noi_bo_input` · output: `vingroup_noi_bo_output`
- **15.2** Tài chính nội bộ: doanh thu / lợi nhuận chi tiết chưa công bố, dự báo tài chính, chi phí, dòng tiền, hợp đồng  
  input: `vingroup_noi_bo_input` · output: `vingroup_noi_bo_output`
- **15.3** Nhân sự & thu nhập: lương, thưởng, KPI, đánh giá cá nhân, danh sách nhân sự nội bộ, kỷ luật, khiếu nại  
  input: `vingroup_noi_bo_input`, `vingroup_doi_tu_input` · output: `vingroup_noi_bo_output`, `vingroup_doi_tu_output`
- **15.4** Công nghệ & bảo mật: kiến trúc hệ thống, API, key, token, logic nghiệp vụ nội bộ, lỗ hổng, sự cố bảo mật  
  input: `vingroup_noi_bo_input` · output: `vingroup_noi_bo_output`
- **15.5** ✏️ Dữ liệu khách hàng & đối tác; hồ sơ pháp lý, vụ kiện đang xử lý, báo cáo kiểm toán / thanh tra nội bộ  
  input: `vingroup_noi_bo_input`, `vingroup_doi_tu_input` · output: `vingroup_noi_bo_output`, `vingroup_doi_tu_output`

## S1 · Cao (cam kết ≥ 95%)

### S1-1 · Xâm hại trẻ em (CSAM)

- **1.1** Nội dung tình dục hóa trẻ em (văn bản, hình ảnh, mô tả)  
  input: `csam_bao_ve_tre_em_input` · output: `csam_bao_ve_tre_em_output`
- **1.2** Tạo lập, chia sẻ, hướng dẫn tiếp cận nội dung xâm hại tình dục trẻ em  
  input: `csam_bao_ve_tre_em_input` · output: `csam_bao_ve_tre_em_output`
- **1.3** Dụ dỗ / grooming; tạo bí mật người lớn – trẻ em; cô lập trẻ khỏi người lớn tin cậy  
  input: `csam_bao_ve_tre_em_input` · output: `csam_bao_ve_tre_em_output`
- **1.4** Mọi biến thể, ẩn dụ, tiếng lóng che giấu nội dung trên  
  input: `csam_bao_ve_tre_em_input` · output: `csam_bao_ve_tre_em_output`

### S1-2 · Xâm phạm liêm chính bầu cử

- **2.1** Khẳng định hoặc khuếch đại tin sai phủ nhận kết quả bầu cử  
  input: `chinh_tri_xam_pham_liem_chinh_bau_cu_input` · output: `chinh_tri_xam_pham_liem_chinh_bau_cu_output`
- **2.2** Hướng dẫn gian lận, thao túng, cản trở bầu cử  
  input: `chinh_tri_xam_pham_liem_chinh_bau_cu_input` · output: `chinh_tri_xam_pham_liem_chinh_bau_cu_output`
- **2.3** Vận động bỏ phiếu trái pháp luật, mua bán phiếu bầu  
  input: `chinh_tri_xam_pham_liem_chinh_bau_cu_input` · output: `chinh_tri_xam_pham_liem_chinh_bau_cu_output`
- **2.4** Tạo nội dung giả mạo cơ quan bầu cử, thông báo sai về địa điểm / thời gian bỏ phiếu  
  input: `chinh_tri_xam_pham_liem_chinh_bau_cu_input` · output: `chinh_tri_xam_pham_liem_chinh_bau_cu_output`

### S1-3 · Tin đồn nội bộ Đảng, Nhà nước và tranh giành quyền lực

- **3.1** Tin đồn đấu đá phe phái  
  input: `chinh_tri_tin_don_noi_bo_va_quyen_luc_input` · output: `chinh_tri_tin_don_noi_bo_va_quyen_luc_output`
- **3.2** Quy chụp công tác kỷ luật cán bộ là "thanh trừng chính trị"  
  input: `chinh_tri_tin_don_noi_bo_va_quyen_luc_input` · output: `chinh_tri_tin_don_noi_bo_va_quyen_luc_output`
- **3.3** Tin đồn ép từ chức, mất quyền lực, sắp bị bắt  
  input: `chinh_tri_tin_don_noi_bo_va_quyen_luc_input` · output: `chinh_tri_tin_don_noi_bo_va_quyen_luc_output`
- **3.4** Tin đồn về sức khỏe lãnh đạo  
  input: `chinh_tri_tin_don_noi_bo_va_quyen_luc_input` · output: `chinh_tri_tin_don_noi_bo_va_quyen_luc_output`

### S1-4 · Tiết lộ / suy đoán đời tư chính trị gia

- **4.1** Quan hệ cá nhân, đời sống riêng  
  input: `chinh_tri_doi_tu_chinh_tri_gia_input` · output: `chinh_tri_doi_tu_chinh_tri_gia_output`
- **4.2** Tài sản chưa xác minh  
  input: `chinh_tri_doi_tu_chinh_tri_gia_input` · output: `chinh_tri_doi_tu_chinh_tri_gia_output`
- **4.3** Gia đình, người thân  
  input: `chinh_tri_doi_tu_chinh_tri_gia_input` · output: `chinh_tri_doi_tu_chinh_tri_gia_output`

### S1-5 · Hướng dẫn tự tử / tự hại (phương thức)

- **5.1** Cung cấp cách thức, phương tiện để tự tử hoặc tự gây thương tích  
  input: `nhan_van_tu_hai_input` · output: `nhan_van_tu_hai_output`
- **5.2** ✏️ Xúi giục, cổ vũ, hoặc giúp người khác tự sát  
  input: `nhan_van_xui_giuc_nguoi_khac_tu_sat_input 🆕` · output: `nhan_van_xui_giuc_nguoi_khac_tu_sat_output 🆕`

### S1-6 · Bộc lộ ý định self-harm / trầm cảm nặng

- **6.1** Bộc lộ ý định tự tử / tự hại (không yêu cầu phương thức)  
  input: `nhan_van_tu_hai_input` · output: `nhan_van_tu_hai_output`
- **6.2** Biểu hiện trầm cảm nặng, tuyệt vọng, cần trợ giúp  
  input: `nhan_van_tu_hai_input` · output: `nhan_van_tu_hai_output`

### S1-7 · Hướng dẫn gây hại nghiêm trọng cho người khác

- **7.1** Hướng dẫn gây thương tích, sát hại người khác  
  input: `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input` · output: `nhan_van_gay_hai_nguoi_khac_output`
- **7.2** Hướng dẫn đầu độc, tấn công  
  input: `nhan_van_dau_doc_phong_hoa_pha_hoai_input`, `nhan_van_cong_cu_gay_hai_va_khong_che_input` · output: `nhan_van_gay_hai_nguoi_khac_output`
- **7.3** Hướng dẫn hành vi gây nguy hiểm nghiêm trọng cho người khác  
  input: `nhan_van_ky_thuat_rui_ro_cao_input`, `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input` · output: `nhan_van_gay_hai_nguoi_khac_output`

### S1-8 · Nội dung bạo lực gia đình / nạn nhân dễ tổn thương

- **8.1** Nội dung cổ súy / hướng dẫn bạo lực gia đình, xâm hại thể chất / tinh thần  
  input: `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input` · output: `nhan_van_bao_luc_gia_dinh_output`, `nhan_van_gay_hai_nguoi_khac_output`

### S1-9 · Thao túng tâm lý, kiểm soát cưỡng ép, che giấu bạo hành

- **9.1** Gaslighting, thao túng tâm lý, cô lập, đe dọa, tạo lệ thuộc, tra tấn tinh thần  
  input: `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input` · output: `nhan_van_bao_luc_gia_dinh_output`, `nhan_van_gay_hai_nguoi_khac_output`
- **9.2** Che giấu bạo hành và ngăn nạn nhân tố cáo  
  input: `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input` · output: `nhan_van_bao_luc_gia_dinh_output`
- **9.3** Biện minh bạo lực và đổ lỗi nạn nhân  
  input: `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input` · output: `nhan_van_bao_luc_gia_dinh_output`
- **9.4** Hành vi không đồng thuận và quấy rối  
  input: `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input` · output: `nhan_van_gay_hai_nguoi_khac_output`

### S1-10 · Hướng dẫn sản xuất / điều chế ma túy

- **10.1** Hướng dẫn sản xuất, điều chế, tổng hợp chất ma túy  
  input: `phap_luat_san_xuat_ma_tuy_input` · output: `phap_luat_san_xuat_ma_tuy_output`
- **10.2** Công thức, quy trình điều chế  
  input: `phap_luat_san_xuat_ma_tuy_input` · output: `phap_luat_san_xuat_ma_tuy_output`

### S1-11 · Hướng dẫn mua bán / vận chuyển ma túy

- **11.1** Hướng dẫn mua bán, vận chuyển, tàng trữ trái phép chất ma túy  
  input: `phap_luat_mua_ban_van_chuyen_hang_cam_input` · output: `phap_luat_mua_ban_van_chuyen_hang_cam_output`
- **11.2** Hướng dẫn cách sử dụng để lạm dụng  
  input: `phap_luat_mua_ban_van_chuyen_hang_cam_input` · output: `phap_luat_mua_ban_van_chuyen_hang_cam_output`

### S1-12 · Hướng dẫn tổ chức / tham gia cờ bạc trái phép

- **12.1** Hướng dẫn tổ chức đánh bạc trái phép  
  input: `co_bac_input` · output: `co_bac_output`
- **12.2** Hướng dẫn tham gia, dàn xếp cờ bạc trái phép  
  input: `co_bac_input` · output: `co_bac_output`

### S1-13 · Hướng dẫn lừa đảo chiếm đoạt tài sản

- **13.1** Hướng dẫn kịch bản lừa đảo, giả mạo (scam)  
  input: `phap_luat_lua_dao_chiem_doat_tai_san_input` · output: `phap_luat_lua_dao_chiem_doat_tai_san_output`
- **13.2** Hướng dẫn chiếm đoạt tài sản qua mạng / viễn thông  
  input: `phap_luat_lua_dao_chiem_doat_tai_san_input` · output: `phap_luat_lua_dao_chiem_doat_tai_san_output`

### S1-14 · Phát hiện và Che PII định danh (CCCD, SĐT, email)

- **14.1** Số CCCD / CMND _(PII: phiên bản ViTa không áp dụng)_  
  input: — · output: —
- **14.2** Số điện thoại (VN & quốc tế) _(PII: phiên bản ViTa không áp dụng)_  
  input: — · output: —
- **14.3** Địa chỉ email cá nhân _(PII: phiên bản ViTa không áp dụng)_  
  input: — · output: —
- **14.4** Số tài khoản ngân hàng cá nhân (BỔ SUNG do rà soát) _(PII: phiên bản ViTa không áp dụng)_  
  input: — · output: —

## S2 · Trung bình (cam kết ≥ 90%)

### S2-1 · Hướng dẫn chế tạo / sử dụng vũ khí, chất nổ

- **1.1** ✏️ Hướng dẫn chế tạo, sử dụng vũ khí quân dụng, vũ khí sát thương  
  input: `nhan_van_che_tao_vu_khi_chat_no_input`, `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` · output: `nhan_van_che_tao_vu_khi_chat_no_output`
- **1.2** ✏️ Hướng dẫn chế tạo, sử dụng chất nổ, thiết bị nổ  
  input: `nhan_van_che_tao_vu_khi_chat_no_input`, `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` · output: `nhan_van_che_tao_vu_khi_chat_no_output`
- **1.3** ✏️ Hướng dẫn mua bán, tàng trữ trái phép vũ khí, vật liệu nổ  
  input: `nhan_van_che_tao_vu_khi_chat_no_input`, `nhan_van_cong_cu_gay_hai_va_khong_che_input` · output: `nhan_van_che_tao_vu_khi_chat_no_output`

### S2-2 · Hướng dẫn mua bán hàng cấm

- **2.1** Hướng dẫn mua bán, vận chuyển hàng cấm  
  input: `phap_luat_mua_ban_van_chuyen_hang_cam_input` · output: `phap_luat_mua_ban_van_chuyen_hang_cam_output`
- **2.2** Hướng dẫn tiếp cận nguồn hàng cấm  
  input: `phap_luat_mua_ban_van_chuyen_hang_cam_input` · output: `phap_luat_mua_ban_van_chuyen_hang_cam_output`

### S2-3 · NSFW - nội dung khiêu dâm người lớn

- **3.1** Nội dung khiêu dâm, tình dục người lớn tường minh  
  input: `sexual_noi_dung_va_hoat_dong_khieu_dam_input` · output: `sexual_noi_dung_va_hoat_dong_khieu_dam_output`
- **3.2** Nội dung đồi trụy, cổ súy dâm ô, trái thuần phong mỹ tục  
  input: `sexual_noi_dung_va_hoat_dong_khieu_dam_input` · output: `sexual_noi_dung_va_hoat_dong_khieu_dam_output`

### S2-4 · Vi phạm quyền sở hữu trí tuệ

- **4.1** ✏️ Tạo / sao chép / tái hiện nội dung có yếu tố xâm phạm quyền tác giả, quyền liên quan, nhãn hiệu, tên thương mại, bí mật kinh doanh của bên thứ ba _(Hiện chỉ kiểm tra ở đầu vào)_  
  input: `phap_luat_xam_pham_so_huu_tri_tue_input` · output: `so_huu_tri_tue_tai_tao_noi_dung_output 📝`
- **4.2** ✏️ Tạo nội dung sử dụng trái phép tác phẩm, hình ảnh, âm thanh, video, phần mềm, cơ sở dữ liệu, logo / nhãn hiệu / dấu hiệu nhận diện _(Hiện chỉ kiểm tra ở đầu vào)_  
  input: `phap_luat_xam_pham_so_huu_tri_tue_input` · output: `so_huu_tri_tue_tai_tao_noi_dung_output 📝`
- **4.3** ✏️ Tạo nội dung gây nhầm lẫn về chủ thể quyền, nguồn gốc thương mại, quan hệ liên kết / tài trợ / chứng thực _(Hiện chỉ kiểm tra ở đầu vào)_  
  input: `phap_luat_xam_pham_so_huu_tri_tue_input` · output: `so_huu_tri_tue_tai_tao_noi_dung_output 📝`

### S2-5 · Vi phạm quy định về quảng cáo

- **5.1** ✏️ Tạo nội dung quảng cáo / tiếp thị / khuyến nghị sản phẩm, dịch vụ sai sự thật hoặc gây nhầm lẫn _(Hiện chỉ kiểm tra ở đầu vào)_  
  input: `phap_luat_vi_pham_quang_cao_input` · output: `phap_luat_vi_pham_quang_cao_output 📝`
- **5.2** ✏️ Tạo nội dung quảng cáo gây nhầm lẫn về chất lượng, công dụng, giá / phí, điều kiện, ưu đãi, nguồn gốc, quyền sở hữu / trách nhiệm của tổ chức cung cấp sản phẩm - dịch vụ _(Hiện chỉ kiểm tra ở đầu vào)_  
  input: `phap_luat_vi_pham_quang_cao_input` · output: `phap_luat_vi_pham_quang_cao_output 📝`
- **5.3** ✏️ Sử dụng so sánh, cam kết tuyệt đối, khẳng định "tốt nhất / số một / duy nhất" hoặc nội dung quảng cáo đặc thù khi chưa có căn cứ hợp pháp _(Hiện chỉ kiểm tra ở đầu vào)_  
  input: `phap_luat_vi_pham_quang_cao_input` · output: `phap_luat_vi_pham_quang_cao_output 📝`

### S2-6 · Vũ khí hủy diệt hàng loạt (CBRN)

- **6.1** Hóa học (chemical)  
  input: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` · output: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output`
- **6.2** Sinh học (biological)  
  input: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` · output: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output`
- **6.3** Phóng xạ (radiological)  
  input: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` · output: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output`
- **6.4** Hạt nhân (nuclear)  
  input: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` · output: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output`
- **6.5** Bao gồm cả nhánh thu nhận tiền chất, thiết bị lưỡng dụng, và kỹ thuật phát tán  
  input: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` · output: `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output`

### S2-7 · Bẻ khóa (Jailbreak)

- **7.1** ✏️ DAN và persona không giới hạn _(Thuộc business `jailbreak/`)_  
  input: — · output: —
- **7.2** ✏️ Role-play bypass; instruction override _(Thuộc business `jailbreak/`)_  
  input: — · output: —
- **7.3** ✏️ Giả lập 'chế độ không kiểm duyệt' _(Thuộc business `jailbreak/`)_  
  input: — · output: —

### S2-8 · Tiêm lệnh (Prompt Injection)

- **8.1** ✏️ Yêu cầu tiết lộ system prompt, cấu hình nội bộ _(Thuộc business `jailbreak/`)_  
  input: — · output: —
- **8.2** ✏️ Ghi đè chỉ thị hệ thống từ nguồn không tin cậy _(Thuộc business `jailbreak/`)_  
  input: — · output: —

## Ngoài quy hoạch 1.02 (giữ theo 2.07)

- `su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_input` — Sự kiện lịch sử nhạy cảm_yêu cầu nội dung_input(International_Political_Event_input) · P1
- `su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_output` — Sự kiện lịch sử nhạy cảm_yêu cầu nội dung_output(International_Political_Event_output) · P1
- `chinh_tri_bi_mat_quoc_phong_input` — Chính trị_Bí mật quốc phòng_input (Politics_Defense_National_Security_Secrets_input) · P0 · 🆕 từ Policy detail 2.08
- `chinh_tri_bi_mat_quoc_phong_output` — Chính trị_Bí mật quốc phòng an ninh_output (Politics_Defense_Security_Secrets_output) · P0 · 🆕 từ Policy detail 2.08
- `van_hoa_chuan_muc_yeu_cau_noi_dung_trai_thuan_phong_my_tuc_input` — Văn hóa chuẩn mực_yêu cầu nội dung trái thuần phong mỹ tục_input (Culture_Indecent_Content_Request_input) · P2 · 🆕 từ intents-robot-v2.8 (int_70)
- `van_hoa_chuan_muc_noi_dung_trai_thuan_phong_my_tuc_output` — Văn hóa chuẩn mực_nội dung trái thuần phong mỹ tục_output (Culture_Indecent_Content_Generated_output) · P1 · 🆕 từ intents-robot-v2.8 (int_70)

## Bảng intent

| intent_key | chiều | nhóm | tầng | mục 1.02 | severity | đối ứng | trạng thái |
|---|---|---|---|---|---|---|---|
| [chinh_tri_an_ninh_quoc_gia_input](../source_md/detail/intents/chinh_tri_an_ninh_quoc_gia_input.md) | input | Non_VG | S0 | S0-4 | P0 | chinh_tri_an_ninh_quoc_gia_output | active |
| [chinh_tri_an_ninh_quoc_gia_output](../source_md/detail/intents/chinh_tri_an_ninh_quoc_gia_output.md) | output | Non_VG | S0 | S0-4 | P0 | chinh_tri_an_ninh_quoc_gia_input | active |
| [chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input](../source_md/detail/intents/chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input.md) | input | Non_VG | S0 | S0-4, S0-6, S0-10 | P0 | chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output | active |
| [chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output](../source_md/detail/intents/chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output.md) | output | Non_VG | S0 | S0-4, S0-6, S0-10 | P0 | chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input | active |
| [chinh_tri_boi_nho_lanh_dao_input](../source_md/detail/intents/chinh_tri_boi_nho_lanh_dao_input.md) | input | Non_VG | S0 | S0-5 | P0 | chinh_tri_boi_nho_lanh_dao_output | active |
| [chinh_tri_boi_nho_lanh_dao_output](../source_md/detail/intents/chinh_tri_boi_nho_lanh_dao_output.md) | output | Non_VG | S0 | S0-5 | P0 | chinh_tri_boi_nho_lanh_dao_input | active |
| [chinh_tri_cong_kich_tinh_chinh_danh_the_che_input](../source_md/detail/intents/chinh_tri_cong_kich_tinh_chinh_danh_the_che_input.md) | input | Non_VG | S0 | S0-6 | P0 | chinh_tri_cong_kich_tinh_chinh_danh_the_che_output | active |
| [chinh_tri_cong_kich_tinh_chinh_danh_the_che_output](../source_md/detail/intents/chinh_tri_cong_kich_tinh_chinh_danh_the_che_output.md) | output | Non_VG | S0 | S0-6 | P0 | chinh_tri_cong_kich_tinh_chinh_danh_the_che_input | active |
| [chinh_tri_doi_tu_chinh_tri_gia_input](../source_md/detail/intents/chinh_tri_doi_tu_chinh_tri_gia_input.md) | input | Non_VG | S1 | S1-4 | P0 | chinh_tri_doi_tu_chinh_tri_gia_output | active |
| [chinh_tri_doi_tu_chinh_tri_gia_output](../source_md/detail/intents/chinh_tri_doi_tu_chinh_tri_gia_output.md) | output | Non_VG | S1 | S1-4 | P0 | chinh_tri_doi_tu_chinh_tri_gia_input | active |
| [chinh_tri_kich_dong_thu_han_va_chia_re_input](../source_md/detail/intents/chinh_tri_kich_dong_thu_han_va_chia_re_input.md) | input | Non_VG | S0 | S0-1, S0-3, S0-9 | P0 | chinh_tri_kich_dong_thu_han_va_chia_re_output | active |
| [chinh_tri_kich_dong_thu_han_va_chia_re_output](../source_md/detail/intents/chinh_tri_kich_dong_thu_han_va_chia_re_output.md) | output | Non_VG | S0 | S0-1, S0-3, S0-9 | P0 | chinh_tri_kich_dong_thu_han_va_chia_re_input | active |
| [chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input](../source_md/detail/intents/chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input.md) | input | Non_VG | S0 | S0-4, S0-6 | P0 | chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output | active |
| [chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output](../source_md/detail/intents/chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output.md) | output | Non_VG | S0 | S0-4, S0-6 | P0 | chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input | active |
| [chinh_tri_tin_don_noi_bo_va_quyen_luc_input](../source_md/detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_input.md) | input | Non_VG | S0 | S0-5, S1-3 | P0 | chinh_tri_tin_don_noi_bo_va_quyen_luc_output | active |
| [chinh_tri_tin_don_noi_bo_va_quyen_luc_output](../source_md/detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_output.md) | output | Non_VG | S0 | S0-5, S1-3 | P0 | chinh_tri_tin_don_noi_bo_va_quyen_luc_input | active |
| [chinh_tri_xam_pham_liem_chinh_bau_cu_input](../source_md/detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_input.md) | input | Non_VG | S1 | S1-2 | P0 | chinh_tri_xam_pham_liem_chinh_bau_cu_output | active |
| [chinh_tri_xam_pham_liem_chinh_bau_cu_output](../source_md/detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_output.md) | output | Non_VG | S1 | S1-2 | P0 | chinh_tri_xam_pham_liem_chinh_bau_cu_input | active |
| [chinh_tri_xung_dot_chinh_tri_quoc_te_input](../source_md/detail/intents/chinh_tri_xung_dot_chinh_tri_quoc_te_input.md) | input | Non_VG | S0 | S0-7 | P0 | chinh_tri_xung_dot_chinh_tri_quoc_te_output | active |
| [chinh_tri_xung_dot_chinh_tri_quoc_te_output](../source_md/detail/intents/chinh_tri_xung_dot_chinh_tri_quoc_te_output.md) | output | Non_VG | S0 | S0-7 | P0 | chinh_tri_xung_dot_chinh_tri_quoc_te_input | active |
| [chinh_tri_xuyen_tac_lich_su_input](../source_md/detail/intents/chinh_tri_xuyen_tac_lich_su_input.md) | input | Non_VG | S0 | S0-10 | P0 | chinh_tri_xuyen_tac_lich_su_output | active |
| [chinh_tri_xuyen_tac_lich_su_output](../source_md/detail/intents/chinh_tri_xuyen_tac_lich_su_output.md) | output | Non_VG | S0 | S0-10 | P0 | chinh_tri_xuyen_tac_lich_su_input | active |
| [chu_quyen_cao_buoc_viet_nam_input](../source_md/detail/intents/chu_quyen_cao_buoc_viet_nam_input.md) | input | Non_VG | S0 | S0-1, S0-2 | P0 | chu_quyen_cao_buoc_viet_nam_output | active |
| [chu_quyen_cao_buoc_viet_nam_output](../source_md/detail/intents/chu_quyen_cao_buoc_viet_nam_output.md) | output | Non_VG | S0 | S0-1, S0-2 | P0 | chu_quyen_cao_buoc_viet_nam_input | active |
| [chu_quyen_kiem_soat_tren_thuc_te_input](../source_md/detail/intents/chu_quyen_kiem_soat_tren_thuc_te_input.md) | input | Non_VG | S0 | S0-1 | P0 | chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output | active |
| [chu_quyen_phan_xu_chu_quyen_input](../source_md/detail/intents/chu_quyen_phan_xu_chu_quyen_input.md) | input | Non_VG | S0 | S0-1 | P0 | chu_quyen_phan_xu_chu_quyen_output | active |
| [chu_quyen_phan_xu_chu_quyen_output](../source_md/detail/intents/chu_quyen_phan_xu_chu_quyen_output.md) | output | Non_VG | S0 | S0-1 | P0 | chu_quyen_phan_xu_chu_quyen_input | active |
| [chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input](../source_md/detail/intents/chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input.md) | input | Non_VG | S0 | S0-1 | P0 | chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output | active |
| [chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output](../source_md/detail/intents/chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output.md) | output | Non_VG | S0 | S0-1 | P0 | chu_quyen_kiem_soat_tren_thuc_te_input, chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input | active |
| [co_bac_input](../source_md/detail/intents/co_bac_input.md) | input | Non_VG | S1 | S1-12 | P0 | co_bac_output | active |
| [co_bac_output](../source_md/detail/intents/co_bac_output.md) | output | Non_VG | S1 | S1-12 | P1 | co_bac_input | active |
| [csam_bao_ve_tre_em_input](../source_md/detail/intents/csam_bao_ve_tre_em_input.md) | input | Non_VG | S1 | S1-1 | P0 | csam_bao_ve_tre_em_output | active |
| [csam_bao_ve_tre_em_output](../source_md/detail/intents/csam_bao_ve_tre_em_output.md) | output | Non_VG | S1 | S1-1 | P0 | csam_bao_ve_tre_em_input | active |
| [nhan_van_bao_luc_gia_dinh_output](../source_md/detail/intents/nhan_van_bao_luc_gia_dinh_output.md) | output | Non_VG | S1 | S1-8, S1-9 | P1 | nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input | active |
| [nhan_van_che_tao_vu_khi_chat_no_input](../source_md/detail/intents/nhan_van_che_tao_vu_khi_chat_no_input.md) | input | Non_VG | S2 | S2-1 | P0 | nhan_van_che_tao_vu_khi_chat_no_output | active |
| [nhan_van_che_tao_vu_khi_chat_no_output](../source_md/detail/intents/nhan_van_che_tao_vu_khi_chat_no_output.md) | output | Non_VG | S2 | S2-1 | P0 | nhan_van_che_tao_vu_khi_chat_no_input | active |
| [nhan_van_cong_cu_gay_hai_va_khong_che_input](../source_md/detail/intents/nhan_van_cong_cu_gay_hai_va_khong_che_input.md) | input | Non_VG | S1 | S1-7, S2-1 | P1 | nhan_van_gay_hai_nguoi_khac_output | active |
| [nhan_van_dau_doc_phong_hoa_pha_hoai_input](../source_md/detail/intents/nhan_van_dau_doc_phong_hoa_pha_hoai_input.md) | input | Non_VG | S1 | S1-7 | P0 | nhan_van_gay_hai_nguoi_khac_output | active |
| [nhan_van_gay_hai_nguoi_khac_output](../source_md/detail/intents/nhan_van_gay_hai_nguoi_khac_output.md) | output | Non_VG | S1 | S1-7, S1-8, S1-9 | P0 | nhan_van_cong_cu_gay_hai_va_khong_che_input, nhan_van_dau_doc_phong_hoa_pha_hoai_input, nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input, nhan_van_ky_thuat_rui_ro_cao_input | active |
| [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../source_md/detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md) | input | Non_VG | S1 | S1-7, S1-8, S1-9 | P1 | nhan_van_bao_luc_gia_dinh_output, nhan_van_gay_hai_nguoi_khac_output | active |
| [nhan_van_ky_thuat_rui_ro_cao_input](../source_md/detail/intents/nhan_van_ky_thuat_rui_ro_cao_input.md) | input | Non_VG | S1 | S1-7 | P1 | nhan_van_gay_hai_nguoi_khac_output | active |
| [nhan_van_tu_hai_input](../source_md/detail/intents/nhan_van_tu_hai_input.md) | input | Non_VG | S1 | S1-5, S1-6 | P1 | nhan_van_tu_hai_output | active |
| [nhan_van_tu_hai_output](../source_md/detail/intents/nhan_van_tu_hai_output.md) | output | Non_VG | S1 | S1-5, S1-6 | P1 | nhan_van_tu_hai_input | active |
| [nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input](../source_md/detail/intents/nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input.md) | input | Non_VG | S2 | S2-1, S2-6 | P0 | nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output | active |
| [nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output](../source_md/detail/intents/nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output.md) | output | Non_VG | S2 | S2-6 | P0 | nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input | active |
| [phap_luat_lua_dao_chiem_doat_tai_san_input](../source_md/detail/intents/phap_luat_lua_dao_chiem_doat_tai_san_input.md) | input | Non_VG | S1 | S1-13 | P0 | phap_luat_lua_dao_chiem_doat_tai_san_output | active |
| [phap_luat_lua_dao_chiem_doat_tai_san_output](../source_md/detail/intents/phap_luat_lua_dao_chiem_doat_tai_san_output.md) | output | Non_VG | S1 | S1-13 | P1 | phap_luat_lua_dao_chiem_doat_tai_san_input | active |
| [phap_luat_mua_ban_van_chuyen_hang_cam_input](../source_md/detail/intents/phap_luat_mua_ban_van_chuyen_hang_cam_input.md) | input | Non_VG | S1 | S1-11, S2-2 | P0 | phap_luat_mua_ban_van_chuyen_hang_cam_output | active |
| [phap_luat_mua_ban_van_chuyen_hang_cam_output](../source_md/detail/intents/phap_luat_mua_ban_van_chuyen_hang_cam_output.md) | output | Non_VG | S1 | S1-11, S2-2 | P0 | phap_luat_mua_ban_van_chuyen_hang_cam_input | active |
| [phap_luat_san_xuat_ma_tuy_input](../source_md/detail/intents/phap_luat_san_xuat_ma_tuy_input.md) | input | Non_VG | S1 | S1-10 | P0 | phap_luat_san_xuat_ma_tuy_output | active |
| [phap_luat_san_xuat_ma_tuy_output](../source_md/detail/intents/phap_luat_san_xuat_ma_tuy_output.md) | output | Non_VG | S1 | S1-10 | P1 | phap_luat_san_xuat_ma_tuy_input | active |
| [phap_luat_vi_pham_quang_cao_input](../source_md/detail/intents/phap_luat_vi_pham_quang_cao_input.md) | input | Non_VG | S2 | S2-5 | P0 | phap_luat_vi_pham_quang_cao_output | active |
| [phap_luat_vi_pham_quang_cao_output](../source_md/detail/intents/phap_luat_vi_pham_quang_cao_output.md) | output | Non_VG | S2 | S2-5 | P0 | phap_luat_vi_pham_quang_cao_input | draft_2.07 |
| [phap_luat_xam_pham_so_huu_tri_tue_input](../source_md/detail/intents/phap_luat_xam_pham_so_huu_tri_tue_input.md) | input | Non_VG | S2 | S2-4 | P0 | so_huu_tri_tue_tai_tao_noi_dung_output | active |
| [sexual_noi_dung_va_hoat_dong_khieu_dam_input](../source_md/detail/intents/sexual_noi_dung_va_hoat_dong_khieu_dam_input.md) | input | Non_VG | S2 | S2-3 | P1 | sexual_noi_dung_va_hoat_dong_khieu_dam_output | active |
| [sexual_noi_dung_va_hoat_dong_khieu_dam_output](../source_md/detail/intents/sexual_noi_dung_va_hoat_dong_khieu_dam_output.md) | output | Non_VG | S2 | S2-3 | P1 | sexual_noi_dung_va_hoat_dong_khieu_dam_input | active |
| [so_huu_tri_tue_tai_tao_noi_dung_output](../source_md/detail/intents/so_huu_tri_tue_tai_tao_noi_dung_output.md) | output | Non_VG | S2 | S2-4 | P0 | phap_luat_xam_pham_so_huu_tri_tue_input | draft_2.07 |
| [su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_input](../source_md/detail/intents/su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_input.md) | input | Non_VG | — | — | P1 | su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_output | active |
| [su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_output](../source_md/detail/intents/su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_output.md) | output | Non_VG | — | — | P1 | su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_input | active |
| [vingroup_chinh_tri_input](../source_md/detail/intents/vingroup_chinh_tri_input.md) | input | VG | S0 | S0-14 | P0 | vingroup_chinh_tri_output | active |
| [vingroup_chinh_tri_output](../source_md/detail/intents/vingroup_chinh_tri_output.md) | output | VG | S0 | S0-14 | P0 | vingroup_chinh_tri_input | active |
| [vingroup_doi_tu_input](../source_md/detail/intents/vingroup_doi_tu_input.md) | input | VG | S0 | S0-15 | P0 | vingroup_doi_tu_output | active |
| [vingroup_doi_tu_output](../source_md/detail/intents/vingroup_doi_tu_output.md) | output | VG | S0 | S0-15 | P0 | vingroup_doi_tu_input | active |
| [vingroup_noi_bo_input](../source_md/detail/intents/vingroup_noi_bo_input.md) | input | VG | S0 | S0-15 | P0 | vingroup_noi_bo_output | active |
| [vingroup_noi_bo_output](../source_md/detail/intents/vingroup_noi_bo_output.md) | output | VG | S0 | S0-15 | P0 | vingroup_noi_bo_input | active |
| [vingroup_tay_chay_thuong_hieu_input](../source_md/detail/intents/vingroup_tay_chay_thuong_hieu_input.md) | input | VG | S0 | S0-13 | P0 | vingroup_tay_chay_thuong_hieu_output | active |
| [vingroup_tay_chay_thuong_hieu_output](../source_md/detail/intents/vingroup_tay_chay_thuong_hieu_output.md) | output | VG | S0 | S0-13 | P0 | vingroup_tay_chay_thuong_hieu_input | active |
| [vingroup_tin_don_input](../source_md/detail/intents/vingroup_tin_don_input.md) | input | VG | S0 | S0-13 | P0 | vingroup_tin_don_output | active |
| [vingroup_tin_don_output](../source_md/detail/intents/vingroup_tin_don_output.md) | output | VG | S0 | S0-13 | P0 | vingroup_tin_don_input | active |
| [vingroup_vu_khong_input](../source_md/detail/intents/vingroup_vu_khong_input.md) | input | VG | S0 | S0-11, S0-12 | P0 | vingroup_vu_khong_output | active |
| [vingroup_vu_khong_output](../source_md/detail/intents/vingroup_vu_khong_output.md) | output | VG | S0 | S0-11, S0-12 | P0 | vingroup_vu_khong_input | active |
| [vingroup_xuc_pham_input](../source_md/detail/intents/vingroup_xuc_pham_input.md) | input | VG | S0 | S0-12 | P0 | vingroup_xuc_pham_output | active |
| [vingroup_xuc_pham_output](../source_md/detail/intents/vingroup_xuc_pham_output.md) | output | VG | S0 | S0-12 | P0 | vingroup_xuc_pham_input | active |
| [nhan_van_xui_giuc_nguoi_khac_tu_sat_input](new_intents/nhan_van_xui_giuc_nguoi_khac_tu_sat_input.md) | input | Non_VG | S1 | S1-5 | P0 | nhan_van_xui_giuc_nguoi_khac_tu_sat_output | new_pending_review |
| [nhan_van_xui_giuc_nguoi_khac_tu_sat_output](new_intents/nhan_van_xui_giuc_nguoi_khac_tu_sat_output.md) | output | Non_VG | S1 | S1-5 | P0 | nhan_van_xui_giuc_nguoi_khac_tu_sat_input | new_pending_review |
| [chinh_tri_cong_kich_chinh_tri_gia_input](new_intents/chinh_tri_cong_kich_chinh_tri_gia_input.md) | input | Non_VG | S0 | S0-8 | P0 | chinh_tri_cong_kich_chinh_tri_gia_output | new_pending_review |
| [chinh_tri_cong_kich_chinh_tri_gia_output](new_intents/chinh_tri_cong_kich_chinh_tri_gia_output.md) | output | Non_VG | S0 | S0-8 | P0 | chinh_tri_cong_kich_chinh_tri_gia_input | new_pending_review |
| [chinh_tri_bi_mat_quoc_phong_input](new_intents/chinh_tri_bi_mat_quoc_phong_input.md) | input | Non_VG | S0 | — | P0 | chinh_tri_bi_mat_quoc_phong_output | new_pending_review |
| [chinh_tri_bi_mat_quoc_phong_output](new_intents/chinh_tri_bi_mat_quoc_phong_output.md) | output | Non_VG | S0 | — | P0 | chinh_tri_bi_mat_quoc_phong_input | new_pending_review |
| [van_hoa_chuan_muc_yeu_cau_noi_dung_trai_thuan_phong_my_tuc_input](../subprompts/van_hoa_chuan_muc_yeu_cau_noi_dung_trai_thuan_phong_my_tuc_input.md) | input | Non_VG | S2 | — | P2 | van_hoa_chuan_muc_noi_dung_trai_thuan_phong_my_tuc_output | new_pending_review |
| [van_hoa_chuan_muc_noi_dung_trai_thuan_phong_my_tuc_output](../subprompts/van_hoa_chuan_muc_noi_dung_trai_thuan_phong_my_tuc_output.md) | output | Non_VG | S2 | — | P1 | van_hoa_chuan_muc_yeu_cau_noi_dung_trai_thuan_phong_my_tuc_input | new_pending_review |

## Ghi chú theo intent

- `chinh_tri_boi_nho_lanh_dao_input`: Phạm vi: Phạm vi theo 1.02 S0-5: lãnh đạo Đảng/Nhà nước Việt Nam (tên trong sheet Danh sách thực thể hoặc chức danh được bảo vệ). Nhánh quốc tế của prompt 2.07 chuyển sang chinh_tri_cong_kich_chinh_tri_gia_input (1.02 xếp ở S0-8).
- `chinh_tri_boi_nho_lanh_dao_input`: 1.02 thắng: danh sách bảo vệ = sheet Danh sách thực thể của 1.02 (không theo danh sách chép trong prompt 2.07). Chính trị gia ngoài phạm vi intent này KHÔNG còn là 'không vi phạm' như prompt 2.07 ghi, mà thuộc chinh_tri_cong_kich_chinh_tri_gia_*.
- `chinh_tri_boi_nho_lanh_dao_output`: Phạm vi: Phạm vi theo 1.02 S0-5: lãnh đạo Đảng/Nhà nước Việt Nam. Nhánh quốc tế chuyển sang chinh_tri_cong_kich_chinh_tri_gia_output.
- `chinh_tri_boi_nho_lanh_dao_output`: 1.02 thắng: danh sách bảo vệ = sheet Danh sách thực thể của 1.02 (không theo danh sách chép trong prompt 2.07). Chính trị gia ngoài phạm vi intent này KHÔNG còn là 'không vi phạm' như prompt 2.07 ghi, mà thuộc chinh_tri_cong_kich_chinh_tri_gia_*.
- `nhan_van_che_tao_vu_khi_chat_no_input`: Mở rộng/giới hạn phạm vi: Phủ TOÀN BỘ mục S2-1 theo 1.02 (tiêu đề mục: 'Hướng dẫn chế tạo / SỬ DỤNG vũ khí, chất nổ'; STT 1.3 'mua bán, tàng trữ trái phép'), không chỉ khâu chế tạo như prompt 2.07.
- `nhan_van_che_tao_vu_khi_chat_no_output`: Mở rộng/giới hạn phạm vi: Phủ TOÀN BỘ mục S2-1 theo 1.02, gồm cả nhánh sử dụng và mua bán/tàng trữ. Lý do: prompt 2.07 chuyển mua bán vũ khí sang mua_ban_van_chuyen_hang_cam_output, intent đó chuyển ngược lại -> vòng lặp, không intent nào nhận.
- `nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input`: Thêm đối ứng nhan_van_gay_hai_nguoi_khac_output (mapping 7.1, 8.1, 9.1, 9.4); summary chỉ ghép bao_luc_gia_dinh_output.
- `nhan_van_tu_hai_input`: Phạm vi: Giữ 1.02 S1-5.1 và S1-6 (chủ thể là chính người dùng). STT 5.2 (xúi giục người khác) thuộc nhan_van_xui_giuc_nguoi_khac_tu_sat_input.
- `nhan_van_tu_hai_output`: Phạm vi: Giữ 1.02 S1-5.1 và S1-6. STT 5.2 thuộc nhan_van_xui_giuc_nguoi_khac_tu_sat_output.
- `phap_luat_mua_ban_van_chuyen_hang_cam_input`: Phạm vi: Giữ nguyên phạm vi 2.07 (hàng cấm NGOÀI ma túy và vũ khí). Vũ khí, vật liệu nổ thuộc nhan_van_che_tao_vu_khi_chat_no_input (đã mở rộng).
- `phap_luat_mua_ban_van_chuyen_hang_cam_output`: Phạm vi: Giữ nguyên phạm vi 2.07. Vũ khí, vật liệu nổ thuộc nhan_van_che_tao_vu_khi_chat_no_output (đã mở rộng).
- `su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_input`: Không thuộc mục 1.02 nào; giữ theo 2.07 (tầng: không gán).
- `su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_output`: Không thuộc mục 1.02 nào; giữ theo 2.07 (tầng: không gán).
- `vingroup_chinh_tri_output`: Strictness 2.07 ghi S0-13 (trượt hàng); sửa theo mapping: S0-14.
- `vingroup_noi_bo_output`: Strictness 2.07 ghi S0-11 (trượt hàng); sửa theo mapping: S0-15.
- `vingroup_tin_don_output`: Strictness 2.07 ghi S0-15 (trượt hàng); sửa theo mapping: S0-13.
- `nhan_van_xui_giuc_nguoi_khac_tu_sat_input`: Intent mới: phủ mục 1.02 chưa có intent; phạm vi lấy theo 1.02; chờ duyệt.
- `nhan_van_xui_giuc_nguoi_khac_tu_sat_output`: Intent mới: phủ mục 1.02 chưa có intent; phạm vi lấy theo 1.02; chờ duyệt.
- `chinh_tri_cong_kich_chinh_tri_gia_input`: Intent mới: phủ mục 1.02 chưa có intent; phạm vi lấy theo 1.02; chờ duyệt.
- `chinh_tri_cong_kich_chinh_tri_gia_input`: Phạm vi: Phủ 1.02 S0-8: MỌI chính trị gia trong nước (ngoài danh sách lãnh đạo được bảo vệ) và MỌI chính trị gia quốc tế - kể cả người có tên trong sheet thực thể. 2.07 giới hạn danh sách đóng -> 1.02 thắng.
- `chinh_tri_cong_kich_chinh_tri_gia_output`: Intent mới: phủ mục 1.02 chưa có intent; phạm vi lấy theo 1.02; chờ duyệt.
- `chinh_tri_cong_kich_chinh_tri_gia_output`: Phạm vi: Phủ 1.02 S0-8 ở chiều output, phạm vi như bản input.
- `chinh_tri_bi_mat_quoc_phong_input`: Intent mới từ Policy detail v2.08 (Overview 2.08: "Thêm intent"); dòng xlsx không có số ID (cột ID ghi "int" hoặc để trống).
- `chinh_tri_bi_mat_quoc_phong_input`: Không thuộc mục 1.02 nào (1.02 không có mục bí mật quốc phòng - an ninh; căn cứ gần nhất: Luật An ninh mạng 2025 cấm tiết lộ bí mật nhà nước, sheet tham chiếu dòng 12). Tầng S0 đề xuất theo Severity P0 và mặt bằng nhóm an ninh quốc gia; chờ người duyệt.
- `chinh_tri_bi_mat_quoc_phong_input`: Tên lệch trong xlsx: cột intent_name ghi "Chính trị_Bí mật quốc phòng_input (Politics_Defense_National_Security_Secrets_input)", khối [INTENT NAME] ghi "Chính trị_Bí mật quốc phòng an ninh_input (Politics_Defense_Security_Secrets_input)". Khóa lấy theo cột intent_name.
- `chinh_tri_bi_mat_quoc_phong_output`: Intent mới từ Policy detail v2.08 (Overview 2.08: "Thêm intent"); dòng xlsx không có số ID (cột ID ghi "int" hoặc để trống).
- `chinh_tri_bi_mat_quoc_phong_output`: Không thuộc mục 1.02 nào (1.02 không có mục bí mật quốc phòng - an ninh; căn cứ gần nhất: Luật An ninh mạng 2025 cấm tiết lộ bí mật nhà nước, sheet tham chiếu dòng 12). Tầng S0 đề xuất theo Severity P0 và mặt bằng nhóm an ninh quốc gia; chờ người duyệt.
- `chinh_tri_bi_mat_quoc_phong_output`: Khóa rút gọn thành chinh_tri_bi_mat_quoc_phong_output (tên xlsx: "…Bí mật quốc phòng an ninh_output") để cùng gốc với bản input.
- `van_hoa_chuan_muc_yeu_cau_noi_dung_trai_thuan_phong_my_tuc_input`: Lấy từ intents-robot-v2.8 (int_70); severity giữ theo bản Robot.
- `van_hoa_chuan_muc_yeu_cau_noi_dung_trai_thuan_phong_my_tuc_input`: Không thuộc mục 1.02 nào; căn cứ gần nhất: S2-3/3.2 "Nội dung đồi trụy, cổ súy dâm ô, trái thuần phong mỹ tục" (mục này đã map cho sexual_noi_dung_va_hoat_dong_khieu_dam_*, không đổi). Tầng S2 đề xuất theo mục đó; chờ người duyệt.
- `van_hoa_chuan_muc_noi_dung_trai_thuan_phong_my_tuc_output`: Lấy từ intents-robot-v2.8 (int_70); severity giữ theo bản Robot.
- `van_hoa_chuan_muc_noi_dung_trai_thuan_phong_my_tuc_output`: Không thuộc mục 1.02 nào; căn cứ gần nhất: S2-3/3.2 "Nội dung đồi trụy, cổ súy dâm ô, trái thuần phong mỹ tục" (mục này đã map cho sexual_noi_dung_va_hoat_dong_khieu_dam_*, không đổi). Tầng S2 đề xuất theo mục đó; chờ người duyệt.

## Sửa đổi so với mapping gốc

- S0-1 · 1.10 input: -chinh_tri_xuyen_tac_lich_su_input, +chu_quyen_cao_buoc_viet_nam_input — cao_buoc_viet_nam phủ đích danh Hiệp ước 1999/biên giới Tây Nam; xuyen_tac_lich_su không nói về biên giới
- S0-1 · 1.10 output: -chinh_tri_xuyen_tac_lich_su_output, +chu_quyen_cao_buoc_viet_nam_output — cao_buoc_viet_nam phủ đích danh Hiệp ước 1999/biên giới Tây Nam; xuyen_tac_lich_su không nói về biên giới
- S0-1 · 1.14 input: -chinh_tri_xuyen_tac_lich_su_input, +chu_quyen_cao_buoc_viet_nam_input — cao_buoc_viet_nam phủ đích danh Hiệp ước 1999/biên giới Tây Nam; xuyen_tac_lich_su không nói về biên giới
- S0-1 · 1.14 output: -chinh_tri_xuyen_tac_lich_su_output, +chu_quyen_cao_buoc_viet_nam_output — cao_buoc_viet_nam phủ đích danh Hiệp ước 1999/biên giới Tây Nam; xuyen_tac_lich_su không nói về biên giới
- S0-1 · 1.15 input: +chu_quyen_cao_buoc_viet_nam_input — cao_buoc_viet_nam phủ 'VN chiếm đất Campuchia', biên giới Tây Nam
- S0-1 · 1.15 output: +chu_quyen_cao_buoc_viet_nam_output — cao_buoc_viet_nam phủ 'VN chiếm đất Campuchia', biên giới Tây Nam
- S0-8 · 8.1 input: -chinh_tri_boi_nho_lanh_dao_input, +chinh_tri_cong_kich_chinh_tri_gia_input — 1.02 chia theo đối tượng: S0-5 = lãnh đạo Đảng/Nhà nước VN, S0-8 = chính trị gia (gồm quốc tế). boi_nho_lanh_dao giữ S0-5; intent mới phủ S0-8
- S0-8 · 8.1 output: -chinh_tri_boi_nho_lanh_dao_output, +chinh_tri_cong_kich_chinh_tri_gia_output — 1.02 chia theo đối tượng: S0-5 = lãnh đạo Đảng/Nhà nước VN, S0-8 = chính trị gia (gồm quốc tế). boi_nho_lanh_dao giữ S0-5; intent mới phủ S0-8
- S0-8 · 8.2 input: -chinh_tri_boi_nho_lanh_dao_input, +chinh_tri_cong_kich_chinh_tri_gia_input — 1.02 chia theo đối tượng: S0-5 = lãnh đạo Đảng/Nhà nước VN, S0-8 = chính trị gia (gồm quốc tế). boi_nho_lanh_dao giữ S0-5; intent mới phủ S0-8
- S0-8 · 8.2 output: -chinh_tri_boi_nho_lanh_dao_output, +chinh_tri_cong_kich_chinh_tri_gia_output — 1.02 chia theo đối tượng: S0-5 = lãnh đạo Đảng/Nhà nước VN, S0-8 = chính trị gia (gồm quốc tế). boi_nho_lanh_dao giữ S0-5; intent mới phủ S0-8
- S0-11 · 11.2 input: -vingroup_tin_don_input, +vingroup_vu_khong_input — quy kết cố ý lừa đảo/gian lận/thao túng thuộc vu khống (tin_don_input dòng 60,105)
- S0-11 · 11.2 output: -vingroup_tin_don_output, +vingroup_vu_khong_output — quy kết cố ý lừa đảo/gian lận/thao túng thuộc vu khống (tin_don_input dòng 60,105)
- S0-13 · 13.2 input: -vingroup_tay_chay_thuong_hieu_input, +vingroup_tin_don_input — giá/tiến độ/quy hoạch/pháp lý không nguồn = tin_don nhóm B2
- S0-13 · 13.2 output: -vingroup_tay_chay_thuong_hieu_output, +vingroup_tin_don_output — giá/tiến độ/quy hoạch/pháp lý không nguồn = tin_don nhóm B2
- S0-14 · 14.3 input: -vingroup_tay_chay_thuong_hieu_input, +vingroup_chinh_tri_input — chinh_tri_input Nhóm 4: so sánh với tập đoàn nhạy cảm chính trị
- S0-14 · 14.3 output: -vingroup_tay_chay_thuong_hieu_output, +vingroup_chinh_tri_output — chinh_tri_input Nhóm 4: so sánh với tập đoàn nhạy cảm chính trị
- S0-15 · 15.5 input: +vingroup_doi_tu_input — dữ liệu khách hàng nhận diện được cá nhân thuộc doi_tu
- S0-15 · 15.5 output: +vingroup_doi_tu_output — dữ liệu khách hàng nhận diện được cá nhân thuộc doi_tu
- S1-5 · 5.2 input: -nhan_van_tu_hai_input, +nhan_van_xui_giuc_nguoi_khac_tu_sat_input — tu_hai chỉ phủ chính người dùng; intent mới chờ duyệt
- S1-5 · 5.2 output: -nhan_van_tu_hai_output, +nhan_van_xui_giuc_nguoi_khac_tu_sat_output — tu_hai chỉ phủ chính người dùng; intent mới chờ duyệt
- S2-1 · 1.3 input: -phap_luat_mua_ban_van_chuyen_hang_cam_input, +nhan_van_che_tao_vu_khi_chat_no_input, +nhan_van_cong_cu_gay_hai_va_khong_che_input — mua_ban tự loại trừ vũ khí; che_tao_vu_khi mở rộng phủ mua bán/tàng trữ (1.3); cong_cu giữ nhánh tìm mua để hại người cụ thể
- S2-1 · 1.3 output: -phap_luat_mua_ban_van_chuyen_hang_cam_output, +nhan_van_che_tao_vu_khi_chat_no_output — 2.07 để hổng chiều output (hai intent chuyển vòng cho nhau); che_tao_vu_khi_output mở rộng phủ
- S2-1 · 1.1 input: +nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input — hợp từ Strictness 2.07 của CBRN input (nhánh vũ khí quy ước thương vong hàng loạt)
- S2-1 · 1.2 input: +nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input — hợp từ Strictness 2.07 của CBRN input (nhánh vũ khí quy ước thương vong hàng loạt)
- S2-4 · 4.1 output: +so_huu_tri_tue_tai_tao_noi_dung_output — 1.02 phủ cả đầu ra; dùng intent nháp sẵn có của 2.07 (ghi chú triển khai: 2.07 hiện chỉ bật đầu vào)
- S2-4 · 4.2 output: +so_huu_tri_tue_tai_tao_noi_dung_output — 1.02 phủ cả đầu ra; dùng intent nháp sẵn có của 2.07 (ghi chú triển khai: 2.07 hiện chỉ bật đầu vào)
- S2-4 · 4.3 output: +so_huu_tri_tue_tai_tao_noi_dung_output — 1.02 phủ cả đầu ra; dùng intent nháp sẵn có của 2.07 (ghi chú triển khai: 2.07 hiện chỉ bật đầu vào)
- S2-5 · 5.1 output: +phap_luat_vi_pham_quang_cao_output — 1.02 phủ cả đầu ra; dùng intent nháp sẵn có của 2.07 (ghi chú triển khai: 2.07 hiện chỉ bật đầu vào)
- S2-5 · 5.2 output: +phap_luat_vi_pham_quang_cao_output — 1.02 phủ cả đầu ra; dùng intent nháp sẵn có của 2.07 (ghi chú triển khai: 2.07 hiện chỉ bật đầu vào)
- S2-5 · 5.3 output: +phap_luat_vi_pham_quang_cao_output — 1.02 phủ cả đầu ra; dùng intent nháp sẵn có của 2.07 (ghi chú triển khai: 2.07 hiện chỉ bật đầu vào)
- S2-7 · 7.1 input: -jailbreak_input — jailbreak có business riêng
- S2-7 · 7.1 output: -jailbreak_output — jailbreak có business riêng
- S2-7 · 7.2 input: -jailbreak_input — jailbreak có business riêng
- S2-7 · 7.2 output: -jailbreak_output — jailbreak có business riêng
- S2-7 · 7.3 input: -jailbreak_input — jailbreak có business riêng
- S2-7 · 7.3 output: -jailbreak_output — jailbreak có business riêng
- S2-8 · 8.1 input: -prompt_injection_input — jailbreak có business riêng
- S2-8 · 8.1 output: -prompt_injection_output — jailbreak có business riêng
- S2-8 · 8.2 input: -prompt_injection_input — jailbreak có business riêng
- S2-8 · 8.2 output: -prompt_injection_output — jailbreak có business riêng

## Kiểm phủ 1.02

Mỗi STT của 1.02 phải có ít nhất một intent ở CẢ hai chiều. Bảng chỉ liệt kê STT chưa phủ.

**Đủ phủ**: tất cả STT ngoài phần loại trừ đều có intent ở cả hai chiều.

Loại trừ có chủ đích:

- S1-14: PII — phiên bản ViTa không áp dụng (ghi trong 1.02)
- S2-7: Jailbreak — business riêng `jailbreak/`
- S2-8: Prompt Injection — business riêng `jailbreak/`
