#!/bin/bash
# Mở một phiên Claude Code HIỆN TRONG APP CLAUDE (Remote Control) cho một việc theo lịch. Tài khoản nào đang đăng nhập cũng được.
# Dùng: bash chay-lich.sh <tên>   (lời giao ở loi-giao/<tên>.md, phần sau khung --- đầu file)
export PATH="$HOME/.bun/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
ID="$1"; GOC="$(cd "$(dirname "$0")" && pwd)"; NAO="$(cd "$GOC/../.." && pwd)"; F="$GOC/loi-giao/$ID.md"
[ -f "$F" ] || { echo "Không có $F"; exit 1; }
LOI=$(awk 'c>=2{print} /^---$/{c++}' "$F"); [ -z "$LOI" ] && LOI=$(cat "$F")
TEN="Lịch · $ID · $(date +%d/%m)"
# Đóng phiên lần trước của cùng việc (đã xong, lịch sử vẫn còn trong app).
for s in $(screen -ls 2>/dev/null | awk -v t=".lich-$ID" '$1 ~ t"$" {print $1}'); do screen -S "$s" -X quit; done
screen -dmS "lich-$ID" -h 3000 bash -c "cd '$NAO' && for v in \$(env | grep -o '^CLAUDE[A-Z_]*'); do unset \$v; done; unset TELEGRAM_STATE_DIR ENABLE_TOOL_SEARCH ENABLE_CLAUDEAI_MCP_SERVERS CLAUDE_CODE_DISABLE_AUTO_MEMORY TELEGRAM_VIEC; exec claude --chrome --remote-control=\"\$1\" --permission-mode auto \"\$0\"" "$LOI" "$TEN"
echo "Đã mở phiên \"$TEN\" (xem trong app Claude)."
