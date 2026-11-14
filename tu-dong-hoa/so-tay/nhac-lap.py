#!/usr/bin/env python3
"""Nhắc lặp cho canh-bot.sh: đọc nhac-viec.md, in các lần nhắc lặp tới giờ trong 60 phút qua chưa gửi.
Dạng dòng: "- mỗi ngày 06:00 · …" · "- mỗi thứ 2, thứ 5 07:00 · …" · "- mỗi chủ nhật 18:00 · …" · "- mỗi ngày 15 09:00 · …" (hằng tháng) · "- chỉ ngày 2026-11-15 07:00 · …" (một lần, dùng cho nhắc có thẻ máy).
"hằng"/"hàng" thay "mỗi" cũng được. Dừng: "(đã dừng)" ngay sau "· ".
Nội dung bắt đầu bằng thẻ máy "[THE] …" (vd [HOI-THOI-QUEN]): in trên một dòng, canh-bot gõ vào phiên bot thay vì gửi thẳng.
Dòng kết bằng "+ việc chưa xong": tin nhắc kèm danh sách việc "[ ]" trong danh-sach-viec.md (việc không hạn cũng có), bỏ mục "Thói quen…".
In mỗi lần nhắc một dòng: "<khoá>\t<nội dung>" (xuống dòng trong nội dung thay bằng \x1f); canh-bot gửi xong thì ghi khoá vào .trang-thai/da-nhac-lap.
Dùng: python3 -I nhac-lap.py <nhac-viec.md> <da-nhac-lap> [danh-sach-viec.md]"""
import datetime as dt, os, re, sys

DONG = re.compile(r"^- (?:mỗi|hằng|hàng|chỉ) (.+?) (\d{1,2}):(\d{2}) · (.+)$")
THU = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "hai": 0, "ba": 1, "tư": 2, "năm": 3, "sáu": 4, "bảy": 5}


def khop(spec, ngay):
    s = spec.strip().lower()
    if s in ("ngày", "sáng", "tối", "chiều", "trưa", "đêm"):
        return True
    m = re.fullmatch(r"ngày (\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return ngay == dt.date(*map(int, m.groups()))
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


KEM = "+ việc chưa xong"


def viec_chua_xong(tep, hom_nay):
    """Danh sách việc "[ ]": quá hạn trước, rồi có hạn, rồi không hạn."""
    try:
        dong = open(tep, encoding="utf-8").read().splitlines()
    except (OSError, TypeError):
        return []
    nhom = ([], [], [])
    for d in dong:
        m = re.match(r"^- \[ \] (.+)$", d.strip())
        if not m:
            continue
        phan = [x.strip() for x in m.group(1).split(" · ")]
        ten = phan[0]
        if ten.lower().startswith("thói quen"):
            continue  # thói quen đã có ba khung hỏi thăm riêng
        han = next((x[4:].strip() for x in phan[1:] if x.startswith("hạn ")), "")
        ngay = re.match(r"\d{4}-\d{2}-\d{2}(?: \d{1,2}:\d{2})?", han)
        han = ngay.group() if ngay else han.split(" (")[0]
        if ngay and ngay.group()[:10] < f"{hom_nay:%Y-%m-%d}":
            nhom[0].append(f"• {ten} (quá hạn {han})")
        elif han:
            nhom[1].append(f"• {ten} (hạn {han})")
        else:
            nhom[2].append(f"• {ten} (chưa có hạn)")
    return nhom[0] + nhom[1] + nhom[2]


def main():
    tep, da = sys.argv[1], sys.argv[2]
    tep_viec = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(tep), "danh-sach-viec.md")
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
                tin = nd
                if nd.endswith(KEM):
                    ds = viec_chua_xong(tep_viec, bay.date())
                    tin = nd[: -len(KEM)].rstrip(" ·.") + "\n\n" + (
                        "Việc chưa xong:\n" + "\n".join(ds) if ds else "Không còn việc nào chưa xong.")
                if tin.startswith("["):  # thẻ máy: canh-bot gõ vào phiên bot, phải nằm trên một dòng
                    tin = re.sub(r"\s*\n+\s*", " / ", tin)
                print(f"{khoa}\t{tin.replace(chr(10), chr(31))}")


if __name__ == "__main__":
    main()
