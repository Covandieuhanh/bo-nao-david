#!/usr/bin/env python3
"""GIAO DIỆN APP DỰNG VIDEO — trang web chỉ chạy trên máy này: python3 -I giao_dien.py → http://localhost:8765
Chỉ là vỏ: mọi việc chạy qua chay.py (máy chạy bước). Không chứa luật dựng nào."""
import json, os, subprocess, sys, time, glob, mimetypes
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
    CHAY[ten] = subprocess.Popen([sys.executable, "-I", str(APP / "chay.py"), *args], stdout=log, stderr=subprocess.STDOUT)


def dang_chay(ten):
    p = CHAY.get(ten)
    return bool(p and p.poll() is None)


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
    tt = chay.doc(KHO / ten / "trang-thai.json"); ct = chay.cong_thuc(tt["cong_thuc"]); b = chay.bien(tt)
    buoc = []
    for bid in ct["buoc"]:
        ph = chay.phieu(bid)
        buoc.append({"id": bid, "ten": ph.get("ten", bid), "loai": ph["loai"], **tt["buoc"].get(bid, {"trang_thai": "chua"})})
    cong = None; dang = tt.get("dang")
    if dang and tt["buoc"].get(dang, {}).get("trang_thai") == "cho-duyet":
        ph = chay.phieu(dang)
        cong = {"id": dang, "ten": ph.get("ten"), "nhan_gop_y": bool(ph.get("gop_y_cho")),
                "tep": [{"ten": Path(chay.thay(h, b)).name, "noi_dung": doc_tep(chay.thay(h, b)) or "(chưa có)"} for h in ph.get("hien", [])],
                "video": chay.thay(ph["video"], b) if ph.get("video") and Path(chay.thay(ph["video"], b)).exists() else None}
    log_buoc = None
    if dang:
        log_buoc = doc_tep(KHO / ten / "log" / f"{dang}.txt", 6000)
    return {"ten": ten, "cong_thuc": ct["ten"], "video": tt["video"], "P": tt["P"], "dang": dang, "dang_chay": dang_chay(ten),
            "buoc": buoc, "cong": cong, "log": log_buoc, "log_chung": doc_tep(KHO / ten / "chay.log", 3000), "token": token(ten),
            "xong_luc": tt.get("xong_luc")}


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

    def do_GET(self):
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
        d = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        ten = d.get("ten", "").strip()
        if not ten or "/" in ten or ten.startswith("."):
            return self.gui({"loi": "tên không hợp lệ"}, 400)
        if dang_chay(ten):
            return self.gui({"loi": "việc này đang chạy"}, 409)
        u = urlparse(self.path).path
        if u == "/api/moi":
            if not Path(os.path.expanduser(d.get("video", ""))).is_file():
                return self.gui({"loi": "không thấy file video"}, 400)
            if chay.la_ban_da_dung(d["video"]):
                return self.gui({"loi": "Video này là bản đã dựng (có sẵn chữ, dấu góc) — chọn video gốc quay từ máy"}, 400)
            if (KHO / ten / "trang-thai.json").exists():
                return self.gui({"loi": "đã có việc tên này"}, 409)
            chay_nen(ten, "moi", d["cong_thuc"], d["video"], ten)
        elif u == "/api/duyet":
            chay_nen(ten, "duyet", ten, *( [d["gop_y"]] if d.get("gop_y") else []))
        elif u == "/api/tiep":
            chay_nen(ten, "tiep", ten)
        elif u == "/api/lai":
            chay_nen(ten, "lai", ten, d["buoc"])
        else:
            return self.gui({"loi": "không có"}, 404)
        self.gui({"ok": True})


if __name__ == "__main__":
    KHO.mkdir(parents=True, exist_ok=True)
    cong = int(os.environ.get("APP_CONG", 8765))
    print(f"App dựng video: http://localhost:{cong}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", cong), H).serve_forever()
