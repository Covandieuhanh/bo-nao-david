#!/usr/bin/env python3
"""CHUẨN ÂM LƯỢNG ĐẦU RA (khối 09, David chốt 2026-11-06): chuan_am.py <video> [--chi-do]
Đo độ to + đỉnh thật cả video. Lệch mục tiêu trong hồ sơ chung (`nhac.do_to_cuoi_LUFS`) quá `nhac.sai_so_LU`, HOẶC đỉnh thật vượt
`nhac.dinh_dB` thì chỉnh cả bài cùng một mức (giữ tương quan giọng và nhạc) và chặn đỉnh ở mẫu 192 kHz (≈ đỉnh thật), không đụng hình.
Trước 10/11/2026 độ to đạt thì bỏ qua đỉnh → podcast thử ra đỉnh −1,0 dB. Chặn đỉnh làm bài nhỏ đi nên đo lại và bù, tối đa 3 lượt, luôn xuất từ bản trước khi chỉnh. --chi-do: chỉ đo, không sửa."""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.realpath(__file__))
NH = json.load(open(os.path.join(HERE, "../../ho-so/chung.json"), encoding="utf-8"))["nhac"]
MUC, SAI = NH["do_to_cuoi_LUFS"], NH["sai_so_LU"]
DINH = 10 ** (NH["dinh_dB"] / 20)


def do(f):
    o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-map", "0:a", "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    tp = re.findall(r"Peak:\s+(-?[\d.]+|-inf) dBFS", o)
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", o)[-1]), (-120.0 if not tp or tp[-1] == "-inf" else float(tp[-1]))


f = os.path.expanduser(sys.argv[1])
i, tp = do(f)
lech = MUC - i
dinh_vuot = tp > NH["dinh_dB"]
if "--chi-do" in sys.argv or (abs(lech) <= SAI and not dinh_vuot):
    print(f"âm lượng {i:.1f} LUFS (chuẩn {MUC}) · đỉnh {tp:.1f} dBTP: {'đạt' if abs(lech) <= SAI and not dinh_vuot else 'chưa đạt'}")
    sys.exit(0)
tam, goc = f + ".chinh-am.mp4", f + ".truoc-chinh.mp4"
os.replace(f, goc)                                  # giữ bản trước khi chỉnh: mỗi lượt xuất lại TỪ BẢN NÀY, không nén AAC chồng
han = 10 ** ((NH["dinh_dB"] - 0.5) / 20)          # chặn thấp hơn chuẩn 0,5 dB: AAC đẩy đỉnh lên lại một chút
gain = lech if abs(lech) > SAI else 0.0
i2, tp2 = i, tp
for luot in range(1, 4):                            # bộ chặn đỉnh làm bài nhỏ đi (10/11/2026 ra −14,8) → đo lại, bù phần thiếu, tối đa 3 lượt
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", goc, "-map", "0:v", "-map", "0:a", "-c:v", "copy",
                    "-af", f"volume={gain:.2f}dB,aresample=192000,alimiter=limit={han:.4f}:level=disabled:attack=5:release=60,aresample=48000",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", tam], check=True)
    i2, tp2 = do(tam)
    if abs(MUC - i2) <= SAI and tp2 <= NH["dinh_dB"]:
        break
    gain += MUC - i2
os.replace(tam, f)
os.remove(goc)
dat = abs(MUC - i2) <= SAI and tp2 <= NH["dinh_dB"]
print(f"âm lượng {i:.1f} → {i2:.1f} LUFS (chuẩn {MUC}) · đỉnh {tp:.1f} → {tp2:.1f} dBTP (chuẩn ≤ {NH['dinh_dB']}) · {luot} lượt: {'đạt' if dat else 'CHƯA ĐẠT'}")
