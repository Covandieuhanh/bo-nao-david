# Xuất bản cuối MP4 (đăng được ngay): render_preview.py <dự án>
# Video gốc + mọi cảnh motion (đè theo thứ tự trong scenes.js) + 5 giây nguồn ảnh (nếu có). Ra <dự án>/video-final.mp4
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import load, node_env

P = os.path.expanduser(sys.argv[1])
d = load(P); pr, scenes, out_ = d["project"], d["scenes"], d["out"]
M = os.path.join(P, "davinci/media")
FPS = f'{pr["fpsNum"]}/{pr["fpsDen"]}'
fr = lambda s: round(s * pr["fpsNum"] / pr["fpsDen"])
credits = os.path.join(M, "nguon_anh.png")
args = ["ffmpeg", "-y", "-v", "error", "-stats", "-i", os.path.join(M, out_["base"])]   # nền: video gốc, hoặc nen_ngang.mp4 (pillar)
# Phụ đề (nếu có) đè trên cùng, chạy từ đầu video
ov = scenes + ([{"id": "phu_de", "start": 0}] if os.path.exists(os.path.join(M, "phu_de.mov")) else [])
for s in ov: args += ["-i", os.path.join(M, s["id"] + ".mov")]
n = len(ov)
fl, prev = ["[0:v:0]setpts=PTS-STARTPTS[b0]"], "b0"
for i, s in enumerate(ov):
    st = fr(s["start"]) * pr["fpsDen"] / pr["fpsNum"]
    fl.append(f"[{i + 1}:v]setpts=PTS-STARTPTS+{st:.6f}/TB[m{i}];[{prev}][m{i}]overlay=eof_action=pass[b{i + 1}]")
    prev = f"b{i + 1}"
# Màn chốt (cta): tiếng "ting" đúng lúc dấu tick nhỏ bật lên (CTA_TICK giây sau đầu cảnh — cta.js)
TICK = float(__import__("re").search(r"CTA_TICK = ([\d.]+)", open(next(p for p in (os.path.join(P, "motion/src/lib/cta.js"), os.path.join(P, "motion/src/cta.js")) if os.path.exists(p))).read()).group(1))     if any(os.path.exists(os.path.join(P, q)) for q in ("motion/src/lib/cta.js", "motion/src/cta.js")) else 1.6
SFXDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets/sfx")
sfx = [(s["start"] + TICK, "ting.wav", 0.55) for s in scenes if s.get("type") == "cta"]
# NHẬN DIỆN chung (brand.json, người dùng chốt 2026-11-04): tiếng ký hiệu kênh đúng lúc hiện tiêu đề mở đầu (cảnh hook đầu tiên;
# podcast không có hook → đầu video)
import json as _bj
BRAND = _bj.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../thu-vien-hinh/brand.json"), encoding="utf-8"))
_hook = next((s for s in scenes if s.get("type") == "hook"), None)
sfx.append(((_hook["start"] if _hook else 0.0), BRAND["sting"], BRAND["stingVol"]))
# Highlight (skill cat-highlight-video, motion/src/highlight.js): tiếng "vút tua" ở mỗi mối nhảy đoạn — đặt giữa khoảng chuyển
# (khoảng chuyển là lặng do cut_highlight.py chèn, nên không đè lời nói)
hlf = os.path.join(P, "motion/src/highlight.js")
if os.path.exists(hlf):
    _t = open(hlf, encoding="utf-8").read().split("export default", 1)[1].strip().rstrip(";")
    if _t != "null":
        import json as _json
        _hl = _json.loads(_t)
        sfx += [(max(0, j["at"] + j["dur"] / 2 - 0.21), "tua.wav", 0.32) for j in _hl["jumps"] if j.get("tone") != "lang"]
A0 = "[0:a]asetpts=PTS-STARTPTS"
# Nhạc nền highlight (highlight.js → music: [{f, a, b, gain}], bài cố định của kênh ở cat-highlight-video/assets/music):
# mỗi bài một khoảng, chồng mờ 0,8 s ở mối, tự hạ khi có lời (sidechaincompress theo tiếng nói) — mức nền ~ −24 dB dưới lời
MUSDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../cat-highlight-video/assets/music")   # cùng bộ dung-video
_mus = [m for m in (locals().get("_hl") or {}).get("music", []) if os.path.exists(os.path.join(MUSDIR, m["f"] + ".mp3"))]
_mv = None; _th = None
# NHẠC THEO TUYẾN NỘI DUNG (David chốt 2026-11-05 — khối 09, hồ sơ chung `nhac`): project.tuyen = vui | tam_su | mat_mat | y_nghia |
# kien_thuc → bài trong bảng. Không ghi tuyến (và không ghi project.music) → DỪNG: không còn mặc định "Upbeat Vlog" cho mọi video
# (podcast tâm sự 2026-11-05 bị gắn nhạc sôi động). project.music = '<bài>' ép tay · '' / null = tắt nhạc.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../khoi")); import hoso as _hoso
NH = _hoso.load("chung").get("nhac", {})
def _pick_music():
    if "music" in pr: return pr["music"] or None
    t = pr.get("tuyen")
    if not t:
        sys.exit("⛔ Thiếu project.tuyen (tuyến nội dung → nhạc nền). Ghi vào motion/src/project.js một trong: "
                 + ", ".join(f"{k} ({v['khi']})" for k, v in NH.get("tuyen", {}).items()) + " — khối 09.")
    row = NH["tuyen"].get(t) or sys.exit(f"⛔ project.tuyen = '{t}' không có trong bảng hồ sơ chung nhac.tuyen")
    if row["bai"]: return row["bai"][0]
    print(f"⚠ tuyến '{t}' chưa có bài riêng — tạm dùng {row['tam']} (chờ David tải bài)"); return row["tam"]
_f = None if _mus else _pick_music()
if not _mus and _f:
    # Video 1 người nói / podcast: nhạc kênh RẤT NHỎ — khoảng trống/mở/kết thấp hơn giọng `khoang_trong_duoi_giong_LU`; khi đang
    # nói nén theo giọng (ngưỡng = giọng − `nen_nguong_duoi_giong_dB`, tỉ lệ `nen_ty_le`, nhả `nen_nha_ms`) → ~30–33 LU dưới giọng (đo 2026-11-05)
    print(f"nhạc nền: {_f} (tuyến {pr.get('tuyen', '—')})")
    _G = {"soi-1": 0.55, "soi-2": 0.5, "lang-1": 1.0, "lang-2": 1.6, "intro-soi": 0.51, "intro-lang": 1.12}
    _o = subprocess.run(["ffmpeg", "-nostats", "-i", os.path.join(M, out_["base"]), "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    _I = [float(x) for x in __import__("re").findall(r"I:\s+(-?[\d.]+) LUFS", _o)]
    _voice = _I[-1] if _I else -20.0
    _mv = 10 ** ((_voice - NH.get("khoang_trong_duoi_giong_LU", BRAND["musicGapLU"]) + 15.5) / 20)
    _th = 10 ** ((_voice - NH.get("nen_nguong_duoi_giong_dB", 14)) / 20)
    _dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(M, out_["base"])],
                                capture_output=True, text=True).stdout)
    _mus = [{"f": _f, "a": 0.0, "b": _dur, "gain": _G.get(_f, 1.0)}]
if _mus:
    XF = 0.8
    for j, m in enumerate(_mus):
        k = len([a for a in args if a == "-i"])
        args += ["-stream_loop", "-1", "-i", os.path.join(MUSDIR, m["f"] + ".mp3")]
        a0 = max(0.0, m["a"] - XF); ln = m["b"] + XF - a0; ms = round(a0 * 1000)
        fi = f",afade=t=in:d={2 * XF if m['a'] > 0 else 0.6}" ; fo = f",afade=t=out:st={ln - 2 * XF:.3f}:d={2 * XF}"
        fl.append(f"[{k}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,atrim=0:{ln:.3f},asetpts=PTS-STARTPTS"
                  f"{fi}{fo},volume={(_mv if _mv is not None else 0.16) * m.get('gain', 1):.4f},adelay={ms}|{ms}[mu{j}]")
    mu = "".join(f"[mu{j}]" for j in range(len(_mus)))
    _scc = (f"sidechaincompress=threshold={_th:.5f}:ratio={NH.get('nen_ty_le', 20)}:attack=20:release={NH.get('nen_nha_ms', 1500)}" if _th
            else "sidechaincompress=threshold=0.03:ratio=6:attack=30:release=450")   # highlight: giữ mức cũ (đã duyệt)
    fl.append(f"{A0},aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,asplit=2[sp0][sp1];"
              f"{mu}amix=inputs={len(_mus)}:duration=longest:normalize=0[mub];"
              f"[mub][sp1]{_scc}[mud];"
              f"[sp0][mud]amix=inputs=2:duration=first:normalize=0[amu]")
    A0 = "[amu]anull"
if sfx:
    for j, (t, name, vol) in enumerate(sfx):
        k = len([a for a in args if a == "-i"])
        args += ["-i", os.path.join(SFXDIR, name)]
        ms = round(t * 1000)
        fl.append(f"[{k}:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms},volume={vol}[td{j}]")
    td = "".join(f"[td{j}]" for j in range(len(sfx)))
    fl.append(f"{A0}[a00];[a00]{td}amix=inputs={len(sfx) + 1}:duration=first:normalize=0[amx]")
    A0 = "[amx]anull"
if os.path.exists(credits):
    kc = len([a for a in args if a == "-i"])   # sau các tiếng hiệu ứng — không cố định n + 1
    args += ["-loop", "1", "-framerate", FPS, "-t", "5", "-i", credits, "-f", "lavfi", "-t", "5", "-i", "anullsrc=r=48000:cl=stereo"]
    fl.append(f"[{prev}]format=yuv420p,setsar=1[vm];[{kc}:v]format=yuv420p,setsar=1,fade=in:st=0:d=0.5[vc]")
    # anullsrc mặc định là u8 (8-bit) → concat hạ CẢ tiếng gốc xuống 8-bit, thêm tiếng rè/xì suốt video. Ép float trước khi nối.
    AF = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
    fl.append(f"{A0},aresample=48000,{AF}[am];[{kc + 1}:a]{AF}[an];[vm][am][vc][an]concat=n=2:v=1:a=1[v][a]")
else:
    fl.append(f"[{prev}]format=yuv420p,setsar=1[v];{A0}[a]")
# Thẻ cuối highlight podcast (the_cuoi.mp4, ~1,8 s — cat-highlight-video luật 13) ghép SAU video, tiếng câm float 48 kHz.
endc = os.path.join(M, "the_cuoi.mp4")
if os.path.exists(endc):
    k = len([a for a in args if a == "-i"])
    ln = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", endc],
                              capture_output=True, text=True).stdout)
    _em = os.path.join(MUSDIR, (_f or "lang-1") + ".mp3")
    if ln > 5 and os.path.exists(_em):   # màn kết YouTube 15–20 s: nhạc kênh nhỏ, vào/ra mềm (không để 20 s im lặng)
        args += ["-i", endc, "-t", f"{ln:.3f}", "-i", _em]
        _eaf = f",volume=0.18,afade=t=in:d=0.8,afade=t=out:st={max(0, ln - 1.5):.2f}:d=1.5"
    else:
        args += ["-i", endc, "-f", "lavfi", "-t", f"{ln:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
        _eaf = ""
    AF = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
    fl[-1] = fl[-1].replace("[v]", "[vpre]").replace("[a]", "[apre]")
    fl.append(f"[vpre]format=yuv420p,setsar=1[vp2];[{k}:v]format=yuv420p,setsar=1,fps={FPS}[ve];[apre]{AF}[ap2];[{k + 1}:a]{AF}{_eaf}[ae];"
              f"[vp2][ap2][ve][ae]concat=n=2:v=1:a=1[v][a]")
# Màn hình bìa (COVER, ~1 s) ghép TRƯỚC video để mạng xã hội lấy làm ảnh bìa: khung đầu = bìa sạch, không phụ đề.
# Tiếng câm ép float 48 kHz (anullsrc mặc định u8 → cả bài bị hạ 8-bit, xem gotchas).
bia = os.path.join(M, "bia.mp4")
if os.path.exists(bia):
    k = len([a for a in args if a == "-i"])
    args += ["-i", bia, "-f", "lavfi", "-t", "1", "-i", "anullsrc=r=48000:cl=stereo"]
    AF = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
    fl[-1] = fl[-1].replace("[v]", "[vmain]").replace("[a]", "[amain]")
    fl.append(f"[{k}:v]format=yuv420p,setsar=1,fps={FPS}[vb];[{k + 1}:a]{AF}[ab];[amain]{AF}[am2];"
              f"[vb][ab][vmain][am2]concat=n=2:v=1:a=1[v][a]")
out = os.path.join(P, "video-final.mp4")
# Độ to đăng mạng xã hội chung cho cả 4 loại: −14 LUFS, đỉnh −1,5 dB (như render-show.mjs của chế độ ghép)
fl.append("[a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
args += ["-filter_complex", ";".join(fl), "-map", "[v]", "-map", "[aout]", "-r", FPS, "-c:v", "libx264", "-preset", "medium",
         "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out]
subprocess.run(args, check=True, env=node_env())
print("done", out)
