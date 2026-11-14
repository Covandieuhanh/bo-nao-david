# Nền khung ngang (chế độ pillar): pillar_base.py <dự án>
# hai_ben.mp4 (node render.mjs hai-ben) + video gốc dọc thu vào cột giữa + tiếng gốc → davinci/media/nen_ngang.mp4
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load, node_env

P = os.path.expanduser(sys.argv[1])
d = load(P); pr, o = d["project"], d["out"]
M = os.path.join(P, "davinci/media")
cw = round(pr["width"] * o["height"] / pr["height"] / 2) * 2          # cùng công thức CENTER trong layout.js
x = round((o["width"] - cw) / 2)
FPS = f'{pr["fpsNum"]}/{pr["fpsDen"]}'
out = os.path.join(M, o["base"])
subprocess.run(["ffmpeg", "-y", "-v", "error", "-stats", "-i", os.path.join(M, "hai_ben.mp4"), "-i", os.path.join(M, pr["source"]),
                "-filter_complex", f"[1:v]scale={cw}:{o['height']}:flags=lanczos,setsar=1[c];[0:v][c]overlay={x}:0:shortest=1[v]",
                "-map", "[v]", "-map", "1:a", "-r", FPS, "-c:v", "h264_videotoolbox", "-b:v", "16M", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True, env=node_env())
print(out)
