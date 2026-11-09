#!/usr/bin/env python3
"""HẠN MỨC + TÀI KHOẢN CLAUDE CỦA APP (David muốn 09/11/2026: chỉ dùng app vẫn tự cân đối được; đổi tài khoản Claude vẫn dùng được).
- Hạn mức: lệnh `/usage` của Claude Code chạy ngầm (0 token) → % đã dùng của phiên 5 giờ + cả tuần, giờ mở lại. Tính cả phần dùng
  ngoài app (chat). Máy chủ giao diện tự hỏi mỗi 5 phút; mỗi bước AI cũng ghi số mới từ `rate_limit_event` của chính lần gọi đó.
- Tài khoản: `claude auth status` (email, gói). Đổi tài khoản: đăng xuất rồi `claude auth login` mở trang đăng nhập trên trình duyệt —
  David tự đăng nhập, app không thấy mật khẩu. App dùng lệnh `claude` của máy nên chạy bằng đúng tài khoản đang đăng nhập.
Lưu ở ~/Movies/_app/_han-muc.json · _tai-khoan.json.
  python3 -I han_muc.py lam-moi | tai-khoan
"""
import json, os, re, subprocess, sys, time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

KHO = Path(os.path.expanduser("~/Movies/_app")); F = KHO / "_han-muc.json"; TK = KHO / "_tai-khoan.json"
THANG = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def _claude():
    sys.path.insert(0, str(Path(__file__).parent)); import goi_ai
    return goi_ai.tim_claude(), goi_ai.ENV


def _ghi(f, d):
    KHO.mkdir(parents=True, exist_ok=True)
    tmp = f.with_suffix(".tmp"); tmp.write_text(json.dumps(d, ensure_ascii=False)); os.replace(tmp, f)


def ghi(su_kien):
    """Từ dòng rate_limit_event của một lần gọi AI. Chỉ cập nhật khung có trong sự kiện, giữ phần khác."""
    info = su_kien.get("rate_limit_info") or {}
    win = info.get("unifiedWindows") or ({info["rateLimitType"]: info} if info.get("rateLimitType") else {})
    d = doc() or {}
    for k, v in win.items():
        if k in ("five_hour", "seven_day"):
            d[k] = {"dung": round(float(v.get("utilization", 0)) * 100), "mo_lai": v.get("resetsAt"), "trang_thai": v.get("status")}
    if win:
        d["luc"] = int(time.time()); _ghi(F, d)


def doc_dong(dong):
    try:
        d = json.loads(dong)
    except ValueError:
        return None
    if d.get("type") == "rate_limit_event":
        ghi(d)
    return d


def doc():
    try:
        return json.loads(F.read_text())
    except Exception:
        return None


def _gio(chu, tz):
    """'Nov 10 at 3:10am' | 'Nov 13 at 1pm' | '3:10am' → giây epoch (giờ theo múi tz Claude in ra)."""
    m = re.search(r"(?:([A-Za-z]{3})\w* (\d{1,2}) at )?(\d{1,2})(?::(\d{2}))?\s*(am|pm)", chu, re.I)
    if not m:
        return None
    mon, day, h, mi, ap = m.groups()
    h = int(h) % 12 + (12 if ap.lower() == "pm" else 0)
    now = datetime.now(ZoneInfo(tz))
    dt = now.replace(month=THANG.get((mon or "").lower()[:3], now.month), day=int(day) if day else now.day, hour=h, minute=int(mi or 0),
                     second=0, microsecond=0)
    if dt < now.replace(second=0, microsecond=0) and not mon:
        dt = dt.replace(day=dt.day + 1) if dt.day < 28 else dt
    return int(dt.timestamp())


def lam_moi():
    """Hỏi `/usage` (0 token). Trả bản ghi mới; lỗi thì giữ bản cũ."""
    claude, env = _claude()
    r = subprocess.run([claude, "-p", "--output-format", "json", "--tools", "", "--setting-sources", "", "--no-session-persistence"],
                       input="/usage", capture_output=True, text=True, timeout=90, cwd=str(KHO), env=env)
    try:
        chu = json.loads(r.stdout).get("result", "")
    except Exception:
        return doc()
    d = doc() or {}
    for khoa, nhan in (("five_hour", r"Current session"), ("seven_day", r"Current week \(all models\)")):
        m = re.search(nhan + r":\s*(\d+)% used(?:\s*·\s*resets ([^\n(]+)\(([^)]+)\))?", chu)
        if m:
            d[khoa] = {"dung": int(m.group(1)), "mo_lai": _gio(m.group(2) or "", m.group(3) or "Asia/Ho_Chi_Minh"), "trang_thai": None}
    if "five_hour" in d or "seven_day" in d:
        d["luc"] = int(time.time()); d["nguon"] = "usage"; _ghi(F, d)
    return doc()


def tai_khoan(moi=False):
    """{email, goi, dang_nhap} — đọc lại khi được yêu cầu hoặc bản lưu cũ hơn 60 s."""
    try:
        cu = json.loads(TK.read_text())
        if not moi and time.time() - cu.get("luc", 0) < 60:
            return cu
    except Exception:
        cu = None
    claude, env = _claude()
    r = subprocess.run([claude, "auth", "status"], capture_output=True, text=True, timeout=30, env=env)
    try:
        s = json.loads(r.stdout)
        d = {"dang_nhap": bool(s.get("loggedIn")), "email": s.get("email"), "goi": s.get("subscriptionType") or s.get("planTier"),
             "cach": s.get("authMethod"), "luc": int(time.time())}
    except Exception:
        d = {"dang_nhap": False, "email": None, "goi": None, "luc": int(time.time())}
    _ghi(TK, d)
    return d


DANG_NHAP = {"p": None}


def doi_tai_khoan():
    """Đăng xuất rồi mở trang đăng nhập Claude trên trình duyệt (David tự đăng nhập). Không chặn máy chủ."""
    claude, env = _claude()
    p = DANG_NHAP.get("p")
    if p and p.poll() is None:
        return {"ok": True, "dang_cho": True}
    subprocess.run([claude, "auth", "logout"], capture_output=True, text=True, timeout=30, env=env)
    KHO.mkdir(parents=True, exist_ok=True)
    DANG_NHAP["p"] = subprocess.Popen([claude, "auth", "login", "--claudeai"], stdin=subprocess.DEVNULL,
                                      stdout=open(KHO / "_dang-nhap.log", "w"), stderr=subprocess.STDOUT, env=env, start_new_session=True)
    TK.unlink(missing_ok=True); F.unlink(missing_ok=True)   # số của tài khoản cũ không còn đúng
    return {"ok": True, "dang_cho": True}


def dang_cho_dang_nhap():
    p = DANG_NHAP.get("p")
    return bool(p and p.poll() is None)


if __name__ == "__main__":
    a = sys.argv[1:]
    print(json.dumps(lam_moi() if a == ["lam-moi"] else tai_khoan(True) if a == ["tai-khoan"] else doc(), ensure_ascii=False))
