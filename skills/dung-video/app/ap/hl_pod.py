#!/usr/bin/env python3
"""HIGHLIGHT TỪ PODCAST ĐỒ HOẠ (skill 7B): hl_pod.py <dự án highlight> <W> dung|render
dung   : mỗi clip — new_podcast.sh cat/<mã>.mp4 hl-<tập>-<mã> doc cat-thua → clip-<mã>/ (chỉ tiếng), transcribe, captions, người nói +
         sóng âm, hl_apply.py (tông, nhạc kho kênh, chữ chính, thẻ cuối), STAGE + theme/fonts lấy từ bản gốc; bản lời từng clip cho Claude.
render : render_doi.py từng clip (podcast: sân khấu nền → podcast_base → render_preview) + tờ kiểm tra."""
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
import json, re, shutil, subprocess, sys
from pathlib import Path
import loi
from hl_chung import HL, S, DV, ENV, pa, tap
H, W, viec = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]; kiem = "--kiem" in sys.argv
POD = DV / "podcast-style-edit/scripts"; APP = DV / "app"
goc = Path((H / "check/goc/du-an-goc.txt").read_text().strip()) if (H / "check/goc/du-an-goc.txt").exists() else None
ids = [o["id"] for o in pa(H)["options"]]
if viec == "dung":
    PY = subprocess.run(["zsh", str(POD / "py_setup.sh")], capture_output=True, text=True, env=ENV).stdout.strip().splitlines()[-1]
    for ma in ids:
        E = H / f"clip-{ma}"
        if not (E / "davinci/media/audio.wav").exists():
            if E.exists(): shutil.move(str(E), str(Path.home() / ".Trash" / f"{H.parent.name}-clip-{ma}-do-dang"))
            subprocess.run(["zsh", str(POD / "new_podcast.sh"), str(H / f"cat/{ma}.mp4"), f"hl-{tap(H)}-{ma}", "doc", "cat-thua"], env=ENV, check=True)
        subprocess.run(["zsh", str(POD / "transcribe.sh"), str(E)], env=ENV, check=True)
        subprocess.run(["python3", "-I", str(S / "captions.py"), str(E)], env=ENV, check=True)
        subprocess.run([PY, str(POD / "speakers.py"), str(E)], env=ENV, check=True)
        subprocess.run([PY, str(POD / "envelope.py"), str(E)], env=ENV, check=True)
        subprocess.run(["python3", "-I", str(HL / "hl_apply.py"), str(H), ma, str(E)], env=ENV, check=True)
        src = E / "motion/src"
        if goc and (goc / "motion/src/scenes.js").exists():   # sân khấu như bản gốc: tên tập, người nói, show
            g = (goc / "motion/src/scenes.js").read_text(encoding="utf-8"); m = re.search(r"export const STAGE = .*?;\n", g, re.S)
            if m:
                s = (src / "scenes.js").read_text(encoding="utf-8")
                (src / "scenes.js").write_text(re.sub(r"export const STAGE = .*?;\n", lambda _: m.group(0), s, count=1, flags=re.S), encoding="utf-8")
            for f in ("theme.js", "fonts.js"):
                if (goc / "motion/src" / f).exists(): shutil.copy2(goc / "motion/src" / f, src / f)
        loi.ban_loi(E / "check/goc/words.srt", E / "check/goc/transcript.srt", W / f"ban-loi-{ma}.txt")
        print(f"clip {ma}: khung podcast dọc xong → {E}")
    (W / "ban-loi-cac-clip.txt").write_text("\n\n".join(f"== clip {ma}\n" + (W / f"ban-loi-{ma}.txt").read_text(encoding="utf-8") for ma in ids), encoding="utf-8")
elif viec == "render":
    for ma in ids:
        E = H / f"clip-{ma}"
        subprocess.run(["python3", "-I", str(APP / "ap/render_doi.py"), str(E)], env=ENV, check=True)
        subprocess.run(["python3", "-I", str(APP / "ap/to_kiem_tra.py"), str(E)], env=ENV, check=True)
