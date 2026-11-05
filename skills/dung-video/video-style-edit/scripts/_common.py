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

def node_eval(project, expr):
    """Đọc dữ liệu JS của dự án (project.js / scenes.js) qua node."""
    code = (f"Promise.all([import('./src/project.js'), import('./src/scenes.js'), import('./src/output.js').catch(() => ({{}}))])"
            f".then(([p, s, o]) => console.log(JSON.stringify({expr})))")
    out = subprocess.check_output(["node", "-e", code], cwd=os.path.join(project, "motion"), env=node_env(), stderr=subprocess.DEVNULL)
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
    if "upload.wikimedia.org" not in url or url.lower().endswith((".svg", ".tif", ".tiff")) or "/thumb/" in url:
        return url
    parts = urllib.parse.urlparse(url).path.split("/")
    return "https://upload.wikimedia.org" + "/".join(parts[:3]) + "/thumb/" + "/".join(parts[3:]) + f"/{width}px-{parts[-1]}"

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
