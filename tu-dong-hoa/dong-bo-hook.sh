#!/bin/bash
# Hook SessionEnd: tự đẩy bộ não lên GitHub khi phiên Claude Code kết thúc (lưới an toàn cho luật "có gì mới thì đẩy ngay").
# Chạy nền, ghi log, không làm phiền phiên.
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$HOME/.claude/logs/sync-nao.log"
mkdir -p "$(dirname "$LOG")"
CTY="$HOME/Documents/bo-nao-veltrix"   # bộ não công ty (kho private riêng): đẩy luôn nếu có trên máy
( echo "== $(date '+%F %T')"; bash "$REPO/tu-dong-hoa/dong-bo.sh" --push; [ -x "$CTY/dong-bo.sh" ] && bash "$CTY/dong-bo.sh" ) >>"$LOG" 2>&1 &
exit 0
