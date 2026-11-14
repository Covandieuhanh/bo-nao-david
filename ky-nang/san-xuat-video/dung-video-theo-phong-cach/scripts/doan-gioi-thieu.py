# TEASER MỞ ĐẦU cho video dài (David duyệt 2026-11-04 — học Have A Sip #118, Tuấn Tiền Tỉ, Trấn Thành: 15–30 s câu đắt nhất trước
# khi chào): doan-gioi-thieu.py <dự án> <từ-đến> [<từ-đến> …]   (giây trong video-hoan-chinh.mp4 bản đã dựng, vd 812.4-818.9)
# Chọn 2–3 câu đắt nhất (nguyên văn, trọn câu — mốc lấy từ phụ đề), tổng 15–25 s. Cắt cứng, đã có sẵn phụ đề/đồ hoạ của bản dựng;
# mối nối fade âm 30 ms + 0,25 s đen nhẹ cuối teaser rồi vào video. Giữ bản cũ là video-hoan-chinh-khong-gioi-thieu.mp4.
# Ghi phat-hanh/doan-gioi-thieu.json {len} → chuong.py tự cộng độ dài teaser vào mốc chương.
import json, os, subprocess, sys
P = os.path.expanduser(sys.argv[1]); segs = [tuple(map(float, a.split("-"))) for a in sys.argv[2:]]
env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
src = os.path.join(P, "video-hoan-chinh-khong-gioi-thieu.mp4")
fin = os.path.join(P, "video-hoan-chinh.mp4")
if not os.path.exists(src): os.rename(fin, src)
# Mỗi đoạn teaser là một đầu vào riêng (-ss/-t): dùng chung một đầu vào cho nhiều nhánh làm ffmpeg giữ cả video trong bộ nhớ
# → video dài bị hệ điều hành giết (SIGKILL, 08/11/2026)
fc, cat, ins = [], "", []
for i, (a, b) in enumerate(segs):
    d = b - a; last = i == len(segs) - 1
    ins += ["-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", src]
    fc.append(f"[{i}:v]setpts=PTS-STARTPTS" + (f",fade=t=out:st={d - 0.25:.3f}:d=0.25" if last else "") + f"[v{i}]")
    fc.append(f"[{i}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.03):.3f}:d=0.03[a{i}]")
    cat += f"[v{i}][a{i}]"
n = len(segs)
fc.append(f"{cat}[{n}:v][{n}:a]concat=n={n + 1}:v=1:a=1[v][a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-i", src, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", fin], check=True, env=env)
L = round(sum(b - a for a, b in segs), 3)
os.makedirs(os.path.join(P, "phat-hanh"), exist_ok=True)
json.dump({"len": L, "cac-doan": segs}, open(os.path.join(P, "phat-hanh/doan-gioi-thieu.json"), "w"))
print(f"teaser {L:.1f} s ({len(segs)} đoạn) → {fin}  · bản không teaser: {src}")
