# Gốc ngang → xuất dọc: ke-hoach-doi-khung.py <dự án> suggest|sheet|apply
#   suggest: khuon-mat.json + transcript → ke-hoach.json (shot theo người nói) + ke-hoach.md + vet-chu-the.jpg + canh-quay.jpg
#   sheet:   vẽ lại canh-quay.jpg sau khi Claude sửa ke-hoach.json
#   apply:   cắt khung dọc theo ke-hoach.json → tu-lieu/video-goc.mp4 (dọc 1080×1920), bản ngang giữ là video-goc-ngang.mp4
# Mỗi shot: target = "A"/"B"… (người, A là người bên trái nhất) | "wide" (cả khung ngang đặt giữa, nền mờ — cho cảnh
#   không có người/nhiều thứ cần thấy cùng lúc) ; cx = tâm khung 0–1 (tuỳ chọn, ghi đè) ; follow = khung trượt theo người
import glob, json, os, re, shutil, statistics as st, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _chung import node_env

P, MODE = os.path.expanduser(sys.argv[1]), sys.argv[2]
O, MEDIA = os.path.join(P, "kiem-tra", "doi-khung"), os.path.join(P, "tu-lieu")
ENV = node_env()
SR = 4                                   # khung dò mặt mỗi giây (phan-tich-doi-khung.sh)
COLORS = ["red", "lime", "cyan", "magenta", "yellow", "orange"]
MIN_SHOT = 1.2                           # shot ngắn hơn (tiếng "ừ", chen ngang) gộp vào shot trước — tránh nhảy khung liên tục

def src():
    v = glob.glob(os.path.join(MEDIA, "video-goc-ngang.*")) or [os.path.join(MEDIA, "video-goc.mp4")]
    return v[0]

def probe(v):
    w, h, fr = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
        "stream=width,height,r_frame_rate", "-of", "csv=p=0", v], env=ENV).decode().strip().split(",")[:3]
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", v], env=ENV))
    return int(w), int(h), fr, dur

def srt(path):
    out = []
    for b in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        m = re.search(r"(\d+):(\d+):(\d+)[,.](\d+) --> (\d+):(\d+):(\d+)[,.](\d+)\n(.*)", b, re.S)
        if m:
            g = [int(x) for x in m.groups()[:8]]
            out.append(dict(s=g[0]*3600+g[1]*60+g[2]+g[3]/1000, e=g[4]*3600+g[5]*60+g[6]+g[7]/1000, t=m.group(9).strip()))
    return out

def tracks_from(frames):
    """Gom mặt qua các khung thành từng người: khớp theo tâm ngang gần nhất (người ngồi/đứng tương đối yên)."""
    tr = []
    for i, faces in enumerate(frames):
        used = set()
        for f in sorted(faces, key=lambda f: -f["w"]):
            if f["w"] < 0.04: continue                          # mặt quá nhỏ (người qua đường, ảnh treo tường)
            cx = f["x"] + f["w"] / 2
            best = min((t for t in tr if id(t) not in used and i - t["last"] < 8 * SR and abs(t["cx"] - cx) < 0.09),
                       key=lambda t: abs(t["cx"] - cx), default=None)
            if best is None:
                best = dict(cx=cx, last=i, pts={}); tr.append(best)
            best["cx"] = 0.7 * best["cx"] + 0.3 * cx; best["last"] = i; best["pts"][i] = f | {"cx": cx}
            used.add(id(best))
    tr = [t for t in tr if len(t["pts"]) >= max(8, 0.03 * len(frames))]
    merged = []                                                 # cùng một người bị mất dấu rồi gặp lại
    for t in sorted(tr, key=lambda t: min(t["pts"])):
        m = st.median(p["cx"] for p in t["pts"].values())
        for u in merged:
            if abs(u["mcx"] - m) < 0.07 and not (set(u["pts"]) & set(t["pts"])):
                u["pts"].update(t["pts"]); break
        else:
            merged.append(dict(pts=dict(t["pts"]), mcx=m))
    merged.sort(key=lambda t: t["mcx"])
    return {chr(65 + k): t["pts"] for k, t in enumerate(merged[:6])}

def suggest():
    v = src(); W, H, _, dur = probe(v)
    frames = json.load(open(os.path.join(O, "khuon-mat.json")))
    tracks = tracks_from(frames)
    sents = srt(os.path.join(P, "kiem-tra", "goc", "ban-chep-loi.srt"))
    shots, prev = [], None
    for s in sents:
        a, b = int(s["s"] * SR), int(s["e"] * SR) + 1
        score = {}
        for k, pts in tracks.items():
            ms = [pts[i]["m"] for i in range(a, b) if i in pts]
            if len(ms) >= 3: score[k] = st.pstdev(ms) * len(ms) / max(1, b - a)   # miệng cử động × thời gian thấy mặt
        rank = sorted(score.items(), key=lambda x: -x[1])
        sure = bool(rank) and rank[0][1] > 0.004 and (len(rank) == 1 or rank[0][1] > 1.3 * rank[1][1])
        if sure: who = rank[0][0]
        elif prev: who = prev
        elif rank: who = rank[0][0]
        else: who = "wide" if not tracks else max(tracks, key=lambda k: len(tracks[k]))
        if not any(i in pts for pts in tracks.values() for i in range(a, b)): who, sure = "wide", True   # không có mặt nào
        shots.append(dict(start=round(s["s"], 2), end=round(s["e"], 2), target=who, sure=sure, text=s["t"][:60]))
        prev = who
    if not shots:
        shots = [dict(start=0, end=dur, target=max(tracks, key=lambda k: len(tracks[k])) if tracks else "wide", sure=False, text="")]
    # Phủ kín thời gian: shot kéo tới đầu câu sau; gộp shot liền nhau cùng người; gộp shot quá ngắn vào shot trước
    shots[0]["start"] = 0
    for x, y in zip(shots, shots[1:]): x["end"] = y["start"]
    shots[-1]["end"] = round(dur, 2)
    out = []
    for s in shots:
        if out and (s["target"] == out[-1]["target"] or s["end"] - s["start"] < MIN_SHOT):
            out[-1]["end"] = s["end"]; out[-1]["sure"] &= s["sure"] or s["target"] == out[-1]["target"]
        else:
            out.append(s)
    for s in out:   # người di chuyển nhiều trong shot → khung trượt theo
        pts = tracks.get(s["target"], {})
        cxs = [pts[i]["cx"] for i in range(int(s["start"] * SR), int(s["end"] * SR)) if i in pts]
        s["follow"] = len(cxs) > 4 and st.pstdev(cxs) > 0.04
    tr = {k: dict(cx=round(st.median(p["cx"] for p in pts.values()), 3), frames=len(pts), color=COLORS[n])
          for n, (k, pts) in enumerate(tracks.items())}
    json.dump(dict(W=W, H=H, tracks=tr, shots=out), open(os.path.join(O, "ke-hoach.json"), "w"), ensure_ascii=False, indent=1)
    json.dump({k: {str(i): p["cx"] for i, p in pts.items()} for k, pts in tracks.items()}, open(os.path.join(O, "vet-chu-the.json"), "w"))
    # vet-chu-the.jpg: khung có nhiều người nhất, ô màu cho từng người
    i = max(range(len(frames)), key=lambda i: sum(i in p for p in tracks.values()))
    img = sorted(glob.glob(os.path.join(O, "f", "*.jpg")))[i]
    boxes = ",".join(f"drawbox=x=iw*{p[i]['x']:.3f}:y=ih*{p[i]['y']:.3f}:w=iw*{p[i]['w']:.3f}:h=ih*{p[i]['h']:.3f}:c={tr[k]['color']}:t=5"
                     for k, p in tracks.items() if i in p) or "null"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", img, "-vf", boxes, "-update", "1", os.path.join(O, "vet-chu-the.jpg")], check=True, env=ENV)
    mmss = lambda t: f"{int(t // 60)}:{t % 60:04.1f}"
    md = ["Người: " + ", ".join(f"{k} = ô {v['color']} (tâm {v['cx']:.2f}, thấy {v['frames'] / SR:.0f}s)" for k, v in tr.items()),
          "", "| # | Từ | Đến | Khung | Chắc | Câu đầu |", "|---|---|---|---|---|---|"]
    for n, s in enumerate(out, 1):
        md.append(f"| {n} | {mmss(s['start'])} | {mmss(s['end'])} | {s['target']}{' (trượt)' if s['follow'] else ''} | "
                  f"{'✓' if s['sure'] else '?'} | {s['text']} |")
    open(os.path.join(O, "ke-hoach.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(md[0]); print(f"{len(out)} shot · {sum(not s['sure'] for s in out)} cần xem lại → {O}/ke-hoach.md")
    sheet()

def centers(plan, fps, dur):
    """Tâm khung (0–1) cho từng khung hình đầu ra; None = shot 'wide'."""
    trk = {k: {int(i): cx for i, cx in v.items()} for k, v in json.load(open(os.path.join(O, "vet-chu-the.json"))).items()}
    n = int(round(dur * fps)); out = [None] * n
    for s in plan["shots"]:
        a, b = int(round(s["start"] * fps)), min(n, int(round(s["end"] * fps)))
        if s["target"] == "wide": continue
        pts = trk.get(s["target"], {})
        seen = [pts[i] for i in range(int(s["start"] * SR), int(s["end"] * SR) + 1) if i in pts]
        fixed = s.get("cx") or (st.median(seen) if seen else plan["tracks"].get(s["target"], {}).get("cx", 0.5))
        if not s.get("follow") or s.get("cx"):
            for k in range(a, b): out[k] = fixed
            continue
        raw, last = [], fixed                                  # trượt: nội suy + trung bình trượt 1,5 s, giữ yên khi lệch < 2%
        for k in range(a, b):
            i = int(k / fps * SR); last = pts.get(i, last); raw.append(last)
        win = max(1, int(0.75 * fps)); cur = raw[0]
        for j in range(len(raw)):
            m = sum(raw[max(0, j - win): j + win + 1]) / len(raw[max(0, j - win): j + win + 1])
            if abs(m - cur) > 0.02: cur += (m - cur) * 0.15
            out[a + j] = cur
    return out

def crop_w(W, H): return min(W, round(H * 9 / 16 / 2) * 2)

def sheet():
    plan = json.load(open(os.path.join(O, "ke-hoach.json")))
    imgs = sorted(glob.glob(os.path.join(O, "f", "*.jpg")))
    W, H = plan["W"], plan["H"]; cwn = crop_w(W, H) / W
    tmp = os.path.join(O, "bang-tam"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    cs = centers(plan, SR, len(imgs) / SR)
    for n, s in enumerate(plan["shots"][:48]):
        i = min(len(imgs) - 1, int((s["start"] + s["end"]) / 2 * SR))
        c = cs[i] if i < len(cs) else None
        vf = "scale=320:-2" if c is None else (f"drawbox=x=iw*{max(0, min(1 - cwn, c - cwn / 2)):.3f}:y=0:w=iw*{cwn:.3f}:h=ih:c=yellow:t=6,"
                                               f"scale=320:-2")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", imgs[i], "-vf", vf, "-update", "1", os.path.join(tmp, f"s{n:03d}.jpg")], check=True, env=ENV)
    k = len(os.listdir(tmp)); cols = min(k, 6)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-pattern_type", "glob", "-i", os.path.join(tmp, "s*.jpg"), "-vf",
                    f"tile={cols}x{(k + cols - 1) // cols}:padding=4:color=white", "-update", "1", os.path.join(O, "canh-quay.jpg")], check=True, env=ENV)
    print(os.path.join(O, "canh-quay.jpg"), f"({k} shot, khung vàng = phần giữ lại; không có khung = wide)")

def apply():
    plan = json.load(open(os.path.join(O, "ke-hoach.json")))
    v = src()
    if v.endswith("video-goc.mp4"):                              # lần đầu: giữ bản ngang
        nv = os.path.join(MEDIA, "video-goc-ngang.mp4"); os.rename(v, nv); v = nv
    W, H, FR, dur = probe(v)
    fn, fd = (int(x) for x in FR.split("/")); fps = fn / fd
    cw = crop_w(W, H)
    cs = centers(plan, fps, dur)
    X = lambda c: max(0, min(W - cw, round(c * W - cw / 2)))
    first = next((c for c in cs if c is not None), 0.5)
    cmd, lastx = [], None
    for k, c in enumerate(cs):
        if c is None: continue
        x = X(c)
        if x != lastx: cmd.append(f"{k / fps:.4f} crop@rf x {x};"); lastx = x
    open(os.path.join(O, "lenh-cat-khung.txt"), "w").write("\n".join(cmd) + "\n")
    wide = [(s["start"], s["end"]) for s in plan["shots"] if s["target"] == "wide"]
    rf = f"sendcmd=f={os.path.join(O, 'lenh-cat-khung.txt')},crop@rf=w={cw}:h={H}:x={X(first)}:y=0,scale=1080:1920:flags=lanczos,setsar=1"
    if wide:
        en = "+".join(f"between(t,{a:.3f},{b:.3f})" for a, b in wide)
        fc = (f"[0:v]split=3[a][b][c];[a]{rf}[rf];"
              f"[b]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30,eq=brightness=-0.2[bg];"
              f"[c]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=0:(H-h)/2,setsar=1[wd];"
              f"[wd][rf]overlay=0:0:enable='not({en})'[v]")
    else:
        fc = f"[0:v]{rf}[v]"
    script = os.path.join(O, "bo-loc.txt"); open(script, "w").write(fc)
    out = os.path.join(MEDIA, "video-goc.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-stats", "-i", v, "-/filter_complex", script, "-map", "[v]", "-map", "0:a",
                    "-r", FR, "-c:v", "h264_videotoolbox", "-b:v", "20M", "-pix_fmt", "yuv420p", "-c:a", "copy",
                    "-movflags", "+faststart", out], check=True, env=ENV)
    open(os.path.join(P, "chuyen-dong", "src", "du-an.js"), "w").write(
        "// Thông số video gốc (đã cắt dọc từ bản ngang) — tự điền bởi ke-hoach-doi-khung.py apply\n"
        f"export default {{fpsNum: {fn}, fpsDen: {fd}, width: 1080, height: 1920, duration: {dur:.3f}, source: 'video-goc.mp4'}};\n")
    print(f"{len(plan['shots'])} shot ({len(wide)} wide) · khung cắt {cw}×{H} → 1080×1920 · {out}")

{"suggest": suggest, "sheet": sheet, "apply": apply}[MODE]()
