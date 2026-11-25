#!/usr/bin/env python3
"""CÔNG CỤ ĐO CHỒNG CHÉO — skill tai-cau-truc.
  python3 -I ky-nang/tai-cau-truc/do-chong-cheo.py [bộ …] [--chi-tiet]      (không ghi bộ = đo mọi bộ trong bo.json)
Đo các "bản luật" (file AI đọc khi làm việc) của từng bộ, xem luật đã chồng nhiều lớp tới đâu:
  dau_ngay  dấu ngày / "chốt 08/11" nằm trong bản luật (ngày thuộc về sổ quyết định, không thuộc luật)
  ghi_de    câu kiểu "thay luật cũ", "ngoại lệ", "nới", "bổ sung 09/11", "chuyển nguyên văn từ SKILL.md cũ" — dấu luật vá lên luật
  trung     câu dài giống hệt nhau ở hai file (một luật hai nhà)
  viet_tat  chữ viết tắt thường ngày ngoài phần code ("vd.", "ko", "TB", "đc", "sl", "tg", "cty") — file phải viết đủ từ (AGENTS.md luật 1)
  mui_ten   mũi tên "→" trong câu văn (ngoài bảng, ngoài chuỗi bước nối lệnh / file) — câu văn viết "thì" / "thành" (AGENTS.md luật 1)
  gan_trung cặp dòng ở hai file khác nhau giống nhau quá nửa số chữ (một ý viết lại theo cách khác ở nhà thứ hai)
  sua       số lần bản luật bị sửa kể từ lần tái bản gần nhất (git, mốc ở lich-su.md) — chỉ nhắc nhẹ
  dong      tổng số dòng bản luật — chỉ để biết độ lớn; bộ não lớn lên vì học thêm, dài không phải là rối
Chuông chỉ kêu vì trùng / rối: một bộ bất kỳ vượt một ngưỡng ở bo.json "nguong" (dau_ngay, ghi_de, trung, gan_trung, viet_tat, mui_ten) → in một dòng
"NÊN NÂNG CẤP" kèm lý do, mã thoát 1 (nâng cấp là cả bộ não một đợt: hoc-lien-tuc Việc 4, dọn bằng tai-cau-truc). "nhac" (sua) vượt chỉ in một dòng nhắc, không kêu. Không sửa file nào.
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

VIET_TAT = re.compile(r"(?<!\w)(?:[Vv][Dd]\.|ko|TB|đc|sl|tg|cty)(?!\w)")
CODE = re.compile(r"```.*?```|`[^`\n]*`|\"[^\"\n]*\"|“[^”\n]*”", re.S)   # bỏ code và chữ trong ngoặc kép (ví dụ được trích, không phải viết tắt)
FILE_GAN = re.compile(r"(\.(md|js|jsx|mjs|py|sh|json|mp4|mov|wav|m4a|srt|jpg|png|txt)\b|`|\]\(|localhost)")

def mui_ten_cau(s):
    """Số dòng văn có đúng một "→" mà hai bên không phải lệnh / file (dòng bảng, khối code, chuỗi từ hai mũi tên trở lên, mũi tên cuối dòng nối sang dòng sau là đúng luật)."""
    n = 0; code = False
    for l in s.split('\n'):
        if l.lstrip().startswith('```'): code = not code; continue
        if code or l.lstrip().startswith('|'): continue
        bare = re.sub(r"`[^`]*`", "`C`", l); bare = re.sub(r'"[^"\n]*"|“[^”\n]*”', '""', bare)
        if bare.count('→') != 1: continue
        i = bare.index('→'); left, right = bare[:i].rstrip(), bare[i + 1:].lstrip()
        if not left.strip(' -*>#(') or not right.strip() or FILE_GAN.search(left[-25:]) or FILE_GAN.search(right[:25]) or re.match(r"[\w./-]+\.\w+", right): continue
        n += 1
    return n

THAY_HOA = re.compile(r"\bTHAY\b")   # chỉ chữ in hoa kiểu "THAY các ngoại lệ"; chữ "thay" thường không phải dấu ghi đè

def khop(path, mau):
    return any(fnmatch.fnmatch(path, m) for m in mau)

def tang_cua(goc, f, _c={}):
    """Tầng của file theo co-so-tri-thuc/tang.json (trục tri thức mục 2); không có bảng thì None."""
    import fnmatch, json
    if 'q' not in _c:
        p = os.path.join(goc, "co-so-tri-thuc", "tang.json")
        _c['q'] = json.load(open(p, encoding="utf-8"))["quy_tac"] if os.path.exists(p) else []
    for mau, t in _c['q']:
        if fnmatch.fnmatch(f, mau) or (mau.endswith("/**") and f.startswith(mau[:-2])) or (mau.startswith("**/") and fnmatch.fnmatch(os.path.basename(f), mau[3:])):
            return t
    return None

def ban_luat(bo):
    c = CFG[bo]; out = set()
    for m in c['ban_luat']:
        for f in glob.glob(os.path.join(REPO, m), recursive=True):
            r = os.path.relpath(f, REPO)
            if os.path.isfile(f) and not khop(r, c.get('bo_qua', [])) and tang_cua(REPO, r) != 3: out.add(r)   # tầng 3 là dữ liệu, không đo
    return sorted(out)

def doc(r):
    s = open(os.path.join(REPO, r), encoding='utf-8', errors='replace').read()
    m = re.search(r"^##\s+Nhật ký\b", s, re.M)
    return s[:m.start()] if m else s

def cau(s):
    for d in re.split(r"(?<=[.!?:])\s+|\n", s):
        t = re.sub(r"[`*_>#|\-\[\]()]", " ", d.lower()); t = re.sub(r"\s+", " ", t).strip()
        if len(t) >= 70: yield t

GT_CHU, GT_NGUONG = 12, 0.5   # dòng có ≥ 12 chữ; hai dòng chung > 50 % số chữ (Jaccard) là gần trùng

def chu(dong):
    """Chỉ phần chữ của dòng: bỏ tiêu đề (mục lục lặp tên khối là đúng thiết kế), bỏ `code`/đường dẫn và địa chỉ link."""
    if dong.lstrip().startswith('#'): return set()
    dong = re.sub(r"`[^`]*`", " ", dong); dong = re.sub(r"\]\([^)]*\)", "] ", dong)
    return set(re.findall(r"\w+", dong.lower()))

def dong_chu(s):
    """Các dòng văn của file: bỏ phần mô tả đầu file (--- … ---, chỉ mục lặp lại là đúng thiết kế) và khối ``` lệnh / cây thư mục."""
    ls = s.splitlines(); i = 0; code = False
    if ls and ls[0].strip() == '---':
        i = next((k for k in range(1, len(ls)) if ls[k].strip() == '---'), 0) + 1
    for k in range(i, len(ls)):
        if ls[k].lstrip().startswith('```'): code = not code; continue
        if not code: yield k + 1, ls[k]

def gan_trung(texts):
    """texts: {file: nội dung}. Trả về {(file a, file b): [(dòng a, dòng b), …]} các cặp dòng gần trùng ở hai file khác nhau."""
    dong = [(r, i, w) for r, s in texts.items() for i, l in dong_chu(s) if len(w := chu(l)) >= GT_CHU]
    chi_muc = defaultdict(list)
    for k, (r, i, w) in enumerate(dong):
        for t in w: chi_muc[t].append(k)
    df = {t: len(v) for t, v in chi_muc.items()}
    out = defaultdict(list)
    for k, (r, i, w) in enumerate(dong):
        hiem = sorted(w, key=lambda t: df[t])[:4]          # ứng viên: dòng chung ít nhất một chữ hiếm
        ung = {j for t in hiem for j in chi_muc[t] if j > k}
        for j in ung:
            r2, i2, w2 = dong[j]
            if r2 != r and len(w & w2) / len(w | w2) > GT_NGUONG:
                out[tuple(sorted([(r, i), (r2, i2)]))[0][0], tuple(sorted([(r, i), (r2, i2)]))[1][0]].append((i, i2))
    return out

def moc(bo):
    """Mốc gần nhất của bộ: tag chung nang-cap-<n> (hoặc tai-ban-<n> / tai-ban-<bộ>-<n> của các đợt cũ), lấy tag mới nhất có thật trong git."""
    p = os.path.join(HERE, 'lich-su.md')
    if not os.path.exists(p): return None
    tags = set(re.findall(rf"`((?:tai-ban|nang-cap)-(?:{bo}-)?\d+)`", open(p, encoding='utf-8').read()))
    try:
        out = subprocess.run(['git', '-C', REPO, 'for-each-ref', '--sort=creatordate', '--format=%(refname:short)', 'refs/tags/tai-ban-*', 'refs/tags/nang-cap-*'],
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
    per = {}; noi = defaultdict(set); tong = defaultdict(int); texts = {}
    for r in files:
        s = doc(r); texts[r] = s
        d = {'dau_ngay': len(NGAY.findall(s)), 'ghi_de': len(GHI_DE.findall(s)) + len(THAY_HOA.findall(s)), 'dong': s.count('\n') + 1,
             'viet_tat': len(VIET_TAT.findall(CODE.sub(' ', s))), 'mui_ten': mui_ten_cau(s)}
        per[r] = d
        for k, v in d.items(): tong[k] += v
        for c in set(cau(s)): noi[c].add(r)
    trung = {c: fs for c, fs in noi.items() if len(fs) > 1}
    tong['trung'] = len(trung)
    gt = gan_trung(texts); tong['gan_trung'] = sum(len(v) for v in gt.values())
    tong['sua'], m = so_lan_sua(bo, files)
    ng = CFG[bo]['nguong']; nh = CFG[bo].get('nhac', {})
    vuot = [f"{k} {tong[k]} > {ng[k]}" for k in ng if tong[k] > ng[k]]
    print(f"\n## Bộ {bo} — {len(files)} file bản luật · mốc nâng cấp gần nhất: {m or 'chưa có'}")
    print('  ' + ' · '.join(f"{k} {tong[k]}/{ng[k]}" for k in ng) + f"  (độ lớn: {tong['dong']} dòng · sửa {tong['sua']} lần)")
    for k in nh:
        if tong[k] > nh[k]: print(f"  · nhắc: {k} {tong[k]} > {nh[k]} — xem có ý trùng mới không (không kêu tái bản)")
    top = sorted(per.items(), key=lambda kv: -(kv[1]['dau_ngay'] + 3 * kv[1]['ghi_de']))[: (len(per) if CHI_TIET else 6)]
    print('  File chồng nhiều nhất:')
    for r, d in top:
        if d['dau_ngay'] + d['ghi_de']: print(f"   - {r}: {d['dau_ngay']} dấu ngày · {d['ghi_de']} câu ghi đè · {d['dong']} dòng")
    if trung:
        print(f'  Câu trùng ở nhiều file ({len(trung)}):' + ('' if CHI_TIET else ' (3 câu đầu, --chi-tiet để xem hết)'))
        for c, fs in list(trung.items())[: (len(trung) if CHI_TIET else 3)]:
            print(f"   - \"{c[:90]}…\" ở {', '.join(sorted(fs))}")
    if gt:
        print(f'  Cặp file có dòng gần trùng ({len(gt)}):' + ('' if CHI_TIET else ' (6 cặp nhiều nhất, --chi-tiet để xem hết)'))
        for (a, b), v in sorted(gt.items(), key=lambda kv: -len(kv[1]))[: (len(gt) if CHI_TIET else 6)]:
            print(f"   - {len(v)} · {a} ↔ {b} (dòng {', '.join(f'{x}↔{y}' for x, y in v[:4])})")
    if vuot:
        ket = 1; vuot_bo.append(f"{bo} ({'; '.join(vuot)})"); print(f"  ⇒ bộ {bo} vượt ngưỡng: " + '; '.join(vuot))
    else:
        print(f"  ⇒ bộ {bo} dưới ngưỡng.")
print('\n' + (f"⇒ NÊN NÂNG CẤP (hoc-lien-tuc Việc 4, dọn bằng tai-cau-truc): vượt ngưỡng ở {', '.join(vuot_bo)}" if vuot_bo else "⇒ Chưa cần nâng cấp."))
sys.exit(ket)
