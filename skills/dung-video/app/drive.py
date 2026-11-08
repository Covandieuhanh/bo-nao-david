#!/usr/bin/env python3
"""GOOGLE DRIVE TRÊN MAC (Drive for desktop, ~/Library/CloudStorage/GoogleDrive-*): drive.py tim <link> · drive.py moi

Mỗi tệp/thư mục Drive trên Mac mang mã Drive trong thuộc tính mở rộng `com.google.drivefs.item-id#S` — đúng mã trong link chia sẻ
(…/file/d/<mã>/…, …?id=<mã>, …/folders/<mã>). App tìm tệp bằng mã đó: KHÔNG tải qua mạng, KHÔNG cần mở quyền chia sẻ công khai,
chỉ thấy tệp của các tài khoản Drive đã liên kết với Mac. Tệp vừa tải lên từ điện thoại cần vài phút để Drive trên Mac thấy.
"""
import ctypes, json, os, re, sys, time
from pathlib import Path

NHA = Path.home()
DUOI = (".mp4", ".mov", ".m4v", ".mts", ".avi", ".mkv")
_libc = ctypes.CDLL("libc.dylib", use_errno=True)
_libc.getxattr.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_uint32, ctypes.c_int]
_libc.getxattr.restype = ctypes.c_ssize_t


def ma_drive(p):
    """Mã Drive của một tệp/thư mục trên Mac (None nếu không có)."""
    buf = ctypes.create_string_buffer(256)
    n = _libc.getxattr(os.fsencode(str(p)), b"com.google.drivefs.item-id#S", buf, 256, 0, 0)
    return buf.raw[:n].decode() if n > 0 else None


def goc_drive():
    """[(tài khoản, thư mục gốc "Drive của tôi")] của mọi tài khoản Drive đã liên kết."""
    ds = []
    for d in sorted((NHA / "Library/CloudStorage").glob("GoogleDrive-*")):
        tk = d.name.split("-", 1)[1]
        for g in d.iterdir():
            if g.is_dir() and not g.name.startswith("."):
                ds.append((tk, g))
    return ds


def ma_tu_link(link):
    link = link.strip()
    for mau in (r"/file/d/([\w-]{20,})", r"/folders/([\w-]{20,})", r"[?&]id=([\w-]{20,})", r"^([\w-]{25,})$"):
        m = re.search(mau, link)
        if m:
            return m.group(1)
    return None


def tim(link, han=25):
    """Tìm tệp/thư mục có mã trong link. Ưu tiên thư mục Video-goc, rồi cả Drive (dừng sau `han` giây)."""
    ma = ma_tu_link(link)
    if not ma:
        return {"loi": "Không đọc được mã tệp trong link. Dán link dạng drive.google.com/file/d/… hoặc …/folders/…"}
    t0 = time.time(); xem = set()
    thu_tu = [g / "Video-goc" for _, g in goc_drive() if (g / "Video-goc").is_dir()] + [g for _, g in goc_drive()]
    for goc in thu_tu:
        if ma_drive(goc) == ma:
            return {"loai": "thu-muc", "p": str(goc)}
        for d, dirs, files in os.walk(goc):
            if d in xem:
                dirs[:] = []; continue
            xem.add(d)
            dirs[:] = [x for x in dirs if not x.startswith(".")]
            for x in dirs:
                if ma_drive(os.path.join(d, x)) == ma:
                    return {"loai": "thu-muc", "p": os.path.join(d, x)}
            for f in files:
                if f.lower().endswith(DUOI) and ma_drive(os.path.join(d, f)) == ma:
                    return {"loai": "video", "p": os.path.join(d, f)}
            if time.time() - t0 > han:
                return {"loi": "Tìm quá lâu chưa thấy. Tệp có thể chưa đồng bộ về Mac (đợi vài phút) — hoặc bỏ tệp vào thư mục Video-goc cho nhanh."}
    return {"loi": "Chưa thấy tệp này trên Mac. Nếu vừa tải lên từ điện thoại, đợi vài phút cho Drive đồng bộ rồi thử lại; "
                   "tệp phải nằm trong Drive của tài khoản đã liên kết với Mac (" + ", ".join(tk for tk, _ in goc_drive()) + ")."}


def moi(so=8):
    """Video mới nhất trong các thư mục Video-goc của mọi tài khoản Drive."""
    ds = []
    for tk, g in goc_drive():
        vg = g / "Video-goc"
        if not vg.is_dir():
            continue
        for f in vg.rglob("*"):
            if f.suffix.lower() in DUOI and not f.name.startswith("."):
                st = f.stat()
                ds.append({"ten": f.name, "p": str(f), "mb": round(st.st_size / 1048576), "luc": st.st_mtime, "tk": tk.split("@")[0]})
    return sorted(ds, key=lambda x: -x["luc"])[:so]


if __name__ == "__main__":
    print(json.dumps(tim(sys.argv[2]) if sys.argv[1] == "tim" else moi(), ensure_ascii=False, indent=1))
