#!/usr/bin/env python3
# KIỂM VIDEO TRÊN MAC (David 20/11/2026: "cần sắp xếp để tôi tự kiểm tra nhanh hơn cho những lần sau").
# CHỈ ĐỌC, không xoá gì. Với mỗi tập trong ~/Movies (tap-*, vlog/*, video-tu-quay/*):
#   dung lượng · bản render đã nằm trên Drive và đã lên mây chưa · bản gốc (1-goc/) đã có trên Drive chưa · xoá được bao nhiêu.
# "Có trên Drive" = cùng tên hoặc cùng cỡ (đúng từng byte) ở thanh-pham/<tập>/, sao-luu-mac/video/<tập>/, tu-lieu-goc/<tập>/;
# "đã lên mây" = file đó đã có mã của Google Drive (com.google.drivefs.item-id). Xoá vẫn chỉ bằng luu-drive.sh (luật "Giữ Mac nhẹ").
#   python3 tu-dong-hoa/kiem-video-mac.py         → in bảng
#   trang http://localhost:8765/mac                → cùng bảng (xem-ket-qua.py gọi kiem())
import os, subprocess, sys

H0 = os.path.expanduser("~")
MOV = os.environ.get("KIEM_MOVIES") or os.path.join(H0, "Movies")   # KIEM_MOVIES: chỉ để thử script
DRIVE = os.path.join(H0, "Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi")
VID = (".mp4", ".mov", ".m4v", ".mkv")
# thư mục trung gian khi dựng: bản chép nguồn, khung tạm, bản thử — dựng lại được, không tính là "bản render"
TRUNG_GIAN = {"chuyen-dong", "public", "tu-lieu", "tam", "kiem-tra", "cat", "src", "rekhung", "node_modules", "xem-nhe", "9-luu-cu"}
NGUON = ("nguon", "video-goc", "goc", "raw-render", "ban-xuat-tho")   # tên file là bản chép nguồn / bản xuất thô


def du(p):
    t = 0
    for r, ds, fs in os.walk(p):
        for f in fs:
            try: t += os.lstat(os.path.join(r, f)).st_size
            except OSError: pass
    return t


def gb(n): return f"{n / 1e9:.1f} GB" if n >= 1e8 else f"{n / 1e6:.0f} MB"


def len_may(p):   # đã có mã Google Drive = đã lên mây
    try: return b"com.google.drivefs.item-id" in subprocess.run(["xattr", p], capture_output=True).stdout
    except OSError: return False


def chi_muc(rels):   # các file video trên Drive của một tập: {(tên), (cỡ)} → đường dẫn
    ten, co = {}, {}
    for rel in rels:
        b = os.path.join(DRIVE, rel)
        for r, _, fs in os.walk(b):
            for f in fs:
                if f.lower().endswith(VID):
                    p = os.path.join(r, f)
                    try: s = os.stat(p).st_size
                    except OSError: continue
                    ten.setdefault((f, s), p); co.setdefault(s, p)
    return ten, co


def tim(p, idx):
    s = os.stat(p).st_size
    return idx[0].get((os.path.basename(p), s)) or idx[1].get(s)


def phan_loai(tap):
    goc, render = [], []
    for r, ds, fs in os.walk(tap):
        rel = os.path.relpath(r, tap).split(os.sep)
        ds[:] = [d for d in ds if d not in TRUNG_GIAN]
        for f in fs:
            if not f.lower().endswith(VID): continue
            p = os.path.join(r, f)
            if os.path.getsize(p) < 1e6: continue
            if rel[0] == "1-goc": goc.append(p)
            elif not os.path.splitext(f)[0].lower().startswith(NGUON): render.append(p)
    return goc, render


def cac_tap():
    out = []
    for n in sorted(os.listdir(MOV)) if os.path.isdir(MOV) else []:
        p = os.path.join(MOV, n)
        if n.startswith("tap-") and os.path.isdir(p): out.append(n)
        elif n in ("vlog", "video-tu-quay") and os.path.isdir(p):
            out += [f"{n}/{m}" for m in sorted(os.listdir(p)) if os.path.isdir(os.path.join(p, m)) and not m.startswith(".")]
    return out


def kiem():
    rows = []
    co_drive = os.path.isdir(DRIVE)
    for rel in cac_tap():
        tap = os.path.join(MOV, rel); ten = os.path.basename(rel)
        size = du(tap); goc, render = phan_loai(tap)
        idx = chi_muc([f"thanh-pham/{ten}", f"sao-luu-mac/video/{rel}", f"tu-lieu-goc/{ten}"]) if co_drive else ({}, {})
        def an_toan(p):
            d = tim(p, idx); return bool(d) and len_may(d)
        r_ok = [p for p in render if an_toan(p)]; g_ok = [p for p in goc if an_toan(p)]
        thieu_r = [os.path.relpath(p, tap) for p in render if p not in r_ok]
        thieu_g = [os.path.relpath(p, tap) for p in goc if p not in g_ok]
        het = not thieu_r and not thieu_g
        rows.append({"tap": rel, "size": size, "render": len(render), "render_ok": len(r_ok), "goc": len(goc), "goc_ok": len(g_ok),
                     "thieu_render": thieu_r, "thieu_goc": thieu_g,
                     "ket_luan": ("🗑 thư mục trống — xoá tay được" if size < 1e6 and not render and not goc
                                  else "✅ an toàn — chuyển bằng luu-drive.sh là xoá được" if het and (render or goc)
                                  else "🆕 chưa có bản render nào (đang làm?)" if not render and not goc
                                  else "❌ chưa an toàn — còn file chưa lên Drive"),
                     "xoa_duoc": size if het and (render or goc) else 0})
    return {"drive": co_drive, "rows": rows}


def bang(k):
    if not k["drive"]: return "⚠️ Google Drive chưa mở: không kiểm được. Mở app Google Drive rồi chạy lại."
    if not k["rows"]: return "~/Movies không còn tập video nào."
    L = ["| Tập | Dung lượng | Bản render trên Drive | Bản gốc trên Drive | Kết luận |", "|---|---|---|---|---|"]
    for r in k["rows"]:
        L.append(f"| {r['tap']} | {gb(r['size'])} | {r['render_ok']}/{r['render']} | {r['goc_ok']}/{r['goc']} | {r['ket_luan']} |")
    tong = sum(r["xoa_duoc"] for r in k["rows"])
    L.append(f"\nXoá được ngay (chạy luu-drive.sh): **{gb(tong)}**.")
    for r in k["rows"]:
        if r["thieu_render"] or r["thieu_goc"]:
            L.append(f"\n**{r['tap']}** còn thiếu trên Drive:")
            L += [f"- render: {x}" for x in r["thieu_render"][:8]] + [f"- gốc: {x}" for x in r["thieu_goc"][:8]]
    return "\n".join(L)


if __name__ == "__main__":
    print(bang(kiem()))
