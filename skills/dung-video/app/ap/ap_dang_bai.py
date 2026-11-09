#!/usr/bin/env python3
"""KẾ HOẠCH ĐĂNG HIGHLIGHT: ap_dang_bai.py <dự án highlight> <dang-bai.json> → dang-bai.md (lịch, kênh, mô tả, bình luận ghim, khung
bìa 0,3 s) + so-lieu.md từ mẫu (khối 16)."""
import json, sys
from pathlib import Path
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))   # python -I không tự thấy file cùng thư mục
from hl_chung import pa, DV
H = Path(sys.argv[1]); kh = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
tit = {o["id"]: o.get("tit", "") for o in pa(H)["options"]}
d = [f"# Kế hoạch đăng highlight — {H.parent.name} — GỢI Ý để David chọn", ""]
for c in kh["clips"]:
    d += [f"## Clip {c['id']} — «{tit.get(c['id'], '')}»", f"- **Lịch:** {c['lich']} · **Kênh:** {', '.join(c['kenh'])} · **Dẫn dắt:** {c.get('dan_dat', '')}",
          "- **Khung bìa:** giây 0,3 (thẻ tít + mặt người nói)", "", "**Mô tả**", c["mo_ta"], "", "**Bình luận ghim**", c["binh_luan_ghim"], ""]
(H / "dang-bai.md").write_text("\n".join(d), encoding="utf-8")
sl = H / "so-lieu.md"
if not sl.exists():
    sl.write_text((DV / "khoi/16-so-lieu/mau-so-lieu.md").read_text(encoding="utf-8").replace("<tên video>", f"Highlight {H.parent.name}"), encoding="utf-8")
print("\n".join(d))
