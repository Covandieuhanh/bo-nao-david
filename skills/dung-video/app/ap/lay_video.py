#!/usr/bin/env python3
"""LẤY VIDEO GỐC VỀ MAC (trước Tạo dự án): lay_video.py <W>

Video trên Google Drive (~/Library/CloudStorage) thường chỉ là "bản trên mây": lệnh `cp` của skill gặp lỗi
`fcopyfile failed: Resource deadlock avoided` và để lại tệp 0 byte (lỗi 08/11/2026, việc img-2858). Bước này ĐỌC tệp theo từng phần
(Drive tự tải về), ghi thẳng vào ~/Movies/tap-<tên>/1-goc/ (đúng chỗ skill để file gốc), kiểm đủ dung lượng + ffprobe mở được,
rồi ghi `video_may` vào trạng thái để các bước sau dùng bản trên Mac. Video vốn nằm trên Mac thì chỉ kiểm, không chép.
"""
import ctypes, json, os, subprocess, sys, time
from pathlib import Path

# Tiến trình chạy nền (app tự chạy bằng LaunchAgent) mặc định KHÔNG được kéo tệp "chỉ trên mây" về → EDEADLK "Resource deadlock
# avoided". Xin bật cho tiến trình này: setiopolicy_np(IOPOL_TYPE_VFS_MATERIALIZE_DATALESS_FILES=3, IOPOL_SCOPE_PROCESS=0, ON=2).
try:
    ctypes.CDLL("libc.dylib").setiopolicy_np(3, 0, 2)
except Exception:
    pass

W = Path(sys.argv[1]); f = W / "trang-thai.json"
tt = json.loads(f.read_text(encoding="utf-8"))
if tt.get("tuy_chon", {}).get("videos"):   # GHÉP VLOG: nhiều clip — clip trên Drive tải về W/goc/, clip trên Mac giữ nguyên
    ra = []
    for v in tt["tuy_chon"]["videos"]:
        v = Path(v)
        if "/Library/CloudStorage/" in str(v):
            d = W / "goc" / v.name; d.parent.mkdir(exist_ok=True)
            if not (d.exists() and d.stat().st_size == v.stat().st_size):
                try:
                    ctypes.CDLL("libc.dylib").setiopolicy_np(3, 0, 2)
                except Exception:
                    pass
                with open(v, "rb") as a, open(d, "wb") as b:
                    while True:
                        k = a.read(8 << 20)
                        if not k: break
                        b.write(k)
                if d.stat().st_size != v.stat().st_size: raise SystemExit(f"Tải chưa đủ: {v.name}")
            print(f"✓ {v.name} (từ Drive)"); ra.append(str(d))
        else:
            print(f"✓ {v.name}"); ra.append(str(v))
    tt["videos_may"] = ra; f.write_text(json.dumps(tt, ensure_ascii=False, indent=1), encoding="utf-8"); sys.exit(0)
nguon = Path(tt["video"]); tap = Path(tt["P"]).parent
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))


def mo_duoc(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True, env=ENV)
    try:
        if float(r.stdout.strip()) > 0: return True
    except ValueError:
        pass
    # WAV ghi âm có khi không ghi tổng thời lượng ở đầu tệp (N/A) — vẫn hợp lệ nếu có luồng tiếng/hình và giải mã được 1 giây
    r = subprocess.run(["ffmpeg", "-v", "error", "-t", "1", "-i", str(p), "-f", "null", "-"], capture_output=True, text=True, env=ENV)
    q = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(p)], capture_output=True, text=True, env=ENV)
    return r.returncode == 0 and bool(q.stdout.strip())


if not nguon.exists():
    raise SystemExit(f"Không thấy video gốc: {nguon}")
if nguon.is_dir():   # nguồn là thư mục dự án bản dài (highlight) — dùng bản sạch trong đó, không cần tải
    print(f"Nguồn là dự án bản dài: {nguon}"); sys.exit(0)
if "/Library/CloudStorage/" not in str(nguon):
    if not mo_duoc(nguon): raise SystemExit(f"Video gốc không mở được (hỏng hoặc chưa ghi xong): {nguon}")
    print(f"Video đã nằm trên Mac: {nguon}"); sys.exit(0)

dich = tap / "1-goc" / nguon.name; dich.parent.mkdir(parents=True, exist_ok=True)
can = nguon.stat().st_size
if dich.exists() and dich.stat().st_size == can and mo_duoc(dich):
    print(f"Đã có bản trên Mac: {dich}")
else:
    tam = dich.with_name("." + dich.name + ".dang-tai"); t0 = time.time(); da = 0
    print(f"Tải từ Drive về Mac: {nguon.name} ({can / 1048576:.0f} MB)…", flush=True)
    for lan in range(1, 4):                                  # Drive đôi khi ngắt giữa chừng → thử lại tối đa 3 lần
        try:
            with open(nguon, "rb") as a, open(tam, "wb") as b:
                while True:
                    k = a.read(8 << 20)
                    if not k: break
                    b.write(k); da += len(k)
            break
        except OSError as e:
            print(f"  lần {lan} lỗi: {e} — thử lại", flush=True); time.sleep(5); da = 0
    if not tam.exists() or tam.stat().st_size != can:
        tam.unlink(missing_ok=True)
        raise SystemExit(f"Tải chưa đủ ({(tam.stat().st_size if tam.exists() else 0) / 1048576:.0f}/{can / 1048576:.0f} MB). "
                         "Kiểm mạng / Drive trên Mac rồi bấm làm lại bước này.")
    os.replace(tam, dich)
    if not mo_duoc(dich):
        raise SystemExit("Tải đủ dung lượng nhưng video không mở được — tệp trên Drive có thể chưa tải lên xong từ điện thoại.")
    print(f"Xong trong {time.time() - t0:.0f} s → {dich}")

tt = json.loads(f.read_text(encoding="utf-8")); tt["video_may"] = str(dich)
f.write_text(json.dumps(tt, ensure_ascii=False, indent=1), encoding="utf-8")
