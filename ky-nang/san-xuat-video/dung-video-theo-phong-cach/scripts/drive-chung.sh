# Dùng chung cho luu-drive.sh, cho-dang.sh: tìm thư mục Google Drive và kiểm file đã lên mây, trên mọi máy.
#   source drive-chung.sh  → $G (gốc "Drive của tôi"), tim_drive, da_len <thư mục>, giai_phong <thư mục>, $DRIVE_KIEM_DUOC (1/0)
# Mac: Google Drive cho máy tính (~/Library/CloudStorage), kiểm lên mây bằng kiem-tai-len-drive.swift.
# Windows (WSL2): giữ đăng nhập Google Drive cho máy tính ở chế độ để tệp trên mây, KHÔNG đồng bộ thư mục nào của máy và
# KHÔNG gắn ổ đó vào Ubuntu (David 26/11/2026, du-an/kho-drive.md mục "Máy Windows"). Chép lên / xuống bằng robocopy phía
# Windows (hàm tai_len, tai_ve). Không hỏi được từng tệp đã lên mây chưa → không tự xoá bản trên máy.
# Đặt DRIVE_GOC=<đường dẫn> để chỉ định tay.
_DC=${${(%):-%x}:A:h}
tim_drive() {
  local d
  if [ -n "$DRIVE_GOC" ]; then G=$DRIVE_GOC; return 0; fi
  [[ $OSTYPE == darwin* ]] || return 1
  for d in "$HOME/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi" "$HOME"/Library/CloudStorage/GoogleDrive-*/"Drive của tôi"(N) "$HOME"/Library/CloudStorage/GoogleDrive-*/"My Drive"(N); do
    [ -d "$d" ] && { G=$d; return 0; }
  done
  return 1
}
# Câu báo khi không thấy Drive (cho-dang.sh, luu-drive.sh, kiem-moi-truong.sh dùng chung)
if [[ $OSTYPE == darwin* ]]; then
  DRIVE_HUONG_DAN="mở ứng dụng Google Drive cho máy tính; thư mục ở chỗ khác thì đặt DRIVE_GOC=<đường dẫn>"
else
  DRIVE_HUONG_DAN="mở Google Drive cho máy tính (đang đăng nhập sẵn, du-an/kho-drive.md mục Máy Windows), chờ ổ Drive hiện ra rồi chạy lại"
fi
if [[ $OSTYPE == darwin* ]]; then
  DRIVE_KIEM_DUOC=1
  _DBIN=~/.cache/dung-video-theo-phong-cach/drive; mkdir -p $_DBIN
  for _t in kiem-tai-len-drive giai-phong-drive; do [ $_DBIN/$_t -nt $_DC/$_t.swift ] || swiftc -O $_DC/$_t.swift -o $_DBIN/$_t || return 1; done
  da_len() { $_DBIN/kiem-tai-len-drive "$1"; }
  giai_phong() { $_DBIN/giai-phong-drive "$1"; }
else
  DRIVE_KIEM_DUOC=0
  da_len() { echo "chua_len=0 (máy này không hỏi được Drive — xem biểu tượng Google Drive trên Windows) "; }
  giai_phong() { :; }
fi
# Máy Windows: chép qua ổ Google Drive từ phía Windows. DRIVE_WIN=<thư mục Windows> để chỉ định tay (dùng khi chạy thử).
tim_drive_windows() {
  [[ $OSTYPE != darwin* ]] && command -v robocopy.exe >/dev/null || return 1
  [ -n "$DRIVE_WIN" ] && { GW=$DRIVE_WIN; return 0; }
  GW=$(powershell.exe -NoProfile -Command '[Console]::OutputEncoding=[Text.Encoding]::UTF8; foreach($d in [char[]](68..90)){ foreach($n in "My Drive",("Drive c"+[char]0x1EE7+"a t"+[char]0xF4+"i")){ $p="${d}:\$n"; if(Test-Path -LiteralPath $p){ $p; exit } } }' 2>/dev/null | tr -d '\r')
  [ -n "$GW" ]
}
duong_win() { wslpath -w "$(realpath "$1")"; }
# _rb <nguồn Windows> <đích Windows> [tham số robocopy ...]; mã thoát của robocopy: bit 1 = có tệp cần/đã chép, bit 2 = đích có tệp thừa, từ 8 = lỗi
_rb() { local a=$1 b=$2; shift 2; robocopy.exe "$a" "$b" /E /FFT /R:3 /W:10 /NP /NJH /NJS "$@" >/dev/null; }
_so() {
  _rb "$1" "$2" /L "${@:3}"; local m=$? thua; (( m < 8 && (m & 1) == 0 )) || return 1
  (( m & 2 )) || return 0
  # desktop.ini là tệp ẩn do chính ứng dụng Drive tạo (cờ /XF của robocopy không lọc tệp thừa ở nơi nhận) → tự lọc ở đây
  thua=$(robocopy.exe "$1" "$2" /E /FFT /L /NP /NJH /NJS "${@:3}" 2>/dev/null | tr -d '
' | grep -a '\*EXTRA' | grep -aiv 'desktop\.ini')
  [ -z "$thua" ] || { echo "⚠ Nơi nhận còn tệp mà nguồn không có (bản cũ đổi tên?), chưa xoá:"; print -r -- "$thua"; }
  return 0
}
# tai_len <thư mục máy> <đường dẫn dưới "My Drive", dùng dấu /> [tham số loại trừ của robocopy ...]
tai_len() {
  local duoi=$2 nguon=$(duong_win "$1") dich="$GW\\${2//\//\\}"; shift 2
  _rb "$nguon" "$dich" "$@"; (( $? < 8 )) || { echo "✗ chép lên Drive lỗi, chạy lại lệnh này"; return 1; }
  _so "$nguon" "$dich" "$@" || { echo "✗ bản trên ổ Drive chưa khớp bản trên máy"; return 1; }
  kiem_len_may "$nguon" "$duoi" "$@"
}
# kiem_len_may <thư mục Windows> <đường dẫn dưới "My Drive"> [tham số loại trừ của robocopy ...]; chờ tối đa DRIVE_CHO giây (mặc định 2 giờ)
kiem_len_may() {
  [ -n "$DRIVE_WIN" ] && { echo "(ổ Drive giả khi chạy thử: bỏ bước kiểm trên mây)"; return 0; }
  local nguon=$1 duoi=$2 x bo=(); shift 2
  for x in "$@"; do [[ $x == /* ]] || bo+=($x); done   # /XF, /XD là cờ robocopy; phần còn lại là tên cần bỏ qua
  local py=$(powershell.exe -NoProfile -Command '(Get-Command python -ErrorAction SilentlyContinue).Source' 2>/dev/null | tr -d '\r')
  [ -n "$py" ] || { echo "✗ KHÔNG KIỂM ĐƯỢC trên mây: máy Windows chưa có Python"; return 3; }
  "$(wslpath -u "$py")" -I -X utf8 "$(wslpath -w $_DC/drive-len-may.py)" "$nguon" "$duoi" --cho ${DRIVE_CHO:-7200} --bo $bo
}
# tai_ve <đường dẫn dưới "My Drive"> <thư mục máy> [tham số loại trừ ...]
tai_ve() {
  mkdir -p "$2"; local nguon="$GW\\${1//\//\\}" dich=$(duong_win "$2"); shift 2
  _rb "$nguon" "$dich" "$@"; (( $? < 8 )) || return 1
  _so "$nguon" "$dich" "$@"
}
LUU_Y_MAY="đã xác nhận từng tệp trên mây ở dòng trên"
kich_thuoc() { wc -c < "$1" | tr -d ' '; }   # thay stat -f %z (chỉ Mac có)
