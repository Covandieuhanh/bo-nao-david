---
description: "Phỏng vấn thiết kế (20/11/2026): dạy tư duy dựng video thành file — người xem cần gì → nguyên lý → hình — để AI nào ở máy nào cũng dựng được chỉ từ GitHub."
---

# Phỏng vấn: tư duy dựng video chỉ dựa vào file (20/11/2026)

**Vấn đề David nêu:** học phải thành *tư duy logic về việc xây dựng video*, không áp code máy móc. Và *"khi không có Claude mà chỉ cần dựa vào các
file thì máy nào cũng có thể dùng bất kì ai nào để làm ra được video"* — thực tế: sửa file trên Mac, dựng video trên máy Windows, máy đó chỉ có GitHub.

**Sự thật đã tra:** máy Windows thật (WSL2) đã cài từ GitHub và đạt `kiem-may.sh` ngày 20/11 (`tu-dong-hoa/may-khac/README.md`) — phần công cụ xong.
Thiếu: tầng tư duy viết thành file, và đường để người dùng yêu cầu hiệu ứng / thêm ảnh.

## Vòng 1 — David: "Đồng ý cả 5"

| # | Câu | Đã chốt |
|---|---|---|
| 1 | "Không có Claude" là ai làm | **Bất kỳ AI nào** (Codex, Gemini, Claude máy khác…) đọc file + chạy script; người chỉ đưa video và duyệt. Không làm hướng dẫn dựng tay không AI |
| 2 | Gốc lý thuyết tầng "người xem cần gì" | **12 nguyên lý Multimedia Learning của Richard Mayer** làm khung, tên tiếng Anh chính xác + một bản dịch duy nhất; gắn những gì đã học từ các kênh vào |
| 3 | Ví dụ giải mẫu | **Claude tự chọn 2–3 video David đã duyệt / đã đăng gần nhất trên Drive**, trình danh sách cho David gật |
| 4 | Ảnh trong repo công khai | **Danh mục kiểu dùng ảnh chụp từ khuôn thử** (hình giả, không mặt David); giải mẫu chỉ ghi lời + mốc + lập luận, không khung hình có mặt David |
| 5 | Yêu cầu hiệu ứng / thêm ảnh | **`yeu-cau.md` + thư mục `them-anh/` trong dự án**, ưu tiên hơn tự chọn, vẫn giữ chữ ký nhận diện + luật nguyên văn. Thêm **bài kiểm suy luận** ~10 đoạn lời mẫu, máy mới tự chạy khi cài và mỗi lần đổi luật |

## Vòng 2 — David: "Đồng ý cả 5"

| # | Câu | Đã chốt |
|---|---|---|
| 6 | Tầng gốc đặt đâu | **File mới `thiet-ke-bo-cuc/nguoi-xem-can-gi.md` làm cửa vào; viết lại `tu-chon.md` theo cái khó → nguyên lý → cách thể hiện**; bảng dấu hiệu → kiểu thành ví dụ dưới nguyên lý (một nhà mỗi luật) |
| 7 | Chuỗi lý do trong kế hoạch cảnh | **Mỗi cảnh `Cần: … · Vì: … · Làm: …`**; cảnh thiếu → P1; cả kế hoạch không có dòng nào → P0 |
| 8 | Thứ tự | **Hai đợt.** Đợt 1: tầng gốc Mayer, viết lại tu-chon, chuỗi lý do + máy soát, `yeu-cau.md` + `them-anh/`, danh mục ảnh khuôn thử, cửa vào AI khác. Đợt 2 (sau khi David gật danh sách video): giải mẫu + bài kiểm suy luận |
| 9 | Chấm bài kiểm | **Đáp án chấp nhận** (nguyên lý đúng, cách được làm, cách không được làm); script so, ≥ 8/10 đạt; đoạn lệch ghi ra cho David chấm |
| 10 | Cửa vào AI khác | **Mục "Dựng video ở máy khác" trong `huong-dan-cho-ai.md`**, thứ tự đọc nguoi-xem-can-gi → tu-chon → bo-cuc → skill dựng, nhắc chạy bài kiểm khi máy mới |

## Tóm tắt
Hết điểm mờ. Còn bỏ ngỏ: danh sách 2–3 video cho đợt 2 (Claude trình khi bắt đầu đợt 2). Bước tiếp: trình 4 phần đợt 1, chờ "duyệt".
