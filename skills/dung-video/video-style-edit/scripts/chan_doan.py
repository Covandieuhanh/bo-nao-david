#!/usr/bin/env python3
"""CHẨN ĐOÁN VIDEO (trinh-bay/tu-chon.md, David chốt 11/11/2026): chan_doan.py <dự án>
Đo những gì máy đo được để Claude tự chọn bố cục nền, lớp thông tin, kiểu cảnh — không hỏi David.
→ check/chan-doan.md (số đo + gợi ý theo tu-chon.md) + check/chan-doan.jpg (6 khung gốc để Claude xem: mặt, chủ thể, rác).
Lời lấy từ motion/src/captions.js, không có thì check/goc/transcript.srt / words.srt."""
import glob, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load, node_env

P = os.path.expanduser(sys.argv[1]); M = os.path.join(P, "davinci/media")
pr = load(P)["project"]; W, H, D = pr["width"], pr["height"], float(pr.get("duration") or 0)

# 1. Lời: [(start, end, text)]
cap = []
cj = os.path.join(P, "motion/src/captions.js")
if os.path.exists(cj):
    t = open(cj, encoding="utf-8").read()
    cap = [(float(a), float(b), x) for a, b, x in re.findall(r"start:\s*([\d.]+),\s*end:\s*([\d.]+),\s*text:\s*[\"'](.*?)[\"']\s*[,}]", t)]
if not cap:
    srt = next((f for f in [os.path.join(P, "check/goc/transcript.srt"), *glob.glob(os.path.join(P, "check/**/*.srt"), recursive=True)] if os.path.exists(f)), None)
    if srt:
        ts = lambda s: sum(float(x) * m for x, m in zip(s.replace(",", ".").split(":"), (3600, 60, 1)))
        for blk in open(srt, encoding="utf-8").read().split("\n\n"):
            L = blk.strip().split("\n")
            if len(L) >= 3 and "-->" in L[1]:
                a, b = L[1].split("-->"); cap.append((ts(a.strip()), ts(b.strip()), " ".join(L[2:])))
if not D and cap: D = cap[-1][1]
words = sum(len(x.split()) for _, _, x in cap)
noi = sum(b - a for a, b, _ in cap)
mat_do = words / (D / 60) if D else 0
LK = re.compile(r"\b(thứ nhất|thứ hai|thứ ba|thứ tư|một là|hai là|ba là|bước \w+|đầu tiên|tiếp theo|sau đó|cuối cùng|thứ \d)\b", re.I)
SO = re.compile(r"\b\d+([.,]\d+)?\s*(%|phần trăm|triệu|nghìn|ngàn|tỷ|tuần|ngày|tháng|năm|phút|giờ|lần|người|bước)?\b", re.I)
lk = [a for a, _, x in cap if LK.search(x)]
so = [a for a, _, x in cap if SO.search(x)]
hoi = [a for a, _, x in cap if "?" in x]
fmt = lambda s: f"{int(s // 60)}:{s % 60:04.1f}"

# 2. Gợi ý theo tu-chon.md bước 3 (bước 2 cần mắt Claude trên chan-doan.jpg)
day = D >= 180 and (mat_do >= 140 or len(lk) + len(so) >= 6)
goi_y = []
if day: goi_y.append(f"DÀY THÔNG TIN ({mat_do:.0f} chữ/phút, {len(lk)} chỗ liệt kê/bước, {len(so)} câu có con số) → bảng ghi chú chạy `GHI_CHU`")
if D > 360: goi_y.append(f"dài {fmt(D)} → CHAPTERS + màn chương / thanh tiến trình ý")
if len(lk) >= 3: goi_y.append(f"{len(lk)} chỗ liệt kê/bước → illus list / flow, the-canh, muc-luc (mốc: {', '.join(fmt(x) for x in lk[:8])})")
if len(so) >= 3: goi_y.append(f"{len(so)} câu có con số → illus count / diagram cot / luoi (mốc: {', '.join(fmt(x) for x in so[:8])})")
if not goi_y: goi_y.append("ít ý, nhịp kể → người + phụ đề + điểm nhấn `nhan`, vài cảnh minh hoạ ở ý chính")

# 3. Tờ 6 khung gốc (bản chưa khung chủ thể nếu có)
src = next((os.path.join(M, f) for f in ("video_goc_truoc_khung.mp4", "video_goc_truoc_cat_khung.mp4", pr["source"]) if os.path.exists(os.path.join(M, f))), None)
jpg = os.path.join(P, "check/chan-doan.jpg")
if src and D:
    tmp = os.path.join(P, "check/chan-doan-tmp"); os.makedirs(tmp, exist_ok=True)
    for i in range(6):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{D * (i + 0.5) / 6:.2f}", "-i", src, "-frames:v", "1", "-vf", "scale=480:-2",
                        f"{tmp}/{i}.jpg"], env=node_env())
    subprocess.run(["ffmpeg", "-v", "error", "-y", *sum([["-i", f"{tmp}/{i}.jpg"] for i in range(6)], []), "-filter_complex",
                    "xstack=inputs=6:layout=0_0|w0_0|w0+w1_0|0_h0|w0_h0|w0+w1_h0", jpg], env=node_env())
    for f in glob.glob(f"{tmp}/*.jpg"): os.remove(f)
    os.rmdir(tmp)

out = [f"# Chẩn đoán — {os.path.basename(os.path.dirname(P)) or P}",
       f"Khung {W}×{H} · dài {fmt(D)} · lời {words} chữ, {mat_do:.0f} chữ/phút · có lời {noi / D * 100 if D else 0:.0f} % thời lượng · {len(hoi)} câu hỏi",
       "", "## Gợi ý lớp thông tin (tu-chon.md bước 3)", *[f"- {g}" for g in goi_y],
       "", "## Claude xem check/chan-doan.jpg rồi ghi (tu-chon.md bước 1–2)",
       "1. Mặt người nói: rõ / nhỏ / không thấy · 2. Chủ thể: … · 3. Rác quanh chủ thể: có / không · 4. Máy quay: đứng yên / dịch",
       "→ bố cục nền: giữ khung gốc / khung chủ thể (khung_chu_the.py) / pillar …"]
open(os.path.join(P, "check/chan-doan.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out)); print(jpg)
