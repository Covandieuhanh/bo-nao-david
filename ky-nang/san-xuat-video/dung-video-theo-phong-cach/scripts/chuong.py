# CHƯƠNG YOUTUBE cho mô tả video (David duyệt 2026-11-04 — học VOV, Trí Tuệ Sáng Suốt, Trinh Pham): chuong.py <dự án>
# Nguồn (theo thứ tự): chuyen-dong/src/canh.js CHAPTERS → TOPICS (podcast) → cảnh `card`/`listItem` có eyebrow/text (1 video)
# → danh-sach-cat.js OVERLAYS `location`/`round` (vlog ghép). Cộng độ dài teaser nếu có (phat-hanh/doan-gioi-thieu.json do doan-gioi-thieu.py ghi).
# Luật YouTube: chương đầu 0:00, ≥ 3 chương, mỗi chương ≥ 10 s. Tên chương = trích lời / tên nơi thật (không bịa đặt).
# Ra phat-hanh/chuong.txt (dán vào mô tả) + in ra màn hình.
import json, os, subprocess, sys
P = os.path.expanduser(sys.argv[1]); M = os.path.join(P, "chuyen-dong")
mont = os.path.exists(os.path.join(M, "src/danh-sach-cat.js")) and not os.path.exists(os.path.join(M, "src/canh.js"))
js = ("import('./src/danh-sach-cat.js').then(m=>console.log(JSON.stringify({o:m.OVERLAYS||[],total:m.TOTAL})))" if mont else
      "import('./src/canh.js').then(m=>console.log(JSON.stringify({c:m.CHAPTERS||[],t:m.TOPICS||[],s:m.SCENES||[]})))")
d = json.loads(subprocess.run(["node", "--input-type=module", "-e", js], cwd=M, capture_output=True, text=True, check=True).stdout)
ch = []
if mont:
    for o in d["o"]:
        if o.get("type") in ("location", "round"):
            ch.append((o["start"], o.get("place") or o.get("text") or ""))
else:
    ch = [(c["at"], c["text"]) for c in d["c"]] or [(t["at"], t["text"].replace("\n", " ")) for t in d["t"]]
    if not ch:
        for s_ in d["s"]:
            pr = s_.get("props") or {}
            if s_.get("type") in ("card", "listItem") and (pr.get("eyebrow") or pr.get("text")):
                ch.append((s_["start"], pr.get("eyebrow") or pr.get("text")))
off = 0.0
tj = os.path.join(P, "phat-hanh/doan-gioi-thieu.json")
if os.path.exists(tj): off = json.load(open(tj))["len"]
nice = lambda x: " ".join(w[:1] + w[1:].lower() for w in x.split()) if x.isupper() else x[:1].upper() + x[1:]   # IN HOA → Hoa Đầu Từ (giữ tên riêng)
ch = sorted((t + off, nice(x.strip())) for t, x in ch if x)
out = [(0.0, "Mở đầu")] if not ch or ch[0][0] > 1 else []
for t, x in ch:
    if out and t - out[-1][0] < 10: continue          # chương < 10 s → gộp vào chương trước
    out.append((0.0 if not out else t, x))
mm = lambda s: f"{int(s // 3600)}:{int(s % 3600 // 60):02d}:{int(s % 60):02d}" if s >= 3600 else f"{int(s // 60)}:{int(s % 60):02d}"
txt = "\n".join(f"{mm(t)} {x}" for t, x in out)
os.makedirs(os.path.join(P, "phat-hanh"), exist_ok=True)
open(os.path.join(P, "phat-hanh/chuong.txt"), "w", encoding="utf-8").write(txt + "\n")
print(txt if len(out) >= 3 else txt + "\n⚠ dưới 3 chương — YouTube không hiện chương; thêm CHAPTERS trong canh.js nếu video đủ dài")
