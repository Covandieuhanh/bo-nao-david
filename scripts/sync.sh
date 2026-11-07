#!/bin/bash
# Chép bộ não mới nhất từ máy (~/.claude) vào repo (chỉ não, skill, việc dở, mẫu; không thành quả), quét bí mật, rồi (nếu có --push) commit và đẩy lên GitHub.
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

# Bộ nhớ: không dùng --delete để một dự án mới ít ghi nhớ không xoá mất bộ nhớ cũ.
# Ưu tiên bộ nhớ của dự án David.Claude (nơi mở phiên), rồi mới tới thư mục memory mới sửa gần nhất mà có nội dung.
MA="$(printf '%s' "$REPO" | sed 's#[^A-Za-z0-9]#-#g')"
MEM="${NAO_MEMORY_DIR:-}"
[ -z "$MEM" ] && [ -f "$CL/projects/$MA/memory/MEMORY.md" ] && MEM="$CL/projects/$MA/memory"
[ -z "$MEM" ] && for d in $(ls -dt "$CL"/projects/*/memory 2>/dev/null); do [ -f "$d/MEMORY.md" ] && { MEM="$d"; break; }; done
# Ghi nhớ tên bắt đầu "may-" chỉ đúng cho một máy: không đưa lên, bỏ cả dòng của nó trong MEMORY.md.
if [ -n "${MEM:-}" ]; then
  rsync -a "${LOAI[@]}" --exclude 'may-*' --exclude MEMORY.md "$MEM/" "$REPO/nao/bo-nho/"
  grep -v '](may-' "$MEM/MEMORY.md" > "$REPO/nao/bo-nho/MEMORY.md" || true
  rm -f "$REPO"/nao/bo-nho/may-*
fi

[ -f "$HOME/Movies/_so-danh-muc/danh-muc.md" ] && cp "$HOME/Movies/_so-danh-muc/danh-muc.md" "$REPO/dang-lam/danh-muc.md"

# Chỉ đưa não lên GitHub. Dự án video, bài đăng, tài liệu đã làm xong ở lại máy (~/Movies) và Drive.

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
