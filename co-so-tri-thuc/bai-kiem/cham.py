#!/usr/bin/env python3
"""Chấm bài kiểm toàn bộ não (co-so-tri-thuc/bai-kiem/README.md).
  python3 -I cham.py <bai-lam.json>   — bài làm: [{"id": "c01", "chon": "A", "vi": "<lý do, nêu file đã dựa vào>"}, …]
  python3 -I cham.py --mau            — in bài làm đúng (đáp án) để thử máy chấm
Một câu ĐẠT khi "chon" trùng đáp án. Đạt khi đúng ít nhất (số câu trừ 1). Câu sai in ra kèm file là nhà của luật để sửa."""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DE = {c['id']: c for c in json.loads((HERE / 'de.json').read_text(encoding='utf-8'))}
DA = json.loads((HERE / 'dap-an.json').read_text(encoding='utf-8'))
NGUONG = len(DE) - 1

if len(sys.argv) < 2:
    print(__doc__); sys.exit(2)
if sys.argv[1] == '--mau':
    print(json.dumps([{'id': k, 'chon': v['dung'], 'vi': v['nha']} for k, v in DA.items()], ensure_ascii=False, indent=1)); sys.exit(0)

bai = {b['id']: b for b in json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))}
dung = 0
for k, v in DA.items():
    b = bai.get(k, {}); chon = str(b.get('chon', '')).strip().upper()[:1]
    if chon == v['dung']:
        dung += 1; print(f"✓ {k}")
    else:
        print(f"✗ {k} · chọn {chon or '(trống)'}, đúng {v['dung']} · tình huống: {DE[k]['tinh_huong']}")
        print(f"    lý do người làm: {b.get('vi', '(không ghi)')}")
        print(f"    nhà của luật cần đọc lại / viết rõ hơn: {v['nha']}")
print(f"\nĐúng {dung}/{len(DA)} → " + ("ĐẠT: người đọc lạnh làm đúng." if dung >= NGUONG else f"CHƯA ĐẠT (cần ít nhất {NGUONG}): sửa nhà của các câu sai cho rõ hơn, rồi cho một AI chưa đọc gì làm lại."))
sys.exit(0 if dung >= NGUONG else 1)
