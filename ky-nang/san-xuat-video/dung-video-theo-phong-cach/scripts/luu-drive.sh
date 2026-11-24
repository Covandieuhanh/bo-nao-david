#!/bin/zsh
# Đưa một tập đã dọn lên Drive rồi xoá trên Mac (luật: ghi nhớ video-chuyen-qua-drive — Mac chỉ giữ việc đang làm).
#   zsh luu-drive.sh ~/Movies/tap-<tên>      (hoặc ~/Movies/vlog/<tên>; chạy nền vì chờ Drive tải lên)
# Chép vào Drive "sao-luu-mac/video/<tập>" (vlog: .../Movies/vlog/<tên>), bỏ node_modules/.remotion/.cache/.DS_Store,
# (gốc đã có y hệt ở tu-lieu-goc/<tập>/ thì bỏ qua), chờ mọi file lên mây xong, so khớp từng file, giải phóng bản cache Drive, rồi mới xoá tập trên Mac.
# Không khớp / quá giờ → giữ nguyên bản Mac, báo lỗi (Claude báo David).
setopt nullglob
T=${1:A}; [ -d "$T" ] || { echo "✗ không có thư mục $1"; exit 1; }
case "$T" in "$HOME/Movies/tap-"*|"$HOME/Movies/vlog/"*) ;; *) echo "✗ chỉ nhận ~/Movies/tap-<tên> hoặc ~/Movies/vlog/<tên>"; exit 1;; esac
source ${0:A:h}/drive-chung.sh || exit 1   # $G, da_len, giai_phong (Mac và Windows/WSL2)
tim_drive || { echo "✗ Không thấy Google Drive: $DRIVE_HUONG_DAN"; exit 1; }
REL=${T#$HOME/Movies/}; DST="$G/sao-luu-mac/video/${REL:h}"; [ "${REL:h}" = . ] && DST="$G/sao-luu-mac/video"
EX=(--exclude node_modules --exclude .remotion --exclude .cache --exclude .DS_Store)
# Gốc đã có y hệt ở tu-lieu-goc/<tập>/ (chép lúc bắt đầu làm) thì không tải lần hai
VG="$G/tu-lieu-goc/${T:t}"
for f in "$T"/1-goc/*(.); do g="$VG/${f:t}"; [ -f "$g" ] && [ $(kich_thuoc "$f") = $(kich_thuoc "$g") ] && EX+=(--exclude "/${T:t}/1-goc/${f:t}") && echo "  gốc đã ở tu-lieu-goc: ${f:t}"; done
mkdir -p "$DST"; echo "$(date +%T) tải ${REL} → sao-luu-mac/video/${REL}"
rsync -a $EX "$T" "$DST/" || { echo "✗ lỗi chép, giữ bản Mac"; exit 1; }
for i in {1..960}; do o=$(da_len "$DST/${T:t}"); [[ $o == *"chua_len=0 "* ]] && break; sleep 15; done
[[ $o == *"chua_len=0 "* ]] || { echo "✗ quá 4 giờ chưa lên mây hết ($o), giữ bản Mac"; exit 1; }
d=$(rsync -a --dry-run -i $EX "$T" "$DST/" | grep -v '^\.d' | head -3)
[ -n "$d" ] && { echo "✗ không khớp, giữ bản Mac: $d"; exit 1; }
[ $DRIVE_KIEM_DUOC = 1 ] || { echo "✓ đã chép lên thư mục Drive và khớp từng file. Máy này không hỏi được Drive đã tải lên mây chưa → GIỮ bản trên máy; khi biểu tượng Google Drive báo xong, xoá tay: rm -rf \"$T\""; exit 0; }
giai_phong "$DST/${T:t}" >/dev/null
rm -rf "$T"; echo "✓ đã lên Drive ($o), đã xoá trên Mac. Ghi loại tập vào du-an/kho-drive.md"
