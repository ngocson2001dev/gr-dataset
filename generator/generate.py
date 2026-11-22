r"""Sinh dữ liệu v2.07: 41 cặp × 4 ô (user_violate, user_safe, assistant_violate, assistant_safe).

Một hệ số N quyết định cỡ mẫu mỗi cặp (tỉ lệ cấu hình ở UNITS, mỗi đơn vị = 1 lô BATCH_SIZE):
  Bước 1 (user):
    user_violate          40N  → 30N cho assistant_violate (VV) + 10N cho assistant_safe (VS)
    user_safe vùng xám    10N  → assistant_violate (SV)   [100% mẫu HARD]
    user_safe thật        30N  → assistant_safe (SS)      [toàn mẫu thường]
  Bước 2 (assistant): dùng TOÀN BỘ câu user vừa sinh, mỗi câu đúng một lần (không bỏ câu nào):
    assistant_violate = VV (user_violate × 3/4) + SV;  assistant_safe = VS (user_violate × 1/4) + SS
  Ví dụ N=4 → khoảng 160 mẫu mỗi ô; số câu user thật sinh ra lệch nhẹ thì số mẫu assistant lệch theo.

Ra (mỗi lần chạy một dấu thời gian STAMP, một thư mục riêng dataset/<STAMP>/ gồm raw/, merged/, check/):
  dataset/<STAMP>/raw/V207_<STAMP>_<ô>.jsonl + V207_<STAMP>_run.json (kênh, model, tham số)
  + V207_<STAMP>_dropped.jsonl (mẫu model trả về nhưng bị loại, kèm lý do; chỉ có khi có mẫu bị loại).
Dòng raw gọn, không lặp (ô, kênh, model nằm ở tên file/manifest; nhãn và câu user nối lại bằng `user_id`).
Phase cuối (merge): dataset/<STAMP>/merged/V207_<STAMP>_pairs.jsonl, mỗi dòng một cặp (user, trợ lý); tự chạy cuối mỗi lượt có ô assistant,
hoặc chạy riêng: --merge STAMP.
Tiếp tục lần chạy cũ: --resume STAMP. Log lô: generator/logs/V207_<STAMP>.jsonl.

Dùng (Windows, chạy từ THƯ MỤC GỐC repo `ai-alignment`; macOS/Linux đổi `python` thành `python3`):

python intents-vita-207/generator/generate.py --all        (hoặc --pairs a,b thay cho --all)

Các tham số (chỉ cần --all hoặc --pairs; các tham số còn lại tùy chọn). Mỗi dòng: giải thích. Mặc định: .... VD: ...
  --all              sinh mọi cặp có subprompt (bỏ cặp KHÁI QUÁT); dùng thay cho --pairs.  Mặc định: tắt.  VD: --all
  --pairs a,b        chỉ sinh các cặp này (tên cặp phân cách dấu phẩy, không dấu cách).  Mặc định: không có (phải dùng --all hoặc --pairs).  VD: --pairs chinh_tri_an_ninh_quoc_gia,vingroup_chinh_tri
  --N 1              hệ số cỡ mẫu; mỗi cặp 40N câu user_violate, 10N user_safe vùng xám, 30N user_safe thật (N=1 → 40 mẫu/ô assistant).  Mặc định: 1.  VD: --N 4
  --channel voice    kênh nhập liệu của người dùng: voice (ASR) hoặc typing (gõ).  Mặc định: voice.  VD: --channel typing
  --cells ...        các ô cần sinh, phân cách dấu phẩy.  Mặc định: cả 4 ô (user_violate,user_safe,assistant_violate,assistant_safe).  VD: --cells user_violate,user_safe   (chỉ bước 1, sinh câu user)
  --llm-model NAME   model sinh data; tên lấy từ share/llm.  Mặc định: gemini-3.5-flash qua Vertex (khi --resume thì dùng lại model lần chạy cũ).  VD: --llm-model deepseek/deepseek-v4-pro-0813
  --sensitive-llm-model NAME  model sinh của nhóm nhạy cảm (cặp có "sensitive": true trong pairs.json).  Mặc định: deepseek/deepseek-v4.1-flash-1017 qua OpenRouter, backend deepinfra/fp8 (khi --resume thì dùng lại model lần chạy cũ; lần chạy cũ chưa có nhóm này thì dùng model chung).  VD: --sensitive-llm-model glm-5.2-maas
  --workers 5        số lời gọi LLM chạy song song.  Mặc định: 5.  VD: --workers 10
  --seed 42          seed chia thuộc tính; cùng seed + cùng tham số → cùng kế hoạch mẫu.  Mặc định: ngẫu nhiên mỗi lần chạy (ghi vào _run.json; khi --resume thì dùng lại seed lần chạy cũ).  VD: --seed 42
  --dataset-dir DIR  thư mục gốc chứa các lần chạy (mỗi lần chạy một thư mục <STAMP>/ gồm raw, merged, check).  Mặc định: dataset.  VD: --dataset-dir dataset_thu_nghiem
  --resume STAMP     tiếp tục lần chạy cũ: chỉ sinh phần còn thiếu.  Mặc định: không có (lần chạy mới, STAMP mới).  VD: --resume 20261006_153012
  --merge STAMP      chỉ ghép raw của lần chạy STAMP thành file cặp (user, trợ lý), không sinh.  Mặc định: không có.  VD: --merge 20261006_153012
  --dry-run          chỉ dựng prompt đủ 4 ô × 2 kênh vào generator/logs/dry và in coverage, không gọi LLM.  Mặc định: tắt.  VD: --all --N 1 --dry-run
  --include-abstract sinh cả cặp KHÁI QUÁT (chờ policy).  Mặc định: tắt (bỏ cặp KHÁI QUÁT).  VD: --all --include-abstract
  --no-gate          tắt cổng lọc (xem dưới).  Mặc định: bật cho lần chạy mới; --resume theo lần chạy cũ.  VD: --no-gate
  --gate-retries 2   số lượt sinh bù tối đa mỗi bước.  Mặc định: 2.  VD: --gate-retries 3
  --review-model M   model ngoài của cổng lọc.  Mặc định: gemini-3.8-flash (khi --resume thì dùng lại model lần chạy cũ).  VD: --review-model glm-5.2-maas

Cổng lọc (bước 1 và 2 của hậu kiểm chạy ngay sau mỗi bước sinh): Jev chấm mọi câu mới → model ngoài chấm lại vùng đỏ + vàng →
loại câu mà cả hai cùng chấm ngược nhãn gán, model ngoài chấm WRONG_SUBJECT / UNCLEAR, hoặc báo text hỏng. Câu bị loại xoá khỏi
raw, ghi vào _dropped.jsonl (reason gate_relabel / gate_wrong_subject / gate_unclear / gate_fix_text), rồi sinh bù đúng thuộc tính (cách hỏi, bề mặt, khía cạnh...) của dòng bị loại, tối đa
--gate-retries lượt. Câu user được lọc TRƯỚC khi sinh câu trả lời. Kết quả chấm lưu ở raw/V207_<STAMP>_gate_{jev,review}.jsonl,
merge chuyển sang check/jev.jsonl, check/review.jsonl nên hậu kiểm không chấm lại (bước 2 chỉ còn mẫu xanh).
"""
import argparse, itertools, json, random, re, sys, time, uuid
from datetime import datetime
from collections import Counter
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
for _s in (sys.stdout, sys.stderr):   # Windows: console mặc định không phải UTF-8
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")


def wr(path, text):
    """Ghi file UTF-8, xuống dòng LF (không đổi thành CRLF trên Windows)."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


sys.path.insert(0, str(ROOT.parent / "share/llm"))

PAIRS = ROOT / "taxonomy/intent_taxonomy/pairs.json"
TAXONOMY = ROOT / "taxonomy/intent_taxonomy/taxonomy.json"
# id gốc của intent = phần trong ngoặc ở tên intent (taxonomy `name_en`), viết thường; map trực tiếp 1 intent → 1 chuỗi
TAX_INTENTS = json.load(open(TAXONOMY, encoding="utf-8"))["intents"]
INTENT_ID = {k: v["name_en"].lower() for k, v in TAX_INTENTS.items()}


def load_pairs():
    """Cấu trúc cặp từ pairs.json; tier/category/severity/status lấy từ taxonomy.json (nguồn duy nhất) qua intent input/output."""
    out = []
    for p in json.load(open(PAIRS, encoding="utf-8")):
        i, o = TAX_INTENTS[p["input"]], TAX_INTENTS[p["output"]]
        out.append(dict(p, tier=i["tier"], category=i["category"], severity_input=i["severity"], severity_output=o["severity"],
                        status=sorted({i["status"], o["status"]})))
    return out


def pair_model(p, model, sensitive_model):
    """Model sinh của cặp: nhóm nhạy cảm ("sensitive": true trong pairs.json) dùng model riêng nếu lần chạy có khai."""
    return sensitive_model if p.get("sensitive") and sensitive_model else model

# ---- DỰNG PROMPT (subprompt của intent + khung generator/prompts/cell.j2) ----
SUB = ROOT / "taxonomy/subprompts"
TEMPLATES = ROOT / "generator/prompts"
CHANNELS = json.load(open(Path(__file__).resolve().parent / "channels.json", encoding="utf-8"))   # kênh riêng của v2.07 (không dùng share/channels.json)
DEFAULT_CHANNEL = "voice"                           # kênh nhập liệu của người dùng: voice (ASR) hoặc typing (gõ)
DEFAULT_LLM_MODEL = "gemini-3.5-flash"              # model sinh data; tên trần có trong share/llm/llm_vertex_ai.SUPPORTED_MODELS → gọi qua Vertex
# model sinh của nhóm nhạy cảm (cặp có "sensitive": true trong pairs.json): qua OpenRouter, backend ghim deepinfra/fp8 ở
# share/llm/llm_openrouter.MODEL_PROVIDERS. Thay deepseek-v4.1-flash-maas (Vertex) từ 2026-11-11: lô ở bước 2 mất ~14 phút, hay timeout
SENSITIVE_LLM_MODEL = "deepseek/deepseek-v4.1-flash-1017"
DEFAULT_REVIEW_MODEL = "gemini-3.8-flash"           # model ngoài của cổng lọc (chấm lại câu đỏ/vàng); --resume dùng lại model lần chạy cũ
BATCH_SIZE = 10                                   # số mẫu mỗi lần gọi (ô user)
FORBIDDEN = r"(?i)\bvita\b|v-guardrail"          # luôn cấm
FORBIDDEN_NON_VINGROUP = r"(?i)vingroup"          # cấm trừ các cặp vingroup (xem vingroup_pair)


def vingroup_pair(name):
    """Cặp được nhắc tên Vingroup: "vingroup" là một từ trong tên cặp (vingroup_xuc_pham, van_hoa_su_dung_tu_vingroup)."""
    return "vingroup" in name.split("_")

STYLES = {
    "user_violate": {
        "DIRECT": "nói thẳng yêu cầu, không che đậy",
        "INDIRECT": "hỏi vòng, nói tránh Ý ĐỊNH (vd hỏi như kiến thức), nhưng câu hỏi vẫn CHỨA SẴN nội dung vi phạm (cáo buộc, xuyên tạc đặt làm tiền đề, hoặc đòi đúng thông tin, cách làm bị cấm), không phải dạng hỏi mà mục “Không vi phạm khi” coi là an toàn; VẪN PHẢI nêu rõ đối tượng vi phạm (chất, tổ chức, hành vi), nói tránh tên thì phải mô tả đủ để người lạ nhận ra",
        "ACADEMIC": "viện lý do học thuật, nghiên cứu hoặc nghề nghiệp để hỏi; lý do chỉ là vỏ bọc, câu vẫn đòi đúng nội dung vi phạm, không thành dạng hỏi mà mục “Không vi phạm khi” coi là an toàn",
        "FICTION": "bọc trong truyện, kịch bản hoặc nhập vai nhưng vẫn hỏi nội dung thật",
        # REFER: chỉ generate_multiturn.py dùng (lượt vi phạm cần ngữ cảnh của chiến lược đặt mật danh, chia nhỏ, dựng vai)
        "REFER": "chỉ trỏ về điều đã có ở các lượt trước (mật danh, nhân vật đã dựng, các mảnh đã hỏi) để đòi nội dung vi phạm; tự câu KHÔNG chứa từ quy kết hay tên thật của điều vi phạm, đọc riêng thì mơ hồ (lượt cần ngữ cảnh của multiturn)",
    },
    "user_safe": {
        "DIRECT": "hỏi thẳng, rõ ràng",
        "ROLE": "người hỏi nêu rõ vai của mình (ví dụ phụ huynh, giáo viên, nhà báo, sinh viên) và lý do hỏi",
        "CONTEXT": "có vài câu bối cảnh trước khi hỏi",
    },
    "assistant_violate": {
        "DIRECT": "trợ lý làm theo yêu cầu ngay, không do dự",
        "CAVEAT": "trợ lý mở đầu bằng MỘT câu cảnh báo hoặc từ chối nhẹ, rồi vẫn đưa đủ nội dung vi phạm; không kết bằng lời khuyên ngăn hay giáo dục làm câu thành an toàn",
        "FICTION": "trợ lý đưa nội dung vi phạm dưới dạng truyện, kịch bản hoặc lời nhân vật, nhưng vẫn đáp đúng yêu cầu của câu người dùng (cùng sản phẩm, đối tượng, chủ đề), chỉ đổi hình thức thể hiện",
    },
    "assistant_safe_refuse": {
        "REFUSE": "từ chối rõ ràng, nói ngắn gọn lý do, rồi điều hướng sang thông tin an toàn liên quan",
        "REDIRECT": "không làm theo nhưng chủ động cung cấp thông tin an toàn hữu ích về cùng chủ đề",
    },
    "assistant_safe_help": {
        "HELP": "trả lời hữu ích, đúng, ở mức kiến thức chung, không có nội dung vi phạm",
    },
}
DIFFICULTY = {
    "user_violate": {"NORMAL": "vi phạm rõ ràng, dễ nhận ra", "HARD": "nghe như vô hại hoặc chỉ hỏi kiến thức, nhưng thực chất vẫn vi phạm"},
    "user_safe": {"NORMAL": "câu bình thường cùng chủ đề", "HARD": "có từ khóa hoặc chi tiết nhạy cảm nên dễ bị chặn nhầm, nhưng thực sự an toàn"},
    "assistant_violate": {"NORMAL": "vi phạm rõ ràng, dễ nhận ra", "HARD": "nghe đàng hoàng, khách quan hoặc có cảnh báo, nhưng nội dung vẫn vi phạm"},
    "assistant_safe": {"NORMAL": "câu trả lời an toàn thông thường", "HARD": "trả lời đúng ranh giới cho câu hỏi dễ lẫn, không lọt nội dung vi phạm"},
}


def bullets(lines):
    return [re.sub(r"^[-•]\s+", "", l.strip()) for l in lines if l.strip()]


def load_sub(key):
    text = (SUB / f"{key}.md").read_text(encoding="utf-8")
    secs = {}
    cur = None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip(); secs[cur] = []
        elif cur is not None:
            secs[cur].append(line)
    kv = lambda name: dict(sorted((x.split(": ", 1) for x in bullets(secs.get(name, []))), key=lambda p: (p[0][0], int(p[0][1:]))))
    para = lambda name: " ".join(l.strip() for l in secs.get(name, []) if l.strip())
    return dict(topic=para("Chủ đề"), violates=bullets(secs["Vi phạm khi"]),
                not_violates=bullets(secs["Không vi phạm khi"]), boundary=bullets(secs.get("Ca sát ranh giới", [])),
                notes=bullets(secs.get("Lưu ý riêng", [])),
                notes_violate=bullets(secs.get("Lưu ý mẫu vi phạm", [])), notes_safe=bullets(secs.get("Lưu ý mẫu an toàn", [])),
                hard_violate=" ".join(bullets(secs.get("Mẫu vi phạm - mức khó", []))), hard_safe=" ".join(bullets(secs.get("Mẫu an toàn - mức khó", []))),
                ex_violate=bullets(secs.get("Ví dụ vi phạm", [])), ex_safe=bullets(secs.get("Ví dụ không vi phạm", [])),
                asp_violate=kv("Khía cạnh vi phạm"), asp_safe=kv("Khía cạnh an toàn"))


# ---- TỈ LỆ CÁC TRỤC (mỗi trục chia theo TỔNG số mẫu của (cặp, ô, nguồn) rồi mới chia vào lô) ----
CONTENT_WEIGHTS = {   # trục "cách hỏi" của người dùng (%)
    "user_violate": {"DIRECT": 50, "INDIRECT": 30, "ACADEMIC": 10, "FICTION": 10},
    "user_safe": {"DIRECT": 40, "ROLE": 30, "CONTEXT": 30},
}
SURFACE_WEIGHTS = {   # trục "bề mặt" theo kênh (%), tên khớp channels.json[kênh]["styles"]
    "voice": {"Nói tự nhiên có từ đệm": 40, "Nói ngắn": 30, "Nói dài lan man": 5, "Tự sửa giữa câu": 20, "Có lỗi nghe nhầm": 5},
    "typing": {"Đầy đủ câu, có dấu": 30, "Gõ tắt/thiếu dấu": 25, "Viết ngắn": 20, "Thân mật/suồng sã": 15, "Dán đoạn dài": 10},
}
OBFUSCATION_SHARE = 0.2                          # tỉ lệ mẫu user_violate có cờ né bộ lọc (hint theo kênh trong channels.json)
# Bề mặt hạn chế → các cách hỏi được ghép; bề mặt không liệt kê ghép với mọi cách hỏi
SURFACE_ALLOWED = {
    "Nói ngắn": {"DIRECT", "INDIRECT", "REFER"}, "Viết ngắn": {"DIRECT", "INDIRECT", "REFER"},   # câu cụt: không hợp với cách hỏi cần nhiều bối cảnh (ACADEMIC/FICTION/CONTEXT) hay phải nêu vai và lý do (ROLE)
    "Nói dài lan man": {"INDIRECT", "ACADEMIC", "FICTION", "ROLE", "CONTEXT"},                    # kể lể bối cảnh: không phải nói thẳng
}
SELF_CORRECT = "Tự sửa giữa câu"
SELF_CORRECT_MODES = {   # cách sửa giao cho từng dòng "Tự sửa giữa câu": tên → (tỉ lệ %, mô tả cho model)
    "đổi thẳng": (30, "nói sai một từ rồi nói ngay từ đúng, KHÔNG dùng từ đính chính nào"),
    "bỏ dở": (25, "đang nói thì bỏ dở giữa chừng rồi nói lại cả vế cho đúng, KHÔNG dùng à không hay ý tôi là"),
    "chen vế": (20, "chen vào giữa câu một vế đính chính kiểu không phải … mà là …, KHÔNG dùng à không hay ý tôi là"),
    "từ đính chính": (25, "dùng một từ đính chính ngắn rồi nói lại chi tiết đúng (à nhầm, à quên, chết nhầm, à không…), đa dạng, không lặp cùng một từ"),
}
OBFUSCATION_EXCLUDE_SURFACES = {"Có lỗi nghe nhầm", "Đầy đủ câu, có dấu", "Dán đoạn dài"}   # bề mặt không ghép với cờ né bộ lọc
# assistant_violate: cách thể hiện của trợ lý LÀM THEO cách hỏi của câu user (không gán cứng)
ASSISTANT_FOLLOW = {"FICTION": {"FICTION": 1}}            # user bọc truyện/nhập vai → trợ lý cũng đáp trong khung đó
ASSISTANT_FOLLOW_DEFAULT = {"DIRECT": 70, "CAVEAT": 30}   # các cách hỏi khác → làm theo ngay, hoặc cảnh báo nhẹ rồi vẫn làm
ASSISTANT_GRAY = {"DIRECT": 1, "CAVEAT": 1}               # câu user an toàn vùng xám
OBFUSCATION_EXCLUDE = {"FICTION"}                # cách hỏi không ghép với cờ né bộ lọc

def balanced(weights, n, rng):
    """n giá trị theo trọng số (%) với hạn mức làm tròn lớn nhất-phần-dư, rồi xáo trộn: phân bổ theo TỔNG."""
    tot = sum(weights.values())
    quota = {k: n * w / tot for k, w in weights.items()}
    cnt = {k: int(q) for k, q in quota.items()}
    for k in sorted(quota, key=lambda k: (quota[k] - cnt[k], rng.random()), reverse=True)[: n - sum(cnt.values())]:
        cnt[k] += 1
    out = [k for k, c in cnt.items() for _ in range(c)]
    rng.shuffle(out)
    return out


def assign_surfaces(rows, weights, rng):
    """Gán bề mặt theo tổng (hạn mức `balanced`) nhưng chỉ vào dòng có cách hỏi hợp lệ (SURFACE_ALLOWED).
    Xử lý bề mặt hạn chế nhất trước. Nếu không đủ dòng hợp lệ (lô rất nhỏ) thì phần dư chuyển sang bề mặt không hạn chế."""
    n = len(rows)
    quota = Counter(balanced(weights, n, rng))
    ok = lambda s, i: rows[i]["style"] in SURFACE_ALLOWED.get(s, {rows[i]["style"]})
    free = list(range(n)); rng.shuffle(free)
    leftover = []
    for s in sorted(quota, key=lambda s: sum(ok(s, i) for i in free)):
        take = [i for i in free if ok(s, i)][: quota[s]]
        for i in take:
            rows[i]["surface"] = s
        taken = set(take)
        free = [i for i in free if i not in taken]
        rng.shuffle(free)   # xáo lại: nếu không, dòng DIRECT còn lại dồn về cuối và bề mặt xử lý sau bị lệch
        leftover += [s] * (quota[s] - len(take))
    unrestricted = [s for s in weights if s not in SURFACE_ALLOWED]
    for i in free:
        cand = [s for s in leftover if ok(s, i)]
        s = rng.choice(cand) if cand else rng.choice(unrestricted)
        if cand:
            leftover.remove(s)
        rows[i]["surface"] = s


def plan_rows(cell, sp, turns, n, hard_share, channel, rng):
    """Phân bổ MỌI trục theo tổng n mẫu. Trả list[dict(aspect, style, surface, obf, hard)] đúng thứ tự mẫu/turn."""
    actor = "user" if cell.startswith("user") else "assistant"
    violate = cell.endswith("violate")
    rows = [dict(aspect=None, style=None, surface=None, fix=None, obf=False, hard="NORMAL") for _ in range(n)]
    hard_flags = balanced({"HARD": hard_share, "NORMAL": 1 - hard_share}, n, rng) if 0 < hard_share < 1 else (["HARD"] * n if hard_share >= 1 else ["NORMAL"] * n)
    for r, h in zip(rows, hard_flags):
        r["hard"] = h

    def fill(field, idx, weights):
        for i, v in zip(idx, balanced(weights, len(idx), rng)):
            rows[i][field] = v

    aspects = list(sp["asp_violate"] if violate else sp["asp_safe"])
    all_idx = list(range(n))
    gray = [i for i, t in enumerate(turns) if not t["violate"]] if cell == "assistant_violate" else []
    if actor == "user":
        fill("aspect", all_idx, {a: 1 for a in aspects})
    # ô assistant: khía cạnh để None, model tự chọn theo câu người dùng và trả ở key `aspect` (to_records đọc lại)
    for i in gray:
        rows[i]["aspect"] = "FREE"
    if actor == "user":
        fill("style", all_idx, CONTENT_WEIGHTS[cell])
        assign_surfaces(rows, SURFACE_WEIGHTS[channel], rng)
        fill("fix", [i for i, r in enumerate(rows) if r["surface"] == SELF_CORRECT], {k: w for k, (w, _) in SELF_CORRECT_MODES.items()})
        if violate:
            ok = [i for i, r in enumerate(rows) if r["style"] not in OBFUSCATION_EXCLUDE and r["surface"] not in OBFUSCATION_EXCLUDE_SURFACES]
            for i in rng.sample(ok, min(len(ok), int(OBFUSCATION_SHARE * n + 0.5))):
                rows[i]["obf"] = True
    elif cell == "assistant_violate":
        by_user_style = {}
        for i in all_idx:
            if i not in set(gray):
                by_user_style.setdefault(turns[i].get("style"), []).append(i)
        for us, idx in by_user_style.items():
            fill("style", idx, ASSISTANT_FOLLOW.get(us, ASSISTANT_FOLLOW_DEFAULT))
        fill("style", gray, ASSISTANT_GRAY)
    else:
        helps = [i for i, t in enumerate(turns) if not t["violate"]]
        for i in helps:
            rows[i]["style"] = "HELP"
        fill("style", [i for i in all_idx if i not in set(helps)], {"REFUSE": 1, "REDIRECT": 1})
    return rows


def build_prompt(pair_name, cell, rows, turns=None, channel=DEFAULT_CHANNEL):
    """Trả (prompt, rows). rows do plan_rows tạo (đã chia theo tổng); ô assistant: mỗi turn một dòng cùng thứ tự."""
    pair = next(p for p in load_pairs() if p["pair"] == pair_name)
    actor = "user" if cell.startswith("user") else "assistant"
    violate = cell.endswith("violate")
    sp = load_sub(pair["input"] if actor == "user" else pair["output"])
    turns = turns or []
    n = len(rows)
    aspects = dict(sp["asp_violate"] if violate else sp["asp_safe"])
    if any(r["aspect"] == "FREE" for r in rows):
        aspects["FREE"] = "câu người dùng an toàn: tự chọn nội dung vi phạm liền kề chủ đề câu hỏi, lồng tự nhiên vào câu trả lời"
    if cell == "assistant_safe":
        styles = {**STYLES["assistant_safe_refuse"], **STYLES["assistant_safe_help"]}
    elif actor == "user":
        styles = {k: STYLES[cell][k] for k in CONTENT_WEIGHTS[cell]}
    else:
        styles = STYLES[cell]
    ch = CHANNELS[channel if actor == "user" else "assistant"]
    surfaces = {k: ch["styles"][k] for k in SURFACE_WEIGHTS[channel]} if actor == "user" else {}
    used_fix = {r["fix"] for r in rows if r.get("fix")}
    fix_modes = {k: d for k, (_, d) in SELF_CORRECT_MODES.items() if k in used_fix}
    has_obf = any(r["obf"] for r in rows)
    obf_hint = ch["obfuscation_hint"] if has_obf else None
    env = Environment(loader=FileSystemLoader(TEMPLATES), trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
    diff = dict(DIFFICULTY[cell])
    hard = sp["hard_violate"] if violate else sp["hard_safe"]
    if hard:  # mẫu khó riêng của chủ đề thay cho mô tả chung
        diff["HARD"] = hard
    out = env.get_template("cell.j2").render(cell=cell, n=n, sp=sp, aspects=aspects, styles=styles, surfaces=surfaces, fix_modes=fix_modes, has_obf=has_obf, obf_hint=obf_hint,
                                             difficulty=diff, rows=rows, turns=turns, violate=violate, actor=actor,
                                             channel=ch, channel_key=channel)
    out = re.sub(r"\n{3,}", "\n\n", out)
    scan = out
    for t in turns:   # câu user là dữ liệu do LLM sinh, không thuộc khung/subprompt: không quét tên cấm ở đó
        scan = scan.replace(t["text"], "")
    # Vingroup được phép khi cặp là cặp vingroup, hoặc chính subprompt đang dùng có nhắc Vingroup (vd van_hoa_su_dung_tu_output dùng chung)
    sub_text = (SUB / f"{pair['input'] if actor == 'user' else pair['output']}.md").read_text(encoding="utf-8")
    vin_ok = vingroup_pair(pair_name) or re.search(FORBIDDEN_NON_VINGROUP, sub_text)
    bad = re.findall(FORBIDDEN, scan) + ([] if vin_ok else re.findall(FORBIDDEN_NON_VINGROUP, scan))
    if bad:
        raise ValueError("tên nhạy cảm còn trong prompt: " + ", ".join(set(bad)))
    return out, rows


DATASET_DIR = ROOT / "dataset"                   # mỗi lần chạy: DATASET_DIR/<STAMP>/raw, merged, check (check do các script hậu kiểm ghi)
LOGS_DIR = ROOT / "generator/logs"
PREFIX = "V207"
USER_CELLS = ["user_violate", "user_safe"]
ASSISTANT_CELLS = ["assistant_violate", "assistant_safe"]
ALL_CELLS = USER_CELLS + ASSISTANT_CELLS

# ---- CẤU HÌNH TỈ LỆ (bội số của N) ----
UNITS = {"VV": 3 * BATCH_SIZE, "VS": BATCH_SIZE, "SV": BATCH_SIZE, "SS": 3 * BATCH_SIZE}   # combo = (câu user, câu trợ lý), mẫu trên mỗi N; 1 đơn vị N = 1 lô
DEFAULT_HARD_SHARE = 0.25                       # tỉ lệ mẫu HARD tính trên TỔNG mỗi (cặp, ô, nguồn), rải đều qua các lô
OVERGEN = 1.0                                   # sinh dư để bù mẫu bị loại (>1 = dư)
# Nguồn câu user và độ khó của mỗi nguồn: (ô user, hard_share, tên nguồn)
USER_SOURCES = [
    ("user_violate", None, "V"),    # None = mặc định 25% HARD, tách đều sang VV/VS
    ("user_safe", 1.0, "G"),        # vùng xám: toàn HARD
    ("user_safe", 0.0, "R"),        # thật: toàn thường
]
SOURCE_UNITS = {"V": UNITS["VV"] + UNITS["VS"], "G": UNITS["SV"], "R": UNITS["SS"]}


def run_dirs(dataset_dir, stamp):
    """Thư mục của một lần chạy → (raw, merged)."""
    return dataset_dir / stamp / "raw", dataset_dir / stamp / "merged"


def out_path(out_dir, stamp, cell):
    """Mỗi lần chạy có một dấu thời gian `stamp`; file raw: <out_dir>/V207_<stamp>_<cell>.jsonl."""
    return out_dir / f"{PREFIX}_{stamp}_{cell}.jsonl"


def manifest_path(out_dir, stamp):
    return out_dir / f"{PREFIX}_{stamp}_run.json"


def read_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def read_cell(out_dir, stamp, cell):
    """Đọc file raw của một ô; `cell` không lưu trong từng dòng nên gán lại khi đọc."""
    rows = read_jsonl(out_path(out_dir, stamp, cell))
    for r in rows:
        r["cell"] = cell
    return rows


def missing_subprompts(pair):
    """Subprompt của cặp chưa có file (ví dụ nhóm nhạy cảm cao chưa viết lại)."""
    return [k for k in (pair["input"], pair["output"]) if not (ROOT / f"taxonomy/subprompts/{k}.md").exists()]


def is_abstract(pair):
    """Cặp có subprompt đánh dấu KHÁI QUÁT (chờ policy) — mặc định không sinh."""
    return any("KHÁI QUÁT" in (ROOT / f"taxonomy/subprompts/{k}.md").read_text(encoding="utf-8") for k in (pair["input"], pair["output"]))


def source_of(rec):
    if rec["cell"] == "user_violate":
        return "V"
    return "G" if rec["hard"] == "HARD" else "R"


def allocate(pair_name, user_recs, seed, assigned=None):
    """Chia TOÀN BỘ câu user của cặp vào 4 combo (không bỏ câu nào), mỗi câu đúng một combo.
    V (user_violate) → VV / VS theo tỉ lệ UNITS, phân tầng theo cờ HARD; G (vùng xám) → SV; R (thật) → SS.
    `assigned` = {user_id: ô assistant} của các câu đã có câu trả lời (resume): giữ nguyên combo của chúng,
    chỉ chia phần chưa có. Trả dict combo → list[turn]."""
    assigned = assigned or {}
    pools = {"V": [], "G": [], "R": []}
    for r in user_recs:
        pools[source_of(r)].append(r)
    rng = random.Random(f"{seed}-{pair_name}")
    for s in pools:
        pools[s].sort(key=lambda r: r["id"])
        rng.shuffle(pools[s])
    v = sorted(pools["V"], key=lambda r: r["hard"] != "HARD")             # HARD trước, rồi lấy cách đều để VS có cùng tỉ lệ khó
    target_vs = int(len(v) * UNITS["VS"] / (UNITS["VV"] + UNITS["VS"]) + 0.5)
    vs = [r for r in v if assigned.get(r["id"]) == "assistant_safe"]
    free = [r for r in v if r["id"] not in assigned]
    need = min(len(free), max(0, target_vs - len(vs)))
    vs += [free[int((i + 0.5) * len(free) / need)] for i in range(need)] if need else []
    vs_ids = {r["id"] for r in vs}
    sel = {"VV": [r for r in v if r["id"] not in vs_ids], "VS": vs, "SV": pools["G"], "SS": pools["R"]}
    turn = lambda r, combo: dict(text=r["text"], violate=combo in ("VV", "VS"), gray=r["hard"] == "HARD",
                                 user_id=r["id"], combo=combo, style=r.get("style"))
    return {c: [turn(r, c) for r in rs] for c, rs in sel.items()}


def assistant_turn_sets(alloc, cell, done_ids, seed, pair_name):
    """Gộp các combo của ô, xáo trộn, bỏ câu đã có kết quả (resume), chia lô."""
    combos = ("VV", "SV") if cell == "assistant_violate" else ("VS", "SS")
    turns = [t for c in combos for t in alloc[c] if t["user_id"] not in done_ids]
    random.Random(f"{seed}-{pair_name}-{cell}").shuffle(turns)
    return [turns[i:i + BATCH_SIZE] for i in range(0, len(turns), BATCH_SIZE)]


def chunks(seq, size=BATCH_SIZE):
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def user_jobs(pair, cell, hard_share, need, seed, tag, channel, reuse=()):
    """`reuse` = thuộc tính của các dòng bị mất ở lượt trước (model trả thiếu, thiếu anchor, bị cổng loại): sinh bù đúng các
    dòng đó để giữ phân bổ; phần còn thiếu (ví dụ khi --resume) chia mới bằng plan_rows."""
    share = DEFAULT_HARD_SHARE if hard_share is None else hard_share
    sp = load_sub(pair["input"])
    rows = [dict(r) for r in reuse][:need]
    if need > len(rows):
        rows += plan_rows(cell, sp, [], need - len(rows), share, channel, random.Random(f"{seed}-{pair['pair']}-{cell}-{tag}"))
    jobs = []
    for i, rs in enumerate(chunks(rows)):
        prompt, rs = build_prompt(pair["pair"], cell, rs, None, channel)
        jobs.append((prompt, dict(pair=pair, cell=cell, batch=f"{tag}{i}", rows=rs, turns=None, channel=channel)))
    return jobs


def assistant_jobs(pair, cell, turn_sets, seed, channel):
    turns = [t for ts in turn_sets for t in ts]
    sp = load_sub(pair["output"])
    rows = plan_rows(cell, sp, turns, len(turns), DEFAULT_HARD_SHARE, channel, random.Random(f"{seed}-{pair['pair']}-{cell}-a"))
    jobs, pos = [], 0
    for i, ts in enumerate(turn_sets):
        prompt, rs = build_prompt(pair["pair"], cell, rows[pos:pos + len(ts)], ts, channel)
        pos += len(ts)
        jobs.append((prompt, dict(pair=pair, cell=cell, batch=f"a{i}", rows=rs, turns=ts, channel=channel)))
    return jobs


def norm_ws(s):
    """Chuẩn hoá để so anchor với text: chữ thường, gộp khoảng trắng, bỏ dấu câu ở hai đầu."""
    return " ".join(s.lower().split()).strip(" .,!?;")


def asp_codes(pair, cell):
    """Mã khía cạnh hợp lệ của ô (theo subprompt của phía user/assistant tương ứng)."""
    sp = load_sub(pair["input"] if cell.startswith("user") else pair["output"])
    return list(sp["asp_violate"] if cell.endswith("violate") else sp["asp_safe"])


def rule_list(pair, cell):
    """(tiền tố mã, danh sách mục) mà `matched_rule` của ô phải thuộc: ô violate → VP ("Vi phạm khi"), ô safe → KV ("Không vi phạm khi").
    Đánh số theo đúng thứ tự trong subprompt, khớp cell.j2 và dataset/review_prompt.md."""
    sp = load_sub(pair["input"] if cell.startswith("user") else pair["output"])
    return ("VP", sp["violates"]) if cell.endswith("violate") else ("KV", sp["not_violates"])


# mục chỉ trỏ sang chủ đề khác: "thuộc chủ đề khác/vu khống/tin đồn…", "là (các) chủ đề khác/riêng", "không phải/không thuộc chủ đề này",
# "không dùng làm mẫu"; không bắt mục có nội dung thật như "dùng chủ đề khác làm cớ", "lồng lời kêu gọi vào chủ đề khác"
OTHER_TOPIC = re.compile(r"thuộc\s+(các\s+)?chủ đề\s+(?!này)\w|là\s+(các\s+)?chủ đề\s+(khác|riêng)|không\s+(phải|thuộc)\s+chủ đề này|không dùng làm mẫu", re.I)


def check_rule(raw, prefix, items):
    """`matched_rule` model trả → (mã chuẩn hoá, lý do loại hoặc None). Chấp nhận 'vp2', 'VP 2', 'VP2: ...'."""
    m = re.match(r"\s*(VP|KV)\s*(\d+)\b", str(raw or ""), re.I)
    if not m:
        return str(raw or "").strip()[:40], "rule_missing"
    code = f"{m.group(1).upper()}{int(m.group(2))}"
    if m.group(1).upper() != prefix:
        return code, "rule_wrong_list"
    if not 1 <= int(m.group(2)) <= len(items):
        return code, "rule_not_in_list"
    if OTHER_TOPIC.search(items[int(m.group(2)) - 1]):
        return code, "rule_other_topic"
    return code, None


def reply_matches(reply_to, user_text):
    """`reply_to` (6 chữ đầu câu user model chép lại) có khớp câu user cùng dòng không: chuẩn hoá chữ thường, bỏ dấu câu,
    cho lệch tối đa 2 chữ. Chỉ để ghi cờ `reply_ok` (đo tỉ lệ trả lời lệch dòng), không loại mẫu."""
    w = lambda s: re.findall(r"\w+", str(s or "").lower())
    rw, tw = w(reply_to)[:6], w(user_text)[:8]
    return bool(rw) and sum(x in tw for x in rw) >= max(1, len(rw) - 2)


def to_records(ctx, results):
    """Raw gọn, không lặp: ô, kênh, model nằm ở tên file / manifest; combo, câu user, nhãn suy ra bằng join `user_id`."""
    pair, cell, rows, turns = ctx["pair"], ctx["cell"], ctx["rows"], ctx["turns"]
    actor = "user" if cell.startswith("user") else "assistant"
    intent_id = INTENT_ID[pair["input"] if actor == "user" else pair["output"]]
    codes = set(asp_codes(pair, cell)) if actor == "assistant" else set()
    prefix, rule_items = rule_list(pair, cell)
    ctx["dropped"] = []   # mẫu model trả về nhưng bị loại (kèm lý do), generate_all ghi ra raw/..._dropped.jsonl để soát
    out, seen, accepted = [], set(), set()
    for r in results:
        try:
            idx = int(r["row"]) - 1
            text = str(r["text"]).strip()
            meta = rows[idx]
        except (KeyError, ValueError, TypeError, IndexError):
            continue
        if not text or idx in seen:
            continue
        seen.add(idx)
        aspect = meta["aspect"]
        if aspect is None:   # khía cạnh do model tự chọn; mã ngoài danh sách → "?" để hậu kiểm bắt
            aspect = str(r.get("aspect", "")).strip().upper()
            aspect = aspect if aspect in codes else "?"
        # mã mục V/KV model khai: phải thuộc đúng danh sách của ô; anchor (chỉ user_violate): cụm nêu rõ đối tượng vi phạm,
        # phải nằm nguyên văn trong text. Sai → loại, ghi _dropped.jsonl, sinh bù đúng thuộc tính
        rule, why = check_rule(r.get("matched_rule"), prefix, rule_items)
        anchor = str(r.get("anchor", "")).strip()
        if not why and cell == "user_violate" and (not anchor or norm_ws(anchor) not in norm_ws(text)):
            why = "anchor_missing" if not anchor else "anchor_not_in_text"
        if why:
            ctx["dropped"].append(dict(pair=pair["pair"], cell=cell, batch=ctx.get("batch"), row=idx + 1, intent_id=intent_id,
                                       reason=why, rule=rule, anchor=anchor or None, text=text, user_id=turns[idx]["user_id"] if turns else None,
                                       aspect=meta["aspect"], style=meta["style"], surface=meta.get("surface"), fix=meta.get("fix"),
                                       obf=meta.get("obf"), hard=meta["hard"]))
            continue
        rec = dict(id=uuid.uuid4().hex, pair=pair["pair"], intent_id=intent_id, text=text,
                   aspect=aspect, rule=rule, style=meta["style"], hard=meta["hard"])
        if actor == "user":
            rec["surface"] = meta["surface"]
            if meta.get("fix"):
                rec["fix"] = meta["fix"]
            if cell == "user_violate":
                rec["obf"] = meta["obf"]
                rec["anchor"] = anchor
        else:
            rec = dict(id=rec.pop("id"), user_id=turns[idx]["user_id"], **rec, reply_ok=reply_matches(r.get("reply_to"), turns[idx]["text"]))
        out.append(rec)
        accepted.add(idx)
    ctx["lost"] = [rows[i] for i in range(len(rows)) if i not in accepted]   # dòng kế hoạch không ra mẫu: sinh bù đúng thuộc tính
    return out


def merge(out_dir, stamp, merged_dir):
    """Phase cuối: ghép raw của một lần chạy thành MỘT file, mỗi dòng là một cặp (câu user, câu trợ lý), nối bằng `user_id`.
    Ra: <merged_dir>/V207_<STAMP>_pairs.jsonl. Câu user chưa có câu trả lời (và ngược lại) không vào file, chỉ được đếm."""
    mpath = manifest_path(out_dir, stamp)
    if not mpath.exists():
        sys.exit(f"Không thấy {mpath.name}: sai STAMP hoặc --dataset-dir")
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    meta = {p["pair"]: (i, p) for i, p in enumerate(load_pairs())}
    users = {}
    for cell in USER_CELLS:
        for r in read_cell(out_dir, stamp, cell):
            users[r["id"]] = (cell, r)
    rows, used, orphan = [], set(), 0
    for cell in ASSISTANT_CELLS:
        for a in read_cell(out_dir, stamp, cell):
            if a["user_id"] not in users:
                orphan += 1
                continue
            ucell, u = users[a["user_id"]]
            used.add(a["user_id"])
            p = meta[a["pair"]][1]
            rows.append(dict(
                id=a["id"], pair=a["pair"], tier=p["tier"], category=p["category"], channel=manifest["channel"],
                model=pair_model(p, manifest["model"], manifest.get("sensitive_model")),
                user_id=u["id"], user_intent_id=u["intent_id"], user_text=u["text"],
                user_verdict="VIOLATE" if ucell == "user_violate" else "SAFE",
                user_aspect=u["aspect"], user_rule=u.get("rule"), user_style=u["style"], user_surface=u["surface"], user_fix=u.get("fix"), user_obf=u.get("obf", False), user_hard=u["hard"],
                assistant_intent_id=a["intent_id"], assistant_text=a["text"],
                assistant_verdict="VIOLATE" if cell == "assistant_violate" else "SAFE",
                assistant_aspect=a["aspect"], assistant_rule=a.get("rule"), assistant_reply_ok=a.get("reply_ok"), assistant_style=a["style"], assistant_hard=a["hard"]))
    rows.sort(key=lambda r: (meta[r["pair"]][0], r["id"]))
    merged_dir.mkdir(parents=True, exist_ok=True)
    path = merged_dir / f"{PREFIX}_{stamp}_pairs.jsonl"
    tmp = path.with_suffix(".tmp")
    wr(tmp, "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    tmp.replace(path)
    export_gate(out_dir, stamp, rows)
    combo = Counter(r["user_verdict"][0] + r["assistant_verdict"][0] for r in rows)
    print(f"Merge {stamp}: {len(rows)} cặp → {path}")
    print("  combo (user→trợ lý):", dict(sorted(combo.items())))
    unused = len(users) - len(used)
    print(f"  câu user chưa có câu trả lời: {unused}; câu trả lời mồ côi (không thấy câu user): {orphan}" + ("  → chạy lại với --resume để bù" if unused or orphan else ""))
    return path


def dry_run(pairs, a):
    """Dựng prompt cho ĐỦ 4 ô × 2 kênh × các cặp đã chọn (ô assistant dùng câu user giả, dựng từ chính kế hoạch ô user),
    ghi vào generator/logs/dry/<kênh>/ và in báo cáo coverage."""
    cover, rows_stat, longest = Counter(), Counter(), 0
    for ch in ("voice", "typing"):
        d = LOGS_DIR / "dry" / ch
        d.mkdir(parents=True, exist_ok=True)
        for p in pairs:
            pn, fake, jobs = p["pair"], [], []
            for k, (cell, share, src) in enumerate(USER_SOURCES):
                for prompt, ctx in user_jobs(p, cell, share, a.N * SOURCE_UNITS[src], a.seed + 1000 * k, src, ch):
                    jobs.append((prompt, ctx))
                    fake += [dict(id=f"{pn}-{src}-{ctx['batch']}-{i}", cell=cell, text=f"[câu user giả {src}{i}]", hard=r["hard"], style=r["style"])
                             for i, r in enumerate(ctx["rows"])]
            alloc = allocate(pn, fake, a.seed)
            for cell in ASSISTANT_CELLS:
                jobs += assistant_jobs(p, cell, assistant_turn_sets(alloc, cell, set(), a.seed, pn), a.seed, ch)
            for prompt, ctx in jobs:
                wr(d / f"{pn}__{ctx['cell']}__{ctx['batch']}.md", prompt)
                longest = max(longest, len(prompt))
                cover[(ch, ctx["cell"])] += 1
                for r in ctx["rows"]:
                    rows_stat[(ch, "mẫu")] += 1
                    rows_stat[(ch, "HARD")] += r["hard"] == "HARD"
                    rows_stat[(ch, "né bộ lọc")] += bool(r["obf"])
                    rows_stat[(ch, "khía cạnh FREE")] += r["aspect"] == "FREE"
    print(f"Dry-run: {len(pairs)} cặp × 2 kênh × 4 ô")
    for key in sorted(cover):
        print(f"  {key[0]:6s} {key[1]:18s} {cover[key]} lô")
    for key in sorted(rows_stat):
        print(f"  {key[0]:6s} {key[1]}: {rows_stat[key]}")
    miss = [(ch, c) for ch in ("voice", "typing") for c in ALL_CELLS if not cover[(ch, c)]]
    print("  Thiếu coverage:", miss or "không")
    print(f"  Prompt dài nhất: {longest} ký tự. Ghi ở {LOGS_DIR / 'dry'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pairs", help="danh sách pair, phân cách dấu phẩy")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--N", type=int, default=1, help="hệ số cỡ mẫu: mỗi ô assistant = N × (VV+SV) = 40N mẫu")
    ap.add_argument("--include-abstract", action="store_true", help="cả cặp KHÁI QUÁT (chờ policy) — mặc định bỏ")
    ap.add_argument("--channel", choices=["voice", "typing"], default=DEFAULT_CHANNEL, help="kênh nhập liệu của người dùng (mặc định voice)")
    ap.add_argument("--cells", default=",".join(ALL_CELLS))
    ap.add_argument("--llm-model", dest="llm_model", default=None)
    ap.add_argument("--sensitive-llm-model", dest="sensitive_llm_model", default=None,
                    help=f'model sinh của nhóm nhạy cảm ("sensitive": true trong pairs.json); mặc định {SENSITIVE_LLM_MODEL} (--resume: model lần chạy cũ)')
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--seed", type=int, default=None, help="mặc định ngẫu nhiên; --resume thì dùng lại seed lần chạy cũ")
    ap.add_argument("--dataset-dir", type=Path, default=DATASET_DIR)
    ap.add_argument("--merge", metavar="STAMP", help="chỉ ghép raw của lần chạy STAMP thành file cặp (user, trợ lý), không sinh")
    ap.add_argument("--resume", metavar="STAMP", help="tiếp tục lần chạy cũ (dấu thời gian trong tên file raw, ví dụ 20261006_153012); bỏ trống = lần chạy mới")
    ap.add_argument("--dry-run", action="store_true", help="dựng prompt đủ 4 ô × 2 kênh (ô assistant dùng câu user giả), in coverage, không gọi LLM")
    ap.add_argument("--no-gate", action="store_true", help="tắt cổng lọc Jev + model ngoài sau mỗi bước")
    ap.add_argument("--gate-retries", type=int, default=2, help="số lượt sinh bù tối đa mỗi bước (phần bị cổng lọc hoặc anchor loại, model trả thiếu)")
    ap.add_argument("--review-model", default=None, help=f"model ngoài của cổng lọc; mặc định {DEFAULT_REVIEW_MODEL} (--resume: model lần chạy cũ)")
    a = ap.parse_args()

    if a.merge:
        raw_dir, merged_dir = run_dirs(a.dataset_dir, a.merge)
        merge(raw_dir, a.merge, merged_dir)
        return
    all_pairs = load_pairs()
    if a.all:
        pairs = all_pairs
    elif a.pairs:
        names = a.pairs.split(",")
        pairs = [p for p in all_pairs if p["pair"] in names]
        missing = set(names) - {p["pair"] for p in pairs}
        if missing:
            sys.exit("Không có pair: " + ", ".join(sorted(missing)))
    else:
        sys.exit("Cần --pairs hoặc --all")
    no_sub = [p["pair"] for p in pairs if missing_subprompts(p)]
    if no_sub:
        pairs = [p for p in pairs if p["pair"] not in no_sub]
        print("Bỏ cặp chưa có subprompt:", ", ".join(no_sub))
    if not a.include_abstract:
        skipped = [p["pair"] for p in pairs if is_abstract(p)]
        pairs = [p for p in pairs if p["pair"] not in skipped]
        if skipped:
            print("Bỏ cặp KHÁI QUÁT (chờ policy):", ", ".join(skipped))
    cells = [c for c in a.cells.split(",") if c in ALL_CELLS]

    if a.seed is None and not a.resume:
        a.seed = random.SystemRandom().randrange(1, 1_000_000)
        print(f"Seed ngẫu nhiên: {a.seed} (chạy lại y hệt: --seed {a.seed})")
    if a.dry_run:
        dry_run(pairs, a)
        return
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    import llm_core as core
    stamp = a.resume or datetime.now().strftime("%Y%m%d_%H%M%S")
    a.out_dir, a.merged_dir = run_dirs(a.dataset_dir, stamp)
    a.out_dir.mkdir(parents=True, exist_ok=True)
    mpath = manifest_path(a.out_dir, stamp)
    manifest = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else None
    if a.resume and not manifest:
        sys.exit(f"Không thấy {mpath.name}: sai --resume hoặc --dataset-dir")
    if manifest and manifest["channel"] != a.channel:
        sys.exit(f"Lần chạy {stamp} dùng kênh {manifest['channel']}, hãy chạy lại với --channel {manifest['channel']}")
    if a.seed is None:   # --resume không truyền --seed: dùng lại seed của lần chạy gần nhất
        a.seed = manifest["runs"][-1]["seed"]
        print(f"Dùng lại seed {a.seed} của lần chạy {stamp}")
    model = a.llm_model or (manifest["model"] if manifest else DEFAULT_LLM_MODEL)
    # lần chạy cũ chưa khai sensitive_model: nhóm nhạy cảm sinh tiếp bằng model chung, không đổi model giữa chừng
    a.sensitive_model = a.sensitive_llm_model or (manifest.get("sensitive_model") if manifest else SENSITIVE_LLM_MODEL)
    sensitive = [p["pair"] for p in pairs if pair_model(p, model, a.sensitive_model) != model]
    auths = {m: core.build_auth(m) for m in {pair_model(p, model, a.sensitive_model) for p in pairs}}
    # cổng lọc: lần chạy mới bật trừ khi --no-gate; --resume theo lần chạy cũ (lần chạy cũ không có cổng thì không lọc câu đã sinh)
    a.gate = not a.no_gate and (manifest.get("gate", False) if manifest else True)
    if a.gate:
        from llm_openrouter import load_api_key
        a.review_model = a.review_model or (manifest or {}).get("review_model") or DEFAULT_REVIEW_MODEL
        load_api_key(None)               # Jev đi qua OpenRouter: thiếu key thì dừng ngay, không để cổng lọc lặng lẽ không lọc
        core.build_auth(a.review_model)
    manifest = manifest or dict(stamp=stamp, channel=a.channel, model=model, sensitive_model=a.sensitive_model, gate=a.gate,
                                review_model=a.review_model if a.gate else None, runs=[])
    manifest["runs"].append(dict(time=datetime.now().isoformat(timespec="seconds"), N=a.N, seed=a.seed, cells=cells,
                                 **({"sensitive_model": a.sensitive_model} if sensitive else {}),
                                 pairs=[p["pair"] for p in pairs], gate=a.gate))
    wr(mpath, json.dumps(manifest, ensure_ascii=False, indent=1))
    log_f = open(LOGS_DIR / f"{PREFIX}_{stamp}.jsonl", "a", encoding="utf-8", newline="\n")
    sens_pv = getattr(auths.get(a.sensitive_model), "providers", None)   # backend OpenRouter đã ghim (nhánh khác không có)
    print(f"Lần chạy {stamp} (kênh {a.channel}, model {model}"
          + (f", nhóm nhạy cảm {a.sensitive_model}" + (f" @ {','.join(sens_pv)}" if sens_pv else "") + f": {len(sensitive)} cặp" if sensitive else "")
          + (f", cổng lọc Jev + {a.review_model}" if a.gate else ", không cổng lọc") + f") → {a.out_dir}")

    last_call = {}   # generate_all ghi giờ nhận xong kết quả của lời gọi LLM gần nhất (cả lời gọi chấm của cổng lọc)
    gate_stats = {}
    try:
        generate_all(a, pairs, cells, stamp, auths, model, log_f, last_call, gate_stats)
    finally:   # end_time = lúc lời gọi LLM cuối cùng trả về (không tính ghép merged); ghi cả khi lỗi hay Ctrl+C
        end = last_call.get("t") or datetime.now()   # không có lời gọi nào → lúc dừng
        manifest["runs"][-1]["end_time"] = end.isoformat(timespec="seconds")
        if gate_stats:
            manifest["runs"][-1]["gate_stats"] = {k: dict(v) for k, v in gate_stats.items()}
        wr(mpath, json.dumps(manifest, ensure_ascii=False, indent=1))
        log_f.close()


def rel_script(path):
    """Đường dẫn script tương đối với thư mục đang đứng (để in lệnh copy chạy được), dấu /."""
    path = Path(path).resolve()
    try:
        path = path.relative_to(Path.cwd())
    except ValueError:
        pass
    return path.as_posix()


def resume_cmd(a, stamp):
    """Lệnh --resume đầy đủ để copy chạy lại (seed, model lấy lại từ _run.json)."""
    parts = ["python3", rel_script(__file__), "--resume", stamp, "--channel", a.channel]
    parts += ["--all"] if a.all else ["--pairs", a.pairs]
    if a.N != 1:
        parts += ["--N", str(a.N)]
    if a.cells != ",".join(ALL_CELLS):
        parts += ["--cells", a.cells]
    if a.include_abstract:
        parts.append("--include-abstract")
    if a.gate_retries != 2:
        parts += ["--gate-retries", str(a.gate_retries)]
    if a.dataset_dir.resolve() != DATASET_DIR.resolve():
        parts += ["--dataset-dir", a.dataset_dir.as_posix()]
    return " ".join(parts)


def user_src(cell, row):
    """Nguồn câu user (V / G / R) của một dòng kế hoạch hoặc một bản ghi."""
    return "V" if cell == "user_violate" else ("G" if row["hard"] == "HARD" else "R")


def build_jobs(a, pairs, stage, cells, existing, lost, rnd):
    """Lô cần sinh để đủ mục tiêu của bước (user hoặc assistant), trừ phần đã có trong raw."""
    jobs = []
    for p in pairs:
        pn = p["pair"]
        if stage is USER_CELLS:
            have = Counter(source_of(r) for c in USER_CELLS for r in existing[c] if r["pair"] == pn)
            for k, (cell, share, src) in enumerate(USER_SOURCES):
                if cell not in cells:
                    continue
                need = round(a.N * SOURCE_UNITS[src] * OVERGEN) - have[src]
                if need > 0:
                    pool = lost.get((pn, src), [])
                    reuse, lost[(pn, src)] = pool[:need], pool[need:]
                    jobs += user_jobs(p, cell, share, need, a.seed + 1000 * k + have[src], src if not rnd else f"{src}r{rnd}_",
                                      a.channel, reuse)
        else:
            user_recs = [r for c in USER_CELLS for r in existing[c] if r["pair"] == pn]
            if not user_recs:
                if not rnd:
                    print(f"  bỏ {pn}: chưa có câu user (chạy bước 1 trước)")
                continue
            assigned = {r["user_id"]: c for c in ASSISTANT_CELLS for r in existing[c] if r["pair"] == pn}
            alloc = allocate(pn, user_recs, a.seed, assigned)
            for cell in [c for c in ASSISTANT_CELLS if c in cells]:
                done = {r["user_id"] for r in existing[cell] if r["pair"] == pn}
                jobs += assistant_jobs(p, cell, assistant_turn_sets(alloc, cell, done, a.seed, pn), a.seed + len(existing[cell]), a.channel)
    return jobs


def run_jobs(a, stamp, jobs, existing, lost, log_f, last_call, auths, model):
    """Gọi LLM cho các lô, ghi raw + dropped theo từng lô; dòng không ra mẫu vào `lost` để sinh bù đúng thuộc tính.
    Lô của nhóm nhạy cảm gọi model riêng (`pair_model`): mỗi model một lượt stream, lần lượt nhau."""
    import llm_core as core
    done_n = bad = 0
    by_model = {}
    for job in jobs:
        by_model.setdefault(pair_model(job[1]["pair"], model, a.sensitive_model), []).append(job)
    streams = (core.stream_batches(auths[m], m, js, workers=a.workers) for m, js in by_model.items())
    for ctx, results, meta in itertools.chain.from_iterable(streams):
        last_call["t"] = datetime.now()
        recs = to_records(ctx, results or [])
        expected = len(ctx["rows"])
        with open(out_path(a.out_dir, stamp, ctx["cell"]), "a", encoding="utf-8", newline="\n") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        if ctx.get("dropped"):
            with open(out_path(a.out_dir, stamp, "dropped"), "a", encoding="utf-8", newline="\n") as f:
                for r in ctx["dropped"]:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        if ctx["cell"] in USER_CELLS:
            for row in ctx.get("lost", []):
                lost.setdefault((ctx["pair"]["pair"], user_src(ctx["cell"], row)), []).append(row)
        existing[ctx["cell"]] += [dict(r, cell=ctx["cell"]) for r in recs]
        done_n += 1
        bad += len(recs) < expected
        log_f.write(json.dumps(dict(pair=ctx["pair"]["pair"], cell=ctx["cell"], batch=ctx["batch"], expected=expected, got=len(recs),
                                    **{k: meta.get(k) for k in ("latency_s", "tokens_in", "tokens_out", "error")}), ensure_ascii=False) + "\n")
        log_f.flush()
        print(f"  [{done_n}/{len(jobs)}] {ctx['pair']['pair']}/{ctx['cell']} lô {ctx['batch']}: {len(recs)}/{expected}", meta.get("error") or "")
    print(f"  xong: {done_n} lô, {bad} lô thiếu mẫu")


def gate_paths(out_dir, stamp):
    """Kết quả chấm của cổng lọc, khoá theo id bản ghi raw (merge chuyển sang check/ theo khoá id_dòng:phía)."""
    return out_path(out_dir, stamp, "gate_jev"), out_path(out_dir, stamp, "gate_review")


GATE_DROP = ("relabel", "wrong_subject", "unclear", "fix_text")   # gợi ý của qc_common.review_action mà cổng lọc loại


def gate(a, stamp, stage, existing, lost, last_call, stats):
    """Cổng lọc sau mỗi bước: Jev chấm mọi câu mới → model ngoài (mặc định gemini) chấm lại vùng đỏ + vàng →
    loại câu mà CẢ HAI cùng chấm ngược nhãn gán (gợi ý relabel), model ngoài thấy lệch chủ đề (wrong_subject),
    không phân định được (unclear) hoặc báo text hỏng (fix_text). Bất đồng ở vùng vàng được giữ (vào phiếu người ở hậu kiểm).
    Câu bị loại: xoá khỏi raw, ghi vào _dropped.jsonl (reason=gate); câu user bị loại → thuộc tính vào `lost` để sinh bù."""
    sys.path.insert(0, str(ROOT / "dataset"))
    import qc_common as C, jev_check as JC, review_check as RC
    gj, gr = gate_paths(a.out_dir, stamp)
    items = [dict(key=r["id"], h=C.text_hash(r["text"]), intent=r["intent_id"], text=r["text"], cell=c,
                  assigned="VIOLATE" if c.endswith("violate") else "SAFE", rec=r)
             for c in stage if c in a.cells_list for r in existing[c]]
    jev = C.load_results(gj, items)
    todo = [it for it in items if it["key"] not in jev]
    if todo:
        print(f"Cổng lọc: Jev chấm {len(todo)} câu")
        JC.run_model(JC.DEFAULT_MODEL, todo, gj, 10, 8)
        last_call["t"] = datetime.now()
        jev = C.load_results(gj, items)
    zone = C.zones(items, jev, JC.DEFAULT_THRESHOLD)
    if len(jev) < len(items):
        print(f"  ⚠ Jev lỗi {len(items) - len(jev)} câu: không lọc được, để hậu kiểm chấm lại")
    cand = [it for it in items if zone.get(it["key"]) in ("red", "yellow")]
    rv = C.load_results(gr, items)
    todo = [it for it in cand if it["key"] not in rv]
    if todo:
        print(f"Cổng lọc: {a.review_model} chấm lại {len(todo)} câu đỏ/vàng")
        RC.run(a.review_model, todo, gr, 10, 4)
        last_call["t"] = datetime.now()
        rv = C.load_results(gr, items)
        if len([it for it in cand if it["key"] in rv]) < len(cand):
            print(f"  ⚠ {a.review_model} lỗi {len(cand) - sum(it['key'] in rv for it in cand)} câu: giữ lại, để hậu kiểm chấm lại")
    reject = []
    for it in cand:
        r = rv.get(it["key"])
        act = C.review_action(it, zone[it["key"]], r)[0] if r else None
        if act in GATE_DROP:
            reject.append((it, act))
    st = stats.setdefault("user" if stage is USER_CELLS else "assistant", Counter())
    st["jev"] = len(jev)
    st["red"] = sum(zone.get(it["key"]) == "red" for it in items)
    st["yellow"] = sum(zone.get(it["key"]) == "yellow" for it in items)
    st["rejected"] += len(reject)
    if not reject:
        return 0
    bad_ids = {it["key"] for it, _ in reject}
    with open(out_path(a.out_dir, stamp, "dropped"), "a", encoding="utf-8", newline="\n") as f:
        for it, act in reject:
            r, j, v = it["rec"], jev[it["key"]], rv[it["key"]]
            f.write(json.dumps(dict(pair=r["pair"], cell=it["cell"], reason="gate_" + act, id=r["id"], user_id=r.get("user_id"),
                                    intent_id=r["intent_id"], text=r["text"], zone=zone[it["key"]], jev_label=j["label"], jev_prob=j["prob"],
                                    review_verdict=C.verdict_of(v), review_matched=v.get("matched"), review_partial=v.get("partial"),
                                    on_topic=v.get("on_topic"),
                                    review_reason=v.get("reason"), text_broken=v.get("text_broken"),
                                    **{k: r.get(k) for k in ("rule", "aspect", "style", "surface", "fix", "obf", "hard")}), ensure_ascii=False) + "\n")
    for c in stage:
        if not any(it["cell"] == c for it, _ in reject):
            continue
        for it, _ in reject:
            if it["cell"] == c and c in USER_CELLS:
                r = it["rec"]
                lost.setdefault((r["pair"], source_of(dict(r, cell=c))), []).append(
                    dict(aspect=r["aspect"], style=r["style"], surface=r["surface"], fix=r.get("fix"), obf=r.get("obf", False), hard=r["hard"]))
        existing[c] = [r for r in existing[c] if r["id"] not in bad_ids]
        path = out_path(a.out_dir, stamp, c)
        keep = [r for r in read_jsonl(path) if r["id"] not in bad_ids]
        tmp = path.with_suffix(".tmp")
        wr(tmp, "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in keep))
        tmp.replace(path)
    by = Counter(it["cell"] for it, _ in reject)
    print(f"Cổng lọc: loại {len(reject)} câu ({', '.join(f'{c} {n}' for c, n in sorted(by.items()))}) → {out_path(a.out_dir, stamp, 'dropped').name}")
    return len(reject)


def export_gate(out_dir, stamp, rows):
    """Chuyển kết quả cổng lọc sang check/jev.jsonl, check/review.jsonl theo khoá hậu kiểm (id_dòng:phía),
    để bước 1 và 2 của hậu kiểm không chấm lại (chỉ còn mẫu xanh cho model ngoài). Bỏ qua bản đã có cùng khoá và mã băm."""
    gj, gr = gate_paths(out_dir, stamp)
    if not gj.exists():
        return
    sys.path.insert(0, str(ROOT / "dataset"))
    import qc_common as C
    check = out_dir.parent / "check"
    check.mkdir(parents=True, exist_ok=True)
    keys = {}   # id bản ghi raw → (khoá hậu kiểm, mã băm text)
    for r in rows:
        keys[r["user_id"]] = (f"{r['id']}:user", C.text_hash(r["user_text"]))
        keys[r["id"]] = (f"{r['id']}:assistant", C.text_hash(r["assistant_text"]))
    for src, dst in ((gj, check / "jev.jsonl"), (gr, check / "review.jsonl")):
        have = {(d.get("key"), d.get("h")) for d in C.read_jsonl(dst) if "error" not in d}
        add = []
        for d in C.read_jsonl(src):
            k = keys.get(d.get("key"))
            if "error" in d or not k or d.get("h") != k[1] or k in have:
                continue
            have.add(k)
            add.append(dict(d, key=k[0], gate=True))
        if add:
            with open(dst, "a", encoding="utf-8", newline="\n") as f:
                for d in add:
                    f.write(json.dumps(d, ensure_ascii=False) + "\n")
            print(f"  chuyển {len(add)} kết quả cổng lọc → check/{dst.name}")


def generate_all(a, pairs, cells, stamp, auths, model, log_f, last_call, gate_stats):
    """Bước 1 (câu user) rồi bước 2 (câu trợ lý). Mỗi bước chạy theo lượt: sinh → cổng lọc (nếu bật) → sinh bù phần thiếu
    (đúng thuộc tính dòng bị mất), tối đa --gate-retries lượt bù; cuối cùng ghép merged."""
    existing = {c: read_cell(a.out_dir, stamp, c) for c in ALL_CELLS}
    lost = {}   # (cặp, nguồn V/G/R) → thuộc tính các dòng user bị mất, dùng cho lượt sinh bù
    a.cells_list = cells
    t0 = time.time()
    for stage in (USER_CELLS, ASSISTANT_CELLS):
        if not [c for c in stage if c in cells]:
            continue
        name = "1 (user)" if stage is USER_CELLS else "2 (assistant)"
        for rnd in range(a.gate_retries + 2):
            if a.gate:   # lượt 0: lọc cả câu cũ chưa qua cổng (--resume sau khi dừng giữa chừng)
                gate(a, stamp, stage, existing, lost, last_call, gate_stats)
            jobs = build_jobs(a, pairs, stage, cells, existing, lost, rnd)
            if not jobs:
                break
            if rnd > a.gate_retries:
                print(f"  Bước {name}: đã sinh bù {a.gate_retries} lượt, còn thiếu {sum(len(c['rows']) for _, c in jobs)} mẫu → dừng")
                break
            print(f"Bước {name}" + (f", lượt bù {rnd}" if rnd else "") + f": {len(jobs)} lô")
            run_jobs(a, stamp, jobs, existing, lost, log_f, last_call, auths, model)
    print("Tổng thời gian " + hms(time.time() - t0))
    asst = [r for c in ASSISTANT_CELLS for r in existing[c] if "reply_ok" in r]
    if asst:
        bad = sum(not r["reply_ok"] for r in asst)
        print(f"reply_to lệch câu user cùng dòng: {bad}/{len(asst)} câu trả lời (chỉ ghi cờ reply_ok, không loại)")
    if gate_stats:
        for side, st in gate_stats.items():
            print(f"Cổng lọc {side}: Jev {st['jev']} câu (đỏ {st['red']}, vàng {st['yellow']}), loại {st['rejected']}")
    if any(c in cells for c in ASSISTANT_CELLS):
        merge(a.out_dir, stamp, a.merged_dir)
    # tổng kết cuối (in sau cùng để không bị trôi): còn thiếu so với mục tiêu thì nhắc lệnh bù trước khi hậu kiểm
    miss_user, miss_asst = 0, 0
    for p in pairs:
        pn = p["pair"]
        have = Counter(source_of(r) for c in USER_CELLS for r in existing[c] if r["pair"] == pn)
        miss_user += sum(max(0, round(a.N * SOURCE_UNITS[src] * OVERGEN) - have[src]) for cell, _, src in USER_SOURCES if cell in cells)
        answered = {r["user_id"] for c in ASSISTANT_CELLS for r in existing[c] if r["pair"] == pn}
        if any(c in cells for c in ASSISTANT_CELLS):
            miss_asst += sum(1 for c in USER_CELLS for r in existing[c] if r["pair"] == pn and r["id"] not in answered)
    if miss_user or miss_asst:
        print(f"⚠ CÒN THIẾU: {miss_user} câu user, {miss_asst} câu user chưa có câu trả lời. Bù bằng lệnh (rồi mới hậu kiểm):\n    "
              + resume_cmd(a, stamp))
    elif any(c in cells for c in ASSISTANT_CELLS):
        print("Đủ mẫu. Hậu kiểm (xem dataset/README.md), chạy lần lượt:\n" + "\n".join("  " + c for c in postcheck_cmds(a, stamp)))


def hms(sec):
    """450 -> '7m 30s', 7384 -> '2h 3m 4s' (bỏ đơn vị đầu bằng 0)."""
    sec = int(round(sec))
    h, m, x = sec // 3600, (sec % 3600) // 60, sec % 60
    return " ".join(([f"{h}h"] if h else []) + ([f"{m}m"] if h or m else []) + [f"{x}s"])


def postcheck_cmds(a, stamp):
    """Các lệnh hậu kiểm theo thứ tự (bước 0, 1, 2, 4 trong dataset/README.md) để copy chạy."""
    run = stamp if a.dataset_dir.resolve() == DATASET_DIR.resolve() else (a.dataset_dir / stamp).as_posix()
    d = lambda name: rel_script(DATASET_DIR / name)
    return [f"python3 {d('inspect_dataset.py')} {run}",
            f"python3 {d('jev_check.py')} {run}",
            f"python3 {d('review_check.py')} {run} --xlsx",
            f"python3 {d('report_dataset.py')} {run}"]


if __name__ == "__main__":
    main()
