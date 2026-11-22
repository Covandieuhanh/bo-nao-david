#!/usr/bin/env python3
# MÁY KIỂM CÂY QUY TRÌNH (quy-trinh.md mục 1) — chạy mỗi lần đẩy GitHub (dong-bo.sh), hoặc tay: python3 -I tu-dong-hoa/kiem-quy-trinh.py
# Chặn khi: (1) lá trỏ tới file không có · (2) lá không ghi "Xong khi" · (3) file quy trình lá (references/, khối) thiếu mục "Xong khi"
# · (4) một SKILL.md dùng chung thiếu mục "Xong khi" · (5) một SKILL.md dùng chung không có lá nào trong cây (việc không có đường vào).
import os, re, sys
R = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CAY = os.path.join(R, 'quy-trinh.md')
loi = []
if not os.path.exists(CAY):
    sys.exit('⛔ thiếu quy-trinh.md (cây quy trình)')
s = open(CAY, encoding='utf-8').read()
co_xong = lambda p: bool(re.search(r'^#+\s*Xong khi|^\*\*Xong khi', open(p, encoding='utf-8').read(), re.M | re.I))

trong_cay = set()
for dong in s.splitlines():
    m = re.match(r'^\|\s*([A-Z]\d+)\s*\|(.*)\|\s*$', dong)
    if not m:
        continue
    la, cot = m.group(1), [c.strip() for c in m.group(2).split('|')]
    if len(cot) < 3 or not cot[-1]:
        loi.append(f'{la}: chưa ghi "Xong khi"')
    for link in re.findall(r'\]\(([^)#\s]+)', dong):
        p = os.path.normpath(os.path.join(R, link))
        if not os.path.exists(p):
            loi.append(f'{la}: trỏ tới file không có — {link}')
            continue
        trong_cay.add(p)
        la_file_quy_trinh = ('/references/' in link or '/mo-dun/' in link) and link.endswith('.md')
        if la_file_quy_trinh and not co_xong(p) and 'theo mục' not in cot[-1]:
            # khối có "Xong khi" ghi ngay trong cây thì đạt; file quy trình lá riêng (references/) bắt buộc có mục
            if '/references/' in link:
                loi.append(f'{la}: file quy trình thiếu mục "Xong khi" — {link}')

# SKILL.md dùng chung (bỏ phần chỉ Mac chính trong phan-rieng-mac.txt)
rieng = set()
pr = os.path.join(R, 'tu-dong-hoa/phan-rieng-mac.txt')
if os.path.exists(pr):
    rieng = {l.strip().rstrip('/') for l in open(pr, encoding='utf-8') if l.strip() and not l.startswith('#')}
for goc, _, files in os.walk(os.path.join(R, 'ky-nang')):
    if 'node_modules' in goc or 'SKILL.md' not in files:
        continue
    p = os.path.join(goc, 'SKILL.md'); rel = os.path.relpath(p, R)
    if any(rel.startswith(x) for x in rieng):
        continue
    if not co_xong(p):
        loi.append(f'{rel}: thiếu mục "Xong khi"')
    if os.path.normpath(p) not in trong_cay:
        loi.append(f'{rel}: chưa có lá nào trong cây quy trình (quy-trinh.md mục 2)')

if loi:
    print('⛔ Cây quy trình chưa đạt (quy-trinh.md):')
    for l in loi:
        print('  -', l)
    sys.exit(1)
print(f'✓ Cây quy trình đạt: {len(trong_cay)} file quy trình, mọi lá có "Xong khi", mọi skill dùng chung có đường vào')
