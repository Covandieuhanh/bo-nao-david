#!/bin/bash
# Gửi David một tin báo cáo qua bot chính (Hermes hoặc Sổ nhớ, xem bot-chinh dưới), và ghi vào sổ để bot tra lại được.
# Dùng: bash tu-dong-hoa/so-tay/bao-cao.sh "✅ Xong: … · Còn lại: … · Chờ anh: …"
# Mọi phiên Claude trên Mac đều dùng được (thói quen cuối việc). Chỉ gửi cho David (allowFrom trong access.json).
# --chi-gui: chỉ gửi, không ghi sổ báo cáo (canh-bot dùng cho nhắc giờ và cảnh báo).
GHI=1; [ "$1" = "--chi-gui" ] && { GHI=0; shift; }
TIN="$*"
[ -z "$TIN" ] && { echo "Thiếu nội dung báo cáo"; exit 1; }
KENH="$HOME/.claude/channels/so-tay"
SO="$HOME/Documents/2-ca-nhan/so-tay/bao-cao-claude.md"
LUC=$(date "+%Y-%m-%d %H:%M")

if [ "$GHI" = 1 ]; then
  [ -e "$SO" ] || printf '# Báo cáo của các phiên Claude\n\n' > "$SO"
  printf -- '- %s · %s\n' "$LUC" "$(echo "$TIN" | tr '\n' ' ')" >> "$SO"
fi

# Báo cáo của việc giao qua Telegram ("#N ✅…" / "#N ❓…") thì ghi trạng thái vào viec-da-giao.md.
if [[ "$TIN" =~ ^#([0-9]+)[[:space:]]*(✅|❓) ]]; then
  N="${BASH_REMATCH[1]}"; [ "${BASH_REMATCH[2]}" = "✅" ] && TT_MOI="xong $(date '+%d/%m %H:%M')" || TT_MOI="chờ anh $(date '+%d/%m %H:%M')"
  bash "$(dirname "$0")/giao-viec.sh" --trang-thai "$N" "$TT_MOI" 2>/dev/null
fi

# Bot gửi tin: .trang-thai/bot-chinh ghi "hermes" thì gửi qua bot Hermes (khung chat chung), không có thì bot Sổ nhớ.
# Quay về bot cũ: xoá file đó. Chỉ gửi bằng sendMessage nên không giành kết nối nhận tin của Hermes.
if [ "${BOT_CHINH:-$(cat "$HOME/Documents/2-ca-nhan/so-tay/.trang-thai/bot-chinh" 2>/dev/null)}" = "hermes" ]; then
  TOKEN=$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$HOME/.hermes/.env" 2>/dev/null | tr -d '"'"'")
  CHAT=$(sed -n 's/^TELEGRAM_ALLOWED_USERS=//p' "$HOME/.hermes/.env" 2>/dev/null | tr -d '"'"'" | cut -d, -f1 | tr -d ' ')
else
  TOKEN=$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$KENH/.env" 2>/dev/null)
  CHAT=$(python3 -c "import json;print(json.load(open('$KENH/access.json'))['allowFrom'][0])" 2>/dev/null)
fi
if [ -z "$TOKEN" ] || [ -z "$CHAT" ]; then echo "Chưa cài bot gửi tin: chỉ ghi vào sổ"; exit 0; fi

KQ=$(curl -s -m 20 "https://api.telegram.org/bot$TOKEN/sendMessage" \
  --data-urlencode "chat_id=$CHAT" --data-urlencode "text=$TIN")
echo "$KQ" | grep -q '"ok":true' && echo "Đã báo David qua Telegram" || { echo "Gửi Telegram lỗi (đã ghi sổ)"; exit 1; }
