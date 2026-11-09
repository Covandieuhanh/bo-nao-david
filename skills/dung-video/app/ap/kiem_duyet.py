#!/usr/bin/env python3
"""Soát kết quả Claude duyệt hình: kiem_duyet.py <canh|lop-phu|ghep> <dự án> <W> — có kế hoạch sửa thì kế hoạch đó phải qua đúng
lệnh kiểm của bước gốc (ap_canh / ap_lop_phu / ap_vlog --kiem)."""
import json, subprocess, sys
from pathlib import Path
loai, P, W = sys.argv[1], sys.argv[2], Path(sys.argv[3]); APP = Path(__file__).resolve().parents[1]
kq = json.loads((W / "duyet-hinh.json").read_text(encoding="utf-8"))
if kq.get("dat") or not kq.get("ke_hoach"):
    print("đạt" if kq.get("dat") else "✗ chưa đạt nhưng thiếu `ke_hoach` sửa — trả kế hoạch sửa đầy đủ"); sys.exit(0 if kq.get("dat") else 1)
tam = W / "duyet-hinh-ke-hoach.tmp.json"; tam.write_text(json.dumps(kq["ke_hoach"], ensure_ascii=False), encoding="utf-8")
lenh = {"canh": ["ap_canh.py", P, str(tam), str(W)], "lop-phu": ["ap_lop_phu.py", P, str(tam)], "ghep": ["ap_vlog.py", P, str(tam)]}[loai]
r = subprocess.run(["python3", "-I", str(APP / "ap" / lenh[0]), *lenh[1:], "--kiem"], capture_output=True, text=True)
print(r.stdout[-3000:]); tam.unlink(missing_ok=True); sys.exit(r.returncode)
