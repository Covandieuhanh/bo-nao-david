#!/usr/bin/env python3
"""TỜ KIỂM TRA cho David xem ở cổng 2 (khối 17 bước 9): to_kiem_tra.py <dự án>
Mốc = giữa + cuối mỗi cảnh, vài chỗ không có cảnh, màn chốt → check_frames.sh ghép thành check/sheet.jpg (có khung an toàn)."""
import json, os, re, subprocess, sys
from pathlib import Path
P = Path(sys.argv[1]); S = Path(__file__).resolve().parents[2] / "video-style-edit/scripts"
s = (P / "motion/src/scenes.js").read_text(encoding="utf-8")
i = s.index("export const SCENES = ") + len("export const SCENES = "); j = s.index("\n];", i) + 2
C = json.loads(s[i:j]); dur = float(re.search(r"duration: *([\d.]+)", (P / "motion/src/project.js").read_text()).group(1))
moc = []
for c in C:
    moc += [(c["start"] + c["end"]) / 2, c["end"] - 0.4]
trong = [t for t in (dur * 0.1, dur * 0.5, dur * 0.8) if not any(c["start"] <= t <= c["end"] for c in C)]
moc = sorted({round(t, 1) for t in moc + trong if 0 < t < dur})[:40]
env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
r = subprocess.run(["zsh", str(S / "check_frames.sh"), str(P), str(P / "video-final.mp4"), *map(str, moc)], env=env)
print(f"{len(moc)} mốc → {P}/check/sheet.jpg"); sys.exit(r.returncode)
