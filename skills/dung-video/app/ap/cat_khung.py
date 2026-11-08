#!/usr/bin/env python3
"""CẮT CHỮ/VIỀN IN CỨNG của video cũ: cat_khung.py <dự án> <W>
Đọc W/khung-trong.txt ("rộng:cao:x:y", Claude chọn ở bước lọc khi xem khung-giua.jpg) → cắt khung trong rồi phóng lại đúng cỡ gốc
(gotchas video-style-edit, 08/11/2026). Làm TRƯỚC tránh che mặt. Bản trước giữ ở davinci/media/video_goc_truoc_cat.mp4. Trống → bỏ qua."""
import os, subprocess, sys
from pathlib import Path
P, W = Path(sys.argv[1]), Path(sys.argv[2])
k = (W / "khung-trong.txt").read_text().strip() if (W / "khung-trong.txt").exists() else ""
if not k:
    print("không có chữ/viền in cứng — bỏ qua"); sys.exit(0)
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
v = P / "davinci/media/video_goc.mp4"; cu = v.with_name("video_goc_truoc_cat.mp4")
if not cu.exists(): os.replace(v, cu)
wh = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(cu)],
                    capture_output=True, text=True, env=ENV).stdout.strip().split(",")
r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(cu), "-vf", f"crop={k},scale={wh[0]}:{wh[1]}:flags=lanczos,setsar=1",
                    "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "copy", str(v)], env=ENV)
print(f"đã cắt khung {k} → phóng lại {wh[0]}×{wh[1]}" if r.returncode == 0 else "LỖI cắt khung"); sys.exit(r.returncode)
