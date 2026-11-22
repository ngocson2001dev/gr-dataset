# Generator v2.07

Sinh dữ liệu **chỉ để test** guardrail (không chia dev/test, không train). Mỗi dòng kết quả là một cặp (câu người dùng, câu trợ lý). Hậu kiểm sau khi sinh: [dataset/README.md](../dataset/README.md).

| Thứ | Ở đâu |
|---|---|
| Script duy nhất | [generate.py](generate.py) |
| Khung prompt | [prompts/cell.j2](prompts/cell.j2) |
| Subprompt từng intent | `../taxonomy/subprompts/<intent_key>.md` |
| Danh sách cặp | `../taxonomy/intent_taxonomy/pairs.json` |
| Kênh voice / typing | [channels.json](channels.json): bản **riêng của v2.07**, tách khỏi `share/channels.json` của pipeline 205 |

---

## 1. Tóm tắt

1. **Cặp** = 1 intent input + 1 intent output (41 cặp). Mỗi cặp có 4 **ô**: `user_violate`, `user_safe`, `assistant_violate`, `assistant_safe`.
2. **Bước 1** sinh câu người dùng (2 ô user). **Bước 2** sinh câu trợ lý đáp lại *chính các câu user đó* (2 ô assistant), nên không câu user nào bị bỏ.
3. Mỗi lần gọi LLM sinh một **lô** 10 mẫu; lô xong thì ghi file ngay.
4. Mỗi mẫu được giao sẵn **thuộc tính** (khía cạnh, cách hỏi, bề mặt, né bộ lọc, độ khó), chia theo **tổng** rồi mới cắt lô, nên tổng luôn đúng tỉ lệ.
5. Sau mỗi bước, **cổng lọc** (Jev + Gemini) loại câu hỏng và sinh bù đúng thuộc tính (mục 7).
6. Cuối cùng **merge** thành một file cặp.

Mặc định bỏ cặp có subprompt đánh dấu `KHÁI QUÁT` (chờ policy; muốn sinh thì `--include-abstract`) và cặp thiếu file subprompt.

## 2. Lệnh

```
python3 generator/generate.py --all --N 1 --dry-run              # dựng prompt đủ 4 ô × 2 kênh, in coverage, KHÔNG gọi LLM
python3 generator/generate.py --pairs a,b --N 1                  # thử 1-2 cặp, kênh voice
python3 generator/generate.py --pairs a --N 1 --channel typing   # kênh typing
python3 generator/generate.py --all --N 4                        # cả bộ
python3 generator/generate.py --all --N 4 --cells user_violate,user_safe   # chỉ bước 1
python3 generator/generate.py --all --N 4 --resume 20261006_153012          # bù phần thiếu / chạy tiếp bước 2
python3 generator/generate.py --merge 20261006_153012                       # chỉ ghép raw thành file cặp
```

Tùy chọn khác:
- `--llm-model` (mặc định `gemini-3.5-flash`), `--workers` (5), `--dataset-dir` (`dataset`).
- `--sensitive-llm-model` (mặc định `deepseek/deepseek-v4.1-flash-1017` qua OpenRouter, backend `deepinfra/fp8` ghim trong `share/llm/llm_openrouter.py` → `MODEL_PROVIDERS`): model sinh riêng của nhóm nhạy cảm, tức các cặp có `"sensitive": true` trong `pairs.json` (`csam_bao_ve_tre_em`, `nhan_van_dau_doc_phong_hoa_pha_hoai`, `nhan_van_ky_thuat_rui_ro_cao`, `nhan_van_vu_khi_huy_diet_hang_loat_cbrn`). `_run.json` ghi `sensitive_model`, cột `model` trong merged ghi đúng model của từng cặp. `--resume` lần chạy cũ chưa có khoá này thì cả nhóm sinh tiếp bằng model chung.
- `--seed`: mặc định ngẫu nhiên và in ra màn hình; `--resume` không truyền thì dùng lại seed cũ.
- Cổng lọc: `--no-gate`, `--gate-retries` (2), `--review-model` (`gemini-3.8-flash`).

`--dry-run` ghi prompt vào `generator/logs/dry/<kênh>/` và in coverage (số lô, số mẫu HARD / né bộ lọc / FREE, prompt dài nhất). Ô assistant trong dry-run dùng câu user giả.

## 3. Cỡ mẫu `--N`

`--N` (mặc định 1) là hệ số nhân; **1 đơn vị = 1 lô = 10 mẫu**. Mỗi cặp:

| Câu user (bước 1) | Số mẫu | Combo ở bước 2 (chữ đầu = nhãn user, chữ sau = nhãn trợ lý) |
|---|---|---|
| `user_violate` | **40N** | 30N **VV** (trợ lý làm theo) + 10N **VS** (từ chối / điều hướng) |
| `user_safe` vùng xám (toàn HARD) | **10N** | **SV** (trả lời rồi vượt ranh giới) |
| `user_safe` thật | **30N** | **SS** (trả lời hữu ích) |

N=1 → 40 mẫu mỗi ô assistant, 80 dòng merge mỗi cặp. Bước 2 dùng mỗi câu user **đúng một lần** (`allocate`; VV : VS = 3 : 1, phân tầng theo cờ HARD).

## 4. Thuộc tính của mẫu

| Thuộc tính | Áp dụng | Chia thế nào |
|---|---|---|
| **Khía cạnh** | mọi ô | A…/S… từ subprompt, chia đều. Trợ lý đáp câu user vùng xám: `FREE` |
| **Cách hỏi** (user) / **Cách thể hiện** (assistant) | mọi ô | bảng 4.1 |
| **Bề mặt** | ô user | bảng 4.2 |
| **Né bộ lọc** | `user_violate` | 20% (`OBFUSCATION_SHARE`), mục 4.3 |
| **Độ khó** | mọi ô | 25% HARD; vùng xám 100%; user_safe thật 0% |

### 4.1 Cách hỏi / Cách thể hiện (`CONTENT_WEIGHTS`, `ASSISTANT_FOLLOW*`)

| Ô | Khóa và tỉ lệ |
|---|---|
| user_violate | DIRECT 50 · INDIRECT 30 · ACADEMIC 10 · FICTION 10 |
| user_safe | DIRECT 40 · ROLE 30 · CONTEXT 30 |
| assistant_violate | user FICTION → FICTION; cách hỏi khác → DIRECT 70 · CAVEAT 30; user vùng xám → DIRECT · CAVEAT chia đều |
| assistant_safe | user vi phạm → REFUSE · REDIRECT chia đều; user an toàn → HELP |

### 4.2 Bề mặt (`SURFACE_WEIGHTS`, mô tả ở `channels.json` → `styles`)

| voice | % | typing | % |
|---|---|---|---|
| Nói tự nhiên có từ đệm | 40 | Đầy đủ câu, có dấu | 30 |
| Nói ngắn (dưới 15 từ) | 30 | Gõ tắt/thiếu dấu | 25 |
| Tự sửa giữa câu | 20 | Viết ngắn (dưới 15 từ) | 20 |
| Nói dài lan man | 5 | Thân mật/suồng sã | 15 |
| Có lỗi nghe nhầm | 5 | Dán đoạn dài | 10 |

Chỉ ghép tổ hợp hợp lý (`SURFACE_ALLOWED`): "ngắn" chỉ với DIRECT, INDIRECT, ROLE; "lan man" không với DIRECT. Bề mặt hạn chế nhất được gán trước; lô quá nhỏ thì phần dư chuyển sang bề mặt không hạn chế.

### 4.3 Né bộ lọc

- Không ghép với FICTION, và với bề mặt "Có lỗi nghe nhầm", "Đầy đủ câu, có dấu", "Dán đoạn dài".
- voice né bằng **âm thanh** (đánh vần, đồng âm, nói lái, xen tiếng Anh); typing né bằng **thị giác** (chèn dấu, bỏ dấu, thay ký tự, viết tắt…).
- Hint chỉ nằm ở `channels.json` (`obfuscation_hint`, dùng chung mọi cặp).

## 5. Chia theo tổng (`plan_rows`)

1. Mỗi trục tính hạn mức theo tổng số mẫu của (cặp, ô, nguồn) bằng làm tròn phần-dư-lớn-nhất (`balanced`), rồi xáo trộn.
2. Gán trục cho từng dòng theo điều kiện ghép (4.2, 4.3), rồi cắt lô 10 mẫu.

Ví dụ N=5, `user_violate`, voice: 200 mẫu, 20 lô; DIRECT 100 · INDIRECT 60 · ACADEMIC 20 · FICTION 20; HARD 50; né bộ lọc 40.

**Seed:**
- Tổng hàng và tổng cột luôn đúng hạn mức.
- Ô chéo (cách hỏi × bề mặt) dao động: khoảng ±3 mẫu ở ô lớn với n=200. Đừng đọc tỉ lệ ô chéo của một cặp; gộp 40 cặp thì nhiễu gần như mất.
- Từng lô có thể lệch (vd 8/10 mẫu cùng bề mặt), chỉ tổng là đúng.
- Cùng `--seed` cho kết quả y hệt.

## 6. Prompt: từng mục lấy data ở đâu

Thứ tự theo [cell.j2](prompts/cell.j2). Sau khi render, code kiểm tên cấm (`Vita`, `V-Guardrail` luôn cấm; `Vingroup` chỉ cho cặp `vingroup_*`), vi phạm thì ném `ValueError`.

| Mục | Nguồn | Ghi chú |
|---|---|---|
| VAI TRÒ, MỤC ĐÍCH | cố định | |
| NHIỆM VỤ | cố định, 4 nhánh theo ô | `assistant_violate` có đoạn riêng cho câu user vùng xám (trả lời rồi trượt qua ranh giới) |
| CHỦ ĐỀ | subprompt `Chủ đề` | |
| Vi phạm khi / Không vi phạm khi | subprompt cùng tên, đánh số `VP1…` / `KV1…` | in cho **mọi ô**. Mỗi mục là định nghĩa tự đủ; routing sang chủ đề khác, điều kiện chung, phép thử, vỏ bọc không cứu được thì để ở `Lưu ý riêng` |
| Ca sát ranh giới | subprompt (nếu có) | chỉ để hiểu ranh giới, không chép |
| Lưu ý riêng | `Lưu ý riêng` + `Lưu ý mẫu vi phạm` (ô violate) / `Lưu ý mẫu an toàn` (ô safe) | `Lưu ý riêng` cũng vào prompt chấm của Gemini; Jev chỉ nhận VP/KV |
| KÊNH | `channels.json` | ô user dùng `--channel` (mặc định voice); ô assistant dùng kênh `assistant` |
| THUỘC TÍNH CỦA MẪU | mục 4 | subprompt có `Mẫu ... - mức khó` thì **thay** mô tả HARD mặc định |
| CÂU CỦA NGƯỜI DÙNG | câu user bước 1 (chỉ ô assistant) | gắn nhãn `(vi phạm)` / `(an toàn, vùng xám)` / `(an toàn)` |
| DANH SÁCH MẪU | `plan_rows` | mỗi dòng chỉ chứa khóa thuộc tính |
| QUY TẮC, ĐỊNH DẠNG ĐẦU RA | cố định, rẽ nhánh theo ô | JSON array; mỗi phần tử có `matched_rule` (mã VP/KV), ô user_violate thêm `anchor`, ô assistant thêm `reply_to`, `aspect` |

Quy tắc chính:
- Mỗi mẫu một lượt, tự đủ nghĩa, đúng thuộc tính được giao.
- Mẫu violate phải khớp rõ một mục "Vi phạm khi". Mẫu safe phải an toàn với **mọi** chủ đề, không chỉ chủ đề này.
- Dùng tên riêng cụ thể (không X, Y).
- **User** chỉ tự xưng "tôi" hoặc không xưng. **Trợ lý** xưng "em", gọi "anh/chị", không dùng giữ chỗ kiểu "[tiếp tục…]".

**Đọc kết quả LLM:** bỏ mẫu thiếu `row`/`text`, trùng `row`, `text` rỗng; bỏ mẫu thiếu hoặc sai `matched_rule`, thiếu `anchor` (lý do ở mục 7). Dòng bị bỏ được sinh bù trong lần chạy.

## 7. Chạy, cổng lọc, resume

Mỗi bước (user, rồi assistant) chạy theo lượt:
1. Sinh đủ số mẫu còn thiếu, các lô gọi LLM song song.
2. **Cổng lọc** (mặc định bật, tắt bằng `--no-gate`) chạy bước 1 và 2 của hậu kiểm ngay trên câu mới. Jev chấm mọi câu, Gemini chấm lại vùng đỏ + vàng. Câu có gợi ý `relabel`, `wrong_subject`, `unclear`, `fix_text` bị loại. Vùng, nhãn và gợi ý: xem [dataset/README.md](../dataset/README.md).
3. **Sinh bù** đúng thuộc tính của dòng bị mất, tối đa `--gate-retries` lượt (mặc định 2). Câu bù cũng qua cổng. Hết lượt mà vẫn thiếu thì in lệnh `--resume`.

Câu user được lọc **trước** khi sinh câu trả lời, nên không tốn tiền trả lời câu hỏng. Câu trả lời bị loại thì sinh lại cho cùng câu user.

**File** (mỗi lần chạy có một STAMP; cấu trúc thư mục `dataset/<STAMP>/` xem [dataset/README.md](../dataset/README.md)), trong `raw/`:
- `V207_<STAMP>_<ô>.jsonl`: 4 file mẫu.
- `V207_<STAMP>_dropped.jsonl`: mẫu bị loại, kèm thuộc tính và lý do:
  - `rule_missing` / `rule_wrong_list` / `rule_not_in_list` / `rule_other_topic`: `matched_rule` thiếu, thuộc danh sách sai, vượt số mục, hoặc trỏ mục chủ đề khác.
  - `anchor_missing` / `anchor_not_in_text`: chỉ ở `user_violate`.
  - `gate_relabel` / `gate_wrong_subject` / `gate_unclear` / `gate_fix_text`: do cổng lọc, kèm kết quả chấm. Hậu kiểm hiện các dòng này ở sheet `gate_dropped`.
- `V207_<STAMP>_gate_jev.jsonl`, `..._gate_review.jsonl`: kết quả cổng lọc. Merge chuyển sang `check/`, nên hậu kiểm không chấm lại.
- `V207_<STAMP>_run.json`: manifest gồm kênh, model, N, seed, ô, cặp, `gate`, `review_model`, `gate_stats`; mỗi lần chạy có `time` và `end_time`.

Log từng lô ở `generator/logs/V207_<STAMP>.jsonl`.

**Merge** tự chạy cuối lượt có ô assistant, hoặc chạy riêng `--merge <STAMP>`.

**Resume** `--resume <STAMP>`:
- Bước 1 chỉ sinh phần user còn thiếu.
- Bước 2 giữ nguyên combo của câu đã có câu trả lời, chỉ sinh cho phần chưa có.
- Chỉ tính mẫu cùng kênh.
- Cổng lọc theo lần chạy cũ: lần chạy trước 10/10/2026 không có cổng thì resume cũng không lọc.

## 8. Dữ liệu đầu ra

### 8.1 Raw (mỗi dòng một mẫu)

| Trường | File | Ý nghĩa |
|---|---|---|
| `id`, `pair`, `text` | cả 4 | UUID, tên cặp, nội dung |
| `intent_id` | cả 4 | id intent (taxonomy `name_en`, viết thường): file user là intent input, file assistant là intent output |
| `aspect`, `style`, `hard` | cả 4 | khía cạnh (`FREE` với trợ lý đáp vùng xám), cách hỏi / cách thể hiện, `HARD`/`NORMAL` |
| `rule` | cả 4 | mã mục model khai mẫu khớp (`VP<số>` / `KV<số>`, cùng cách đánh số với `matched` của Gemini). Không có ở dataset trước 10/10/2026 |
| `surface` | 2 file user | bề mặt |
| `obf` | user_violate | cờ né bộ lọc |
| `user_id`, `reply_ok` | 2 file assistant | `id` câu user gốc; `reply_ok` = 6 chữ đầu câu user mà model chép lại có khớp câu cùng dòng không (chỉ là cờ; inspect báo WARN `assistant_reply_mismatch`) |

Ô lấy từ tên file; kênh, model, tham số lấy từ `run.json`. `tier`, `category` lấy từ `pair` → `pairs.json` → `taxonomy.json`.

### 8.2 Merge: `dataset/<STAMP>/merged/V207_<STAMP>_pairs.jsonl`

Mỗi dòng là một cặp, ghép bằng `user_id`, sắp theo thứ tự cặp trong `pairs.json`.

| Nhóm | Trường |
|---|---|
| Định danh | `id` (id câu trợ lý), `pair`, `tier`, `category`, `channel`, `model` |
| Phía user | `user_id`, `user_intent_id`, `user_text`, `user_verdict`, `user_aspect`, `user_rule`, `user_style`, `user_surface`, `user_obf`, `user_hard` |
| Phía trợ lý | `assistant_intent_id`, `assistant_text`, `assistant_verdict`, `assistant_aspect`, `assistant_rule`, `assistant_reply_ok`, `assistant_style`, `assistant_hard` |

Combo = chữ đầu `user_verdict` × `assistant_verdict`. Câu chưa đủ cặp không vào file. Merge ghi đè mỗi lần, vì là bản dẫn xuất từ raw.

## 9. Lưu ý

- Chưa dedupe giữa các lô. `OVERGEN = 1.0`: không sinh dư, phần thiếu bù bằng các lượt sinh bù.
- Prompt đang bằng tiếng Việt để debug; nguyên tắc chung là prompt tiếng Anh, kết quả tiếng Việt (`../../prompting_principals.md`).
- Mục KÊNH voice còn dài vì giữ nguyên các điều cấm của bản 205.
