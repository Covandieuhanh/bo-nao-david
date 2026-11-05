# TEASER MỞ ĐẦU cho video dài (David duyệt 2026-11-04 — học Have A Sip #118, Tuấn Tiền Tỉ, Trấn Thành: 15–30 s câu đắt nhất trước
# khi chào): teaser.py <dự án> <từ-đến> [<từ-đến> …]   (giây trong video-final.mp4 bản đã dựng, vd 812.4-818.9)
# Chọn 2–3 câu đắt nhất (nguyên văn, trọn câu — mốc lấy từ phụ đề), tổng 15–25 s. Cắt cứng, đã có sẵn phụ đề/đồ hoạ của bản dựng;
# mối nối fade âm 30 ms + 0,25 s đen nhẹ cuối teaser rồi vào video. Giữ bản cũ là video-final-khong-teaser.mp4.
# Ghi phat-hanh/teaser.json {len} → chapters.py tự cộng độ dài teaser vào mốc chương.
import json, os, subprocess, sys
P = os.path.expanduser(sys.argv[1]); segs = [tuple(map(float, a.split("-"))) for a in sys.argv[2:]]
env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
src = os.path.join(P, "video-final-khong-teaser.mp4")
fin = os.path.join(P, "video-final.mp4")
if not os.path.exists(src): os.rename(fin, src)
fc, cat = [], ""
for i, (a, b) in enumerate(segs):
    d = b - a; last = i == len(segs) - 1
    vf = f"trim={a}:{b},setpts=PTS-STARTPTS" + (f",fade=t=out:st={d - 0.25:.3f}:d=0.25" if last else "")
    fc.append(f"[0:v]{vf}[v{i}]")
    fc.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.03):.3f}:d=0.03[a{i}]")
    cat += f"[v{i}][a{i}]"
fc.append(f"[0:v]setpts=PTS-STARTPTS[vm];[0:a]asetpts=PTS-STARTPTS[am]")
fc.append(f"{cat}[vm][am]concat=n={len(segs) + 1}:v=1:a=1[v][a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", fin], check=True, env=env)
L = round(sum(b - a for a, b in segs), 3)
os.makedirs(os.path.join(P, "phat-hanh"), exist_ok=True)
json.dump({"len": L, "segs": segs}, open(os.path.join(P, "phat-hanh/teaser.json"), "w"))
print(f"teaser {L:.1f} s ({len(segs)} đoạn) → {fin}  · bản không teaser: {src}")
