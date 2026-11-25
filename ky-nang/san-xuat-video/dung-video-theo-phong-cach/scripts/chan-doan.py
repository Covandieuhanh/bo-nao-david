#!/usr/bin/env python3
"""CHẨN ĐOÁN VIDEO (thiet-ke-bo-cuc/tu-chon.md, David chốt 11/11/2026): chan-doan.py <dự án>
Đo những gì máy đo được để Claude tự chọn bố cục nền, lớp thông tin, kiểu cảnh — không hỏi David.
→ kiem-tra/chan-doan.md (số đo + gợi ý theo tu-chon.md) + kiem-tra/chan-doan.jpg (6 khung gốc để Claude xem: mặt, chủ thể, rác).
Lời lấy từ chuyen-dong/src/phu-de.js, không có thì kiem-tra/goc/ban-chep-loi.srt / moc-tung-tu.srt."""
import glob, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _chung import load, node_env

P = os.path.expanduser(sys.argv[1]); M = os.path.join(P, "tu-lieu")
cap = []
GHEP = not os.path.exists(os.path.join(P, "chuyen-dong/src/du-an.js")) and os.path.exists(os.path.join(P, "chuyen-dong/src/danh-sach-cat.js"))
if GHEP:   # khuôn ghép (vlog, highlight, bản theo hướng — 19/11/2026: trước đây máy này chỉ đọc khuôn 1 video nên khuôn ghép bỏ qua chẩn đoán)
    code = ("import('./src/danh-sach-cat.js').then((e) => console.log(JSON.stringify({W: e.W, H: e.H, T: e.TOTAL, "
            "S: (e.SUBS || []).map((x) => [x.start, x.end, x.text])})))")
    e = json.loads(subprocess.check_output(["node", "-e", code], cwd=os.path.join(P, "chuyen-dong"), env=node_env(), stderr=subprocess.DEVNULL))
    W, H, D = e["W"], e["H"], float(e["T"] or 0); cap = [tuple(x) for x in e["S"]]
    M = os.path.join(P, "chuyen-dong/public/doan-video"); pr = {"source": "c1.mp4"}
else:
    pr = load(P)["project"]; W, H, D = pr["width"], pr["height"], float(pr.get("duration") or 0)

# 1. Lời: [(start, end, text)]
cj = os.path.join(P, "chuyen-dong/src/phu-de.js")
if not cap and os.path.exists(cj):
    t = open(cj, encoding="utf-8").read()
    cap = [(float(a), float(b), x) for a, b, x in re.findall(r"start:\s*([\d.]+),\s*end:\s*([\d.]+),\s*text:\s*[\"'](.*?)[\"']\s*[,}]", t)]
if not cap:
    srt = next((f for f in [os.path.join(P, "kiem-tra/goc/ban-chep-loi.srt"), *glob.glob(os.path.join(P, "kiem-tra/**/*.srt"), recursive=True)] if os.path.exists(f)), None)
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
SS = re.compile(r"\b(không phải|mà là|thay vì|so với|khác với|trước đây|bây giờ|còn)\b", re.I)
NQ = re.compile(r"\b(nếu mà|nếu|bởi vì|tại vì|cho nên|dẫn đến|vì thế)\b", re.I)
CX = re.compile(r"\b(thương|sợ|khóc|buồn|vui|hạnh phúc|đau|mệt|áp lực|cô đơn|tự hào|biết ơn|yêu)\b", re.I)
ss = [a for a, _, x in cap if SS.search(x)]; nq = [a for a, _, x in cap if NQ.search(x)]; cx = [a for a, _, x in cap if CX.search(x)]
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
if len(ss) >= 3: goi_y.append(f"{len(ss)} câu so sánh / đổi ý → illus vs, diagram tu-thanh, the-canh gạch chữ (mốc: {', '.join(fmt(x) for x in ss[:8])})")
if len(nq) >= 6: goi_y.append(f"{len(nq)} câu nhân quả / điều kiện → illus flow, diagram chuyen-giao (mốc: {', '.join(fmt(x) for x in nq[:8])})")
if not goi_y: goi_y.append("ít ý, nhịp kể → người + phụ đề + điểm nhấn `nhan`, vài cảnh minh hoạ ở ý chính")
if GHEP: goi_y.append("khuôn ghép có sẵn: illus (single/flow/vs/count/list) · diagram (tang, vong, moc, cot, luoi, tu-thanh, chuyen-giao) · "
                      "chips · callout · action · pointer · pow — dùng theo bảng tu-chon.md bước 4, không chỉ pow")
# Tín hiệu thẩm mỹ (tu-chon.md bước 2b) — công cụ đo, Claude chọn
tone = ("lắng, cảm xúc" if len(cx) >= 3 and mat_do < 150 else "kiến thức, nhịp đều" if day or len(lk) + len(so) >= 4 else "kể chuyện / trò chuyện")
tham_my = [f"giọng: {tone} ({len(cx)} câu cảm xúc, {mat_do:.0f} chữ/phút, {len(hoi)} câu hỏi)",
           f"khung {'dọc' if H > W else 'ngang'}, dài {fmt(D)} → {'mỗi lúc một điểm nhìn, chữ to' if H > W else 'có chỗ cho người + ý cùng lúc'}"]

# 3. Tờ 6 khung gốc (bản chưa khung chủ thể nếu có)
src = next((os.path.join(M, f) for f in ("video-goc-truoc-khung.mp4", "video-goc-truoc-cat-khung.mp4", pr["source"]) if os.path.exists(os.path.join(M, f))), None)
jpg = os.path.join(P, "kiem-tra/chan-doan.jpg")
if src and D:
    tmp = os.path.join(P, "kiem-tra/chan-doan-tam"); os.makedirs(tmp, exist_ok=True)
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
       "", "## Tín hiệu thẩm mỹ (tu-chon.md bước 2b)", *[f"- {g}" for g in tham_my],
       "", "## Claude xem kiem-tra/chan-doan.jpg rồi ghi (tu-chon.md bước 1–2)",
       "1. Mặt người nói: rõ / nhỏ / không thấy · 2. Chủ thể: … · 3. Rác quanh chủ thể: có / không · 4. Máy quay: đứng yên / dịch",
       "→ bố cục nền: giữ khung gốc / khung chủ thể (khung-chu-the.py) / pillar …",
       "Thẩm mỹ: nền … · kiểu hình … · chuyển cảnh … · nhạc … vì …  (bắt buộc, soat-canh báo nếu thiếu)",
       "⚠️ Người chiếm < ~50 % khung (ngồi xa, hai bên tường trống) + nội dung kiến thức / DÀY THÔNG TIN → KHUNG CHỦ THỂ quanh người + bảng `GHI_CHU`, không giữ khung gốc"]
open(os.path.join(P, "kiem-tra/chan-doan.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out)); print(jpg)
