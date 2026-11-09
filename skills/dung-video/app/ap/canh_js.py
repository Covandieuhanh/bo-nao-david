"""Đọc motion/src/scenes.js bằng node (đúng như Remotion đọc), không bắt AI viết dạng JSON.
AI làm theo skill viết scenes.js bằng cú pháp JavaScript tự do (khoá không ngoặc, dấu phẩy cuối, chú thích) — lỗi 09/11/2026 khi máy
đọc file như JSON. doc(P) → dict mọi export (SCENES, CHAPTERS, SIDES…)."""
import json, os, subprocess
from pathlib import Path


def doc(P):
    f = (Path(P) / "motion/src/scenes.js").resolve()
    js = f"const m = await import({json.dumps(f.as_uri())}); console.log(JSON.stringify(Object.fromEntries(Object.entries(m))));"
    r = subprocess.run(["node", "--no-warnings", "--input-type=module", "-e", js], capture_output=True, text=True,
                       env=dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", "")))
    if r.returncode:
        raise SystemExit("Không đọc được scenes.js: " + r.stderr[-1500:])
    return json.loads(r.stdout)


def canh(P):
    return doc(P)["SCENES"]
