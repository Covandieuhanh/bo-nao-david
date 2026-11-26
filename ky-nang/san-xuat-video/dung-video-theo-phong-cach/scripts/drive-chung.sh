# Dùng chung cho luu-drive.sh, cho-dang.sh: tìm thư mục Google Drive và kiểm file đã lên mây, trên mọi máy.
#   source drive-chung.sh  → $G (gốc "Drive của tôi"), tim_drive, da_len <thư mục>, giai_phong <thư mục>, $DRIVE_KIEM_DUOC (1/0)
# Mac: Google Drive cho máy tính (~/Library/CloudStorage), kiểm lên mây bằng kiem-tai-len-drive.swift.
# Windows (WSL2): KHÔNG đồng bộ Drive thành ổ trên máy (David 26/11/2026, du-an/kho-drive.md mục "Máy Windows") → tim_drive
# không tự tìm ổ Drive; video gốc tải bằng link, kết quả ở lại trên máy. Chỉ khi đặt DRIVE_GOC mới chép vào thư mục đó
# (không hỏi được trạng thái tải lên → không tự xoá bản trên máy).
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
  DRIVE_HUONG_DAN="máy này không đồng bộ Drive (du-an/kho-drive.md, mục Máy Windows): video gốc tải bằng link, kết quả ở trên máy"
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
kich_thuoc() { wc -c < "$1" | tr -d ' '; }   # thay stat -f %z (chỉ Mac có)
