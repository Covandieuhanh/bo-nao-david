#!/bin/bash
# Cài bộ não vào máy mới cho Claude Code. Sao lưu file cũ trước khi ghi đè.
# Dùng: bash scripts/install.sh [thư mục dự án sẽ mở Claude Code]   (mặc định: thư mục đang đứng)
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
CL="$HOME/.claude"
DU_AN="${1:-$PWD}"
DU_AN="$(cd "$DU_AN" && pwd)"
SAO_LUU="$CL/backups/truoc-cai-nao-$(date +%Y%m%d-%H%M%S)"

mkdir -p "$CL/skills" "$SAO_LUU"
for f in CLAUDE.md David.md; do [ -e "$CL/$f" ] && cp "$CL/$f" "$SAO_LUU/"; done
for s in dung-video hoi-chuyen-gia playwright-cli; do
  [ -d "$CL/skills/$s" ] && cp -R "$CL/skills/$s" "$SAO_LUU/$s"
done

cp "$REPO/nao/CLAUDE-toan-cuc.md" "$CL/CLAUDE.md"
cp "$REPO/nao/David.md" "$CL/David.md"

for s in dung-video hoi-chuyen-gia playwright-cli; do
  rsync -a --delete "$REPO/skills/$s/" "$CL/skills/$s/"
done

# Lối tắt để Claude nhận lệnh /<tên skill>
for s in cat-highlight-video dang-da-kenh podcast-style-edit video-style-edit; do
  rm -rf "$CL/skills/$s"
  ln -s "$CL/skills/dung-video/$s" "$CL/skills/$s"
done

# Bộ nhớ gắn theo đường dẫn dự án (Claude Code đổi mọi ký tự không phải chữ/số thành dấu -)
MA="$(printf '%s' "$DU_AN" | sed 's#[^A-Za-z0-9]#-#g')"
MEM="$CL/projects/$MA/memory"
mkdir -p "$MEM"
[ -z "$(ls -A "$MEM" 2>/dev/null)" ] || cp -R "$MEM" "$SAO_LUU/memory"
rsync -a "$REPO/nao/bo-nho/" "$MEM/"

# Sổ danh mục: chỉ chép khi máy chưa có, để không đè sổ đang dùng
mkdir -p "$HOME/Movies/_so-danh-muc"
[ -f "$HOME/Movies/_so-danh-muc/danh-muc.md" ] || cp "$REPO/dang-lam/danh-muc.md" "$HOME/Movies/_so-danh-muc/danh-muc.md"

echo "Xong. Bản sao lưu: $SAO_LUU"
echo "Bộ nhớ gắn với dự án: $DU_AN"
echo "Kiểm tra công cụ dựng video: zsh \"$CL/skills/dung-video/video-style-edit/scripts/check_env.sh\""
