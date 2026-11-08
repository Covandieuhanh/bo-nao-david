#!/usr/bin/env python3
"""CẬP NHẬT KHUNG DỰNG cho một dự án đang làm: cap_nhat_khung.py <dự án> [--xem]

Lúc tạo dự án, skill CHÉP khung dựng Remotion + thư viện hình vào <dự án>/motion (để dự án cũ render lại vẫn ra như cũ).
Sửa thư viện hình / template sau đó thì dự án đang làm không tự theo — chạy lệnh này: chép lại khung dựng mới nhất,
GIỮ NGUYÊN dữ liệu riêng của video (DU_LIEU dưới đây), ghi lại hồ sơ tham số. Bản cũ cất ở check/khung-truoc-<giờ>/.
Sau đó render lại (render_doi.py thấy khung đổi → render tất cả).  --xem: chỉ liệt kê tệp khác, không chép (ra_soat.py dùng).
"""
import filecmp, os, shutil, subprocess, sys, time
from pathlib import Path

DV = Path(__file__).resolve().parents[2]
MAU = DV / "video-style-edit/assets/remotion-template"
# Dữ liệu riêng của từng video (kịch bản, phụ đề, thông số, vị trí mặt, khung xuất, người nói…) — không bao giờ ghi đè.
DU_LIEU = {"scenes.js", "captions.js", "project.js", "output.js", "placement.js", "mat.js", "speakers.js", "envelope.js", "highlight.js",
           "hoso.json"}   # hoso.json sinh lại từ hồ sơ tham số
NGOAI = ("render.mjs", "preview.mjs", "package.json")


def khac_biet(P):
    """[(tệp mẫu, tệp dự án, tên hiển thị)] của khung dựng khác bản mới nhất của skill."""
    M = Path(P) / "motion"; ds = []
    for goc in (MAU / "src").rglob("*"):
        r = goc.relative_to(MAU / "src")
        if r.parts[0] in DU_LIEU or goc.is_dir():
            continue
        that, dich = goc.resolve(), M / "src" / r          # thư viện hình (src/lib) là liên kết → so / chép bản thật
        if not dich.exists() or not filecmp.cmp(that, dich, shallow=False):
            ds.append((that, dich, str(r)))
    for f in NGOAI:
        if (MAU / f).exists() and (not (M / f).exists() or not filecmp.cmp(MAU / f, M / f, shallow=False)):
            ds.append((MAU / f, M / f, f))
    return ds


def cap_nhat(P):
    M = Path(P) / "motion"; ds = khac_biet(P)
    if ds:
        cat = Path(P) / "check" / f"khung-truoc-{time.strftime('%Y%m%d-%H%M%S')}"
        shutil.copytree(M / "src", cat / "src")
        for f in NGOAI:
            if (M / f).exists(): shutil.copy2(M / f, cat / f)
        for goc, dich, _ in ds:
            dich.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(goc, dich)
    subprocess.run(["python3", "-I", str(DV / "khoi/hoso.py"), "lam-video", str(M / "src/hoso.json")], capture_output=True)
    if any(t == "package.json" for *_, t in ds):
        env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
        subprocess.run(["npm", "install", "--no-fund", "--no-audit"], cwd=M, env=env, capture_output=True)
    ten = [t for *_, t in ds]
    print(f"Cập nhật khung dựng: {len(ten)} tệp mới/đổi" + (f" ({', '.join(ten[:12])}{'…' if len(ten) > 12 else ''})" if ten else " — đã là bản mới nhất"))
    if ds: print(f"Bản cũ cất ở {cat}")


if __name__ == "__main__":
    P = Path(sys.argv[1])
    if not (P / "motion/src").is_dir():
        raise SystemExit("Dự án chưa có khung dựng (chưa qua bước Tạo dự án).")
    if "--xem" in sys.argv:
        print("\n".join(t for *_, t in khac_biet(P)))
    else:
        cap_nhat(P)
