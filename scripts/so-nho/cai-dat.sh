#!/bin/bash
# Cài bot Sổ nhớ (chạy lại bao nhiêu lần cũng được, không ghi đè dữ liệu).
set -e
GOC="$(cd "$(dirname "$0")" && pwd)"
DATA="$HOME/Documents/2-ca-nhan/so-nho"
NHAN="com.david.so-nho"
PLIST="$HOME/Library/LaunchAgents/$NHAN.plist"

mkdir -p "$DATA/hop-thu" "$DATA/nhat-ky" "$DATA/.claude" "$DATA/.trang-thai" "$HOME/.claude/channels/so-nho"
cp "$GOC/luat-bot.md" "$DATA/CLAUDE.md"
cp "$GOC/settings.json" "$DATA/.claude/settings.json"

tao() { [ -e "$DATA/$1" ] || printf '%s\n\n' "$2" > "$DATA/$1"; }
tao viec-can-lam.md "# Việc cần làm"
tao lich-hen.md "# Lịch/hẹn"
tao y-tuong.md "# Ý tưởng"
tao nguoi.md "# Người"
tao kien-thuc.md "# Kiến thức"
tao nhac-viec.md "# Nhắc đúng giờ (giờ Đức)"
tao nhom.md "# Các nhóm của Sổ nhớ

| File | Nhóm |
|---|---|
| viec-can-lam.md | Việc cần làm |
| lich-hen.md | Lịch/hẹn |
| y-tuong.md | Ý tưởng |
| nguoi.md | Người |
| kien-thuc.md | Kiến thức |
| nhat-ky/<YYYY-MM>.md | Nhật ký |
| nhac-viec.md | Nhắc đúng giờ |
| hop-thu/<YYYY-MM>.md | Nguyên văn mọi tin |"

# Tin thư mục để phiên bot không hỏi lúc mở.
python3 - "$DATA" <<'PY'
import json, sys, os
p = os.path.expanduser("~/.claude.json"); d = json.load(open(p))
d.setdefault("projects", {}).setdefault(sys.argv[1], {})["hasTrustDialogAccepted"] = True
json.dump(d, open(p + ".tmp", "w"), indent=2); os.replace(p + ".tmp", p)
PY

chmod +x "$GOC/canh-bot.sh"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$NHAN</string>
  <key>ProgramArguments</key><array><string>/usr/bin/screen</string><string>-DmS</string><string>so-nho-canh</string><string>/bin/bash</string><string>$GOC/canh-bot.sh</string></array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardErrorPath</key><string>$DATA/.trang-thai/launchd.err</string>
</dict></plist>
EOF
launchctl bootout "gui/$(id -u)/$NHAN" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "Đã cài. Dữ liệu: $DATA · xem phiên bot: screen -r so-nho (thoát: Ctrl-A rồi D)"
