#!/usr/bin/env python3
"""MÁY CHẠY BƯỚC của app dựng video. App không chứa luật: đọc công thức (cong-thuc/<loại>.json) + phiếu bước (buoc/<id>.json).

  python3 -I chay.py moi <công thức> <video gốc> <tên>   → tạo việc mới ở ~/Movies/_app/<tên>/ rồi chạy
  python3 -I chay.py tiep <tên>                           → chạy tiếp từ bước chưa xong (dừng ở cổng duyệt)
  python3 -I chay.py duyet <tên> [góp ý]                  → duyệt cổng đang chờ (có góp ý → chạy lại bước Claude của cổng)
  python3 -I chay.py lai <tên> <bước>                     → chạy lại từ bước đó trở đi
  python3 -I chay.py xem <tên>                            → in trạng thái

Ba loại bước: co-dinh (chạy lệnh) · claude (goi_claude.py, ra JSON đúng khuôn, có lệnh kiểm) · duyet (dừng chờ David).
Biến trong lệnh: {APP} {DV} {S} {HL} {P} {W} {VIDEO} {TEN} {HO_SO}. Thêm bước = thêm buoc/<id>.json + tên vào công thức, không sửa file này.
"""
import json, os, subprocess, sys, time, glob
from pathlib import Path

APP = Path(__file__).resolve().parent
DV = APP.parent                                   # skills/dung-video
KHO = Path(os.path.expanduser("~/Movies/_app"))   # trạng thái từng việc (sản phẩm, ở lại máy)
ENV = dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", ""))


def doc(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def ghi(p, d):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    tmp = str(p) + ".tmp"
    Path(tmp).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, p)


def cong_thuc(ten):
    return doc(APP / "cong-thuc" / f"{ten}.json")


def phieu(bid):
    if bid.startswith("CONG-"):
        return {"id": bid, "loai": "duyet", "ten": "Cổng duyệt " + bid[5:]} | (doc(APP / "buoc" / f"{bid}.json") if (APP / "buoc" / f"{bid}.json").exists() else {})
    return doc(APP / "buoc" / f"{bid}.json")


def noi_luu(ten):
    """Thư mục dự án mà new_project.sh sẽ tạo (một nguồn: noi_luu.sh của skill)."""
    r = subprocess.run(["zsh", "-c", f'source "{DV}/video-style-edit/scripts/noi_luu.sh"; noi_luu "$1"', "_", ten],
                       capture_output=True, text=True, env=ENV)
    return r.stdout.strip().splitlines()[-1]


def la_ban_da_dung(video):
    """Video đã dựng (có sẵn chữ, dấu góc, thanh thời gian) không được làm video gốc — phủ thêm sẽ chồng hai lớp
    (luật skill: không phủ lên video đã có chữ đốt sẵn). Lỗi gặp 08/11 khi thử bằng clip-C/video-final.mp4."""
    p = str(Path(video).expanduser().resolve())
    mv = str(Path("~/Movies").expanduser().resolve())
    return ("video-final" in Path(p).name or p.startswith(mv + "/_app/")
            or (p.startswith(mv + "/") and any(x in p for x in ("/2-ban-dai/", "/3-highlight/", "/motion/", "/davinci/"))))


TEN_KHUNG = {"giu": "giữ khung gốc", "ngang": "xuất NGANG 1920×1080 từ gốc dọc (video giữa, chữ hai bên — cần SIDES)",
             "doc": "xuất DỌC 1080×1920 từ gốc ngang (bám người nói)"}


def ghi_tuy_chon(W, tc):
    """Tuỳ chọn David chọn khi tạo việc → file chữ cho Claude đọc (yêu cầu của David luôn ưu tiên hơn suy luận)."""
    d = [f"Khung xuất: {TEN_KHUNG.get(tc.get('khung', 'giu'))}",
         f"Thẻ tít mở đầu (hook): {'CÓ — David yêu cầu' if tc.get('hook') else 'không'}",
         f"Lịch phát (ghi lên thẻ cuối): {tc.get('lich') or 'không có'}",
         f"Ảnh minh hoạ: {dict(mac_dinh='chỉ khi cần (mặc định biểu tượng vẽ)', khong='KHÔNG dùng ảnh nào', them='thêm ảnh cho mọi thứ cụ thể').get(tc.get('anh', 'mac_dinh'))}",
         f"Yêu cầu riêng của David: {tc.get('yeu_cau') or 'không có'}"]
    Path(W).mkdir(parents=True, exist_ok=True)
    (Path(W) / "tuy-chon.txt").write_text("\n".join(d) + "\n", encoding="utf-8")


def bien(tt):
    ct = cong_thuc(tt["cong_thuc"]); tc = tt.get("tuy_chon", {})
    return {"APP": str(APP), "DV": str(DV), "S": str(DV / "video-style-edit/scripts"), "HL": str(DV / "cat-highlight-video/scripts"),
            "P": tt["P"], "W": str(KHO / tt["ten"]), "VIDEO": tt["video"], "TEN": tt["ten"], "HO_SO": ct.get("ho_so", "chung"),
            "TAP": str(Path(tt["P"]).parent), "KHUNG": tc.get("khung", "giu"), "HOOK": "co" if tc.get("hook") else "khong"}


def thay(s, b):
    for k, v in b.items():
        s = s.replace("{" + k + "}", v)
    return s


def dieu_kien(ph, b):
    """`khi`: lệnh shell, mã thoát 0 → làm bước này; khác 0 → bỏ qua (vd chỉ làm thumbnail khi video ngang)."""
    if not ph.get("khi"):
        return True
    return subprocess.run(["zsh", "-c", thay(ph["khi"], b)], env=ENV, capture_output=True).returncode == 0


def chay_lenh(lenh, log, cwd=None):
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"\n$ {lenh}\n"); f.flush()
        r = subprocess.run(["zsh", "-c", lenh], stdout=f, stderr=subprocess.STDOUT, env=ENV, cwd=cwd)
    return r.returncode


def mot_buoc(tt, bid, gop_y=None):
    ph = phieu(bid); b = bien(tt)
    W = Path(b["W"]); log = W / "log" / f"{bid}.txt"; log.parent.mkdir(parents=True, exist_ok=True)
    if not dieu_kien(ph, b):
        return "bo-qua"
    if ph["loai"] == "duyet":
        return "cho-duyet"
    if ph["loai"] == "co-dinh":
        lenh = ph["lenh"] if isinstance(ph["lenh"], list) else [ph["lenh"]]
        for l in lenh:
            if chay_lenh(thay(l, b), log, cwd=thay(ph["cwd"], b) if ph.get("cwd") else None) != 0:
                return "loi"
        return "xong"
    if ph["loai"] == "claude":
        cmd = [sys.executable, "-I", str(APP / "goi_claude.py"), str(APP / "buoc" / f"{bid}.json"), json.dumps(b, ensure_ascii=False)]
        if gop_y:
            cmd.append(gop_y)
        with open(log, "a", encoding="utf-8") as f:
            r = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, env=ENV)
        return "xong" if r.returncode == 0 else "loi"
    raise SystemExit(f"loại bước lạ: {ph['loai']}")


def chay(tt_path, tu=None, gop_y=None):
    tt = doc(tt_path)
    ds = cong_thuc(tt["cong_thuc"])["buoc"]
    if tu:
        for x in ds[ds.index(tu):]:
            tt["buoc"].pop(x, None)
    for bid in ds:
        cu = tt["buoc"].get(bid, {}).get("trang_thai")
        if cu in ("xong", "bo-qua", "da-duyet"):
            continue
        tt["dang"] = bid; tt["buoc"][bid] = {"trang_thai": "dang-chay", "luc": time.strftime("%H:%M:%S")}; ghi(tt_path, tt)
        kq = mot_buoc(tt, bid, gop_y if bid == tu else None)
        tt = doc(tt_path)
        tt["buoc"][bid] = {"trang_thai": kq, "luc": time.strftime("%H:%M:%S")}
        ghi(tt_path, tt)
        print(f"[{time.strftime('%H:%M:%S')}] {bid}: {kq}", flush=True)
        if kq in ("loi", "cho-duyet"):
            return kq
    tt["dang"] = None; tt["xong_luc"] = time.strftime("%Y-%m-%d %H:%M"); ghi(tt_path, tt)
    return "xong-het"


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return
    lenh = a[0]
    if lenh == "moi":
        ct, video, ten = a[1], os.path.expanduser(a[2]), a[3]
        if la_ban_da_dung(video):
            raise SystemExit("Video này là bản đã dựng (có sẵn chữ, dấu góc). Chọn video gốc quay từ máy.")
        W = KHO / ten; p = W / "trang-thai.json"
        if p.exists():
            raise SystemExit(f"Đã có việc '{ten}' — dùng: chay.py tiep {ten}")
        tc = json.loads(a[4]) if len(a) > 4 else {}
        ghi(p, {"ten": ten, "cong_thuc": ct, "video": video, "P": noi_luu(ten), "buoc": {}, "tuy_chon": tc,
                "tao_luc": time.strftime("%Y-%m-%d %H:%M")})
        ghi_tuy_chon(W, tc)
        print(chay(p))
    elif lenh == "tiep":
        print(chay(KHO / a[1] / "trang-thai.json"))
    elif lenh == "duyet":
        p = KHO / a[1] / "trang-thai.json"; tt = doc(p); cong = tt.get("dang")
        if not cong or tt["buoc"].get(cong, {}).get("trang_thai") != "cho-duyet":
            raise SystemExit("Không có cổng nào đang chờ duyệt.")
        gop = " ".join(a[2:]).strip()
        if gop:  # góp ý → chạy lại bước Claude mà cổng này duyệt, kèm góp ý
            ph = phieu(cong); lai = ph.get("gop_y_cho")
            if not lai:
                raise SystemExit("Cổng này không nhận góp ý.")
            print(chay(p, tu=lai, gop_y=gop))
        else:
            tt["buoc"][cong] = {"trang_thai": "da-duyet", "luc": time.strftime("%H:%M:%S")}; ghi(p, tt)
            print(chay(p))
    elif lenh == "lai":
        print(chay(KHO / a[1] / "trang-thai.json", tu=a[2]))
    elif lenh == "xem":
        tt = doc(KHO / a[1] / "trang-thai.json")
        for bid in cong_thuc(tt["cong_thuc"])["buoc"]:
            print(f"{tt['buoc'].get(bid, {}).get('trang_thai', '·'):10} {bid}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
