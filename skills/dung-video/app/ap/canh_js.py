"""Đọc motion/src/scenes.js bằng node (đúng như Remotion đọc), không bắt AI viết dạng JSON.
AI làm theo skill viết scenes.js bằng cú pháp JavaScript tự do (khoá không ngoặc, dấu phẩy cuối, chú thích) — lỗi 09/11/2026 khi máy
đọc file như JSON. doc(P) → dict mọi export (SCENES, CHAPTERS, SIDES…)."""
import json, os, subprocess
from pathlib import Path


def doc(P, ten="scenes.js"):
    f = (Path(P) / "motion/src" / ten).resolve()
    js = f"const m = await import({json.dumps(f.as_uri())}); console.log(JSON.stringify(Object.fromEntries(Object.entries(m))));"
    r = subprocess.run(["node", "--no-warnings", "--input-type=module", "-e", js], capture_output=True, text=True,
                       env=dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", "")))
    if r.returncode:
        raise SystemExit("Không đọc được scenes.js: " + r.stderr[-1500:])
    return json.loads(r.stdout)


def canh(P):
    return doc(P)["SCENES"]


CHU = {"text", "tieu_de", "label", "quote", "ten", "title", "eyebrow", "name", "subtitle", "lines"}   # khoá chứa chữ trên màn hình


def chu_tren_man(o, out=None):
    """Mọi chữ trên màn hình trong props (lồng nhau) — để soát nguyên văn. Cảnh tự vẽ đặt chữ ở các khoá này."""
    out = [] if out is None else out
    if isinstance(o, list):
        for x in o: chu_tren_man(x, out)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in CHU and isinstance(v, str): out.append(v)
            elif k in CHU and isinstance(v, list) and all(isinstance(x, str) for x in v): out.extend(v)
            elif k == "nhan" and isinstance(v, str): out.append(v)
            else: chu_tren_man(v, out)
    return out
