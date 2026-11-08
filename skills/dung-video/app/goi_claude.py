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
    return text


def goi(bin_, he_thong, noi_dung, khuon, mo_hinh):
    cmd = [bin_, "-p", "--model", mo_hinh, "--tools", "", "--setting-sources", "", "--no-session-persistence",
           "--output-format", "json", "--json-schema", json.dumps(khuon, ensure_ascii=False), "--system-prompt", he_thong]
    t = time.time()
    r = subprocess.run(cmd, input=noi_dung, capture_output=True, text=True, timeout=1800)
    try:
        d = json.loads(r.stdout)
    except Exception:
        raise SystemExit(f"Claude trả về không đọc được:\n{r.stdout[-2000:]}\n{r.stderr[-2000:]}")
    if d.get("is_error"):
        raise SystemExit(f"Claude báo lỗi: {d.get('result')}")
    kq = d.get("structured_output")
    if kq is None:
        s = (d.get("result") or "").strip()
        s = s[s.find("{"): s.rfind("}") + 1] if "{" in s else s
        kq = json.loads(s)
    return kq, {"giay": round(time.time() - t), "usage": d.get("usage"), "cost": d.get("total_cost_usd")}


def main():
    ph = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    b = json.loads(sys.argv[2]); gop_y = sys.argv[3] if len(sys.argv) > 3 else ""
    he_thong = dung_loi_nhac((APP / ph["loi_nhac"]).read_text(encoding="utf-8"), b)
    phan = []
    for d in ph.get("doc", []):
        p = Path(thay(d["file"], b))
        if not p.exists():
            if d.get("tuy_chon"):
                continue
            raise SystemExit(f"Thiếu file đầu vào: {p}")
        phan.append(f"=== {d['nhan']} ===\n{p.read_text(encoding='utf-8')}")
    if gop_y:
        cu = Path(thay(ph["ra"], b))
        if cu.exists():
            phan.append(f"=== KẾ HOẠCH LẦN TRƯỚC ===\n{cu.read_text(encoding='utf-8')}")
        phan.append(f"=== GÓP Ý CỦA DAVID (làm theo, giữ nguyên phần không bị nhắc) ===\n{gop_y}")
    noi_dung = "\n\n".join(phan)
    khuon = json.loads((APP / ph["khuon"]).read_text(encoding="utf-8"))
    mo_hinh = os.environ.get("APP_MO_HINH") or MO_HINH.get(ph.get("mo_hinh", "vua"), ph.get("mo_hinh", "sonnet"))
    bin_ = tim_claude(); ra = Path(thay(ph["ra"], b)); W = Path(b["W"])
    for lan in (1, 2):
        kq, tk = goi(bin_, he_thong, noi_dung, khuon, mo_hinh)
        ra.parent.mkdir(parents=True, exist_ok=True)
        ra.write_text(json.dumps(kq, ensure_ascii=False, indent=1), encoding="utf-8")
        with open(W / "token.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"buoc": ph["id"], "lan": lan, "mo_hinh": mo_hinh, "do_dai_gui": len(he_thong) + len(noi_dung), **tk},
                               ensure_ascii=False) + "\n")
        print(f"Claude ({mo_hinh}) lần {lan}: {tk['giay']} s · {tk['usage'] and tk['usage'].get('output_tokens')} token ra")
        if not ph.get("kiem"):
            return
        r = subprocess.run(["zsh", "-c", thay(ph["kiem"], b)], capture_output=True, text=True)
        print(r.stdout[-3000:], r.stderr[-1500:])
        if r.returncode == 0:
            return
        noi_dung += (f"\n\n=== KẾ HOẠCH VỪA TRẢ ===\n{json.dumps(kq, ensure_ascii=False)}\n\n=== LỖI KHI KIỂM (sửa đúng các lỗi này, "
                     f"giữ nguyên phần còn lại) ===\n{r.stdout[-3000:]}")
    raise SystemExit("Kế hoạch vẫn sai sau 2 lần — xem log.")


if __name__ == "__main__":
    main()
