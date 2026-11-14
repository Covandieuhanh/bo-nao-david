#!/bin/bash
# Đồng bộ 2 chiều bộ não giữa máy này và GitHub.
# Trên máy đã cài (cai-dat-bo-nao.sh), ~/.claude/david.md, CLAUDE.md, skills, bộ nhớ và sổ danh mục là LỐI TẮT trỏ vào repo này,
# nên máy và repo là một bản. Lệnh này chỉ còn việc kéo bản mới từ GitHub về và đẩy thay đổi trên máy lên.
#
# Dùng:
#   bash tu-dong-hoa/dong-bo.sh          kéo về rồi đẩy lên (2 chiều) — mặc định
#   bash tu-dong-hoa/dong-bo.sh --push   như trên (giữ tên cũ "cập nhật não")
#   bash tu-dong-hoa/dong-bo.sh --keo    chỉ kéo bản mới từ GitHub về (đầu phiên)
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"
CHE_DO="${1:---push}"

kiem_loi_tat() {
  local CL="$HOME/.claude" thieu=0
  for p in "$CL/david.md" "$CL/CLAUDE.md" "$CL/skills/san-xuat-video" "$CL/skills/thu-thap-yeu-cau" "$CL/skills/dieu-khien-trinh-duyet"; do
    [ -L "$p" ] || { echo "⚠ $p không phải lối tắt vào repo — chạy: bash $REPO/tu-dong-hoa/cai-dat-bo-nao.sh $REPO"; thieu=1; }
  done
  return 0
}

keo() {
  git fetch -q origin || { echo "⚠ Không kết nối được GitHub, bỏ qua bước kéo."; return 0; }
  if ! git pull -q --rebase --autostash origin main; then
    echo "⛔ Kéo về bị xung đột. Repo đang dừng giữa chừng: xem 'git status', sửa xong chạy 'git rebase --continue' (hoặc 'git rebase --abort' để quay lại)."
    exit 1
  fi
}

case "$CHE_DO" in
  --keo)
    keo; kiem_loi_tat; echo "Đã kéo bản mới nhất từ GitHub." ;;
  --push|--day|*)
    kiem_loi_tat
    python3 -I "$REPO/tu-dong-hoa/quet-bi-mat.py" "$REPO" || { echo "⛔ Quét thấy bí mật, không đẩy."; exit 1; }
    python3 -I "$REPO/tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py" || { echo "⛔ Có link gãy (co-so-tri-thuc/quy-uoc-lien-ket.md), sửa rồi đẩy lại."; exit 1; }
    git add -A
    if ! git diff --cached --quiet; then
      git status --short | tail -30
      git commit -q -m "Cập nhật bộ não $(date '+%F %H:%M')"
    fi
    keo
    if [ -n "$(git log origin/main..HEAD --oneline 2>/dev/null)" ]; then
      git push -q origin main && echo "Đã đẩy lên GitHub." || { echo "⚠ Đẩy lên GitHub thất bại."; exit 1; }
    else
      echo "Máy và GitHub đã giống nhau."
    fi ;;
esac
