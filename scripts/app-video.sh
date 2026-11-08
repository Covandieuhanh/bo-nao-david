#!/bin/zsh
# App dựng video tự chạy nền (LaunchAgent của macOS): mở máy là có http://localhost:8765, tắt/lỗi thì macOS tự bật lại.
#   zsh scripts/app-video.sh cai      → cài + bật (chạy lại lệnh này sau khi đổi máy / đổi chỗ repo)
#   zsh scripts/app-video.sh go       → tắt hẳn + gỡ
#   zsh scripts/app-video.sh khoi-lai → khởi động lại (sau khi sửa code app) — việc đang dựng KHÔNG bị ngắt
#   zsh scripts/app-video.sh xem      → có đang chạy không
# File cấu hình nằm ở ~/Library/LaunchAgents (của máy này, không lên GitHub). Log: ~/Movies/_app/may-chu.log
set -e
TEN=vn.davidtran.app-dung-video
PL=~/Library/LaunchAgents/$TEN.plist
REPO=${0:A:h:h}
APP=$REPO/skills/dung-video/app/giao_dien.py
PY=$(command -v /opt/homebrew/bin/python3 || command -v python3)
UID_=$(id -u)

case ${1:-xem} in
  cai)
    mkdir -p ~/Library/LaunchAgents ~/Movies/_app
    cat > $PL <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$TEN</string>
  <key>ProgramArguments</key><array><string>$PY</string><string>-I</string><string>$APP</string></array>
  <key>WorkingDirectory</key><string>$REPO</string>
  <key>EnvironmentVariables</key><dict>
    <key>PATH</key><string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    <key>HOME</key><string>$HOME</string>
  </dict>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>ProcessType</key><string>Interactive</string>
  <key>AbandonProcessGroup</key><true/>
  <key>StandardOutPath</key><string>$HOME/Movies/_app/may-chu.log</string>
  <key>StandardErrorPath</key><string>$HOME/Movies/_app/may-chu.log</string>
</dict></plist>
EOF
    launchctl bootout gui/$UID_/$TEN 2>/dev/null || true
    launchctl bootstrap gui/$UID_ $PL
    echo "Đã cài. Mở http://localhost:8765" ;;
  go)
    launchctl bootout gui/$UID_/$TEN 2>/dev/null || true
    rm -f $PL; echo "Đã gỡ app tự chạy." ;;
  khoi-lai)
    launchctl kickstart -k gui/$UID_/$TEN && echo "Đã khởi động lại." ;;
  xem)
    launchctl print gui/$UID_/$TEN 2>/dev/null | grep -E "^\s+(state|pid) =" || echo "Chưa cài (zsh scripts/app-video.sh cai)" ;;
  *) sed -n 2,7p $0 ;;
esac
