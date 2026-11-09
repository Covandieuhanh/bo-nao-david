#!/usr/bin/env python3
"""PHÁT HÀNH VLOG: ap_phat_hanh_vlog.py <dự án> <phat-hanh-vlog.json> — thumbnail từ CHÍNH clip của vlog (cN@giây, khối 14),
chương YouTube (chapters.py lấy nhãn địa điểm), phat-hanh.md, so-lieu.md."""
import json, re, subprocess, sys
from pathlib import Path
from hl_chung import S, ENV, DV
P = Path(sys.argv[1]); kh = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")); ph = P / "phat-hanh"; ph.mkdir(exist_ok=True)
tb = []
for i, t in enumerate(kh.get("thumbnail", []), 1):
    r = subprocess.run(["zsh", str(S / "thumbnail.sh"), str(P), f"{t['clip']}@{t['giay']}", t["dong1"], t["dong2"], str(i)], env=ENV, capture_output=True, text=True)
    tb.append(f"- `thumb-{i}.jpg`: {t['clip']} giây {t['giay']}, chữ \"{t['dong1']} / {t['dong2']}\"" + ("" if r.returncode == 0 else " (⚠ lỗi tạo ảnh)"))
ch = subprocess.run(["python3", "-I", str(S / "chapters.py"), str(P)], env=ENV, capture_output=True, text=True).stdout.strip()
md = [f"# Phát hành — {P.name} — GỢI Ý để David chọn", "", "## 3 tiêu đề"] + [f"{i}. {t}" for i, t in enumerate(kh["tieu_de"], 1)]
md += ["", "## Mô tả", kh["mo_ta"], ""] + (["## Chương YouTube", ch, ""] if ch else []) + ["## Bình luận ghim", kh["binh_luan_ghim"], ""]
if kh.get("khung_bia"): md += ["## Khung bìa đề xuất", kh["khung_bia"], ""]
if tb: md += ["## Thumbnail gợi ý (để David chọn)"] + tb
(ph / "phat-hanh.md").write_text("\n".join(md), encoding="utf-8")
if not (P / "so-lieu.md").exists():
    (P / "so-lieu.md").write_text((DV / "khoi/16-so-lieu/mau-so-lieu.md").read_text(encoding="utf-8").replace("<tên video>", kh["tieu_de"][0]), encoding="utf-8")
print("\n".join(md))
