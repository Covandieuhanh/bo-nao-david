"""Phần dùng chung của các phép đo (không phải luật — chay_kiem chỉ chạy file kiem_*.py).
loai(P): 'ghep' (khuôn ghép clip: edl.js — highlight người nói, vlog) | 'mot' (1 video / podcast: scenes.js).
loi(P): [(giây đầu, giây cuối, chữ)] trên DÒNG THỜI GIAN BẢN CUỐI — mot: check/goc/words.srt · ghep: SUBS của edl.js."""
import json, os, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ap"))
import canh_js, loi as _loi  # noqa: E402

ENV = dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", ""))
HS = json.load(open(Path(__file__).resolve().parents[2] / "ho-so/chung.json", encoding="utf-8"))


def loai(P):
    return "ghep" if (Path(P) / "motion/src/edl.js").exists() else "mot" if (Path(P) / "motion/src/scenes.js").exists() else None


def edl(P):
    return canh_js.doc(P, "edl.js")


def loi(P):
    if loai(P) == "ghep":
        return [(s["start"], s["end"], s["text"]) for s in edl(P).get("SUBS", [])]
    f = Path(P) / "check/goc/words.srt"
    return [(a, b, t) for a, b, t in _loi.doc_srt(f)] if f.exists() else []


def final(P):
    f = Path(P) / "video-final.mp4"
    return f if f.exists() else None


def rms_cua_so(f, buoc=0.4):
    """Mức RMS (dB) mỗi cửa sổ `buoc` giây của cả file — một lượt ffmpeg."""
    n = int(48000 * buoc)
    r = subprocess.run(["ffmpeg", "-nostats", "-i", str(f), "-vn", "-ac", "1", "-ar", "48000", "-af",
                        f"asetnsamples={n},astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-",
                        "-f", "null", "-"], capture_output=True, text=True, env=ENV)
    ra = []
    for m in re.finditer(r"RMS_level=(-?[\d.]+|-inf)", r.stdout + r.stderr):
        ra.append(-120.0 if m.group(1) == "-inf" else float(m.group(1)))
    return ra
