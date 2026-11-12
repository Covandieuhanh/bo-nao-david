#!/usr/bin/env python3
"""Tìm lại cuộc trò chuyện cũ với Claude trên Mac này (học từ "session search" của Hermes), không gọi AI.
Tìm trong lịch sử phiên Claude Code (~/.claude/projects/*/*.jsonl): lời David và lời Claude chứa MỌI từ khoá.
In tối đa N đoạn mới nhất: ngày giờ · tên phiên · ai nói · đoạn trích quanh từ khoá.
Dùng: python3 -I tim-phien.py "từ khoá 1" ["từ khoá 2" …] [--so 8] [--ngay 60]"""
import glob, json, os, sys, time

GOC = os.path.expanduser("~/.claude/projects")


def chu(c):
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return " ".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    return ""


def main():
    a = sys.argv[1:]
    so, ngay = 8, 90
    if "--so" in a:
        i = a.index("--so"); so = int(a[i + 1]); del a[i:i + 2]
    if "--ngay" in a:
        i = a.index("--ngay"); ngay = int(a[i + 1]); del a[i:i + 2]
    tu = [x.lower() for x in a if x.strip()]
    if not tu:
        print(__doc__); return
    moc = time.time() - ngay * 86400
    tep = [f for f in glob.glob(f"{GOC}/*/*.jsonl") if os.path.getmtime(f) >= moc]
    kq = []
    for f in tep:
        ten = ""
        for l in open(f, encoding="utf-8", errors="ignore"):
            if '"ai-title"' in l:
                try: ten = json.loads(l).get("aiTitle") or ten
                except Exception: pass
            low = l.lower()
            if not all(x in low for x in tu):
                continue
            try:
                o = json.loads(l)
            except Exception:
                continue
            if o.get("type") not in ("user", "assistant"):
                continue
            s = chu((o.get("message") or {}).get("content")).replace("\n", " ")
            sl = s.lower()
            if not s or not all(x in sl for x in tu) or "system-reminder" in sl[:300]:
                continue
            i = sl.find(tu[0])
            kq.append((o.get("timestamp", "")[:16].replace("T", " "), ten or os.path.basename(f)[:8],
                       "David" if o["type"] == "user" else "Claude", s[max(0, i - 150): i + 250]))
    kq.sort(reverse=True)
    if not kq:
        print("Không tìm thấy."); return
    for t, ten, ai, doan in kq[:so]:
        print(f"- {t} UTC · {ten} · {ai}: …{doan}…")
    if len(kq) > so:
        print(f"(còn {len(kq) - so} đoạn khác; thêm từ khoá cho hẹp lại)")


if __name__ == "__main__":
    main()
