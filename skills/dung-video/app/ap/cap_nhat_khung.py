#!/usr/bin/env python3
"""CẬP NHẬT KHUNG DỰNG cho một dự án đang làm: cap_nhat_khung.py <dự án>

Lúc tạo dự án, skill CHÉP khung dựng Remotion + thư viện hình vào <dự án>/motion (để dự án cũ render lại vẫn ra như cũ).
Sửa thư viện hình / template sau đó thì dự án đang làm không tự theo — chạy lệnh này: chép lại khung dựng mới nhất,
GIỮ NGUYÊN dữ liệu riêng của video (DU_LIEU dưới đây), ghi lại hồ sơ tham số. Bản cũ cất ở check/khung-truoc-<giờ>/.
Sau đó render lại (render_doi.py thấy khung đổi → render tất cả).
"""
import filecmp, os, shutil, subprocess, sys, time
from pathlib import Path

DV = Path(__file__).resolve().parents[2]
MAU = DV / "video-style-edit/assets/remotion-template"
# Dữ liệu riêng của từng video (kịch bản, phụ đề, thông số, vị trí mặt, khung xuất, người nói…) — không bao giờ ghi đè.
DU_LIEU = {"scenes.js", "captions.js", "project.js", "output.js", "placement.js", "mat.js", "speakers.js", "envelope.js", "highlight.js"}

P = Path(sys.argv[1]); M = P / "motion"
if not (M / "src").is_dir():
    raise SystemExit("Dự án chưa có khung dựng (chưa qua bước Tạo dự án).")
cat = P / "check" / f"khung-truoc-{time.strftime('%Y%m%d-%H%M%S')}"
shutil.copytree(M / "src", cat / "src", symlinks=False)
for f in ("render.mjs", "preview.mjs", "package.json"):
    if (M / f).exists(): shutil.copy2(M / f, cat / f)

doi = []
for goc in (MAU / "src").rglob("*"):
    r = goc.relative_to(MAU / "src")
    if r.parts[0] in DU_LIEU or r.parts[0] == "hoso.json" or goc.is_dir():   # hoso.json sinh lại từ hồ sơ bên dưới
        continue
    dich = M / "src" / r
    that = goc.resolve()                                   # thư viện hình (src/lib) là liên kết → chép bản thật
    if not dich.exists() or not filecmp.cmp(that, dich, shallow=False):
        dich.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(that, dich); doi.append(str(r))
goi_lai = False
for f in ("render.mjs", "preview.mjs", "package.json"):
    if (MAU / f).exists() and (not (M / f).exists() or not filecmp.cmp(MAU / f, M / f, shallow=False)):
        shutil.copy2(MAU / f, M / f); doi.append(f); goi_lai |= f == "package.json"
subprocess.run(["python3", "-I", str(DV / "khoi/hoso.py"), "lam-video", str(M / "src/hoso.json")], capture_output=True)
if goi_lai:
    env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
    subprocess.run(["npm", "install", "--no-fund", "--no-audit"], cwd=M, env=env, capture_output=True)
if not doi:
    shutil.rmtree(cat)
print(f"Cập nhật khung dựng: {len(doi)} tệp mới/đổi" + (f" ({', '.join(doi[:12])}{'…' if len(doi) > 12 else ''})" if doi else " — đã là bản mới nhất"))
if doi: print(f"Bản cũ cất ở {cat}")
