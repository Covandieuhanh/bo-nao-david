#!/usr/bin/env python3
"""CHỤP THỬ PODCAST trước render (skill podcast bước 7, ghi nhớ "podcast phủ hình 30%": David chốt ảnh rồi mới render):
pod_chup_thu.py <dự án> <W> — mỗi cảnh ở lúc đầy nhất + sân khấu (nen@) ở từng ý đang bàn → pod_stills.sh → check/stills.jpg;
đo tỉ lệ phủ hình và khoảng trống dài nhất → W/chup-thu.md."""
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import json, re, subprocess, sys
from pathlib import Path
from hl_chung import DV, ENV
P, W = Path(sys.argv[1]), Path(sys.argv[2]); src = P / "motion/src"
s = (src / "scenes.js").read_text(encoding="utf-8"); i = s.index("export const SCENES = ") + 22; j = s.index("\n];", i) + 2
C = json.loads(s[i:j]); dur = float(re.search(r"duration: *([\d.]+)", (src / "project.js").read_text()).group(1))
tp = [float(x) for x in re.findall(r"\{at: ([\d.]+), text:", s[s.find("export const TOPICS"):])] if "export const TOPICS" in s else []
def day(c):   # lúc "đầy nhất": sau mốc phần tử cuối hiện ~0,8 s
    ats = [float(v) for v in re.findall(r'"(?:at|quoteAt|doneAt)": ([\d.]+)', json.dumps(c["props"]))]
    return min(c["end"] - 0.2, (max(ats) + 0.8) if ats else (c["start"] + c["end"]) / 2)
moc = [f"{c['id']}@{day(c):.1f}" for c in C] + [f"nen@{min(dur - 1, t + 1.5):.1f}" for t in tp[:12]]
subprocess.run(["zsh", str(DV / "podcast-style-edit/scripts/pod_stills.sh"), str(P), *moc], env=ENV, check=True)
phu = sorted((c["start"], c["end"]) for c in C if c["type"] != "cta"); cov = 0; last = 0; gap = (0, 0)
for a, b in phu:
    if a - last > gap[1] - gap[0]: gap = (last, a)
    cov += max(0, b - max(a, last)); last = max(last, b)
if dur - last > gap[1] - gap[0]: gap = (last, dur)
mm = lambda t: f"{int(t // 60)}:{int(t % 60):02d}"
md = [f"# Chụp thử trước render — {P.parent.name}", "", f"- {len(C)} cảnh · phủ hình **{cov / dur * 100:.0f}%** thời lượng (chuẩn ~30%, cân theo nội dung)",
      f"- Khoảng trống dài nhất: {mm(gap[0])}–{mm(gap[1])} ({gap[1] - gap[0]:.0f} s)", f"- Ảnh: `check/stills.jpg` ({len(moc)} mốc)"]
(W / "chup-thu.md").write_text("\n".join(md) + "\n", encoding="utf-8"); print("\n".join(md))
