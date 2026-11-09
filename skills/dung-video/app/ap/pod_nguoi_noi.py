#!/usr/bin/env python3
"""AI ĐANG NÓI + SÓNG ÂM (khối 12): pod_nguoi_noi.py <dự án> <W> — speakers.py (pyannote nếu có) + envelope.py, rồi tóm tắt lượt
nói (W/nguoi-noi.txt: người 0/1, tỉ lệ, vài lượt đầu kèm lời) để Claude đặt tên/vai đúng ở bước kịch bản."""
import json, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import loi
from hl_chung import DV, ENV
P, W = Path(sys.argv[1]), Path(sys.argv[2]); POD = DV / "podcast-style-edit/scripts"
PY = subprocess.run(["zsh", str(POD / "py_setup.sh")], capture_output=True, text=True, env=ENV).stdout.strip().splitlines()[-1]
subprocess.run([PY, str(POD / "speakers.py"), str(P)], env=ENV, check=True)
subprocess.run([PY, str(POD / "envelope.py"), str(P)], env=ENV, check=True)
s = (P / "motion/src/speakers.js").read_text(encoding="utf-8")
d = json.loads(re.sub(r"(\w+):", r'"\1":', s[s.index("{"): s.rindex("}") + 1]).replace('""', '"'))
L = loi.doc_srt(P / "check/goc/transcript.srt"); tong = {}
for t in d["turns"]: tong[t["spk"]] = tong.get(t["spk"], 0) + t["end"] - t["start"]
out = [f"Số người nói (máy đoán): {d['count']}"] + [f"- người {k}: {v / 60:.1f} phút" for k, v in sorted(tong.items())] + ["", "Vài lượt đầu:"]
for t in d["turns"][:12]:
    cau = " ".join(x[2] for x in L if t["start"] - 0.5 <= x[0] < t["end"])[:160]
    out.append(f"[{t['start']:.0f}–{t['end']:.0f}s] người {t['spk']}: {cau}")
(W / "nguoi-noi.txt").write_text("\n".join(out) + "\n", encoding="utf-8"); print("\n".join(out))
