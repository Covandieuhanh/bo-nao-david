#!/bin/bash
# Kiểm tra sau khi đổi tài khoản Claude (hoặc cài máy mới): mọi thứ tự chạy có còn chạy không.
# Dùng: bash tu-dong-hoa/kiem-tra-tai-khoan.sh   → mỗi dòng ✅ / ❌ kèm cách sửa.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
NAO="$(cd "$(dirname "$0")/.." && pwd)"; TT="$HOME/Documents/2-ca-nhan/so-tay/.trang-thai"; LOI=0
ok() { echo "✅ $1"; }; hong() { echo "❌ $1 → $2"; LOI=1; }

TK=$(claude auth status 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('email','') if d.get('loggedIn') else '')" 2>/dev/null)
[ -n "$TK" ] && ok "Claude trong Terminal đã đăng nhập (phiên lịch, giao việc dùng đăng nhập này)" || hong "Claude trong Terminal chưa đăng nhập" "chạy: claude auth login"
[ -s "$HOME/.claude/channels/so-tay/claude-token" ] && ok "Bot có mã đăng nhập dài hạn (không chết khi Terminal bị đăng xuất)" || echo "⚪ Bot chưa có mã dài hạn → nên tạo: xem tu-dong-hoa/so-tay/README.md mục Mã đăng nhập dài hạn"

[ -s "$NAO/tu-dong-hoa/lich/lich-chay.md" ] && ok "Lịch tự chạy có trong repo (tu-dong-hoa/lich/lich-chay.md, mở phiên hiện trong app)" || hong "Thiếu lịch tự chạy" "bash $NAO/tu-dong-hoa/dong-bo.sh --keo"
launchctl list 2>/dev/null | grep -q com.david.so-tay && ok "Máy canh bot đang chạy (nhắc giờ, tóm tắt sáng, mở phiên lịch)" || hong "Máy canh bot không chạy" "bash $NAO/tu-dong-hoa/so-tay/cai-dat.sh"
[ -n "$(cat "$TT/nhip" 2>/dev/null | grep phien-ok)" ] && ok "Bot Sổ nhớ đang mở" || hong "Bot Sổ nhớ chưa mở" "chờ 2 phút để máy canh tự mở; vẫn hỏng thì xem $TT/canh-bot.log"
[ -s "$HOME/.claude/channels/so-tay/.env" ] && ok "Token bot Telegram có trên máy" || hong "Thiếu token bot" "dán token vào ~/.claude/channels/so-tay/.env"
grep -q "dong-bo.sh" "$HOME/.claude/settings.json" 2>/dev/null && ok "Hook đồng bộ GitHub + tự học đã cài" || hong "Thiếu hook" "bash $NAO/tu-dong-hoa/cai-dat-bo-nao.sh $NAO"
[ -L "$HOME/.claude/david.md" ] && [ -e "$HOME/.claude/david.md" ] && ok "Skill, hồ sơ, bộ nhớ trỏ vào repo" || hong "Lối tắt bộ não hỏng" "bash $NAO/tu-dong-hoa/cai-dat-bo-nao.sh $NAO"
claude plugin list 2>/dev/null | grep -qi telegram && ok "Plugin Telegram đã cài" || hong "Thiếu plugin Telegram" "claude plugin install telegram@claude-plugins-official --scope user"
echo "Còn phải tự làm trong app (máy không kiểm được): tiện ích Claude in Chrome đăng nhập đúng tài khoản; Zalo/Messenger/Telegram Web trong Chrome còn đăng nhập."
exit $LOI
