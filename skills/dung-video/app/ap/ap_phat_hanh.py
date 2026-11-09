#!/usr/bin/env python3
"""ÁP GÓI PHÁT HÀNH: ap_phat_hanh.py <dự án> <phat-hanh.json> [--kiem]
Claude viết chữ (tiêu đề, mô tả, bình luận ghim) và TRÍCH câu cho khung bìa / thumbnail / teaser; script tìm mốc rồi:
phat-hanh/phat-hanh.md · thumbnail.sh (chỉ video ngang) · teaser.py + chapters.py (video dài YouTube) · so-lieu.md từ mẫu."""
import json, os, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import loi  # noqa: E402

DV = Path(__file__).resolve().parents[2]; S = DV / "video-style-edit/scripts"
ENV = dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", ""))


def mm(s):
    return f"{int(s // 60)}:{int(s % 60):02d}"


def du_an(P):
    s = (Path(P) / "motion/src/project.js").read_text(encoding="utf-8")
    g = lambda k: float(re.search(rf"{k}: *([\d.]+)", s).group(1))
    return g("width"), g("height"), g("duration")


def main():
    P, kp = sys.argv[1], sys.argv[2]; kiem = "--kiem" in sys.argv
    kh = json.loads(Path(kp).read_text(encoding="utf-8")); T = loi.tu(Path(P) / "check/goc/words.srt"); loi_ds = []
    w, h, dur = du_an(P); ngang = w > h
    pod = "podcast: true" in (Path(P) / "motion/src/project.js").read_text(encoding="utf-8")

    def m(q, sau=0):
        r = loi.tim(q, T, sau=sau)
        if not r: loi_ds.append(f"không tìm thấy câu trích «{q}»")
        return r

    bia = m(kh["khung_bia_trich"]) if kh.get("khung_bia_trich") else None
    thumbs = [((m(t["trich"]) if not pod else (0, 0, 1)), t) for t in kh.get("thumbnail", [])] if ngang else []
    teaser = []
    for t in kh.get("teaser", []) if dur > 180 else []:
        a = m(t["trich_dau"]); b = m(t["trich_cuoi"], sau=a[0] if a else 0) if a else None
        if a and b: teaser.append((a[0] - 0.1, b[1] + 0.2))
    if teaser and not 12 <= sum(b - a for a, b in teaser) <= 35:
        loi_ds.append(f"teaser dài {sum(b - a for a, b in teaser):.0f} s — cần 15–25 s (2–3 câu đắt, trọn câu)")
    for x in loi_ds: print("✗", x)
    if loi_ds: sys.exit(1)
    if kiem: return
    ph = Path(P) / "phat-hanh"; ph.mkdir(exist_ok=True)
    tb = []
    for i, (r, t) in enumerate(thumbs, 1):
        env = dict(ENV, **({"THUMB_NUM": str(t["so_lon"])} if t.get("so_lon") else {}))
        nguon = f"{r[0] + 0.3:.1f}"
        if pod:   # podcast chỉ có tiếng: bìa KHÔNG MẶT = nền hoạ tiết + hình theo ý + "DAVID · PODCAST" (khối 14)
            env.update(THUMB_HINH=t.get("hinh") or "danh-sach", THUMB_TAG="PODCAST"); nguon = "-"
        sub = subprocess.run(["zsh", str(S / "thumbnail.sh"), P, nguon, t["dong1"], t["dong2"], str(i)], env=env,
                             capture_output=True, text=True)
        tb.append(f"- `thumb-{i}.jpg`: giây {r[0] + 0.3:.0f}, chữ \"{t['dong1']} / {t['dong2']}\"" + ("" if sub.returncode == 0 else " (⚠ lỗi tạo ảnh)"))
    if teaser:
        subprocess.run(["python3", "-I", str(S / "teaser.py"), P] + [f"{a:.2f}-{b:.2f}" for a, b in teaser], env=ENV)
    chuong = ""
    if dur > 180:
        r = subprocess.run(["python3", "-I", str(S / "chapters.py"), P], env=ENV, capture_output=True, text=True)
        chuong = r.stdout.strip()
    md = [f"# Phát hành — {Path(P).parent.name} ({mm(dur)}) — GỢI Ý để David chọn", "", "## 3 tiêu đề"]
    md += [f"{i}. {t}" for i, t in enumerate(kh["tieu_de"], 1)]
    nguon = Path(P) / "nguon-anh.txt"
    md += ["", "## Mô tả", kh["mo_ta"] + ("\n\n" + nguon.read_text(encoding="utf-8").strip() if nguon.exists() else ""), ""]
    if chuong: md += ["## Chương YouTube", chuong, ""]
    md += ["## Bình luận ghim", kh["binh_luan_ghim"], ""]
    if bia: md += ["## Khung bìa đề xuất", f"Giây {mm(bia[0] + 0.3)} — «{kh['khung_bia_trich']}»", ""]
    if tb: md += ["## Thumbnail gợi ý (để David chọn)"] + tb + [""]
    (ph / "phat-hanh.md").write_text("\n".join(md), encoding="utf-8")
    sl = Path(P) / "so-lieu.md"
    if not sl.exists():
        mau = (DV / "khoi/16-so-lieu/mau-so-lieu.md").read_text(encoding="utf-8")
        sl.write_text(mau.replace("<tên video>", kh["tieu_de"][0]), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
