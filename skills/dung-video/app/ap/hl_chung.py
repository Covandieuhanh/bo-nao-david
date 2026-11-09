"""Dùng chung cho công thức HIGHLIGHT: đường dẫn, đọc phuong-an, danh sách clip."""
import json, os
from pathlib import Path
DV = Path(__file__).resolve().parents[2]
HL = DV / "cat-highlight-video/scripts"; S = DV / "video-style-edit/scripts"
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))


def pa(H):
    return json.loads((Path(H) / "phuong-an.json").read_text(encoding="utf-8"))


def clips(H):
    """[(mã, thư mục dựng clip)] theo phuong-an.json — clip-<mã> nằm cạnh 3-highlight (new_montage.sh hl-<tập>-<mã>)."""
    return [(o["id"], Path(H) / f"clip-{o['id']}") for o in pa(H)["options"]]


def tap(H):
    return Path(H).parent.name[4:]          # ~/Movies/tap-<tập>/3-highlight → <tập>
