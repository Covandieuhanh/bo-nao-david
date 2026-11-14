# Tờ duyệt liên kết (chế độ ghép): link_sheet.py <dự án>
# Mỗi đoạn trích dẫn trong edl.js thành 1 hàng: [người nói lúc bắt đầu câu | khung trích dẫn đúng như sẽ render]
# → check/links.jpg, đánh số hàng theo thứ tự trong video (khớp bảng liên kết trong ke-hoach-ghep.md).
# Chạy SAU khi viết edl.js, TRƯỚC khi render — người dùng duyệt tờ này + kế hoạch rồi mới render.
import json, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import node_env

P = os.path.expanduser(sys.argv[1])
M = os.path.join(P, "motion")
ENV = node_env()
cites = json.loads(subprocess.check_output(["node", "-e",
    "import('./src/edl.js').then(m=>console.log(JSON.stringify(m.SEGS.filter(s=>s.cite))))"],
    cwd=M, env=ENV, stderr=subprocess.DEVNULL))
if not cites:
    sys.exit("Chưa có đoạn trích dẫn nào trong edl.js")
mids = [f"{s['start'] + s['dur'] / 2:.2f}" for s in cites]
subprocess.run(["node", "stills.mjs", *mids], cwd=M, env=ENV, check=True, capture_output=True)
tmp = os.path.join(P, "check", "links_tmp"); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
for k, (s, t) in enumerate(zip(cites, mids)):
    face = os.path.join(tmp, f"a{k}.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s['audio']['from'] + 0.3:.2f}", "-i",
                    os.path.join(M, "public", "clips", s["audio"]["clip"] + ".mp4"), "-frames:v", "1",
                    "-vf", "scale=360:-2", "-update", "1", face], check=True, env=ENV)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", face, "-i", os.path.join(P, "check", "stills", f"{t}.jpg"),
                    "-filter_complex", "[1:v]scale=360:-2[b];[0:v][b]hstack=2,pad=iw+20:ih+20:10:10:white",
                    "-update", "1", os.path.join(tmp, f"r{k:02d}.jpg")], check=True, env=ENV)
cols = 1 if len(cites) < 3 else 2
subprocess.run(["ffmpeg", "-v", "error", "-y", "-pattern_type", "glob", "-i", os.path.join(tmp, "r*.jpg"), "-vf",
                f"tile={cols}x{-(-len(cites) // cols)}:color=white", "-update", "1", os.path.join(P, "check", "links.jpg")],
               check=True, env=ENV)
for k, s in enumerate(cites, 1):
    print(f"{k}. {s['audio']['clip']} {s['audio']['from']:.1f}s → {s['clip']} {s['from']:.1f}–{s['to']:.1f}s"
          f" ({s['dur']:.1f}s){'  «' + s['cite']['label'] + '»' if s['cite'].get('label') else ''}")
print(os.path.join(P, "check", "links.jpg"))
