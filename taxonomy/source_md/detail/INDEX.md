# Mục lục file chi tiết (Policy detail v2.07 ForViTa)

> Nguồn: `V-Guardrail_Policy_detail_v2_07_ForViTa.xlsx`

Sheet phụ: [Keyword - Toxic](keyword_toxic.md) · [Keyword_General](keyword_general.md) · [summary intent](summary_intent.md)

## context_input_VG (7 dòng)

| intent_key | dòng | ID xlsx | intent_name | Severity | Strictness / Map |
|---|---|---|---|---|---|
| [vingroup_vu_khong_input](intents/vingroup_vu_khong_input.md) | 2 | int_30 | Vingroup_vu khống_input (Vingroup_Defamation_input) | P0 | S0-11 · Vu khống / cáo buộc phạm pháp - pháp nhân |
| [vingroup_xuc_pham_input](intents/vingroup_xuc_pham_input.md) | 3 | int_31 | Vingroup_xúc phạm_input (Vingroup_Insult_Harassment_input) | P0 | S0-12 · Chửi bới / hạ nhục / bôi nhọ lãnh đạo VG |
| [vingroup_tay_chay_thuong_hieu_input](intents/vingroup_tay_chay_thuong_hieu_input.md) | 4 | int_39 | Vingroup_tẩy chay thương hiệu_input (Vingroup_Brand_Boycott_input) | P0 | S0-13 · Kêu gọi tẩy chay / tiêu cực / ảnh hưởng uy tín thương hiệu |
| [vingroup_doi_tu_input](intents/vingroup_doi_tu_input.md) | 5 | int_40 | Vingroup_đời tư_input (Vingroup_Privacy_input) | P0 |  |
| [vingroup_chinh_tri_input](intents/vingroup_chinh_tri_input.md) | 6 | int_48 | Vingroup_chính trị_input (Vingroup_Political_Association_input) | P0 | S0-14 · Gán động cơ chính trị cho Vingroup |
| [vingroup_tin_don_input](intents/vingroup_tin_don_input.md) | 7 | int_49 | Vingroup_tin đồn_input (Vingroup_Rumor_input) | P0 | S0-13 · Kêu gọi tẩy chay / tiêu cực / ảnh hưởng uy tín thương hiệu |
| [vingroup_noi_bo_input](intents/vingroup_noi_bo_input.md) | 8 | int_50 | Vingroup_nội bộ_input (Vingroup_Internal_Confidential_input) | P0 | S0-15 · Tiết lộ thông tin nội bộ / bí mật kinh doanh Vingroup |

## context_output_VG (7 dòng)

| intent_key | dòng | ID xlsx | intent_name | Severity | Strictness / Map |
|---|---|---|---|---|---|
| [vingroup_xuc_pham_output](intents/vingroup_xuc_pham_output.md) | 2 | int_01 | Vingroup_xúc phạm_output (Vingroup_Insult_Harassment_output) | P0 | S0-12 · Chửi bới / hạ nhục / bôi nhọ lãnh đạo VG |
| [vingroup_doi_tu_output](intents/vingroup_doi_tu_output.md) | 3 | int_04 | Vingroup_đời tư_output (Vingroup_Privacy_output) | P0 |  |
| [vingroup_chinh_tri_output](intents/vingroup_chinh_tri_output.md) | 4 | int_03 | Vingroup_chính trị_output (Vingroup_Political_Association_output) | P0 | S0-13 · Kêu gọi tẩy chay / tiêu cực / ảnh hưởng uy tín thương hiệu |
| [vingroup_tin_don_output](intents/vingroup_tin_don_output.md) | 5 | int_05 | Vingroup_tin đồn_output (Vingroup_Rumor_output) | P0 | S0-15 · Tiết lộ thông tin nội bộ / bí mật kinh doanh Vingroup |
| [vingroup_noi_bo_output](intents/vingroup_noi_bo_output.md) | 6 | int_07 | Vingroup_nội bộ_output (Vingroup_Internal_Confidential_output) | P0 | S0-11 · Vu khống / cáo buộc phạm pháp - pháp nhân |
| [vingroup_tay_chay_thuong_hieu_output](intents/vingroup_tay_chay_thuong_hieu_output.md) | 7 | int_22 | Vingroup_tẩy chay thương hiệu_output (Vingroup_Brand_Boycott_output) | P0 | S0-13 · Kêu gọi tẩy chay / tiêu cực / ảnh hưởng uy tín thương hiệu |
| [vingroup_vu_khong_output](intents/vingroup_vu_khong_output.md) | 8 | int_17 | Vingroup_vu khống_output (Vingroup_Defamation_output) | P0 | S0-11 · Vu khống / cáo buộc phạm pháp |

## context_input_Non_VG (31 dòng)

| intent_key | dòng | ID xlsx | intent_name | Severity | Strictness / Map |
|---|---|---|---|---|---|
| [chu_quyen_kiem_soat_tren_thuc_te_input](intents/chu_quyen_kiem_soat_tren_thuc_te_input.md) | 2 | int_02 | Chủ quyền_kiểm soát trên thực tế_input (Sovereignty_DeFacto_Control_input) | P0 | S0-1 · Phủ nhận / khẳng định trái chủ quyền (đường lưỡi bò, Hoàng Sa - Trường Sa, Biển đông, Đường biên giới) |
| [nhan_van_che_tao_vu_khi_chat_no_input](intents/nhan_van_che_tao_vu_khi_chat_no_input.md) | 3 | int_09 | Nhân văn_chế tạo vũ khí chất nổ_input (Humanity_Weapon_Explosive_Device_input) | P0 | S2-1 · Hướng dẫn chế tạo / sử dụng vũ khí, chất nổ |
| [nhan_van_dau_doc_phong_hoa_pha_hoai_input](intents/nhan_van_dau_doc_phong_hoa_pha_hoai_input.md) | 4 | int_10 | Nhân văn_đầu độc phóng hỏa phá hoại_input (Humanity_Poison_Arson_Sabotage_input) | P0 | S1-7 · Hướng dẫn gây hại nghiêm trọng cho người khác |
| [nhan_van_ky_thuat_rui_ro_cao_input](intents/nhan_van_ky_thuat_rui_ro_cao_input.md) | 5 | int_11 | Nhân văn_kỹ thuật rủi ro cao_input (Humanity_UnsafeHighRisk_Technical_input) | P1 |  |
| [nhan_van_cong_cu_gay_hai_va_khong_che_input](intents/nhan_van_cong_cu_gay_hai_va_khong_che_input.md) | 6 | int_15 | Nhân văn_công cụ gây hại và khống chế_input (Humanity_HarmTool_Incapacitation_input) | P1 | S2-1 · Hướng dẫn chế tạo / sử dụng vũ khí, chất nổ (nhánh mua/kiếm vũ khí, thiết bị gây choáng) S1-7 · Hướng dẫn gây hại nghiêm trọng cho người khác (nhánh thuốc an thần/gây mê/hóa chất khống chế người khác) |
| [nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input](intents/nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input.md) | 7 | int_18 | Nhân văn_vũ khí hủy diệt hàng loạt CBRN_input (Humanity_CBRN_MassDestruction_input) | P0 | S2-6 · Vũ khí hủy diệt hàng loạt (CBRN) (nhánh CBRN) S2-1 · Hướng dẫn chế tạo / sử dụng vũ khí, chất nổ (nhánh vũ khí quy ước nhằm thương vong hàng loạt) |
| [chinh_tri_cong_kich_tinh_chinh_danh_the_che_input](intents/chinh_tri_cong_kich_tinh_chinh_danh_the_che_input.md) | 8 | int_20 | Chính trị_công kích tính chính danh thể chế_input (Politics_State_System_Legitimacy_Attack_input) | P0 | S0-6 · Công kích / bôi nhọ chế độ chính trị |
| [chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input](intents/chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_input.md) | 9 | int_21 | Chính trị_lật đổ và huy động chống Nhà nước_input (Politics_Regime_Change_and_Anti_State_Mobilization_input) | P0 | S0-4 · Kêu gọi lật đổ / phát tán tài liệu chống Nhà nước |
| [chinh_tri_xuyen_tac_lich_su_input](intents/chinh_tri_xuyen_tac_lich_su_input.md) | 10 | int_22 | Chính trị_xuyên tạc lịch sử_input (Politics_Historical_Revisionism_input) | P0 | S0-10 · Xuyên tạc / quy kết sai lịch sử tranh cãi |
| [chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input](intents/chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_input.md) | 11 | int_23 | Chính trị_biểu tượng và tuyên truyền chống chế độ_input (Politics_Anti_Regime_Symbols_and_Propaganda_input) | P0 | S0-4 · Kêu gọi lật đổ / phát tán tài liệu chống Nhà nước (nhánh tuyên truyền tài liệu chống Nhà nước) |
| [chinh_tri_tin_don_noi_bo_va_quyen_luc_input](intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_input.md) | 12 | int_26 | Chính trị_tin đồn nội bộ và quyền lực_input (Politics_Political_Rumor_and_Internal_Power_Disinformation_input) | P0 | S1-3 · Tin đồn nội bộ Đảng, Nhà nước và tranh giành quyền lực |
| [csam_bao_ve_tre_em_input](intents/csam_bao_ve_tre_em_input.md) | 13 | int_33 | CSAM_bảo vệ trẻ em_input (Illegal_CSAM_input) | P0 | S1-1 · Xâm hại trẻ em (CSAM) |
| [phap_luat_xam_pham_so_huu_tri_tue_input](intents/phap_luat_xam_pham_so_huu_tri_tue_input.md) | 14 | int_34 | Pháp luật_xâm phạm sở hữu trí tuệ_input (Illegal_IP_Infringement_input) | P0 | S2-4 · Vi phạm quyền sở hữu trí tuệ |
| [phap_luat_vi_pham_quang_cao_input](intents/phap_luat_vi_pham_quang_cao_input.md) | 15 | int_35 | Pháp luật_vi phạm quảng cáo_input (Illegal_Advertising_Violation_input) | P0 | S2-5 · Vi phạm quy định về quảng cáo |
| [phap_luat_san_xuat_ma_tuy_input](intents/phap_luat_san_xuat_ma_tuy_input.md) | 16 | int_36 | Pháp luật_sản xuất ma túy_input (Illegal_Drug_Production_input) | P0 | S1-10 · Hướng dẫn sản xuất / điều chế ma túy |
| [phap_luat_lua_dao_chiem_doat_tai_san_input](intents/phap_luat_lua_dao_chiem_doat_tai_san_input.md) | 17 | int_38 | Pháp luật_lừa đảo chiếm đoạt tài sản_input (Illegal_Fraud_Scam_input) | P0 | S1-13 · Hướng dẫn lừa đảo chiếm đoạt tài sản |
| [co_bac_input](intents/co_bac_input.md) | 18 | int_41 | Cờ bạc_input (Illegal_Gambling_input) | P0 | S1-12 · Hướng dẫn tổ chức / tham gia cờ bạc trái phép |
| [sexual_noi_dung_va_hoat_dong_khieu_dam_input](intents/sexual_noi_dung_va_hoat_dong_khieu_dam_input.md) | 19 | int_43 | Sexual_nội dung và hoạt động khiêu dâm_input (Sexual_Adult_Content_input) | P1 | S2-3 · NSFW - nội dung khiêu dâm người lớn |
| [chinh_tri_doi_tu_chinh_tri_gia_input](intents/chinh_tri_doi_tu_chinh_tri_gia_input.md) | 20 | int_44 | Chính trị_đời tư chính trị gia_input (Politics_Protected_Person_Privacy_input) | P0 | S1-4 · Tiết lộ / suy đoán đời tư chính trị gia |
| [chinh_tri_an_ninh_quoc_gia_input](intents/chinh_tri_an_ninh_quoc_gia_input.md) | 21 | int_45 | Chính trị_An ninh quốc gia_input (Politics_National_Security_input) | P0 | S0-4 · Kêu gọi lật đổ / phát tán tài liệu chống Nhà nước (nhánh kêu gọi lật đổ, tổ chức chống Nhà nước) |
| [chu_quyen_phan_xu_chu_quyen_input](intents/chu_quyen_phan_xu_chu_quyen_input.md) | 22 | int_46 | Chủ quyền_phán xử chủ quyền_input (Sovereignty_Adjudication_Request_input) | P0 | S0-1 · Phủ nhận / khẳng định trái chủ quyền (đường lưỡi bò, Hoàng Sa - Trường Sa, Biển đông, Đường biên giới) (khớp gạch đầu dòng "Kết luận 'bên khác sở hữu hợp pháp' trái lập trường VN") |
| [chu_quyen_cao_buoc_viet_nam_input](intents/chu_quyen_cao_buoc_viet_nam_input.md) | 23 | int_47 | Chủ quyền_cáo buộc Việt Nam_input (Sovereignty_Vietnam_Accusation_input) | P0 | S0-2 · Cáo buộc Việt Nam (chiếm đất / bán nước / xâm lược) |
| [chinh_tri_boi_nho_lanh_dao_input](intents/chinh_tri_boi_nho_lanh_dao_input.md) | 24 | int_55 | Chính trị_bôi nhọ lãnh đạo_input (Politics_Protected_Person_Defamation_input) | P0 | S0-5 · Vu khống lãnh đạo Đảng, Nhà nước (nhánh trong_nuoc) S0-8 · Công kích / hạ nhục chính trị gia (nhánh quoc_te) |
| [chinh_tri_xam_pham_liem_chinh_bau_cu_input](intents/chinh_tri_xam_pham_liem_chinh_bau_cu_input.md) | 25 | int_53 | Chính trị_xâm phạm liêm chính bầu cử_input (Politics_Election_Integrity_input) | P0 | S1-2 · Xâm phạm liêm chính bầu cử |
| [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md) | 26 | int_49 | Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input) | P1 | S1-7 · Hướng dẫn gây hại nghiêm trọng cho người khác (nhánh physical) S1-9 · Thao túng tâm lý, kiểm soát cưỡng ép, che giấu bạo hành (nhánh coercive, concealment, justification, quấy rối) S1-8 · Nội dung bạo lực gia đình / nạn nhân dễ tổn thương (nhánh nạn nhân trong gia đình) |
| [nhan_van_tu_hai_input](intents/nhan_van_tu_hai_input.md) | 27 | int_48 | Nhân văn_tự hại_input (Humanity_SelfHarm_input) | P1 | S1-5 · Hướng dẫn tự tử / tự hại (phương thức) (nhánh A - phương thức, nhánh C - liều gây chết) S1-6 · Bộc lộ ý định self-harm / trầm cảm nặng (nhánh B - bộc lộ ý định) |
| [chinh_tri_kich_dong_thu_han_va_chia_re_input](intents/chinh_tri_kich_dong_thu_han_va_chia_re_input.md) | 28 | int_56 | Chính trị_kích động thù hằn và chia rẽ_input (Politics_Hate_and_Division_Incitement_input) | P0 | S0-3 · Kích động xung đột chủ quyền (nhánh chu_quyen) S0-9 · Kích động chia rẽ dân tộc / tôn giáo (nhánh dan_toc, ton_giao, cong_dong, vung_mien) |
| [phap_luat_mua_ban_van_chuyen_hang_cam_input](intents/phap_luat_mua_ban_van_chuyen_hang_cam_input.md) | 29 | int_58 | Pháp luật_mua bán vận chuyển hàng cấm_input (Illegal_Contraband_Trafficking_input) | P0 | S1-11 · Hướng dẫn mua bán / vận chuyển ma túy (nhánh ma túy) S2-2 · Hướng dẫn mua bán hàng cấm (nhánh hàng cấm, hàng lậu) |
| [chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input](intents/chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_input.md) | 30 | int_52 | Chủ quyền_phủ nhận và khẳng định trái chủ quyền_input (Sovereignty_Denial_and_False_Claim_input) | P0 | S0-1 · Phủ nhận / khẳng định trái chủ quyền (đường lưỡi bò, Hoàng Sa - Trường Sa, Biển đông, Đường biên giới) |
| [su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_input](intents/su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_input.md) | 31 | int_62 | Sự kiện lịch sử nhạy cảm_yêu cầu nội dung_input(International_Political_Event_input) | P1 |  |
| [chinh_tri_xung_dot_chinh_tri_quoc_te_input](intents/chinh_tri_xung_dot_chinh_tri_quoc_te_input.md) | 32 | int_64 | Chính trị_xung đột Chính trị quốc tế_input (Politics_International_Conflict_input) | P0 |  |

## context_output_Non_VG (28 dòng)

| intent_key | dòng | ID xlsx | intent_name | Severity | Strictness / Map |
|---|---|---|---|---|---|
| [nhan_van_bao_luc_gia_dinh_output](intents/nhan_van_bao_luc_gia_dinh_output.md) | 3 | int_10 | Nhân văn_bạo lực gia đình_output (Humanity_DomesticViolence_output) | P1 | S1-8 · Nội dung bạo lực gia đình / nạn nhân dễ tổn thương S1 |
| [csam_bao_ve_tre_em_output](intents/csam_bao_ve_tre_em_output.md) | 4 | int_11 | CSAM_bảo vệ trẻ em_output (Illegal_CSAM_output) | P0 | S1-1 · Xâm hại trẻ em (CSAM) S1 |
| [co_bac_output](intents/co_bac_output.md) | 5 | int_12 | Cờ bạc_output (Illegal_Gambling_output) | P1 | S1-12 · Hướng dẫn tổ chức / tham gia cờ bạc trái phép S1 |
| [sexual_noi_dung_va_hoat_dong_khieu_dam_output](intents/sexual_noi_dung_va_hoat_dong_khieu_dam_output.md) | 6 | int_15 | Sexual_nội dung và hoạt động khiêu dâm_output (Sexual_Adult_Content_output) | P1 | S2-3 · NSFW - nội dung khiêu dâm người lớn S2 |
| [phap_luat_san_xuat_ma_tuy_output](intents/phap_luat_san_xuat_ma_tuy_output.md) | 7 | int_19 | Pháp luật_sản xuất ma túy_output (Illegal_Drug_Production_output) | P1 | S1-10 · Hướng dẫn sản xuất / điều chế ma túy S1 |
| [phap_luat_lua_dao_chiem_doat_tai_san_output](intents/phap_luat_lua_dao_chiem_doat_tai_san_output.md) | 8 | int_21 | Pháp luật_lừa đảo chiếm đoạt tài sản_output (Illegal_Fraud_Scam_output) | P1 | S1-13 · Hướng dẫn lừa đảo chiếm đoạt tài sản S1 |
| [chinh_tri_doi_tu_chinh_tri_gia_output](intents/chinh_tri_doi_tu_chinh_tri_gia_output.md) | 9 | int_24 | Chính trị_đời tư chính trị gia_output (Politics_Protected_Person_Privacy_output) | P0 | S1-4 · Tiết lộ / suy đoán đời tư chính trị gia S1 |
| [chinh_tri_xuyen_tac_lich_su_output](intents/chinh_tri_xuyen_tac_lich_su_output.md) | 10 | int_25 | Chính trị_xuyên tạc lịch sử_output (Politics_Historical_Revisionism_output) | P0 | S0-10 · Xuyên tạc / quy kết sai lịch sử tranh cãi S0 |
| [chinh_tri_an_ninh_quoc_gia_output](intents/chinh_tri_an_ninh_quoc_gia_output.md) | 11 | int_26 | Chính trị_An ninh quốc gia_output (Politics_National_Security_output) | P0 | S0-4 · Kêu gọi lật đổ / phát tán tài liệu chống Nhà nước (nhánh lật đổ, tổ chức chống Nhà nước) S0 |
| [chinh_tri_cong_kich_tinh_chinh_danh_the_che_output](intents/chinh_tri_cong_kich_tinh_chinh_danh_the_che_output.md) | 12 | int_27 | Chính trị_công kích tính chính danh thể chế_output (Politics_State_System_Legitimacy_Attack_output) | P0 | S0-6 · Công kích / bôi nhọ chế độ chính trị S0 |
| [chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output](intents/chinh_tri_lat_do_va_huy_dong_chong_nha_nuoc_output.md) | 13 | int_28 | Chính trị_lật đổ và huy động chống Nhà nước_output (Politics_Regime_Change_and_Anti_State_Mobilization_output) | P0 | S0-4 · Kêu gọi lật đổ / phát tán tài liệu chống Nhà nước S0 |
| [chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output](intents/chinh_tri_bieu_tuong_va_tuyen_truyen_chong_che_do_output.md) | 14 | int_29 | Chính trị_biểu tượng và tuyên truyền chống chế độ_output (Politics_Anti_Regime_Symbols_and_Propaganda_output) | P0 | S0-4 · Kêu gọi lật đổ / phát tán tài liệu chống Nhà nước (nhánh tuyên truyền chống Nhà nước) S0 |
| [chinh_tri_tin_don_noi_bo_va_quyen_luc_output](intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_output.md) | 15 | int_30 | Chính trị_tin đồn nội bộ và quyền lực_output (Politics_Political_Rumor_and_Internal_Power_Disinformation_output) | P0 | S1-3 · Tin đồn nội bộ Đảng, Nhà nước và tranh giành quyền lực S1 |
| [nhan_van_che_tao_vu_khi_chat_no_output](intents/nhan_van_che_tao_vu_khi_chat_no_output.md) | 16 | int_33 | Nhân văn_chế tạo vũ khí chất nổ_output (Humanity_Weapon_Explosive_Device_output) | P0 | S2-1 · Hướng dẫn chế tạo / sử dụng vũ khí, chất nổ S2 |
| [nhan_van_gay_hai_nguoi_khac_output](intents/nhan_van_gay_hai_nguoi_khac_output.md) | 17 | int_34 | Nhân văn_gây hại người khác_output (Humanity_HarmOthers_output) | P0 | S1-7 · Hướng dẫn gây hại nghiêm trọng cho người khác S1 |
| [chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output](intents/chu_quyen_phu_nhan_va_khang_dinh_trai_chu_quyen_output.md) | 18 | int_36 | Chủ quyền_phủ nhận và khẳng định trái chủ quyền_output (Sovereignty_Denial_and_False_Claim_output) | P0 | S0-1 · Phủ nhận / khẳng định trái chủ quyền (đường lưỡi bò, Hoàng Sa - Trường Sa, Biển đông, Đường biên giới) S0 |
| [chu_quyen_cao_buoc_viet_nam_output](intents/chu_quyen_cao_buoc_viet_nam_output.md) | 19 | int_37 | Chủ quyền_cáo buộc Việt Nam_output (Sovereignty_Vietnam_Accusation_output) | P0 | S0-2 · Cáo buộc Việt Nam (chiếm đất / bán nước / xâm lược) S0 |
| [chu_quyen_phan_xu_chu_quyen_output](intents/chu_quyen_phan_xu_chu_quyen_output.md) | 20 | int_39 | Chủ quyền_phán xử chủ quyền_output (Sovereignty_Adjudication_output) | P0 | S0-1 · Phủ nhận / khẳng định trái chủ quyền (đường lưỡi bò, Hoàng Sa - Trường Sa, Biển đông, Đường biên giới) (khớp gạch đầu dòng "Kết luận 'bên khác sở hữu hợp pháp' trái lập trường VN") S0 |
| [nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output](intents/nhan_van_vu_khi_huy_diet_hang_loat_cbrn_output.md) | 21 | int_40 | Nhân văn_vũ khí hủy diệt hàng loạt CBRN_output (Humanity_CBRN_MassDestruction_output) | P0 | S2-6 · Vũ khí hủy diệt hàng loạt (CBRN) S2 |
| [chinh_tri_xung_dot_chinh_tri_quoc_te_output](intents/chinh_tri_xung_dot_chinh_tri_quoc_te_output.md) | 22 | int_43 | Chính trị_xung đột chính trị quốc tế_output (Politics_International_Conflict_output) | P0 | S0-7 · Xung đột quốc tế S0 |
| [chinh_tri_boi_nho_lanh_dao_output](intents/chinh_tri_boi_nho_lanh_dao_output.md) | 23 | int_55 | Chính trị_bôi nhọ lãnh đạo_output (Politics_Protected_Person_Defamation_output) | P0 | S0-5 · Vu khống lãnh đạo Đảng, Nhà nước (nhánh trong_nuoc) S0-8 · Công kích / hạ nhục chính trị gia (nhánh quoc_te) S0 |
| [chinh_tri_xam_pham_liem_chinh_bau_cu_output](intents/chinh_tri_xam_pham_liem_chinh_bau_cu_output.md) | 24 | int_53 | Chính trị_xâm phạm liêm chính bầu cử_output (Politics_Election_Integrity_output) | P0 | S1-2 · Xâm phạm liêm chính bầu cử S1 |
| [nhan_van_tu_hai_output](intents/nhan_van_tu_hai_output.md) | 25 | int_52 | Nhân văn_tự hại_output (Humanity_SelfHarm_output) | P1 | S1-5 · Hướng dẫn tự tử / tự hại (phương thức) S1 |
| [chinh_tri_kich_dong_thu_han_va_chia_re_output](intents/chinh_tri_kich_dong_thu_han_va_chia_re_output.md) | 26 | int_56 | Chính trị_kích động thù hằn và chia rẽ_output (Politics_Hate_and_Division_Incitement_output) | P0 | S0-3 · Kích động xung đột chủ quyền (nhánh chu_quyen) S0-9 · Kích động chia rẽ dân tộc / tôn giáo (nhánh dan_toc, ton_giao, cong_dong, vung_mien) S0 |
| [phap_luat_mua_ban_van_chuyen_hang_cam_output](intents/phap_luat_mua_ban_van_chuyen_hang_cam_output.md) | 27 | int_59 | Pháp luật_mua bán vận chuyển hàng cấm_output (Illegal_Contraband_Trafficking_output) | P0 | S1-11 · Hướng dẫn mua bán / vận chuyển ma túy (nhánh ma túy) S2-2 · Hướng dẫn mua bán hàng cấm (nhánh hàng cấm, hàng lậu) S1 / S2 |
| [su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_output](intents/su_kien_lich_su_nhay_cam_yeu_cau_noi_dung_output.md) | 28 | int_62 | Sự kiện lịch sử nhạy cảm_yêu cầu nội dung_output(International_Political_Event_output) | P1 |  |
| [so_huu_tri_tue_tai_tao_noi_dung_output](intents/so_huu_tri_tue_tai_tao_noi_dung_output.md) | 29 | — | Sở hữu trí tuệ_tái tạo nội dung_output (Intellectual_Property_Reproduction_output) | P0 |  |
| [phap_luat_vi_pham_quang_cao_output](intents/phap_luat_vi_pham_quang_cao_output.md) | 30 | — | Pháp luật_vi phạm quảng cáo_output (Illegal_Advertising_Violation_output) | P0 |  |

## JailbreakPrompt Injection (4 dòng)

| intent_key | dòng | ID xlsx | intent_name | Severity | Strictness / Map |
|---|---|---|---|---|---|
| [jailbreak_input](intents/jailbreak_input.md) | 2 | FN_01 | Jailbreak_input | P0 | S3-9 · Bẻ khóa (Jailbreak) S3 |
| [prompt_injection_input](intents/prompt_injection_input.md) | 3 | FN_02 | Prompt Injection_Input |  | S3-10 · Tiêm lệnh (Prompt Injection) S3 |
| [jailbreak_output](intents/jailbreak_output.md) | 4 | FN_03 | Jailbreak_Output | P0 | S3-9 · Bẻ khóa (Jailbreak) S3 |
| [prompt_injection_output](intents/prompt_injection_output.md) | 5 | FN_04 | Prompt Injection_Output | P0 | S3-10 · Tiêm lệnh (Prompt Injection) S3 |
