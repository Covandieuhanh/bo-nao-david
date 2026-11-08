#!/usr/bin/env python3
"""GIAO DIỆN APP DỰNG VIDEO — trang web chỉ chạy trên máy này: python3 -I giao_dien.py → http://localhost:8765
Chỉ là vỏ: mọi việc chạy qua chay.py (máy chạy bước). Không chứa luật dựng nào."""
import ipaddress, json, os, re, signal, socket, subprocess, sys, time, glob, mimetypes
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

APP = Path(__file__).resolve().parent
KHO = Path(os.path.expanduser("~/Movies/_app"))
MOVIES = Path(os.path.expanduser("~/Movies")).resolve()
CHAY = {}  # tên việc → tiến trình đang chạy
sys.path.insert(0, str(APP))
import chay  # noqa: E402


def chay_nen(ten, *args):
    KHO.joinpath(ten).mkdir(parents=True, exist_ok=True)
    log = open(KHO / ten / "chay.log", "a", encoding="utf-8")
    log.write(f"\n=== {time.strftime('%Y-%m-%d %H:%M:%S')} chay.py {' '.join(args)}\n"); log.flush()
    p = subprocess.Popen([sys.executable, "-I", str(APP / "chay.py"), *args], stdout=log, stderr=subprocess.STDOUT,
                         start_new_session=True)   # nhóm tiến trình riêng: nút Dừng tắt được cả render/ffmpeg con
    CHAY[ten] = p; (KHO / ten / "pid").write_text(str(p.pid))


def pid(ten):
    try:
        return int((KHO / ten / "pid").read_text())
    except Exception:
        return None


def dang_chay(ten):
    p = CHAY.get(ten)
    if p is not None:
        return p.poll() is None
    n = pid(ten)               # máy chủ khởi động lại khi việc vẫn chạy
    if not n:
        return False
    try:
        os.kill(n, 0); return True
    except OSError:
        return False


def dung(ten):
    """Dừng việc đang chạy (cả tiến trình con), đánh dấu bước dở là ⏸ để Chạy tiếp làm lại đúng bước đó."""
    n = pid(ten)
    if n and dang_chay(ten):
        for sig in (signal.SIGTERM, signal.SIGKILL):
            try: os.killpg(n, sig)
            except OSError: break
            for _ in range(20):
                if not dang_chay(ten): break
                time.sleep(0.2)
            if not dang_chay(ten): break
    f = KHO / ten / "trang-thai.json"; tt = chay.doc(f)
    for k, v in tt["buoc"].items():
        if v.get("trang_thai") == "dang-chay":
            tt["buoc"][k] = {"trang_thai": "da-dung", "luc": time.strftime("%H:%M:%S")}
    chay.ghi(f, tt)
    with open(KHO / ten / "chay.log", "a", encoding="utf-8") as lg:
        lg.write(f"\n=== {time.strftime('%H:%M:%S')} David bấm Dừng\n")


def doc_tep(p, toi_da=20000):
    try:
        s = Path(p).read_text(encoding="utf-8")
        return s[-toi_da:]
    except Exception:
        return None


def token(ten):
    f = KHO / ten / "token.jsonl"; tong = {"lan_goi": 0, "vao": 0, "ra": 0}
    if f.exists():
        for l in f.read_text(encoding="utf-8").splitlines():
            d = json.loads(l); u = d.get("usage") or {}
            tong["lan_goi"] += 1
            tong["vao"] += u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)
            tong["ra"] += u.get("output_tokens", 0)
    return tong


def chi_tiet(ten):
    f = KHO / ten / "trang-thai.json"; tt = chay.doc(f)
    if not dang_chay(ten) and any(v.get("trang_thai") == "dang-chay" for v in tt["buoc"].values()):
        for k, v in tt["buoc"].items():      # tiến trình đã chết giữa chừng (tắt máy, tắt app) → coi như đã dừng
            if v.get("trang_thai") == "dang-chay":
                tt["buoc"][k] = {"trang_thai": "da-dung", "luc": v.get("luc")}
        chay.ghi(f, tt)
    ct = chay.cong_thuc(tt["cong_thuc"]); b = chay.bien(tt)
    buoc = []
    for bid in ct["buoc"]:
        ph = chay.phieu(bid)
        buoc.append({"id": bid, "ten": ph.get("ten", bid), "loai": ph["loai"], **tt["buoc"].get(bid, {"trang_thai": "chua"})})
    cong = None; dang = tt.get("dang")
    if dang and tt["buoc"].get(dang, {}).get("trang_thai") == "cho-duyet":
        ph = chay.phieu(dang)
        cong = {"id": dang, "ten": ph.get("ten"), "nhan_gop_y": bool(ph.get("gop_y_cho")),
                "tep": [{"ten": Path(chay.thay(h, b)).name, "noi_dung": doc_tep(chay.thay(h, b)) or "(chưa có)"} for h in ph.get("hien", [])],
                "video": chay.thay(ph["video"], b) if ph.get("video") and Path(chay.thay(ph["video"], b)).exists() else None,
                "anh": [str(x) for a in ph.get("anh", []) for x in sorted(Path("/").glob(chay.thay(a, b).lstrip("/")))],
                "chon_anh": None}
        if ph.get("chon_anh"):
            ca = ph["chon_anh"]; dich = Path(chay.thay(ca["dich"], b))
            ds = [str(x) for x in sorted(Path("/").glob(chay.thay(ca["tep"], b).lstrip("/")))]
            if ds:
                cong["chon_anh"] = {"nhan": ca.get("nhan", "Chọn ảnh"), "ds": ds, "da_chon": (KHO / ten / "da-chon-anh.txt").read_text().strip()
                                    if (KHO / ten / "da-chon-anh.txt").exists() and dich.exists() else None}
    log_buoc = None
    if dang:
        log_buoc = doc_tep(KHO / ten / "log" / f"{dang}.txt", 6000)
    return {"ten": ten, "cong_thuc": ct["ten"], "video": tt["video"], "P": tt["P"], "dang": dang, "dang_chay": dang_chay(ten),
            "buoc": buoc, "cong": cong, "log": log_buoc, "log_chung": doc_tep(KHO / ten / "chay.log", 3000), "token": token(ten),
            "xong_luc": tt.get("xong_luc")}


def thu_xoa(ten):
    """Những thư mục sẽ vào Thùng rác khi xoá dự án: trạng thái app + cả tập ~/Movies/tap-<tên> (gốc, bản dài, highlight)."""
    ds = [KHO / ten]
    f = KHO / ten / "trang-thai.json"
    if f.exists():
        P = Path(chay.doc(f)["P"])
        tap = P.parent if P.name == "2-ban-dai" else P
        if tap.exists() and str(tap.resolve()).startswith(str(MOVIES) + "/") and tap.resolve() != MOVIES:
            ds.append(tap)
    out = []
    for d in ds:
        if d.exists():
            n = sum(x.stat().st_size for x in d.rglob("*") if x.is_file() and not x.is_symlink())
            out.append({"duong_dan": str(d), "mb": round(n / 1048576)})
    return out


def xoa(ten):
    """Chuyển vào Thùng rác (lấy lại được), không xoá hẳn."""
    rac = Path.home() / ".Trash"; luc = time.strftime("%H%M%S")
    for x in thu_xoa(ten):
        d = Path(x["duong_dan"]); dich = rac / d.name
        if dich.exists():
            dich = rac / f"{d.name}-{luc}"
        os.rename(d, dich) if os.stat(d).st_dev == os.stat(rac).st_dev else __import__("shutil").move(str(d), str(dich))


def video_goc():
    ds = []
    for d in ["~/Downloads", "~/Desktop", "~/Movies/video-goc", "~/Movies/_video-goc"]:
        for f in glob.glob(os.path.expanduser(d) + "/**/*", recursive=True):
            if f.lower().endswith((".mp4", ".mov", ".m4v")) and not chay.la_ban_da_dung(f):
                ds.append((os.path.getmtime(f), f))
    return [f for _, f in sorted(ds, reverse=True)[:40]]


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def gui(self, d, ma=200, kieu="application/json; charset=utf-8"):
        b = d if isinstance(d, bytes) else json.dumps(d, ensure_ascii=False).encode()
        self.send_response(ma); self.send_header("Content-Type", kieu); self.send_header("Content-Length", str(len(b)))
        self.end_headers(); self.wfile.write(b)

    def cho_phep(self):
        """Chỉ chính máy này + thiết bị trong mạng Tailscale của David (100.64.0.0/10, fd7a:115c:a1e0::/48).
        Máy khác cùng wifi hay ngoài Internet đều bị chặn, dù máy chủ nghe trên mọi cổng mạng."""
        ip = ipaddress.ip_address(self.client_address[0].split("%")[0])
        if ip.version == 6 and ip.ipv4_mapped: ip = ip.ipv4_mapped
        if ip.is_loopback or ip in ipaddress.ip_network("100.64.0.0/10") or ip in ipaddress.ip_network("fd7a:115c:a1e0::/48"):
            return True
        self.gui({"loi": "chỉ mở được trên máy này hoặc thiết bị trong Tailscale của David"}, 403)
        return False

    def do_GET(self):
        if not self.cho_phep(): return
        u = urlparse(self.path); q = parse_qs(u.query)
        try:
            if u.path == "/":
                return self.gui((APP / "giao_dien.html").read_bytes(), kieu="text/html; charset=utf-8")
            if u.path == "/api/viec":
                ds = []
                for f in sorted(KHO.glob("*/trang-thai.json"), key=os.path.getmtime, reverse=True):
                    tt = chay.doc(f); dang = tt.get("dang")
                    ds.append({"ten": tt["ten"], "cong_thuc": tt["cong_thuc"], "dang": dang, "dang_chay": dang_chay(tt["ten"]),
                               "trang_thai": tt["buoc"].get(dang, {}).get("trang_thai") if dang else ("xong" if tt.get("xong_luc") else "chua")})
                return self.gui(ds)
            if u.path == "/api/chi-tiet":
                return self.gui(chi_tiet(q["ten"][0]))
            if u.path == "/api/cong-thuc":
                return self.gui([{"id": f.stem, "ten": chay.doc(f)["ten"]} for f in sorted((APP / "cong-thuc").glob("*.json"))])
            if u.path == "/api/thu-xoa":
                return self.gui(thu_xoa(q["ten"][0]))
            if u.path == "/api/video-goc":
                return self.gui(video_goc())
            if u.path == "/tep":
                return self.tep(q["p"][0])
            self.gui({"loi": "không có"}, 404)
        except Exception as e:
            self.gui({"loi": str(e)}, 500)

    def tep(self, p):
        f = Path(p).resolve()
        if not (str(f).startswith(str(MOVIES)) and f.is_file()):
            return self.gui({"loi": "chỉ mở file trong ~/Movies"}, 403)
        n = f.stat().st_size; rg = self.headers.get("Range"); a, b = 0, n - 1
        if rg and rg.startswith("bytes="):
            x, y = rg[6:].split("-"); a = int(x or 0); b = int(y) if y else min(n - 1, a + 8 * 1024 * 1024)
        self.send_response(206 if rg else 200)
        self.send_header("Content-Type", mimetypes.guess_type(str(f))[0] or "application/octet-stream")
        self.send_header("Accept-Ranges", "bytes"); self.send_header("Content-Length", str(b - a + 1))
        if rg: self.send_header("Content-Range", f"bytes {a}-{b}/{n}")
        self.end_headers()
        with open(f, "rb") as fh:
            fh.seek(a); con = b - a + 1
            while con > 0:
                k = fh.read(min(1 << 20, con))
                if not k: break
                try: self.wfile.write(k)
                except (BrokenPipeError, ConnectionResetError): return
                con -= len(k)

    def do_POST(self):
        if not self.cho_phep(): return
        if urlparse(self.path).path == "/api/tai-len":
            return self.tai_len()
        d = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        ten = d.get("ten", "").strip()
        if not ten or "/" in ten or ten.startswith("."):
            return self.gui({"loi": "tên không hợp lệ"}, 400)
        u = urlparse(self.path).path
        if u == "/api/dung":
            dung(ten); return self.gui({"ok": True})
        if dang_chay(ten):
            return self.gui({"loi": "việc này đang chạy"}, 409)
        if u == "/api/xoa":
            xoa(ten); CHAY.pop(ten, None); return self.gui({"ok": True})
        if u == "/api/moi":
            if not Path(os.path.expanduser(d.get("video", ""))).is_file():
                return self.gui({"loi": "không thấy file video"}, 400)
            if chay.la_ban_da_dung(d["video"]):
                return self.gui({"loi": "Video này là bản đã dựng (có sẵn chữ, dấu góc) — chọn video gốc quay từ máy"}, 400)
            if (KHO / ten / "trang-thai.json").exists():
                return self.gui({"loi": "đã có việc tên này"}, 409)
            chay_nen(ten, "moi", d["cong_thuc"], d["video"], ten, json.dumps(d.get("tuy_chon", {}), ensure_ascii=False))
        elif u == "/api/chon-anh":
            tt = chay.doc(KHO / ten / "trang-thai.json"); ph = chay.phieu(tt.get("dang") or ""); b = chay.bien(tt)
            ca = ph.get("chon_anh") or {}; tep = Path(d.get("tep", "")).resolve()
            ds = [x.resolve() for x in Path("/").glob(chay.thay(ca.get("tep", "-"), b).lstrip("/"))]
            if tep not in ds:
                return self.gui({"loi": "ảnh không có trong danh sách"}, 400)
            __import__("shutil").copyfile(tep, chay.thay(ca["dich"], b)); (KHO / ten / "da-chon-anh.txt").write_text(str(tep))
            return self.gui({"ok": True})
        elif u == "/api/duyet":
            chay_nen(ten, "duyet", ten, *( [d["gop_y"]] if d.get("gop_y") else []))
        elif u == "/api/tiep":
            chay_nen(ten, "tiep", ten)
        elif u == "/api/lai":
            chay_nen(ten, "lai", ten, d["buoc"])
        else:
            return self.gui({"loi": "không có"}, 404)
        self.gui({"ok": True})


def _tai_len(self):
    """Nhận video kéo thả / chọn tệp: ghi thẳng vào ~/Movies/tap-<tên>/1-goc/ (đúng chỗ skill lưu file gốc)."""
    q = parse_qs(urlparse(self.path).query); ten = q.get("ten", [""])[0]; tep = os.path.basename(q.get("tep", [""])[0])
    if not re.fullmatch(r"[a-z0-9-]+", ten) or not tep or tep.startswith("."):
        return self.gui({"loi": "tên tập hoặc tên tệp không hợp lệ"}, 400)
    if not tep.lower().endswith((".mp4", ".mov", ".m4v", ".mts", ".avi", ".mkv")):
        return self.gui({"loi": "chỉ nhận tệp video"}, 400)
    d = MOVIES / f"tap-{ten}" / "1-goc"; d.mkdir(parents=True, exist_ok=True); f = d / tep
    con = int(self.headers.get("Content-Length", 0)); tmp = f.with_name("." + tep + ".dang-tai")
    with open(tmp, "wb") as fh:
        while con > 0:
            k = self.rfile.read(min(1 << 20, con))
            if not k: break
            fh.write(k); con -= len(k)
    if con > 0:
        tmp.unlink(missing_ok=True); return self.gui({"loi": "tải lên bị ngắt"}, 400)
    os.replace(tmp, f)
    return self.gui({"ok": True, "duong_dan": str(f)})


H.tai_len = _tai_len


if __name__ == "__main__":
    KHO.mkdir(parents=True, exist_ok=True)
    cong = int(os.environ.get("APP_CONG", 8765))
    print(f"App dựng video: http://localhost:{cong}", flush=True)
    class MayChu(ThreadingHTTPServer):
        address_family = socket.AF_INET6          # nghe cả IPv4 lẫn IPv6 (Tailscale dùng cả hai); quyền vào lọc ở H.cho_phep
        def server_bind(self):
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0); super().server_bind()
    MayChu(("::", cong), H).serve_forever()
