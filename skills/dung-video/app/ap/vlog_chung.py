"""Ghép vlog: danh sách clip của dự án (clips.tsv do new_montage.sh ghi)."""
from pathlib import Path


def ds_clip(P):
    out = []
    f = Path(P) / "clips.tsv"
    for l in f.read_text(encoding="utf-8").splitlines():
        x = l.split("\t")
        if x and x[0].startswith("c") and x[0][1:].isdigit():
            out.append(x[0])
    return out or sorted(p.name for p in (Path(P) / "check").glob("c[0-9]*"))
