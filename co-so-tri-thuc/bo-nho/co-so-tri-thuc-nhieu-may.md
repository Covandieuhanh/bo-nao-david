---
name: co-so-tri-thuc-nhieu-may
description: "Nhiều thiết bị của David (Mac và Windows) cùng dùng bộ não trên GitHub, dựng video cho kết quả như Mac chính; thiết bị nào cũng đẩy được lên GitHub, thiết bị khác chỉ làm video; khoá phiên bản và kiem-tra-thiet-bi.sh"
metadata:
  type: project
---

David chốt 20/11/2026: dùng thêm nhiều thiết bị, cả Windows lẫn Mac, để dựng video theo đúng skill. Thiết bị khác cài qua GitHub phải làm được đủ quy trình và cho kết quả như Mac chính. Mac chính là nơi chủ yếu cập nhật bộ não và skill.

- **Thiết bị nào cũng ngang nhau về đồng bộ.** David nói: "không phải máy phụ, cũng là máy của tôi". Thiết bị nào đăng nhập GitHub của David thì kéo về và đẩy lên được. Hệ thống không chia thiết bị chính / thiết bị phụ.
- **GitHub công khai chỉ giữ phần dùng chung** (20/11/2026): phần riêng của Mac chính (bot, lịch chạy, trang xem kết quả, lưu trữ) nằm ở repo riêng tư `bo-nao-david-mac`, xem [[co-so-tri-thuc-github-ban-goc]].
- **Thiết bị khác chỉ làm video.** Bot Telegram, lịch tự chạy, trang xem kết quả, đăng bài chỉ chạy ở Mac chính. Lệnh `cai-dat-bo-nao.sh --chi-video`; thiết bị không phải Mac tự bật chế độ này.
- **Windows chạy qua WSL2** (Ubuntu trong Windows). David để Claude chọn cách tốt nhất; WSL2 chạy được nguyên script của Mac nên hệ thống chỉ giữ một bộ skill.

**Why:** David muốn sản xuất video ở nhiều thiết bị mà kết quả giống hệt nhau, không phải giữ nhiều bộ skill.
**How to apply:**
- Việc cập nhật phiên bản công cụ dựng thì làm ở Mac chính: sửa `tu-dong-hoa/thiet-bi-khac/phien-ban.env` và lockfile mẫu, tạo lại bản chuẩn (`kiem-tra-thiet-bi.sh --tao-chuan`), đẩy lên GitHub.
- Script skill mới không được ghi cố định thành phần chỉ Mac có (`/opt/homebrew/bin/...`, `/System/Library/Fonts`, Vision, `stat -f`). Dùng `do-mat.sh`, `font_he_thong()`, `drive-chung.sh`.
- Đuôi file phải đúng chữ hoa / chữ thường, vì WSL2 phân biệt còn Mac thì không.

Chi tiết: [tu-dong-hoa/thiet-bi-khac/README.md](../../tu-dong-hoa/thiet-bi-khac/README.md), `huong-dan-cai-dat.md` mục 2–3. Liên quan [[co-so-tri-thuc-github-ban-goc]].

Gốc: khối 2 (Hành động) của tu-duy-goc.md — mọi máy chạy cùng một bộ skill và cùng quy trình nên ra cùng một kết quả như máy chính.
