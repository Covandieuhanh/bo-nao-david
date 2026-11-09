#!/usr/bin/env python3
"""Tờ hình trải đều video: tạo trong thư mục mới, mọi khung phải cắt thành công, không dùng ảnh kiểm cũ."""
import os, subprocess, sys, tempfile
from pathlib import Path
v, ra = sys.argv[1], Path(sys.argv[2]); n = int(sys.argv[3]) if len(sys.argv)>3 else 24
if n < 2: raise SystemExit("Cần ít nhất hai khung để kiểm")
env = dict(os.environ, PATH="/opt/homebrew/bin:"+os.environ.get("PATH", ""))
r=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",v],capture_output=True,text=True,env=env,check=True)
d=float(r.stdout); ra.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix="to-hinh-",dir=ra.parent) as tmp:
    tmp=Path(tmp)
    for i in range(n):
        t=min(d-0.05,max(0.0,d*i/(n-1)))
        f=tmp/f"{i:03d}.jpg"
        cmd=["ffmpeg","-v","error","-y","-ss",f"{t:.2f}","-i",v,"-frames:v","1","-vf"]
        r=subprocess.run(cmd+[f"scale=360:-2,drawtext=text='{t:.1f}s':x=8:y=8:fontsize=22:fontcolor=white:box=1:boxcolor=black@0.6",str(f)],capture_output=True,env=env)
        if r.returncode:
            subprocess.run(cmd+["scale=360:-2",str(f)],env=env,check=True)
            print(f"Lưu ý: khung {t:.1f}s không ghi được chữ mốc")
        if not f.exists():raise SystemExit(f"Không lấy được khung {t:.2f}s; dừng thay vì dùng ảnh cũ")
    output=tmp/"sheet.jpg"
    subprocess.run(["ffmpeg","-v","error","-y","-framerate","1","-i",str(tmp/"%03d.jpg"),"-vf",f"tile=6x{(n+5)//6}","-frames:v","1",str(output)],env=env,check=True)
    os.replace(output,ra)
print(f"{n} khung (cả đầu/cuối) → {ra}")
