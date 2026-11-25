# Phụ đề đầy đủ (chế độ 1 video): phu-de.py <dự án>
# kiem-tra/goc/moc-tung-tu.srt (mốc từng từ của bản sạch) → chuyen-dong/src/phu-de.js: [{start, end, text}], mỗi dòng phụ đề ≤ ~40 ký tự,
# không vắt dòng qua hai câu. Đây là BẢN NHÁP: Claude đọc lại từng dòng, sửa chính tả lỗi Whisper (tên riêng,
# từ nghe nhầm) nhưng giữ nguyên lời người nói — không rút gọn, không diễn đạt lại.
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

P = os.path.expanduser(sys.argv[1])
MAXC, GAP = 34, 0.45   # ~37 ký tự/dòng ở cỡ 42 px trong vùng an toàn

def srt(path):
    out = []
    for b in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        m = re.search(r"(\d+):(\d+):(\d+)[,.](\d+) --> (\d+):(\d+):(\d+)[,.](\d+)\n(.*)", b, re.S)
        if m:
            g = [int(x) for x in m.groups()[:8]]
            out.append(dict(s=g[0]*3600+g[1]*60+g[2]+g[3]/1000, e=g[4]*3600+g[5]*60+g[6]+g[7]/1000, t=m.group(9)))
    return out

# Khung là từng CÂU của ban-chep-loi.srt (không vắt dòng qua hai câu, và lần chạy theo câu ít bịa đặt hơn lần theo từ);
# mốc trong câu lấy từ moc-tung-tu.srt. Bỏ câu Whisper hay bịa đặt khi im lặng.
BREAK = {"thì", "là", "và", "nhưng", "mà", "để", "nên", "khi", "cho", "với", "về", "rồi", "hay", "hoặc", "vì", "nếu",
         "còn", "tức", "thế", "kiểu", "gọi", "rằng", "của", "trong"}
FAKE = re.compile(r"subscribe|đăng ký kênh|Ghiền Mì Gõ|bỏ lỡ những video|cảm ơn các bạn đã (xem|theo dõi)", re.I)
toks = []
for t in srt(os.path.join(P, "kiem-tra", "goc", "moc-tung-tu.srt")):
    if not t["t"].strip(): continue
    if toks and not t["t"].startswith(" "):        # token không có dấu cách đầu = phần sau của từ trước
        toks[-1]["e"] = t["e"]
    else:
        toks.append(dict(s=t["s"], e=t["e"]))

caps = []
for seg in srt(os.path.join(P, "kiem-tra", "goc", "ban-chep-loi.srt")):
    text = seg["t"].strip()
    if not text or FAKE.search(text): continue
    ws = text.split()
    inside = [w for w in toks if seg["s"] - 0.05 <= w["s"] < seg["e"]]
    if len(inside) == len(ws):                    # khớp số từ → dùng mốc từng từ
        times = [(w["s"], w["e"]) for w in inside]
    else:                                         # không khớp → chia mốc theo số ký tự
        tot = sum(len(w) + 1 for w in ws); acc = 0; times = []
        for w in ws:
            a_ = seg["s"] + (seg["e"] - seg["s"]) * acc / tot; acc += len(w) + 1
            times.append((a_, seg["s"] + (seg["e"] - seg["s"]) * acc / tot))
    # Chia câu thành dòng ≤ MAXC ký tự, dài gần bằng nhau; ưu tiên ngắt sau dấu phẩy hoặc trước từ nối, không tách
    # đôi một từ ghép ("chia | sẻ", "bí | mật" là xấu — tiếng Việt viết rời âm tiết nên phải chọn chỗ ngắt có nghĩa)
    n = max(1, -(-len(text) // MAXC))
    cuts, start = [], 0
    for k in range(1, n):
        ideal = len(text) * k / n
        best, best_sc = None, None
        for i in range(start + 1, len(ws)):
            pos = len(" ".join(ws[:i]))
            if abs(pos - ideal) > len(text) / n * 0.4: continue
            sc = -abs(pos - ideal) / 4
            if ws[i - 1].endswith((",", ".", "?", "!")): sc += 6
            if ws[i].lower() in BREAK: sc += 4
            if best_sc is None or sc > best_sc: best, best_sc = i, sc
        if best: cuts.append(best); start = best
    bounds = [0] + cuts + [len(ws)]
    for a_, b_ in zip(bounds, bounds[1:]):
        caps.append(dict(start=round(times[a_][0], 2), end=round(times[b_ - 1][1], 2), text=" ".join(ws[a_:b_]),
                         first=a_ == 0))
# Giữ dòng trên màn hình tới dòng kế (tối đa thêm 0,6 s) để đỡ nháy
for x, y in zip(caps, caps[1:]):
    x["end"] = round(min(y["start"], x["end"] + 0.6), 2)
if caps: caps[-1]["end"] = round(caps[-1]["end"] + 0.6, 2)
for c in caps:   # viết hoa chữ đầu CÂU (dòng nối tiếp giữ chữ thường)
    if c.pop("first"): c["text"] = c["text"][:1].upper() + c["text"][1:]
dst = os.path.join(P, "chuyen-dong", "src", "phu-de.js")
body = ",\n".join(f"  {{start: {c['start']}, end: {c['end']}, text: {json.dumps(c['text'], ensure_ascii=False)}}}" for c in caps)
open(dst, "w", encoding="utf-8").write(
    "// Phụ đề đầy đủ lời nói (mốc bản sạch) — nháp từ scripts/phu-de.py, Claude sửa chính tả, giữ nguyên lời.\n"
    f"export default [\n{body}\n];\n")
print(dst, len(caps), "dòng")
