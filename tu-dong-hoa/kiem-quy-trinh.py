#!/usr/bin/env python3
# CÔNG CỤ KIỂM TRA CÂY QUY TRÌNH (quy-trinh.md mục 2, khung lá) — chạy mỗi lần đẩy GitHub (dong-bo.sh), hoặc tay: python3 -I tu-dong-hoa/kiem-quy-trinh.py
# Chặn khi: (1) lá trỏ tới file không có · (2) lá không ghi "Điểm duyệt" hoặc "Xong khi" · (3) file quy trình lá riêng (references/) thiếu
# mục "Điểm duyệt" hoặc "Xong khi" · (4) một SKILL.md dùng chung thiếu mục "Xong khi" · (5) một SKILL.md dùng chung không có lá nào trong cây.
import os, re, sys
R = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CAY = os.path.join(R, 'quy-trinh.md')
loi = []
if not os.path.exists(CAY):
    sys.exit('⛔ thiếu quy-trinh.md (cây quy trình)')
s = open(CAY, encoding='utf-8').read()
co_muc = lambda p, ten: bool(re.search(rf'^#+\s*{ten}|^\*\*{ten}', open(p, encoding='utf-8').read(), re.M | re.I))

trong_cay, so_la = set(), 0
for dong in s.splitlines():
    m = re.match(r'^\|\s*([A-Z]\d+)\s*\|(.*)\|\s*$', dong)
    if not m:
        continue
    so_la += 1
    la, cot = m.group(1), [c.strip() for c in m.group(2).split('|')]
    if len(cot) < 4:
        loi.append(f'{la}: thiếu cột (Việc · Quy trình · Điểm duyệt · Xong khi)')
        continue
    if not cot[-2]:
        loi.append(f'{la}: chưa ghi "Điểm duyệt" (Đ1 / Đ2 / Đ3 ở bước nào, hoặc "không có")')
    if not cot[-1]:
        loi.append(f'{la}: chưa ghi "Xong khi"')
    for link in re.findall(r'\]\(([^)#\s]+)', dong):
        p = os.path.normpath(os.path.join(R, link))
        if not os.path.exists(p):
            loi.append(f'{la}: trỏ tới file không có — {link}')
            continue
        trong_cay.add(p)
        if '/references/' in link and link.endswith('.md'):
            for ten in ('Điểm duyệt', 'Xong khi'):
                if not co_muc(p, ten):
                    loi.append(f'{la}: file quy trình thiếu mục "{ten}" — {link}')

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
    if not co_muc(p, 'Xong khi'):
        loi.append(f'{rel}: thiếu mục "Xong khi"')
    if os.path.normpath(p) not in trong_cay:
        loi.append(f'{rel}: chưa có lá nào trong cây quy trình (quy-trinh.md mục 3)')

if loi:
    print('⛔ Cây quy trình chưa đạt (quy-trinh.md):')
    for l in loi:
        print('  -', l)
    sys.exit(1)
print(f'✓ Cây quy trình đạt: {so_la} lá, {len(trong_cay)} file quy trình; mọi lá có điểm duyệt và "Xong khi", mọi skill dùng chung có đường vào')
