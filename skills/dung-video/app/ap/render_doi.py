#!/usr/bin/env python3
"""RENDER CHỈ PHẦN BỊ ĐỔI: render_doi.py <dự án>
So scenes.js / captions.js / project.js với lần render trước (check/app-render.json): lần đầu hoặc đổi phong cách → render tất cả;
góp ý chỉ đổi vài cảnh → chỉ render các cảnh đó (+ phu-de nếu phụ đề đổi, + the-cuoi/hai-ben nếu project đổi). Rồi render_preview.py."""
import hashlib, json, os, re, subprocess, sys
from pathlib import Path
P = Path(sys.argv[1]); src = P / "motion/src"; S = Path(__file__).resolve().parents[2] / "video-style-edit/scripts"
h = lambda t: hashlib.md5(t.encode()).hexdigest()
DU_LIEU = {"scenes.js", "captions.js", "project.js", "output.js", "placement.js", "mat.js", "speakers.js", "envelope.js", "highlight.js"}
s = (src / "scenes.js").read_text(encoding="utf-8")
i = s.index("export const SCENES = ") + len("export const SCENES = "); j = s.index("\n];", i) + 2
moi = {"canh": {c["id"]: h(json.dumps(c, sort_keys=True)) for c in json.loads(s[i:j])},
       "phu_de": h((src / "captions.js").read_text(encoding="utf-8")), "du_an": h((src / "project.js").read_text(encoding="utf-8")),
       "con_lai": h(s[j:]),
       # khung dựng = mọi tệp code trong motion/src trừ dữ liệu riêng của video (đổi thư viện hình / template → render lại tất cả)
       "giao_dien": h("".join(f.read_text(encoding="utf-8", errors="ignore") for f in sorted(src.rglob("*"))
                              if f.is_file() and f.relative_to(src).parts[0] not in DU_LIEU))}
snap = P / "check/app-render.json"; cu = json.loads(snap.read_text()) if snap.exists() else None
media = P / "davinci/media"
if not cu or cu["giao_dien"] != moi["giao_dien"]:
    ids = []                                          # render tất cả
else:
    ids = [k for k, v in moi["canh"].items() if cu["canh"].get(k) != v or not (media / f"{k}.mov").exists()]
    if cu["phu_de"] != moi["phu_de"]: ids.append("phu-de")
    if cu["du_an"] != moi["du_an"] or cu["con_lai"] != moi["con_lai"]: ids += ["the-cuoi", "hai-ben", "phu-de"]
    for k in set(cu["canh"]) - set(moi["canh"]):      # cảnh đã bỏ
        (media / f"{k}.mov").unlink(missing_ok=True)
    if not ids:
        ids = ["__khong__"]
env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
print("render:", "tất cả" if not ids else ("không cảnh nào đổi" if ids == ["__khong__"] else ", ".join(dict.fromkeys(ids))), flush=True)
if ids != ["__khong__"]:
    subprocess.run(["node", "render.mjs", *dict.fromkeys(ids)], cwd=P / "motion", env=env, check=True)
subprocess.run(["python3", "-I", str(S / "render_preview.py"), str(P)], env=env, check=True)
snap.write_text(json.dumps(moi))
