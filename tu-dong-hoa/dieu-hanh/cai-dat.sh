#!/bin/bash
# Cài bot Điều hành (chạy lại bao nhiêu lần cũng được). Cần token trước: tạo bot ở @BotFather rồi
#   bash tu-dong-hoa/dieu-hanh/cai-dat.sh "<token BotFather đưa>"   (lần sau chạy không cần token)
# Token lưu ở ~/.claude/channels/dieu-hanh/.env (chmod 600, không lên GitHub). Người được nhắn: lấy allowFrom của bot Sổ nhớ.
set -e
GOC="$(cd "$(dirname "$0")" && pwd)"
KENH="$HOME/.claude/channels/dieu-hanh"
NHAN="com.david.dieu-hanh"
PLIST="$HOME/Library/LaunchAgents/$NHAN.plist"
TT="$HOME/Documents/2-ca-nhan/so-tay/.trang-thai"
PY="$(command -v /opt/homebrew/bin/python3 || command -v python3)"
mkdir -p "$KENH" "$TT"; chmod 700 "$KENH"

if [ -n "$1" ]; then
  printf 'TELEGRAM_BOT_TOKEN=%s\n' "$1" > "$KENH/.env"; chmod 600 "$KENH/.env"
  rm -f "$TT/dieu-hanh-offset"
fi
[ -s "$KENH/.env" ] || { echo "Chưa có token: chạy lại kèm token BotFather đưa."; exit 1; }
TOKEN=$(sed -n 's/^TELEGRAM_BOT_TOKEN=//p' "$KENH/.env")
TEN=$(curl -s -m 15 "https://api.telegram.org/bot$TOKEN/getMe" | "$PY" -c 'import json,sys;d=json.load(sys.stdin);print(d["result"]["username"] if d.get("ok") else "")' 2>/dev/null || true)
[ -n "$TEN" ] || { echo "Token không đúng (Telegram từ chối). Kiểm lại token rồi chạy lại."; exit 1; }

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$NHAN</string>
  <key>ProgramArguments</key><array><string>$PY</string><string>-I</string><string>$GOC/bot.py</string></array>
  <key>ProcessType</key><string>Interactive</string>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>ThrottleInterval</key><integer>30</integer>
  <key>StandardErrorPath</key><string>$TT/dieu-hanh.err</string>
</dict></plist>
EOF
launchctl bootout "gui/$(id -u)/$NHAN" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"

# Bot Sổ nhớ nhận luật mới (đã chuyển phần điều khiển Claude sang đây): chép luật, tắt phiên bot để máy canh mở lại với luật mới,
# khởi động lại máy canh để chạy bản canh-bot.sh mới (nhắc giờ qua Sổ nhớ, canh nhịp bot Điều hành).
DATA="$HOME/Documents/2-ca-nhan/so-tay"
cp "$GOC/../so-tay/quy-tac-bot.md" "$DATA/CLAUDE.md"
screen -ls 2>/dev/null | awk '$1 ~ /\.so-tay$/ {print $1}' | while read -r id; do screen -S "$id" -X quit; done
launchctl kickstart -k "gui/$(id -u)/com.david.so-tay" 2>/dev/null || true
echo "Đã cài bot Điều hành @$TEN. Mở Telegram, nhắn bot /start. Nhật ký: $TT/dieu-hanh.log"
