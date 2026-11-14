#!/usr/bin/env python3
"""BỘ MẪU CHUẨN — chạy sau MỖI lần sửa khối / thư viện hình / hồ sơ (đợt 4, 2026-11-04).
  python3 -I kiem-mau.py [tên mẫu …] [--chot]
Với mỗi mẫu trong mau.json: dựng lại dự án mẫu bằng KHUNG DỰNG + THƯ VIỆN + HỒ SƠ hiện tại (chép template mới, giữ dữ liệu cũ của dự
án: lời, kịch bản, mốc), chụp các khung cố định, ghép tờ `<tên>/moi.jpg`, so với `<tên>/chuan.jpg` (SSIM; < 0,97 = có thay đổi hình
→ mở 2 tờ xem có đúng ý không). `--chot` = nhận bản mới làm chuẩn. Không đụng dự án gốc (làm trong thư mục tạm)."""
import json, os, re, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.realpath(__file__)); D = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(D, "mo-dun")); import ho_so as hoso
ENV = dict(os.environ, PATH="/opt/homebrew/bin:" + os.environ.get("PATH", ""))
TPL = {"remotion": os.path.join(D, "dung-video-theo-phong-cach/assets/remotion-template"), "montage": os.path.join(D, "dung-video-theo-phong-cach/assets/montage-template")}
DATA = {"remotion": ["phu-de.js", "canh.js", "du-an.js", "vi-tri.js", "nguoi-noi.js", "duong-bao-am.js", "doan-noi-bat.js", "dau-ra.js"],
        "montage": ["danh-sach-cat.js", "nang-lop.js"]}
args = [a for a in sys.argv[1:] if not a.startswith("--")]; CHOT = "--chot" in sys.argv
run = lambda *c, **k: subprocess.run(list(c), check=True, env=ENV, **k)
def link_tree(src, dst):
    for root, _, files in os.walk(src):
        rd = os.path.join(dst, os.path.relpath(root, src)); os.makedirs(rd, exist_ok=True)
        for f in files:
            s, t = os.path.join(root, f), os.path.join(rd, f)
            try: os.link(os.path.realpath(s), t)
            except OSError: shutil.copy2(s, t)
def sheet(imgs, out, w=360):
    ins = sum((["-i", i] for i in imgs), [])
    fl = ";".join(f"[{k}]scale={w}:-2,pad={w}:ih:0:0[s{k}]" for k in range(len(imgs))) + ";" + "".join(f"[s{k}]" for k in range(len(imgs))) + f"hstack=inputs={len(imgs)}"
    run("ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fl, "-frames:v", "1", out)
res = []
for m in json.load(open(os.path.join(HERE, "mau.json"), encoding="utf-8")):
    if args and m["ten"] not in args: continue
    P = os.path.expanduser(m["du_an"]); W = tempfile.mkdtemp(prefix=f"mau-{m['ten']}-"); M = os.path.join(W, "motion")
    shutil.copytree(TPL[m["khung"]], M, symlinks=False)          # bản thật thư viện hình (src/lib)
    for f in DATA[m["khung"]]:
        s = os.path.join(P, "motion/src", f)
        if os.path.exists(s): shutil.copy2(s, os.path.join(M, "src", f))
    hoso.dump(m["loai"], os.path.join(M, "src/hoso.json"))
    os.symlink(os.path.join(P, "motion/node_modules"), os.path.join(M, "node_modules"))
    if os.path.isdir(os.path.join(P, "motion/public")): link_tree(os.path.join(P, "motion/public"), os.path.join(M, "public"))
    for extra in m.get("them_canh", []):
        p = os.path.join(M, "src/canh.js"); s = open(p, encoding="utf-8").read()
        s = s.replace("export const SCENES = [\n", "export const SCENES = [\n  " + extra + ",\n", 1); open(p, "w", encoding="utf-8").write(s)
    imgs = []
    if m["khung"] == "remotion":
        os.makedirs(os.path.join(W, "davinci"), exist_ok=True); os.symlink(os.path.join(P, "davinci/media"), os.path.join(W, "davinci/media"))
        shots = [f"{i}@{t}" for i, t in m["chup"]] + [f"phu-de@{t}" for _, t in m["chup"]]
        run("node", "xem-truoc.mjs", *shots, cwd=M, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pod = "podcast: true" in open(os.path.join(M, "src/du-an.js")).read()
        base_v = os.path.join(P, "davinci/media/video_goc.mp4")
        for i, t in m["chup"]:
            o = os.path.join(W, f"{i}@{t}.jpg"); ov = os.path.join(W, "check/motion", f"{i}@{t}.png"); pd = os.path.join(W, "check/motion", f"phu-de@{t}.png")
            if pod or not os.path.exists(base_v):
                bg = os.path.join(W, "check/motion", f"nen@{t}.png")
                if not os.path.exists(bg): run("node", "xem-truoc.mjs", f"nen@{t}", cwd=M, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                run("ffmpeg", "-v", "error", "-y", "-i", bg, "-i", ov, "-i", pd, "-filter_complex", "[0][1]overlay[a];[a][2]overlay", "-frames:v", "1", o)
            else:
                run("ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", base_v, "-i", ov, "-i", pd, "-filter_complex",
                    "[1]scale=iw:ih[o];[0][o]scale2ref[b][o2];[b][o2]overlay[a];[a][2]overlay", "-frames:v", "1", o)
            imgs.append(o)
    else:
        run("node", "anh-tinh.mjs", *map(str, m["chup_s"]), cwd=M, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        imgs = [os.path.join(W, "check/stills", f"{t}.jpg") for t in m["chup_s"]]
    d = os.path.join(HERE, m["ten"]); os.makedirs(d, exist_ok=True)
    moi, chuan = os.path.join(d, "moi.jpg"), os.path.join(d, "chuan.jpg"); sheet(imgs, moi)
    if CHOT or not os.path.exists(chuan):
        shutil.copy2(moi, chuan); res.append(f"{m['ten']}: CHỐT làm chuẩn"); continue
    o = subprocess.run(["ffmpeg", "-v", "info", "-i", moi, "-i", chuan, "-lavfi", "[0][1]scale2ref[a][b];[a][b]ssim", "-f", "null", "-"],
                       capture_output=True, text=True, env=ENV).stderr
    v = float(re.search(r"All:([\d.]+)", o).group(1)) if re.search(r"All:([\d.]+)", o) else 0
    res.append(f"{m['ten']}: SSIM {v:.3f}" + ("  ⚠ hình đổi — mở moi.jpg / chuan.jpg xem có đúng ý" if v < 0.97 else "  ✓ giữ nguyên"))
    shutil.rmtree(W, ignore_errors=True)
print("\n".join(res))
