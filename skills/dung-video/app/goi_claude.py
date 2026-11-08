#!/usr/bin/env python3
"""GỌI CLAUDE cho một bước `claude`: goi_claude.py <buoc/x.json> '<biến JSON>' [góp ý]

Gửi đúng phần cần: lời nhắc của bước (loi-nhac/*.md) + các file khai trong `doc`. Claude không có công cụ, không đọc skill,
chỉ trả về MỘT JSON đúng khuôn (khuon/*.json). Lệnh `kiem` của bước soát JSON; sai → gửi lại một lần kèm lỗi.
Dùng chính Claude Code trên máy (`claude -p`), tính vào gói của David. Ghi token mỗi lần gọi vào {W}/token.jsonl.

Trong lời nhắc dùng được: {{ho_so:khoá.con}} (giá trị hồ sơ tham số của loại video) · {{bieu_tuong}} (mọi biểu tượng đang có
trong thư viện hình) · {{file:đường/dẫn}} (chèn file trong skills/dung-video). Thêm biểu tượng hay tuyến nhạc → Claude tự thấy.
"""
import glob, json, os, re, shutil, subprocess, sys, time
from pathlib import Path

APP = Path(__file__).resolve().parent
DV = APP.parent
sys.path.insert(0, str(DV / "khoi")); sys.path.insert(0, str(APP / "ap"))
import hoso, loi  # noqa: E402

MO_HINH = {"nhe": "haiku", "vua": "sonnet", "manh": "opus"}


def tim_claude():
    for c in [os.environ.get("CLAUDE_BIN"), shutil.which("claude"), os.path.expanduser("~/.local/bin/claude"),
              os.path.expanduser("~/.claude/local/claude")]:
        if c and os.path.exists(c):
            return c
    ds = glob.glob(os.path.expanduser("~/Library/Application Support/Claude/claude-code/*/*/claude.app/Contents/MacOS/claude"))
    if ds:
        return max(ds, key=os.path.getmtime)
    raise SystemExit("Không tìm thấy lệnh claude. Xem app/README.md mục 'Lần đầu'.")


def thay(s, b):
    for k, v in b.items():
        s = s.replace("{" + k + "}", v)
    return s


def dung_loi_nhac(text, b):
    cfg = hoso.load(b["HO_SO"])
    text = re.sub(r"\{\{ho_so:([\w.]+)\}\}", lambda m: json.dumps(hoso.get(cfg, m.group(1)), ensure_ascii=False), text)
    text = text.replace("{{bieu_tuong}}", " ".join(loi.bieu_tuong()))
    text = re.sub(r"\{\{file:([^}]+)\}\}", lambda m: (DV / m.group(1)).read_text(encoding="utf-8"), text)
    text = re.sub(r"\{\{muc:([^|}]+)\|([^}]+)\}\}", lambda m: muc(DV / m.group(1), m.group(2)), text)
    text = text.replace("{{kieu_canh}}", ", ".join(sorted(loi.kieu_canh())))
    return text


def muc(f, tieu_de):
    """Trích một mục (từ dòng tiêu đề chứa `tieu_de` tới tiêu đề cùng cấp kế tiếp) — luật vẫn ở một nhà, lời nhắc chỉ trỏ tới."""
    d = f.read_text(encoding="utf-8").split("\n")
    i = next(k for k, x in enumerate(d) if x.startswith("#") and tieu_de in x)
    cap = len(d[i]) - len(d[i].lstrip("#"))
    j = next((k for k in range(i + 1, len(d)) if d[k].startswith("#") and len(d[k]) - len(d[k].lstrip("#")) <= cap), len(d))
    return "\n".join(d[i:j])

