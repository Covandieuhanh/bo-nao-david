#!/usr/bin/env python3
"""BỘ KIỂM PHỦ LUẬT (trục tri thức mục 4: lỗi nào cũng thành câu kiểm; mục tiêu mọi luật tầng 1 có câu kiểm).
Đọc các file tầng 0–1 (co-so-tri-thuc/tang.json), tách "luật" = dòng có cụm in đậm **…** ở đầu, gom theo mục ##; so với hai bộ đáp án
(co-so-tri-thuc/bai-kiem/dap-an.json, ky-nang/san-xuat-video/thiet-ke-bo-cuc/de.json): một luật được coi là có câu kiểm khi một đáp án nhắc
tên file đó và (số mục hoặc ba chữ đầu của luật). In tỉ lệ phủ và luật chưa có câu kiểm. Dùng: python3 -I tu-dong-hoa/hoc-lien-tuc/phu-cau-kiem.py [--het]"""
import os, re, sys, json, fnmatch
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))); os.chdir(R)
HET = '--het' in sys.argv
t = json.load(open('co-so-tri-thuc/tang.json', encoding='utf-8'))
files = [m for m, g in t['quy_tac'] if g in (0, 1) and '*' not in m and m.endswith('.md') and os.path.exists(m)]
dap = ''
for p in ['co-so-tri-thuc/bai-kiem/dap-an.json', 'ky-nang/san-xuat-video/thiet-ke-bo-cuc/de.json']:
    if os.path.exists(p): dap += open(p, encoding='utf-8').read().lower()
LUAT = re.compile(r'^\s*(?:[-*]|\d+\.)?\s*\*\*([^*\n]{6,}?)\*\*', re.M)
tong = phu = 0; thieu = {}
for f in files:
    s = open(f, encoding='utf-8').read(); ten = os.path.basename(f).lower(); co_file = ten in dap
    muc = '0'
    for d in s.split('\n'):
        h = re.match(r'^##\s*(\d+)', d)
        if h: muc = h.group(1); continue
        m = LUAT.match(d)
        if not m: continue
        luat = m.group(1).strip(' :')
        tu = re.findall(r'\w+', luat.lower())[:3]
        co = co_file and (f'mục {muc}' in dap and f'{ten} mục {muc}' in dap or (len(tu) >= 2 and ' '.join(tu) in dap))
        tong += 1; phu += bool(co)
        if not co: thieu.setdefault(f, []).append(f'mục {muc}: {luat[:70]}')
print(f'Bộ kiểm phủ luật tầng 0–1: {phu}/{tong} luật có câu kiểm ({100 * phu // max(tong, 1)} %)')
for f, ds in thieu.items():
    print(f'  {f}: thiếu {len(ds)}')
    for d in ds[: (len(ds) if HET else 4)]: print('    -', d)
