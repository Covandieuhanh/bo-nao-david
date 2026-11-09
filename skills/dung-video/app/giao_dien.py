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


def ten_tai(f):
    """Tên tệp khi tải về: theo tên tập — img-2888.mp4, su-tap-trung-clip-A.mp4, the-view-vung-tau.mp4 (vlog)."""
    if f.name != "video-final.mp4":
        return f.name
    cha = f.parent
    if cha.name.startswith("clip-"): return f"{cha.parent.parent.name.removeprefix('tap-')}-{cha.name}.mp4"
    if cha.name == "2-ban-dai": return f"{cha.parent.name.removeprefix('tap-')}.mp4"
    return f"{cha.name}.mp4"


def tu_may(ip):
    """Ai bấm: Mac này hay thiết bị Tailscale nào (tên máy trong Tailscale) — ghi vào nhật ký mỗi lần duyệt / góp ý / chạy."""
    if ip in ("127.0.0.1", "::1", "::ffff:127.0.0.1"):
        return "Mac này"
    try:
        r = subprocess.run(["/Applications/Tailscale.app/Contents/MacOS/Tailscale", "status", "--json"], capture_output=True, text=True, timeout=5)
        ip4 = ip.replace("::ffff:", "")
        for x in json.loads(r.stdout).get("Peer", {}).values():
            if ip4 in x.get("TailscaleIPs", []):
                return x.get("HostName") or ip4
    except Exception:
        pass
    return ip


def chay_nen(ten, *args, ai=""):
    KHO.joinpath(ten).mkdir(parents=True, exist_ok=True)
    log = open(KHO / ten / "chay.log", "a", encoding="utf-8")
    log.write(f"\n=== {time.strftime('%Y-%m-%d %H:%M:%S')} chay.py {' '.join(args)}" + (f"  ← bấm từ: {ai}" if ai else "") + "\n"); log.flush()
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
    if not dang_chay(ten) and any(v.get("trang_thai") in ("dang-chay", "xep-hang") for v in tt["buoc"].values()):
        for k, v in tt["buoc"].items():      # tiến trình đã chết giữa chừng (tắt máy, tắt app) → coi như đã dừng
            if v.get("trang_thai") in ("dang-chay", "xep-hang"):
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
                "tep": [{"ten": (h.get("nhan") if isinstance(h, dict) else None) or Path(chay.thay(h if isinstance(h, str) else h["file"], b)).name,
                         "gon": isinstance(h, dict) and h.get("gon", False),
                         "noi_dung": doc_tep(chay.thay(h if isinstance(h, str) else h["file"], b), 200000) or "(chưa có)"}
                        for h in ph.get("hien", [])],
                "video": [str(x) for x in sorted(Path("/").glob(chay.thay(ph["video"], b).lstrip("/")))] if ph.get("video") else [],
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
    rs = {"buoc_cu": [], "khung_cu": []}
    if not dang_chay(ten):
        try:
            import ra_soat; rs = ra_soat.ra_soat(ten)
        except Exception as e:
            rs["loi"] = str(e)
    giu = KHO / "_dang-giu.txt"
    P_ = Path(tt["P"])   # video đã xong: bản cuối, các clip highlight, thumbnail đã chọn — xem/tải bất kỳ lúc nào
    xong = [str(x) for x in [P_ / "video-final.mp4", *sorted(P_.glob("clip-*/video-final.mp4"))] if x.exists()]
    anh_bia = [str(x) for x in [P_ / "phat-hanh/thumbnail.jpg"] if x.exists()]
    gy = KHO / ten / "gop-y.json"
    trao_doi = json.loads(gy.read_text(encoding="utf-8")) if gy.exists() else []
    return {"video_xong": xong, "anh_bia": anh_bia, "trao_doi": trao_doi, "hang_doi": giu.read_text().strip() if giu.exists() else None, "ra_soat": rs, "ten": ten, "cong_thuc": ct["ten"], "video": tt["video"], "P": tt["P"], "dang": dang, "dang_chay": dang_chay(ten),
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


NHA = Path.home().resolve()
DUOI_VIDEO = (".mp4", ".mov", ".m4v", ".mts", ".avi", ".mkv")


def trong_nha(p):
    """Trình duyệt tệp chỉ đi trong thư mục nhà, bỏ thư mục ẩn và ~/Library (trừ Google Drive ở ~/Library/CloudStorage)."""
    try:
        p = Path(p).expanduser().resolve()
        r = p.relative_to(NHA)
    except Exception:
        return None
    if any(x.startswith(".") for x in r.parts):
        return None
    if r.parts[:1] == ("Library",) and r.parts[:2] != ("Library", "CloudStorage"):
        return None
    return p


def noi_nhanh():
    ds = [("Tải về", NHA / "Downloads"), ("Màn hình nền", NHA / "Desktop"), ("Phim", NHA / "Movies")]
    for d in sorted((NHA / "Library/CloudStorage").glob("GoogleDrive-*")):
        tk = d.name.split("-", 1)[1].split("@")[0]
        for goc in d.iterdir():
            if (goc / "Video-goc").is_dir(): ds.insert(0, (f"Drive Video-goc ({tk})", goc / "Video-goc"))
            if goc.is_dir() and not goc.name.startswith("."): ds.append((f"Drive {tk}", goc))
    return [{"ten": t, "p": str(p)} for t, p in ds if p.is_dir()]


def thu_muc(p):
    p = trong_nha(p)
    if not p or not p.is_dir():
        raise ValueError("không mở được thư mục này")
    muc = []
    for x in p.iterdir():
        if x.name.startswith(".") or x.name.startswith("._"):
            continue
        try:
            st = x.stat()
        except OSError:
            continue
        if x.is_dir():
            muc.append({"ten": x.name, "p": str(x), "loai": "thu-muc", "luc": st.st_mtime})
        elif x.suffix.lower() in DUOI_VIDEO:
            muc.append({"ten": x.name, "p": str(x), "loai": "video", "mb": round(st.st_size / 1048576), "luc": st.st_mtime,
                        "drive": "/Library/CloudStorage/" in str(x), "da_dung": chay.la_ban_da_dung(x)})
    muc.sort(key=lambda m: (m["loai"] != "thu-muc", -m["luc"] if m["loai"] == "video" else 0, m["ten"].lower()))
    cha = trong_nha(p.parent) if p != NHA else None
    return {"p": str(p), "hien": str(p).replace(str(NHA), "~", 1), "cha": str(cha) if cha and cha != p else None, "muc": muc[:400]}


def anh_nho(p):
    """Ảnh nhỏ một khung của video (lưu đệm ~/Movies/_app/_anh-nho). Không làm cho tệp trên Drive để khỏi kéo cả tệp về."""
    p = trong_nha(p)
    if not p or not p.is_file() or "/Library/CloudStorage/" in str(p):
        return None
    import hashlib
    st = p.stat(); dem = KHO / "_anh-nho" / (hashlib.md5(f"{p}{st.st_mtime}".encode()).hexdigest() + ".jpg")
    if not dem.exists():
        dem.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["/opt/homebrew/bin/ffmpeg", "-v", "error", "-y", "-ss", "1", "-i", str(p), "-frames:v", "1",
                        "-vf", "scale=240:-2", str(dem)], timeout=30)
    return dem if dem.exists() else None


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
            if u.path == "/api/tap-ban-dai":   # nguồn cho highlight: tập đã dựng bản dài, còn bản sạch
                ds = []
                for v in sorted(MOVIES.glob("tap-*/2-ban-dai/davinci/media/video_goc.mp4"), key=os.path.getmtime, reverse=True):
                    P = v.parents[2]
                    ds.append({"tap": P.parent.name[4:], "p": str(P), "co_hl": (P.parent / "3-highlight").exists()})
                return self.gui(ds)
            if u.path == "/api/drive-moi":
                import drive; return self.gui(drive.moi())
            if u.path == "/api/tu-link":
                import drive; return self.gui(drive.tim(q.get("link", [""])[0], han=20))
            if u.path == "/api/noi-nhanh":
                return self.gui(noi_nhanh())
            if u.path == "/api/thu-muc":
                try:
                    return self.gui(thu_muc(q.get("p", [str(NHA / "Downloads")])[0]))
                except (ValueError, PermissionError) as e:
                    return self.gui({"loi": str(e) if isinstance(e, ValueError) else "macOS chưa cho app đọc thư mục này"}, 400)
            if u.path == "/api/anh-nho":
                f = anh_nho(q["p"][0])
                return self.gui(f.read_bytes(), kieu="image/jpeg") if f else self.gui({"loi": "không có ảnh"}, 404)
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
        if self.path.find("&tai=1") > 0:   # nút Tải về: lưu tệp thay vì phát
            from urllib.parse import quote
            self.send_header("Content-Disposition", f"attachment; filename*=UTF-8''{quote(ten_tai(f))}")
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
        if u == "/api/gop-y":
            if d.get("loai") not in ("video", "bai-dang", "loc") or not d.get("gop_y", "").strip():
                return self.gui({"loi": "thiếu góp ý"}, 400)
            chay_nen(ten, "gop", ten, d["loai"], d["gop_y"].strip(), ai=tu_may(self.client_address[0]))
            return self.gui({"ok": True})
        if u == "/api/don-tap":   # dọn file tạm cả tập (bản dài + highlight) hoặc vlog — vào Thùng rác; việc đang dở tự bỏ qua (don_tap.py)
            tt = chay.doc(KHO / ten / "trang-thai.json"); P = Path(tt["P"])
            dich = P if P.parent.name == "vlog" else P.parent
            r = subprocess.run([sys.executable, "-I", str(APP.parent / "video-style-edit/scripts/don_tap.py"), "--xoa", str(dich)],
                               capture_output=True, text=True, timeout=600)
            with open(KHO / ten / "chay.log", "a", encoding="utf-8") as lg:
                lg.write(f"\n=== {time.strftime('%H:%M:%S')} Dọn tập ← bấm từ: {tu_may(self.client_address[0])}\n{r.stdout[-2000:]}")
            return self.gui({"ok": True, "ket_qua": r.stdout.strip().split("\n")[-3:]})
        if u == "/api/cap-nhat-khung":
            tt = chay.doc(KHO / ten / "trang-thai.json")
            if not (Path(tt["P"]) / "motion/src").is_dir():
                return self.gui({"loi": "dự án chưa qua bước Tạo dự án — chưa có khung dựng để cập nhật"}, 400)
            r = subprocess.run([sys.executable, "-I", str(APP / "ap/cap_nhat_khung.py"), tt["P"]], capture_output=True, text=True, timeout=600)
            with open(KHO / ten / "chay.log", "a", encoding="utf-8") as lg:
                lg.write(f"\n=== {time.strftime('%H:%M:%S')} David bấm Cập nhật khung dựng\n{r.stdout}{r.stderr}")
            if r.returncode != 0:
                return self.gui({"loi": (r.stdout + r.stderr)[-500:]}, 500)
            doi = "0 tệp" not in r.stdout
            if doi and tt["buoc"].get("render", {}).get("trang_thai") in ("xong", "loi", "da-dung"):
                chay_nen(ten, "lai", ten, "render")      # đã render rồi → render lại với khung mới (các bước Claude sau đó dùng lại kết quả cũ, ai=tu_may(self.client_address[0]))
            return self.gui({"ok": True, "ket_qua": r.stdout.strip().split("\n")[0], "render_lai": doi and "render" in tt["buoc"]})
        if u == "/api/xoa":
            xoa(ten); CHAY.pop(ten, None); return self.gui({"ok": True})
        if u == "/api/moi":
            vv = Path(os.path.expanduser(d.get("video", "")))
            if not (vv.is_file() or (vv.is_dir() and (vv / "davinci/media/video_goc.mp4").exists())):
                return self.gui({"loi": "không thấy file video"}, 400)
            if chay.la_ban_da_dung(d["video"]):
                return self.gui({"loi": "Video này là bản đã dựng (có sẵn chữ, dấu góc) — chọn video gốc quay từ máy"}, 400)
            if (KHO / ten / "trang-thai.json").exists():
                return self.gui({"loi": "đã có việc tên này"}, 409)
            chay_nen(ten, "moi", d["cong_thuc"], d["video"], ten, json.dumps(d.get("tuy_chon", {}), ensure_ascii=False), ai=tu_may(self.client_address[0]))
        elif u == "/api/chon-anh":
            tt = chay.doc(KHO / ten / "trang-thai.json"); ph = chay.phieu(tt.get("dang") or ""); b = chay.bien(tt)
            ca = ph.get("chon_anh") or {}; tep = Path(d.get("tep", "")).resolve()
            ds = [x.resolve() for x in Path("/").glob(chay.thay(ca.get("tep", "-"), b).lstrip("/"))]
            if tep not in ds:
                return self.gui({"loi": "ảnh không có trong danh sách"}, 400)
            __import__("shutil").copyfile(tep, chay.thay(ca["dich"], b)); (KHO / ten / "da-chon-anh.txt").write_text(str(tep))
            return self.gui({"ok": True})
        elif u == "/api/duyet":
            chay_nen(ten, "duyet", ten, *( [d["gop_y"]] if d.get("gop_y") else []), ai=tu_may(self.client_address[0]))
        elif u == "/api/tiep":
            chay_nen(ten, "tiep", ten, ai=tu_may(self.client_address[0]))
        elif u == "/api/lai":
            chay_nen(ten, "lai", ten, d["buoc"], ai=tu_may(self.client_address[0]))
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
