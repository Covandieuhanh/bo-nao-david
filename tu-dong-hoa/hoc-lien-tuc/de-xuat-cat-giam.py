#!/usr/bin/env python3
"""ĐỀ XUẤT CẮT GIẢM (trục tri thức mục 4 "đi xuống cũng có luật"; hoc-lien-tuc Việc 4): liệt kê thứ lâu không dùng để David quyết cất vào lưu trữ.
(1) ghi nhớ không file nào trỏ tới (ngoài MEMORY.md, chi-muc.md) và không sửa quá 30 ngày; (2) skill không có tín hiệu dùng 30 ngày (máy này);
(3) ý tưởng chờ quá 30 ngày chưa chốt. Chỉ đề xuất, không xoá. Dùng: python3 -I tu-dong-hoa/hoc-lien-tuc/de-xuat-cat-giam.py [số ngày]"""
import os, re, sys, glob, json, subprocess, datetime as dt
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))); os.chdir(R)
NGAY = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 30
hom_nay = dt.date.today()
def ngay_sua(p):
    o = subprocess.run(['git', 'log', '-1', '--format=%ad', '--date=short', '--', p], capture_output=True, text=True).stdout.strip()
    return dt.date.fromisoformat(o) if o else hom_nay
van_ban = ''
for p in glob.glob('**/*.md', recursive=True):
    if 'node_modules' in p or p.endswith(('MEMORY.md', 'chi-muc.md')): continue
    van_ban += open(p, encoding='utf-8', errors='ignore').read()
print(f'== Ghi nhớ không ai trỏ tới và không sửa quá {NGAY} ngày')
n = 0
for p in sorted(glob.glob('co-so-tri-thuc/bo-nho/*.md')):
    ten = os.path.basename(p)[:-3]
    if ten == 'MEMORY': continue
    if ten in van_ban: continue
    tuoi = (hom_nay - ngay_sua(p)).days
    if tuoi > NGAY: print(f'  - {ten} ({tuoi} ngày)'); n += 1
print('  (không có)' if n == 0 else f'  → {n} ghi nhớ: đề xuất cất co-so-tri-thuc/bo-nho/luu-tru/, David duyệt')
print(f'== Skill không có tín hiệu dùng trong {NGAY} ngày (máy này)')
th = os.path.expanduser('~/.claude/hoc-lien-tuc/tin-hieu.jsonl'); dung = set()
if os.path.exists(th):
    for l in open(th, encoding='utf-8', errors='ignore'):
        try: o = json.loads(l)
        except Exception: continue
        try: luc = dt.datetime.strptime(o.get('luc', '')[:10], '%Y-%m-%d').date()
        except ValueError: continue
        if (hom_nay - luc).days <= NGAY: dung |= set(o.get('skill', {}).keys())
    skills = [os.path.basename(os.path.dirname(p)) for p in glob.glob('ky-nang/*/SKILL.md') + glob.glob('ky-nang/san-xuat-video/*/SKILL.md')]
    for s in sorted(set(skills) - dung): print(f'  - {s}')
else: print('  (chưa có sổ tín hiệu ở máy này)')
print(f'== Ý tưởng chờ quá {NGAY} ngày chưa chốt (du-an/danh-sach-y-tuong.md)')
n = 0
for d in open('du-an/danh-sach-y-tuong.md', encoding='utf-8').read().split('\n'):
    if not d.startswith('| ') or d.startswith('| #'): continue
    m = re.search(r'(\d\d)/(\d\d)/(20\d\d)', d)
    if not m or '✅' in d: continue
    tuoi = (hom_nay - dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))).days
    if tuoi > NGAY: print('  -', d.split('|')[2].strip()[:70], f'({tuoi} ngày)'); n += 1
print('  (không có)' if n == 0 else f'  → hỏi David giữ hay bỏ')
