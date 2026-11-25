#!/usr/bin/env python3
"""Công cụ kiểm tra ngôn từ (co-so-tri-thuc/bang-thuat-ngu.md mục "Thuật ngữ trong văn bản"), bảng thay ở tu-dong-hoa/ngon-tu.py.
  python3 -I tu-dong-hoa/kiem-ngon-tu.py          quét cả bộ não, báo từ khẩu ngữ còn sót (cảnh báo, mã 0)
  python3 -I tu-dong-hoa/kiem-ngon-tu.py --sua    thay từ cũ bằng thuật ngữ chuẩn trong mọi file (trừ lời trích, dòng trích dẫn, tài liệu nguồn)
Quét: .md .txt .json (mọi chuỗi) · .py .sh .mjs .js (chỉ chú thích và thông báo). Bỏ: .git, node_modules, tai-lieu-tham-khao, nguon-tham-khao, bảng thuật ngữ, file này."""
import os, sys, unicodedata
R = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(R, 'tu-dong-hoa')); import ngon_tu as NT
BO_DIR = ('.git', 'node_modules', 'tai-lieu-tham-khao', 'nguon-tham-khao', 'out', 'dist')
BO_FILE = ('bang-thuat-ngu.md', 'kiem-ngon-tu.py', 'ngon_tu.py')
LOAI = {'.md': 'md', '.txt': 'md', '.json': 'json', '.py': 'code', '.sh': 'code', '.mjs': 'code', '.js': 'code'}
sua = '--sua' in sys.argv
ket, da_sua = {}, 0
for goc, ds, fs in os.walk(R):
    ds[:] = [d for d in ds if d not in BO_DIR]
    for f in fs:
        duoi = os.path.splitext(f)[1]
        if duoi not in LOAI or f in BO_FILE: continue
        p = os.path.join(goc, f); rel = os.path.relpath(p, R).replace(os.sep, '/')
        try: s = unicodedata.normalize('NFC', open(p, encoding='utf-8').read())
        except (UnicodeDecodeError, OSError): continue
        if sua:
            s2 = NT.thay_van_ban(s, LOAI[duoi])
            if s2 != s: open(p, 'w', encoding='utf-8').write(s2); da_sua += 1; s = s2
        # quét phần ngoài lời trích
        ngoai = '\n'.join(('' if d.lstrip().startswith('>') else ''.join(x for i, x in enumerate(NT._Q.split(d)) if i % 2 == 0)) for d in s.split('\n')).lower()
        n = {w: ngoai.count(w) for w in NT.TU_CU if w in ngoai}
        if n: ket[rel] = n
if sua: print(f'Đã thay trong {da_sua} file.')
if not ket: print('✓ Ngôn từ: không còn từ khẩu ngữ ngoài lời trích.'); sys.exit(0)
tong = sum(sum(v.values()) for v in ket.values())
print(f'⚠ Ngôn từ: {tong} chỗ còn từ cũ trong {len(ket)} file (bang-thuat-ngu.md mục văn bản; thay bằng --sua hoặc sửa tay nếu nghĩa khác):')
for p, n in sorted(ket.items(), key=lambda x: -sum(x[1].values()))[:25]:
    print('  ', p, ' · '.join(f'{k} ×{v}' for k, v in n.items()))
