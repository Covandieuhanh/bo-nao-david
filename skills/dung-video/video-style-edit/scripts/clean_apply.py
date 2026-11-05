# Áp cắt + sửa chiều hình: clean_apply.py <dự án>
# Đọc check/clean/cuts.json (chỉ các cut ok=true) → davinci/media/video_goc.mp4 (bản sạch), giữ bản thô là
# video_goc_raw.<ext>, cập nhật motion/src/project.js, ghi segments.json (mốc thô ↔ mốc sạch) + bảng vào cuts.md.
#   orient: danh sách trong "180", "cw" (xoay phải 90°), "ccw" (xoay trái 90°), "mirror" (lật gương)
#   zoom:   "alt" = đoạn xen kẽ phóng 1,08× để che cú nhảy hình ở mối cắt giữa video; "none" = không
import glob, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import node_env

P = os.path.expanduser(sys.argv[1])
MEDIA, O = os.path.join(P, "davinci", "media"), os.path.join(P, "check", "clean")
ENV = node_env()
cfg = json.load(open(os.path.join(O, "cuts.json"), encoding="utf-8"))

raw = glob.glob(os.path.join(MEDIA, "video_goc_raw.*"))
if raw:
    raw = raw[0]
else:   # lần đầu: đổi tên bản thô (macOS không phân biệt hoa/thường: .MP4 và .mp4 là MỘT file)
    src = glob.glob(os.path.join(MEDIA, "video_goc.*"))[0]
    raw = os.path.join(MEDIA, "video_goc_raw" + os.path.splitext(src)[1])
    os.rename(src, raw)

probe = lambda *a: subprocess.check_output(["ffprobe", "-v", "error", *a, raw], env=ENV).decode().strip()
DUR = float(probe("-show_entries", "format=duration", "-of", "csv=p=0"))
W, H, FR = probe("-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate", "-of", "csv=p=0").split(",")[:3]
W, H = int(W), int(H)
rot = probe("-select_streams", "v:0", "-show_entries", "stream_side_data=rotation", "-of", "csv=p=0")
if re.search(r"-?(90|270)\b", rot): W, H = H, W
fn, fd = (int(x) for x in FR.split("/"))
fps = fn / fd
snap = lambda t: round(t * fps) / fps

# Đoạn giữ = toàn bộ trừ các cut ok (gộp chồng lấn), làm tròn về khung
cuts = sorted((max(0, c["start"]), min(DUR, c["end"])) for c in cfg["cuts"] if c.get("ok"))
keep, t = [], 0.0
for a, b in cuts:
    if a > t: keep.append([t, a])
    t = max(t, b)
if t < DUR: keep.append([t, DUR])
keep = [[snap(a), snap(b)] for a, b in keep if b - a >= 0.2]

orient = {"180": "hflip,vflip", "cw": "transpose=1", "ccw": "transpose=2", "mirror": "hflip"}
vf = [orient[o] for o in cfg.get("orient", [])]
if any(o in ("cw", "ccw") for o in cfg.get("orient", [])): W, H = H, W
# Chuẩn hoá cỡ khung: component thiết kế trên 1080×1920 (dọc) / 1920×1080 (ngang). Video iPhone đã cắt (vd. 770×1368)
# hay 720p → phóng về khung chuẩn; tỉ lệ lệch 9:16 quá 2% thì giữ tỉ lệ, cạnh ngắn = 1080.
short, long_ = sorted((W, H))
OS, OL = (1080, 1920) if abs(long_ / short - 16 / 9) < 0.04 else (1080, round(1080 * long_ / short / 2) * 2)
OW, OH = (OS, OL) if H > W else (OL, OS)
fit = f"scale={OW}:{OH}:flags=lanczos,setsar=1"
Z = 1.08
zoom = f"crop=trunc(iw/{Z}/2)*2:trunc(ih/{Z}/2)*2:(iw-ow)/2:(ih-oh)*0.35"   # neo cao để giữ mặt

fc, cat = [], ""
for i, (a, b) in enumerate(keep):
    v = [f"trim=start={a:.4f}:end={b:.4f}", "setpts=PTS-STARTPTS", *vf]
    if cfg.get("zoom", "alt") == "alt" and i % 2: v.append(zoom)
    v.append(fit)
    d = b - a
    fc.append(f"[0:v]{','.join(v)}[v{i}]")
    fc.append(f"[0:a]atrim=start={a:.4f}:end={b:.4f},asetpts=PTS-STARTPTS,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
              f"afade=t=in:d=0.015,afade=t=out:st={max(0, d - 0.03):.4f}:d=0.03[a{i}]")   # chống tiếng "tách" ở mối
    cat += f"[v{i}][a{i}]"
fc.append(f"{cat}concat=n={len(keep)}:v=1:a=1[v][a]")

out = os.path.join(MEDIA, "video_goc.mp4")
script = os.path.join(O, "filter.txt")
open(script, "w").write(";\n".join(fc))
subprocess.run(["ffmpeg", "-y", "-v", "error", "-stats", "-i", raw, "-/filter_complex", script,
                "-map", "[v]", "-map", "[a]", "-r", FR, "-fps_mode", "cfr",
                "-c:v", "h264_videotoolbox", "-b:v", "20M", "-pix_fmt", "yuv420p",   # mã hoá phần cứng: libx264 chậm ~10×
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True, env=ENV)

new_dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out], env=ENV))
open(os.path.join(P, "motion", "src", "project.js"), "w").write(
    "// Thông số video gốc (bản đã làm sạch) — tự điền bởi clean_apply.py\n"
    f"export default {{fpsNum: {fn}, fpsDen: {fd}, width: {OW}, height: {OH}, duration: {new_dur:.3f}, source: 'video_goc.mp4'}};\n")

# Bảng quy đổi mốc thô → mốc sạch (dùng khi đổi cắt sau khi đã có scenes.js)
seg, c = [], 0.0
for a, b in keep:
    seg.append(dict(raw_start=a, raw_end=b, clean_start=round(c, 3))); c += b - a
json.dump(seg, open(os.path.join(O, "segments.json"), "w"), indent=1)
mmss = lambda t: f"{int(t // 60)}:{t % 60:04.1f}"
with open(os.path.join(O, "cuts.md"), "a", encoding="utf-8") as f:
    f.write(f"\n## Đã áp ({len(cuts)} cắt, xoay/lật: {cfg.get('orient') or 'không'}, zoom: {cfg.get('zoom', 'alt')})\n"
            f"Thô {DUR:.1f}s → sạch {new_dur:.1f}s (−{DUR - new_dur:.1f}s). Mối nối trong bản sạch: "
            + ", ".join(mmss(s["clean_start"]) for s in seg[1:]) + "\n")
print(f"{len(keep)} đoạn · {DUR:.1f}s → {new_dur:.1f}s · {OW}x{OH} → {out}")
