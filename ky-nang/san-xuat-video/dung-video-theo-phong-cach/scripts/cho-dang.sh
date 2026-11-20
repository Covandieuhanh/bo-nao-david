#!/bin/zsh
# BẢN CUỐI CHỜ ĐĂNG TRÊN MAC (David 20/11/2026: "những kết quả cuối cùng mà tôi chưa đăng thì vẫn cần phải có trong mac để có khi đăng";
# "tôi chỉ quan tâm đến các kết quả cuối thôi"). Mac giữ đúng bản cuối chưa đăng ở ~/Movies/cho-dang/<tập>/ (cùng khuôn thanh-pham:
# ban-dai/, highlight/, bài đăng, ảnh bìa). Bản gốc + dự án dựng chỉ ở Drive (luu-drive.sh).
#   zsh cho-dang.sh lay <tập>    chép Drive thanh-pham/<tập>/ → ~/Movies/cho-dang/<tập>/, so khớp từng file
#   zsh cho-dang.sh gui <tập>    chép ~/Movies/cho-dang/<tập>/ → Drive thanh-pham/<tập>/ (vừa render xong), chờ lên mây, so khớp
#   zsh cho-dang.sh xong <tập>   ĐĂNG XONG: kiểm thanh-pham/<tập>/ có đủ và đã lên mây, ghi da-dang.txt trên Drive, rồi mới xoá bản Mac
# Không khớp / chưa lên mây → giữ bản Mac, báo lỗi.
setopt nullglob
V=$1 TAP=${2:t}
[ -n "$V" ] && [ -n "$TAP" ] || { echo "cách dùng: cho-dang.sh lay|gui|xong <tập>"; exit 2; }
source ${0:A:h}/drive-chung.sh || exit 1   # $G, da_len (Mac và Windows/WSL2)
tim_drive || { echo "✗ Google Drive chưa mở"; exit 1; }
TP="$G/thanh-pham/$TAP" CD="$HOME/Movies/cho-dang/$TAP"
EX=(--exclude .DS_Store --exclude da-dang.txt)
khop() { [ -z "$(rsync -a --dry-run -i $EX "$1/" "$2/" | grep -v '^\.d')" ]; }   # mọi file nguồn đã có y hệt ở đích
cho_len() { for i in {1..480}; do o=$(da_len "$1"); [[ $o == *"chua_len=0 "* ]] && return 0; sleep 15; done; echo "✗ quá 2 giờ chưa lên mây ($o)"; return 1; }
case $V in
  lay)
    [ -d "$TP" ] || { echo "✗ không có $TP"; exit 1; }
    mkdir -p "$CD"; rsync -a $EX "$TP/" "$CD/" && khop "$TP" "$CD" || { echo "✗ chép về chưa khớp"; exit 1; }
    echo "✓ $TAP: bản cuối đã ở ~/Movies/cho-dang/$TAP ($(du -sh "$CD" | cut -f1))";;
  gui)
    [ -d "$CD" ] || { echo "✗ không có $CD"; exit 1; }
    mkdir -p "$TP"; rsync -a $EX "$CD/" "$TP/" || exit 1; cho_len "$TP" || exit 1
    khop "$CD" "$TP" || { echo "✗ Drive chưa khớp bản Mac"; exit 1; }
    echo "✓ $TAP: thanh-pham trên Drive khớp bản Mac, đã lên mây";;
  xong)
    [ -d "$CD" ] || { echo "✓ $TAP: Mac không còn bản chờ đăng"; exit 0; }
    rsync -a $EX "$CD/" "$TP/" || exit 1; cho_len "$TP" || exit 1   # thiếu gì trên Drive thì bổ sung trước
    khop "$CD" "$TP" || { echo "✗ Drive chưa khớp, giữ bản Mac"; exit 1; }
    date "+đã đăng %d/%m/%Y %H:%M" > "$TP/da-dang.txt"
    [ $DRIVE_KIEM_DUOC = 1 ] || { echo "✓ $TAP: đã ghi da-dang.txt. Máy này không hỏi được Drive → giữ bản trên máy; Drive báo xong thì xoá tay: rm -rf \"$CD\""; exit 0; }
    rm -rf "${CD:?}"; rmdir "$HOME/Movies/cho-dang" 2>/dev/null
    echo "✓ $TAP: đã đăng, bản cuối vẫn ở Drive thanh-pham/$TAP, đã xoá trên Mac";;
  *) echo "cách dùng: cho-dang.sh lay|gui|xong <tập>"; exit 2;;
esac
