"""Thư viện chung: đọc lời Whisper, làm BẢN LỜI GỌN cho Claude, và TÌM MỐC GIÂY từ câu trích nguyên văn.
Claude chỉ trích câu; mốc giây do đây tìm — Claude không phải dò mốc (trước đây tốn nhiều lượt nhất)."""
import difflib, re, unicodedata
from pathlib import Path


def _giay(x):
    h, m, r = x.strip().split(":"); s, ms = r.replace(".", ",").split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def doc_srt(p):
    out = []
    for khoi in Path(p).read_text(encoding="utf-8").replace("\r", "").split("\n\n"):
        d = [x for x in khoi.split("\n") if x.strip()]
        if len(d) >= 2 and "-->" in d[1]:
            a, b = d[1].split("-->")
            out.append((_giay(a), _giay(b), " ".join(d[2:]).strip()))
    return out


def chuan(s):
    s = unicodedata.normalize("NFC", s.lower().replace("**", ""))
    return re.sub(r"[^\w\s]", " ", s).split()


def tu(words_srt):
    """[(start, end, token)] — mỗi từ Whisper có thể ra 0..n token sau khi chuẩn hoá."""
    out = []
    for a, b, t in doc_srt(words_srt):
        for k in chuan(t):
            out.append((a, b, k))
    return out


def ban_loi(words_srt, transcript_srt, out):
    """Bản lời gọn: mỗi dòng `[giây] câu` theo đoạn Whisper; chữ lấy từ words.srt để trích là khớp mốc."""
    W = doc_srt(words_srt); dong = []
    for a, b, _ in doc_srt(transcript_srt):
        cau = " ".join(t for s, e, t in W if a - 0.01 <= s < b - 0.01).strip()
        if cau:
            dong.append(f"[{a:.1f}] {cau}")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text("\n".join(dong) + "\n", encoding="utf-8")
    return len(dong)


def tim(trich, T, sau=0.0, gan=None, nguong=0.72):
    """Tìm câu trích trong T=tu(). Trả (start, end, độ khớp) hoặc None. `sau`: chỉ tìm sau giây này; `gan`: ưu tiên gần giây này."""
    q = chuan(trich)
    if not q:
        return None
    n = len(q); toks = [t for _, _, t in T]
    hop = []
    for i in range(len(T) - n + 1):
        if T[i][0] < sau - 0.01:
            continue
        if toks[i:i + n] == q:
            hop.append((1.0, i, n))
    if not hop:
        qs = " ".join(q)
        for i in range(len(T)):
            if T[i][0] < sau - 0.01 or (toks[i] != q[0] and (i + n - 1 >= len(T) or toks[i + n - 1] != q[-1])):
                continue
            for m in {n - 1, n, n + 1}:
                if m < 1 or i + m > len(T):
                    continue
                r = difflib.SequenceMatcher(None, qs, " ".join(toks[i:i + m])).ratio()
                if r >= nguong:
                    hop.append((r, i, m))
    if not hop:
        return None
    if gan is not None:
        hop.sort(key=lambda h: (-round(h[0], 2), abs(T[h[1]][0] - gan)))
    else:
        hop.sort(key=lambda h: (-round(h[0], 2), h[1]))
    r, i, m = hop[0]
    return T[i][0], T[i + m - 1][1], round(r, 2)


def bieu_tuong():
    """Mọi tên biểu tượng trong thư viện hình (ICONS của Icons.jsx) — thêm biểu tượng là app tự thấy."""
    f = Path(__file__).resolve().parents[2] / "thu-vien-hinh/Icons.jsx"
    s = f.read_text(encoding="utf-8"); s = s[s.index("export const ICONS = {"):]; s = s[:s.index("\n};")]
    return list(dict.fromkeys(re.findall(r"^\s*'?([a-zA-Z0-9_-]+)'?\s*:", s, re.M)))


def kieu_canh(root_jsx=None):
    """Kiểu cảnh đăng ký trong TYPES của Root.jsx (dự án, hoặc template) — thêm kiểu vào template là app tự nhận."""
    f = Path(root_jsx) if root_jsx else Path(__file__).resolve().parents[2] / "video-style-edit/assets/remotion-template/src/Root.jsx"
    s = re.sub(r"//[^\n]*", "", f.read_text(encoding="utf-8"))
    m = re.search(r"const TYPES = \{(.*?)\};", s, re.S)
    return set(re.findall(r"(?:^|[{,])\s*(\w+)\s*:", m.group(1), re.M)) - {"sides", "captions", "stage", "cover", "endcard"}


def co_trong_loi(text, T, a, b, phu=20.0, them=frozenset()):
    """Tỉ lệ token của `text` có mặt trong lời quanh [a-phu, b+phu] — soát chữ trên màn hình là nguyên văn."""
    q = [t for t in chuan(text) if not t.isdigit()]
    if not q:
        return 1.0
    vung = {t for s, e, t in T if a - phu <= s <= b + phu} | set(them)   # them: chữ đã sửa chính tả (sua_chu), coi như lời thật
    return sum(t in vung for t in q) / len(q)


if __name__ == "__main__":   # loi.py ban-loi <words.srt> <transcript.srt> <ra>
    import sys
    if sys.argv[1] == "ban-loi":
        print(ban_loi(*sys.argv[2:5]), "dòng lời")
