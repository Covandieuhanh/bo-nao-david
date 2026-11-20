---
name: co-so-tri-thuc-nhieu-may
description: "Nhiều máy của David (Mac + Windows) cùng dùng bộ não GitHub, dựng video ra như Mac chính; máy nào cũng đẩy được, máy khác chỉ làm video; khoá phiên bản + kiem-may.sh"
metadata:
  type: project
---

David chốt 20/11/2026: dùng thêm nhiều máy, cả Windows lẫn Mac, để dựng video theo đúng skill. Máy khác cài qua GitHub phải làm được đủ quy trình và ra kết quả như Mac chính. Mac chính là nơi chủ yếu cập nhật bộ não và skill.

- **Máy nào cũng ngang nhau về đồng bộ.** David nói: "không phải máy phụ, cũng là máy của tôi". Máy nào đăng nhập GitHub của David thì kéo về và đẩy lên được. Không chia máy chính / máy phụ.
- **GitHub công khai chỉ giữ phần dùng chung** (20/11/2026): phần riêng Mac chính (bot, lịch, trang xem, lưu trữ) ở repo riêng tư `bo-nao-david-mac`, xem [[co-so-tri-thuc-github-ban-goc]].
- **Máy khác chỉ làm video.** Bot Telegram, lịch tự chạy, trang xem kết quả, đăng bài chỉ chạy ở Mac chính. Lệnh `cai-dat-bo-nao.sh --chi-video`; máy không phải Mac tự bật chế độ này.
- **Windows chạy qua WSL2** (Ubuntu trong Windows). David để Claude chọn cách tốt nhất; WSL2 chạy được nguyên script của Mac nên chỉ giữ một bộ skill.

**Why:** David muốn sản xuất video ở nhiều máy mà kết quả giống hệt, không phải giữ nhiều bộ skill.
**How to apply:**
- Nâng công cụ dựng thì làm ở Mac chính: sửa `tu-dong-hoa/may-khac/phien-ban.env` và lockfile khuôn, tạo lại bản chuẩn (`kiem-may.sh --tao-chuan`), đẩy GitHub.
- Script skill mới không được ghi cứng thứ chỉ Mac có (`/opt/homebrew/bin/...`, `/System/Library/Fonts`, Vision, `stat -f`). Dùng `do-mat.sh`, `font_he_thong()`, `drive-chung.sh`.
- Đuôi file phải đúng chữ hoa/thường, vì WSL2 phân biệt còn Mac thì không.

Chi tiết: [tu-dong-hoa/may-khac/README.md](../../tu-dong-hoa/may-khac/README.md), `huong-dan-cai-dat.md` mục 2–3. Liên quan [[co-so-tri-thuc-github-ban-goc]].
