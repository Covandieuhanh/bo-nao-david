#!/bin/bash
# Canh bot Sổ nhớ: launchd chạy script này suốt (KeepAlive), mỗi phút kiểm một vòng.
# Lịch tự chạy: tu-dong-hoa/lich/lich-chay.md, tới giờ mở phiên hiện trong app Claude (Remote Control), tài khoản nào cũng được.
# Tự sửa: phiên chết · thừa phiên · máy chủ Telegram chết hoặc mất kết nối mạng · phiên treo · hộp thoại chặn · đổi tài khoản (cả đổi trên app: mở sẵn đăng nhập Terminal) ·
#         làm mới ngữ cảnh 4h sáng. Việc theo giờ: tóm tắt 7h, nhắc đúng giờ (gửi thẳng, không cần Claude), sao lưu Drive 3h.
# Báo David qua Telegram (gửi thẳng) khi: chưa đăng nhập Claude · hết hạn mức · mở lại liên tục · mất mạng lâu.
# Mac ngủ / mất mạng (gặp 15–16/11: gập máy chạy pin, ngủ 15 giờ, lịch 7h bị bỏ): khi có mạng và Mac thức hẳn (hai vòng liền nhau)
#   thì chạy bù lịch lỡ (đuôi "· bù Nh"), nhắc giờ lỡ dưới 12 giờ (ghi "trễ"), gửi lại tin trong hàng chờ, gõ [SAU-MAT-MANG] vào bot, nhắn David 📶.
#   Lúc Mac chỉ tỉnh vài giây (DarkWake) thì không mở/làm mới phiên nào: phiên mở ra sẽ đông cứng khi máy ngủ lại.
export PATH="$HOME/.bun/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

GOC="$(cd "$(dirname "$0")" && pwd)"
DATA="$HOME/Documents/2-ca-nhan/so-tay"
TT="$DATA/.trang-thai"
TEN="so-tay"
KENH="$HOME/.claude/channels/so-tay"   # thư mục riêng: phiên Claude khác không thấy token nên không giành bot
TOKEN_FILE="$KENH/.env"
# Mã đăng nhập dài hạn của Claude (~1 năm, David tự tạo bằng "claude setup-token", không lên GitHub): có thì bot dùng mã này,
# không phụ thuộc đăng nhập Terminal (đăng nhập thường có lúc mất khi Mac ngủ + mất mạng lâu, gặp 17/11 19:44).
# Phiên lịch / phiên việc hiện trong app (Remote Control) vẫn cần đăng nhập thường.
MA_FILE="$KENH/claude-token"
DRIVE="$HOME/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi/sao-luu-mac/so-tay"
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

# Tên "so-tay" là đầu của "so-tay-canh" nên screen -S "so-tay" bị nhầm: luôn gọi phiên bot bằng mã đủ (12345.so-tay).
sid() { screen -ls 2>/dev/null | awk -v t=".$TEN" '$1 ~ t"$" {print $1; exit}'; }
dang_chay() { [ -n "$(sid)" ]; }
may_chu() { pgrep -fx ".*/bun server\.ts" | head -1; }  # khớp đúng tiến trình, không khớp lệnh khác có chữ "bun server.ts"
co_ma() { [ -s "$MA_FILE" ]; }
tai_khoan_bot() { co_ma && echo "ma-dai-han" || tai_khoan; } # bot dùng mã dài hạn nếu có, không thì đăng nhập thường
tai_khoan() { env -u CLAUDE_CODE_OAUTH_TOKEN claude auth status 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('email','') if d.get('loggedIn') else '')" 2>/dev/null; }
tai_khoan_app() { # tài khoản app Claude trên Mac đang dùng = thư mục phiên app vừa được ghi gần nhất (chỉ đọc tên thư mục, không đụng mã đăng nhập)
  ls -td "$HOME/Library/Application Support/Claude/claude-code-sessions"/*/*/ 2>/dev/null | head -1 | awk -F/ '{print $(NF-2)}'; }
tuoi_phien() { echo $(( $(date +%s) - $(cat "$TT/mo-luc" 2>/dev/null || echo 0) )); }
gui() { # gõ một tin vào phiên bot; lỗi nếu bot chưa sẵn sàng
  dang_chay && [ -n "$(may_chu)" ] || return 1
  # Dán qua bộ đệm của screen: "stuff" bỏ im lặng chuỗi dài hơn ~1024 byte (tin hỏi thói quen kèm việc chưa xong ~1900 byte bị mất, gặp 14/11).
  printf '%s' "$1" > "$TT/tin-go.txt"
  screen -S "$(sid)" -p 0 -X readbuf -e utf8 "$TT/tin-go.txt" && screen -S "$(sid)" -p 0 -X paste . || return 1
  sleep 2; screen -S "$(sid)" -p 0 -X stuff $'\r'
}
LS_BOT="$HOME/.claude/projects/-Users-moon-Documents-2-ca-nhan-so-tay"
da_nhan() { # $1 nội dung, $2 khoá: tin thẻ máy đã vào lịch sử phiên bot chưa (dòng có đầu tin + giờ khung ở cuối)
  find "$LS_BOT" -name '*.jsonl' -mmin -120 -print0 2>/dev/null | xargs -0 grep -hF -- "${1:0:24}" 2>/dev/null | grep -qF -- " ${2:0:16}\""; }
xoa_cho() { [ -f "$TT/cho-bot" ] && { grep -vF -- "$1" "$TT/cho-bot" > "$TT/cho-bot.tmp"; mv "$TT/cho-bot.tmp" "$TT/cho-bot"; }; }
man_hinh() { rm -f "$TT/man-hinh.txt"; screen -S "$(sid)" -p 0 -X hardcopy "$TT/man-hinh.txt" 2>/dev/null; sleep 1; LC_ALL=C tr -d '\000' < "$TT/man-hinh.txt" 2>/dev/null; }
gui_thang() { BAO_CAO_KHONG_CHO=1 bash "$GOC/bao-cao.sh" --chi-gui "$1" >/dev/null 2>&1; } # gửi David, không qua Claude (lỗi thì vòng sau tự thử lại, không vào hàng chờ)
gui_nhac() { BAO_CAO_KHONG_CHO=1 bash "$GOC/bao-cao.sh" --chi-gui --so-nho "$1" >/dev/null 2>&1; } # nhắc giờ: qua bot Sổ nhớ (cảnh báo máy, 📶 qua bot Điều hành)
tre_nhan() { # $1 "YYYY-MM-DD HH:MM" giờ hẹn: trễ quá 60 phút thì in nhãn trễ
  local t=$(date -j -f "%Y-%m-%d %H:%M" "$1" +%s 2>/dev/null || echo "$BAY")
  [ $(( BAY - t )) -gt 3600 ] && echo " (trễ, hẹn ${1:11:5} ${1:8:2}/${1:5:2} — Mac ngủ hoặc mất mạng)"; }
bot_nghi_giay() { local f=$(ls -t "$LS_BOT"/*.jsonl 2>/dev/null | head -1); [ -n "$f" ] && echo $(( $(date +%s) - $(stat -f %m "$f") )) || echo 99999; }
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
  screen -dmS "$TEN" -h 2000 bash -c "cd '$DATA' && { [ -s '$MA_FILE' ] && export CLAUDE_CODE_OAUTH_TOKEN=\$(cat '$MA_FILE'); }; TELEGRAM_STATE_DIR=$KENH MCP_TIMEOUT=120000 ENABLE_TOOL_SEARCH=false ENABLE_CLAUDEAI_MCP_SERVERS=false CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 exec claude --channels plugin:telegram@claude-plugins-official --permission-mode dontAsk --model opus"
  date +%F > "$TT/mo-ngay"; echo "$TK" > "$TT/tai-khoan"; date +%s > "$TT/mo-luc"; rm -f "$TT/ban-tu" "$TT/mat-mang-tu" "$TT/noi-lai"
  ghi "mo phien bot ($1)"
  # Mở lại liên tục (>4 lần trong 30 phút) là có lỗi không tự sửa được.
  local gan=$(awk -v t=$(( $(date +%s) - 1800 )) '$1>t' "$TT/lan-mo" | wc -l | tr -d ' ')
  [ "$gan" -gt 4 ] && canh_bao mo-lai 3600 "đã tự mở lại $gan lần trong 30 phút (lý do cuối: $1). Cần xem lại: screen -r so-tay, nhật ký $LOG."
  sleep 25; [ -z "$(may_chu)" ] && { ghi "mo phien chua co may chu, noi lai"; noi_lai; sleep 10; }
  gui "[KHOI-DONG] Phiên mới. Đọc lướt nhom.md, không gửi gì."
}
noi_lai() { # nối lại máy chủ Telegram trong phiên (Claude đôi khi bỏ qua bước bật máy chủ lúc mở phiên)
  screen -S "$(sid)" -p 0 -X stuff "/mcp reconnect plugin:telegram:telegram"; sleep 1
  screen -S "$(sid)" -p 0 -X stuff $'\033'; sleep 0.5; screen -S "$(sid)" -p 0 -X stuff $'\r'; }
co_mang() { curl -s -m 8 -o /dev/null https://api.telegram.org; }
fm() { awk -v k="$2" 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f&&index($0,k":")==1{sub("^[^:]*:[ ]*","");print;exit}' "$1" 2>/dev/null; } # khung đầu lời giao lịch
chrome_noi() { pgrep -f "chrome-native-host chrome-extension://" >/dev/null; } # tiện ích Claude in Chrome đang nối với máy
danh_thuc_chrome() { pgrep -x "Google Chrome" >/dev/null || open -ga "Google Chrome"; } # Chrome tắt thì mở ngầm; tiện ích tự nối khi Chrome chạy
het_bu() { # $1 tên việc, $2 "YYYY-MM-DD HH:MM" giờ gốc: giờ (epoch) hết hạn chạy bù theo lich-chay.md
  local h=$(grep -E "· $1( ·|$)" "$GOC/../lich/lich-chay.md" | grep -oE 'bù [0-9]+h' | head -1 | tr -dc 0-9)
  echo $(( $(date -j -f "%Y-%m-%d %H:%M" "$2" +%s 2>/dev/null || echo "$BAY") + ${h:-1} * 3600 )); }
mo_dang_nhap() { # mất đăng nhập thường: mở Terminal "claude auth login" một lần mỗi lần mất (David bấm cho phép; không đăng nhập thay)
  [ -f "$TT/da-mo-dang-nhap" ] && return
  osascript -e 'tell application "Terminal" to activate' -e 'tell application "Terminal" to do script "claude auth login"' >/dev/null 2>&1
  touch "$TT/da-mo-dang-nhap"; ghi "mo Terminal dang nhap"; }
noi_telegram() { lsof -nP -a -p "$1" -iTCP -sTCP:ESTABLISHED 2>/dev/null | grep -q ':443'; }

while true; do
  NGAY=$(date +%F); GIO=$(date +%H); BAY=$(date +%s)
  # Mac thức hẳn và có mạng chưa: vòng trước cách quá 3 phút là máy vừa ngủ (hoặc chỉ tỉnh chốc lát).
  CUOI=$(cat "$TT/vong-cuoi" 2>/dev/null || echo "$BAY"); KHOANG=$(( BAY - CUOI ))
  ON_DINH=0; [ "$KHOANG" -lt 180 ] && ON_DINH=1
  MANG=0; co_mang && MANG=1
  if [ "$MANG" = 0 ] || [ "$ON_DINH" = 0 ]; then
    [ -f "$TT/gian-doan-tu" ] || { echo "$CUOI" > "$TT/gian-doan-tu"; ghi "gian doan (mang=$MANG, cach vong truoc ${KHOANG}s)"; }
  elif [ -f "$TT/gian-doan-tu" ]; then
    GD_TU=$(cat "$TT/gian-doan-tu"); GD=$(( BAY - GD_TU )); rm -f "$TT/gian-doan-tu"
    ghi "co mang va Mac thuc lai sau ${GD}s"
    [ "$GD" -ge 600 ] && { echo "$GD_TU $GD" > "$TT/vua-noi-lai"; : > "$TT/bu-lan-nay"; date +%s > "$TT/vua-noi-lai-luc"; }
  fi
  SAN_SANG=0; [ "$MANG" = 1 ] && [ "$ON_DINH" = 1 ] && SAN_SANG=1
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
  TK=$(tai_khoan_bot)
  if [ -z "$TK" ]; then
    ghi "chua dang nhap Claude"; dang_chay && tat_bot
    if [ "$SAN_SANG" = 1 ]; then mo_dang_nhap; canh_bao dang-nhap 21600 "Claude trong Terminal bị đăng xuất (app Claude không liên quan), bot đang tắt. Em đã mở Terminal đăng nhập: trên trình duyệt anh chọn tài khoản rồi bấm cho phép, bot tự chạy lại sau 1 phút. Muốn hết hẳn lỗi này: tạo mã dài hạn (claude setup-token, xem tu-dong-hoa/so-tay/README.md)."; fi
    sleep 60; continue
  fi

  if co_ma && [ "$SAN_SANG" = 1 ]; then
    if [ -z "$(tai_khoan)" ]; then
      mo_dang_nhap; canh_bao dang-nhap-lich 21600 "Claude trong Terminal bị đăng xuất. Bot vẫn chạy (mã dài hạn), nhưng phiên lịch 7:00 và việc giao cần đăng nhập: em đã mở Terminal, anh bấm cho phép trên trình duyệt."
    else rm -f "$TT/da-mo-dang-nhap"; fi
  fi
  co_ma || rm -f "$TT/da-mo-dang-nhap"
  # 1. Đúng một phiên bot đang chạy.
  SO=$(screen -ls 2>/dev/null | awk -v t=".$TEN" '$1 ~ t"$"' | wc -l | tr -d ' ')
  if [ "$SO" -gt 1 ]; then ghi "co $SO phien, tat bot thua"; tat_bot; fi
  if [ "$SAN_SANG" = 0 ]; then
    :  # Mac chỉ tỉnh chốc lát hoặc chưa có mạng: giữ nguyên phiên bot, chờ thức hẳn
  elif ! dang_chay; then
    tat_bot; mo_bot "phien khong chay"
  elif [ "$TK" != "$(cat "$TT/tai-khoan" 2>/dev/null)" ]; then
    tat_bot; mo_bot "doi tai khoan"
  elif [ "$GIO" -ge 4 ] && [ "$(cat "$TT/mo-ngay" 2>/dev/null)" != "$NGAY" ] && [ "$(bot_nghi_giay)" -gt 300 ]; then
    # làm mới chỉ khi bot nghỉ ≥ 5 phút: đang xử lý tin (vd tin dồn sau mất mạng) mà tắt thì tin mất
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
        NHAT=$(ls -t "$HOME/.claude/projects/-Users-moon-Documents-2-ca-nhan-so-tay/"*.jsonl 2>/dev/null | head -1)
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
  # Lỡ giờ (Mac ngủ, mất mạng) thì còn nhắc trong 12 giờ, tin ghi "trễ".
  BAY_GIO=$(date "+%Y-%m-%d %H:%M"); TU=$(date -v-12H "+%Y-%m-%d %H:%M")
  grep -E '^- [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2} · ' "$DATA/nhac-viec.md" 2>/dev/null | grep -vE '· \((đã|da) ' | while IFS= read -r dong; do
    LUC="${dong:2:16}"
    if [[ ! "$LUC" > "$BAY_GIO" ]] && [[ ! "$LUC" < "$TU" ]] && ! grep -qF -- "- $LUC · " "$TT/da-nhac" 2>/dev/null; then
      gui_nhac "⏰ Nhắc: ${dong:21}$(tre_nhan "$LUC")" && echo "$dong" >> "$TT/da-nhac" && ghi "nhac $LUC"
    fi
  done
  # Nhắc lặp: "- mỗi ngày / mỗi thứ 2, thứ 5 / mỗi ngày 15 HH:MM · nội dung" (nhac-lap.py tính lần tới giờ).
  # Dòng kết bằng "+ việc chưa xong" thì tin kèm việc [ ] trong danh-sach-viec.md (kể cả việc không hạn).
  python3 -I "$GOC/nhac-lap.py" --bu 720 "$DATA/nhac-viec.md" "$TT/da-nhac-lap" "$DATA/danh-sach-viec.md" 2>>"$LOG" | while IFS=$'\t' read -r khoa nd; do
    if [[ "$nd" == \[* ]] && [ "$HERMES" = 1 ]; then
      # Bot chính là Hermes: nhắc có thẻ máy do lịch Hermes tự soạn và gửi, ở đây chỉ đánh dấu để không gửi trùng.
      echo "$khoa" >> "$TT/da-nhac-lap"; continue
    fi
    if [[ "$nd" == \[* ]]; then
      # Nội dung bắt đầu bằng thẻ máy (vd [HOI-THOI-QUEN]): gõ vào phiên bot để bot đọc sổ rồi tự soạn tin.
      # Gõ xong chưa tính là đã gửi: chỉ đánh dấu khi tin hiện trong lịch sử phiên bot (gặp 14/11 16:00: gõ vào phiên sắp tắt, tin mất).
      # Chưa thấy sau 5 phút thì gõ lại (tối đa 3 lần); bot đang mở lại thì chờ; quá 3 lần hoặc trễ quá 30 phút thì gửi thẳng chữ cố định (bỏ thẻ).
      if da_nhan "$nd" "$khoa"; then
        echo "$khoa" >> "$TT/da-nhac-lap"; xoa_cho "$khoa"; ghi "nhac lap qua bot ${khoa:0:16} (bot da nhan)"; continue
      fi
      CHO=$(awk -F'\t' -v k="$khoa" '$1==k {print $2" "$3}' "$TT/cho-bot" 2>/dev/null | tail -1)
      GO_LUC=${CHO% *}; LAN=${CHO#* }; [ -z "$CHO" ] && { GO_LUC=0; LAN=0; }
      TRE=$(( BAY - $(date -j -f "%Y-%m-%d %H:%M" "${khoa:0:16}" +%s 2>/dev/null || echo "$BAY") ))
      if [ "$LAN" -lt 3 ] && [ "$TRE" -lt 1800 ]; then
        [ $(( BAY - GO_LUC )) -lt 300 ] && continue          # vừa gõ, chờ bot nhận (bot bận thì tin xếp hàng)
        [ "$(tuoi_phien)" -lt 90 ] && continue                # phiên vừa mở, còn đang khởi động
        if gui "$nd ${khoa:0:16}"; then
          printf '%s\t%s\t%s\n' "$khoa" "$BAY" "$(( LAN + 1 ))" >> "$TT/cho-bot"; ghi "go nhac lap vao bot ${khoa:0:16} lan $(( LAN + 1 ))"
        fi
        continue                                              # bot chưa sẵn sàng: phút sau thử lại
      fi
      ghi "bot khong nhan nhac lap ${khoa:0:16} (lan $LAN, tre ${TRE}s), gui thang"; xoa_cho "$khoa"
      nd="${nd#*] }"
    fi
    gui_nhac "⏰ Nhắc: ${nd//$'\x1f'/$'\n'}$(tre_nhan "${khoa:0:16}")" && echo "$khoa" >> "$TT/da-nhac-lap" && ghi "nhac lap ${khoa:0:16}"
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
    SIDV=$(grep "^| $N |" "$DATA/viec-da-giao.md" 2>/dev/null | awk -F'|' '{gsub(/ /,"",$5); print $5}')
    F="$HOME/.claude/projects/-Users-moon-Documents-bo-nao-david/$SIDV.jsonl"
    if [ -n "$SIDV" ] && [ -f "$F" ] && [ $(( BAY - $(stat -f %m "$F") )) -gt 43200 ]; then
      bash "$GOC/giao-viec.sh" --dung "$N" >/dev/null; bash "$GOC/giao-viec.sh" --trang-thai "$N" "đã đóng (nghỉ 12 giờ)"; ghi "dong viec $N"
    fi
  done

  # Đổi tài khoản trên app Claude: Claude trong Terminal giữ đăng nhập riêng, không tự đổi theo (phiên việc chạy nhưng không hiện trên app, gặp 14/11/2026).
  # Máy mở sẵn Terminal chạy "claude auth login" và nhắn David bấm cho phép trên trình duyệt. Không tự đăng nhập thay David.
  TKA=$(tai_khoan_app)
  if [ -n "$TKA" ] && [ "$TKA" != "$(cat "$TT/tai-khoan-app" 2>/dev/null)" ]; then
    if [ -s "$TT/tai-khoan-app" ]; then
      ghi "app doi tai khoan -> mo dang nhap Terminal"
      osascript -e 'tell application "Terminal" to activate' -e 'tell application "Terminal" to do script "claude auth logout; claude auth login"' >/dev/null 2>&1
      gui_thang "🔑 Anh vừa đổi tài khoản trên app Claude. Em đã mở Terminal để đăng nhập lại Claude trong Terminal: trên trình duyệt anh chọn đúng tài khoản mới rồi bấm cho phép. Xong bước này phiên việc mới hiện trên app."
    fi
    echo "$TKA" > "$TT/tai-khoan-app"
  fi

  # Lịch tự chạy (tu-dong-hoa/lich/lich-chay.md): tới giờ mở một phiên hiện trong app Claude, tài khoản nào cũng được.
  # Chỉ chạy khi có mạng và Mac thức hẳn; chưa thì để đó (không đánh dấu), lần lỡ được chạy bù trong hạn "· bù Nh".
  [ "$SAN_SANG" = 1 ] && python3 -I "$GOC/nhac-lap.py" "$GOC/../lich/lich-chay.md" "$TT/da-lich-chay" /dev/null 2>>"$LOG" | while IFS=$'\t' read -r khoa nd; do
    ID="${nd%% *}"; GOC_LUC="${khoa:0:16}"; LG="$GOC/../lich/loi-giao/$ID.md"
    # Việc cần Chrome ("chrome: bat-buoc"): chờ tiện ích Claude in Chrome nối xong mới mở phiên (17/11: Mac thức 06:56, lịch 07:00 chạy khi Chrome chưa nối, ra bản trống).
    # Chờ 10 phút chưa nối thì nhắn David; còn dưới 15 phút hạn bù thì chạy luôn (phiên tự chờ thêm và ghi cảnh báo).
    CHO_F="$TT/cho-chrome-$ID"
    if [ "$(fm "$LG" chrome)" = "bat-buoc" ] && ! chrome_noi; then
      [ -f "$CHO_F" ] || { echo "$BAY" > "$CHO_F"; ghi "lich $ID cho Chrome noi"; }
      danh_thuc_chrome
      [ $(( BAY - $(cat "$CHO_F") )) -ge 600 ] && canh_bao "chrome-$ID" 21600 "việc lịch $ID đang chờ Chrome: tiện ích Claude in Chrome chưa nối. Anh mở Chrome, bấm biểu tượng Claude trên thanh tiện ích là máy tự chạy tiếp."
      [ $(( $(het_bu "$ID" "$GOC_LUC") - BAY )) -gt 900 ] && continue
      ghi "lich $ID het cho Chrome, chay luon"
    fi
    [ -f "$CHO_F" ] && { ghi "lich $ID: Chrome da noi sau $(( BAY - $(cat "$CHO_F") ))s"; rm -f "$CHO_F"; }
    if [ -n "$(tre_nhan "$GOC_LUC")" ]; then
      bash "$GOC/../lich/chay-lich.sh" "$ID" "$GOC_LUC" >/dev/null 2>>"$LOG" && { ghi "chay bu lich $ID (goc $GOC_LUC)"; echo "$ID (lịch ${GOC_LUC:11:5} ${GOC_LUC:8:2}/${GOC_LUC:5:2})" >> "$TT/bu-lan-nay"; }
    else
      bash "$GOC/../lich/chay-lich.sh" "$ID" >/dev/null 2>>"$LOG" && ghi "chay lich $ID (phien hien trong app)"
    fi
    echo "$khoa" >> "$TT/da-lich-chay"
    echo "$BAY|$ID|0" >> "$TT/mo-lich"
    [ -n "$(fm "$LG" kiem)" ] && echo "$BAY|$ID|$GOC_LUC|1" >> "$TT/kiem-lich"
  done

  # Canh sớm (19/11: phiên lịch kẹt ở hộp hỏi "tin cậy thư mục" suốt 3 tiếng): 3 phút sau khi mở phiên lịch, chụp màn hình.
  # Hộp hỏi tin cậy thư mục của chính bộ não (bo-nao-david, bo-nao-veltrix) thì tự chọn "Yes"; hộp lạ thì nhắn David ngay kèm màn hình.
  if [ -s "$TT/mo-lich" ]; then
    : > "$TT/mo-lich.tmp"
    while IFS='|' read -r MLUC MID MLAN; do
      [ -z "$MID" ] && continue
      [ $(( BAY - MLUC )) -lt 180 ] && { echo "$MLUC|$MID|$MLAN" >> "$TT/mo-lich.tmp"; continue; }
      MS=$(screen -ls 2>/dev/null | awk -v t=".lich-$MID" '$1 ~ t"$" {print $1; exit}'); [ -z "$MS" ] && continue
      rm -f "$TT/man-lich.txt"; screen -S "$MS" -p 0 -X hardcopy "$TT/man-lich.txt" 2>/dev/null; sleep 1
      MH=$(LC_ALL=C tr -d '\000' < "$TT/man-lich.txt" 2>/dev/null | LC_ALL=C grep -av '^[[:space:]]*$'); rm -f "$TT/man-lich.txt"
      echo "$MH" | LC_ALL=C grep -aqE "Enter to confirm|Esc to cancel|Do you trust|\(y/n\)" || continue   # phiên đang chạy bình thường
      if [ "$MLAN" -lt 2 ] && echo "$MH" | LC_ALL=C grep -aqE "trust" && echo "$MH" | LC_ALL=C grep -aqE "Documents/bo-nao-(david|veltrix)"; then
        screen -S "$MS" -p 0 -X stuff $'\033[B'; sleep 1; screen -S "$MS" -p 0 -X stuff $'\r'
        ghi "canh som lich $MID: hop hoi tin cay thu muc bo nao, tu chon Yes"; echo "$BAY|$MID|$(( MLAN + 1 ))" >> "$TT/mo-lich.tmp"
      else
        gui_thang "⚠️ Phiên lịch $MID đang kẹt ở một câu hỏi trên màn hình (máy không tự trả lời được):
$(echo "$MH" | head -15 | cut -c1-120)
Anh mở phiên \"Lịch · $MID\" trong app Claude trả lời giúp." && ghi "canh som lich $MID: ket hop hoi la, bao David" || echo "$MLUC|$MID|$MLAN" >> "$TT/mo-lich.tmp"
      fi
    done < "$TT/mo-lich"
    mv "$TT/mo-lich.tmp" "$TT/mo-lich"
  fi

  # Tự thử khi lệnh mở phiên lịch bị sửa (luật: thêm việc mới không được làm hỏng việc cũ): chay-lich.sh đổi thì mở thử một phiên y hệt,
  # trả lời được thì ghi sổ; kẹt thì nhắn David ngay, khỏi đợi tới giờ lịch.
  CL_SUM=$(md5 -q "$GOC/../lich/chay-lich.sh" 2>/dev/null)
  if [ "$SAN_SANG" = 1 ] && [ -n "$CL_SUM" ] && [ "$CL_SUM" != "$(cat "$TT/chay-lich.md5" 2>/dev/null)" ]; then
    echo "$CL_SUM" > "$TT/chay-lich.md5"
    ( if KQ=$(bash "$GOC/../lich/thu-mo-phien.sh" 2>&1); then ghi "tu thu chay-lich.sh: dat"
      else ghi "tu thu chay-lich.sh: hong"; gui_thang "⚠️ Lệnh mở phiên lịch vừa bị sửa và mở thử thì hỏng (lịch sáng mai sẽ kẹt):
$(echo "$KQ" | tail -12 | cut -c1-120)"; fi ) &
  fi

  # Kiểm kết quả lịch ("kiem: <file>", {ngay} = ngày của lịch): 90 phút sau khi mở phiên mà file chưa có / chưa mới / còn dòng CHUA-DOC-DUOC
  # (Chrome chưa nối, hết hạn mức, phiên treo) thì tự chạy lại một lần; lần 2 vẫn chưa được thì nhắn David.
  if [ "$SAN_SANG" = 1 ] && [ -s "$TT/kiem-lich" ]; then
    : > "$TT/kiem-lich.tmp"
    while IFS='|' read -r LUC KID KGOC LAN; do
      [ -z "$KID" ] && continue
      if [ $(( BAY - LUC )) -lt 5400 ]; then echo "$LUC|$KID|$KGOC|$LAN" >> "$TT/kiem-lich.tmp"; continue; fi
      KLG="$GOC/../lich/loi-giao/$KID.md"; KF="$(fm "$KLG" kiem)"; KF="${KF//\{ngay\}/${KGOC:0:10}}"; KF="${KF/#\~/$HOME}"
      if [ -f "$KF" ] && [ "$(stat -f %m "$KF")" -ge "$LUC" ] && ! grep -q "CHUA-DOC-DUOC" "$KF"; then
        ghi "kiem lich $KID ($KGOC): dat"
      elif [ "$(fm "$KLG" chrome)" = "bat-buoc" ] && ! chrome_noi && [ "$(het_bu "$KID" "$KGOC")" -gt "$BAY" ]; then
        danh_thuc_chrome; echo "$LUC|$KID|$KGOC|$LAN" >> "$TT/kiem-lich.tmp"  # chờ Chrome nối rồi mới chạy lại
        canh_bao "chrome-$KID" 21600 "việc lịch $KID chưa đọc được vì Chrome chưa nối. Anh mở Chrome, bấm biểu tượng Claude trên thanh tiện ích là máy tự chạy lại."
      elif [ "$LAN" -lt 2 ] && [ "$(het_bu "$KID" "$KGOC")" -gt "$BAY" ]; then
        bash "$GOC/../lich/chay-lich.sh" "$KID" "$KGOC" >/dev/null 2>>"$LOG" && { ghi "kiem lich $KID ($KGOC): chua dat, chay lai"; echo "$BAY|$KID|0" >> "$TT/mo-lich"; }
        echo "$BAY|$KID|$KGOC|$(( LAN + 1 ))" >> "$TT/kiem-lich.tmp"
      else
        gui_thang "⚠️ Việc lịch $KID (${KGOC:11:5} ${KGOC:8:2}/${KGOC:5:2}) chạy $LAN lần vẫn chưa ra kết quả đủ. Anh mở phiên \"Lịch · $KID\" trong app Claude xem giúp (có thể Chrome chưa nối, trang đòi đăng nhập, hoặc hết hạn mức Claude)." \
          && ghi "kiem lich $KID ($KGOC): that bai, bao David" || echo "$LUC|$KID|$KGOC|$LAN" >> "$TT/kiem-lich.tmp"
      fi
    done < "$TT/kiem-lich"
    mv "$TT/kiem-lich.tmp" "$TT/kiem-lich"
  fi

  # Hàng chờ gửi lại: tin bao-cao.sh gửi hỏng (mất mạng) được gửi lại khi có mạng, kèm giờ gốc.
  if [ "$MANG" = 1 ]; then
    for f in $(ls "$TT/hang-cho-gui/"*.txt 2>/dev/null | sort); do
      LUC0=$(head -1 "$f"); NOI=$(tail -n +2 "$f"); SN=""; [[ "$f" == *.so-nho.txt ]] && SN="--so-nho"
      if BAO_CAO_KHONG_CHO=1 bash "$GOC/bao-cao.sh" --chi-gui $SN "↻ Gửi lại tin lúc ${LUC0:11:5} ${LUC0:8:2}/${LUC0:5:2} (lúc đó mất mạng):
$NOI" >/dev/null 2>&1; then
        rm -f "$f"; ghi "gui lai tin $LUC0"; echo "$LUC0" >> "$TT/gui-lai-lan-nay"
      else break; fi
    done
  fi

  # Vừa có mạng lại sau ≥ 10 phút: gõ [SAU-MAT-MANG] vào bot (rà tin dồn), rồi nhắn David một tin 📶. Chờ 3 phút cho lịch bù và hàng chờ chạy xong.
  if [ -f "$TT/vua-noi-lai" ] && [ "$SAN_SANG" = 1 ] && [ $(( BAY - $(cat "$TT/vua-noi-lai-luc") )) -ge 180 ]; then
    read -r TU_LUC GD < "$TT/vua-noi-lai"
    GD_CHU="$(( GD / 3600 )) giờ $(( GD % 3600 / 60 )) phút"
    if [ "$HERMES" != 1 ] && [ ! -f "$TT/da-go-sau-mat-mang" ]; then
      gui "[SAU-MAT-MANG] Mac vừa có mạng lại sau $GD_CHU (từ $(date -r "$TU_LUC" '+%H:%M %d/%m')). Rà tin David nhắn trong lúc đó còn chưa xử lý thì xử lý ngay." && touch "$TT/da-go-sau-mat-mang"
    fi
    BU=$(paste -sd ',' "$TT/bu-lan-nay" 2>/dev/null | sed 's/,/, /g'); GL=$(wc -l < "$TT/gui-lai-lan-nay" 2>/dev/null | tr -d ' ')
    TIN="📶 Mac có mạng lại sau $GD_CHU (ngủ hoặc mất mạng từ $(date -r "$TU_LUC" '+%H:%M %d/%m')).
Chạy bù: ${BU:-không có việc lịch nào lỡ}.
Gửi lại: ${GL:-0} tin gửi hỏng.
Anh nhắn gì trong lúc đó mà chưa thấy em trả lời thì nhắn lại giúp em."
    if gui_thang "$TIN"; then
      ghi "bao David co mang lai (bu: ${BU:-0}; gui lai: ${GL:-0})"; rm -f "$TT/vua-noi-lai" "$TT/vua-noi-lai-luc" "$TT/bu-lan-nay" "$TT/gui-lai-lan-nay" "$TT/da-go-sau-mat-mang"
    fi
  fi

  # Bot Điều hành (tu-dong-hoa/dieu-hanh/bot.py, launchd com.david.dieu-hanh giữ sống): đã có token mà quá 10 phút không có nhịp thì khởi động lại, vẫn không được thì báo qua Sổ nhớ.
  if [ -s "$HOME/.claude/channels/dieu-hanh/.env" ] && [ "$SAN_SANG" = 1 ]; then
    NH=$(( BAY - $(cat "$TT/dieu-hanh-nhip" 2>/dev/null || echo 0) ))
    if [ "$NH" -gt 600 ]; then
      if [ ! -f "$TT/dieu-hanh-da-khoi-dong" ]; then
        launchctl kickstart -k "gui/$(id -u)/com.david.dieu-hanh" 2>/dev/null; touch "$TT/dieu-hanh-da-khoi-dong"; ghi "bot dieu hanh mat nhip ${NH}s, khoi dong lai"
      else
        if [ $(( BAY - $(cat "$TT/bao-dieu-hanh" 2>/dev/null || echo 0) )) -ge 10800 ]; then
          gui_nhac "⚠️ Máy Mac: bot Điều hành không nhận lệnh (mất nhịp ${NH}s): nút duyệt và giao việc ở đó tạm không chạy, anh nhắn việc ở đây em vẫn giao được. Xem $TT/dieu-hanh.log, cài lại: bash tu-dong-hoa/dieu-hanh/cai-dat.sh" && date +%s > "$TT/bao-dieu-hanh" && ghi "canh bao dieu-hanh"
        fi
      fi
    else rm -f "$TT/dieu-hanh-da-khoi-dong"; fi
  fi

  # Nhịp sống cho lệnh kiểm tra sức khoẻ.
  echo "$BAY $(dang_chay && echo phien-ok || echo phien-tat) $([ -n "$(may_chu)" ] && echo telegram-ok || echo telegram-tat)" > "$TT/nhip"
  date +%s > "$TT/vong-cuoi"
  sleep 60
done
