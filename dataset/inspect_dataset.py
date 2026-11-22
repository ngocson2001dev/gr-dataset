r"""Soi dataset merged để phát hiện lỗi có hệ thống: thống kê, gợi ý vùng có vấn đề, gắn cờ từng dòng. Tất định, không gọi model.

Tầng 1: luật theo từng dòng (lỗi hình thức, thuộc tính sai). Tầng 2: thống kê cả tập (phân bổ lệch, mẫu câu lặp, trùng lặp)
và chỉ ra bề mặt / pair / cụm từ nào đang có vấn đề. Kết quả là gợi ý để người rà soát, không tự sửa dữ liệu.

Bước 0 của hậu kiểm (chạy trước Jev để không trả tiền chấm câu đằng nào cũng phải sửa). Đọc merged đã phủ bản sửa trong
check/work/decisions.jsonl. Câu có lỗi ERROR được đưa vào phiếu cho người (review_todo.xlsx, do review_check.py ghi) và
không vào dataset cuối cho tới khi được sửa.

Chạy từ root folder (Windows):
  python intents-vita-207/dataset/inspect_dataset.py 20261006_231257

  <run>          STAMP của lần chạy (thư mục dataset/<STAMP>) hoặc đường dẫn thư mục đó (bắt buộc).
  --xlsx         Ghi thêm inspect.xlsx (các dòng bị cờ để người xem). Mặc định: tắt.

Ra (trong dataset/<STAMP>/check/work/):
  inspect.md     báo cáo tổng hợp (số lỗi theo mã, thống kê tầng 2, cảnh báo)
  inspect.xlsx   (chỉ khi --xlsx) các dòng bị cờ: id, pair, mã lỗi, text
Thoát với mã 1 nếu có lỗi mức ERROR.

Mức độ: ERROR = sai hẳn (chắc chắn phải sửa); WARN = nghi ngờ (người xem); INFO = chỉ thống kê.
Ngưỡng cảnh báo tầng 2 nằm ở THRESH bên dưới.
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "generator"))   # import hằng số từ generate.py
import generate as G  # noqa: E402  hằng số phân bổ, tên cấm, kênh
sys.path.insert(0, str(Path(__file__).resolve().parent))
import qc_common as C  # noqa: E402

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

L = r"[^\W\d_]"  # một chữ cái unicode (kể cả tiếng Việt có dấu)
VI_PARTICLES = set("àáạảãýỳỵỷỹởờơôêếềệểễưừứựửữ")   # từ một chữ của tiếng Việt, không phải chữ cái đánh vần


class SpacedLetters:
    """Chuỗi ≥3 chữ cái rời cách nhau bằng khoảng trắng; bỏ các từ một chữ tiếng Việt (à, ý, ạ, ở, ê…) dính ở hai đầu chuỗi."""
    RUN = re.compile(rf"(?<!\w){L}(?: {L}){{2,}}(?!\w)")

    def search(self, txt):
        for m in self.RUN.finditer(txt):
            t = m.group().split(" ")
            while t and t[0].lower() in VI_PARTICLES:
                t.pop(0)
            while t and t[-1].lower() in VI_PARTICLES:
                t.pop()
            if len(t) >= 3:
                return m
        return None


PATTERNS = {   # lỗi né bộ lọc sai kênh: tách chữ, gạch nối, ký tự chèn, chấm lửng giữa từ, khoảng trắng lạ
    "spaced_letters": SpacedLetters(),                                          # "H ồ i", "T r u n g Q u o c"
    "hyphenated": re.compile(rf"(?<![\w-]){L}+(?:-{L}+){{2,}}(?![\w-])"),     # "Cam-pu-chia"
    "inserted_chars": re.compile(rf"(?<!\w){L}(?:[.\u00b7\u2022*_/\-]{L}){{2,}}(?!\w)"),   # "V.N.C.H"
    "mid_ellipsis": re.compile(rf"{L}+(?:\.{{2,}}|\u2026){L}+"),              # "Tr...ung"
    "odd_whitespace": re.compile("[\u200b\u200c\u200d\u2060\ufeff\u00a0\u2009\u202f]"),
}

THRESH = {
    "filler_open_share": 0.30,   # tỉ lệ câu user mở đầu bằng từ đệm (OPENER_WORDS) trong một bề mặt vượt mức này → cảnh báo
    "tu_sua_khuon": 0.30,        # tỉ lệ khuôn "à không…" trong bề mặt "Tự sửa giữa câu"
    "dist_gap": 0.05,            # chênh lệch tuyệt đối giữa tỉ lệ thực và tỉ lệ phân bổ (toàn tập)
    "ngram_share": 0.03,         # một cụm 4 từ xuất hiện ở quá tỉ lệ này số dòng user
    "near_dup": 0.8,             # Jaccard trên cụm 3 từ trong cùng pair
    "short_words": 20,           # "Nói ngắn" (<15 từ) vượt ngưỡng này → WARN
    "min_words_user": 3,
    "max_words_user": 150,
    "min_words_assistant": 5,
}
OPENER_WORDS = {"à", "ừm", "ờ", "ơ", "ừ", "thì", "ờm", "ừa", "dạ", "ê", "này"}
KHUON_CHINH = re.compile(r"à không|ý (tôi|em|mình) là", re.I)   # hai cụm bị lạm dụng nhất
TU_SUA_KHUON = re.compile(r"à không|à nhầm|ý (tôi|em|mình) là|không phải.{0,40}(mà|là) |nói lại|đúng hơn", re.I)
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
CJK = re.compile("[぀-ヿ㐀-䶿一-鿿가-힯]")
MARKDOWN = re.compile(r"\*\*|`|^\s*#{1,6}\s|^\s*[-*•]\s|^\s*\d+\.\s", re.M)
PLACEHOLDER = re.compile(r"\[[^\]\n]{1,40}\]|\{\{|\}\}|<[^>\n]{1,40}>")
VOICE_BAD = re.compile(r"[\"'“”‘’:]|\.\.\.|…")
XO = r"(?:b|c|ch|d|đ|g|gh|h|k|kh|l|m|n|ng|nh|p|ph|q|r|s|t|th|tr|v|x)ờ"   # tên chữ cái kiểu "vờ", "phờ", "nờ"
_VW = r"(?:i|a|e|o|ê|ô|ơ|u|ư|y|ạm|ạch|ương|uợng|ép|en|tê|vê)"
# đánh vần tên: "vờ i nờ", "phờ ạm" (tên chữ + vần), hoặc ≥3 tên chữ liền ("tờ rờ ô"); 2 tên chữ liền như "lờ đờ" là từ thật, không bắt
LETTER_SPELL = re.compile(rf"(?i)(?<!\w)(?:{XO}\s+{_VW}|{XO}\s+{XO}\s+(?:{XO}|{_VW}))(?!\w)")
CAPS_WORD = re.compile(r"\b[A-ZÀ-Ỹ]{4,}\b")

SEV = {}
def code(name, sev):
    SEV[name] = sev
    return name


def words(s):
    return re.findall(r"\w+", s.lower())


def valid_assistant_styles(verdict):
    return set(G.STYLES["assistant_violate"]) if verdict == "VIOLATE" else (
        set(G.STYLES["assistant_safe_refuse"]) | set(G.STYLES["assistant_safe_help"]))


def row_checks(r, channel):
    """Trả danh sách mã lỗi của một dòng (tầng 1)."""
    out = []
    ut, at = r["user_text"] or "", r["assistant_text"] or ""
    for who, txt in (("user", ut), ("assistant", at)):
        for name, rx in PATTERNS.items():
            if rx.search(txt):
                if who == "user" and channel == "typing" and r["user_obf"] and name != "odd_whitespace":   # typing: né bộ lọc bằng thị giác là đúng yêu cầu prompt
                    out.append(code(f"user_{name}_obf", "INFO"))
                    continue
                soft = name == "odd_whitespace" or (who == "assistant" and name in ("hyphenated", "inserted_chars"))   # trợ lý hay có tên miền, thuật ngữ có gạch nối
                out.append(code(f"{who}_{name}", "WARN" if soft else "ERROR"))
        if re.search(G.FORBIDDEN, txt):
            out.append(code(f"{who}_forbidden_name", "ERROR"))
        if not r["pair"].startswith("vingroup_") and re.search(G.FORBIDDEN_NON_VINGROUP, txt):
            out.append(code(f"{who}_forbidden_name_vingroup", "ERROR"))
        if PLACEHOLDER.search(txt):
            out.append(code(f"{who}_placeholder", "WARN"))
        if CJK.search(txt):
            out.append(code(f"{who}_cjk", "ERROR"))
        if EMOJI.search(txt):
            typing_user = who == "user" and channel == "typing"   # kênh gõ cho phép emoji (channels.json)
            out.append(code("user_emoji_typing", "WARN") if typing_user else code(f"{who}_emoji", "ERROR"))
        if not txt.strip():
            out.append(code(f"{who}_empty", "ERROR"))
    # kênh voice: ký hiệu văn bản mà ASR không xuất ra (theo channels.json)
    if channel == "voice":
        if VOICE_BAD.search(ut):
            out.append(code("user_voice_forbidden_char", "ERROR"))
        if "\n" in ut or MARKDOWN.search(ut):
            out.append(code("user_voice_newline_markdown", "ERROR"))
        if LETTER_SPELL.search(ut):   # đánh vần tên bằng tên chữ cái: người nói thật không nói vậy, model hay đánh vần sai
            out.append(code("user_voice_letter_spelling", "WARN"))
        if CAPS_WORD.search(ut):
            out.append(code("user_voice_caps_word", "WARN"))
    # trợ lý: văn xuôi liền mạch, không markdown/gạch đầu dòng
    if MARKDOWN.search(at):
        out.append(code("assistant_markdown", "ERROR"))
    # độ dài
    nu, na = len(words(ut)), len(words(at))
    if nu < THRESH["min_words_user"]:
        out.append(code("user_too_short", "WARN"))
    if nu > THRESH["max_words_user"]:
        out.append(code("user_too_long", "WARN"))
    if na < THRESH["min_words_assistant"]:
        out.append(code("assistant_too_short", "WARN"))
    if r["user_surface"] in ("Nói ngắn", "Viết ngắn") and nu >= THRESH["short_words"]:
        out.append(code("user_short_but_long", "WARN"))   # sai thuộc tính bề mặt, nhãn vẫn đúng → không chặn khỏi dataset cuối
    # thuộc tính hợp lệ
    cell = "user_violate" if r["user_verdict"] == "VIOLATE" else "user_safe"
    if r["user_style"] not in G.CONTENT_WEIGHTS[cell]:
        out.append(code("user_invalid_style", "ERROR"))
    if r["user_surface"] not in G.SURFACE_WEIGHTS[channel]:
        out.append(code("user_invalid_surface", "ERROR"))
    allowed = G.SURFACE_ALLOWED.get(r["user_surface"])
    if allowed and r["user_style"] not in allowed:
        legacy = r["user_style"] == "ROLE" and r["user_surface"] in ("Nói ngắn", "Viết ngắn")   # dataset sinh trước 2026-10-09 còn ghép ROLE với câu ngắn: chỉ cảnh báo
        out.append(code("surface_style_role_short", "WARN") if legacy else code("surface_style_mismatch", "ERROR"))
    if r["user_obf"]:
        if r["user_verdict"] != "VIOLATE":
            out.append(code("obf_on_safe", "ERROR"))
        if r["user_style"] in G.OBFUSCATION_EXCLUDE or r["user_surface"] in G.OBFUSCATION_EXCLUDE_SURFACES:
            out.append(code("obf_invalid", "ERROR"))
    if r["assistant_style"] not in valid_assistant_styles(r["assistant_verdict"]):
        out.append(code("assistant_invalid_style", "ERROR"))
    if r.get("assistant_reply_ok") is False:   # reply_to model chép không khớp câu user cùng dòng: có thể trả lời lệch dòng
        out.append(code("assistant_reply_mismatch", "WARN"))
    if r["assistant_aspect"] == "?":   # model tự chọn khía cạnh nhưng trả mã ngoài danh sách (xem generate.to_records)
        out.append(code("assistant_unknown_aspect", "WARN"))
    if r["assistant_style"] == "FICTION" and r["user_style"] != "FICTION":
        out.append(code("assistant_fiction_without_user_fiction", "WARN"))
    if r["user_style"] == "FICTION" and r["assistant_verdict"] == "VIOLATE" and r["assistant_style"] != "FICTION":
        out.append(code("assistant_ignores_fiction", "WARN"))
    # kiểu mẫu câu (INFO ở mức dòng, cảnh báo ở tầng 2)
    first = (words(ut) or [""])[0]
    if first in OPENER_WORDS:
        out.append(code("user_filler_opener", "INFO"))
    if r["user_surface"] == "Tự sửa giữa câu" and TU_SUA_KHUON.search(ut):
        out.append(code("user_self_correct_template", "INFO"))
    return out


def shingles(s, k=3):
    w = words(s)
    return {" ".join(w[i:i + k]) for i in range(max(1, len(w) - k + 1))}


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "–"


def stage2(rows, channel):
    """Thống kê cả tập (tầng 2). Trả (dòng báo cáo markdown, cờ theo id)."""
    md, flags = [], collections.defaultdict(list)
    n = len(rows)

    # 1. mở đầu bằng từ đệm theo bề mặt
    md.append("## T2.1 Từ mở đầu câu user theo bề mặt")
    by_surf = collections.defaultdict(list)
    for r in rows:
        by_surf[r["user_surface"]].append(r)
    md.append("| bề mặt | số câu | mở bằng từ đệm | từ mở đầu phổ biến nhất |\n|---|---|---|---|")
    for s, rs in sorted(by_surf.items(), key=lambda x: -len(x[1])):
        c = collections.Counter((words(r["user_text"]) or [""])[0] for r in rs)
        filler = sum(v for k, v in c.items() if k in OPENER_WORDS)
        top, tv = c.most_common(1)[0]
        over = filler / len(rs) > THRESH["filler_open_share"]
        md.append(f"| {s} | {len(rs)} | {pct(filler, len(rs))}{' ⚠' if over else ''} | “{top}” {pct(tv, len(rs))} |")
        if over:
            for r in rs:
                if (words(r["user_text"]) or [""])[0] in OPENER_WORDS:
                    flags[r["id"]].append(code("t2_filler_opener_excess", "WARN"))

    # 2. khuôn tự sửa
    rs = by_surf.get("Tự sửa giữa câu", [])
    if rs and any(r.get("user_fix") for r in rs):   # dataset có giao cách sửa từng dòng: đo theo cách sửa
        md.append("\n## T2.2 Cách sửa trong “Tự sửa giữa câu” (có “à không / ý tôi là”)")
        md.append("| cách sửa | số câu | có à không / ý tôi là |\n|---|---|---|")
        for m in G.SELF_CORRECT_MODES:
            sub = [r for r in rs if r.get("user_fix") == m]
            k = [r for r in sub if KHUON_CHINH.search(r["user_text"])]
            wrong = m != "từ đính chính"   # chỉ cách "từ đính chính" được dùng hai cụm này
            md.append(f"| {m} | {len(sub)} | {len(k)} ({pct(len(k), len(sub))}){' ⚠' if wrong and k else ''} |")
            for r in k if wrong else []:
                flags[r["id"]].append(code("t2_self_correct_wrong_mode", "WARN"))
    elif rs:
        k = [r for r in rs if TU_SUA_KHUON.search(r["user_text"])]
        md.append(f"\n## T2.2 Khuôn “à không / ý tôi là…” trong “Tự sửa giữa câu”\n{len(k)}/{len(rs)} = {pct(len(k), len(rs))}"
                  + (" ⚠" if len(k) / len(rs) > THRESH["tu_sua_khuon"] else ""))
        if len(k) / len(rs) > THRESH["tu_sua_khuon"]:
            for r in k:
                flags[r["id"]].append(code("t2_self_correct_template_excess", "WARN"))

    # 3. phân bổ thực tế so với phân bổ cấu hình (toàn tập, theo ô user)
    md.append("\n## T2.3 Phân bổ thực tế so với cấu hình (toàn tập)")
    md.append("| trục | giá trị | thực tế | cấu hình | lệch |\n|---|---|---|---|---|")
    gaps = 0
    for cell, verdict in (("user_violate", "VIOLATE"), ("user_safe", "SAFE")):
        sub = [r for r in rows if r["user_verdict"] == verdict]
        if not sub:
            continue
        w = G.CONTENT_WEIGHTS[cell]
        tot = sum(w.values())
        for key, want in w.items():
            have = sum(1 for r in sub if r["user_style"] == key) / len(sub)
            gap = have - want / tot
            gaps += abs(gap) > THRESH["dist_gap"]
            md.append(f"| {cell} cách hỏi | {key} | {100*have:.1f}% | {100*want/tot:.1f}% | {100*gap:+.1f}{' ⚠' if abs(gap) > THRESH['dist_gap'] else ''} |")
        sw = G.SURFACE_WEIGHTS[channel]
        stot = sum(sw.values())
        for key, want in sw.items():
            have = sum(1 for r in sub if r["user_surface"] == key) / len(sub)
            gap = have - want / stot
            gaps += abs(gap) > THRESH["dist_gap"]
            md.append(f"| {cell} bề mặt | {key} | {100*have:.1f}% | {100*want/stot:.1f}% | {100*gap:+.1f}{' ⚠' if abs(gap) > THRESH['dist_gap'] else ''} |")
        if verdict == "VIOLATE":
            have = sum(1 for r in sub if r["user_obf"]) / len(sub)
            gap = have - G.OBFUSCATION_SHARE
            md.append(f"| {cell} né bộ lọc | CÓ | {100*have:.1f}% | {100*G.OBFUSCATION_SHARE:.1f}% | {100*gap:+.1f}{' ⚠' if abs(gap) > THRESH['dist_gap'] else ''} |")
        have = sum(1 for r in sub if r["user_hard"] == "HARD") / len(sub)
        md.append(f"| {cell} độ khó | HARD | {100*have:.1f}% | {100*G.DEFAULT_HARD_SHARE:.1f}%* | {100*(have-G.DEFAULT_HARD_SHARE):+.1f} |")
    md.append("\n*HARD của user_safe có thể cao hơn do vùng xám; chỉ INFO.")

    # 4. trùng lặp
    md.append("\n## T2.4 Trùng lặp")
    seen = {}
    exact = 0
    for who in ("user_text", "assistant_text"):
        seen = {}
        for r in rows:
            key = " ".join(words(r[who]))
            if key in seen:
                exact += 1
                flags[r["id"]].append(code(f"t2_duplicate_{who.split('_')[0]}", "ERROR"))
                flags[seen[key]].append(code(f"t2_duplicate_{who.split('_')[0]}", "ERROR"))
            else:
                seen[key] = r["id"]
    md.append(f"- Trùng hệt (sau chuẩn hoá): {exact} cặp")
    near = 0
    bypair = collections.defaultdict(list)
    for r in rows:
        bypair[r["pair"]].append(r)
    for rs in bypair.values():
        for who in ("user_text", "assistant_text"):
            sh = [shingles(r[who]) for r in rs]
            for i in range(len(rs)):
                for j in range(i + 1, len(rs)):
                    a, b = sh[i], sh[j]
                    if a and b and len(a & b) / len(a | b) >= THRESH["near_dup"]:
                        if " ".join(words(rs[i][who])) != " ".join(words(rs[j][who])):
                            near += 1
                            c = f"t2_near_duplicate_{who.split('_')[0]}"
                            flags[rs[i]["id"]].append(code(c, "WARN"))
                            flags[rs[j]["id"]].append(code(c, "WARN"))
    md.append(f"- Gần trùng (Jaccard ≥ {THRESH['near_dup']}, cùng pair): {near} cặp")

    # 5. cụm 4 từ lặp nhiều
    md.append("\n## T2.5 Cụm 4 từ lặp nhiều ở câu user")
    c4 = collections.Counter()
    for r in rows:
        w = words(r["user_text"])
        c4.update({" ".join(w[i:i + 4]) for i in range(len(w) - 3)})
    md.append("| cụm | số dòng | tỉ lệ |\n|---|---|---|")
    for g, v in c4.most_common(15):
        md.append(f"| {g} | {v} | {pct(v, n)}{' ⚠' if v / n > THRESH['ngram_share'] else ''} |")
    return md, flags


def side_of(code_name):
    """Mã lỗi thuộc câu nào: mã có tiền tố/hậu tố assistant → câu trợ lý; còn lại (thuộc tính, trùng id...) → câu user."""
    return "assistant" if code_name.startswith("assistant_") or code_name.endswith("_assistant") else "user"


def inspect_rows(rows):
    """Tầng 1 + 2 trên các dòng merged → (cờ theo id: list mã đã sắp, dòng markdown của tầng 2)."""
    channel = rows[0]["channel"]
    flags = collections.defaultdict(list)
    ids = collections.Counter(r["id"] for r in rows)
    uids = collections.Counter(r["user_id"] for r in rows)
    for r in rows:
        flags[r["id"]].extend(row_checks(r, channel))
        if ids[r["id"]] > 1:
            flags[r["id"]].append(code("duplicate_id", "ERROR"))
        if uids[r["user_id"]] > 1:
            flags[r["id"]].append(code("user_id_reused", "WARN"))
    md2, flags2 = stage2(rows, channel)
    for k, v in flags2.items():
        flags[k].extend(v)
    return {r["id"]: sorted(set(flags[r["id"]])) for r in rows}, md2


def errors_by_key(flags):
    """key (id:side) → danh sách mã ERROR của câu đó."""
    out = collections.defaultdict(list)
    for rid, cs in flags.items():
        for c in cs:
            if SEV[c] == "ERROR":
                out[f"{rid}:{side_of(c)}"].append(c)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run")
    ap.add_argument("--xlsx", action="store_true")
    a = ap.parse_args()
    P = C.Paths(C.run_dir(a.run))
    rows, _ = C.load_rows(P)
    channel = rows[0]["channel"]
    flags, md2 = inspect_rows(rows)

    by_code = collections.Counter()
    sev_rows = collections.Counter()
    for r in rows:
        cs = flags[r["id"]]
        by_code.update(cs)
        for s in ("ERROR", "WARN"):
            if any(SEV[c] == s for c in cs):
                sev_rows[s] += 1
    n_err = sev_rows["ERROR"]

    md = [f"# Kiểm tra {P.merged.name}", f"- {len(rows)} dòng, kênh {channel} (đã phủ bản sửa trong decisions)",
          f"- Dòng có ERROR: {sev_rows['ERROR']} · có WARN: {sev_rows['WARN']}", "", "## T1 Số dòng theo mã lỗi",
          "| mức | mã | số dòng |\n|---|---|---|"]
    for c, v in sorted(by_code.items(), key=lambda x: ({"ERROR": 0, "WARN": 1, "INFO": 2}[SEV[x[0]]], -x[1])):
        md.append(f"| {SEV[c]} | {c} | {v} |")
    md.append("")
    md.extend(md2)
    report = P.work / "inspect.md"
    report.write_text("\n".join(md) + "\n", encoding="utf-8")

    flagged = [r for r in rows if any(SEV[c] != "INFO" for c in flags[r["id"]])]
    xlsx = None
    if a.xlsx:
        wb = Workbook()
        ws = wb.active
        ws.title = "flagged"
        head = ["id", "pair", "user_id", "severity", "flags", "user_surface", "user_style", "user_obf", "user_text", "assistant_text"]
        ws.append(head)
        for r in flagged:
            cs = [c for c in flags[r["id"]] if SEV[c] != "INFO"]
            severity = "ERROR" if any(SEV[c] == "ERROR" for c in cs) else "WARN"
            ws.append([r["id"], r["pair"], r["user_id"], severity, "; ".join(cs), r["user_surface"], r["user_style"], r["user_obf"],
                       r["user_text"], r["assistant_text"]])
        for c in ws[1]:
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor="0F766E")
        widths = {"id": 14, "pair": 28, "user_id": 14, "flags": 36, "user_text": 60, "assistant_text": 60}
        for i, h in enumerate(head, 1):
            ws.column_dimensions[get_column_letter(i)].width = widths.get(h, 14)
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical="top")
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        xlsx = P.work / "inspect.xlsx"
        wb.save(xlsx)

    print(f"{len(rows)} dòng · ERROR {n_err} dòng · WARN {sev_rows['WARN']} dòng · bị cờ {len(flagged)}")
    print(f"→ {report}" + (f"\n→ {xlsx}" if xlsx else "  (thêm --xlsx để ghi danh sách dòng bị cờ)"))
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
