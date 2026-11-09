#!/usr/bin/env python3
"""SỬA MỐC CẮT THEO ĐỘ LỚN TIẾNG: hl_moc.py <dự án highlight>
Chạy loud_check.py của skill (một nguồn luật), đọc mốc đề xuất từng câu rồi áp vào phuong-an.json — việc trước đây Claude làm tay.
Mốc lệch > 1 s hoặc "nói liền" → giữ mốc Whisper (an toàn hơn đoán)."""
import json, re, subprocess, sys
from pathlib import Path
from hl_chung import HL, ENV
H = Path(sys.argv[1]); f = H / "phuong-an.json"; pa = json.loads(f.read_text(encoding="utf-8"))
out = subprocess.run(["python3", "-I", str(HL / "loud_check.py"), str(H)], capture_output=True, text=True, env=ENV).stdout
print(out[-4000:])
de = {}; cur = None; k = 0
for l in out.splitlines():
    m = re.match(r"=== Phương án (\S+)", l)
    if m: cur = m.group(1); k = 0; continue
    if re.match(r"\d+\. ", l): k += 1; continue
    m = re.match(r"\s+(start|end)\s+([\d.]+) →\s+(\S+)(\s+⚠ lệch > 1 s)?", l)
    if m and cur and not m.group(4) and re.match(r"[\d.]+$", m.group(3)):
        de[(cur, k, m.group(1))] = float(m.group(3))
n = 0
for o in pa["options"]:
    for i, p in enumerate(o["pieces"], 1):
        for kk in ("start", "end"):
            v = de.get((o["id"], i, kk))
            if v is not None and abs(v - p[kk]) > 0.01:
                p[kk] = v; n += 1
f.write_text(json.dumps(pa, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Đã áp {n} mốc theo độ lớn tiếng")
