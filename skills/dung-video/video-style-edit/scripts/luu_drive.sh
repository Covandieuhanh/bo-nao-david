#!/bin/zsh
# Đưa một tập đã dọn lên Drive rồi xoá trên Mac (luật: ghi nhớ video-chuyen-qua-drive — Mac chỉ giữ việc đang làm).
#   zsh luu_drive.sh ~/Movies/tap-<tên>      (hoặc ~/Movies/vlog/<tên>; chạy nền vì chờ Drive tải lên)
# Chép vào Drive "Sao-luu-mac/Movies/<tập>" (vlog: .../Movies/vlog/<tên>), bỏ node_modules/.remotion/.cache/.DS_Store,
# chờ mọi file lên mây xong, so khớp từng file, giải phóng bản cache Drive, rồi mới xoá tập trên Mac.
# Không khớp / quá giờ → giữ nguyên bản Mac, báo lỗi (Claude báo David).
setopt nullglob
T=${1:A}; [ -d "$T" ] || { echo "✗ không có thư mục $1"; exit 1; }
case "$T" in "$HOME/Movies/tap-"*|"$HOME/Movies/vlog/"*) ;; *) echo "✗ chỉ nhận ~/Movies/tap-<tên> hoặc ~/Movies/vlog/<tên>"; exit 1;; esac
G="$HOME/Library/CloudStorage/GoogleDrive-covandieuhanh@gmail.com/Drive của tôi"
[ -d "$G" ] || { echo "✗ Google Drive chưa mở (không thấy $G)"; exit 1; }
REL=${T#$HOME/Movies/}; DST="$G/Sao-luu-mac/Movies/${REL:h}"; [ "${REL:h}" = . ] && DST="$G/Sao-luu-mac/Movies"
BIN=~/.cache/video-style-edit/drive; mkdir -p $BIN; SC=${0:A:h}
for t in upcheck evict; do [ $BIN/$t -nt $SC/drive_$t.swift ] || swiftc -O $SC/drive_$t.swift -o $BIN/$t || exit 1; done
EX=(--exclude node_modules --exclude .remotion --exclude .cache --exclude .DS_Store)
mkdir -p "$DST"; echo "$(date +%T) tải ${REL} → Sao-luu-mac/Movies/${REL}"
rsync -a $EX "$T" "$DST/" || { echo "✗ lỗi chép, giữ bản Mac"; exit 1; }
for i in {1..960}; do o=$($BIN/upcheck "$DST/${T:t}"); [[ $o == *"chua_len=0 "* ]] && break; sleep 15; done
[[ $o == *"chua_len=0 "* ]] || { echo "✗ quá 4 giờ chưa lên mây hết ($o), giữ bản Mac"; exit 1; }
d=$(rsync -a --dry-run -i $EX "$T" "$DST/" | grep -v '^\.d' | head -3)
[ -n "$d" ] && { echo "✗ không khớp, giữ bản Mac: $d"; exit 1; }
$BIN/evict "$DST/${T:t}" >/dev/null
rm -rf "$T"; echo "✓ đã lên Drive ($o), đã xoá trên Mac. Ghi loại tập vào dang-lam/kho-drive.md"
