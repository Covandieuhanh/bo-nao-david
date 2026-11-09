#!/usr/bin/env python3
"""Chạy MỌI luật kiểm trong thư mục này (file kiem_*.py): chay_kiem.py <dự án> <W> → W/kiem.md.
Thêm luật kiểm = thả thêm một file kiem_<tên>.py: nhận <dự án>, in MỘT dòng kết quả, mã thoát 0 = đạt, 1 = không đạt.
Có luật kiểm thất bại thì dừng; chưa được chuyển phát hành hoặc báo đạt."""
import glob, os, subprocess, sys
from pathlib import Path
P, W = sys.argv[1], sys.argv[2]; dong = []; loi = 0
ENV = dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", ""))
for f in sorted(glob.glob(str(Path(__file__).parent / "kiem_*.py"))):
    r = subprocess.run([sys.executable, "-I", f, P], capture_output=True, text=True, env=ENV, timeout=900)
    loi += r.returncode != 0
    kq = (r.stdout.strip().splitlines() or [r.stderr.strip()[-200:]])[-1]
    dong.append(f"- {'✅' if r.returncode == 0 else '❌'} **{Path(f).stem[5:]}**: {kq}")
md = "# Kết quả kiểm tự động\n\n" + "\n".join(dong) + "\n"
Path(W, "kiem.md").write_text(md, encoding="utf-8"); print(md)

sys.exit(1 if loi else 0)
