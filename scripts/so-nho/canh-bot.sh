#!/bin/bash
# Canh bot Sổ nhớ: launchd chạy script này suốt (KeepAlive).
# - Giữ Mac thức, giữ phiên bot chạy trong screen tên "so-nho".
# - Mở lại phiên khi lỗi, khi đổi tài khoản Claude, và mỗi ngày lúc 4h (làm mới ngữ cảnh).
# - 7h sáng nhắc bot gửi tóm tắt; 3h sáng sao lưu sổ nhớ lên Drive.
export PATH="$HOME/.bun/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

DATA="$HOME/Documents/2-ca-nhan/so-nho"
TT="$DATA/.trang-thai"
TEN="so-nho"
TOKEN_FILE="$HOME/.claude/channels/so-nho/.env"  # thư mục riêng: phiên Claude khác không thấy token nên không giành bot
DRIVE="$HOME/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi/Sao-luu-mac/So-nho"
mkdir -p "$TT"
LOG="$TT/canh-bot.log"
ghi() { echo "$(date '+%F %T') $*" >> "$LOG"; }

# Chỉ một bản canh chạy: bản mới tắt bản cũ còn sót.
CU=$(cat "$TT/canh.pid" 2>/dev/null)
if [ -n "$CU" ] && [ "$CU" != "$$" ] && kill -0 "$CU" 2>/dev/null; then kill "$CU"; sleep 1; fi
echo $$ > "$TT/canh.pid"

# launchd xếp tiến trình nền vào hàng ưu tiên thấp (đọc/sửa file chậm 10 giây mỗi lần): gỡ ra cho bot chạy như app thường.
taskpolicy -B -p $$ 2>/dev/null; taskpolicy -t 0 -l 0 -p $$ 2>/dev/null

# Giữ Mac không ngủ (khi cắm điện) chừng nào script còn chạy.
caffeinate -is -w $$ &

dang_chay() { screen -ls 2>/dev/null | grep -q "[0-9]\.$TEN[[:space:]]"; }
tai_khoan() { claude auth status 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('email','') if d.get('loggedIn') else '')" 2>/dev/null; }
gui() { # gõ một tin vào phiên bot
  screen -S "$TEN" -p 0 -X stuff "$1"; sleep 1; screen -S "$TEN" -p 0 -X stuff $'\r'
}
tat_bot() { # tắt mọi phiên bot (kể cả phiên thừa)
  screen -ls 2>/dev/null | awk -v t=".$TEN" '$1 ~ t"$" {print $1}' | while read -r id; do screen -S "$id" -X quit; done
  sleep 3; }
mo_bot() {
  screen -dmS "$TEN" -h 2000 bash -c "cd '$DATA' && TELEGRAM_STATE_DIR=$HOME/.claude/channels/so-nho MCP_TIMEOUT=120000 ENABLE_TOOL_SEARCH=false ENABLE_CLAUDEAI_MCP_SERVERS=false CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 exec claude --channels plugin:telegram@claude-plugins-official --permission-mode dontAsk --model haiku --debug-file $TT/debug.log"
  date +%F > "$TT/mo-ngay"; echo "$TK" > "$TT/tai-khoan"
  ghi "mo phien bot"
  sleep 25; gui "[KHOI-DONG] Phiên mới. Đọc lướt nhom.md, không gửi gì."
}

while true; do
  NGAY=$(date +%F); GIO=$(date +%H)
  if [ ! -s "$TOKEN_FILE" ]; then ghi "chua co token"; sleep 300; continue; fi
  TK=$(tai_khoan)
  if [ -z "$TK" ]; then
    ghi "chua dang nhap Claude"; dang_chay && tat_bot; sleep 300; continue
  fi

  SO=$(screen -ls 2>/dev/null | awk -v t=".$TEN" '$1 ~ t"$"' | wc -l | tr -d ' ')
  if [ "$SO" -gt 1 ]; then ghi "co $SO phien, tat bot thua"; tat_bot; fi
  if ! dang_chay; then
    mo_bot
  elif [ "$TK" != "$(cat "$TT/tai-khoan" 2>/dev/null)" ]; then
    ghi "doi tai khoan, mo lai"; tat_bot; mo_bot
  elif [ "$GIO" -ge 4 ] && [ "$(cat "$TT/mo-ngay" 2>/dev/null)" != "$NGAY" ]; then
    ghi "lam moi hang ngay"; tat_bot; mo_bot
  fi

  if [ "$GIO" -ge 7 ] && [ "$GIO" -lt 12 ] && [ "$(cat "$TT/tom-tat" 2>/dev/null)" != "$NGAY" ]; then
    gui "[TOM-TAT-SANG] Gửi David tóm tắt hôm nay $NGAY."; echo "$NGAY" > "$TT/tom-tat"; ghi "gui tom tat"
  fi

  # Nhắc đúng giờ: dòng "- YYYY-MM-DD HH:MM · nội dung" trong nhac-viec.md, tới giờ thì gửi một lần.
  BAY_GIO=$(date "+%Y-%m-%d %H:%M")
  grep -E '^- [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2} · ' "$DATA/nhac-viec.md" 2>/dev/null | while IFS= read -r dong; do
    LUC="${dong:2:16}"
    if [[ ! "$LUC" > "$BAY_GIO" ]] && ! grep -qxF -- "$dong" "$TT/da-nhac" 2>/dev/null; then
      echo "$dong" >> "$TT/da-nhac"; gui "[NHAC-VIEC] ${dong:21}"; ghi "nhac $LUC"; sleep 5
    fi
  done

  if [ "$GIO" -ge 3 ] && [ -d "$(dirname "$DRIVE")" ] && [ "$(cat "$TT/sao-luu" 2>/dev/null)" != "$NGAY" ]; then
    mkdir -p "$DRIVE" && rsync -a --exclude ".trang-thai" --exclude ".claude" "$DATA/" "$DRIVE/" \
      && echo "$NGAY" > "$TT/sao-luu" && ghi "sao luu Drive"
  fi
  sleep 60
done
