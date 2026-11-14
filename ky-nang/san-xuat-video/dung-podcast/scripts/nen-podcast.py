#!/usr/bin/env python3
"""Nền video podcast: nen-podcast.py <dự án> — tu-lieu/nen.mp4 (node xuat-video.mjs nen) + audio.m4a → video-goc.mp4.
Từ đây mọi bước của skill gốc dùng video-goc.mp4 như "video gốc" (render_preview, check_frames, pillar_base)."""
import os, subprocess, sys
P = os.path.expanduser(sys.argv[1]); M = os.path.join(P, "tu-lieu")
out = os.path.join(M, "video-goc.mp4")
subprocess.run(["/opt/homebrew/bin/ffmpeg", "-y", "-v", "error", "-i", os.path.join(M, "nen.mp4"), "-i", os.path.join(M, "audio.m4a"),
                "-map", "0:v:0", "-map", "1:a:0", "-c", "copy", "-shortest", "-movflags", "+faststart", out], check=True)
print(out)
