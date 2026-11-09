#!/usr/bin/env python3
"""SỔ DANH MỤC (khối 00 mục 7): so_danh_muc.py <dự án> <W> <trạng thái>
Thêm/cập nhật một dòng của tập này trong dang-lam/danh-muc.md (nơi duy nhất ghi trạng thái từng tài nguyên).
Dòng nhận ra bằng `<tên tập>` trong cột Tài nguyên; có rồi thì chỉ đổi cột Trạng thái."""
import json, re, sys, time
from pathlib import Path
P, W, tt = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
SO = Path(__file__).resolve().parents[4] / "dang-lam/danh-muc.md"
tap = P.parent.name
if tap.startswith("tap-thu-") or P.name.startswith("thu-"):   # việc THỬ của Claude không ghi vào sổ thật (lỗi 09/11/2026)
    print("việc thử — không ghi sổ danh mục"); sys.exit(0)
loc = json.loads((W / "loc-va-cat.json").read_text())["loc"] if (W / "loc-va-cat.json").exists() else {"ket_luan": "✂️ Trích ngắn từ gốc"}
dm = loc.get("diem", {}); diem = sum(dm.values()) if dm else "—"
lr = " · ⚠️ đã cảnh báo lằn ranh" if loc.get("lan_ranh") else ""
d = SO.read_text(encoding="utf-8").split("\n")
moc = f"`~/Movies/{tap}`"
k = next((n for n, x in enumerate(d) if moc in x and x.startswith("|")), None)
if k is not None:
    o = d[k].split("|"); o[-2] = f" {tt} "; d[k] = "|".join(o)
else:
    dong = (f"| {time.strftime('%Y-%m-%d')} | Video {tap[4:]} (app dựng, {moc}) | {loc.get('ket_luan', '')}{lr} | {diem} | "
            f"{loc.get('nhanh', '')} | {loc.get('de_xuat', '')} | — | {tt} |")
    cuoi = max(n for n, x in enumerate(d) if x.startswith("| 20"))
    d.insert(cuoi + 1, dong)
SO.write_text("\n".join(d), encoding="utf-8"); print("sổ danh mục:", tap, "→", tt)
