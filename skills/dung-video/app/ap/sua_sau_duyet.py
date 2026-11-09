#!/usr/bin/env python3
"""SỬA SAU KHI CLAUDE DUYỆT HÌNH: sua_sau_duyet.py <canh|lop-phu|ghep> <dự án> <W>
Đọc W/duyet-hinh.json. Đạt → chỉ ghi W/duyet-hinh.md. Chưa đạt + có kế hoạch sửa → thay kế hoạch, dựng lại ĐÚNG phần bị đổi
(cảnh: ap_canh → tránh che → soát → render_doi → tờ kiểm tra · highlight: ap_lop_phu → bảo vệ → render từng clip · vlog: ap_vlog →
bảo vệ → render-show), rồi ghi W/duyet-hinh.md (nhận xét + đã sửa). Một lần sửa; chat_luong.py gọi AI xem lại rồi mới cho đi tiếp."""
import json, shutil, subprocess, sys, time
from pathlib import Path
loai, P, W = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
APP = Path(__file__).resolve().parents[1]; S = APP.parent / "video-style-edit/scripts"
import os
ENV = dict(os.environ, PATH="/opt/homebrew/bin:/usr/local/bin:" + os.environ.get("PATH", ""))
ten_kq = "duyet-chup-thu" if loai in ("canh-truoc", "video-truoc") else "duyet-hinh"
kq = json.loads((W / f"{ten_kq}.json").read_text(encoding="utf-8"))
md = ["# Claude duyệt ảnh chụp thử (trước render)" if loai in ("canh-truoc", "video-truoc") else "# Claude duyệt hình sau render", "", f"**Kết luận:** {'✅ đạt' if kq.get('dat') else '🔧 đã thực hiện sửa, cần AI kiểm lại'}", "", kq.get("nhan_xet", ""), ""]
chay = lambda *c, **k: subprocess.run(list(c), env=ENV, check=True, **k)
if not kq.get("dat") and kq.get("ke_hoach"):
    ten = {"video-truoc": "ke-hoach-canh.json", "canh-truoc": "ke-hoach-canh.json", "canh": "ke-hoach-canh.json", "lop-phu": "lop-phu.json", "ghep": "ke-hoach-ghep.json", "hl-pod": "hl-pod.json"}[loai]
    shutil.copy2(W / ten, W / f"{ten}.truoc-duyet-{time.strftime('%H%M%S')}")
    (W / ten).write_text(json.dumps(kq["ke_hoach"], ensure_ascii=False, indent=1), encoding="utf-8")
    if loai == "video-truoc":
        chay("python3", "-I", str(APP / "ap/ap_canh.py"), str(P), str(W / ten), str(W))
        r = subprocess.run(["zsh", str(S / "face_place.sh"), str(P)], env=ENV, capture_output=True, text=True)
        if r.returncode and "script này cho khung dọc" not in r.stdout+r.stderr: raise SystemExit(r.stderr)
        chay("node", str(S / "soat_canh.mjs"), str(P), cwd=P/"motion")
        chay("python3", "-I", str(APP / "ap/chup_thu.py"), str(P), str(W))
    elif loai == "canh-truoc":   # podcast trước render: sửa kịch bản → soát → chụp lại (chưa render)
        chay("python3", "-I", str(APP / "ap/ap_canh.py"), str(P), str(W / ten), str(W))
        chay("node", str(S / "soat_canh.mjs"), str(P), cwd=P / "motion")
        chay("python3", "-I", str(APP / "ap/pod_chup_thu.py"), str(P), str(W))
    elif loai == "canh":
        chay("python3", "-I", str(APP / "ap/ap_canh.py"), str(P), str(W / ten), str(W))
        if "podcast: true" not in (P / "motion/src/project.js").read_text():
            r = subprocess.run(["zsh", str(S / "face_place.sh"), str(P)], env=ENV, capture_output=True, text=True)
            print(r.stdout[-1500:])   # video ngang: face_place.py báo "script này cho khung dọc" sau khi đã ghi mat.js — không phải lỗi
            if r.returncode != 0 and "script này cho khung dọc" not in r.stdout + r.stderr:
                raise SystemExit(r.stderr[-1500:] or "face_place.sh lỗi")
        chay("node", str(S / "soat_canh.mjs"), str(P), cwd=P / "motion")
        chay("python3", "-I", str(APP / "ap/render_doi.py"), str(P))
        chay("python3", "-I", str(APP / "ap/to_kiem_tra.py"), str(P))
    elif loai == "lop-phu":
        chay("python3", "-I", str(APP / "ap/ap_lop_phu.py"), str(P), str(W / ten))
        chay("python3", "-I", str(APP / "ap/hl_moi_clip.py"), str(P), "bao-ve")
        chay("python3", "-I", str(APP / "ap/hl_moi_clip.py"), str(P), "render")
        for video in sorted(P.glob("clip-*/video-final.mp4")):
            chay("python3", "-I", str(APP / "ap/to_hinh.py"), str(video), str(video.parent / "check/sheet.jpg"), "18")
    elif loai == "hl-pod":
        chay("python3", "-I", str(APP / "ap/hl_pod.py"), str(P), str(W), "ap")
        chay("python3", "-I", str(APP / "ap/hl_pod.py"), str(P), str(W), "render")
    else:
        chay("python3", "-I", str(APP / "ap/ap_vlog.py"), str(P), str(W / ten))
        chay("python3", "-I", str(S / "lift.py"), str(P)); chay("python3", "-I", str(S / "overlay_guard.py"), str(P))
        chay("node", "render-show.mjs", cwd=P / "motion")
        chay("python3", "-I", str(APP / "ap/to_hinh.py"), str(P / "video-final.mp4"), str(P / "check/sheet.jpg"), "30")
    md += ["**Đã sửa:** kế hoạch cũ cất ở `" + f"{ten}.truoc-duyet-*" + "`; dựng lại phần bị đổi."]
(W / f"{ten_kq}.md").write_text("\n".join(md) + "\n", encoding="utf-8"); print("\n".join(md))
