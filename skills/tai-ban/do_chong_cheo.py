#!/usr/bin/env python3
"""MÁY ĐO CHỒNG CHÉO — skill tai-ban (David chốt 10/11/2026).
  python3 -I skills/tai-ban/do_chong_cheo.py [bộ …] [--chi-tiet]      (không ghi bộ = đo mọi bộ trong bo.json)
Đo các "bản luật" (file AI đọc khi làm việc) của từng bộ, xem luật đã chồng nhiều lớp tới đâu:
  dau_ngay  dấu ngày / "chốt 08/11" nằm trong bản luật (ngày thuộc về sổ quyết định, không thuộc luật)
  ghi_de    câu kiểu "thay luật cũ", "ngoại lệ", "nới", "bổ sung 09/11", "chuyển nguyên văn từ SKILL.md cũ" — dấu luật vá lên luật
  trung     câu dài giống hệt nhau ở hai file (một luật hai nhà)
  sua       số lần bản luật bị sửa kể từ lần tái bản gần nhất (git, mốc ở lich-su.md)
  dong      tổng số dòng bản luật
Một bộ bất kỳ vượt một ngưỡng (bo.json "nguong") → in một dòng "NÊN TÁI BẢN TOÀN BỘ" kèm lý do, mã thoát 1 (tái bản là cả đợt, mọi bộ). Không sửa file nào.
Phần "## Nhật ký" cuối file là sổ, không tính.
"""
import fnmatch, glob, json, os, re, subprocess, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
CFG = json.load(open(os.path.join(HERE, 'bo.json'), encoding='utf-8'))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
CHI_TIET = '--chi-tiet' in sys.argv

NGAY = re.compile(r"20\d\d-\d\d-\d\d|\b\d{1,2}/\d{1,2}/20\d\d\b|"
                  r"\b(?:chốt|sửa|duyệt|thêm|bổ sung|nới|đổi|cập nhật|học)\s+(?:ngày\s+)?\d{1,2}/\d{1,2}\b", re.I)
GHI_DE = re.compile(r"thay luật|thay các|thay thế luật|thắng mọi|không còn áp|nới luật|nới\)|luật cũ|"
                    r"bổ sung 20\d\d|bổ sung \d{1,2}/\d{1,2}|chuyển nguyên văn từ SKILL\.md cũ|\(cũ[,)]|đã bỏ|bỏ từ \d|thay cho luật", re.I)   # "ngoại lệ" không tính: luật viết sạch vẫn có ngoại lệ thật

THAY_HOA = re.compile(r"\bTHAY\b")   # chỉ chữ in hoa kiểu "THAY các ngoại lệ"; chữ "thay" thường không phải dấu ghi đè

def khop(path, mau):
    return any(fnmatch.fnmatch(path, m) for m in mau)

def ban_luat(bo):
    c = CFG[bo]; out = set()
    for m in c['ban_luat']:
        for f in glob.glob(os.path.join(REPO, m), recursive=True):
            r = os.path.relpath(f, REPO)
            if os.path.isfile(f) and not khop(r, c.get('bo_qua', [])): out.add(r)
    return sorted(out)

def doc(r):
    s = open(os.path.join(REPO, r), encoding='utf-8', errors='replace').read()
    m = re.search(r"^##\s+Nhật ký\b", s, re.M)
    return s[:m.start()] if m else s

def cau(s):
    for d in re.split(r"(?<=[.!?:])\s+|\n", s):
        t = re.sub(r"[`*_>#|\-\[\]()]", " ", d.lower()); t = re.sub(r"\s+", " ", t).strip()
        if len(t) >= 70: yield t

def moc(bo):
    """Mốc gần nhất của bộ: tag chung tai-ban-<n> (tái bản toàn bộ) hoặc tag riêng cũ tai-ban-<bộ>-<n>, lấy tag mới nhất có thật trong git."""
    p = os.path.join(HERE, 'lich-su.md')
    if not os.path.exists(p): return None
    tags = set(re.findall(rf"`(tai-ban-(?:{bo}-)?\d+)`", open(p, encoding='utf-8').read()))
    try:
        out = subprocess.run(['git', '-C', REPO, 'for-each-ref', '--sort=creatordate', '--format=%(refname:short)', 'refs/tags/tai-ban-*'],
                             capture_output=True, text=True, check=True).stdout.split()
    except Exception:
        out = []
    co = [t for t in out if t in tags]
    return co[-1] if co else None

def so_lan_sua(bo, files):
    m = moc(bo)
    rng = [f'{m}..HEAD'] if m else []
    try:
        out = subprocess.run(['git', '-C', REPO, 'rev-list', '--count', *rng, 'HEAD', '--', *files] if not m else
                             ['git', '-C', REPO, 'rev-list', '--count', *rng, '--', *files], capture_output=True, text=True, check=True).stdout
        return int(out.strip()), m
    except Exception:
        return 0, m

ket = 0; vuot_bo = []
for bo in (args or [k for k in CFG if not k.startswith('_')]):
    if bo not in CFG: print(f'không có bộ "{bo}" trong bo.json'); continue
    files = ban_luat(bo)
    per = {}; noi = defaultdict(set); tong = defaultdict(int)
    for r in files:
        s = doc(r)
        d = {'dau_ngay': len(NGAY.findall(s)), 'ghi_de': len(GHI_DE.findall(s)) + len(THAY_HOA.findall(s)), 'dong': s.count('\n') + 1}
        per[r] = d
        for k, v in d.items(): tong[k] += v
        for c in set(cau(s)): noi[c].add(r)
    trung = {c: fs for c, fs in noi.items() if len(fs) > 1}
    tong['trung'] = len(trung)
    tong['sua'], m = so_lan_sua(bo, files)
    ng = CFG[bo]['nguong']
    vuot = [f"{k} {tong[k]} > {ng[k]}" for k in ng if tong[k] > ng[k]]
    print(f"\n## Bộ {bo} — {len(files)} file bản luật · mốc tái bản gần nhất: {m or 'chưa có'}")
    print('  ' + ' · '.join(f"{k} {tong[k]}/{ng[k]}" for k in ng))
    top = sorted(per.items(), key=lambda kv: -(kv[1]['dau_ngay'] + 3 * kv[1]['ghi_de']))[: (len(per) if CHI_TIET else 6)]
    print('  File chồng nhiều nhất:')
    for r, d in top:
        if d['dau_ngay'] + d['ghi_de']: print(f"   - {r}: {d['dau_ngay']} dấu ngày · {d['ghi_de']} câu ghi đè · {d['dong']} dòng")
    if trung:
        print(f'  Câu trùng ở nhiều file ({len(trung)}):' + ('' if CHI_TIET else ' (3 câu đầu, --chi-tiet để xem hết)'))
        for c, fs in list(trung.items())[: (len(trung) if CHI_TIET else 3)]:
            print(f"   - \"{c[:90]}…\" ở {', '.join(sorted(fs))}")
    if vuot:
        ket = 1; vuot_bo.append(f"{bo} ({'; '.join(vuot)})"); print(f"  ⇒ bộ {bo} vượt ngưỡng: " + '; '.join(vuot))
    else:
        print(f"  ⇒ bộ {bo} dưới ngưỡng.")
print('\n' + (f"⇒ NÊN TÁI BẢN TOÀN BỘ (skill tai-ban): vượt ngưỡng ở {', '.join(vuot_bo)}" if vuot_bo else "⇒ Chưa cần tái bản."))
sys.exit(ket)
