# Đưa mốc nhảy đoạn + thanh tập gốc vào dự án dựng: hl_apply.py <dự án highlight $P> <mã phương án> <dự án dựng $E>
# Đọc $P/cat/<id>-map.json (cut_highlight.py) → ghi $E/motion/src/highlight.js: hiệu ứng tua (Tua.jsx) ở mỗi mối nhảy, thanh
# thời gian của CẢ tập gốc (Timeline.jsx), tiếng "vút tua" (render_preview.py). Chạy sau bước làm sạch / new_podcast.sh vì mốc
# của $E có thể lệch so với clip cắt:
#   - podcast ($E/check/trim.txt "Cắt thừa: đầu Xs") → trừ X
#   - người nói ($E/check/clean/segments.json của clean_apply.py) → quy đổi mốc thô → mốc sạch
# Chạy lại mỗi khi làm sạch lại. In bảng mốc nhảy để đặt cảnh không đè khoảng chuyển.
import json, os, re, sys

P, ID, E = (os.path.expanduser(a) for a in sys.argv[1:4])
m = json.load(open(os.path.join(P, "cat", f"{ID}-map.json")))
tr = os.path.join(E, "check/trim.txt")
segf = os.path.join(E, "check/clean/segments.json")
if os.path.exists(segf):
    cs = json.load(open(segf))
    def conv(t):
        for s in cs:
            if s["raw_start"] <= t <= s["raw_end"]: return s["clean_start"] + t - s["raw_start"]
        nxt = [s for s in cs if s["raw_start"] > t]           # rơi vào đoạn bị cắt → mép đoạn giữ kế tiếp
        return nxt[0]["clean_start"] if nxt else cs[-1]["clean_start"] + cs[-1]["raw_end"] - cs[-1]["raw_start"]
else:
    off = float(re.search(r"đầu ([\d.]+)s", open(tr, encoding="utf-8").read()).group(1)) if os.path.exists(tr) else 0.0
    conv = lambda t: max(0.0, t - off)
r3 = lambda x: round(x, 3)
hl = dict(src_duration=m["src_duration"],
          segs=[dict(s, clip_start=r3(conv(s["clip_start"])), clip_end=r3(conv(s["clip_end"]))) for s in m["segs"]],
          jumps=[dict(j, at=r3(conv(j["at"]))) for j in m["jumps"]])
# Thanh của cả tập gốc chỉ khi cắt kiểu cũ có chuyển cảnh tua (--tua); mặc định (2026-11-04) cắt cứng → thanh thường của clip
hl["bar"] = bool(m["jumps"])
# Tông từng đoạn (phuong-an.json "tone": lang | soi, mặc định soi) → chuyển cảnh lắng không vệt quét/tiếng vút + nhạc nền đổi theo tông
pcs = next(o for o in json.load(open(os.path.join(P, "phuong-an.json"), encoding="utf-8"))["options"] if o["id"] == ID)["pieces"]
tone_of = lambda src: next((p.get("tone", "soi") for p in pcs if p["start"] - 0.5 <= src <= p["end"] + 0.5), "soi")
for s in hl["segs"]: s["tone"] = tone_of(s["src_start"])
for j in hl["jumps"]: j["tone"] = tone_of(j["src_to"])
MUS = {"soi": "soi-1", "lang": "lang-1"}
mus = []
for s in hl["segs"]:
    if mus and mus[-1]["k"] == s["tone"]: mus[-1]["b"] = s["clip_end"]
    else: mus.append(dict(k=s["tone"], a=0.0 if not mus else mus[-1]["b"], b=s["clip_end"]))
GAIN = {"soi-1": 0.55, "soi-2": 0.5, "lang-1": 1.0, "lang-2": 1.6}   # cân về ~ −15 LUFS (xem hl_edl.py)
hl["music"] = [dict(f=MUS[x["k"]], a=x["a"], b=x["b"], gain=GAIN[MUS[x["k"]]]) for x in mus]
# Thẻ cuối dẫn về bản đầy đủ (luật 13): phuong-an.json "endcard": {"title"?, "speaker"?} — trống thì EndCard.jsx lấy STAGE
# (tên tập + người nói gốc). Không có khoá "endcard" (vd. kiểu vòng lặp) → không thẻ cuối.
_plan = json.load(open(os.path.join(P, "phuong-an.json"), encoding="utf-8"))
if isinstance(_plan.get("endcard"), dict):
    hl["endcard"] = dict({k: v for k, v in _plan["endcard"].items() if k in ("title", "speaker", "schedule") and v}, len=1.8)
out = os.path.join(E, "motion/src/highlight.js")
head = open(out, encoding="utf-8").read().split("export default", 1)[0] if os.path.exists(out) else ""
open(out, "w", encoding="utf-8").write(head + "export default " + json.dumps(hl, ensure_ascii=False) + ";\n")
mm = lambda s: f"{int(s // 60)}:{s % 60:04.1f}"
print(f"{out} · tập gốc {mm(hl['src_duration'])} · {len(hl['jumps'])} mối nhảy (đặt cảnh tránh các khoảng này):")
for j in hl["jumps"]: print(f"  {j['at']:6.2f}–{j['at'] + j['dur']:.2f} s → tới {mm(j['src_to'])} tập gốc")
