# Hàm dùng chung cho các script Python của quy trình
import json, os, subprocess, urllib.parse

UA = "video-edit-local/1.0"   # không đưa thông tin cá nhân vào User-Agent

def node_env():
    env = dict(os.environ)
    nvm = os.path.expanduser("~/.nvm/versions/node")
    if os.path.isdir(nvm):
        vers = sorted(os.listdir(nvm))
        if vers: env["PATH"] = os.path.join(nvm, vers[-1], "bin") + ":" + env.get("PATH", "")
    env["PATH"] = "/opt/homebrew/bin:" + env["PATH"]
    return env

_MA_HOA = None

def ma_hoa_h264(bitrate="20M"):
    """Tham số ffmpeg mã hoá H.264 hợp với MÁY ĐANG CHẠY — để máy nào kéo GitHub về cũng chạy được, không ghi cứng bộ mã hoá của một máy:
    Mac → h264_videotoolbox · máy có card NVIDIA (Windows WSL, Linux) → h264_nvenc · còn lại → libx264 (chậm hơn nhưng máy nào cũng có).
    Thử mã hoá 1 khung để chắc bộ đó chạy thật (ffmpeg có thể liệt kê nvenc mà máy không có card)."""
    global _MA_HOA
    if _MA_HOA is None:
        _MA_HOA = "libx264"
        for enc in ("h264_videotoolbox", "h264_nvenc"):
            r = subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "color=c=black:s=256x144:d=0.1", "-frames:v", "1",
                                "-c:v", enc, "-f", "null", "-"], capture_output=True, env=node_env())
            if r.returncode == 0:
                _MA_HOA = enc
                break
    if _MA_HOA == "libx264":
        return ["-c:v", "libx264", "-preset", "fast", "-crf", "17"]
    return ["-c:v", _MA_HOA, "-b:v", bitrate]

def node_eval(project, expr):
    """Đọc dữ liệu JS của dự án (du-an.js / canh.js) qua node."""
    code = (f"Promise.all([import('./src/du-an.js'), import('./src/canh.js'), import('./src/dau-ra.js').catch(() => ({{}}))])"
            f".then(([p, s, o]) => console.log(JSON.stringify({expr})))")
    out = subprocess.check_output(["node", "-e", code], cwd=os.path.join(project, "chuyen-dong"), env=node_env(), stderr=subprocess.DEVNULL)
    return json.loads(out)

def load(project):
    """project = khung video gốc (khung thiết kế); out = khung xuất {width, height, base} (= video gốc nếu không đổi khung)."""
    d = node_eval(project, "{project: p.default, scenes: s.SCENES, output: o.default || null}")
    o, pr = d["output"], d["project"]
    d["out"] = dict(width=o["width"], height=o["height"], base=o["base"], layout=o["layout"]) if o else \
        dict(width=pr["width"], height=pr["height"], base=pr["source"], layout=None)
    return d

def nframes(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets",
                                   "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", path], env=node_env()).decode()
    return int(out.strip().split(",")[0])

def wiki_thumb(url, width):
    """Wikimedia chỉ cho phép một số độ rộng ảnh thu nhỏ chuẩn (500, 960, 1280...)."""
    if "upload.wikimedia.org" not in url or url.lower().endswith((".svg", ".tif", ".tiff")) or "/anh-thu-nho/" in url:
        return url
    parts = urllib.parse.urlparse(url).path.split("/")
    return "https://upload.wikimedia.org" + "/".join(parts[:3]) + "/anh-thu-nho/" + "/".join(parts[3:]) + f"/{width}px-{parts[-1]}"

def curl(url, dst, timeout=90):
    """Tải bằng curl (Wikimedia chặn urllib của Python với lỗi 429)."""
    r = subprocess.run(["curl", "-s", "-f", "-L", "-m", str(timeout), "-A", UA, "-o", dst, url])
    if r.returncode != 0 and os.path.exists(dst):
        os.remove(dst)
    return r.returncode == 0

def safe_zone(w, h):
    if h > w:
        return dict(left=70, right=w - 180, top=210, bottom=h - 500)
    return dict(left=round(w * .05), right=round(w * .95), top=round(h * .05), bottom=round(h * .85))

def font_he_thong(dam=True, unicode=False):
    """Font Arial của máy (Pillow): Mac → Windows (WSL2 đọc C:\\Windows\\Fonts) → Linux (ttf-mscorefonts) → DejaVu (báo lệch)."""
    mac = "/System/Library/Fonts/Supplemental/" + ("Arial Unicode.ttf" if unicode else "Arial Bold.ttf" if dam else "Arial.ttf")
    ds = [mac, "/mnt/c/Windows/Fonts/" + ("arialbd.ttf" if dam and not unicode else "arial.ttf"),
          "/usr/share/fonts/truetype/msttcorefonts/" + ("Arial_Bold.ttf" if dam and not unicode else "Arial.ttf"),
          "/usr/share/fonts/truetype/dejavu/" + ("DejaVuSans-Bold.ttf" if dam and not unicode else "DejaVuSans.ttf")]
    for p in ds:
        if os.path.exists(p):
            if "dejavu" in p: print("⚠ Máy này không có Arial → dùng DejaVu, chữ sẽ khác bản Mac (cài: sudo apt install ttf-mscorefonts-installer)")
            return p
    raise FileNotFoundError("không tìm thấy font Arial / DejaVu")
