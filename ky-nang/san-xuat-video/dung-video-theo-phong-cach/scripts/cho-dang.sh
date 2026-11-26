#!/bin/zsh
# BẢN CUỐI CHỜ ĐĂNG TRÊN MAC (David 20/11/2026: "những kết quả cuối cùng mà tôi chưa đăng thì vẫn cần phải có trong mac để có khi đăng";
# "tôi chỉ quan tâm đến các kết quả cuối thôi"). Mac giữ đúng bản cuối chưa đăng ở ~/Movies/cho-dang/<tập>/ (cùng mẫu thanh-pham:
# ban-dai/, highlight/, bài đăng, ảnh bìa). Bản gốc + dự án dựng chỉ ở Drive (luu-drive.sh).
# ĐỦ HẾT LÊN DRIVE (David 25/11/2026: "khi quy trình đã làm ra sản phẩm gì thì đều tải lên drive đầy đủ hết"): mỗi tập có cả bản xem
# nhẹ (gui tự làm), và mỗi buổi gốc có thư mục _buoi-<buổi>/ (lệnh buoi) chứa kết quả chung: hướng nào ra gì, phân hướng, lời, nhật ký.
#   zsh cho-dang.sh lay <tập>    chép Drive thanh-pham/<tập>/ → ~/Movies/cho-dang/<tập>/, so khớp từng file
#   zsh cho-dang.sh gui <tập>    làm bản xem nhẹ nếu chưa có, chép ~/Movies/cho-dang/<tập>/ → Drive thanh-pham/<tập>/, chờ lên mây, so khớp
#   zsh cho-dang.sh buoi <buổi>  gom ~/Movies/<buổi>/ (doc-truoc.md, phan-huong.md, lời, lỗi kỹ năng) + nhật ký 3 hướng
#                                → ~/Movies/cho-dang/_buoi-<buổi>/ → Drive thanh-pham/_buoi-<buổi>/, so khớp
#   zsh cho-dang.sh xong <tập>   ĐĂNG XONG: kiểm thanh-pham/<tập>/ có đủ và đã lên mây, ghi da-dang.txt trên Drive, rồi mới xoá bản Mac
# Không khớp / chưa lên mây → giữ bản Mac, báo lỗi.
setopt nullglob
V=$1 TAP=${2:t}
[ -n "$V" ] && [ -n "$TAP" ] || { echo "cách dùng: cho-dang.sh lay|gui|buoi|xong <tập>"; exit 2; }
BO_NAO=${0:A:h}/../../../..
source ${0:A:h}/drive-chung.sh || exit 1   # $G, da_len (Mac và Windows/WSL2)
# Máy ngoài Mac không đồng bộ Drive (David 26/11/2026): gui, buoi vẫn làm đủ bản trên máy, không chép lên đâu
KHONG_DRIVE=0
if ! tim_drive; then
  [[ $OSTYPE == darwin* ]] && { echo "✗ Không thấy Google Drive: $DRIVE_HUONG_DAN"; exit 1; }
  KHONG_DRIVE=1 G=/khong-co-drive
  [ $V = lay ] && { echo "✗ lay cần Drive: $DRIVE_HUONG_DAN"; exit 1; }
fi
# đường dẫn để David mở bằng Windows Explorer
o_dau() { command -v wslpath >/dev/null && wslpath -w "$(realpath "$1")" || echo "$1"; }
TP="$G/thanh-pham/$TAP" CD="$HOME/Movies/cho-dang/$TAP"
EX=(--exclude .DS_Store --exclude da-dang.txt)
[[ $OSTYPE == darwin* ]] || EX+=(--no-perms --modify-window=2)   # ổ Drive trên Windows không giữ quyền tệp Linux, giờ chỉ tới giây
khop() { [ -z "$(rsync -a --dry-run -i $EX "$1/" "$2/" | grep -v '^\.d')" ]; }   # mọi file nguồn đã có y hệt ở đích
cho_len() { for i in {1..480}; do o=$(da_len "$1"); [[ $o == *"chua_len=0 "* ]] && return 0; sleep 15; done; echo "✗ quá 2 giờ chưa lên mây ($o)"; return 1; }
# Bản xem nhẹ cho điện thoại (< 30 MB với video 10 phút): 854 px, 250 kbit/s; làm cho mỗi bản dài chưa có
xem_nhe() { local v x; for v in "$1"/ban-dai/*.mp4; do x="$1/xem-nhanh-${v:t:r}.mp4"; [ "$x" -nt "$v" ] && continue
  ffmpeg -v error -y -i "$v" -vf scale=854:-2 -c:v libx264 -preset veryfast -b:v 250k -maxrate 300k -bufsize 600k \
    -c:a aac -b:a 64k -movflags +faststart "$x" || { echo "✗ không làm được bản xem nhẹ ${x:t}"; return 1; }
  # ffmpeg có lúc báo lỗi đọc (thiếu bộ nhớ trên ổ Windows gắn vào WSL) mà vẫn thoát 0 → bản nhẹ bị cụt; so thời lượng, lệch quá 1 giây thì xoá và báo
  local a=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$v") b=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$x")
  (( ${a:-0} - ${b:-0} < 1 && ${b:-0} - ${a:-0} < 1 )) || { rm -f "$x"; echo "✗ bản xem nhẹ ${x:t} cụt (${b%.*}s / ${a%.*}s): chạy lại, hoặc làm bằng ffmpeg trên Windows"; return 1; }; done; }
LEN="đã lên mây"; [ $DRIVE_KIEM_DUOC = 1 ] || LEN="đã vào ổ Drive (lên mây: xem biểu tượng Google Drive trên Windows)"
gui_drive() { [ $KHONG_DRIVE = 1 ] && return 0; mkdir -p "$TP"; rsync -a $EX "$CD/" "$TP/" || exit 1; cho_len "$TP" || exit 1
  khop "$CD" "$TP" || { echo "✗ Drive chưa khớp bản trên máy"; exit 1; }; }
case $V in
  lay)
    [ -d "$TP" ] || { echo "✗ không có $TP"; exit 1; }
    mkdir -p "$CD"; rsync -a $EX "$TP/" "$CD/" && khop "$TP" "$CD" || { echo "✗ chép về chưa khớp"; exit 1; }
    echo "✓ $TAP: bản cuối đã ở ~/Movies/cho-dang/$TAP ($(du -sh "$CD" | cut -f1))";;
  gui)
    [ -d "$CD" ] || { echo "✗ không có $CD"; exit 1; }
    xem_nhe "$CD" || exit 1
    gui_drive
    [ $KHONG_DRIVE = 1 ] && { print -r -- "✓ $TAP: bản cuối ở $(o_dau "$CD") — CHƯA lên Drive (máy này không đồng bộ Drive)"; exit 0; }
    echo "✓ $TAP: thanh-pham trên Drive khớp bản trên máy ($(ls -R "$CD" | grep -c '\.') tệp), $LEN";;
  buoi)
    B=$HOME/Movies/$TAP; TP="$G/thanh-pham/_buoi-$TAP" CD="$HOME/Movies/cho-dang/_buoi-$TAP"
    for f in doc-truoc.md phan-huong.md; do [ -f $B/$f ] || { echo "✗ thiếu $B/$f (viết theo dung-video-theo-phong-cach/references/tach-theo-huong.md mục Giao)"; exit 1; }; done
    mkdir -p "$CD"; cp $B/doc-truoc.md $CD/; cp $B/phan-huong.md $CD/phan-huong-3-huong.md
    for l in $B/kiem-tra/loi-ky-nang.md $B/2-ban-day-du/kiem-tra/loi-ky-nang.md; do [ -f $l ] && { cp $l $CD/; break; }; done   # lỗi kỹ năng ở kiem-tra/ của buổi hoặc của bản đầy đủ
    for n in $BO_NAO/du-an/nhat-ky-noi-dung/huong-*.md; do cp $n $CD/nhat-ky-${n:t}; done
    PD=$B/2-ban-day-du/chuyen-dong/src/phu-de.js SRT=$B/2-ban-day-du/kiem-tra/lam-sach/ban-chep-loi.srt
    if [ -f $PD ]; then   # bản lời đã sửa (phụ đề cả buổi) → văn bản có mốc giờ
      node --no-warnings -e 'import(process.argv[1]).then(m=>{const f=s=>[s/3600,s%3600/60,s%60].map(x=>String(Math.floor(x)).padStart(2,"0")).join(":");
        require("fs").writeFileSync(process.argv[2],"# Bản chép lời cả buổi (nội bộ, không đăng)\n\n"+m.default.map(c=>`[${f(c.start)}] ${c.text.replace(/\n/g," ")}`).join("\n")+"\n")})' $PD $CD/ban-chep-loi-ca-buoi.txt || exit 1
    elif [ -f $SRT ]; then cp $SRT $CD/ban-chep-loi-ca-buoi.srt; fi
    gui_drive
    [ $KHONG_DRIVE = 1 ] && { print -r -- "✓ _buoi-$TAP: kết quả chung ở $(o_dau "$CD") — CHƯA lên Drive (máy này không đồng bộ Drive)"; exit 0; }
    echo "✓ _buoi-$TAP: kết quả chung của buổi trên Drive khớp bản trên máy ($(ls "$CD" | wc -l | tr -d ' ') tệp), $LEN";;
  xong)
    [ -d "$CD" ] || { echo "✓ $TAP: Mac không còn bản chờ đăng"; exit 0; }
    [ $KHONG_DRIVE = 1 ] && { date "+đã đăng %d/%m/%Y %H:%M" > "$CD/da-dang.txt"; print -r -- "✓ $TAP: đã ghi da-dang.txt, giữ bản ở $(o_dau "$CD") (chưa có bản trên Drive nên không xoá)"; exit 0; }
    rsync -a $EX "$CD/" "$TP/" || exit 1; cho_len "$TP" || exit 1   # thiếu gì trên Drive thì bổ sung trước
    khop "$CD" "$TP" || { echo "✗ Drive chưa khớp, giữ bản Mac"; exit 1; }
    date "+đã đăng %d/%m/%Y %H:%M" > "$TP/da-dang.txt"
    [ $DRIVE_KIEM_DUOC = 1 ] || { echo "✓ $TAP: đã ghi da-dang.txt. Máy này không hỏi được Drive → giữ bản trên máy; Drive báo xong thì xoá tay: rm -rf \"$CD\""; exit 0; }
    rm -rf "${CD:?}"; rmdir "$HOME/Movies/cho-dang" 2>/dev/null
    echo "✓ $TAP: đã đăng, bản cuối vẫn ở Drive thanh-pham/$TAP, đã xoá trên Mac";;
  *) echo "cách dùng: cho-dang.sh lay|gui|buoi|xong <tập>"; exit 2;;
esac
