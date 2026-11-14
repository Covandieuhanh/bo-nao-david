#!/bin/bash
# Chạy một việc theo lịch bằng Claude Code trong Terminal: không cần app Claude, tài khoản nào đang đăng nhập cũng được.
# Dùng: bash chay-lich.sh <tên>   (lời giao ở loi-giao/<tên>.md, phần sau khung --- đầu file)
export PATH="$HOME/.bun/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
ID="$1"; GOC="$(cd "$(dirname "$0")" && pwd)"; NAO="$(cd "$GOC/../.." && pwd)"
F="$GOC/loi-giao/$ID.md"; TT="$HOME/Documents/2-ca-nhan/so-tay/.trang-thai"; mkdir -p "$TT"; LOG="$TT/lich-$ID.log"
[ -f "$F" ] || { echo "$(date '+%F %T') khong co $F" >> "$LOG"; exit 1; }
LOI=$(awk 'c>=2{print} /^---$/{c++}' "$F")
[ -z "$LOI" ] && LOI=$(cat "$F")
cd "$NAO" || exit 1
for v in $(env | grep -o '^CLAUDE[A-Z_]*'); do unset "$v"; done
unset TELEGRAM_STATE_DIR ENABLE_TOOL_SEARCH ENABLE_CLAUDEAI_MCP_SERVERS CLAUDE_CODE_DISABLE_AUTO_MEMORY TELEGRAM_VIEC
echo "$(date '+%F %T') bat dau $ID" >> "$LOG"
claude -p "$LOI" --permission-mode auto >> "$LOG" 2>&1; KQ=$?
echo "$(date '+%F %T') xong $ID (ma $KQ)" >> "$LOG"
if [ "$KQ" -ne 0 ]; then
  bash "$NAO/tu-dong-hoa/so-tay/bao-cao.sh" --chi-gui "⚠️ Lịch '$ID' chạy lỗi (mã $KQ). Có thể Claude trong Terminal chưa đăng nhập hoặc hết hạn mức. Xem .trang-thai/lich-$ID.log" >/dev/null 2>&1
fi
exit $KQ
