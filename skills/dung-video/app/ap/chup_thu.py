"""Chụp đủ từng cảnh + phụ đề tại khung đầy nhất, trước render thật."""
import json, os, re, subprocess, sys
from pathlib import Path
P, W = Path(sys.argv[1]), Path(sys.argv[2]); DV = Path(__file__).resolve().parents[2]
S = DV / "video-style-edit/scripts"; env = dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:"+os.environ.get("PATH", ""))
def run(*args, **kw): subprocess.run(args, env=env, check=True, **kw)
s = (P/"motion/src/scenes.js").read_text(); i=s.index("export const SCENES = ")+len("export const SCENES = "); j=s.index("\n];",i)+2
C=json.loads(s[i:j]); moc=[]
for c in C:
    t=max(c["start"], c["end"]-0.25)
    moc += [f"{c['id']}@{t:.2f}", f"phu-de@{t:.2f}"]
# Loại ảnh preview cũ: cảnh bị xoá không được lẫn vào tờ duyệt mới.
for f in (P/"check/motion").glob("*@*.png"): f.unlink()
run("python3", str(S/"safe_guide.py"), str(P))
if (P/"motion/src/output.js").exists() and re.search(r"export default\s*\{[^;]*pillar", (P/"motion/src/output.js").read_text(), re.S):
    run("node", "render.mjs", "hai-ben", cwd=P/"motion")
    run("python3", "-I", str(S/"pillar_base.py"), str(P))
if not moc: raise SystemExit("Không có cảnh để kiểm thẩm mỹ")
run("node", "preview.mjs", *moc, cwd=P/"motion")
run("zsh", str(S/"composite_stills.sh"), str(P))
(W/"chup-thu.md").write_text(f"# Chụp thử trước render\n\n{len(C)} cảnh, chụp cuối mỗi cảnh kèm phụ đề.\n")
