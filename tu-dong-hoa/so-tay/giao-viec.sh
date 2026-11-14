#!/bin/bash
# Bot Sổ nhớ giao một việc cho phiên Claude Code thật, chạy trên Mac ở chế độ Remote Control:
# phiên hiện như khung chat bình thường trong app Claude trên điện thoại và claude.ai/code, David xem và gõ tiếp được.
# Dùng: bash giao-viec.sh "<yêu cầu nguyên văn của David>"     → in ra số việc
#       bash giao-viec.sh --tiep <số> "<lời David>"             → gõ vào phiên đó (phiên đã đóng thì mở lại)
#       bash giao-viec.sh --dung <số>                           → đóng phiên đó
#       bash giao-viec.sh --trang-thai <số> "<trạng thái>"      → ghi trạng thái (bao-cao.sh gọi khi phiên báo xong/hỏi)
NAO="$HOME/Documents/David.Claude"
DATA="$HOME/Documents/2-ca-nhan/so-tay"
TT="$DATA/.trang-thai"
SO="$DATA/viec-da-giao.md"
mkdir -p "$TT"
[ -e "$SO" ] || printf '# Việc giao cho Claude qua Telegram\n\n| # | Giao lúc | Việc | Phiên | Trạng thái |\n|---|---|---|---|---|\n' > "$SO"
export PATH="$HOME/.bun/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

LOI_DAN() { cat <<EOF
Đây là việc David giao qua Telegram (việc #$1). Phiên này là phiên Claude Code bình thường ở chế độ Remote Control:
David có thể xem và gõ vào đây từ app Claude trên điện thoại hoặc claude.ai/code, hoặc nhắn qua bot Telegram (lời sẽ được gõ vào phiên này).
Làm theo AGENTS.md và skill đúng với việc, như mọi phiên khác.
Phiên chạy toàn quyền, tự làm tới kết quả, không xin phép từng bước (David chốt 12/11: chỉ quan tâm kết quả).
Xoá file, cài/gỡ phần mềm, sửa cấu hình máy hoặc Claude: máy tự cho chạy và ghi sổ; kể lại các bước đó trong tin báo cáo cuối.
Máy chỉ còn hỏi David khi đăng/gửi ra ngoài, tốn tiền, đẩy đè GitHub, xoá ổ đĩa; bị từ chối thì đừng lách, hỏi David.
Mỗi khi XONG, hoặc khi CẦN DAVID QUYẾT, chạy:
  bash tu-dong-hoa/so-tay/bao-cao.sh "#$1 ✅ Xong: … · Ở đâu: … · Còn lại: …"   hoặc   "#$1 ❓ Chờ anh: <câu hỏi rõ ràng bằng tiếng Việt, có gợi ý trả lời>"
rồi dừng lượt chờ David. Tin báo cáo ngắn, tiếng Việt, không quá 5 dòng.
EOF
}

sid_cua() { grep "^| $1 |" "$SO" | awk -F'|' '{gsub(/ /,"",$5); print $5}'; }
ten_cua() { # cắt theo chữ (không theo byte) để không hỏng chữ có dấu
  echo "Telegram #$1 · $(grep "^| $1 |" "$SO" | awk -F'|' '{print $4}' | python3 -I -c 'import sys;print(sys.stdin.read().strip()[:40])')"; }
man_hinh_cua() { screen -ls 2>/dev/null | awk -v t=".viec-$1" '$1 ~ t"$" {print $1; exit}'; }

chay() { # $1 số việc, $2 tên hiện trong app, $3 cờ phiên (--session-id / --resume) $4 id, $5 lời nhắn
  # Bỏ mọi biến môi trường CLAUDE* (phiên gọi có thể là phiên khác) và thư mục token của bot (phiên việc không được giành bot).
  # Toàn quyền (bypassPermissions) như David ngồi máy; TELEGRAM_VIEC=1 bật cổng duyệt (cong-duyet.py): đa số tự chạy + ghi sổ, chỉ gửi/đăng/tốn tiền/đẩy đè mới hỏi David.
  screen -dmS "viec-$1" -h 3000 bash -c "cd '$NAO' && for v in \$(env | grep -o '^CLAUDE[A-Z_]*'); do unset \$v; done; unset TELEGRAM_STATE_DIR ENABLE_TOOL_SEARCH ENABLE_CLAUDEAI_MCP_SERVERS CLAUDE_CODE_DISABLE_AUTO_MEMORY; export TELEGRAM_VIEC=1; exec claude $3 $4 --remote-control=\"\$1\" --permission-mode bypassPermissions \"\$0\"" "$5" "$2"
}

go_vao() { # gõ một tin vào phiên đang mở
  local s=$(man_hinh_cua "$1"); [ -z "$s" ] && return 1
  # Không bấm Esc: Esc ngắt việc đang làm. Phiên đang bận thì Claude tự xếp hàng tin này.
  screen -S "$s" -p 0 -X stuff "$2"; sleep 1; screen -S "$s" -p 0 -X stuff $'\r'
}

doi_trang_thai() { # $1 số, $2 trạng thái mới
  python3 -I - "$SO" "$1" "$2" <<'PY'
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
    SID=$(sid_cua "$2"); [ -z "$SID" ] && { echo "Không có việc #$2"; exit 1; }
    if go_vao "$2" "$3"; then
      doi_trang_thai "$2" "đang làm (tiếp $(date +%H:%M))"; echo "Đã gõ vào phiên việc #$2"
    else
      chay "$2" "$(ten_cua "$2")" --resume "$SID" "David nhắn qua Telegram: $3"
      doi_trang_thai "$2" "đang làm (mở lại $(date +%H:%M))"; echo "Phiên việc #$2 đã đóng, đã mở lại và chuyển lời"
    fi ;;
  --dung)
    S=$(man_hinh_cua "$2"); [ -n "$S" ] && screen -S "$S" -X quit && doi_trang_thai "$2" "đã đóng $(date '+%d/%m %H:%M')" && echo "Đã đóng phiên việc #$2" || echo "Việc #$2 không mở" ;;
  --trang-thai)
    doi_trang_thai "$2" "$3" ;;
  *)
    [ -z "$1" ] && { echo "Thiếu yêu cầu"; exit 1; }
    N=$(( $(cat "$TT/so-viec-giao" 2>/dev/null || echo 0) + 1 )); echo $N > "$TT/so-viec-giao"
    SID=$(uuidgen | tr 'A-Z' 'a-z')
    printf '| %s | %s | %s | %s | đang làm |\n' "$N" "$(date '+%Y-%m-%d %H:%M')" "$(echo "$*" | tr '|\n' '/ ' | python3 -I -c 'import sys;print(sys.stdin.read().strip()[:120])')" "$SID" >> "$SO"
    chay "$N" "$(ten_cua "$N")" --session-id "$SID" "$(LOI_DAN $N)

Yêu cầu nguyên văn của David: $*"
    echo "Đã giao việc #$N. Phiên tên \"$(ten_cua "$N")\" hiện trong app Claude (điện thoại, claude.ai/code)." ;;
esac
