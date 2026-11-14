#!/usr/bin/env python3
"""Dò và sửa lời "ảo" của Whisper (2026-11-10).

Whisper chạy cả file dài đôi khi kẹt vòng: một đoạn 30 s (hoặc cả bài) chỉ còn câu bịa kiểu
"Hãy subscribe cho kênh … để không bỏ lỡ những video hấp dẫn". Lỗi không cố định — chép lại
riêng đoạn đó thường ra đúng lời.

  loi-ao.py kiem <ban-chep-loi.srt>                 → in các đoạn ảo; mã thoát 1 nếu còn ảo
  loi-ao.py sua <am-thanh-16k.wav> <thư mục> [ngôn ngữ] → chép lại riêng từng đoạn ảo (transcript + words)
"""
import os, re, subprocess, sys, tempfile

MODEL = os.path.expanduser("~/whisper-models/ggml-large-v3-turbo.bin")
BIA = re.compile(r"subscribe|đăng ký kênh|ghiền mì gõ|không bỏ lỡ những video", re.I)
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))


def ts(s):
    h, m, r = s.split(":"); return int(h) * 3600 + int(m) * 60 + float(r.replace(",", "."))


def fmt(t):
    t = max(0.0, t); ms = round(t * 1000)
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def doc(p):
    if not os.path.exists(p): return []
    out = []
    for blk in re.split(r"\n\s*\n", open(p, encoding="utf-8").read().strip()):
        ln = blk.strip().splitlines()
        i = next((k for k, l in enumerate(ln) if "-->" in l), None)
        if i is None: continue
        a, b = [ts(x.strip()) for x in ln[i].split("-->")]
        out.append([a, b, " ".join(ln[i + 1:]).strip()])
    return out


def ghi(p, segs):
    with open(p, "w", encoding="utf-8") as f:
        for n, (a, b, t) in enumerate(segs, 1): f.write(f"{n}\n{fmt(a)} --> {fmt(b)}\n {t}\n\n")


def doan_ao(segs):
    """Các khoảng [a, b] bị ảo: câu bịa quen thuộc, câu lặp ≥ 3 lần chiếm >30%, hoặc đoạn ≥ 25 s mà rất ít chữ."""
    if not segs: return [[0.0, None]]
    txt = [s[2] for s in segs]
    lap = {x for x in set(txt) if x and txt.count(x) >= 3 and txt.count(x) / len(txt) > 0.3}
    bad = [[a, b] for a, b, t in segs
           if BIA.search(t) or t in lap or (b - a >= 25 and len(t.split()) < (b - a) * 0.8)]
    gop = []
    for a, b in bad:
        if gop and a - gop[-1][1] < 1: gop[-1][1] = b
        else: gop.append([a, b])
    return gop


def chep(wav, a, b, lang, words):
    """Chép lại riêng [a, b]. Whisper không cố định và nhạy với độ dài đoạn (đo 2026-11-10: đoạn dài đúng
    30/60/90 s ra lời đúng, 29,98 s hay 30,5 s lại bịa) — thử các cửa sổ dài bội số 30 s phủ [a, b],
    tiếng gốc rồi tiếng đã lọc; chỉ giữ câu có điểm giữa nằm trong [a, b]."""
    import math
    k = max(1, math.ceil((b - a) / 30 - 1e-6))
    with tempfile.TemporaryDirectory() as d:
        w = os.path.join(d, "a.wav")
        for loc in ([], ["-af", "highpass=f=120,dynaudnorm"]):
            for n in (k, k + 1, k + 2):
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-t", str(30 * n), "-i", wav, *loc, w],
                               check=True, env=ENV)
                cmd = ["whisper-cli", "-m", MODEL, "-l", lang, "-f", w, "-mc", "0", "-np", "-osrt", "-of", os.path.join(d, "o")]
                if words: cmd[-4:-4] = ["-ml", "1", "-sow"]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=ENV)
                ra = [[x + a, y + a, t] for x, y, t in doc(os.path.join(d, "o.srt"))
                      if t and a - 0.05 <= (x + y) / 2 + a <= b + 0.05]
                if ra and not doan_ao([[x - a, y - a, t] for x, y, t in ra] if not words else gom(ra)):
                    return ra
    return None


def gom(words):
    """Gộp từ thành câu ~ mỗi 8 s để dò ảo trên moc-tung-tu.srt."""
    out = []
    for a, b, t in words:
        if out and a - out[-1][0] < 8: out[-1][1] = b; out[-1][2] += " " + t
        else: out.append([a, b, t])
    return out


def lech(segs, words):
    """Khoảng mà moc-tung-tu.srt không khớp transcript (words ảo riêng)."""
    import difflib
    bad = []
    for a, b, t in segs:
        w = " ".join(x[2] for x in words if a - 0.3 <= (x[0] + x[1]) / 2 <= b + 0.3)
        n = lambda s: re.sub(r"[^\w ]", "", s.lower()).split()
        if difflib.SequenceMatcher(a=n(t), b=n(w), autojunk=False).ratio() < 0.5:
            if bad and a - bad[-1][1] < 1: bad[-1][1] = b
            else: bad.append([a, b])
    return bad


def sua(wav, O, lang="vi"):
    tp, wp = os.path.join(O, "ban-chep-loi.srt"), os.path.join(O, "moc-tung-tu.srt")
    segs, words = doc(tp), doc(wp)
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                         "-of", "csv=p=0", wav], env=ENV))
    hong = []
    for a, b in doan_ao(segs):
        b = dur if b is None else min(dur, b)
        print(f"Lời ảo {fmt(a)}–{fmt(b)} → chép lại riêng đoạn này")
        ra = chep(wav, a, b, lang, False)
        if ra is None: hong.append([a, b]); continue
        segs = sorted([s for s in segs if not a - 0.05 <= (s[0] + s[1]) / 2 <= b + 0.05] + ra)
    for _ in range(3):   # chép lại một khoảng có thể hụt từ ở ranh giới → kiểm lại
        sai = lech(segs, words)
        if not sai: break
        for a, b in sai:
            print(f"Mốc từng từ lệch lời {fmt(a)}–{fmt(b)} → chép lại words đoạn này")
            ra = chep(wav, a, b, lang, True)
            if ra is None: continue
            words = sorted([s for s in words if not a - 0.3 <= (s[0] + s[1]) / 2 <= b + 0.3] + ra)
    hong += lech(segs, words)
    # từ nằm ngoài mọi câu của transcript (vd câu bịa ở đuôi bài) → bỏ
    words = [w for w in words if any(a - 0.3 <= (w[0] + w[1]) / 2 <= b + 0.3 for a, b, _ in segs)]
    ghi(tp, segs); ghi(wp, words)
    for a, b in hong: print(f"⛔ Vẫn còn lời ảo {fmt(a)}–{fmt(b)}")
    return 1 if hong else 0


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "kiem":
        con = doan_ao(doc(sys.argv[2]))
        for a, b in con: print(f"Lời ảo {fmt(a)}–{fmt(b or 0)}")
        sys.exit(1 if con else 0)
    if len(sys.argv) >= 4 and sys.argv[1] == "sua":
        sys.exit(sua(sys.argv[2], sys.argv[3], *(sys.argv[4:5])))
    sys.exit(__doc__)
