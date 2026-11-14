#!/usr/bin/env python3
"""Dời lời đã chép từ bản thô sang bản sạch (không chép lại): doi-moc-loi.py <dự án>
Đọc kiem-tra/lam-sach/{ban-chep-loi,moc-tung-tu}.srt (mốc bản thô) + cac-doan.json → kiem-tra/goc/{ban-chep-loi,moc-tung-tu}.srt (mốc bản sạch).
Từ / câu nằm trong đoạn đã cắt bị bỏ. Dùng khi chỉ cắt vài đoạn (vd. lời chào kênh cũ ở video dài) — nhanh, nhẹ máy hơn
phan-tich-video.sh và giữ nguyên chữ đã soát. (2026-11-08)"""
import json, os, re, sys
P = os.path.expanduser(sys.argv[1])
seg = json.load(open(os.path.join(P, "kiem-tra/lam-sach/cac-doan.json")))
T = lambda h, m, s, ms: int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
def f(x):
    x = max(0, x); h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)) % 1000:03d}"
def mp(t):
    for g in seg:
        if g["raw_start"] - 0.05 <= t <= g["raw_end"] + 0.05: return g["clean_start"] + min(max(t, g["raw_start"]), g["raw_end"]) - g["raw_start"]
    return None
os.makedirs(os.path.join(P, "kiem-tra/goc"), exist_ok=True)
for name in ("ban-chep-loi", "moc-tung-tu"):
    src = os.path.join(P, f"kiem-tra/lam-sach/{name}.srt")
    if not os.path.exists(src): continue
    txt = open(src, encoding="utf-8").read(); out = []; n = 0
    for m in re.finditer(r"(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)\n([^\n]*)", txt):
        a, b = mp(T(*m.groups()[:4])), mp(T(*m.groups()[4:8]))
        if a is None or b is None or b < a: continue
        n += 1; out.append(f"{n}\n{f(a)} --> {f(b)}\n{m.group(9)}\n")
    open(os.path.join(P, f"kiem-tra/goc/{name}.srt"), "w", encoding="utf-8").write("\n".join(out))
    print(name, n, "dòng")
