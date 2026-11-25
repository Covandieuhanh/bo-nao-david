#!/usr/bin/env python3
"""Máy kiểm ngôn từ (co-so-tri-thuc/bang-thuat-ngu.md mục "Thuật ngữ trong văn bản"): quét file .md tầng 0–2 (theo tang.json),
báo từ cũ không dùng nữa còn sót. Chỉ cảnh báo (mã 0); sửa dần: mỗi lần sửa file nào thì thay hết từ cũ trong file đó."""
import os, re, json, fnmatch, sys
R = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
t = json.load(open(os.path.join(R, 'co-so-tri-thuc/tang.json'), encoding='utf-8'))
def tang(p):
    for mau, tg in t['quy_tac']:
        if fnmatch.fnmatch(p, mau.replace('**', '*')): return tg
    return 2
TU_CU = ['móc vào', 'nhà duy nhất', 'một nhà', 'nhà của', 'đi lên', 'tỉa', 'gác cổng', 'người đọc lạnh', 'đến tận nơi xem']
BO = ('node_modules', 'luu-tru', 'tai-lieu-tham-khao', 'nguon-tham-khao', 'bo-nho', 'nghien-cuu', 'kien-thuc')
ket = {}
for goc, _, fs in os.walk(R):
    rel = os.path.relpath(goc, R)
    if rel.startswith('.git') or any(b in rel.split(os.sep) for b in BO): continue
    for f in fs:
        if not f.endswith('.md'): continue
        p = os.path.join(rel, f).replace(os.sep, '/').lstrip('./')
        if tang(p) == 3 or p.endswith('bang-thuat-ngu.md'): continue
        s = open(os.path.join(goc, f), encoding='utf-8', errors='ignore').read().lower()
        n = {w: s.count(w) for w in TU_CU if w in s}
        if n: ket[p] = n
if not ket: print('✓ Ngôn từ: không còn từ cũ ở tầng 0–2.'); sys.exit(0)
tong = sum(sum(v.values()) for v in ket.values())
print(f'⚠ Ngôn từ: {tong} chỗ còn từ cũ trong {len(ket)} file (bang-thuat-ngu.md mục văn bản); sửa khi chạm file:')
for p, n in sorted(ket.items(), key=lambda x: -sum(x[1].values()))[:15]:
    print('  ', p, ' · '.join(f'{k} ×{v}' for k, v in n.items()))
