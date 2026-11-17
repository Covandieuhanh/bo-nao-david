#!/bin/bash
# Cài launchd com.david.xem-ket-qua: trang xem kết quả video + trang bài đăng (http://localhost:8765, /bai-dang)
# tự bật mỗi khi mở máy, tự chạy lại nếu tắt (David 17/11/2026: "Có, tự bật").
# Dùng: bash tu-dong-hoa/cai-trang-xem.sh   ·   gỡ: launchctl bootout gui/$(id -u)/com.david.xem-ket-qua && rm ~/Library/LaunchAgents/com.david.xem-ket-qua.plist
set -e
GOC="$(cd "$(dirname "$0")/.." && pwd)"
NHAN="com.david.xem-ket-qua"
PLIST="$HOME/Library/LaunchAgents/$NHAN.plist"
PY="$(command -v python3)"
LOG="$HOME/Library/Logs/xem-ket-qua.log"
mkdir -p "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
cat > "$PLIST" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$NHAN</string>
  <key>ProgramArguments</key><array><string>$PY</string><string>$GOC/tu-dong-hoa/xem-ket-qua.py</string><string>--khong-mo</string></array>
  <key>WorkingDirectory</key><string>$GOC</string>
  <key>EnvironmentVariables</key><dict><key>PATH</key><string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string></dict>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>$LOG</string>
  <key>StandardErrorPath</key><string>$LOG</string>
</dict></plist>
PL
# Tắt bản đang chạy tay (nếu có) để launchd giữ cổng 8765
pkill -f "tu-dong-hoa/xem-ket-qua.py" 2>/dev/null || true; sleep 1
launchctl bootout "gui/$(id -u)/$NHAN" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
sleep 2
curl -s -o /dev/null -w "Trang xem: http://localhost:8765/bai-dang → %{http_code}\n" http://localhost:8765/bai-dang
