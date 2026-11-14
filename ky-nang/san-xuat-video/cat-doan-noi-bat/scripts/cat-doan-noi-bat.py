# Cắt + ghép các câu đã chọn thành clip highlight: cat-doan-noi-bat.py <dự án> [mã phương án, mặc định tất cả]
# Đọc <dự án>/phuong-an.json:
#   {"options": [{"id": "A", "chon_y": {"boi_canh": "...", "y_tron": "...", "mang_ve": "...", "chua_lai": "..."}, "pieces": [{"start": 812.4, "end": 817.9, "role": "CHAM", "text": "...", "zoom": false}, ...]}, ...]}
# pieces theo THỨ TỰ PHÁT trong clip; start/end = mốc chữ đầu / chữ cuối trong video nguồn (lấy từ words.srt). Script tự:
#   - lùi 0,15 s trước chữ đầu, thêm 0,25 s sau chữ cuối (không mất âm)
#   - thêm 1 s lặng sau câu KEUGOI kết bằng "?" và sau câu cuối clip nếu là KEUGOI (người xem kịp nghĩ) — lặng chèn vào
#     (giữ khung cuối + tiếng câm), không lấy tiếng nguồn phía sau vì câu kế tiếp có thể nói liền
#   - "zoom": true → khung dồn chậm 1,0 → 1,12× vào giữa suốt câu đó (cú chốt ở câu kêu gọi)
#   - gộp hai câu liền nhau trong nguồn khi khoảng giữa ≤ 0,6 s (giữ nguyên nhịp nói); > 0,6 s thì cắt bỏ khoảng lặng
#     (không gộp câu có zoom hoặc có 1 s lặng — chúng luôn là đoạn riêng)
#   - CẮT CỨNG ở mỗi mối nhảy (David chốt 2026-11-04: "sao chép chuẩn kênh lớn" — clip DOAC/Hormozi giấu mối cắt, không chip
#     tua). --tua bật lại kiểu cũ: chèn 0,4 s giữ khung + nhoè dọc ở mối nhảy (chip ⏩ + thanh tập gốc do bước dựng thêm).
#   - cắt khoảng lặng ≥ 0,45 s BÊN TRONG câu còn 0,24 s (khoang-lang.py) — trừ câu có zoom (cú chốt giữ nhịp)
#   - fade âm 15/30 ms ở mỗi mối (chống tiếng "tách"), mọi nhánh tiếng về fltp 48 kHz stereo trước concat
#   - mã hoá phần cứng h264_videotoolbox (libx264 chậm ~10×)
# Ra cat/<id>.mp4 (khung như nguồn) + cat/<id>-map.json (mốc clip ↔ mốc nguồn) + bảng ở cat/<id>.md.
# Tự kiểm: chép lời lại bản cắt (whisper.cpp) → so với "text" đã chọn; chữ thừa (lọt từ câu bên cạnh) / chữ thiếu (bị cụt)
# in ra và ghi cuối cat/<id>.md. Bỏ kiểm bằng --khong-kiem.
import difflib, json, os, re, subprocess, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../mo-dun")); import ho_so as hoso   # tham số: ho-so-thuong-hieu/highlight
_H = hoso.load('highlight')
PRE, POST, ZOOM = 0.15, hoso.get(_H, 'cat_lang.bien_cau_s', 0.25), 0.12
JOIN, TAIL = hoso.get(_H, 'cat_lang.gop_cau_lien_s', 0.6), hoso.get(_H, 'cat_lang.lang_sau_cau_hoi_s', 1.0)
HALF = 0.2 if "--tua" in sys.argv else 0.0   # nửa khoảng chuyển cảnh kiểu cũ (0,4 s mỗi mối nhảy)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pauses
args = [a for a in sys.argv[1:] if not a.startswith("--")]
P = os.path.expanduser(args[0]); only = args[1] if len(args) > 1 else None
CHECK = "--khong-kiem" not in sys.argv
MODEL = os.path.expanduser("~/whisper-models/ggml-large-v3-turbo.bin")
norm = lambda s: re.sub(r"[^\w\s]", " ", s.lower()).split()

def verify(clip, expected):
    """Chép lời bản cắt, so từng từ với lời đã chọn → (độ khớp, chữ thừa, chữ thiếu)."""
    w = clip[:-4] + "-kiem"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-vn", "-ac", "1", "-ar", "16000", w + ".wav"], check=True, env=env)
    subprocess.run(["whisper-cli", "-m", MODEL, "-l", "vi", "-f", w + ".wav", "-otxt", "-of", w, "-np"],
                   check=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(w + ".wav")
    got, exp = norm(open(w + ".txt", encoding="utf-8").read()), norm(expected)
    sm = difflib.SequenceMatcher(a=exp, b=got, autojunk=False)
    extra, miss = [], []
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op in ("replace", "insert"): extra.append(" ".join(got[b1:b2]))
        if op in ("replace", "delete"): miss.append(" ".join(exp[a1:a2]))
    return sm.ratio(), extra, miss
plan = json.load(open(os.path.join(P, "phuong-an.json"), encoding="utf-8"))
if plan.get("status") == "blocked" or not plan.get("options"):
    sys.exit("⛔ phuong-an.json chưa có clip để cắt" + (f": {plan['reason']}" if plan.get("reason") else "") + " — sửa đầu vào rồi chạy lại bước chọn ý.")
src = next(os.path.join(P, f) for f in sorted(os.listdir(P)) if f.startswith("nguon."))
env = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src], env=env))
# khung hiển thị (ffmpeg tự áp metadata xoay khi giải mã) — để cắt lại đúng cỡ sau khi phóng
info = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
    "stream=width,height:stream_side_data=rotation", "-of", "json", src], env=env))["streams"][0]
VW, VH = info["width"], info["height"]
if abs(int(next((x.get("rotation", 0) for x in info.get("side_data_list", [])), 0))) in (90, 270): VW, VH = VH, VW
fmt = lambda s: f"{int(s // 60)}:{s % 60:05.2f}"

for opt in plan["options"]:
    if only and opt["id"] != only: continue
    # BỐN CÂU CHỌN Ý (David chốt 2026-11-07): thiếu một câu thì không cắt, chọn lại ý.
    _cy = opt.get("chon_y") or {}
    _thieu = [k for k in ("boi_canh", "y_tron", "mang_ve", "chua_lai") if not str(_cy.get(k, "")).strip()]
    if _thieu: sys.exit(f"⛔ Clip {opt['id']} thiếu chon_y: {', '.join(_thieu)} — đọc bốn câu chọn ý trong SKILL.md, chọn lại ý.")
    pcs = opt["pieces"]
    segs = []
    for i, p in enumerate(pcs):
        tail = p.get("role") == "KEUGOI" and (i == len(pcs) - 1 or p.get("text", "").rstrip().endswith("?"))
        zoom = bool(p.get("zoom"))
        a = max(0.0, p["start"] - PRE)
        b = min(dur, p["end"] + POST)
        pad = TAIL if tail else 0.0
        if segs and not segs[-1]["lock"] and not zoom and 0 <= p["start"] - segs[-1]["src_end_word"] <= JOIN:
            segs[-1].update(b=b, src_end_word=p["end"], lock=tail, pad=pad); segs[-1]["pieces"].append(i)   # liền nhau trong nguồn → một đoạn
        else:
            segs.append(dict(a=a, b=b, src_end_word=p["end"], pieces=[i], zoom=zoom, lock=tail or zoom, pad=pad))
    # tách khoảng lặng trong câu: mỗi đoạn → nhiều đoạn con nối cứng (chuyển cảnh kiểu cũ chỉ ở ranh giới đoạn gốc)
    phys = []
    for i, s in enumerate(segs):
        parts = [(s["a"], s["b"])] if s["zoom"] else pauses.split(P, s["a"], s["b"])
        for k, (x, y) in enumerate(parts):
            phys.append(dict(a=x, b=y, zoom=s["zoom"], pad=s["pad"] if k == len(parts) - 1 else 0.0,
                             pieces=s["pieces"] if k == 0 else [], first=k == 0, last=k == len(parts) - 1))
    for i, s in enumerate(phys):
        s["h0"] = HALF if i > 0 and s["first"] else 0.0
        s["h1"] = HALF if i < len(phys) - 1 and s["last"] else 0.0
    segs = phys
    args, fc = ["ffmpeg", "-v", "error", "-y"], []
    for i, s in enumerate(segs):
        d = s["b"] - s["a"]
        args += ["-ss", f"{s['a']:.3f}", "-t", f"{d:.3f}", "-i", src]   # tua trước -i: nhanh với video dài, vẫn chính xác khi mã hoá lại
        zf = (f"scale=w='trunc(iw*(1+{ZOOM}*t/{d:.3f})/2)*2':h=-2:eval=frame,crop={VW}:{VH}," if False else "")   # không zoom (13/11/2026 — David: không thẩm mỹ)
        h0, h1 = s["h0"], s["h1"]
        tail = s["pad"] + h1
        vp = (f",tpad=start_mode=clone:start_duration={h0}" if h0 else "") + (f",tpad=stop_mode=clone:stop_duration={tail}" if tail else "")
        blur = f",gblur=sigma=0.5:sigmaV=42:enable='lt(t,{h0})+gte(t,{h0 + d + s['pad']:.3f})'" if h0 or h1 else ""   # nhoè dọc kiểu tua
        ap = (f",adelay={round(h0 * 1000)}:all=1" if h0 else "") + (f",apad=pad_dur={tail}" if tail else "")
        fc.append(f"[{i}:v:0]setpts=PTS-STARTPTS,{zf}format=yuv420p{vp}{blur}[v{i}]")
        fc.append(f"[{i}:a:0]asetpts=PTS-STARTPTS,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
                  f"afade=t=in:d=0.015,afade=t=out:st={max(0, d - 0.03):.4f}:d=0.03{ap}[a{i}]")
    fc.append("".join(f"[v{i}][a{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=1[v][a]")
    out = os.path.join(P, "cat", f"{opt['id']}.mp4"); os.makedirs(os.path.dirname(out), exist_ok=True)
    args += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
             "-c:v", "h264_videotoolbox", "-b:v", "20M", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", out]
    subprocess.run(args, check=True, env=env)
    t, rows, mp, jumps = 0.0, [], [], []
    for j, s in enumerate(segs):
        d = s["b"] - s["a"]; t += s["h0"]                 # clip_start..clip_end = phần có lời của đoạn (không gồm khoảng chuyển)
        mp.append(dict(clip_start=round(t, 3), clip_end=round(t + d, 3), src_start=round(s["a"], 3), src_end=round(s["b"], 3), pad=s["pad"]))
        for k in s["pieces"]:
            p = pcs[k]; rows.append(f"| {k + 1} | {fmt(t + max(0, p['start'] - s['a']))} | {fmt(p['start'])}–{fmt(p['end'])} | {p.get('role', '')} | {p.get('text', '')} |")
        t += d + s["pad"]
        if s["h1"]:
            jumps.append(dict(at=round(t, 3), dur=round(s["h1"] + HALF, 3), src_from=round(s["b"], 3), src_to=round(segs[j + 1]["a"] + PRE, 3)))
        t += s["h1"]
    json.dump(dict(src_duration=round(dur, 3), clip_duration=round(t, 3), segs=mp, jumps=jumps),
              open(os.path.join(P, "cat", f"{opt['id']}-map.json"), "w"), indent=1)
    warn = ""   # độ dài theo ý, không có số cố định (David chốt 2026-11-07)
    _ghep = [f"{fmt(a['end'])} → {fmt(b['start'])}" for a, b in zip(pcs, pcs[1:]) if b["start"] - a["end"] > 30 or b["start"] < a["end"]]
    _chon = ["## Bốn câu chọn ý", *[f"- **{k}:** {_cy[k]}" for k in ("boi_canh", "y_tron", "mang_ve", "chua_lai")], "",
             "## Lời đọc nối", " ".join(p.get("text", "") for p in pcs), ""] + ([f"## Đoạn ghép xa nhau (báo David)", *[f"- {g}" for g in _ghep], ""] if _ghep else [])
    md = [f"# Clip {opt['id']} — {t:.1f} s{warn}", "", f"{len(segs)} đoạn cắt từ nguồn (gồm khoảng lặng trong câu đã rút)", "", *_chon,
          "| # | Mốc clip | Mốc nguồn | Vai | Lời |", "|---|---|---|---|---|", *rows]
    print(f"{out}  {t:.1f}s  {len(segs)} đoạn{warn}")
    if CHECK:
        r, extra, miss = verify(out, " ".join(p.get("text", "") for p in pcs))
        ok = r >= 0.9 and not extra and not miss
        md += ["", f"## Kiểm lời (chép lại bản cắt) — khớp {r:.0%}{'' if ok else ' ⚠'}",
               f"- Chữ thừa (lọt từ câu bên cạnh / Whisper nghe khác): {', '.join(extra) or 'không'}",
               f"- Chữ thiếu (bị cụt / Whisper nghe khác): {', '.join(miss) or 'không'}",
               f"- Lời chép lại: cat/{opt['id']}-kiem.txt"]
        print(f"   kiểm lời: khớp {r:.0%} · thừa: {extra or '—'} · thiếu: {miss or '—'}")
    open(os.path.join(P, "cat", f"{opt['id']}.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
