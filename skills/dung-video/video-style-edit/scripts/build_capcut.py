#!/usr/bin/env python3
"""Dự án CapCut (draft) để người dùng tự chỉnh — CHỈ khi được yêu cầu: build_capcut.py <dự án> [thư mục draft CapCut]
Chạy bằng venv có pycapcut (scripts/capcut_setup.sh). Tạo draft "edit-<tên>" trong thư mục dự án của CapCut:
  track video chính = video_goc.mp4 (bản sạch, có tiếng)
  track "Hieu ung"  = mỗi cảnh một clip <id>.mov (ProRes 4444 nền trong suốt) đặt đúng mốc → kéo, cắt, xoá từng cảnh
  track "Phu de"    = phụ đề là CHỮ CapCut (sửa chữ, font, màu, vị trí ngay trong CapCut), từ motion/src/captions.js
Media được liên kết cứng (hard link, không tốn thêm ổ) vào <draft>/media — CapCut bản App Store chạy sandbox, đọc file
trong thư mục của nó chắc chắn hơn. Kèm $P/phu-de.srt để nhập vào app khác. Mở lại CapCut để thấy dự án."""
import json, os, re, shutil, sys
import pycapcut as cc

P = os.path.expanduser(sys.argv[1]).rstrip("/")
NAME = os.path.basename(P)
CANDS = [os.path.expanduser("~/Library/Containers/com.lemon.lvoverseas/Data/Movies/CapCut/User Data/Projects/com.lveditor.draft"),
         os.path.expanduser("~/Movies/CapCut/User Data/Projects/com.lveditor.draft")]
ROOT = os.path.expanduser(sys.argv[2]) if len(sys.argv) > 2 else \
    next((c for c in CANDS if os.path.isdir(c)), CANDS[0] if os.path.isdir(os.path.expanduser("~/Library/Containers/com.lemon.lvoverseas")) else CANDS[1])
os.makedirs(ROOT, exist_ok=True)

SRC = os.path.join(P, "motion/src")
proj = open(os.path.join(SRC, "project.js")).read()
W = int(re.search(r"width: (\d+)", proj).group(1)); H = int(re.search(r"height: (\d+)", proj).group(1))
FPS = int(re.search(r"fpsNum: (\d+)", proj).group(1)) / int(re.search(r"fpsDen: (\d+)", proj).group(1))
out = re.search(r"^export default \{layout: '(\w+)', width: (\d+), height: (\d+)", open(os.path.join(SRC, "output.js")).read(), re.M) \
    if os.path.exists(os.path.join(SRC, "output.js")) else None
OW, OH = (int(out.group(2)), int(out.group(3))) if out else (W, H)
fr = lambda s: round(s * FPS) / FPS
us = lambda s: int(round(s * 1_000_000))

body = open(os.path.join(SRC, "scenes.js")).read()
scenes = [(m.group(1), float(m.group(2))) for m in re.finditer(r"\{id: '([^']+)', type: '\w+', start: ([\d.]+), end: [\d.]+", body)]
caps = [(float(a), float(b), json.loads(t)) for a, b, t in
        re.findall(r"\{start: ([\d.]+), end: ([\d.]+), text: (\"(?:[^\"\\]|\\.)*\")\}", open(os.path.join(SRC, "captions.js")).read())]

# Phụ đề dạng SRT (dùng cho app khác; CapCut dùng chữ dựng sẵn bên dưới)
ts = lambda s: "%02d:%02d:%02d,%03d" % (int(s // 3600), int(s % 3600 // 60), int(s % 60), int(round(s % 1 * 1000)) % 1000)
open(os.path.join(P, "phu-de.srt"), "w", encoding="utf-8").write(
    "".join(f"{i}\n{ts(fr(a))} --> {ts(fr(b))}\n{t}\n\n" for i, (a, b, t) in enumerate(caps, 1)))

folder = cc.DraftFolder(ROOT)
draft_name = f"edit-{NAME[5:] if NAME.startswith('edit-') else NAME}"
script = folder.create_draft(draft_name, OW, OH, fps=round(FPS), allow_replace=True)
DRAFT = os.path.join(ROOT, draft_name)
MEDIA = os.path.join(DRAFT, "media"); os.makedirs(MEDIA, exist_ok=True)

def bring(src):
    dst = os.path.join(MEDIA, os.path.basename(src))
    if os.path.exists(dst): os.remove(dst)
    try: os.link(src, dst)
    except OSError: shutil.copy2(src, dst)
    return dst

M = os.path.join(P, "davinci/media")
base = os.path.join(M, "nen_ngang.mp4") if out else os.path.join(M, "video_goc.mp4")   # pillar: nền ngang đã ghép
script.add_track(cc.TrackType.video)
vm = cc.VideoMaterial(bring(base))
script.add_segment(cc.VideoSegment(vm, cc.Timerange(0, vm.duration)))
if out:   # nền ngang không có tiếng → lấy tiếng bản sạch
    script.add_track(cc.TrackType.audio)
    am = cc.AudioMaterial(bring(os.path.join(M, "video_goc.mp4")))
    script.add_segment(cc.AudioSegment(am, cc.Timerange(0, am.duration)))

script.add_track(cc.TrackType.video, "Hieu ung", relative_index=1)
missing = []
for sid, start in scenes:
    f = os.path.join(M, f"{sid}.mov")
    if not os.path.exists(f): missing.append(sid); continue
    m = cc.VideoMaterial(bring(f))
    script.add_segment(cc.VideoSegment(m, cc.Timerange(us(fr(start)), m.duration)), "Hieu ung")

# Phụ đề: chữ trắng đậm trên nền đen mờ, ở đáy vùng an toàn (như bản Remotion: đáy y = H − 506 trên khung dọc)
script.add_track(cc.TrackType.text, "Phu de")
cy = (OH - 506 - 60) if OH > OW else OH * 0.86
style = cc.TextStyle(size=6.0, bold=True, align=1, auto_wrapping=True, max_line_width=0.72)
bg = cc.TextBackground(color="#000000", alpha=0.58, round_radius=0.3, height=0.18, width=0.12)
clip = cc.ClipSettings(transform_y=-(cy - OH / 2) / (OH / 2))
for a, b, t in caps:
    a, b = fr(a), fr(b)
    if b <= a: continue
    script.add_segment(cc.TextSegment(t, cc.Timerange(us(a), us(b) - us(a)), style=style, background=bg, clip_settings=clip), "Phu de")

script.save()

# Font phụ đề = font chữ thường của dự án (BODY trong theme.js, đậm) — CapCut không có sẵn → kèm file TTF (Google Fonts)
# vào <draft>/fonts, trỏ mọi chữ phụ đề tới file đó, và cài vào ~/Library/Fonts để chọn được trong danh sách font của CapCut.
family = re.search(r"BODY = '\"([^\"]+)\"", open(os.path.join(SRC, "theme.js")).read()).group(1)
fname = family.replace(" ", "") + "-Bold.ttf"
cache = os.path.expanduser(f"~/.cache/video-style-edit/fonts/{fname}")
if not os.path.exists(cache):
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    url = f"https://raw.githubusercontent.com/google/fonts/main/ofl/{family.replace(' ', '').lower()}/{fname}"
    os.system(f"curl -sSfL -o '{cache}' '{url}'")
font_file = None
if os.path.exists(cache):
    os.makedirs(os.path.join(DRAFT, "fonts"), exist_ok=True)
    font_file = os.path.join(DRAFT, "fonts", fname); shutil.copy2(cache, font_file)
    user_font = os.path.expanduser(f"~/Library/Fonts/{fname}")
    if not os.path.exists(user_font): shutil.copy2(cache, user_font)
else:
    print(f"⚠ Không tải được font {family} — phụ đề dùng font mặc định của CapCut")

# CapCut bản Mac (App Store, sandbox):
#  - mở dự án bằng draft_info.json (draft_content.json chỉ bản Windows đọc) → ghi cả hai
#  - tự thấy thư mục của nó là /Users/<tên>/Movies/CapCut/... (không phải đường dẫn thật trong ~/Library/Containers)
#    → mọi đường dẫn media/font viết theo dạng đó, giống file CapCut tự tạo (root_meta_info.json)
CONTAINER = os.path.expanduser("~/Library/Containers/com.lemon.lvoverseas/Data")
seen = lambda p: (os.path.expanduser("~") + p[len(CONTAINER):]) if p and p.startswith(CONTAINER) else p
dc = os.path.join(DRAFT, "draft_content.json")
d = json.load(open(dc))
for t in d["materials"]["texts"]:
    if not font_file: break
    c = json.loads(t["content"])
    for st in c["styles"]: st["font"] = {"id": "", "path": seen(font_file)}
    t["content"] = json.dumps(c, ensure_ascii=False)
    t.update(font_path=seen(font_file), font_name=family, font_title=family, font_id="", font_resource_id="")
for kind in ("videos", "audios"):
    for m in d["materials"].get(kind, []):
        m["path"] = seen(m.get("path"))
if sys.platform == "darwin":
    ver = os.popen("defaults read /Applications/CapCut.app/Contents/Info.plist CFBundleShortVersionString 2>/dev/null").read().strip() or "9.5.0"
    for k in ("platform", "last_modified_platform"):
        d[k].update(os="mac", app_version=ver)
for f in ("draft_content.json", "draft_info.json"):
    json.dump(d, open(os.path.join(DRAFT, f), "w"), ensure_ascii=False)
# Ảnh bìa + thông tin dự án theo đường dẫn CapCut thấy
os.system(f"ffmpeg -v error -y -ss 1 -i '{base}' -frames:v 1 -vf scale=360:-2 '{os.path.join(DRAFT, 'draft_cover.jpg')}'")
mp = os.path.join(DRAFT, "draft_meta_info.json")
meta = json.load(open(mp))
try:   # CapCut đã ghi nhận dự án cùng tên (root_meta_info.json) → giữ mã cũ để nó nhận đúng dự án
    known = [x for x in json.load(open(os.path.join(ROOT, "root_meta_info.json")))["all_draft_store"] if x.get("draft_name") == draft_name]
    if known: meta["draft_id"] = known[0]["draft_id"]
except Exception: pass
meta.update(draft_fold_path=seen(DRAFT), draft_root_path=seen(ROOT), draft_name=draft_name, draft_cover="draft_cover.jpg",
            tm_duration=d["duration"])
json.dump(meta, open(mp, "w"), ensure_ascii=False)
if font_file: print(f"Font phụ đề: {family} Bold ({font_file})")
print(f"Draft: {DRAFT}")
print(f"{len(scenes) - len(missing)} clip hiệu ứng, {len(caps)} dòng phụ đề" + (f" — THIẾU clip: {', '.join(missing)}" if missing else ""))
print(os.path.join(P, "phu-de.srt"))
