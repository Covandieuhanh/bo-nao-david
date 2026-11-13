# Trang xem kết quả (David 13/11/2026: "cần một chỗ xem lại toàn bộ kết quả đã xong — video render, thumbnail, nội dung đăng bài").
# Chỉ ĐỌC, không dựng, không tốn token: đọc thư mục Drive Video-xong/ (tap-<tên>/ban-dai|highlight/) và trả một trang web.
#   python3 scripts/xem-ket-qua.py            → http://localhost:8765 (mở luôn trình duyệt)
# Mỗi tập: video (.mp4), ảnh (.jpg/.png — thumbnail), chữ đăng bài (.md/.txt — phat-hanh.md, chuong.txt). Bước phát hành của skill dựng
# chép đủ ba thứ vào Drive (luat-chung.md mục "Xong là để xem được").
import html, http.server, os, re, socketserver, sys, urllib.parse, webbrowser

ROOT = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi/Video-xong")
PORT = int(os.environ.get("PORT", 8765))
VID, IMG, TXT = (".mp4", ".mov", ".m4v"), (".jpg", ".jpeg", ".png", ".webp"), (".md", ".txt")

def md(s):
    """Markdown tối giản → HTML (tiêu đề, gạch đầu dòng, đậm, đoạn)."""
    out = []
    for l in html.escape(s).split("\n"):
        l = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", l)
        l = re.sub(r"`(.+?)`", r"<code>\1</code>", l)
        m = re.match(r"^(#{1,4}) (.*)", l)
        if m: out.append(f"<h{len(m.group(1)) + 2}>{m.group(2)}</h{len(m.group(1)) + 2}>")
        elif l.startswith("- "): out.append(f"<div class=li>• {l[2:]}</div>")
        elif l.strip(): out.append(f"<p>{l}</p>")
    return "\n".join(out)

def tap_list():
    res = []
    for d in sorted(os.listdir(ROOT), key=lambda n: -os.path.getmtime(os.path.join(ROOT, n))):
        p = os.path.join(ROOT, d)
        if d.startswith(".") or not os.path.isdir(p): continue
        files = []
        for r, _, fs in os.walk(p):
            for f in sorted(fs):
                if not f.startswith("."): files.append(os.path.relpath(os.path.join(r, f), ROOT))
        res.append((d, os.path.getmtime(p), files))
    return res

def page(sel):
    taps = tap_list()
    sel = sel or (taps[0][0] if taps else "")
    nav = "".join(f'<a class="{"on" if t == sel else ""}" href="/?tap={urllib.parse.quote(t)}">{html.escape(t.replace("tap-", ""))}'
                  f'<small>{sum(f.endswith(VID) for f in fs)} video</small></a>' for t, _, fs in taps)
    body = ""
    for t, _, fs in taps:
        if t != sel: continue
        body += f"<h1>{html.escape(t.replace('tap-', ''))}</h1>"
        for nhom in ("ban-dai", "highlight", ""):
            grp = [f for f in fs if (f.split(os.sep)[1] if f.count(os.sep) > 1 else "") == nhom]
            if not grp: continue
            body += f"<h2>{ {'ban-dai': 'Bản dài', 'highlight': 'Clip ngắn', '': 'Khác'}[nhom] }</h2><div class=grid>"
            for f in grp:
                u = "/f/" + urllib.parse.quote(f); n = html.escape(os.path.basename(f))
                if f.lower().endswith(VID): body += f'<figure><video controls preload=metadata src="{u}#t=1"></video><figcaption>{n}</figcaption></figure>'
                elif f.lower().endswith(IMG): body += f'<figure><a href="{u}" target=_blank><img src="{u}"></a><figcaption>{n}</figcaption></figure>'
            body += "</div>"
            for f in grp:
                if f.lower().endswith(TXT):
                    try: body += f'<details open><summary>{html.escape(os.path.basename(f))}</summary><div class=md>{md(open(os.path.join(ROOT, f), encoding="utf-8").read())}</div></details>'
                    except Exception: pass
    return f"""<!doctype html><html lang=vi><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Kết quả video</title><style>
:root{{--bg:#141418;--card:#1e1e24;--tx:#eee;--dim:#999;--ac:#ff7a2f}}
body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.55 -apple-system,system-ui,sans-serif;display:flex;min-height:100vh}}
nav{{width:250px;flex:none;background:#0e0e11;padding:16px 10px;overflow:auto;height:100vh;position:sticky;top:0;box-sizing:border-box}}
nav b{{display:block;color:var(--ac);margin:0 8px 12px;letter-spacing:.05em}}
nav a{{display:block;padding:8px 10px;border-radius:8px;color:var(--tx);text-decoration:none}} nav a.on,nav a:hover{{background:var(--card)}}
nav small{{display:block;color:var(--dim);font-size:12px}}
main{{flex:1;padding:20px 28px;min-width:0}} h1{{margin:0 0 4px}} h2{{color:var(--ac);font-size:17px;margin:26px 0 10px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}}
figure{{margin:0;background:var(--card);border-radius:10px;overflow:hidden}} video,img{{width:100%;display:block;max-height:520px;background:#000;object-fit:contain}}
figcaption{{padding:6px 10px;color:var(--dim);font-size:13px;word-break:break-all}}
details{{background:var(--card);border-radius:10px;padding:10px 16px;margin-top:14px}} summary{{cursor:pointer;color:var(--ac)}}
.md p{{margin:6px 0}} .md .li{{margin:2px 0 2px 8px}} code{{color:var(--ac)}}
@media(max-width:700px){{body{{display:block}} nav{{width:auto;height:auto;position:static;display:flex;overflow-x:auto;gap:4px}} nav b{{display:none}} nav a{{flex:none}} main{{padding:16px}}}}
</style><nav><b>KẾT QUẢ VIDEO</b>{nav}</nav><main>{body or '<p>Chưa có tập nào trong Drive Video-xong.</p>'}</main></html>"""

class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path.startswith("/f/"):
            p = os.path.realpath(os.path.join(ROOT, urllib.parse.unquote(u.path[3:])))
            if not p.startswith(os.path.realpath(ROOT)) or not os.path.isfile(p): return self.send_error(404)
            return self.send_file(p)
        b = page(urllib.parse.parse_qs(u.query).get("tap", [""])[0]).encode()
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Content-Length", len(b)); self.end_headers()
        self.wfile.write(b)
    def send_file(self, p):   # có Range để tua video (Safari bắt buộc)
        size = os.path.getsize(p); a, b = 0, size - 1
        m = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range", ""))
        if m:
            if m.group(1): a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else size - 1
            else: a = size - int(m.group(2))
            self.send_response(206); self.send_header("Content-Range", f"bytes {a}-{b}/{size}")
        else: self.send_response(200)
        self.send_header("Content-Type", self.guess_type(p)); self.send_header("Accept-Ranges", "bytes"); self.send_header("Content-Length", b - a + 1)
        self.end_headers()
        with open(p, "rb") as f:
            f.seek(a); left = b - a + 1
            try:
                while left > 0:
                    c = f.read(min(1 << 20, left))
                    if not c: break
                    self.wfile.write(c); left -= len(c)
            except (BrokenPipeError, ConnectionResetError): pass

class S(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads = True; allow_reuse_address = True

if __name__ == "__main__":
    srv = S(("127.0.0.1", PORT), H)
    print(f"Trang xem kết quả: http://localhost:{PORT}")
    if "--khong-mo" not in sys.argv: webbrowser.open(f"http://localhost:{PORT}")
    srv.serve_forever()
