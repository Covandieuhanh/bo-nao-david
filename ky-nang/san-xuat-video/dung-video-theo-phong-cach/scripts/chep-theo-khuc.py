#!/usr/bin/env python3
"""Chép lời theo từng phân đoạn ngắn rồi hợp nhất (chính xác hơn chép cả file nơi ồn).
Dùng: python3 -I chep-theo-khuc.py <video|am-thanh> <thư-mục-ra> [độ-dài-khúc-giây]
Ra: <thư-mục-ra>/khuc-NNNN.json (whisper) và loi-hop-nhat.txt (mốc giờ + chữ).
Lưu ý: cuối mỗi khúc whisper hay bịa câu kêu gọi đăng ký; script lọc các câu đó, người làm vẫn phải soát tay chỗ nghi ngờ."""
import json, os, subprocess, sys, glob
src, out = sys.argv[1], sys.argv[2]
L = float(sys.argv[3]) if len(sys.argv) > 3 else 30.0
os.makedirs(out, exist_ok=True)
ep = os.path.expanduser('~/.local/bin')
os.environ['PATH'] = ep + os.pathsep + os.environ['PATH']
dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src]).decode().strip())
MODEL = os.environ.get('WHISPER_MODEL') or next(iter(glob.glob(os.path.expanduser('~/.local/share/whisper/*large-v3-turbo*.bin')) + glob.glob(os.path.expanduser('~/**/ggml-large-v3-turbo*.bin'), recursive=True)), None)
if not MODEL: sys.exit('Không thấy mô hình whisper; đặt biến WHISPER_MODEL')
BIA = ('subscribe', 'đăng ký kênh', 'ghiền mì gõ', 'cảm ơn các bạn đã theo dõi')
t, i, rows = 0.0, 0, []
while t < dur:
    wav = f'{out}/k{i:04d}.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-t', str(L), '-i', src, '-ac', '1', '-ar', '16000',
                    '-af', 'highpass=f=80,lowpass=f=7500,loudnorm', wav], check=True)
    base = f'{out}/khuc-{i:04d}'
    subprocess.run(['whisper-cli', '-m', MODEL, '-f', wav, '-l', 'vi', '-mc', '0', '-bs', '8', '-bo', '8', '-oj', '-of', base],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for s in json.load(open(base + '.json', encoding='utf-8'))['transcription']:
            tx = s['text'].strip(); a = s['offsets']['from'] / 1000 + t; b = s['offsets']['to'] / 1000 + t
            if tx and not any(k in tx.lower() for k in BIA): rows.append((a, b, tx))
    except Exception as e:
        print('lỗi phân đoạn', i, e)
    os.remove(wav); t += L; i += 1
with open(f'{out}/loi-hop-nhat.txt', 'w', encoding='utf-8') as f:
    for a, b, tx in rows: f.write(f'[{a:8.2f} → {b:8.2f}] {tx}\n')
print('xong', len(rows), 'câu ->', f'{out}/loi-hop-nhat.txt')
