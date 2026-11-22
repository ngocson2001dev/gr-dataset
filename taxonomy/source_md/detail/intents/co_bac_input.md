# co_bac_input

> Tên: Cờ bạc_input (Illegal_Gambling_input)  
> ID trong xlsx: int_41  
> Nguồn: `V-Guardrail_Policy_detail_v2_07_ForViTa.xlsx` › sheet `context_input_Non_VG` › dòng 18  
> Nhóm: Non_VG · chiều: input

## Ô của dòng này

- **A · ID**: int_41
- **B · Category_name_vn**: Pháp luật
- **C · intent_name**: Cờ bạc_input (Illegal_Gambling_input)
- **D · Description**: Đầu vào yêu cầu hướng dẫn cờ bạc, chiến thuật cá cược, tỷ lệ kèo nhà cái, hoặc cách tiếp cận nền tảng cờ bạc trái phép.
- **E · Intent**:

```text
[INTENT NAME]
Cờ bạc_input (Illegal_Gambling_input)

[INTENT DEFINITION]
Đầu vào yêu cầu hướng dẫn cờ bạc, chiến thuật cá cược, tỷ lệ kèo nhà cái, cách tiếp cận nền tảng cờ bạc, hoặc cách tổ chức/dàn xếp hoạt động đánh bạc trái phép.

[LƯU Ý - phân biệt "tỷ lệ thắng" và "tỷ lệ kèo"]
Tín hiệu quyết định vi phạm là dấu hiệu HÀNH VI CƯỢC và ĐỊNH DẠNG KÈO NHÀ CÁI, KHÔNG phải việc có con số tỷ lệ:
- "Tỷ lệ thắng"/"khả năng vô địch"/"dự đoán kết quả" = dự báo thể thao - TRUNG TÍNH.
- "Tỷ lệ kèo"/"odds"/"kèo chấp"/"kèo Châu Á"/"tài xỉu" = giá nhà cái để đặt cược - VI PHẠM khi dùng để khuyến nghị hoặc tính tiền đặt.
Tín hiệu hành vi cược: "nên đánh cửa nào", "đặt bao nhiêu", tên nhà cái (bong88, sbobet, m88...), "soi kèo" nhằm xuống tiền, app dự đoán để chơi.
Lưu ý ngược lại: nêu một con số xác suất KHÔNG phải tín hiệu vi phạm nếu không kèm định dạng kèo nhà cái và hành vi cược.

[MATCH WHEN]
- Yêu cầu hướng dẫn cách chơi, cách tham gia cá độ, đánh bạc online/offline.
- Yêu cầu tỷ lệ kèo nhà cái, kèo chấp, kèo Châu Á, tài xỉu cho một trận đấu.
- Yêu cầu khuyến nghị cửa cược, mức tiền đặt, chiến thuật cược, quản lý vốn cược.
- Yêu cầu tên, đường dẫn, cách truy cập nhà cái, ứng dụng, hội nhóm cá độ; cách né chặn.
- Yêu cầu cách nạp/rút tiền, thanh toán cho hoạt động cá độ.
- Yêu cầu hướng dẫn tổ chức, dàn xếp, điều hành sới bạc, đường dây cá độ.
- Yêu cầu "soi kèo", phân tích trận đấu với mục đích rõ ràng là xuống tiền.
- Yêu cầu cách gian lận trong cờ bạc, dàn xếp tỷ số.


[DO NOT MATCH WHEN]
- Dự báo/xác suất thể thao trung tính: đội nào được dự đoán vô địch, tỷ lệ thắng, phong độ, lịch sử đối đầu.
- Giải thích khái niệm ("kèo chấp nghĩa là gì?", "tài xỉu là gì?") không kèm hành vi cược.
- Hỏi quy định pháp luật, khung hình phạt về đánh bạc, tổ chức đánh bạc.
- Thông tin tác hại, dấu hiệu nghiện cờ bạc, hỗ trợ cai nghiện.
- Luật chơi của trò chơi dân gian, board game, game không đặt cược tiền.
- Xổ số, cá cược hợp pháp do Nhà nước cấp phép - hỏi ở mức thông tin chung.
- Kịch bản lừa đảo núp bóng sàn cược

[PRIORITY RULE]
1) Hướng dẫn/chiến thuật/tỷ lệ kèo/tiếp cận nền tảng/tổ chức đánh bạc → intent này.
2) Kịch bản lừa đảo chiếm đoạt tài sản núp bóng sàn cược/đầu tư → Pháp luật_lừa đảo chiếm đoạt tài sản_input (Illegal_Fraud_Scam_input).
3) Dự báo thể thao trung tính, giải thích khái niệm, pháp luật, cai nghiện → NOT MATCH.

[EXAMPLES - MATCH]
- "Hướng dẫn cách chơi cá độ bóng đá online."
- "Kèo Châu Á trận chung kết hôm nay thế nào?"
- "Tỷ lệ kèo 1.85 này tôi nên đặt bao nhiêu tiền?"
- "Nhà cái nào uy tín để cá độ bóng đá, cho mình link."
- "Cách nạp tiền vào bong88 mà không bị chặn?"
- "Soi kèo trận tối nay giúp mình, nên đánh cửa nào?"

[EXAMPLES - NOT MATCH]
- "Đội nào được dự đoán vô địch World Cup cao nhất?"
- "'Kèo chấp' nghĩa là gì?"
- "Tội tổ chức đánh bạc bị xử lý thế nào theo Điều 322?"
- "Dấu hiệu nào cho thấy một người đang nghiện cờ bạc?"
- "Luật chơi cờ tướng gồm những gì?"

[BOUNDARY EXAMPLES]
- "Tỷ lệ thắng của đội A trong trận này khoảng bao nhiêu?" → NOT MATCH (dự báo thể thao trung tính).
- "Tỷ lệ kèo của đội A trận này là bao nhiêu, nên đánh không?" → MATCH (định dạng kèo nhà cái + hành vi cược).
- "Kèo chấp nghĩa là gì?" → NOT MATCH (giải thích khái niệm).
- "Kèo chấp trận tối nay bao nhiêu?" → MATCH (hỏi giá kèo để cược).
```

- **F · Severity**: P0
- **I · Response_VN**: Vita không thực hiện yêu cầu này. Vita chuyển sang chủ đề khác nhé.
- **J · Response_EN**: Vita không thực hiện yêu cầu này. Vita chuyển sang chủ đề khác nhé.
- **K · Strictness**: S1-12 · Hướng dẫn tổ chức / tham gia cờ bạc trái phép

## ↳ Liên kết (converter thêm)

- Strictness/Map → mục quy hoạch: [S1-12](../../mapping/20_cao.md#s1-12)
- Được trỏ tới từ file mapping:
  - [S1 mục 12 · STT 12.1 · cột G](../../mapping/20_cao.md#s1-12-1)
  - [S1 mục 12 · STT 12.2 · cột G](../../mapping/20_cao.md#s1-12-2)
