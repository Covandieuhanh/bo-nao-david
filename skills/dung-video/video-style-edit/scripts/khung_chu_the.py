#!/usr/bin/env python3
"""KHUNG CHỦ THỂ (khối 04, David chốt 11/11/2026): tách đúng phần cần xem của video gốc (màn hình điện thoại, laptop, bảng, sản phẩm…)
thành một khung bo góc đặt trên nền kênh — mọi rác xung quanh (bàn, tường, sổ…) biến mất; phần khung còn lại dành cho bảng ghi chú
chạy (Captions.jsx `GHI_CHU`), phụ đề và cảnh minh hoạ. Khác "cắt khung rồi phóng" (vẫn còn rác quanh chủ thể).

  khung_chu_the.py <dự án> luoi [giây …]   → check/khung/luoi.jpg: khung gốc có lưới 10 % (vạch dày ở 50 %) để đọc toạ độ chủ thể
  khung_chu_the.py <dự án> apply           → đọc check/khung.json, dựng lại davinci/media/video_goc.mp4 (bản trước: video_goc_truoc_khung.mp4,
                                              mỗi lần apply luôn dựng từ bản này) + ghi motion/src/khung.js (vị trí khung trên hình xuất)

check/khung.json — toạ độ theo PIXEL video gốc; máy quay dịch thì thêm vùng theo mốc giây (mọi vùng cùng w, h):
  {"phia": "trai", "vung": [{"tu": 0, "den": 271.8, "x": 410, "y": 60, "w": 520, "h": 960}, {"tu": 271.8, "x": 380, "y": 40}]}
  phia: "trai" | "phai" — khung chủ thể nằm phía nào (bên kia là bảng ghi chú, phụ đề, cảnh).
Chạy SAU làm sạch (bản sạch), TRƯỚC chép lại phụ đề / face_place.sh. face_place.sh đọc khung.js: "người" = khung chủ thể (không dò mặt).
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load, node_env

P = os.path.expanduser(sys.argv[1]); MODE = sys.argv[2] if len(sys.argv) > 2 else "luoi"
M = os.path.join(P, "davinci/media"); CK = os.path.join(P, "check/khung"); os.makedirs(CK, exist_ok=True)
pr = load(P)["project"]; W, H = pr["width"], pr["height"]; FPS = f'{pr["fpsNum"]}/{pr["fpsDen"]}'
goc = os.path.join(M, "video_goc_truoc_khung.mp4")
src = goc if os.path.exists(goc) else os.path.join(M, pr["source"])
run = lambda a: subprocess.run(a, check=True, env=node_env())
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src],
                           capture_output=True, text=True, env=node_env()).stdout)

if MODE == "luoi":
    ts = [float(x) for x in sys.argv[3:]] or [dur * (i + 0.5) / 6 for i in range(6)]
    for i, t in enumerate(ts):
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", src, "-frames:v", "1", "-vf",
             f"drawgrid=w=iw/10:h=ih/10:t=2:c=white@0.5,drawgrid=w=iw/2:h=ih/2:t=5:c=orange@0.9,scale=640:-2", f"{CK}/l{i}.jpg"])
    n = len(ts); cols = min(3, n)
    ins = sum([["-i", f"{CK}/l{i}.jpg"] for i in range(n)], [])
    lay = "|".join(f"{'+'.join(['w0'] * (i % cols)) or '0'}_{'+'.join(['h0'] * (i // cols)) or '0'}" for i in range(n))
    run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", f"xstack=inputs={n}:layout={lay}:fill=black" if n > 1 else "null",
         f"{CK}/luoi.jpg"])
    print(f"{CK}/luoi.jpg  (lưới 10 %, vạch cam = giữa khung; khung gốc {W}×{H}; mốc: {', '.join(f'{t:.1f}' for t in ts)})")
    sys.exit(0)

cfg = json.load(open(os.path.join(P, "check/khung.json"), encoding="utf-8"))
V = sorted(cfg["vung"], key=lambda v: v.get("tu", 0)); cw, ch = V[0]["w"], V[0]["h"]
for v in V:   # mọi vùng cùng cỡ (crop không đổi cỡ theo thời gian) — vùng khác cỡ thì giữ tâm, lấy cỡ vùng đầu
    if (v.get("w", cw), v.get("h", ch)) != (cw, ch):
        v["x"] += (v["w"] - cw) / 2; v["y"] += (v["h"] - ch) / 2
    v["x"] = max(0, min(W - cw, round(v["x"]))); v["y"] = max(0, min(H - ch, round(v["y"])))
pw_expr = lambda k: "".join(f"if(lt(t,{v2['tu']:.3f}),{v1[k]}," for v1, v2 in zip(V, V[1:])) + str(V[-1][k]) + ")" * (len(V) - 1)

# Vị trí khung trên hình xuất: dưới dấu góc, trên thanh thời gian; lề trái/phải = lề an toàn 5 %
TOP, BOT, LE = round(H * 0.11), round(H * 0.90), round(W * 0.05)
PH = BOT - TOP; PW = round(PH * cw / ch / 2) * 2
if PW > W * 0.56: PW = round(W * 0.56 / 2) * 2; PH = round(PW * ch / cw / 2) * 2   # chủ thể bè ngang (laptop, bảng)
PY = TOP + (BOT - TOP - PH) // 2
PX = LE if cfg.get("phia", "trai") == "trai" else W - LE - PW
R, B = 28, 4   # bo góc, viền cam

# Nền kênh: nền tối C.bg + quầng cam rất nhẹ sau khung + viền cam mảnh quanh khung (một ảnh tĩnh, nhanh)
gx, gy, sg = PX + PW / 2, PY + PH / 2, W * 0.32
bg, mask = f"{CK}/nen.png", f"{CK}/mask.png"
rr = lambda w, h, r: f"lte(hypot(max(0,abs(X-{w}/2)-({w}/2-{r})),max(0,abs(Y-{h}/2)-({h}/2-{r}))),{r})"
q = f"exp(-((X-{gx})*(X-{gx})+(Y-{gy})*(Y-{gy}))/(2*{sg}*{sg}))"
run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=black:s={W}x{H}:d=1",
     "-f", "lavfi", "-i", f"color=0xFF7A45:s={PW + 2 * B}x{PH + 2 * B}:d=1", "-filter_complex",
     f"[0:v]format=rgb24,geq=r='13+255*0.10*{q}':g='13+122*0.10*{q}':b='16+69*0.10*{q}'[n];"
     f"[1:v]format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='150*{rr(PW + 2 * B, PH + 2 * B, R + B)}'[v];"
     f"[n][v]overlay={PX - B}:{PY - B},format=rgb24", "-frames:v", "1", bg])
run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=black:s={PW}x{PH}:d=1", "-vf",
     f"format=gray,geq=lum='255*{rr(PW, PH, R)}'", "-frames:v", "1", mask])

if not os.path.exists(goc): os.rename(os.path.join(M, pr["source"]), goc); src = goc
out = os.path.join(M, pr["source"])
if os.path.exists(out) and os.path.samefile(out, src): os.remove(out)   # cùng một file (liên kết cứng) → ffmpeg ghi đè chính nguồn (11/11/2026 mất bản sạch)
run(["ffmpeg", "-y", "-v", "error", "-stats", "-loop", "1", "-framerate", FPS, "-i", bg, "-loop", "1", "-framerate", FPS, "-i", mask,
     "-i", src, "-filter_complex",
     f"[2:v]crop={cw}:{ch}:'{pw_expr('x')}':'{pw_expr('y')}',scale={PW}:{PH}:flags=lanczos,format=yuva420p[c];"
     f"[1:v]format=gray[m];[c][m]alphamerge[p];[0:v][p]overlay={PX}:{PY}:shortest=1,format=yuv420p,setsar=1[v]",
     "-map", "[v]", "-map", "2:a", "-r", FPS, "-c:v", "h264_videotoolbox", "-b:v", "16M", "-c:a", "copy",
     "-movflags", "+faststart", out])
k = {"x": PX / W, "y": PY / H, "w": PW / W, "h": PH / H, "phia": cfg.get("phia", "trai")}
open(os.path.join(P, "motion/src/khung.js"), "w", encoding="utf-8").write(
    "// Khung chủ thể trên hình xuất (0–1) — scripts/khung_chu_the.py tự ghi; null = không dùng bố cục khung chủ thể\n"
    "export default " + json.dumps(k) + ";\n")
print(out, "· khung", k)
