#!/usr/bin/env python3
"""Đo chi phí tra cứu của Claude bằng 10 câu hỏi thử (cau-hoi-thu.json).

Mô phỏng cách Claude tra: tìm từ khoá, mở các file khớp nhiều từ nhất (tối đa 3, file nhỏ trước).
  - cach cu  : tìm trong toàn văn mọi file .md
  - chi muc  : tìm trong co-so-tri-thuc/chi-muc.md (mỗi file một dòng), rồi mở 3 file đầu
Chi phí = số byte phải đọc tới khi mở được file đúng (≈ token × 3–4 với tiếng Việt). Trúng = file đúng nằm trong 3 file mở đầu.
Dùng: python3 tu-dong-hoa/lien-ket/do-truy-xuat.py
"""
import json, os, re, glob
GOC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CH = json.load(open(os.path.join(os.path.dirname(__file__), "cau-hoi-thu.json"), encoding="utf-8"))
# Trang điều hướng (chỉ mục, bản đồ) không tính là nội dung: cách cũ không có chúng, cách mới chỉ dùng để tìm.
DIEU_HUONG = ("co-so-tri-thuc/chi-muc.md", "ban-do/")
files = [os.path.relpath(f, GOC) for f in glob.glob(f"{GOC}/**/*.md", recursive=True)
         if "/.git/" not in f and "/assets/" not in f and not os.path.islink(f)]
files = [f for f in files if not f.startswith(DIEU_HUONG)]
text = {f: open(os.path.join(GOC, f), encoding="utf-8", errors="ignore").read() for f in files}
size = {f: len(text[f].encode()) for f in files}

def mo_toi_khi_trung(cands, dung):
    """Mở lần lượt theo thứ tự (khớp nhiều từ trước, file nhỏ trước) tới khi gặp file đúng.
    Trả về (byte đã đọc, trúng trong 3 file đầu)."""
    thu_tu = [f for f, n in sorted(cands.items(), key=lambda x: (-x[1], size_of(x[0])))]
    doc = 0
    for i, f in enumerate(thu_tu):
        doc += size_of(f)
        if f in dung:
            return doc, i < 3
    return doc, False

def size_of(f):
    return size.get(f, 0)

def cach_cu(q):
    c = {f: sum(t.lower() in text[f].lower() for t in q["tu"]) for f in files}
    c = {f: n for f, n in c.items() if n}
    doc, ok = mo_toi_khi_trung(c, q["dung"])
    return doc + 60 * len(c), ok

def chi_muc(q):
    p = os.path.join(GOC, "co-so-tri-thuc", "chi-muc.md")
    if not os.path.exists(p): return None, None
    dong = {}
    for l in open(p, encoding="utf-8"):
        m = re.search(r"\]\(([^)]+\.md)\)", l)
        if m:
            f = os.path.normpath(os.path.join("co-so-tri-thuc", m.group(1)))
            if not f.startswith(DIEU_HUONG): dong[f] = l
    c = {f: sum(t.lower() in l.lower() for t in q["tu"]) for f, l in dong.items()}
    c = {f: n for f, n in c.items() if n}
    doc, ok = mo_toi_khi_trung(c, q["dung"])
    return sum(len(dong[f].encode()) for f in c) + doc, ok

tc = tm = 0; hc = hm = 0
print(f"{'câu':4} {'cũ byte':>9} {'trúng':>5} | {'chỉ mục':>9} {'trúng':>5}")
for i, q in enumerate(CH, 1):
    bc, okc = cach_cu(q); bm, okm = chi_muc(q)
    tc += bc; hc += okc
    if bm is not None: tm += bm; hm += okm
    print(f"{i:<4} {bc:>9} {'✓' if okc else '✗':>5} | {bm if bm is not None else '-':>9} {('✓' if okm else '✗') if bm is not None else '-':>5}")
print(f"Tổng cũ: {tc} byte, trúng {hc}/10")
if tm: print(f"Tổng chỉ mục: {tm} byte, trúng {hm}/10, giảm {100 - 100 * tm // tc}%")
