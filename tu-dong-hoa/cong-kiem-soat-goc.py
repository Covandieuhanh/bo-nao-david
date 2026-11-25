#!/usr/bin/env python3
"""Cổng kiểm soát gốc (co-so-tri-thuc/truc-tri-thuc.md mục 7). Chạy trong dong-bo.sh --push; tay: python3 -I tu-dong-hoa/cong-kiem-soat-goc.py
File tầng 0 (co-so-tri-thuc/tang.json) có thay đổi chưa đẩy mà co-so-tri-thuc/so-dan-chung-goc.md không có dòng ghi (trong 7 ngày,
đúng tên file, loại "nâng cấp" hoặc "đổi gốc"; đổi gốc phải có trạng thái "chốt") → trả mã 1, không đẩy."""
import os, re, json, subprocess, sys, datetime, fnmatch
R = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
t = json.load(open(os.path.join(R, 'co-so-tri-thuc/tang.json'), encoding='utf-8'))
def tang(p):
    for mau, tg in t['quy_tac']:
        if fnmatch.fnmatch(p, mau.replace('**', '*')): return tg
    return 2
def git(*a):
    return subprocess.run(['git', '-C', R, *a], capture_output=True, text=True).stdout.split()
doi = set(git('diff', '--name-only', 'HEAD')) | set(git('diff', '--name-only', '--cached')) | set(git('log', '--name-only', '--format=', 'origin/main..HEAD'))
goc = sorted(p for p in doi if tang(p) == 0)
if not goc: sys.exit(0)
so = open(os.path.join(R, 'co-so-tri-thuc/so-dan-chung-goc.md'), encoding='utf-8').read()
hom_nay = datetime.date.today(); loi = []
for p in goc:
    dong_ok = False
    for d in so.splitlines():
        if not d.startswith('| 20') or p not in d: continue
        try: ngay = datetime.date.fromisoformat(d.split('|')[1].strip())
        except ValueError: continue
        if (hom_nay - ngay).days > 7: continue
        if 'đổi gốc' in d and 'chốt' not in d: continue
        if 'nâng cấp' in d or 'đổi gốc' in d: dong_ok = True; break
    if not dong_ok: loi.append(p)
if loi:
    print('⛔ File gốc (tầng 0) thay đổi mà sổ dẫn chứng chưa ghi:', *loi, sep='\n  - ')
    print('Ghi một dòng vào co-so-tri-thuc/so-dan-chung-goc.md (ngày hôm nay, tên file, "nâng cấp" hoặc "đổi gốc" đã chốt, lời David) rồi đẩy lại.')
    sys.exit(1)
print('✓ Cổng kiểm soát gốc: ' + ', '.join(goc) + ' có dòng sổ dẫn chứng.')
