#!/bin/bash
# Kiểm tra sau khi đổi tài khoản Claude (hoặc cài máy mới): mọi thứ tự chạy có còn chạy không.
# Dùng: bash tu-dong-hoa/kiem-tra-tai-khoan.sh   → mỗi dòng ✅ / ❌ kèm cách sửa.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
NAO="$(cd "$(dirname "$0")/.." && pwd)"; TT="$HOME/Documents/2-ca-nhan/so-tay/.trang-thai"; LOI=0
ok() { echo "✅ $1"; }; hong() { echo "❌ $1 → $2"; LOI=1; }

TK=$(claude auth status 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('email','') if d.get('loggedIn') else '')" 2>/dev/null)
[ -n "$TK" ] && ok "Claude trong Terminal đã đăng nhập (bot, giao việc, lịch gom/đóng gói dùng đăng nhập này)" || hong "Claude trong Terminal chưa đăng nhập" "chạy: claude auth login"

APP=$(ls -td "$HOME/Library/Application Support/Claude/claude-code-sessions"/*/*/ 2>/dev/null | head -1)
if [ -z "$APP" ]; then hong "Chưa thấy tài khoản app Claude" "mở app Claude, đăng nhập"
elif grep -q '"tong-hop-tin-nhan"' "$APP/scheduled-tasks.json" 2>/dev/null; then ok "Lịch tổng hợp tin nhắn có trong tài khoản app đang mở"
else hong "Tài khoản app đang mở chưa có lịch tổng hợp tin" "python3 -I $NAO/tu-dong-hoa/lich/cai-lich-app.py rồi mở lại app"; fi

launchctl list 2>/dev/null | grep -q com.david.so-tay && ok "Máy canh bot đang chạy (nhắc giờ, tóm tắt sáng, lịch gom/đóng gói)" || hong "Máy canh bot không chạy" "bash $NAO/tu-dong-hoa/so-tay/cai-dat.sh"
[ -n "$(cat "$TT/nhip" 2>/dev/null | grep phien-ok)" ] && ok "Bot Sổ nhớ đang mở" || hong "Bot Sổ nhớ chưa mở" "chờ 2 phút để máy canh tự mở; vẫn hỏng thì xem $TT/canh-bot.log"
[ -s "$HOME/.claude/channels/so-tay/.env" ] && ok "Token bot Telegram có trên máy" || hong "Thiếu token bot" "dán token vào ~/.claude/channels/so-tay/.env"
grep -q "dong-bo.sh" "$HOME/.claude/settings.json" 2>/dev/null && ok "Hook đồng bộ GitHub + tự học đã cài" || hong "Thiếu hook" "bash $NAO/tu-dong-hoa/cai-dat-bo-nao.sh $NAO"
[ -L "$HOME/.claude/david.md" ] && [ -e "$HOME/.claude/david.md" ] && ok "Skill, hồ sơ, bộ nhớ trỏ vào repo" || hong "Lối tắt bộ não hỏng" "bash $NAO/tu-dong-hoa/cai-dat-bo-nao.sh $NAO"
claude plugin list 2>/dev/null | grep -qi telegram && ok "Plugin Telegram đã cài" || hong "Thiếu plugin Telegram" "claude plugin install telegram@claude-plugins-official --scope user"
echo "Còn phải tự làm trong app (máy không kiểm được): tiện ích Claude in Chrome đăng nhập đúng tài khoản; Zalo/Messenger/Telegram Web còn đăng nhập."
exit $LOI
