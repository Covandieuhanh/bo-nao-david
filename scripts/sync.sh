#!/bin/bash
# Chép bộ não mới nhất từ máy (~/.claude) vào repo, quét bí mật, rồi (nếu có --push) commit và đẩy lên GitHub.
# Dùng: bash scripts/sync.sh [--push]
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
CL="$HOME/.claude"
LOAI=(--exclude .DS_Store --exclude __pycache__ --exclude '*.pyc' --exclude node_modules --exclude .venv)

mkdir -p "$REPO/nao/bo-nho" "$REPO/skills" "$REPO/dang-lam"
cp "$CL/CLAUDE.md" "$REPO/nao/CLAUDE-toan-cuc.md"
cp "$CL/David.md" "$REPO/nao/David.md"

for s in dung-video hoi-chuyen-gia playwright-cli; do
  rsync -a --delete "${LOAI[@]}" "$CL/skills/$s/" "$REPO/skills/$s/"
done

# Bộ nhớ: lấy thư mục memory mới sửa gần nhất. Không dùng --delete để một dự án mới ít ghi nhớ không xoá mất bộ nhớ cũ.
MEM="${NAO_MEMORY_DIR:-$(ls -dt "$CL"/projects/*/memory 2>/dev/null | head -1)}"
[ -n "$MEM" ] && rsync -a "${LOAI[@]}" "$MEM/" "$REPO/nao/bo-nho/"

[ -f "$HOME/Movies/_so-danh-muc/danh-muc.md" ] && cp "$HOME/Movies/_so-danh-muc/danh-muc.md" "$REPO/dang-lam/danh-muc.md"

# Tài liệu và kịch bản của video đang làm. Video và file nặng không đưa lên, thành phẩm ở Drive.
[ -f "$REPO/dang-lam/du-an-video.txt" ] && while read -r ten dich; do
  [ -z "${ten:-}" ] && continue
  P="$HOME/Movies/$ten"; [ -d "$P" ] || continue
  D="$REPO/dang-lam/$dich"; mkdir -p "$D"
  rsync -a --include '*.md' --include 'phuong-an.json' --include 'phat-hanh/***' --include 'motion/' --include 'motion/src/' \
    --include 'motion/src/captions.js' --include 'motion/src/scenes.js' --include 'motion/src/highlight.js' --include 'motion/src/endcard.js' --include 'motion/src/project.js' \
    --exclude '*' "${LOAI[@]}" "$P/" "$D/"
done < "$REPO/dang-lam/du-an-video.txt"

python3 -I "$REPO/scripts/quet-bi-mat.py" "$REPO"

cd "$REPO"
git status --short | tail -30
if [ "${1:-}" = "--push" ]; then
  git add -A
  git diff --cached --quiet && { echo "Không có gì mới."; exit 0; }
  git commit -q -m "Cập nhật bộ não $(date +%F)"
  git push
  echo "Đã đẩy lên GitHub."
fi
