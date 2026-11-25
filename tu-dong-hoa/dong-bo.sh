#!/bin/bash
# Đồng bộ 2 chiều bộ não giữa máy này và GitHub.
# Trên máy đã cài (cai-dat-bo-nao.sh), ~/.claude/david.md, CLAUDE.md, skills, bộ nhớ và sổ danh mục là LỐI TẮT trỏ vào repo này,
# nên máy và repo là một bản. Lệnh này chỉ còn việc kéo bản mới từ GitHub về và đẩy thay đổi trên máy lên.
#
# HAI REPO, MỘT THƯ MỤC (David 20/11/2026: "trên github chỉ còn những cái có thể dùng chung"):
#   - bo-nao-david (công khai, .git): phần dùng chung — mọi máy kéo / đẩy.
#   - bo-nao-david-mac (riêng tư, .git-mac, chỉ Mac chính): đúng các đường dẫn trong tu-dong-hoa/phan-rieng-mac.txt
#     (bot Telegram, lịch tự chạy, trang xem kết quả, lưu trữ…). File vẫn nằm đúng chỗ cũ, nên bot và lịch không phải cài lại.
#   Máy không có .git-mac (máy chỉ dựng video) chỉ đồng bộ repo công khai.
#
# Dùng:
#   bash tu-dong-hoa/dong-bo.sh          kéo về rồi đẩy lên (2 chiều) — mặc định
#   bash tu-dong-hoa/dong-bo.sh --push   như trên (giữ tên cũ "cập nhật não")
#   bash tu-dong-hoa/dong-bo.sh --keo    chỉ kéo bản mới từ GitHub về (đầu phiên)
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"
CHE_DO="${1:---push}"
DS_RIENG="$REPO/tu-dong-hoa/phan-rieng-mac.txt"
RIENG=(); while IFS= read -r l; do RIENG+=("$l"); done < <(grep -v '^#' "$DS_RIENG" 2>/dev/null | sed '/^[[:space:]]*$/d; s|/$||')   # bash 3 của Mac không có mapfile
CO_RIENG=0; [ -d "$REPO/.git-mac" ] && CO_RIENG=1
gr() { git --git-dir="$REPO/.git-mac" --work-tree="$REPO" "$@"; }   # lệnh git cho repo riêng
gc() { git "$@"; }                                                   # lệnh git cho repo công khai

# Repo công khai luôn bỏ qua phần riêng (ghi vào .git/info/exclude — chỉ trên máy, không lên GitHub)
loai_tru_rieng() {
  local ex="$REPO/.git/info/exclude" tam
  mkdir -p "$(dirname "$ex")"; tam=$(mktemp)
  sed '/# >>> phan-rieng-mac/,/# <<< phan-rieng-mac/d' "$ex" 2>/dev/null > "$tam"
  { echo "# >>> phan-rieng-mac (tự sinh từ tu-dong-hoa/phan-rieng-mac.txt — không sửa thủ công)"
    for p in "${RIENG[@]}"; do echo "/$p"; done
    echo "# <<< phan-rieng-mac"; } >> "$tam"
  mv "$tam" "$ex"
}

kiem_loi_tat() {
  local CL="$HOME/.claude" thieu=0
  for p in "$CL/david.md" "$CL/CLAUDE.md" "$CL/skills/san-xuat-video" "$CL/skills/thu-thap-yeu-cau" "$CL/skills/dieu-khien-trinh-duyet"; do
    [ -L "$p" ] || { echo "⚠ $p không phải lối tắt vào repo — chạy: bash $REPO/tu-dong-hoa/cai-dat-bo-nao.sh $REPO"; thieu=1; }
  done
  return 0
}

# Nhiều máy cùng đẩy (Mac + các máy dựng video, 20/11/2026): kéo về trước, git tự gộp khi hai máy sửa khác chỗ.
# Hai máy sửa trùng một dòng → huỷ lần gộp (repo về nguyên trạng, không mất bản nào), ghi sổ XUNG_DOT; đầu phiên sau Claude thấy và báo David.
XUNG_DOT="$HOME/.claude/logs/xung-dot-nao.txt"
keo() {   # keo <gc|gr> <tên repo>
  local G=$1 TEN=$2 tep
  $G fetch -q origin || { echo "⚠ Không kết nối được GitHub ($TEN), bỏ qua bước kéo."; return 0; }
  if ! $G pull -q --rebase --autostash origin main; then
    tep=$($G diff --name-only --diff-filter=U 2>/dev/null | tr '\n' ' ')
    $G rebase --abort >/dev/null 2>&1
    mkdir -p "$(dirname "$XUNG_DOT")"
    echo "$(date '+%F %H:%M') máy $(hostname -s 2>/dev/null || hostname) và GitHub ($TEN) cùng sửa trùng chỗ: ${tep:-(không rõ file)}. Bản trên máy vẫn giữ nguyên, chưa đẩy." >> "$XUNG_DOT"
    echo "⛔ Xung đột khi kéo về $TEN (hai máy sửa trùng chỗ): ${tep:-xem git status}. Đã huỷ gộp, repo giữ nguyên bản trên máy. Nhờ Claude gộp thủ công rồi chạy lại dong-bo.sh."
    exit 1
  fi
}

day() {   # day <gc|gr> <tên repo> <thông điệp>
  local G=$1 TEN=$2
  if ! $G diff --cached --quiet; then
    $G status --short | grep -v '^??' | tail -30
    $G commit -q -m "$3 $(date '+%F %H:%M')"
  fi
  keo "$G" "$TEN"
  if [ -n "$($G log origin/main..HEAD --oneline 2>/dev/null)" ]; then
    $G push -q origin main && echo "Đã đẩy lên GitHub ($TEN)." || { echo "⚠ Đẩy lên GitHub thất bại ($TEN)."; exit 1; }
  else
    echo "Máy và GitHub đã giống nhau ($TEN)."
  fi
}

loai_tru_rieng
case "$CHE_DO" in
  --keo)
    [ -s "$XUNG_DOT" ] && { echo "⛔ Lần đồng bộ trước bị xung đột, bộ não máy này CHƯA lên GitHub:"; cat "$XUNG_DOT"; }
    keo gc bo-nao-david
    [ $CO_RIENG = 1 ] && keo gr bo-nao-david-mac
    rm -f "$XUNG_DOT"; kiem_loi_tat; echo "Đã kéo bản mới nhất từ GitHub." ;;
  --push|--day|*)
    kiem_loi_tat
    python3 -I "$REPO/tu-dong-hoa/quet-bi-mat.py" "$REPO" || { echo "⛔ Quét thấy bí mật, không đẩy."; exit 1; }
    python3 -I "$REPO/tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py" || { echo "⛔ Có link gãy (co-so-tri-thuc/quy-uoc-lien-ket.md), sửa rồi đẩy lại."; exit 1; }
    python3 -I "$REPO/tu-dong-hoa/kiem-quy-trinh.py" || { echo "⛔ Cây quy trình chưa đạt (quy-trinh.md mục 2): việc gì cũng phải có lá, điểm duyệt, Xong khi, sửa rồi đẩy lại."; exit 1; }
    python3 -I "$REPO/tu-dong-hoa/cong-kiem-soat-goc.py" || { echo "⛔ Cổng kiểm soát gốc (truc-tri-thuc.md mục 7): file tầng 0 đổi phải có dòng trong so-dan-chung-goc.md."; exit 1; }
    python3 -I "$REPO/tu-dong-hoa/kiem-ngon-tu.py" || true
    # Vòng tuần (hoc-lien-tuc Việc 1) quá 7 ngày thì nhắc, không chặn
    VT=$(ls "$REPO/du-an/hoc-lien-tuc/" 2>/dev/null | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}' | sort | tail -1 | cut -c1-10)
    if [ -n "$VT" ] && [ $(( ( $(date +%s) - $(date -d "$VT" +%s 2>/dev/null || date -j -f %Y-%m-%d "$VT" +%s) ) / 86400 )) -gt 7 ]; then echo "⚠ Vòng tuần gần nhất $VT, đã quá 7 ngày: chạy bash tu-dong-hoa/hoc-lien-tuc/vong-tuan.sh"; fi
    # Sổ tay riêng (chỉ trên máy, không lên GitHub): kiểm + sinh chỉ mục, không chặn đẩy.
    [ -d "$HOME/Documents/2-ca-nhan/so-tay" ] && { python3 -I "$REPO/tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py" --goc "$HOME/Documents/2-ca-nhan/so-tay" || true; }
    gc add -A
    # Chốt chặn: phần riêng không bao giờ lên repo công khai (kể cả khi .git/info/exclude bị mất)
    lot=$(gc diff --cached --name-only --diff-filter=ACMRT | grep -E "^($(printf '%s|' "${RIENG[@]}" | sed 's/|$//; s/\./\\./g'))(/|$)" || true)
    if [ -n "$lot" ]; then gc reset -q -- $lot; echo "⚠ Đã chặn phần riêng Mac khỏi repo công khai: $(echo $lot | head -c 200)"; fi
    day gc bo-nao-david "Cập nhật bộ não"
    if [ $CO_RIENG = 1 ]; then
      co=(); for p in "${RIENG[@]}"; do { [ -e "$p" ] || [ -n "$(gr ls-files -- "$p" | head -1)" ]; } && co+=("$p"); done
      [ ${#co[@]} -gt 0 ] && gr add -A -- "${co[@]}"
      day gr bo-nao-david-mac "Cập nhật phần riêng Mac"
    fi
    rm -f "$XUNG_DOT" ;;
esac
