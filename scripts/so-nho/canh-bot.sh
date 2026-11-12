#!/bin/bash
# Canh bot Sổ nhớ: launchd chạy script này suốt (KeepAlive), mỗi phút kiểm một vòng.
# Tự sửa: phiên chết · thừa phiên · máy chủ Telegram chết hoặc mất kết nối mạng · phiên treo · hộp thoại chặn · đổi tài khoản ·
#         làm mới ngữ cảnh 4h sáng. Việc theo giờ: tóm tắt 7h, nhắc đúng giờ (gửi thẳng, không cần Claude), sao lưu Drive 3h.
# Báo David qua Telegram (gửi thẳng) khi: chưa đăng nhập Claude · hết hạn mức · mở lại liên tục · mất mạng lâu.
export PATH="$HOME/.bun/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

GOC="$(cd "$(dirname "$0")" && pwd)"
DATA="$HOME/Documents/2-ca-nhan/so-nho"
TT="$DATA/.trang-thai"
TEN="so-nho"
KENH="$HOME/.claude/channels/so-nho"   # thư mục riêng: phiên Claude khác không thấy token nên không giành bot
TOKEN_FILE="$KENH/.env"
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
# Giữ Mac không ngủ (khi cắm điện) chừng nào script còn chạy. Gập máy thì macOS vẫn ngủ.
caffeinate -is -w $$ &

# Tên "so-nho" là đầu của "so-nho-canh" nên screen -S "so-nho" bị nhầm: luôn gọi phiên bot bằng mã đủ (12345.so-nho).
sid() { screen -ls 2>/dev/null | awk -v t=".$TEN" '$1 ~ t"$" {print $1; exit}'; }
dang_chay() { [ -n "$(sid)" ]; }
may_chu() { pgrep -fx ".*/bun server\.ts" | head -1; }  # khớp đúng tiến trình, không khớp lệnh khác có chữ "bun server.ts"
tai_khoan() { claude auth status 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('email','') if d.get('loggedIn') else '')" 2>/dev/null; }
tuoi_phien() { echo $(( $(date +%s) - $(cat "$TT/mo-luc" 2>/dev/null || echo 0) )); }
gui() { # gõ một tin vào phiên bot; lỗi nếu bot chưa sẵn sàng
  dang_chay && [ -n "$(may_chu)" ] || return 1
  screen -S "$(sid)" -p 0 -X stuff "$1"; sleep 1; screen -S "$(sid)" -p 0 -X stuff $'\r'
}
man_hinh() { rm -f "$TT/man-hinh.txt"; screen -S "$(sid)" -p 0 -X hardcopy "$TT/man-hinh.txt" 2>/dev/null; sleep 1; tr -d '\000' < "$TT/man-hinh.txt" 2>/dev/null; }
gui_thang() { bash "$GOC/bao-cao.sh" --chi-gui "$1" >/dev/null 2>&1; } # gửi David, không qua Claude
canh_bao() { # $1 khoá, $2 số giây giữa hai lần báo, $3 nội dung
  local f="$TT/bao-$1"
  [ $(( $(date +%s) - $(cat "$f" 2>/dev/null || echo 0) )) -lt "$2" ] && return
  gui_thang "⚠️ Máy Mac: $3" && date +%s > "$f" && ghi "canh bao $1"
}
tat_bot() { # tắt mọi phiên bot (kể cả phiên thừa) và máy chủ Telegram còn sót
  screen -ls 2>/dev/null | awk -v t=".$TEN" '$1 ~ t"$" {print $1}' | while read -r id; do screen -S "$id" -X quit; done
  sleep 3; pkill -f "^claude --channels" 2>/dev/null; sleep 1; }
mo_bot() { # $1 lý do
  echo "$(date +%s)" >> "$TT/lan-mo"
  screen -dmS "$TEN" -h 2000 bash -c "cd '$DATA' && TELEGRAM_STATE_DIR=$KENH MCP_TIMEOUT=120000 ENABLE_TOOL_SEARCH=false ENABLE_CLAUDEAI_MCP_SERVERS=false CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 exec claude --channels plugin:telegram@claude-plugins-official --permission-mode dontAsk --model opus"
  date +%F > "$TT/mo-ngay"; echo "$TK" > "$TT/tai-khoan"; date +%s > "$TT/mo-luc"; rm -f "$TT/ban-tu" "$TT/mat-mang-tu" "$TT/noi-lai"
  ghi "mo phien bot ($1)"
  # Mở lại liên tục (>4 lần trong 30 phút) là có lỗi không tự sửa được.
  local gan=$(awk -v t=$(( $(date +%s) - 1800 )) '$1>t' "$TT/lan-mo" | wc -l | tr -d ' ')
  [ "$gan" -gt 4 ] && canh_bao mo-lai 3600 "đã tự mở lại $gan lần trong 30 phút (lý do cuối: $1). Cần xem lại: screen -r so-nho, nhật ký $LOG."
  sleep 25; [ -z "$(may_chu)" ] && { ghi "mo phien chua co may chu, noi lai"; noi_lai; sleep 10; }
  gui "[KHOI-DONG] Phiên mới. Đọc lướt nhom.md, không gửi gì."
}
noi_lai() { # nối lại máy chủ Telegram trong phiên (Claude đôi khi bỏ qua bước bật máy chủ lúc mở phiên)
  screen -S "$(sid)" -p 0 -X stuff "/mcp reconnect plugin:telegram:telegram"; sleep 1
  screen -S "$(sid)" -p 0 -X stuff $'\033'; sleep 0.5; screen -S "$(sid)" -p 0 -X stuff $'\r'; }
co_mang() { curl -s -m 8 -o /dev/null https://api.telegram.org; }
noi_telegram() { lsof -nP -a -p "$1" -iTCP -sTCP:ESTABLISHED 2>/dev/null | grep -q ':443'; }

while true; do
  NGAY=$(date +%F); GIO=$(date +%H); BAY=$(date +%s)
  # Giữ nhật ký gọn.
  [ "$(wc -l < "$LOG" 2>/dev/null || echo 0)" -gt 3000 ] && tail -1500 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"
  [ -f "$TT/lan-mo" ] && tail -50 "$TT/lan-mo" > "$TT/lan-mo.tmp" && mv "$TT/lan-mo.tmp" "$TT/lan-mo"

  # Bot chính là Hermes (.trang-thai/bot-chinh ghi "hermes"): không giữ phiên bot Sổ nhớ nữa, chỉ còn nhắc giờ, sao lưu, đóng phiên việc.
  # Tóm tắt sáng và nhắc có thẻ máy ([HOI-THOI-QUEN]…) là việc của lịch Hermes. Quay về bot cũ: xoá file bot-chinh.
  HERMES=0; [ "$(cat "$TT/bot-chinh" 2>/dev/null)" = "hermes" ] && HERMES=1
  if [ "$HERMES" = 1 ]; then
    dang_chay && { tat_bot; ghi "bot chinh la Hermes: tat phien bot So nho"; }
  else
  if [ ! -s "$TOKEN_FILE" ]; then ghi "chua co token"; sleep 300; continue; fi
  TK=$(tai_khoan)
  if [ -z "$TK" ]; then
    ghi "chua dang nhap Claude"; dang_chay && tat_bot
    canh_bao dang-nhap 21600 "Claude trên Mac chưa đăng nhập (hoặc hết hạn), bot đang tắt. Mở Claude trên Mac đăng nhập lại, bot tự chạy lại sau 5 phút."
    sleep 300; continue
  fi

  # 1. Đúng một phiên bot đang chạy.
  SO=$(screen -ls 2>/dev/null | awk -v t=".$TEN" '$1 ~ t"$"' | wc -l | tr -d ' ')
  if [ "$SO" -gt 1 ]; then ghi "co $SO phien, tat bot thua"; tat_bot; fi
  if ! dang_chay; then
    tat_bot; mo_bot "phien khong chay"
  elif [ "$TK" != "$(cat "$TT/tai-khoan" 2>/dev/null)" ]; then
    tat_bot; mo_bot "doi tai khoan"
  elif [ "$GIO" -ge 4 ] && [ "$(cat "$TT/mo-ngay" 2>/dev/null)" != "$NGAY" ]; then
    tat_bot; mo_bot "lam moi hang ngay"
  elif [ "$(tuoi_phien)" -gt 40 ]; then
    MC=$(may_chu)
    MH=$(man_hinh)
    if [ -z "$MC" ]; then
      # 2. Máy chủ Telegram không chạy (Claude bỏ qua lúc mở phiên, bị giành, 409 kéo dài): gõ /mcp reconnect, 3 lần không được thì mở lại phiên.
      LAN=$(( $(cat "$TT/noi-lai" 2>/dev/null || echo 0) + 1 ))
      if [ "$LAN" -le 3 ]; then echo "$LAN" > "$TT/noi-lai"; ghi "noi lai Telegram lan $LAN"; noi_lai
      else rm -f "$TT/noi-lai"; tat_bot; mo_bot "khong co may chu Telegram"; fi
    elif ! noi_telegram "$MC"; then
      # 3. Máy chủ còn nhưng không giữ kết nối tới Telegram.
      [ -f "$TT/mat-mang-tu" ] || echo "$BAY" > "$TT/mat-mang-tu"
      MAT=$(( BAY - $(cat "$TT/mat-mang-tu") ))
      if co_mang; then
        [ "$MAT" -gt 180 ] && { tat_bot; mo_bot "mat ket noi Telegram ${MAT}s"; }
      else
        ghi "khong co mang ${MAT}s"
        [ "$MAT" -gt 1800 ] && canh_bao mat-mang 7200 "Mac mất mạng hơn 30 phút. Có mạng lại bot tự nối, tin nhắn trong lúc mất mạng vẫn được nhận sau."
      fi
    else
      rm -f "$TT/mat-mang-tu" "$TT/noi-lai"
      # 4. Hết hạn mức gói Claude: báo David một lần mỗi 3 giờ.
      if echo "$MH" | grep -qiE "usage limit|limit reached|hit your limit|reached your|out of (extra )?usage"; then
        canh_bao han-muc 10800 "gói Claude đã hết hạn mức, bot tạm không trả lời được. Hạn mức mở lại theo giờ ghi trên màn hình Claude; tin nhắn vẫn được giữ."
      fi
      # 5. Hộp thoại chặn (chọn mục, xác nhận): bấm Esc.
      if echo "$MH" | grep -qE "Enter to (confirm|select)|to navigate"; then
        ghi "hop thoai chan, bam Esc"; screen -S "$(sid)" -p 0 -X stuff $'\033'
      fi
      # 6. Phiên treo: đang làm (có "esc to interrupt") liên tục quá 10 phút thì ngắt, quá 15 phút thì mở lại.
      if echo "$MH" | grep -q "esc to interrupt"; then
        [ -f "$TT/ban-tu" ] || echo "$BAY" > "$TT/ban-tu"
        BAN=$(( BAY - $(cat "$TT/ban-tu") ))
        if [ "$BAN" -gt 900 ]; then tat_bot; mo_bot "treo ${BAN}s"
        elif [ "$BAN" -gt 600 ] && [ ! -f "$TT/da-ngat" ]; then ghi "ban ${BAN}s, ngat"; screen -S "$(sid)" -p 0 -X stuff $'\033'; touch "$TT/da-ngat"; fi
      else
        rm -f "$TT/ban-tu" "$TT/da-ngat"
        # 7. Gọn ngữ cảnh (đỡ token): bot nghỉ quá 30 phút thì /clear, tin sau bắt đầu sạch (mọi thứ đã nằm trong file).
        NHAT=$(ls -t "$HOME/.claude/projects/-Users-moon-Documents-2-ca-nhan-so-nho/"*.jsonl 2>/dev/null | head -1)
        if [ -n "$NHAT" ]; then
          DAU="$NHAT $(stat -f %m "$NHAT")"
          if [ $(( BAY - $(stat -f %m "$NHAT") )) -gt 1800 ] && [ "$DAU" != "$(cat "$TT/da-gon" 2>/dev/null)" ]; then
            screen -S "$(sid)" -p 0 -X stuff "/clear"; sleep 1; screen -S "$(sid)" -p 0 -X stuff $'\r'
            echo "$DAU" > "$TT/da-gon"; ghi "nghi 30 phut, /clear"
          fi
        fi
      fi
    fi
  fi
  fi  # hết phần giữ phiên bot Sổ nhớ

  # Tóm tắt sáng: chỉ đánh dấu đã gửi khi gửi được (bot chưa sẵn sàng thì thử lại phút sau, tới 12h).
  if [ "$HERMES" != 1 ] && [ "$GIO" -ge 7 ] && [ "$GIO" -lt 12 ] && [ "$(cat "$TT/tom-tat" 2>/dev/null)" != "$NGAY" ]; then
    HOM_QUA=$(grep -c "^$(date -v-1d +%F).*mo phien bot" "$LOG")
    gui "[TOM-TAT-SANG] Gửi David tóm tắt hôm nay $NGAY. Cuối tin thêm một dòng: bot tự mở lại $HOM_QUA lần hôm qua." \
      && echo "$NGAY" > "$TT/tom-tat" && ghi "gui tom tat"
  fi

  # Nhắc đúng giờ: dòng "- YYYY-MM-DD HH:MM · nội dung" trong nhac-viec.md. Gửi thẳng qua Telegram nên bot hỏng vẫn nhắc được.
  # Chỉ nhắc mục tới giờ trong 60 phút qua (Mac ngủ dậy vẫn kịp), bỏ dòng đã dời/xong/bỏ; mỗi giờ hẹn chỉ nhắc một lần dù dòng bị sửa chữ.
  BAY_GIO=$(date "+%Y-%m-%d %H:%M"); TU=$(date -v-60M "+%Y-%m-%d %H:%M")
  grep -E '^- [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2} · ' "$DATA/nhac-viec.md" 2>/dev/null | grep -vE '· \((đã|da) ' | while IFS= read -r dong; do
    LUC="${dong:2:16}"
    if [[ ! "$LUC" > "$BAY_GIO" ]] && [[ ! "$LUC" < "$TU" ]] && ! grep -qF -- "- $LUC · " "$TT/da-nhac" 2>/dev/null; then
      gui_thang "⏰ Nhắc: ${dong:21}" && echo "$dong" >> "$TT/da-nhac" && ghi "nhac $LUC"
    fi
  done
  # Nhắc lặp: "- mỗi ngày / mỗi thứ 2, thứ 5 / mỗi ngày 15 HH:MM · nội dung" (nhac-lap.py tính lần tới giờ).
  # Dòng kết bằng "+ việc chưa xong" thì tin kèm việc [ ] trong viec-can-lam.md (kể cả việc không hạn).
  python3 -I "$GOC/nhac-lap.py" "$DATA/nhac-viec.md" "$TT/da-nhac-lap" "$DATA/viec-can-lam.md" 2>>"$LOG" | while IFS=$'\t' read -r khoa nd; do
    if [[ "$nd" == \[* ]] && [ "$HERMES" = 1 ]; then
      # Bot chính là Hermes: nhắc có thẻ máy do lịch Hermes tự soạn và gửi, ở đây chỉ đánh dấu để không gửi trùng.
      echo "$khoa" >> "$TT/da-nhac-lap"; continue
    fi
    if [[ "$nd" == \[* ]]; then
      # Nội dung bắt đầu bằng thẻ máy (vd [HOI-THOI-QUEN]): gõ vào phiên bot để bot đọc sổ rồi tự soạn tin.
      # Bot chưa sẵn sàng thì gửi thẳng chữ cố định (bỏ thẻ) để David vẫn được nhắc.
      if gui "$nd ${khoa:0:16}"; then echo "$khoa" >> "$TT/da-nhac-lap"; ghi "nhac lap qua bot ${khoa:0:16}"; continue; fi
      nd="${nd#*] }"
    fi
    gui_thang "⏰ Nhắc: ${nd//$'\x1f'/$'\n'}" && echo "$khoa" >> "$TT/da-nhac-lap" && ghi "nhac lap ${khoa:0:16}"
  done
  [ -f "$TT/da-nhac-lap" ] && tail -500 "$TT/da-nhac-lap" > "$TT/da-nhac-lap.tmp" && mv "$TT/da-nhac-lap.tmp" "$TT/da-nhac-lap"

  if [ "$GIO" -ge 3 ] && [ -d "$(dirname "$DRIVE")" ] && [ "$(cat "$TT/sao-luu" 2>/dev/null)" != "$NGAY" ]; then
    mkdir -p "$DRIVE" && rsync -a --exclude ".trang-thai" --exclude ".claude" "$DATA/" "$DRIVE/" \
      && echo "$NGAY" > "$TT/sao-luu" && ghi "sao luu Drive"
  fi

  # Múi giờ của Mac cho bot (CLAUDE.md nhập file này). Đổi múi (David chỉnh đồng hồ Mac) thì mở lại bot để nhận.
  MG="Múi giờ của Mac hiện là $(date +%Z) (UTC$(date +%z | sed 's/\(..\)$/:\1/')). Mọi giờ trong sổ nhớ và nhac-viec.md theo múi này."
  if [ "$MG" != "$(cat "$TT/mui-gio.md" 2>/dev/null)" ]; then
    echo "$MG" > "$TT/mui-gio.md"; ghi "mui gio: $MG"; dang_chay && { tat_bot; mo_bot "doi mui gio"; }
  fi

  # Phiên việc giao qua Telegram nghỉ quá 12 giờ thì đóng cho nhẹ máy (lịch sử vẫn còn trong app Claude; nhắn tiếp thì tự mở lại).
  screen -ls 2>/dev/null | grep -oE '\.viec-[0-9]+' | tr -d '.' | sed 's/viec-//' | while read -r N; do
    SIDV=$(grep "^| $N |" "$DATA/viec-giao.md" 2>/dev/null | awk -F'|' '{gsub(/ /,"",$5); print $5}')
    F="$HOME/.claude/projects/-Users-moon-Documents-David-Claude/$SIDV.jsonl"
    if [ -n "$SIDV" ] && [ -f "$F" ] && [ $(( BAY - $(stat -f %m "$F") )) -gt 43200 ]; then
      bash "$GOC/giao-viec.sh" --dung "$N" >/dev/null; bash "$GOC/giao-viec.sh" --trang-thai "$N" "đã đóng (nghỉ 12 giờ)"; ghi "dong viec $N"
    fi
  done

  # Nhịp sống cho lệnh kiểm tra sức khoẻ.
  echo "$BAY $(dang_chay && echo phien-ok || echo phien-tat) $([ -n "$(may_chu)" ] && echo telegram-ok || echo telegram-tat)" > "$TT/nhip"
  sleep 60
done
