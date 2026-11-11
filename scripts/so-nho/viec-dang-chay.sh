#!/bin/bash
# In ra mọi việc Claude đang có trên Mac, cho bot Sổ nhớ trả lời "đang chạy gì?".
DATA="$HOME/Documents/2-ca-nhan/so-nho"
python3 - "$DATA" <<'PY'
import json, glob, os, sys, time, subprocess, re
data = sys.argv[1]; now = time.time() * 1000
man = subprocess.run(['screen', '-ls'], capture_output=True, text=True).stdout
dang_giao = sorted(re.findall(r'\.viec-(\d+)\s', man), key=int)

print('## Việc giao qua Telegram đang chạy')
print(', '.join('#' + s for s in dang_giao) if dang_giao else 'Không có')

print('\n## Các phiên Claude hoạt động trong 3 giờ qua (mod Sổ việc)')
rows = []
for f in glob.glob(os.path.expanduser('~/.claude/so-viec/phien/*.json')):
    try: d = json.load(open(f))
    except Exception: continue
    if now - d.get('updatedAt', 0) > 3 * 3600e3: continue
    if d.get('cwd', '').endswith('so-nho'): continue  # bỏ chính bot
    o = d.get('open') or {}
    phut = int(o.get('activeMs', 0) / 60000)
    rows.append((d.get('updatedAt', 0), f"- {'ĐANG CHẠY' if d.get('running') else 'nghỉ'} · {d.get('title') or 'không tên'} · loại {o.get('type', '?')} · {phut} phút · cập nhật {time.strftime('%H:%M', time.localtime(d.get('updatedAt', 0) / 1000))}"))
print('\n'.join(r for _, r in sorted(rows, reverse=True)) or 'Không có')
PY
echo; echo "## Sức khoẻ bot"
TT="$DATA/.trang-thai"; read -r LUC PH TG < "$TT/nhip" 2>/dev/null
echo "Kiểm lần cuối: $( [ -n "$LUC" ] && echo "$(( ($(date +%s) - LUC) )) giây trước · $PH · $TG" || echo "chưa có")"
echo "Tự mở lại hôm nay: $(grep -c "^$(date +%F).*mo phien bot" "$TT/canh-bot.log" 2>/dev/null) lần · cảnh báo gần nhất: $(grep "canh bao" "$TT/canh-bot.log" 2>/dev/null | tail -1 | cut -c1-60)"
echo; echo "## Việc dở và chờ David quyết: đọc TRANG-THAI-HIEN-TAI.md (bảng 'Đang làm dở', mục 'Câu hỏi còn mở')"
