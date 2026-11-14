# Chỗ lưu dự án theo TẬP (David chốt 2026-11-07): mọi thứ cùng một nội dung gốc nằm chung một thư mục.
#   ~/Movies/tap-<tên>/1-goc/            file gốc (liên kết cứng / bản chép)
#   ~/Movies/tap-<tên>/2-ban-day-du/        dự án bản dài (podcast / video tự quay)
#   ~/Movies/tap-<tên>/3-doan-noi-bat/      kế hoạch cắt + clip-<id>/ (mỗi clip một dự án)
#   ~/Movies/vlog/<tên>/                 vlog (tên ngắn bắt đầu bằng vlog-)
# Dùng: source noi_luu.sh; P=$(noi_luu <tên-ngắn>)   — tên "hl-<tên>-<id>" = clip highlight của tập <tên>.
noi_luu() {
  local N=$1 R
  case $N in
    hl-*)   R=${N#hl-}; echo ~/Movies/tap-${R%-*}/3-doan-noi-bat/clip-${R##*-};;
    vlog-*) echo ~/Movies/vlog/${N#vlog-};;
    *)      echo ~/Movies/tap-$N/2-ban-day-du;;
  esac
}
# Đặt file gốc vào 1-goc của tập (liên kết cứng, không tốn chỗ; khác ổ thì chép). Bỏ qua clip highlight và vlog.
luu_goc() {
  local SRC=$1 N=$2 D
  case $N in hl-*|vlog-*) return 0;; esac
  D=~/Movies/tap-$N/1-goc; mkdir -p "$D"
  [ -e "$D/${SRC:t}" ] || ln "$SRC" "$D/${SRC:t}" 2>/dev/null || cp "$SRC" "$D/${SRC:t}"
}
