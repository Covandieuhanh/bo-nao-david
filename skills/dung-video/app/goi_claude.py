#!/usr/bin/env python3
"""GỌI CLAUDE cho một bước `claude`: goi_claude.py <buoc/x.json> '<biến JSON>' [góp ý]

Gửi đúng phần cần: lời nhắc của bước (loi-nhac/*.md) + các file khai trong `doc`. Claude không đọc skill (chỉ mở ảnh khi phiếu bước khai `anh`),
chỉ trả về MỘT JSON đúng khuôn (khuon/*.json). Lệnh `kiem` của bước soát JSON; sai → gửi lại một lần kèm lỗi.
Dùng chính Claude Code trên máy (`claude -p`), tính vào gói của David. Ghi token mỗi lần gọi vào {W}/token.jsonl.

Trong lời nhắc dùng được: {{ho_so:khoá.con}} (giá trị hồ sơ tham số của loại video) · {{bieu_tuong}} (mọi biểu tượng đang có
trong thư viện hình) · {{file:đường/dẫn}} (chèn file trong skills/dung-video). Thêm biểu tượng hay tuyến nhạc → Claude tự thấy.
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys, time
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
    """Ghép lời nhắc; lặp tới khi hết chỗ chèn (một lời nhắc có thể chèn lời nhắc khác, vd podcast chèn kịch bản cảnh)."""
    for _ in range(4):
        moi = _ghep(text, b)
        if moi == text: break
        text = moi
    return text


def _ghep(text, b):
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



def goi(bin_, he_thong, noi_dung, khuon, mo_hinh, anh=()):
    """anh: ảnh Claude cần XEM (chiều hình, viền in cứng, chọn ảnh minh hoạ) — chỉ khi đó mới bật công cụ Read, chỉ đọc các thư mục đó."""
    cong_cu = ["--tools", "Read", "--allowedTools", "Read"] + sum((["--add-dir", str(Path(a).parent)] for a in anh), []) if anh else ["--tools", ""]
    cmd = [bin_, "-p", "--model", mo_hinh, *cong_cu, "--setting-sources", "", "--no-session-persistence",
           "--output-format", "json", "--json-schema", json.dumps(khuon, ensure_ascii=False), "--system-prompt", he_thong]
    t = time.time()
    r = subprocess.run(cmd, input=noi_dung, capture_output=True, text=True, timeout=1800, cwd=str(Path(anh[0]).parent) if anh else None)
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


def so_gop_y(W, buoc):
    """Góp ý của David áp dụng cho bước này: các góp ý có `tu` là bước này hoặc một bước trước nó trong công thức."""
    f = W / "gop-y.json"
    if not f.exists():
        return ""
    sys.path.insert(0, str(APP)); import chay
    ds_buoc = chay.cong_thuc(json.loads((W / "trang-thai.json").read_text(encoding="utf-8"))["cong_thuc"])["buoc"]
    vt = ds_buoc.index(buoc) if buoc in ds_buoc else 10 ** 6
    dong = []
    for g in json.loads(f.read_text(encoding="utf-8")):
        tu = g.get("tu") if g.get("tu") in ds_buoc else ds_buoc[0]
        if ds_buoc.index(tu) <= vt:
            dong.append(f"- [{g['luc']}] {g['david']}")
    return "\n".join(dong)


def ghi_phan_hoi(W, buoc, phan_hoi):
    f = W / "gop-y.json"
    if not f.exists() or not phan_hoi:
        return
    ds = json.loads(f.read_text(encoding="utf-8"))
    ds[-1].setdefault("claude", []).append({"buoc": buoc, "luc": time.strftime("%H:%M"), "noi_dung": phan_hoi})
    f.write_text(json.dumps(ds, ensure_ascii=False, indent=1), encoding="utf-8")


def dau_luat(he_thong, khuon, mo_hinh):
    """Dấu của LUẬT một bước Claude (lời nhắc đã ghép skill + khuôn + mô hình) — ra_soat.py so lại để biết skill đổi sau khi bước chạy."""
    return hashlib.sha256("\x00".join([he_thong, json.dumps(khuon, sort_keys=True), mo_hinh]).encode()).hexdigest()


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
    ra = Path(thay(ph["ra"], b)); W = Path(b["W"])
    luat_goc = he_thong                       # dấu luật (ra_soat) tính trên luật skill, không tính phần góp ý
    so = so_gop_y(W, ph["id"])
    if so:
        phan.append("=== GÓP Ý CỦA DAVID CHO VIDEO NÀY (luôn áp dụng: tên riêng, chính tả, nội dung… — thắng mọi suy luận) ===\n" + so)
        he_thong += ("\n\n# Góp ý của David\nPhần GÓP Ý CỦA DAVID luôn được áp dụng. Tên riêng/chính tả David sửa → dùng đúng chữ David ghi ở MỌI chỗ "
                     "(chữ trên màn hình, `sua_chu` cho phụ đề, bài đăng). Ghi `phan_hoi`: 1–2 câu tiếng Việt cho David biết đã sửa gì.")
    if gop_y:
        if ra.exists():
            phan.append(f"=== KẾ HOẠCH LẦN TRƯỚC ===\n{ra.read_text(encoding='utf-8')}")
        phan.append(f"=== GÓP Ý CỦA DAVID (làm theo, giữ nguyên phần không bị nhắc) ===\n{gop_y}")
    anh = [str(x) for a in ph.get("anh", []) for x in sorted(Path("/").glob(thay(a, b).lstrip("/")))]
    if anh:
        phan.append("=== ẢNH CẦN XEM (mở từng ảnh bằng công cụ Read trước khi trả lời) ===\n" + "\n".join(anh))
    noi_dung = "\n\n".join(phan)
    khuon = json.loads((APP / ph["khuon"]).read_text(encoding="utf-8"))
    mo_hinh = os.environ.get("APP_MO_HINH") or MO_HINH.get(ph.get("mo_hinh", "vua"), ph.get("mo_hinh", "sonnet"))
    # NHỚ KẾT QUẢ: cùng lời nhắc (luật đã ghép) + cùng đầu vào + cùng ảnh + cùng khuôn + cùng mô hình → dùng lại, không gọi Claude.
    # Sửa skill chỗ không liên quan bước này, hoặc làm lại từ một bước phía trước mà đầu vào bước này không đổi → 0 token.
    the = hashlib.sha256("\x00".join([he_thong, noi_dung, json.dumps(khuon, sort_keys=True), mo_hinh,
                                       *[hashlib.sha256(Path(a).read_bytes()).hexdigest() for a in anh]]).encode()).hexdigest()
    nho = W / "nho-claude" / f"{ph['id']}.txt"
    (W / "nho-claude").mkdir(parents=True, exist_ok=True)
    (W / "nho-claude" / f"{ph['id']}.luat").write_text(dau_luat(luat_goc, khuon, mo_hinh))
    if not os.environ.get("APP_KHONG_NHO") and ra.exists() and nho.exists() and nho.read_text().strip() == the:
        print("Đầu vào không đổi so với lần trước — dùng lại kết quả cũ, không gọi Claude (0 token).")
        return
    bin_ = tim_claude()
    for lan in (1, 2):
        kq, tk = goi(bin_, he_thong, noi_dung, khuon, mo_hinh, anh)
        ra.parent.mkdir(parents=True, exist_ok=True)
        ra.write_text(json.dumps(kq, ensure_ascii=False, indent=1), encoding="utf-8")
        with open(W / "token.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"buoc": ph["id"], "lan": lan, "mo_hinh": mo_hinh, "do_dai_gui": len(he_thong) + len(noi_dung), **tk},
                               ensure_ascii=False) + "\n")
        print(f"Claude ({mo_hinh}) lần {lan}: {tk['giay']} s · {tk['usage'] and tk['usage'].get('output_tokens')} token ra")
        r = subprocess.run(["zsh", "-c", thay(ph["kiem"], b)], capture_output=True, text=True) if ph.get("kiem") else None
        if r:
            print(r.stdout[-3000:], r.stderr[-1500:])
        if r is None or r.returncode == 0:
            nho.parent.mkdir(exist_ok=True); nho.write_text(the)
            if gop_y: ghi_phan_hoi(W, ph["id"], kq.get("phan_hoi"))
            return
        noi_dung += (f"\n\n=== KẾ HOẠCH VỪA TRẢ ===\n{json.dumps(kq, ensure_ascii=False)}\n\n=== LỖI KHI KIỂM (sửa đúng các lỗi này, "
                     f"giữ nguyên phần còn lại) ===\n{r.stdout[-3000:]}")
    raise SystemExit("Kế hoạch vẫn sai sau 2 lần — xem log.")


if __name__ == "__main__":
    main()
