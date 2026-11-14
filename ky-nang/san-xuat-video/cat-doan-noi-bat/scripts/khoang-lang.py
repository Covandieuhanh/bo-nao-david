# Cắt khoảng lặng BÊN TRONG câu cho video ngắn (David chốt 2026-11-04: "sao chép chuẩn kênh lớn" — DOAC, Hormozi, Jay Shetty
# cắt sạch khoảng chết, nhịp nói liền). Dùng chung cho cat-doan-noi-bat.py (bản kiểm lời, nhánh podcast) và danh-sach-cat-doan-noi-bat.py (nhánh người nói).
# split(P, a, b) → các đoạn giữ [(a1, b1), …] trong [a, b]: mỗi khoảng lặng ≥ MIN_GAP s (theo kiem-tra/goc/am-luong-05.txt, cùng ngưỡng
# kiem-am-luong.py) bị rút còn 2 × KEEP s. Không đụng 0,25 s đầu/cuối câu (mốc đã soát bằng loud_check).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../mo-dun")); import ho_so as hoso   # tham số: ho-so-thuong-hieu/highlight
_H = hoso.load('doan-noi-bat')
STEP = 0.05
MIN_GAP, KEEP, EDGE = hoso.get(_H, 'cat_lang.trong_cau_min_s', 0.45), hoso.get(_H, 'cat_lang.giu_s', 0.12), 0.25
_cache = {}

def _load(P):
    if P not in _cache:
        L = [tuple(map(float, l.split())) for l in open(os.path.join(P, "kiem-tra/goc/am-luong-05.txt")) if l.strip()]
        lv = sorted(v for _, v in L)
        p10, p50 = lv[len(lv) // 10], lv[len(lv) // 2]
        _cache[P] = (L, p10 + 0.35 * (p50 - p10))
    return _cache[P]

def split(P, a, b):
    if not os.path.exists(os.path.join(P, "kiem-tra/goc/am-luong-05.txt")):
        return [(a, b)]
    L, thr = _load(P)
    i0, i1 = round((a + EDGE) / STEP), round((b - EDGE) / STEP)
    keep, cur, q = [], a, None
    for i in range(max(0, i0), min(len(L), i1 + 1)):
        if L[i][1] < thr:
            q = i if q is None else q
            continue
        if q is not None and (i - q) * STEP >= MIN_GAP:
            keep.append((cur, q * STEP + KEEP)); cur = i * STEP - KEEP
        q = None
    keep.append((cur, b))
    return [(round(x, 3), round(y, 3)) for x, y in keep if y - x > 0.1]
