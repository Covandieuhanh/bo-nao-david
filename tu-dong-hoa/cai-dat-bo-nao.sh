#!/bin/bash
# Cài bộ não vào máy cho Claude Code: biến repo này thành bản DUY NHẤT trên máy.
# ~/.claude/david.md, CLAUDE.md, các skill, thư mục bộ nhớ và sổ danh mục được thay bằng LỐI TẮT trỏ vào repo,
# nên sửa ở máy là sửa trong repo; dong-bo.sh chỉ còn kéo về / đẩy lên GitHub (2 chiều).
# Bản cũ trên máy được sao lưu trước khi thay. Chạy lại nhiều lần không sao.
# Dùng: bash tu-dong-hoa/cai-dat-bo-nao.sh [thư mục dự án sẽ mở Claude Code] [--chi-video]   (mặc định: chính repo này)
#   --chi-video: máy chỉ dựng video (Windows qua WSL2, Mac khác; David 20/11/2026) — đồng bộ 2 chiều như Mac chính, nhưng không cài
#   bot Telegram, lịch tự chạy, trang xem kết quả. Máy không phải Mac tự bật chế độ này. Công cụ dựng: tu-dong-hoa/may-khac/cai-cong-cu-video.sh
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
CL="$HOME/.claude"
CHI_VIDEO=0; DU_AN=""
for a in "$@"; do case "$a" in --chi-video) CHI_VIDEO=1;; *) DU_AN="$a";; esac; done
[ "$(uname)" = Darwin ] || CHI_VIDEO=1
DU_AN="${DU_AN:-$REPO}"
DU_AN="$(cd "$DU_AN" && pwd)"
SAO_LUU="$CL/backups/truoc-cai-nao-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$CL/skills" "$SAO_LUU"

# Thay $2 (đường dẫn trên máy) bằng lối tắt tới $1 (trong repo); bản cũ chuyển vào sao lưu.
lien_ket() {
  local dich="$1" cho="$2"
  [ -e "$dich" ] || return 0          # phần riêng Mac chính (repo riêng tư) không có ở máy này → bỏ qua
  [ -L "$cho" ] && [ "$(readlink "$cho")" = "$dich" ] && return 0
  if [ -e "$cho" ] || [ -L "$cho" ]; then mv "$cho" "$SAO_LUU/$(basename "$cho")-$RANDOM"; fi
  mkdir -p "$(dirname "$cho")"
  ln -s "$dich" "$cho"
  echo "  $cho → $dich"
}

# Mac chính: kéo repo riêng tư bo-nao-david-mac (bot Telegram, lịch tự chạy, trang xem kết quả, lưu trữ) vào CÙNG thư mục.
# Danh sách phần riêng: tu-dong-hoa/phan-rieng-mac.txt. Máy chỉ dựng video bỏ qua bước này.
if [ $CHI_VIDEO = 0 ] && [ ! -d "$REPO/.git-mac" ]; then
  if git clone -q --bare https://github.com/Covandieuhanh/bo-nao-david-mac.git "$REPO/.git-mac" 2>/dev/null; then
    GR() { git --git-dir="$REPO/.git-mac" --work-tree="$REPO" "$@"; }
    GR config core.bare false; GR config status.showUntrackedFiles no
    GR config user.name "$(git -C "$REPO" config user.name)"; GR config user.email "$(git -C "$REPO" config user.email)"
    GR checkout main 2>/dev/null && echo "Phần riêng Mac chính: đã kéo bo-nao-david-mac" \
      || echo "⚠ Phần riêng Mac: có file trùng tên chưa ghi đè — xem: git --git-dir=$REPO/.git-mac --work-tree=$REPO status"
  else
    echo "⚠ Không kéo được repo riêng tư bo-nao-david-mac (chưa gh auth login đúng tài khoản?). Bot, lịch sẽ thiếu."
  fi
fi

echo "Lối tắt vào repo:"
lien_ket "$REPO/co-so-tri-thuc/chi-dan-toan-cuc.md" "$CL/CLAUDE.md"
lien_ket "$REPO/co-so-tri-thuc/david.md" "$CL/david.md"
for s in san-xuat-video san-pham-hoa thu-thap-yeu-cau dieu-khien-trinh-duyet thiet-ke-trang-cuon tai-cau-truc tong-hop-tin-nhan hoc-lien-tuc; do
  lien_ket "$REPO/ky-nang/$s" "$CL/skills/$s"
done
# Lối tắt để Claude nhận lệnh /<tên skill>
for s in cat-doan-noi-bat phan-phoi-da-kenh phan-tich-video-mau dung-podcast dung-video-theo-phong-cach; do
  lien_ket "$REPO/ky-nang/san-xuat-video/$s" "$CL/skills/$s"
done

# Agent dùng chung (mô hình nhỏ cho việc đọc, tìm, tóm tắt)
for a in "$REPO"/tac-tu/*.md; do lien_ket "$a" "$CL/agents/$(basename "$a")"; done

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
if [ $CHI_VIDEO = 1 ]; then
  python3 -I "$REPO/tu-dong-hoa/cai-hook.py" "$REPO" --chi-video
  echo "chi-video" > "$CL/vai-may"     # vai trò máy: các script biết đây là máy chỉ dựng video
else
  python3 -I "$REPO/tu-dong-hoa/cai-hook.py" "$REPO"
  echo "chinh" > "$CL/vai-may"
fi

# Plugin của Claude Code: chỉ Telegram. Mod giao diện đã gỡ hết 13/11/2026 (ghi nhớ quy-tac-khong-dung-mod-giao-dien).
if [ $CHI_VIDEO = 0 ] && command -v claude >/dev/null 2>&1; then
  claude plugin install telegram@claude-plugins-official --scope user >/dev/null 2>&1 && echo "Plugin: telegram" || echo "⚠ Chưa cài được telegram"
fi

echo "Xong. Bản cũ (nếu có): $SAO_LUU"
echo "Bộ nhớ gắn với dự án: $DU_AN"
echo "Kiểm tra công cụ dựng video: zsh \"$CL/skills/san-xuat-video/dung-video-theo-phong-cach/scripts/kiem-moi-truong.sh\""
[ $CHI_VIDEO = 1 ] && echo "Máy chỉ dựng video. Bước tiếp: bash \"$REPO/tu-dong-hoa/may-khac/cai-cong-cu-video.sh\" rồi zsh \"$REPO/tu-dong-hoa/may-khac/kiem-may.sh\" (cần Google Drive)"
exit 0
