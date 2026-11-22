"""Xuất file Excel review từ taxonomy/subprompts/*.md.

Dùng:  python3 taxonomy/review/export_review.py [--force]
Nguồn: subprompts/<intent_key>.md, ../intent_taxonomy/taxonomy.json, ../intent_taxonomy/pairs.json và RULES.md (cùng thư mục này).
Mặc định từ chối ghi đè nếu file Excel hiện có đã có cột "Quyết định" hay "Ghi chú" được điền; --force để bỏ qua.
"""
import json,sys
from pathlib import Path
from openpyxl import Workbook,load_workbook
from openpyxl.styles import Font,Alignment,PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

REV=Path(__file__).resolve().parent; TAX=REV.parent; SUB=TAX/'subprompts'
OUT=REV/'v207_subprompts_review.xlsx'
T=json.load(open(TAX/'intent_taxonomy/taxonomy.json',encoding='utf-8'))['intents']
P=json.load(open(TAX/'intent_taxonomy/pairs.json',encoding='utf-8'))
pair_of={}
for p in P:
    for k in (p['input'],p['output']): pair_of[k]=p['pair']
    for k in p.get('extra_output',[]): pair_of[k]=p['pair']
HIGH=("cbrn","csam_bao_ve_tre_em","che_tao_vu_khi_chat_no","cong_cu_gay_hai")
SECS=["Chủ đề","Vi phạm khi","Không vi phạm khi","Ca sát ranh giới","Lưu ý riêng","Lưu ý mẫu vi phạm","Lưu ý mẫu an toàn","Mẫu vi phạm - mức khó","Mẫu an toàn - mức khó","Khía cạnh vi phạm","Khía cạnh an toàn"]

if OUT.exists() and "--force" not in sys.argv:
    ws0=load_workbook(OUT)["SUBPROMPTS"]; h0=[c.value for c in ws0[1]]
    filled=[r[1] for r in ws0.iter_rows(min_row=2,values_only=True) if r[h0.index("Quyết định")] or r[h0.index("Ghi chú của người review")]]
    if filled: sys.exit(f"{OUT.name} đã có quyết định/ghi chú ở {len(filled)} dòng; áp dụng xong rồi chạy lại với --force.")

def parse(t):
    d={};cur=None;st=""
    for l in t.splitlines():
        if l.startswith("Trạng thái:"): st=l[11:].strip()
        elif l.startswith("## "): cur=l[3:].strip(); d[cur]=[]
        elif cur is not None and l.strip(): d[cur].append(l)
    return {k:"\n".join(v) for k,v in d.items()},st

CELLS=["user_violate","user_safe","assistant_violate","assistant_safe"]
for p in P:   # pairs.json chỉ có cấu trúc: metadata lấy từ taxonomy.json, chủ đề từ subprompt input
    i=T[p['input']]; f=SUB/f"{p['input']}.md"
    p['severity_input']=i['severity']; p['muc']=i.get('muc',[]); p['cells']={c:f"{p['pair']}__{c}" for c in CELLS}
    p['topic']=parse(f.read_text(encoding="utf-8"))[0].get('Chủ đề','') if f.exists() else ''

wb=Workbook(); ws=wb.active; ws.title="SUBPROMPTS"
hdr=["#","intent_key","Tên intent","Chiều","Nhóm","Danh mục","Mức","Tầng/Mục 1.02","Cặp (pair)","Rủi ro","Trạng thái","Số ký tự"]+SECS+["Quyết định","Ghi chú của người review"]
ws.append(hdr)
keys=[]
for p in P: keys+=[p['input'],p['output']]
keys=list(dict.fromkeys(keys))
for k in T:
    if k not in keys: keys.append(k)
for i,k in enumerate(keys,1):
    f=SUB/f"{k}.md"; t=f.read_text(encoding="utf-8") if f.exists() else ""; d,st=parse(t); I=T[k]
    if not t: st="chưa có file"
    risk="CAO NHẤT" if any(h in k for h in HIGH) else ""
    ws.append([i,k,I['name'],I['direction'],I['group'],I['category'],I['severity'],", ".join(I.get('muc',[])) or "none",pair_of.get(k,""),risk,st or "đầy đủ",len(t)]+[d.get(s,"") for s in SECS]+["",""])
widths={"A":5,"B":38,"C":38,"D":8,"E":9,"F":12,"G":6,"H":14,"I":30,"J":11,"K":16,"L":9}
for c,w in widths.items(): ws.column_dimensions[c].width=w
for j in range(13,13+len(SECS)): ws.column_dimensions[ws.cell(1,j).column_letter].width=48 if j-13 not in (0,) else 36
ws.column_dimensions[ws.cell(1,13+len(SECS)).column_letter].width=14; ws.column_dimensions[ws.cell(1,14+len(SECS)).column_letter].width=40
for c in ws[1]: c.font=Font(bold=True,color="FFFFFF"); c.fill=PatternFill("solid",fgColor="305496"); c.alignment=Alignment(wrap_text=True,vertical="center")
red=PatternFill("solid",fgColor="FCE4D6")
for r in ws.iter_rows(min_row=2):
    for c in r: c.alignment=Alignment(wrap_text=True,vertical="top")
    if r[9].value:
        for c in r[:12]: c.fill=red
ws.freeze_panes="C2"; ws.auto_filter.ref=ws.dimensions
dv=DataValidation(type="list",formula1='"Duyệt,Sửa,Bỏ,Hỏi policy"',allow_blank=True); ws.add_data_validation(dv)
dv.add(f"{ws.cell(2,13+len(SECS)).column_letter}2:{ws.cell(1+len(keys),13+len(SECS)).column_letter}{1+len(keys)}")

w3=wb.create_sheet("PAIRS"); w3.append(["pair","Chủ đề","input","output","output bổ sung","Mức","Mục 1.02","4 ô sinh dữ liệu"])
for p in P: w3.append([p['pair'],p['topic'],p['input'],p['output'],", ".join(p.get('extra_output',[])),p.get('severity_input',''),", ".join(p.get('muc',[])),", ".join(p['cells'].values())])
for c in w3[1]: c.font=Font(bold=True)
for col,w in zip("ABCDEFGH",(36,60,38,38,30,6,18,60)): w3.column_dimensions[col].width=w
w4=wb.create_sheet("RULES")
for l in (REV/'RULES.md').read_text(encoding="utf-8").splitlines(): w4.append([l])
w4.column_dimensions["A"].width=150
w5=wb.create_sheet("HƯỚNG DẪN")
for l in [f"Mỗi dòng ở sheet SUBPROMPTS là subprompt của một intent ({len(T)} dòng); file gốc nằm ở taxonomy/subprompts/<intent_key>.md.",
 "Cột 'Quyết định': Duyệt / Sửa / Bỏ / Hỏi policy; ghi nhận xét vào cột kế bên. Sửa file .md rồi xuất lại Excel.",
 "Dòng tô cam (Rủi ro = CAO NHẤT): chỉ khái quát từ tên intent, chưa đọc nguồn, chờ team policy bổ sung chi tiết.",
 "Subprompt chèn vào khung generator/prompts/cell.j2; 'Khía cạnh vi phạm/an toàn' thành bảng khóa A1.., S1.."]:
    w5.append([l])
w5.column_dimensions["A"].width=140
wb.save(OUT); print(OUT,len(keys))
