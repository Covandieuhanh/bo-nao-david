#!/usr/bin/env python3
"""CÔNG CỤ THĂNG CẤP (trục tri thức mục 4): đếm chủ đề lặp lại trong các sổ tầng 3 rồi đề xuất thăng cấp; chỉ đề xuất, không tự sửa.
Nguồn đọc: mọi nhat-ky-thay-doi.md, loi-thuong-gap.md, du-an/nhat-ky-noi-dung/, co-so-tri-thuc/so-dan-chung-goc.md, ghi nhớ co-so-tri-thuc/bo-nho/,
và sổ tín hiệu ~/.claude/hoc-lien-tuc/tin-hieu.jsonl (lời David sửa, chỉ ở máy này).
Khoá gom nhóm: tham chiếu file trong dấu ` `, liên kết [[ghi-nho]], "khối N", và bốn chữ đầu của lời trích trong ngoặc kép.
Đề xuất: khoá xuất hiện ở ≥ 2 mục khác ngày → nên có cách làm ở tầng 2 (kiểm xem quy trình đã ghi chưa); ≥ 3 mục khác ngày → đủ điều kiện
lên tầng 1 nếu đã có câu kiểm, David chốt. Dùng: python3 -I tu-dong-hoa/hoc-lien-tuc/thang-cap.py [--chi-tiet]"""
import os, re, sys, glob, json, subprocess
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))); os.chdir(R)
CHI_TIET = '--chi-tiet' in sys.argv
NGAY = re.compile(r'(20\d\d-\d\d-\d\d|\d\d/\d\d/20\d\d)')
TRICH = re.compile(r'[“"]([^”"]{12,})[”"]')
THAM = re.compile(r'`([a-z0-9_./-]+\.(?:md|py|sh|mjs|js|json))`|\[\[([a-z0-9-]+)\]\]|(khối [1-4])')
BO = ('luu-tru', 'node_modules', 'tai-lieu-tham-khao', 'nguon-tham-khao', 'chi-muc.md', 'MEMORY.md')

def muc_tu_file(p):
    """Tách một file sổ thành các mục: dòng gạch đầu dòng có ngày, hoặc đoạn dưới tiêu đề ##."""
    s = open(p, encoding='utf-8', errors='ignore').read()
    if os.path.basename(p).startswith(('nhat-ky', 'so-dan-chung')):
        return [(d, p) for d in s.split('\n') if d.startswith(('- ', '| 20')) and NGAY.search(d)]
    if 'loi-thuong-gap' in p:
        return [(x.strip(), p) for x in re.split(r'\n## ', s)[1:]]
    if '/bo-nho/' in p:   # ghi nhớ: cả file là một mục
        return [(s, p)]
    return [(d, p) for d in s.split('\n') if d.startswith('| ') and NGAY.search(d)]

muc = []
for mau in ['**/nhat-ky-thay-doi.md', '**/loi-thuong-gap.md', 'du-an/nhat-ky-noi-dung/*.md', 'co-so-tri-thuc/so-dan-chung-goc.md', 'co-so-tri-thuc/bo-nho/*.md']:
    for p in glob.glob(mau, recursive=True):
        if any(b in p for b in BO): continue
        muc += muc_tu_file(p)
th = os.path.expanduser('~/.claude/hoc-lien-tuc/tin-hieu.jsonl')
if os.path.exists(th):
    for l in open(th, encoding='utf-8', errors='ignore'):
        try: o = json.loads(l)
        except Exception: continue
        for c in o.get('david_sua', []): muc.append((f'"{c}" ({o.get("luc", "")[:10]})', 'tín hiệu phiên'))

def khoa(text, la_ghi_nho=False):
    """Ghi nhớ trỏ chéo nhau ([[...]], tên file, dòng Gốc khối N) là liên kết, không phải lần lặp: với ghi nhớ chỉ lấy lời trích của David."""
    ks = set()
    for a, b, c in ([] if la_ghi_nho else THAM.findall(text)):
        if a: ks.add(os.path.basename(a))
        if b: ks.add('[[' + b + ']]')
        if c: ks.add(c)
    for q in TRICH.findall(text):
        tu = re.findall(r'\w+', q.lower())
        if len(tu) >= 4: ks.add('"' + ' '.join(tu[:4]) + '…"')
    return ks

dem = {}
for text, nguon in muc:
    ng = NGAY.search(text); ng = ng.group(1) if ng else '?'
    for k in khoa(text, '/bo-nho/' in nguon):
        dem.setdefault(k, {'lan': set(), 'nguon': set(), 'vi_du': text[:110]})
        dem[k]['lan'].add((ng, nguon)); dem[k]['nguon'].add(nguon)

# câu kiểm đã có?
cau_kiem = ''
for p in ['co-so-tri-thuc/bai-kiem/dap-an.json', 'ky-nang/san-xuat-video/thiet-ke-bo-cuc/de.json']:
    if os.path.exists(p): cau_kiem += open(p, encoding='utf-8', errors='ignore').read().lower()
luat = ''
for p in glob.glob('ky-nang/**/*.md', recursive=True) + ['quy-trinh.md', 'AGENTS.md']:
    if any(b in p for b in BO) or 'references/' in p: continue
    luat += open(p, encoding='utf-8', errors='ignore').read().lower()

# Lọc báo nhầm (26/11/2026): khoá đã nằm ở tầng 0–1 thì không cần thăng cấp; tên file được nhắc nhiều là do file hay bị sửa, không phải một luật lặp.
import fnmatch
TANG = json.load(open('co-so-tri-thuc/tang.json', encoding='utf-8'))['quy_tac']
def tang(p):
    for m, g in TANG:
        if fnmatch.fnmatch(p, m): return g
    return 2
def duong_dan(ten):
    return [p.replace(os.sep, '/') for p in glob.glob('**/' + ten, recursive=True) if not any(b in p for b in BO)]
def tang_nguon_ghi_nho(ten):
    """Ghi nhớ ghi 'Nguồn của luật: `x`' (hoặc trỏ tới file) → tầng thấp nhất của các file nguồn đó."""
    p = f'co-so-tri-thuc/bo-nho/{ten}.md'
    if not os.path.exists(p): return None
    s = open(p, encoding='utf-8', errors='ignore').read()
    dong = [l for l in s.split('\n') if 'guồn của luật' in l or 'Luật nằm' in l] or [s]
    ts = []
    for l in dong:
        for f in re.findall(r'`([A-Za-z0-9_./-]+\.md)`', l) + re.findall(r'\b(AGENTS\.md|CLAUDE\.md|david\.md)\b', l):
            for q in (duong_dan(os.path.basename(f)) or [f]): ts.append(tang(q))
    return min(ts) if ts else None
bo_qua = {'khối tư duy gốc (tầng 0)': 0, 'file đã ở tầng 0–1': 0, 'file tầng 2–3 hay bị sửa': 0, 'ghi nhớ đã có nguồn luật ở tầng 0–1': 0}

de_xuat = []
for k, v in dem.items():
    ngay_khac = len({n for n, _ in v['lan']})
    if ngay_khac < 2: continue
    if k.startswith('khối '): bo_qua['khối tư duy gốc (tầng 0)'] += 1; continue
    if not k.startswith(('[[', '"')):
        ps = duong_dan(k)
        if ps and min(tang(p) for p in ps) <= 1: bo_qua['file đã ở tầng 0–1'] += 1
        else: bo_qua['file tầng 2–3 hay bị sửa'] += 1
        continue
    if k.startswith('[['):
        t = tang_nguon_ghi_nho(k.strip('[]'))
        if t is not None and t <= 1: bo_qua['ghi nhớ đã có nguồn luật ở tầng 0–1'] += 1; continue
    goc = k.strip('`"[]…').lower()
    co_cau_kiem = goc[:25] in cau_kiem
    co_trong_luat = goc[:25] in luat
    if ngay_khac >= 3: muc_tieu = 'tầng 1 (đủ 3 lần)' + ('' if co_cau_kiem else ', thiếu câu kiểm') + ' — David chốt'
    else: muc_tieu = 'tầng 2 (cách làm)' + (' — đã có trong quy trình' if co_trong_luat else ' — chưa thấy trong quy trình')
    de_xuat.append((ngay_khac, k, muc_tieu, sorted(v['nguon'])[:3], v['vi_du']))
de_xuat.sort(key=lambda x: -x[0])
print(f'Đọc {len(muc)} mục sổ · {len(dem)} khoá · {len(de_xuat)} khoá lặp ≥ 2 lần khác ngày cần xem')
print('Bỏ qua (đã ở đúng tầng): ' + ' · '.join(f'{k} {n}' for k, n in bo_qua.items() if n))
if not de_xuat: print('Chưa có chủ đề nào lặp đủ để đề xuất thăng cấp.'); sys.exit(0)
print('Đề xuất (chỉ báo, David chốt mới sửa tầng 1):')
for n, k, mt, ng, vd in de_xuat[:15 if not CHI_TIET else 60]:
    print(f'  {n}× {k} → {mt}')
    if CHI_TIET: print('     nguồn:', ', '.join(os.path.basename(x) for x in ng), '· ví dụ:', vd)
