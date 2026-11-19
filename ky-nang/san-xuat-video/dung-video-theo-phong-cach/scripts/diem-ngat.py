#!/usr/bin/env python3
"""ĐIỂM NGẮT TIẾNG (khối 02 + 13, 19/11/2026): diem-ngat.py <video> <giây> [<giây> …]
Với mỗi mốc định cắt, tìm chỗ nhỏ tiếng gần nhất TRƯỚC và SAU (≥ 0,15 s) để cắt không cụt chữ, kèm vạch năng lượng ±2 s
(mỗi ký tự 50 ms: # to · + vừa · . nhỏ). Ngưỡng "nhỏ" tự tính theo nền ồn của chính đoạn (quán cà phê khác phòng kín).

Vì sao: mốc từng từ của whisper lệch 0,5–2 s (tập marketing 19/11: "chị đang cảm thấy" ghi 1140,84 mà nói ở 1141,6) → cắt theo mốc từ
dễ cụt chữ. Cắt ở chỗ ngắt tiếng, rồi chép lời lại đoạn đã ghép để nghe chữ đầu / cuối từng mối (khối 13)."""
import array, math, subprocess, sys, shutil

ff = shutil.which('ffmpeg') or '/opt/homebrew/bin/ffmpeg'
src = sys.argv[1]
for w in sys.argv[2:]:
    c = float(w); a = max(0, c - 2); b = c + 2
    raw = subprocess.run([ff, '-v', 'error', '-ss', f'{a:.2f}', '-t', f'{b - a:.2f}', '-i', src, '-vn', '-ac', '1', '-ar', '16000',
                          '-af', 'highpass=f=150,lowpass=f=3900', '-f', 's16le', '-'], capture_output=True).stdout
    x = array.array('h', raw); n = 320   # 20 ms
    db = [20 * math.log10((math.sqrt(sum(v * v for v in x[i:i + n]) / n) + 1) / 32768) for i in range(0, len(x) - n, n)]
    if not db: print(f'{c}: không đọc được tiếng'); continue
    nen = sorted(db)[len(db) // 5]; lo = nen + 4          # nhỏ = trong 4 dB trên nền ồn
    runs, s0 = [], None
    for i, d in enumerate(db + [0]):
        if d <= lo and s0 is None: s0 = i
        if (d > lo or i == len(db)) and s0 is not None:
            if (i - s0) * 0.02 >= 0.15: runs.append((a + s0 * 0.02, a + i * 0.02))
            s0 = None
    truoc = max((r for r in runs if (r[0] + r[1]) / 2 <= c), key=lambda r: r[1], default=None)
    sau = min((r for r in runs if (r[0] + r[1]) / 2 > c), key=lambda r: r[0], default=None)
    bar = ''.join('#' if d > lo + 8 else '+' if d > lo else '.' for d in db[::2][:80])
    f = lambda r: f'{(r[0] + r[1]) / 2:.2f} (lặng {r[1] - r[0]:.2f} s)' if r else 'không có'
    print(f'{c:.2f}: cắt trước → {f(truoc)} · cắt sau → {f(sau)}\n   {a:.1f} |{bar}| {b:.1f}')
