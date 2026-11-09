#!/usr/bin/env python3
"""DỰNG KHUNG TỪNG CLIP (nhánh người nói, skill 7A): hl_dung.py <dự án highlight>
Mỗi phương án: new_montage.sh hl-<tập>-<mã> <nguồn> → clip-<mã>/, hl_edl.py viết edl.js, chép kho nhạc kênh.
Giữ bản edl.js gốc (edl.goc.js) để bước lớp phủ luôn áp lên bản sạch (chạy lại không bị nhân đôi)."""
import glob, shutil, subprocess, sys
from pathlib import Path
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))   # python -I không tự thấy file cùng thư mục
from hl_chung import HL, S, ENV, clips, tap
H = Path(sys.argv[1]); nguon = glob.glob(str(H / "nguon.*"))[0]
for ma, E in clips(H):
    if not (E / "motion/public/clips/c1.mp4").exists():
        if E.exists(): shutil.move(str(E), str(Path.home() / ".Trash" / f"{H.parent.name}-clip-{ma}-do-dang"))
        subprocess.run(["zsh", str(S / "new_montage.sh"), f"hl-{tap(H)}-{ma}", nguon], env=ENV, check=True)
    subprocess.run(["python3", "-I", str(HL / "hl_edl.py"), str(H), str(E), ma], env=ENV, check=True)
    shutil.copy2(E / "motion/src/edl.js", E / "motion/src/edl.goc.js")
    for m in (HL.parent / "assets/music").glob("*.mp3"):
        shutil.copy2(m, E / "motion/public/sfx" / m.name)
    print(f"clip {ma}: khung dựng xong → {E}")
