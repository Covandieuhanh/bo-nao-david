#!/usr/bin/env python3
"""CHẠY MỘT VIỆC CHO MỌI CLIP: hl_moi_clip.py <dự án highlight> bao-ve|render|kiem
bao-ve: lift.py + overlay_guard.py (lớp phủ không che mặt/thân trên) · render: render-show.mjs (NỐI TIẾP, không song song — tốn RAM)
kiem: mọi luật kiểm (app/kiem) cho từng clip → <W>/kiem.md gộp."""
import subprocess, sys
from pathlib import Path
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))   # python -I không tự thấy file cùng thư mục
from hl_chung import S, ENV, clips
H, viec = Path(sys.argv[1]), sys.argv[2]; W = sys.argv[3] if len(sys.argv) > 3 else None
md = ["# Kết quả kiểm tự động — các clip highlight", ""]
for ma, E in clips(H):
    print(f"== clip {ma}", flush=True)
    if viec == "bao-ve":
        subprocess.run(["python3", "-I", str(S / "lift.py"), str(E)], env=ENV, check=True)
        subprocess.run(["python3", "-I", str(S / "overlay_guard.py"), str(E)], env=ENV, check=True)
    elif viec == "render":
        subprocess.run(["node", "render-show.mjs"], cwd=E / "motion", env=ENV, check=True)
        if not (E / "video-final.mp4").exists(): raise SystemExit(f"clip {ma}: chưa ra video-final.mp4")
    elif viec == "kiem":
        r = subprocess.run(["python3", "-I", str(Path(__file__).resolve().parents[1] / "kiem/chay_kiem.py"), str(E), str(E / "check")],
                           env=ENV, capture_output=True, text=True)
        md += [f"## Clip {ma}"] + [l for l in r.stdout.splitlines() if l.startswith("- ")] + [""]
if viec == "kiem" and W:
    Path(W, "kiem.md").write_text("\n".join(md), encoding="utf-8"); print("\n".join(md))
