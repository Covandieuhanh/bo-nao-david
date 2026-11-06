#!/usr/bin/env python3
"""CHUẨN ÂM LƯỢNG ĐẦU RA (khối 09, David chốt 2026-11-06): chuan_am.py <video> [--chi-do]
Đo độ to cả video. Lệch mục tiêu trong hồ sơ chung (`nhac.do_to_cuoi_LUFS`) quá `nhac.sai_so_LU` thì chỉnh cả bài
cùng một mức, giữ nguyên tương quan giọng và nhạc, không đụng hình. --chi-do: chỉ đo, không sửa."""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.realpath(__file__))
NH = json.load(open(os.path.join(HERE, "../../ho-so/chung.json"), encoding="utf-8"))["nhac"]
MUC, SAI = NH["do_to_cuoi_LUFS"], NH["sai_so_LU"]
DINH = 10 ** (NH["dinh_dB"] / 20)


def do(f):
    o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-map", "0:a", "-af", "ebur128", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", o)[-1])


f = os.path.expanduser(sys.argv[1])
i = do(f)
lech = MUC - i
if "--chi-do" in sys.argv or abs(lech) <= SAI:
    print(f"âm lượng {i:.1f} LUFS (chuẩn {MUC}): {'đạt' if abs(lech) <= SAI else f'lệch {lech:+.1f} LU'}")
    sys.exit(0)
tam = f + ".chinh-am.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-map", "0:v", "-map", "0:a", "-c:v", "copy",
                "-af", f"volume={lech:.2f}dB,alimiter=limit={DINH:.4f}:level=disabled", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", tam], check=True)
os.replace(tam, f)
print(f"âm lượng {i:.1f} → {do(f):.1f} LUFS (chuẩn {MUC})")
