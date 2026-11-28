#!/bin/bash
# Hook SessionStart (mọi phiên Claude Code, mọi thư mục): đưa vào đầu phiên bảng chỉ đường tới bộ não của David
# bằng đường dẫn đầy đủ, lệnh bắt buộc đọc trước việc đầu tiên, và trạng thái việc hiện tại (David 28/11/2026:
# "mở bất kì phiên mới nào thì cũng mặc định phải đọc qua bộ não trước").
# Nạp sẵn (qua ~/.claude/CLAUDE.md): luật chung, sáu luật AGENTS.md, mục tiêu, hồ sơ david.md. Phần dài đọc theo việc,
# để mỗi phiên chỉ tốn khoảng 8 nghìn token nạp sẵn thay vì khoảng 40 nghìn (David chọn 28/11/2026).
# Bỏ qua: phiên bot Sổ nhớ (đã có luật riêng, tối ưu token).
REPO="$(cd "$(dirname "$0")/.." && pwd)"
VAO=$(cat 2>/dev/null)
CWD=$(printf '%s' "$VAO" | python3 -c "import json,sys
try: print(json.load(sys.stdin).get('cwd',''))
except Exception: print('')" 2>/dev/null)
case "$CWD" in "$HOME/Documents/2-ca-nhan/so-tay"*) exit 0;; esac
[ -n "${TELEGRAM_STATE_DIR:-}" ] && exit 0

cat <<EOF
BỘ NÃO CỦA DAVID — đọc trước khi làm (bắt buộc ở mọi phiên, mọi thư mục)
Gốc bộ não: $REPO (đường dẫn tương đối trong AGENTS.md tính từ đây). Đã nạp sẵn: luật chung, AGENTS.md (sáu luật), muc-tieu.md, david.md.
Trước việc đầu tiên David giao (không áp dụng cho câu hỏi nhanh, tra cứu), mở đúng phần cần, đọc theo thứ tự:
1. $REPO/co-so-tri-thuc/tu-duy-goc.md — cách nghĩ gốc của mọi việc (bốn khối)
2. $REPO/ky-nang/chuan-muc-lam-viec.md — thói quen chung mọi việc (mục 0–4)
3. $REPO/quy-trinh.md — cây quy trình: tìm lá của việc; có lá thì tự làm trọn, chưa có thì trình 4 phần chờ "duyệt"
4. $REPO/bao-cao-trang-thai.md — việc đang làm, việc chờ David quyết
5. $REPO/co-so-tri-thuc/bo-nho/MEMORY.md — mục lục bài học, quyết định: mở file liên quan
6. $REPO/co-so-tri-thuc/hinh-mau/README.md — làm việc gì cũng học từ hình mẫu đã thành công
Tìm nhanh: grep -i "<từ khoá>" $REPO/co-so-tri-thuc/chi-muc.md rồi mở đúng file. Thuật ngữ: $REPO/co-so-tri-thuc/bang-thuat-ngu.md
Việc công ty Veltrix: ~/Documents/bo-nao-veltrix/AGENTS.md. Cuối việc: cập nhật bộ não và đẩy lên GitHub theo luật 6.
EOF

# Trạng thái hiện tại: dòng việc của ba mục đầu bao-cao-trang-thai.md (gọn, tối đa khoảng 1.500 chữ)
if [ -f "$REPO/bao-cao-trang-thai.md" ]; then
  echo "--- Trạng thái hiện tại (bao-cao-trang-thai.md) ---"
  awk '/^## (Ưu tiên|Đang làm chưa xong|Chờ David quyết định)/{f=1; print; next} /^## /{f=0} f && /^[-|0-9]/' "$REPO/bao-cao-trang-thai.md" \
    | cut -c1-220 | head -c 1500
  echo
fi
exit 0
