#!/usr/bin/env python3
"""Nhắc lặp cho canh-bot.sh: đọc nhac-viec.md, in các lần nhắc lặp tới giờ trong 60 phút qua chưa gửi.
Dạng dòng: "- mỗi ngày 06:00 · …" · "- mỗi thứ 2, thứ 5 07:00 · …" · "- mỗi chủ nhật 18:00 · …" · "- mỗi ngày 15 09:00 · …" (hằng tháng).
"hằng"/"hàng" thay "mỗi" cũng được. Dừng: "(đã dừng)" ngay sau "· ".
In mỗi lần nhắc một dòng: "<khoá>\t<nội dung>"; canh-bot gửi xong thì ghi khoá vào .trang-thai/da-nhac-lap.
Dùng: python3 -I nhac-lap.py <nhac-viec.md> <da-nhac-lap>"""
import datetime as dt, re, sys

DONG = re.compile(r"^- (?:mỗi|hằng|hàng) (.+?) (\d{1,2}):(\d{2}) · (.+)$")
THU = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "hai": 0, "ba": 1, "tư": 2, "năm": 3, "sáu": 4, "bảy": 5}


def khop(spec, ngay):
    s = spec.strip().lower()
    if s in ("ngày", "sáng", "tối", "chiều", "trưa", "đêm"):
        return True
    m = re.fullmatch(r"ngày (\d{1,2})", s)
    if m:
        return ngay.day == int(m.group(1))
    thu = set()
    for p in re.split(r"\s*(?:,|và)\s*", s):
        p = p.strip()
        if p in ("chủ nhật", "cn"):
            thu.add(6)
        elif p.startswith("thứ "):
            k = p[4:].strip()
            if k in THU:
                thu.add(THU[k])
            else:
                return False
        elif p:
            return False
    return ngay.weekday() in thu


def main():
    tep, da = sys.argv[1], sys.argv[2]
    try:
        dong = open(tep, encoding="utf-8").read().splitlines()
    except OSError:
        return
    try:
        da_gui = set(open(da, encoding="utf-8").read().splitlines())
    except OSError:
        da_gui = set()
    bay = dt.datetime.now().replace(second=0, microsecond=0)
    for d in dong:
        m = DONG.match(d.strip())
        if not m or m.group(4).startswith("(đã "):
            continue
        spec, h, p, nd = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        for lui in (0, 1):  # hôm nay và hôm qua (khoảng 60 phút vắt qua nửa đêm)
            ngay = bay.date() - dt.timedelta(days=lui)
            luc = dt.datetime.combine(ngay, dt.time(h % 24, p % 60))
            if not (bay - dt.timedelta(minutes=60) <= luc <= bay) or not khop(spec, ngay):
                continue
            khoa = f"{luc:%Y-%m-%d %H:%M} | {nd}"
            if khoa not in da_gui:
                print(f"{khoa}\t{nd}")


if __name__ == "__main__":
    main()
