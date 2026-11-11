#!/bin/bash
# Bot Sổ nhớ giao một việc cho phiên Claude Code mới chạy nền trong thư mục bộ não.
# Dùng: bash giao-viec.sh "<yêu cầu nguyên văn của David>"     → in ra số việc
#       bash giao-viec.sh --tiep <số> "<lời David trả lời>"     → phiên đó làm tiếp
#       bash giao-viec.sh --dung <số>                           → tắt việc đó
NAO="$HOME/Documents/David.Claude"
DATA="$HOME/Documents/2-ca-nhan/so-nho"
TT="$DATA/.trang-thai"
SO="$DATA/viec-giao.md"
LOGS="$TT/viec"
mkdir -p "$LOGS"
[ -e "$SO" ] || printf '# Việc giao cho Claude qua Telegram\n\n| # | Giao lúc | Việc | Phiên | Trạng thái |\n|---|---|---|---|---|\n' > "$SO"

# Phiên làm việc không được đụng tới bot Telegram (plugin sẽ giành bot nếu thấy token), không kế thừa cấu hình thu gọn của bot.
unset TELEGRAM_STATE_DIR ENABLE_TOOL_SEARCH ENABLE_CLAUDEAI_MCP_SERVERS CLAUDE_CODE_DISABLE_AUTO_MEMORY
export PATH="$HOME/.bun/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

LOI_DAN() { cat <<EOF
Đây là việc David giao qua Telegram (việc #$1). David không ngồi trước máy, không trả lời được trong phiên này.
Làm theo AGENTS.md và skill đúng với việc, như một phiên bình thường. Không dùng công cụ hỏi David (AskUserQuestion) trong phiên.
Khi XONG, hoặc khi CẦN DAVID QUYẾT (nhất là trước khi đăng, gửi, xoá — luật 5), chạy:
  bash scripts/so-nho/bao-cao.sh "#$1 ✅ Xong: … · Ở đâu: … · Còn lại: …"   hoặc   "#$1 ❓ Chờ anh: <câu hỏi, có gợi ý trả lời>"
rồi kết thúc lượt. David trả lời qua bot thì phiên này được mở lại để làm tiếp. Tin báo cáo ngắn, tiếng Việt, không quá 5 dòng.
EOF
}

chay() { # $1 số việc, $2 cờ phiên (--session-id / --resume), $3 id, $4 lời nhắn
  screen -dmS "viec-$1" bash -c "cd '$NAO' && claude -p $2 $3 --permission-mode auto --name 'Telegram #$1' \"\$0\" >> '$LOGS/$1.log' 2>&1; echo \"--- het \$(date '+%F %T')\" >> '$LOGS/$1.log'" "$4"
}

doi_trang_thai() { # $1 số, $2 trạng thái mới
  python3 - "$SO" "$1" "$2" <<'PY'
import sys
p,so,tt=sys.argv[1:]; ls=open(p).read().split('\n')
for i,l in enumerate(ls):
    if l.startswith(f'| {so} |'):
        c=l.split('|'); c[5]=f' {tt} '; ls[i]='|'.join(c)
open(p,'w').write('\n'.join(ls))
PY
}

case "$1" in
  --tiep)
    SID=$(grep "^| $2 |" "$SO" | awk -F'|' '{gsub(/ /,"",$5); print $5}')
    [ -z "$SID" ] && { echo "Không có việc #$2"; exit 1; }
    screen -ls | grep -q "\.viec-$2[[:space:]]" && { echo "Việc #$2 vẫn đang chạy, chờ nó báo rồi trả lời"; exit 1; }
    chay "$2" --resume "$SID" "David trả lời qua Telegram: $3"
    doi_trang_thai "$2" "đang chạy (tiếp $(date +%H:%M))"; echo "Việc #$2 đang làm tiếp" ;;
  --dung)
    screen -S "viec-$2" -X quit 2>/dev/null && doi_trang_thai "$2" "đã dừng $(date +%H:%M)" && echo "Đã dừng việc #$2" || echo "Việc #$2 không chạy" ;;
  *)
    [ -z "$1" ] && { echo "Thiếu yêu cầu"; exit 1; }
    SO_VIEC=$(( $(cat "$TT/so-viec-giao" 2>/dev/null || echo 0) + 1 )); echo $SO_VIEC > "$TT/so-viec-giao"
    SID=$(uuidgen | tr 'A-Z' 'a-z')
    printf '| %s | %s | %s | %s | đang chạy |\n' "$SO_VIEC" "$(date '+%Y-%m-%d %H:%M')" "$(echo "$*" | tr '|\n' '/ ' | cut -c1-120)" "$SID" >> "$SO"
    chay "$SO_VIEC" --session-id "$SID" "$(LOI_DAN $SO_VIEC)

Yêu cầu nguyên văn của David: $*"
    echo "Đã giao việc #$SO_VIEC" ;;
esac
