#!/bin/bash
# Cài bộ não vào máy cho Claude Code: biến repo này thành bản DUY NHẤT trên máy.
# ~/.claude/David.md, CLAUDE.md, các skill, thư mục bộ nhớ và sổ danh mục được thay bằng LỐI TẮT trỏ vào repo,
# nên sửa ở máy là sửa trong repo; sync.sh chỉ còn kéo về / đẩy lên GitHub (2 chiều).
# Bản cũ trên máy được sao lưu trước khi thay. Chạy lại nhiều lần không sao.
# Dùng: bash scripts/install.sh [thư mục dự án sẽ mở Claude Code]   (mặc định: chính repo này)
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
lien_ket "$REPO/nao/CLAUDE-toan-cuc.md" "$CL/CLAUDE.md"
lien_ket "$REPO/nao/David.md" "$CL/David.md"
for s in dung-video hoi-chuyen-gia playwright-cli scroll-craft tai-ban; do
  lien_ket "$REPO/skills/$s" "$CL/skills/$s"
done
# Lối tắt để Claude nhận lệnh /<tên skill>
for s in cat-highlight-video dang-da-kenh hoc-video-mau podcast-style-edit video-style-edit; do
  lien_ket "$REPO/skills/dung-video/$s" "$CL/skills/$s"
done

# Bộ nhớ gắn theo đường dẫn dự án (Claude Code đổi mọi ký tự không phải chữ/số thành dấu -)
MA="$(printf '%s' "$DU_AN" | sed 's#[^A-Za-z0-9]#-#g')"
MEM="$CL/projects/$MA/memory"
# Ghi nhớ riêng máy (may-*) đang có thì giữ lại trong repo (không lên GitHub vì .gitignore)
if [ -d "$MEM" ] && [ ! -L "$MEM" ]; then
  for f in "$MEM"/may-*.md; do [ -e "$f" ] && cp -n "$f" "$REPO/nao/bo-nho/"; done
fi
lien_ket "$REPO/nao/bo-nho" "$MEM"

# Sổ danh mục
lien_ket "$REPO/dang-lam/danh-muc.md" "$HOME/Movies/_so-danh-muc/danh-muc.md"

# Hook đồng bộ 2 chiều: đầu phiên kéo về, cuối phiên đẩy lên
python3 -I "$REPO/scripts/cai-hook.py" "$REPO"

# Mod (plugin của Claude Code), cài cho mọi phiên trên máy, mọi tài khoản Claude:
# Sổ việc của David (đọc thẳng từ repo) + 3 mod cộng đồng đã đọc mã nguồn 11/11/2026 (mods/README.md).
if command -v claude >/dev/null 2>&1; then
  claude plugin marketplace add "$REPO" >/dev/null 2>&1 || true
  claude plugin marketplace add johnnyvizz/claude-kit >/dev/null 2>&1 || true
  claude plugin marketplace add nateherkai/claude-code-mods >/dev/null 2>&1 || true
  for p in so-viec@david-claude savvy-progress@claude-kit collision-guard@nateherk-mods goal-meter@nateherk-mods; do
    claude plugin install "$p" --scope user >/dev/null 2>&1 && echo "Mod: $p" || echo "⚠ Chưa cài được mod $p"
  done
  [ -d "$HOME/.claude/so-viec/nhap" ] || python3 -I "$REPO/mods/so-viec/scripts/nhap-lich-su.py" || true
fi

echo "Xong. Bản cũ (nếu có): $SAO_LUU"
echo "Bộ nhớ gắn với dự án: $DU_AN"
echo "Kiểm tra công cụ dựng video: zsh \"$CL/skills/dung-video/video-style-edit/scripts/check_env.sh\""
