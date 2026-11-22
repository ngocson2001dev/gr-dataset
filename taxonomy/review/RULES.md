# Quy tắc tạo subprompt cho mọi intent

Một intent = một file `<intent_key>.md` trong `../subprompts/`. Thư mục này (`review/`) chứa quy tắc, script và file Excel review (danh sách cặp ở `../intent_taxonomy/pairs.json`). Mẫu chuẩn: `phap_luat_san_xuat_ma_tuy_input.md` và `_output.md`. Subprompt được inject vào `generator/prompts/cell.j2`; người đọc là một LLM khác chưa có bất kỳ context nào.

## A. Quy trình mỗi intent

1. **Đọc**: file đặc tả ở `../source_md/detail/intents/<intent_key>.md` (cột Intent), mục 1.02 tương ứng (`../intent_taxonomy/taxonomy.json` → `muc`, `norms`) trong `../source_md/mapping/`.
2. **Vòng 1, đối chiếu 1.02** (lý do giữ/bỏ ghi vào cột "Ghi chú của người review" của Excel hoặc báo cho người duyệt):
   - Giữ nội dung 2.07 nếu **cùng lĩnh vực** với mục 1.02, dù từ khóa không có trong 1.02. Hai bản bổ sung cho nhau.
   - Bỏ nội dung chỉ khi nó thuộc **mục khác** của 1.02 hoặc sai lĩnh vực. Ghi lý do.
   - Thêm từ 1.02 những gì 2.07 thiếu: từ khóa, tên lóng, biến thể, STT chưa được phủ.
   - Mâu thuẫn giữa hai bản: **1.02 thắng** (phạm vi, tầng, danh sách thực thể).
3. **Vòng 2, gọn cho LLM ngoài**: áp mục B và C. Mục tiêu: giữ đủ ngữ cảnh với ít token nhất.
4. **Kiểm tra**: `python3 generator/generate.py --pairs <pair> --N 1 --dry-run` (prompt ra ở `generator/logs/dry/`), đọc prompt cuối của đủ 4 ô, không còn cảnh báo, rồi tick mục F.
5. **Review**: xuất Excel bằng `python3 taxonomy/review/export_review.py` (mục I); người duyệt điền cột "Quyết định" và ghi chú, sau đó sửa `.md` theo review và xuất lại.
6. Người duyệt chốt từng nhóm; chỉ sau đó mới sang nhóm tiếp.

## B. Cấu trúc file (các header `##` cố định)

| Header | Bắt buộc | Quy tắc |
|---|---|---|
| Chủ đề | có | MỘT đoạn **trung lập**, gộp cả chủ đề lẫn mô tả: chỉ nói intent này nói về cái gì (lĩnh vực, đối tượng, phạm vi). **KHÔNG** phán xét vi phạm hay an toàn, **KHÔNG** viết như hành vi vi phạm ("Hướng dẫn…", "Trợ lý hướng dẫn…"), **KHÔNG** có ví dụ, vì đoạn này dùng chung cho ô vi phạm lẫn ô an toàn. Mọi quy định vi phạm hay không (khung bọc có cứu được không, điều kiện đồng thời, phép thử) nằm ở "Vi phạm khi" và "Không vi phạm khi". Không dùng tên intent, mã, tiền tố "Pháp luật_". Prompt không còn mục "Định nghĩa" riêng. |
| Vi phạm khi | có | 5–9 gạch đầu dòng, mỗi dòng một hành vi cụ thể. Input bắt đầu bằng "Hỏi/Yêu cầu…", output bằng "Nêu/Hướng dẫn/Khẳng định…". Đây là nơi chứa **mọi quy định vi phạm**: điều kiện đồng thời, khung bọc (học thuật, hư cấu) có cứu được không, phép thử, dấu hiệu đặc trưng. |
| Không vi phạm khi | có | 4–8 gạch. Chỉ các trường hợp an toàn thật sự (hỏi tác hại, pháp luật, lịch sử, từ chối kèm điều hướng…). Mọi quy định "thế nào là an toàn" nằm ở đây. |
| Ca sát ranh giới | nên có | 4–6 cặp câu đối chứng, dạng `"câu" → vi phạm / không vi phạm (lý do ngắn)`. Mỗi cặp cùng chủ đề, khác kết luận. Đây là nơi duy nhất chứa ví dụ. Mỗi câu phải **tự đủ nghĩa** (đơn lượt, nêu rõ đối tượng, không "lá cờ đó", "vụ này"), dùng **tên riêng cụ thể** (không X/Y/A/B; người hư cấu thì kèm chức danh), và với file output thì là **lời của trợ lý** (giọng "em"/"anh/chị"), không phải câu hỏi của người dùng. Prompt dặn LLM không chép lại, không lặp mô-típ; giữ nguyên cả bộ, không xoay vòng. |
| Lưu ý riêng | khi cần | Chỉ dẫn **trực tiếp, mang tính ràng buộc/hướng dẫn** áp cho cả hai nhãn: "Chỉ xoay quanh…", "Không trộn…", "Dùng đúng tên và chức danh…". KHÔNG viết như ghi chú thông tin để người đọc lại, KHÔNG giải thích vì sao, KHÔNG nghiêng về vi phạm hay an toàn (quy định nhãn thuộc "Vi phạm khi" / "Không vi phạm khi" hoặc hai mục lưu ý theo nhãn). Không nêu tên intent khác. |
| Lưu ý mẫu vi phạm / Lưu ý mẫu an toàn | khi cần | Chỉ dẫn viết mẫu, chỉ áp cho một nhãn (prompt nối vào mục Lưu ý của ô tương ứng). Cũng viết trực tiếp, dạng chỉ dẫn. |
| Mẫu vi phạm - mức khó / Mẫu an toàn - mức khó | có | Một đoạn mô tả "khó" nghĩa là gì ở chủ đề này (không phải ví dụ). Thay mô tả HARD chung trong prompt. |
| Khía cạnh vi phạm / Khía cạnh an toàn | có | 6–12 dòng `- A1: …` / `- S1: …`. Mỗi khía cạnh là một góc khác biệt của chủ đề (đối tượng, kiểu hành vi, STT 1.02). Khía cạnh vi phạm phủ **mọi STT** của mục 1.02; khía cạnh an toàn là các chủ đề thật sự an toàn gần chủ đề. Mỗi dòng một ý, đủ để LLM hiểu mà không cần chú thích. |

## C. Quy tắc nội dung (vòng 2)

**Phải bỏ**
- Mọi thứ trỏ sang **intent khác**: dòng `→ Tên_intent`, PRIORITY RULE, tên hay mã intent, mã S0/S1/P0, mã STT. LLM không hiểu routing. Điều cần giữ chỉ là: "đừng trộn chủ đề X vào mẫu", viết bằng lời thường trong **Lưu ý riêng**.
- Thuật ngữ của classifier: MATCH / NOT MATCH, "đầu vào/đầu ra" (dùng "câu của người dùng / câu trả lời của trợ lý"), "tầng", "nhãn", "intent".
- Tên sản phẩm, tên trợ lý và tên tập đoàn (Vita, V-Guardrail, Vingroup). **Ngoại lệ duy nhất**: các cặp `vingroup_*` được nêu "Vingroup", tên lãnh đạo, thương hiệu.
- Tín hiệu hay ví dụ đa lượt ("chia nhỏ qua nhiều lượt", "lượt trước"…). Chỉ sinh đơn lượt.
- Ví dụ lặp ý, ví dụ lẫn nhãn của intent khác, ví dụ chứa số liệu hay chức danh có thể lỗi thời.
- Lỗi chính tả, dòng lặp, ghi chú cho người review.
- Ký hiệu thay thế thực thể ("X", "Y", "A", "B", "nước X", "công ty X"): model dễ chép nguyên ký hiệu vào dữ liệu. Dùng tên cụ thể.
- Ví dụ hay mô tả đặt trong mục **Chủ đề** (mục này chỉ mô tả trung lập).

**Phải sửa**
- Giọng trợ lý: ví dụ output dùng **"em"** tự xưng, **"anh/chị"** gọi người dùng; không dùng "Vita", "mình", "tôi" cho trợ lý.
- Ví dụ người dùng vi phạm intent khác (như "…và mua ở đâu" ở nhóm sản xuất): cắt phần lẫn hoặc bỏ ví dụ.
- Đoạn dài viết thành câu ngắn, trực tiếp. Hướng dẫn > giải thích > ví dụ.
- Danh sách thực thể: Thủ tướng hiện tại là Lê Minh Hưng; Tô Lâm vừa là Tổng Bí thư vừa là Chủ tịch nước. Không nêu chức danh, số liệu, năm chưa chắc chắn; dùng tên và chức danh theo `../source_md/mapping/40_danh_sach_thuc_the.md`.

**Phải giữ**
- Cách phân biệt vi phạm / không vi phạm của intent, ca sát ranh giới, các quy tắc riêng quan trọng (ví dụ nhóm chủ quyền: câu trả lời an toàn phải nêu lập trường Việt Nam; trung lập về chủ quyền là vi phạm).
- Lệch giữa các vế của 2.07 (ví dụ "trung tính là an toàn" vs "trung lập là vi phạm"): chọn một cách đọc nhất quán theo 1.02 và ghi vào review.

## D. Quy tắc theo loại intent

- **Cặp input ↔ output**: viết cả hai file; ví dụ ở output là câu trả lời của trợ lý, không phải yêu cầu của người dùng.
- **Output dùng chung nhiều input**: chỉ một file output; mỗi input vẫn sinh ô assistant theo ngữ cảnh của mình (xem `pairs.json`).
- **Intent không có output riêng** (như `chu_quyen_kiem_soat_tren_thuc_te`): ô assistant dùng subprompt output của intent đối ứng ghi trong `pairs.json`.
- **Intent mới** (`intent_taxonomy/new_intents/`) và **output nháp không ID**: coi như intent thường, đối chiếu 1.02 ở vòng 1.
- **Jailbreak / prompt injection, PII**: ngoài phạm vi (business riêng / không áp dụng cho ViTa).
- **Vũ khí, chất nổ, hủy diệt hàng loạt**: subprompt hiện chỉ viết **khái quát** vì người soạn không đọc nguồn nhóm này (xem mục G); đây là giới hạn của người soạn, KHÔNG phải giới hạn nội dung generator được sinh. Chi tiết do team policy bổ sung.
- **Hành vi nhắm người thật** (tin đồn, bôi nhọ, đời tư): mẫu dùng tên và chức danh theo danh sách thực thể.

## E. Giới hạn kích thước

Mỗi file subprompt ≲ 5.500 ký tự (cặp ma túy mẫu: khoảng 5.000). Prompt render của một ô ≲ 6.500 ký tự (cặp thường); nhóm Vingroup được dài hơn vì danh sách đối tượng bảo vệ. Vượt thì cắt ví dụ và lặp ý trước, không cắt ranh giới.

## F. Checklist một file (tick hết mới nộp review)

- [ ] Có đủ header bắt buộc, đúng thứ tự, tên header chính xác.
- [ ] "Chủ đề" trung lập, không ví dụ, không phán xét vi phạm hay an toàn; mọi quy định nhãn nằm ở "Vi phạm khi" / "Không vi phạm khi".
- [ ] "Lưu ý riêng" là chỉ dẫn trực tiếp cho cả hai nhãn, không phải ghi chú thông tin, không nghiêng về một nhãn.
- [ ] Không còn: tên hay mã intent khác, `→`, MATCH/NOT MATCH, Vita/V-Guardrail/Vingroup (trừ nhóm Vingroup), mã S/P/STT, ghi chú review.
- [ ] Mọi STT của mục 1.02 tương ứng đều có ít nhất một khía cạnh vi phạm.
- [ ] Nội dung 2.07 vượt 1.02 đã được xét theo "cùng lĩnh vực"; phần bỏ/giữ có lý do trong file review.
- [ ] Ca sát ranh giới là cặp đối chứng, không lẫn nhãn intent khác.
- [ ] Ví dụ output là lời trợ lý, dùng "em" / "anh/chị"; mọi ví dụ tự đủ nghĩa và dùng tên cụ thể (không X/Y/A/B).
- [ ] Không có chỉ dẫn giới hạn nội dung generator (mục H).
- [ ] Render đủ 4 ô, đọc lại, không thấy chỗ khó hiểu với người chưa biết gì về dự án.
- [ ] Không có số liệu, chức danh, năm chưa xác minh.

## G. Nhóm rủi ro cao nhất: KHÔNG đọc nội dung nguồn

Sáu intent sau (cùng `nhan_van_cong_cu_gay_hai_va_khong_che_input`, xử lý khái quát như nhóm này) nằm ở vùng mà đọc hay viết chi tiết có thể khiến cả cuộc trò chuyện bị chặn (CBRN, tình dục hóa trẻ em, chế tạo vũ khí và chất nổ):

- `nhan_van_vu_khi_huy_diet_hang_loat_cbrn_input` / `_output`
- `csam_bao_ve_tre_em_input` / `_output`
- `nhan_van_che_tao_vu_khi_chat_no_input` / `_output`

Quy tắc:
1. **Không mở, không đọc, không dán** file đặc tả nguồn của các intent này, cũng như các dòng STT chi tiết của mục 1.02 tương ứng (S1-1, S2-1, S2-6). Không đọc kết quả sinh `assistant_violate` / `user_violate` của chúng trong chat.
2. (Áp dụng cho người soạn subprompt, không áp dụng cho nội dung generator sinh.) Viết subprompt **chỉ từ tên intent và tiêu đề mục 1.02**, ở mức khái quát: loại hành vi, không thao tác, không tên chất hay vật liệu, không thông số, không ví dụ, không mô tả chi tiết.
3. Mọi mục `Vi phạm khi`, `Ca sát ranh giới`, `Khía cạnh` chỉ ghi **loại nội dung** ở mức phân loại. Chi tiết do team policy bổ sung trước khi sinh dữ liệu; file đánh dấu `Trạng thái: KHÁI QUÁT, chờ policy`.
4. Công cụ hỗ trợ (script dump, lint) bỏ qua sáu intent này; kiểm tra chất lượng bằng chỉ số (độ dài, định dạng, quét tên), không đọc nội dung.
5. Intent kề vùng này (`nhan_van_cong_cu_gay_hai_va_khong_che`, vũ khí trong phạm vi mua bán): xử lý như nhóm trên khi nguồn nhắc tới vũ khí; khi chưa chắc thì viết khái quát.

## H. Không giới hạn nội dung generator sinh

Subprompt **không được** chứa chỉ dẫn giới hạn mức độ chi tiết, độ cụ thể hay độ tường minh của nội dung generator sinh (kiểu "chỉ ở mức loại nội dung", "không nêu tên chất / thao tác / số liệu", "dùng giá trị giả", "không viết chi tiết"). Điều kiện duy nhất: mẫu **thỏa nhãn yêu cầu** (vi phạm hoặc an toàn). Các dòng ranh giới nhãn (ví dụ mẫu an toàn không được chứa yếu tố vi phạm, đối tượng phải đúng chủ đề, không trộn chủ đề khác) vẫn giữ.

## I. Review và xuất Excel

- File Excel review sinh từ chính các subprompt: `python3 taxonomy/review/export_review.py` → `taxonomy/review/v207_subprompts_review.xlsx` (sheet SUBPROMPTS, PAIRS, RULES, HƯỚNG DẪN). Excel chỉ là bản đọc; **sửa nội dung ở file `.md`**, không sửa trong Excel.
- Người duyệt điền cột "Quyết định" (Duyệt / Sửa / Bỏ / Hỏi policy) và "Ghi chú của người review". Sau khi áp dụng xong thì xuất lại.
- Script từ chối ghi đè khi Excel hiện có đã có quyết định hay ghi chú; chỉ dùng `--force` khi các ghi chú đó đã được áp dụng. Nên giữ bản đã review thành một file riêng (ví dụ `…round1_reviewed.xlsx`) trước khi xuất lại.
- Dòng tô cam (Rủi ro = CAO NHẤT) là nhóm mục G, chưa được review nội dung.
