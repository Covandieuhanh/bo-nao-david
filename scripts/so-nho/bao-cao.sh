#!/bin/bash
# Gửi David một tin báo cáo qua bot Sổ nhớ, và ghi vào sổ để bot tra lại được.
# Dùng: bash scripts/so-nho/bao-cao.sh "✅ Xong: … · Còn lại: … · Chờ anh: …"
# Mọi phiên Claude trên Mac đều dùng được (thói quen cuối việc). Chỉ gửi cho David (allowFrom trong access.json).
TIN="$*"
[ -z "$TIN" ] && { echo "Thiếu nội dung báo cáo"; exit 1; }
KENH="$HOME/.claude/channels/so-nho"
SO="$HOME/Documents/2-ca-nhan/so-nho/bao-cao-claude.md"
LUC=$(date "+%Y-%m-%d %H:%M")

[ -e "$SO" ] || printf '# Báo cáo của các phiên Claude\n\n' > "$SO"
printf -- '- %s · %s\n' "$LUC" "$(echo "$TIN" | tr '\n' ' ')" >> "$SO"

TOKEN=$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$KENH/.env" 2>/dev/null)
CHAT=$(python3 -c "import json;print(json.load(open('$KENH/access.json'))['allowFrom'][0])" 2>/dev/null)
if [ -z "$TOKEN" ] || [ -z "$CHAT" ]; then echo "Chưa cài bot Sổ nhớ: chỉ ghi vào sổ"; exit 0; fi

KQ=$(curl -s -m 20 "https://api.telegram.org/bot$TOKEN/sendMessage" \
  --data-urlencode "chat_id=$CHAT" --data-urlencode "text=$TIN")
echo "$KQ" | grep -q '"ok":true' && echo "Đã báo David qua Telegram" || { echo "Gửi Telegram lỗi (đã ghi sổ)"; exit 1; }
