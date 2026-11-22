# Cao (tầng S1)

> Nguồn: `V-Guardrail_Mapping_Quy hoạch 1.02 với Chính sách chi tiết.xlsx` › sheet `Cao` (vùng A1:M42)

- **A1**: MỨC RỦI RO: CAO    |    Cam kết ≥ 95%
  - _ô gộp A1:M1_
- **A2**:

```text
Mức rủi ro cao tập trung vào các chủ đề có khả năng gây hậu quả nghiêm trọng, bao gồm đe dọa tính mạng con người, xâm hại trẻ em, cờ bạc/cá độ, lừa đảo và vi phạm bảo vệ dữ liệu cá nhân.
```

  - _ô gộp A2:M2_

**Tiêu đề cột (dòng 3)**

- **A3**: Số thứ tự
- **B3**: STT chi tiết
- **C3**: Danh mục
- **D3**: Ý định vi phạm
- **E3**: Nhóm nội dung
- **F3**: Mô tả (đã tách theo từng dòng)
- **G3**: Ánh xạ Bộ ý định chi tiết v2.05 - INPUT
- **H3**: Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT
- **I3**: Trạng thái rà soát
- **J3**: Từ khóa tham chiếu (dùng để nhận diện ý định)
- **K3**: Căn cứ pháp luật
- **L3**: Mức phạt / chế tài / rủi ro khủng hoảng truyền thông
- **M3**: So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025

<a id="s1-1"></a>
## S1-1 · Mục 1: Xâm hại trẻ em (CSAM)

- **A · Số thứ tự**: 1
  - _ô gộp A4:A7 — áp cho STT 1.1–1.4_
- **C · Danh mục**: Pháp luật
  - _ô gộp C4:C7 — áp cho STT 1.1–1.4_
- **D · Ý định vi phạm**: Xâm hại trẻ em (CSAM)
  - _ô gộp D4:D7 — áp cho STT 1.1–1.4_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp ĐỐI TƯỢNG (trẻ em, trẻ, bé, em bé, học sinh, thiếu nhi, vị thành niên, tuổi teen) với HÀNH VI (mọi thuật ngữ tình dục tường minh + dụ dỗ, rủ đi chơi một mình, đừng nói với bố mẹ)
```

  - _ô gộp J4:J7 — áp cho STT 1.1–1.4_
- **K · Căn cứ pháp luật**: Luật Trẻ em 2016; Luật ANM; BLHS
  - _ô gộp K4:K7 — áp cho STT 1.1–1.4_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS (Đ.142, 145, 146, 147)
  - _ô gộp L4:L7 — áp cho STT 1.1–1.4_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M4:M7 — áp cho STT 1.1–1.4_

<a id="s1-1-1"></a>
### 1.1 (dòng 4)

- **B · STT chi tiết**: 1.1
- **F · Mô tả (đã tách theo từng dòng)**: Nội dung tình dục hóa trẻ em (văn bản, hình ảnh, mô tả)
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_33 – CSAM_bảo vệ trẻ em_input (Illegal_CSAM_input)
  - ↳ [csam_bao_ve_tre_em_input](../detail/intents/csam_bao_ve_tre_em_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_11 – CSAM_bảo vệ trẻ em_output (Illegal_CSAM_output)
  - ↳ [csam_bao_ve_tre_em_output](../detail/intents/csam_bao_ve_tre_em_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-1-2"></a>
### 1.2 (dòng 5)

- **B · STT chi tiết**: 1.2
- **F · Mô tả (đã tách theo từng dòng)**: Tạo lập, chia sẻ, hướng dẫn tiếp cận nội dung xâm hại tình dục trẻ em
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_33 – CSAM_bảo vệ trẻ em_input (Illegal_CSAM_input)
  - ↳ [csam_bao_ve_tre_em_input](../detail/intents/csam_bao_ve_tre_em_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_11 – CSAM_bảo vệ trẻ em_output (Illegal_CSAM_output)
  - ↳ [csam_bao_ve_tre_em_output](../detail/intents/csam_bao_ve_tre_em_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-1-3"></a>
### 1.3 (dòng 6)

- **B · STT chi tiết**: 1.3
- **F · Mô tả (đã tách theo từng dòng)**: Dụ dỗ / grooming; tạo bí mật người lớn – trẻ em; cô lập trẻ khỏi người lớn tin cậy
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_33 – CSAM_bảo vệ trẻ em_input (Illegal_CSAM_input)
  - ↳ [csam_bao_ve_tre_em_input](../detail/intents/csam_bao_ve_tre_em_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_11 – CSAM_bảo vệ trẻ em_output (Illegal_CSAM_output)
  - ↳ [csam_bao_ve_tre_em_output](../detail/intents/csam_bao_ve_tre_em_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-1-4"></a>
### 1.4 (dòng 7)

- **B · STT chi tiết**: 1.4
- **F · Mô tả (đã tách theo từng dòng)**: Mọi biến thể, ẩn dụ, tiếng lóng che giấu nội dung trên
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_33 – CSAM_bảo vệ trẻ em_input (Illegal_CSAM_input)
  - ↳ [csam_bao_ve_tre_em_input](../detail/intents/csam_bao_ve_tre_em_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_11 – CSAM_bảo vệ trẻ em_output (Illegal_CSAM_output)
  - ↳ [csam_bao_ve_tre_em_output](../detail/intents/csam_bao_ve_tre_em_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-2"></a>
## S1-2 · Mục 2: Xâm phạm liêm chính bầu cử

- **A · Số thứ tự**: 2
  - _ô gộp A8:A11 — áp cho STT 2.1–2.4_
- **C · Danh mục**: Chính trị
  - _ô gộp C8:C11 — áp cho STT 2.1–2.4_
- **D · Ý định vi phạm**: Xâm phạm liêm chính bầu cử
  - _ô gộp D8:D11 — áp cho STT 2.1–2.4_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp PHẠM VI (bầu cử, ứng cử, Quốc hội, Hội đồng nhân dân, đại biểu, phiếu bầu, hòm phiếu, tổ bầu cử, danh sách cử tri, Hội đồng bầu cử quốc gia) với HÀNH VI (gian lận, làm giả phiếu, bỏ phiếu hộ, bỏ phiếu nhiều lần, mua phiếu, bán phiếu, ép bỏ phiếu, thao túng kết quả, tráo hòm phiếu, sửa kết quả, bầu cử là dàn dựng, đảng cử dân bầu, tẩy chay bầu cử, cản trở bỏ phiếu)
```

  - _ô gộp J8:J11 — áp cho STT 2.1–2.4_
- **K · Căn cứ pháp luật**: Luật Bầu cử ĐBQH và ĐB HĐND 2015; BLHS; Luật ANM
  - _ô gộp K8:K11 — áp cho STT 2.1–2.4_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS
  - _ô gộp L8:L11 — áp cho STT 2.1–2.4_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M8:M11 — áp cho STT 2.1–2.4_

<a id="s1-2-1"></a>
### 2.1 (dòng 8)

- **B · STT chi tiết**: 2.1
- **F · Mô tả (đã tách theo từng dòng)**: Khẳng định hoặc khuếch đại tin sai phủ nhận kết quả bầu cử
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_input (Politics_Election_Integrity_input)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_input](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_output (Politics_Election_Integrity_output)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_output](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-2-2"></a>
### 2.2 (dòng 9)

- **B · STT chi tiết**: 2.2
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn gian lận, thao túng, cản trở bầu cử
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_input (Politics_Election_Integrity_input)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_input](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_output (Politics_Election_Integrity_output)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_output](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-2-3"></a>
### 2.3 (dòng 10)

- **B · STT chi tiết**: 2.3
- **F · Mô tả (đã tách theo từng dòng)**: Vận động bỏ phiếu trái pháp luật, mua bán phiếu bầu
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_input (Politics_Election_Integrity_input)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_input](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_output (Politics_Election_Integrity_output)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_output](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-2-4"></a>
### 2.4 (dòng 11)

- **B · STT chi tiết**: 2.4
- **F · Mô tả (đã tách theo từng dòng)**: Tạo nội dung giả mạo cơ quan bầu cử, thông báo sai về địa điểm / thời gian bỏ phiếu
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_input (Politics_Election_Integrity_input)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_input](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_53 – Chính trị_xâm phạm liêm chính bầu cử_output (Politics_Election_Integrity_output)
  - ↳ [chinh_tri_xam_pham_liem_chinh_bau_cu_output](../detail/intents/chinh_tri_xam_pham_liem_chinh_bau_cu_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-3"></a>
## S1-3 · Mục 3: Tin đồn nội bộ Đảng, Nhà nước và tranh giành quyền lực

- **A · Số thứ tự**: 3
  - _ô gộp A12:A15 — áp cho STT 3.1–3.4_
- **C · Danh mục**: Chính trị
  - _ô gộp C12:C15 — áp cho STT 3.1–3.4_
- **D · Ý định vi phạm**: Tin đồn nội bộ Đảng, Nhà nước và tranh giành quyền lực
  - _ô gộp D12:D15 — áp cho STT 3.1–3.4_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp ĐỐI TƯỢNG (danh sách cán bộ lãnh đạo trong nước) với TIN ĐỒN QUYỀN LỰC (sắp bị bắt, sắp bị kỷ luật, bị ép từ chức, mất quyền lực, bị thất sủng, bị đưa vào tầm ngắm, phe cánh, vây cánh, đấu đá, thanh trừng, triệt hạ, hạ bệ, thâm cung bí sử, tin nội bộ, rò rỉ từ hội nghị) hoặc TIN ĐỒN SỨC KHỎE (ốm nặng, nhập viện, sắp chết, đã chết, tình trạng sức khỏe, không xuất hiện lâu rồi)
```

  - _ô gộp J12:J15 — áp cho STT 3.1–3.4_
- **K · Căn cứ pháp luật**: BLHS; Luật ANM; BLDS
  - _ô gộp K12:K15 — áp cho STT 3.1–3.4_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS
  - _ô gộp L12:L15 — áp cho STT 3.1–3.4_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M12:M15 — áp cho STT 3.1–3.4_

<a id="s1-3-1"></a>
### 3.1 (dòng 12)

- **B · STT chi tiết**: 3.1
- **F · Mô tả (đã tách theo từng dòng)**: Tin đồn đấu đá phe phái
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_26 – Chính trị_tin đồn nội bộ và quyền lực_input (Politics_Political_Rumor_and_Internal_Power_Disinformation_input)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_input](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_30 - Chính trị_tin đồn nội bộ và quyền lực_output (Politics_Political_Rumor_and_Internal_Power_Disinformation_output)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_output](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-3-2"></a>
### 3.2 (dòng 13)

- **B · STT chi tiết**: 3.2
- **F · Mô tả (đã tách theo từng dòng)**: Quy chụp công tác kỷ luật cán bộ là "thanh trừng chính trị"
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_26 – Chính trị_tin đồn nội bộ và quyền lực_input (Politics_Political_Rumor_and_Internal_Power_Disinformation_input)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_input](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_30 – Chính trị_tin đồn nội bộ và quyền lực_output (Politics_Political_Rumor_and_Internal_Power_Disinformation_output)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_output](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-3-3"></a>
### 3.3 (dòng 14)

- **B · STT chi tiết**: 3.3
- **F · Mô tả (đã tách theo từng dòng)**: Tin đồn ép từ chức, mất quyền lực, sắp bị bắt
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_26 – Chính trị_tin đồn nội bộ và quyền lực_input (Politics_Political_Rumor_and_Internal_Power_Disinformation_input)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_input](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_30 – Chính trị_tin đồn nội bộ và quyền lực_output (Politics_Political_Rumor_and_Internal_Power_Disinformation_output)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_output](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-3-4"></a>
### 3.4 (dòng 15)

- **B · STT chi tiết**: 3.4
- **F · Mô tả (đã tách theo từng dòng)**: Tin đồn về sức khỏe lãnh đạo
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_26 – Chính trị_tin đồn nội bộ và quyền lực_input (Politics_Political_Rumor_and_Internal_Power_Disinformation_input)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_input](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_30 – Chính trị_tin đồn nội bộ và quyền lực_output (Politics_Political_Rumor_and_Internal_Power_Disinformation_output)
  - ↳ [chinh_tri_tin_don_noi_bo_va_quyen_luc_output](../detail/intents/chinh_tri_tin_don_noi_bo_va_quyen_luc_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-4"></a>
## S1-4 · Mục 4: Tiết lộ / suy đoán đời tư chính trị gia

- **A · Số thứ tự**: 4
  - _ô gộp A16:A18 — áp cho STT 4.1–4.3_
- **C · Danh mục**: Chính trị
  - _ô gộp C16:C18 — áp cho STT 4.1–4.3_
- **D · Ý định vi phạm**: Tiết lộ / suy đoán đời tư chính trị gia
  - _ô gộp D16:D18 — áp cho STT 4.1–4.3_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp ĐỐI TƯỢNG (chính trị gia trong nước - xem sheet "Danh sách thực thể") với THÔNG TIN RIÊNG TƯ (nhà riêng, số điện thoại, lịch trình, trường của con, tài sản cá nhân, sức khỏe, đời tư, tài sản chưa kê khai, có bao nhiêu tiền, con học trường nào, quan hệ ngoài luồng với ai)
```

  - _ô gộp J16:J18 — áp cho STT 4.1–4.3_
- **K · Căn cứ pháp luật**: BLDS; Luật BVDLCN 2025
  - _ô gộp K16:K18 — áp cho STT 4.1–4.3_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử phạt VPHC đến 3 tỷ (tổ chức) / 1,5 tỷ (cá nhân).
  - _ô gộp L16:L18 — áp cho STT 4.1–4.3_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung thêm từ khoá
  - _ô gộp M16:M18 — áp cho STT 4.1–4.3_

<a id="s1-4-1"></a>
### 4.1 (dòng 16)

- **B · STT chi tiết**: 4.1
- **E · Nhóm nội dung**: Chặn tiết lộ / suy đoán thông tin của chính trị gia
- **F · Mô tả (đã tách theo từng dòng)**: Quan hệ cá nhân, đời sống riêng
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_44 – Chính trị_đời tư chính trị gia_input (Politics_Protected_Person_Privacy_input)
  - ↳ [chinh_tri_doi_tu_chinh_tri_gia_input](../detail/intents/chinh_tri_doi_tu_chinh_tri_gia_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_24 – Chính trị_đời tư chính trị gia_output (Politics_Protected_Person_Privacy_output)
  - ↳ [chinh_tri_doi_tu_chinh_tri_gia_output](../detail/intents/chinh_tri_doi_tu_chinh_tri_gia_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-4-2"></a>
### 4.2 (dòng 17)

- **B · STT chi tiết**: 4.2
- **E · Nhóm nội dung**: Chặn tiết lộ / suy đoán thông tin của chính trị gia
- **F · Mô tả (đã tách theo từng dòng)**: Tài sản chưa xác minh
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_44 – Chính trị_đời tư chính trị gia_input (Politics_Protected_Person_Privacy_input)
  - ↳ [chinh_tri_doi_tu_chinh_tri_gia_input](../detail/intents/chinh_tri_doi_tu_chinh_tri_gia_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_24 – Chính trị_đời tư chính trị gia_output (Politics_Protected_Person_Privacy_output)
  - ↳ [chinh_tri_doi_tu_chinh_tri_gia_output](../detail/intents/chinh_tri_doi_tu_chinh_tri_gia_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-4-3"></a>
### 4.3 (dòng 18)

- **B · STT chi tiết**: 4.3
- **E · Nhóm nội dung**: Chặn tiết lộ / suy đoán thông tin của chính trị gia
- **F · Mô tả (đã tách theo từng dòng)**: Gia đình, người thân
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_44 – Chính trị_đời tư chính trị gia_input (Politics_Protected_Person_Privacy_input)
  - ↳ [chinh_tri_doi_tu_chinh_tri_gia_input](../detail/intents/chinh_tri_doi_tu_chinh_tri_gia_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_24 – Chính trị_đời tư chính trị gia_output (Politics_Protected_Person_Privacy_output)
  - ↳ [chinh_tri_doi_tu_chinh_tri_gia_output](../detail/intents/chinh_tri_doi_tu_chinh_tri_gia_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-5"></a>
## S1-5 · Mục 5: Hướng dẫn tự tử / tự hại (phương thức)

- **A · Số thứ tự**: 5
  - _ô gộp A19:A20 — áp cho STT 5.1–5.2_
- **C · Danh mục**: Nhân văn
  - _ô gộp C19:C20 — áp cho STT 5.1–5.2_
- **D · Ý định vi phạm**: Hướng dẫn tự tử / tự hại (phương thức)
  - _ô gộp D19:D20 — áp cho STT 5.1–5.2_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp Ý ĐỊNH (cách tự tử, cách tự sát, làm sao để chết, cách kết thúc cuộc đời, cách tự làm đau, cách tự hại, how to kill myself, cách chết không đau, chết êm ái) với YÊU CẦU (liều lượng, bao nhiêu viên, uống bao nhiêu, trong bao lâu, cách nào chắc chắn, cách nào nhanh nhất)
```

  - _ô gộp J19:J20 — áp cho STT 5.1–5.2_
- **K · Căn cứ pháp luật**: BLHS
  - _ô gộp K19:K20 — áp cho STT 5.1–5.2_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS (Đ.131)
  - _ô gộp L19:L20 — áp cho STT 5.1–5.2_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M19:M20 — áp cho STT 5.1–5.2_

<a id="s1-5-1"></a>
### 5.1 (dòng 19)

- **B · STT chi tiết**: 5.1
- **F · Mô tả (đã tách theo từng dòng)**: Cung cấp cách thức, phương tiện để tự tử hoặc tự gây thương tích
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_48 – Nhân văn_tự hại_input (Humanity_SelfHarm_input)
  - ↳ [nhan_van_tu_hai_input](../detail/intents/nhan_van_tu_hai_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_52 – Nhân văn_tự hại_output (Humanity_SelfHarm_output)
  - ↳ [nhan_van_tu_hai_output](../detail/intents/nhan_van_tu_hai_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-5-2"></a>
### 5.2 (dòng 20)

- **B · STT chi tiết**: 5.2
- **F · Mô tả (đã tách theo từng dòng)**: Xúi giục, cổ vũ, hoặc giúp người khác tự sát
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_48 – Nhân văn_tự hại_input (Humanity_SelfHarm_input)
  - ↳ [nhan_van_tu_hai_input](../detail/intents/nhan_van_tu_hai_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_52 – Nhân văn_tự hại_output (Humanity_SelfHarm_output)
  - ↳ [nhan_van_tu_hai_output](../detail/intents/nhan_van_tu_hai_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-6"></a>
## S1-6 · Mục 6: Bộc lộ ý định self-harm / trầm cảm nặng

- **A · Số thứ tự**: 6
  - _ô gộp A21:A22 — áp cho STT 6.1–6.2_
- **C · Danh mục**: Nhân văn
  - _ô gộp C21:C22 — áp cho STT 6.1–6.2_
- **D · Ý định vi phạm**: Bộc lộ ý định self-harm / trầm cảm nặng
  - _ô gộp D21:D22 — áp cho STT 6.1–6.2_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Từ khóa đơn lẻ: muốn chết, không muốn sống, chán sống, sống làm gì nữa, mệt mỏi quá rồi, tuyệt vọng, không lối thoát, biến mất khỏi thế giới này, ngủ mãi không dậy, trầm cảm, không thiết tha gì, khóc suốt, mất ngủ triền miên, tự làm đau mình
```

  - _ô gộp J21:J22 — áp cho STT 6.1–6.2_
- **K · Căn cứ pháp luật**: Nghĩa vụ an toàn người dùng
  - _ô gộp K21:K22 — áp cho STT 6.1–6.2_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M21:M22 — áp cho STT 6.1–6.2_

<a id="s1-6-1"></a>
### 6.1 (dòng 21)

- **B · STT chi tiết**: 6.1
- **F · Mô tả (đã tách theo từng dòng)**: Bộc lộ ý định tự tử / tự hại (không yêu cầu phương thức)
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_48 – Nhân văn_tự hại_input (Humanity_SelfHarm_input)
  - ↳ [nhan_van_tu_hai_input](../detail/intents/nhan_van_tu_hai_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_52 – Nhân văn_tự hại_output (Humanity_SelfHarm_output)
  - ↳ [nhan_van_tu_hai_output](../detail/intents/nhan_van_tu_hai_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-6-2"></a>
### 6.2 (dòng 22)

- **B · STT chi tiết**: 6.2
- **F · Mô tả (đã tách theo từng dòng)**: Biểu hiện trầm cảm nặng, tuyệt vọng, cần trợ giúp
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_48 – Nhân văn_tự hại_input (Humanity_SelfHarm_input)
  - ↳ [nhan_van_tu_hai_input](../detail/intents/nhan_van_tu_hai_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_52 – Nhân văn_tự hại_output (Humanity_SelfHarm_output)
  - ↳ [nhan_van_tu_hai_output](../detail/intents/nhan_van_tu_hai_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-7"></a>
## S1-7 · Mục 7: Hướng dẫn gây hại nghiêm trọng cho người khác

- **A · Số thứ tự**: 7
  - _ô gộp A23:A25 — áp cho STT 7.1–7.3_
- **C · Danh mục**: Nhân văn
  - _ô gộp C23:C25 — áp cho STT 7.1–7.3_
- **D · Ý định vi phạm**: Hướng dẫn gây hại nghiêm trọng cho người khác
  - _ô gộp D23:D25 — áp cho STT 7.1–7.3_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp MỤC TIÊU (người, ai đó, hàng xóm, vợ, chồng, sếp, đồng nghiệp, nạn nhân) với HÀNH VI GÂY HẠI (cách giết, cách sát hại, cách đầu độc, cách gây thương tích, cách phóng hỏa, cách đốt nhà, cách phá hoại, cách làm hỏng phanh, cách cắt phanh, cách gây tai nạn, cách đâm xe, cách làm nổ lốp, cách vô hiệu hóa túi khí, cách theo dõi, cách khống chế)

Cụm đơn lẻ: thuốc độc không phát hiện được, cách gây tai nạn giả, cách phi tang chứng cứ/thi thể, cách xóa dấu vết hiện trường
Nhóm rủi ro trên xe: cách drift trên cao tốc, cách tắt ABS khi đang chạy, cách vô hiệu hóa hệ thống an toàn xe, thử thách nín thở trong xe, cách khóa trẻ trong xe, cách chạy xe ngược chiều
```

  - _ô gộp J23:J25 — áp cho STT 7.1–7.3_
- **K · Căn cứ pháp luật**: BLHS
  - _ô gộp K23:K25 — áp cho STT 7.1–7.3_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Khung rất nặng theo hành vi.
  - _ô gộp L23:L25 — áp cho STT 7.1–7.3_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M23:M25 — áp cho STT 7.1–7.3_

<a id="s1-7-1"></a>
### 7.1 (dòng 23)

- **B · STT chi tiết**: 7.1
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn gây thương tích, sát hại người khác
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_49 – Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input)
  - ↳ [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_34 – Nhân văn_gây hại người khác_output (Humanity_HarmOthers_output)
  - ↳ [nhan_van_gay_hai_nguoi_khac_output](../detail/intents/nhan_van_gay_hai_nguoi_khac_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-7-2"></a>
### 7.2 (dòng 24)

- **B · STT chi tiết**: 7.2
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn đầu độc, tấn công
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**:

```text
- int_10 – Nhân văn_đầu độc phóng hỏa phá hoại_input (Humanity_Poison_Arson_Sabotage_input)
- int_15 – Nhân văn_công cụ gây hại và khống chế_input (Humanity_HarmTool_Incapacitation_input)
```

  - ↳ [nhan_van_dau_doc_phong_hoa_pha_hoai_input](../detail/intents/nhan_van_dau_doc_phong_hoa_pha_hoai_input.md)
  - ↳ [nhan_van_cong_cu_gay_hai_va_khong_che_input](../detail/intents/nhan_van_cong_cu_gay_hai_va_khong_che_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_34 – Nhân văn_gây hại người khác_output (Humanity_HarmOthers_output)
  - ↳ [nhan_van_gay_hai_nguoi_khac_output](../detail/intents/nhan_van_gay_hai_nguoi_khac_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-7-3"></a>
### 7.3 (dòng 25)

- **B · STT chi tiết**: 7.3
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn hành vi gây nguy hiểm nghiêm trọng cho người khác
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**:

```text
- int_11 – Nhân văn_kỹ thuật rủi ro cao_input (Humanity_UnsafeHighRisk_Technical_input)
- int_49 – Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input)
```

  - ↳ [nhan_van_ky_thuat_rui_ro_cao_input](../detail/intents/nhan_van_ky_thuat_rui_ro_cao_input.md)
  - ↳ [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_34 – Nhân văn_gây hại người khác_output (Humanity_HarmOthers_output)
  - ↳ [nhan_van_gay_hai_nguoi_khac_output](../detail/intents/nhan_van_gay_hai_nguoi_khac_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-8"></a>
## S1-8 · Mục 8: Nội dung bạo lực gia đình / nạn nhân dễ tổn thương

<a id="s1-8-1"></a>
_STT chi tiết 8.1 — dòng 26_

- **A · Số thứ tự**: 8
- **B · STT chi tiết**: 8.1
- **C · Danh mục**: Nhân văn
- **D · Ý định vi phạm**: Nội dung bạo lực gia đình / nạn nhân dễ tổn thương
- **F · Mô tả (đã tách theo từng dòng)**: Nội dung cổ súy / hướng dẫn bạo lực gia đình, xâm hại thể chất / tinh thần
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_49 – Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input)
  - ↳ [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**:

```text
- int_10 – Nhân văn_bạo lực gia đình_output (Humanity_DomesticViolence_output)
- int_34 – Nhân văn_gây hại người khác_output (Humanity_HarmOthers_output)
```

  - ↳ [nhan_van_bao_luc_gia_dinh_output](../detail/intents/nhan_van_bao_luc_gia_dinh_output.md)
  - ↳ [nhan_van_gay_hai_nguoi_khac_output](../detail/intents/nhan_van_gay_hai_nguoi_khac_output.md)
- **I · Trạng thái rà soát**: Đã map
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp ĐỐI TƯỢNG (vợ, chồng, con, bố mẹ, người yêu, bạn đời, osin, người giúp việc, người già trong nhà) với HÀNH VI (cách trị vợ, cách dạy chồng, cách đánh không để lại dấu vết, cách nhốt, cách cấm ra khỏi nhà, cách tịch thu điện thoại, vợ hư thì phải, đàn ông có quyền đánh, đánh vợ là bình thường)
```

- **K · Căn cứ pháp luật**: Luật PCBLGĐ; BLHS
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS (Đ.134, Đ.140, Đ.185 - có thể phạt tù đến 20 năm)
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới

<a id="s1-9"></a>
## S1-9 · Mục 9: Thao túng tâm lý, kiểm soát cưỡng ép, che giấu bạo hành

- **A · Số thứ tự**: 9
  - _ô gộp A27:A30 — áp cho STT 9.1–9.4_
- **C · Danh mục**: Nhân văn
  - _ô gộp C27:C30 — áp cho STT 9.1–9.4_
- **D · Ý định vi phạm**: Thao túng tâm lý, kiểm soát cưỡng ép, che giấu bạo hành
  - _ô gộp D27:D30 — áp cho STT 9.1–9.4_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Độc lập hoặc kết hợp ĐỐI TƯỢNG (vợ, chồng, con, bố mẹ, người yêu, bạn đời, người tình, người phụ thuộc về kinh tế/công việc/quyền lực) với HÀNH VI (thao túng tâm lý; kiểm soát cưỡng ép; che giấu bạo hành – xóa dấu vết, ngụy trang thành, không để ai biết)
```

  - _ô gộp J27:J30 — áp cho STT 9.1–9.4_
- **K · Căn cứ pháp luật**: Luật Phòng, chống bạo lực gia đình 2022; BLHS; Luật Bình đẳng giới 2006
  - _ô gộp K27:K30 — áp cho STT 9.1–9.4_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS
  - _ô gộp L27:L30 — áp cho STT 9.1–9.4_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M27:M30 — áp cho STT 9.1–9.4_

<a id="s1-9-1"></a>
### 9.1 (dòng 27)

- **B · STT chi tiết**: 9.1
- **F · Mô tả (đã tách theo từng dòng)**: Gaslighting, thao túng tâm lý, cô lập, đe dọa, tạo lệ thuộc, tra tấn tinh thần
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_49 – Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input)
  - ↳ [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**:

```text
- int_10 – Nhân văn_bạo lực gia đình_output (Humanity_DomesticViolence_output)
- int_34 – Nhân văn_gây hại người khác_output (Humanity_HarmOthers_output)
```

  - ↳ [nhan_van_bao_luc_gia_dinh_output](../detail/intents/nhan_van_bao_luc_gia_dinh_output.md)
  - ↳ [nhan_van_gay_hai_nguoi_khac_output](../detail/intents/nhan_van_gay_hai_nguoi_khac_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-9-2"></a>
### 9.2 (dòng 28)

- **B · STT chi tiết**: 9.2
- **F · Mô tả (đã tách theo từng dòng)**: Che giấu bạo hành và ngăn nạn nhân tố cáo
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_49 – Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input)
  - ↳ [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_10 – Nhân văn_bạo lực gia đình_output (Humanity_DomesticViolence_output)
  - ↳ [nhan_van_bao_luc_gia_dinh_output](../detail/intents/nhan_van_bao_luc_gia_dinh_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-9-3"></a>
### 9.3 (dòng 29)

- **B · STT chi tiết**: 9.3
- **F · Mô tả (đã tách theo từng dòng)**: Biện minh bạo lực và đổ lỗi nạn nhân
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_49 – Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input)
  - ↳ [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_10 – Nhân văn_bạo lực gia đình_output (Humanity_DomesticViolence_output)
  - ↳ [nhan_van_bao_luc_gia_dinh_output](../detail/intents/nhan_van_bao_luc_gia_dinh_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-9-4"></a>
### 9.4 (dòng 30)

- **B · STT chi tiết**: 9.4
- **F · Mô tả (đã tách theo từng dòng)**: Hành vi không đồng thuận và quấy rối
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_49 – Nhân văn_gây hại và kiểm soát người khác_input (Humanity_HarmOthers_CoerciveControl_input)
  - ↳ [nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input](../detail/intents/nhan_van_gay_hai_va_kiem_soat_nguoi_khac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_34 - Nhân văn_gây hại người khác_output (Humanity_HarmOthers_output)
  - ↳ [nhan_van_gay_hai_nguoi_khac_output](../detail/intents/nhan_van_gay_hai_nguoi_khac_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-10"></a>
## S1-10 · Mục 10: Hướng dẫn sản xuất / điều chế ma túy

- **A · Số thứ tự**: 10
  - _ô gộp A31:A32 — áp cho STT 10.1–10.2_
- **C · Danh mục**: Pháp luật
  - _ô gộp C31:C32 — áp cho STT 10.1–10.2_
- **D · Ý định vi phạm**: Hướng dẫn sản xuất / điều chế ma túy
  - _ô gộp D31:D32 — áp cho STT 10.1–10.2_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp CHẤT (ma túy, ma túy đá, hàng đá, methamphetamine, meth, ketamine, ke, thuốc lắc, MDMA, LSD, heroin, cocaine, cần sa, cỏ, bóng cười, nước vui, nước biển, tem giấy, tiền chất) với HÀNH VI SẢN XUẤT (cách điều chế, cách tổng hợp, công thức, quy trình, cách nấu, cách chiết xuất, cách trồng, tỷ lệ pha, dung môi, cách tinh chế, yield, cách làm tại nhà)
```

  - _ô gộp J31:J32 — áp cho STT 10.1–10.2_
- **K · Căn cứ pháp luật**: BLHS
  - _ô gộp K31:K32 — áp cho STT 10.1–10.2_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS (Đ.248).
  - _ô gộp L31:L32 — áp cho STT 10.1–10.2_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M31:M32 — áp cho STT 10.1–10.2_

<a id="s1-10-1"></a>
### 10.1 (dòng 31)

- **B · STT chi tiết**: 10.1
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn sản xuất, điều chế, tổng hợp chất ma túy
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_36 – Pháp luật_sản xuất ma túy_input (Illegal_Drug_Production_input)
  - ↳ [phap_luat_san_xuat_ma_tuy_input](../detail/intents/phap_luat_san_xuat_ma_tuy_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_19 – Pháp luật_sản xuất ma túy_output (Illegal_Drug_Production_output)
  - ↳ [phap_luat_san_xuat_ma_tuy_output](../detail/intents/phap_luat_san_xuat_ma_tuy_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-10-2"></a>
### 10.2 (dòng 32)

- **B · STT chi tiết**: 10.2
- **F · Mô tả (đã tách theo từng dòng)**: Công thức, quy trình điều chế
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_36 – Pháp luật_sản xuất ma túy_input (Illegal_Drug_Production_input)
  - ↳ [phap_luat_san_xuat_ma_tuy_input](../detail/intents/phap_luat_san_xuat_ma_tuy_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_19 – Pháp luật_sản xuất ma túy_output (Illegal_Drug_Production_output)
  - ↳ [phap_luat_san_xuat_ma_tuy_output](../detail/intents/phap_luat_san_xuat_ma_tuy_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-11"></a>
## S1-11 · Mục 11: Hướng dẫn mua bán / vận chuyển ma túy

- **A · Số thứ tự**: 11
  - _ô gộp A33:A34 — áp cho STT 11.1–11.2_
- **C · Danh mục**: Pháp luật
  - _ô gộp C33:C34 — áp cho STT 11.1–11.2_
- **D · Ý định vi phạm**: Hướng dẫn mua bán / vận chuyển ma túy
  - _ô gộp D33:D34 — áp cho STT 11.1–11.2_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp CHẤT (như mục 10) với HÀNH VI GIAO DỊCH (mua/bán ở đâu, tìm nguồn, tìm mối, giá bao nhiêu, cách vận chuyển, cách giấu, cách qua trạm, cách qua chốt, cách tránh chó nghiệp vụ, cách đóng gói, cách dùng cho phê, dùng bao nhiêu để phê)
```

  - _ô gộp J33:J34 — áp cho STT 11.1–11.2_
- **K · Căn cứ pháp luật**: BLHS
  - _ô gộp K33:K34 — áp cho STT 11.1–11.2_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS (Đ.249, Đ.250, Đ.251).
  - _ô gộp L33:L34 — áp cho STT 11.1–11.2_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M33:M34 — áp cho STT 11.1–11.2_

<a id="s1-11-1"></a>
### 11.1 (dòng 33)

- **B · STT chi tiết**: 11.1
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn mua bán, vận chuyển, tàng trữ trái phép chất ma túy
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_58 – Pháp luật_mua bán vận chuyển hàng cấm_input (Illegal_Contraband_Trafficking_input)
  - ↳ [phap_luat_mua_ban_van_chuyen_hang_cam_input](../detail/intents/phap_luat_mua_ban_van_chuyen_hang_cam_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_59 – Pháp luật_mua bán vận chuyển hàng cấm_output (Illegal_Contraband_Trafficking_output)
  - ↳ [phap_luat_mua_ban_van_chuyen_hang_cam_output](../detail/intents/phap_luat_mua_ban_van_chuyen_hang_cam_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-11-2"></a>
### 11.2 (dòng 34)

- **B · STT chi tiết**: 11.2
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn cách sử dụng để lạm dụng
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_58 – Pháp luật_mua bán vận chuyển hàng cấm_input (Illegal_Contraband_Trafficking_input)
  - ↳ [phap_luat_mua_ban_van_chuyen_hang_cam_input](../detail/intents/phap_luat_mua_ban_van_chuyen_hang_cam_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_59 – Pháp luật_mua bán vận chuyển hàng cấm_output (Illegal_Contraband_Trafficking_output)
  - ↳ [phap_luat_mua_ban_van_chuyen_hang_cam_output](../detail/intents/phap_luat_mua_ban_van_chuyen_hang_cam_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-12"></a>
## S1-12 · Mục 12: Hướng dẫn tổ chức / tham gia cờ bạc trái phép

- **A · Số thứ tự**: 12
  - _ô gộp A35:A36 — áp cho STT 12.1–12.2_
- **C · Danh mục**: Pháp luật
  - _ô gộp C35:C36 — áp cho STT 12.1–12.2_
- **D · Ý định vi phạm**: Hướng dẫn tổ chức / tham gia cờ bạc trái phép
  - _ô gộp D35:D36 — áp cho STT 12.1–12.2_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp HÌNH THỨC (cá độ, cá cược, đánh bạc, lô đề, số đề, bóng đá + kèo, tài xỉu, baccarat, xóc đĩa, poker ăn tiền, game bài đổi thưởng, nổ hũ, slot, casino online) với HÀNH VI (cách chơi, cách bắt kèo, soi kèo, tỷ lệ kèo hôm nay, cách tổ chức, mở sòng, làm nhà cái, cách nạp tiền, link vào, trang uy tín, cách tránh bị bắt, cách chuyển tiền cược, app nào chơi được, cách dàn xếp tỷ số)
```

  - _ô gộp J35:J36 — áp cho STT 12.1–12.2_
- **K · Căn cứ pháp luật**: BLHS
  - _ô gộp K35:K36 — áp cho STT 12.1–12.2_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS (Đ.321, Đ.322)
  - _ô gộp L35:L36 — áp cho STT 12.1–12.2_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M35:M36 — áp cho STT 12.1–12.2_

<a id="s1-12-1"></a>
### 12.1 (dòng 35)

- **B · STT chi tiết**: 12.1
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn tổ chức đánh bạc trái phép
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_41 – Cờ bạc_input (Illegal_Gambling_input)
  - ↳ [co_bac_input](../detail/intents/co_bac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_12 – Cờ bạc_output (Illegal_Gambling_output)
  - ↳ [co_bac_output](../detail/intents/co_bac_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-12-2"></a>
### 12.2 (dòng 36)

- **B · STT chi tiết**: 12.2
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn tham gia, dàn xếp cờ bạc trái phép
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_41 – Cờ bạc_input (Illegal_Gambling_input)
  - ↳ [co_bac_input](../detail/intents/co_bac_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_12 – Cờ bạc_output (Illegal_Gambling_output)
  - ↳ [co_bac_output](../detail/intents/co_bac_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-13"></a>
## S1-13 · Mục 13: Hướng dẫn lừa đảo chiếm đoạt tài sản

- **A · Số thứ tự**: 13
  - _ô gộp A37:A38 — áp cho STT 13.1–13.2_
- **C · Danh mục**: Pháp luật
  - _ô gộp C37:C38 — áp cho STT 13.1–13.2_
- **D · Ý định vi phạm**: Hướng dẫn lừa đảo chiếm đoạt tài sản
  - _ô gộp D37:D38 — áp cho STT 13.1–13.2_
- **J · Từ khóa tham chiếu (dùng để nhận diện ý định)**:

```text
Kết hợp MỤC TIÊU / KÊNH (tin nhắn, SMS, email, website, fanpage, tổng đài, ngân hàng, tài khoản, thẻ tín dụng, OTP, mã xác thực, ví điện tử, app, khách hàng) với HÀNH VI LỪA ĐẢO (kịch bản lừa, cách lừa, cách scam, mẫu tin nhắn giả, giả danh, mạo danh, giả mạo tổng đài, cách lấy OTP, cách vượt OTP, cách chiếm tài khoản, cách hack tài khoản, tạo web giả, clone website, phishing, cách dụ chuyển tiền, cách moi thông tin, cách lấy CCCD của người khác)
```

  - _ô gộp J37:J38 — áp cho STT 13.1–13.2_
- **K · Căn cứ pháp luật**: BLHS
  - _ô gộp K37:K38 — áp cho STT 13.1–13.2_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử lý theo BLHS (Đ.174).
  - _ô gộp L37:L38 — áp cho STT 13.1–13.2_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M37:M38 — áp cho STT 13.1–13.2_

<a id="s1-13-1"></a>
### 13.1 (dòng 37)

- **B · STT chi tiết**: 13.1
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn kịch bản lừa đảo, giả mạo (scam)
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_38 – Pháp luật_lừa đảo chiếm đoạt tài sản_input (Illegal_Fraud_Scam_input)
  - ↳ [phap_luat_lua_dao_chiem_doat_tai_san_input](../detail/intents/phap_luat_lua_dao_chiem_doat_tai_san_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_21 – Pháp luật_lừa đảo chiếm đoạt tài sản_output (Illegal_Fraud_Scam_output)
  - ↳ [phap_luat_lua_dao_chiem_doat_tai_san_output](../detail/intents/phap_luat_lua_dao_chiem_doat_tai_san_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-13-2"></a>
### 13.2 (dòng 38)

- **B · STT chi tiết**: 13.2
- **F · Mô tả (đã tách theo từng dòng)**: Hướng dẫn chiếm đoạt tài sản qua mạng / viễn thông
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: - int_38 – Pháp luật_lừa đảo chiếm đoạt tài sản_input (Illegal_Fraud_Scam_input)
  - ↳ [phap_luat_lua_dao_chiem_doat_tai_san_input](../detail/intents/phap_luat_lua_dao_chiem_doat_tai_san_input.md)
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: - int_21 – Pháp luật_lừa đảo chiếm đoạt tài sản_output (Illegal_Fraud_Scam_output)
  - ↳ [phap_luat_lua_dao_chiem_doat_tai_san_output](../detail/intents/phap_luat_lua_dao_chiem_doat_tai_san_output.md)
- **I · Trạng thái rà soát**: Đã map

<a id="s1-14"></a>
## S1-14 · Mục 14: Phát hiện và Che PII định danh (CCCD, SĐT, email)

- **A · Số thứ tự**: 14
  - _ô gộp A39:A42 — áp cho STT 14.1–14.4_
- **C · Danh mục**: PII (Dữ liệu cá nhân)
  - _ô gộp C39:C42 — áp cho STT 14.1–14.4_
- **D · Ý định vi phạm**: Phát hiện và Che PII định danh (CCCD, SĐT, email)
  - _ô gộp D39:D42 — áp cho STT 14.1–14.4_
- **K · Căn cứ pháp luật**: Luật BVDLCN 2025 (91/2025) + NĐ 356/2025
  - _ô gộp K39:K42 — áp cho STT 14.1–14.4_
- **L · Mức phạt / chế tài / rủi ro khủng hoảng truyền thông**: Xử phạt VPHC đến 3 tỷ (tổ chức) / 1,5 tỷ (cá nhân).
  - _ô gộp L39:L42 — áp cho STT 14.1–14.4_
- **M · So sánh Chính sách từ khoá nhạy cảm Vivi đã được phê duyệt 26/06/2025**: Bổ sung mới
  - _ô gộp M39:M42 — áp cho STT 14.1–14.4_

<a id="s1-14-1"></a>
### 14.1 (dòng 39)

- **B · STT chi tiết**: 14.1
- **E · Nhóm nội dung**: Phát hiện & Che
- **F · Mô tả (đã tách theo từng dòng)**: Số CCCD / CMND
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **I · Trạng thái rà soát**: Đã map

<a id="s1-14-2"></a>
### 14.2 (dòng 40)

- **B · STT chi tiết**: 14.2
- **E · Nhóm nội dung**: Phát hiện & Che
- **F · Mô tả (đã tách theo từng dòng)**: Số điện thoại (VN & quốc tế)
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **I · Trạng thái rà soát**: Đã map

<a id="s1-14-3"></a>
### 14.3 (dòng 41)

- **B · STT chi tiết**: 14.3
- **E · Nhóm nội dung**: Phát hiện & Che
- **F · Mô tả (đã tách theo từng dòng)**: Địa chỉ email cá nhân
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **I · Trạng thái rà soát**: Đã map

<a id="s1-14-4"></a>
### 14.4 (dòng 42)

- **B · STT chi tiết**: 14.4
- **E · Nhóm nội dung**: Phát hiện & Che
- **F · Mô tả (đã tách theo từng dòng)**: Số tài khoản ngân hàng cá nhân (BỔ SUNG do rà soát)
- **G · Ánh xạ Bộ ý định chi tiết v2.05 - INPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **H · Ánh xạ Bộ ý định chi tiết v2.05 - OUTPUT**: Đã define ở tính năng PII nhưng phiên bản ViTa không apply tính năng detect PII
- **I · Trạng thái rà soát**: Đã map
