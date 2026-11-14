#!/bin/bash
# Cài bộ não vào máy cho Claude Code: biến repo này thành bản DUY NHẤT trên máy.
# ~/.claude/David.md, CLAUDE.md, các skill, thư mục bộ nhớ và sổ danh mục được thay bằng LỐI TẮT trỏ vào repo,
# nên sửa ở máy là sửa trong repo; sync.sh chỉ còn kéo về / đẩy lên GitHub (2 chiều).
# Bản cũ trên máy được sao lưu trước khi thay. Chạy lại nhiều lần không sao.
# Dùng: bash tu-dong-hoa/install.sh [thư mục dự án sẽ mở Claude Code]   (mặc định: chính repo này)
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
CL="$HOME/.claude"
DU_AN="${1:-$REPO}"
DU_AN="$(cd "$DU_AN" && pwd)"
SAO_LUU="$CL/backups/truoc-cai-nao-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$CL/skills" "$SAO_LUU"

# Thay $2 (đường dẫn trên máy) bằng lối tắt tới $1 (trong repo); bản cũ chuyển vào sao lưu.
lien_ket() {
  local dich="$1" cho="$2"
  [ -L "$cho" ] && [ "$(readlink "$cho")" = "$dich" ] && return 0
  if [ -e "$cho" ] || [ -L "$cho" ]; then mv "$cho" "$SAO_LUU/$(basename "$cho")-$RANDOM"; fi
  mkdir -p "$(dirname "$cho")"
  ln -s "$dich" "$cho"
  echo "  $cho → $dich"
}

echo "Lối tắt vào repo:"
lien_ket "$REPO/co-so-tri-thuc/chi-dan-toan-cuc.md" "$CL/CLAUDE.md"
lien_ket "$REPO/co-so-tri-thuc/David.md" "$CL/David.md"
for s in san-xuat-video san-pham-hoa thu-thap-yeu-cau playwright-cli scroll-craft tai-cau-truc tong-hop-tin-nhan hoc-lien-tuc; do
  lien_ket "$REPO/ky-nang/$s" "$CL/skills/$s"
done
# Lối tắt để Claude nhận lệnh /<tên skill>
for s in cat-doan-noi-bat phan-phoi-da-kenh phan-tich-video-mau dung-podcast dung-video-theo-phong-cach; do
  lien_ket "$REPO/ky-nang/san-xuat-video/$s" "$CL/skills/$s"
done

# Bộ nhớ gắn theo đường dẫn dự án (Claude Code đổi mọi ký tự không phải chữ/số thành dấu -)
MA="$(printf '%s' "$DU_AN" | sed 's#[^A-Za-z0-9]#-#g')"
MEM="$CL/projects/$MA/memory"
# Ghi nhớ riêng máy (thiet-bi-*) đang có thì giữ lại trong repo (không lên GitHub vì .gitignore)
if [ -d "$MEM" ] && [ ! -L "$MEM" ]; then
  for f in "$MEM"/thiet-bi-*.md; do [ -e "$f" ] && cp -n "$f" "$REPO/co-so-tri-thuc/bo-nho/"; done
fi
lien_ket "$REPO/co-so-tri-thuc/bo-nho" "$MEM"

# Sổ danh mục
lien_ket "$REPO/du-an/danh-muc-noi-dung.md" "$HOME/Movies/_danh-muc-noi-dung/danh-muc-noi-dung.md"

# Hook đồng bộ 2 chiều: đầu phiên kéo về, cuối phiên đẩy lên
python3 -I "$REPO/tu-dong-hoa/cai-hook.py" "$REPO"

# Plugin của Claude Code: chỉ Telegram. Mod giao diện đã gỡ hết 13/11/2026 (ghi nhớ quy-tac-mod-tu-chay).
if command -v claude >/dev/null 2>&1; then
  claude plugin install telegram@claude-plugins-official --scope user >/dev/null 2>&1 && echo "Plugin: telegram" || echo "⚠ Chưa cài được telegram"
fi

echo "Xong. Bản cũ (nếu có): $SAO_LUU"
echo "Bộ nhớ gắn với dự án: $DU_AN"
echo "Kiểm tra công cụ dựng video: zsh \"$CL/skills/san-xuat-video/dung-video-theo-phong-cach/scripts/check_env.sh\""
