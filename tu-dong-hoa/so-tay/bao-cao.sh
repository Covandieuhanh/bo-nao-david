#!/bin/bash
# Gửi David một tin báo cáo qua bot chính (Hermes hoặc Sổ nhớ, xem bot-chinh dưới), và ghi vào sổ để bot tra lại được.
# Dùng: bash tu-dong-hoa/so-tay/bao-cao.sh "✅ Xong: … · Còn lại: … · Chờ anh: …"
# Mọi phiên Claude trên Mac đều dùng được (thói quen cuối việc). Chỉ gửi cho David (allowFrom trong access.json).
# --chi-gui: chỉ gửi, không ghi sổ báo cáo (canh-bot dùng cho nhắc giờ và cảnh báo).
# Gửi hỏng (mất mạng…) sau 3 lần thử: tin vào hàng chờ .trang-thai/hang-cho-gui/, canh-bot gửi lại khi có mạng (kèm giờ gốc).
# BAO_CAO_KHONG_CHO=1: không đưa vào hàng chờ (canh-bot tự thử lại nhắc giờ, và khi gửi lại từ hàng chờ).
# --anh <file>: gửi kèm một ảnh (gửi ảnh trước, tin chữ ngay sau) — lịch đăng bài dùng để David chép bài + ảnh đi đăng.
# Hai bot (20/11): mặc định gửi qua bot Điều hành (báo cáo phiên, duyệt, cảnh báo máy); --so-nho gửi qua bot Sổ nhớ
#   (nhắc giờ, tin nhắn tổng hợp 📬 — tin David trả lời trong Sổ nhớ). Chưa cài bot Điều hành thì mọi tin qua Sổ nhớ như cũ.
# --nut '<json inline_keyboard>': kèm nút bấm (duyet-tu-xa.py). Tin "#N ✅ … Đóng phiên #N" tự có nút [Đóng phiên #N].
GHI=1; ANH=""; BOT="dieu-hanh"; NUT=""
while [ $# -gt 0 ]; do
  case "$1" in
    --chi-gui) GHI=0; shift ;;
    --anh) ANH="$2"; shift 2 ;;
    --so-nho) BOT="so-nho"; shift ;;
    --nut) NUT="$2"; shift 2 ;;
    *) break ;;
  esac
done
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
  TOKEN=""
  [ "$BOT" = "dieu-hanh" ] && TOKEN=$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$HOME/.claude/channels/dieu-hanh/.env" 2>/dev/null)
  [ -z "$TOKEN" ] && { TOKEN=$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$KENH/.env" 2>/dev/null); NUT=""; }  # Sổ nhớ không xử lý nút bấm
  CHAT=$(python3 -c "import json;print(json.load(open('$KENH/access.json'))['allowFrom'][0])" 2>/dev/null)
fi
if [ -z "$NUT" ] && [ "$BOT" = "dieu-hanh" ] && [[ "$TIN" =~ ^#([0-9]+)[[:space:]]*✅ ]] && [[ "$TIN" == *"Đóng phiên"* ]]; then
  NUT='[[{"text":"Đóng phiên #'"${BASH_REMATCH[1]}"'","callback_data":"dong|'"${BASH_REMATCH[1]}"'"}]]'
fi
[ -n "$NUT" ] && [ -n "$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$HOME/.claude/channels/dieu-hanh/.env" 2>/dev/null)" ] || NUT=""
if [ -z "$TOKEN" ] || [ -z "$CHAT" ]; then echo "Chưa cài bot gửi tin: chỉ ghi vào sổ"; exit 0; fi

if [ -n "$ANH" ]; then
  if [ -f "$ANH" ]; then
    curl -s -m 60 "https://api.telegram.org/bot$TOKEN/sendPhoto" -F "chat_id=$CHAT" -F "photo=@$ANH" | grep -q '"ok":true' \
      || echo "Gửi ảnh lỗi: $ANH"
  else echo "Không thấy ảnh: $ANH"; fi
fi
THEM=(); [ -n "$NUT" ] && THEM=(--data-urlencode "reply_markup={\"inline_keyboard\":$NUT}")
for LAN in 1 2 3; do
  KQ=$(curl -s -m 20 "https://api.telegram.org/bot$TOKEN/sendMessage" \
    --data-urlencode "chat_id=$CHAT" --data-urlencode "text=$TIN" "${THEM[@]}")
  echo "$KQ" | grep -q '"ok":true' && { echo "Đã báo David qua Telegram"; exit 0; }
  # Bot Điều hành chưa nhắn được cho David (chưa bấm Start, bị chặn, token sai): chuyển qua bot Sổ nhớ ngay, không nút.
  if [ "$BOT" = "dieu-hanh" ] && echo "$KQ" | grep -qE '"error_code":(400|401|403|404)'; then
    TK2=$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$KENH/.env" 2>/dev/null)
    if [ -n "$TK2" ] && [ "$TK2" != "$TOKEN" ]; then
      echo "Bot Điều hành lỗi ($(echo "$KQ" | sed -n 's/.*"description":"\([^"]*\)".*/\1/p')), chuyển qua Sổ nhớ"
      TOKEN="$TK2"; THEM=(); BOT="so-nho"; continue
    fi
  fi
  [ "$LAN" -lt 3 ] && sleep 5
done
if [ "${BAO_CAO_KHONG_CHO:-0}" != 1 ]; then
  CHO="$HOME/Documents/2-ca-nhan/so-tay/.trang-thai/hang-cho-gui"; mkdir -p "$CHO"
  DUOI=""; [ "$BOT" = "so-nho" ] && DUOI=".so-nho"
  printf '%s\n%s' "$LUC" "$TIN" > "$CHO/$(date +%s)-$$$DUOI.txt"
  echo "Gửi Telegram lỗi: đã vào hàng chờ, có mạng máy tự gửi lại"; exit 1
fi
echo "Gửi Telegram lỗi"; exit 1
