#!/bin/bash
# Hook SessionEnd: tự đẩy bộ não lên GitHub khi phiên Claude Code kết thúc (lưới an toàn cho luật "có gì mới thì đẩy ngay").
# Chạy nền, ghi log, không làm phiền phiên.
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$HOME/.claude/logs/sync-nao.log"
mkdir -p "$(dirname "$LOG")"
( echo "== $(date '+%F %T')"; bash "$REPO/tu-dong-hoa/sync.sh" --push ) >>"$LOG" 2>&1 &
exit 0
