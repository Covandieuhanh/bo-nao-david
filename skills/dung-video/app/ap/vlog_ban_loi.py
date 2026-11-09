#!/usr/bin/env python3
"""LỜI TỪNG CLIP cho Claude: vlog_ban_loi.py <dự án> <W> → W/ban-loi-clip.txt: mỗi clip thời lượng + lời có mốc (giây trong clip)."""
import subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import loi
from vlog_chung import ds_clip
from hl_chung import ENV
P, W = Path(sys.argv[1]), Path(sys.argv[2]); out = []
for c in ds_clip(P):
    v = P / f"motion/public/clips/{c}.mp4"
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(v)], capture_output=True, text=True, env=ENV).stdout.strip()
    out.append(f"== {c} · {float(dur or 0):.1f} s · lưới hình: check/{c}/contact.jpg")
    w, t = P / f"check/{c}/words.srt", P / f"check/{c}/transcript.srt"
    if w.exists() and t.exists():
        tmp = W / f".bl-{c}.txt"; loi.ban_loi(w, t, tmp); out += tmp.read_text(encoding="utf-8").splitlines() or ["(không lời)"]; tmp.unlink()
    else:
        out.append("(không lời)")
    out.append("")
(W / "ban-loi-clip.txt").write_text("\n".join(out), encoding="utf-8"); print(f"{len(ds_clip(P))} clip")
