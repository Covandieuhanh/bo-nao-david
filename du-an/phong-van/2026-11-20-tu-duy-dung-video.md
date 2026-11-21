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
| 5 | Yêu cầu hiệu ứng / thêm ảnh | **`yeu-cau.md` + thư mục `them-anh/` trong dự án**, ưu tiên hơn tự chọn, vẫn giữ chữ ký nhận diện + luật nguyên văn. Thêm **bài kiểm suy luận** khoảng 10 đoạn lời mẫu, máy mới tự chạy khi cài và mỗi lần đổi luật |

## Vòng 2 — David: "Đồng ý cả 5"

| # | Câu | Đã chốt |
|---|---|---|
| 6 | Tầng gốc đặt đâu | **File mới `thiet-ke-bo-cuc/nguoi-xem-can-gi.md` làm cửa vào; viết lại `tu-chon.md` theo cái khó → nguyên lý → cách thể hiện**; bảng dấu hiệu → kiểu thành ví dụ dưới nguyên lý (một nhà mỗi luật) |
| 7 | Chuỗi lý do trong kế hoạch cảnh | **Mỗi cảnh `Cần: … · Vì: … · Làm: …`**; cảnh thiếu → P1; cả kế hoạch không có dòng nào → P0 |
| 8 | Thứ tự | **Hai đợt.** Đợt 1: tầng gốc Mayer, viết lại tu-chon, chuỗi lý do + máy soát, `yeu-cau.md` + `them-anh/`, danh mục ảnh khuôn thử, cửa vào AI khác. Đợt 2 (sau khi David gật danh sách video): giải mẫu + bài kiểm suy luận |
| 9 | Chấm bài kiểm | **Đáp án chấp nhận** (nguyên lý đúng, cách được làm, cách không được làm); script so, ít nhất 8/10 đạt; đoạn lệch ghi ra cho David chấm |
| 10 | Cửa vào AI khác | **Mục "Dựng video ở máy khác" trong `huong-dan-cho-ai.md`**, thứ tự đọc nguoi-xem-can-gi → tu-chon → bo-cuc → skill dựng, nhắc chạy bài kiểm khi máy mới |

## Tóm tắt
Hết điểm mờ. David duyệt đợt 1 (thêm bước "loại nội dung cả video"; loại lấy từ những gì Claude đã biết qua Drive và các phiên, hiện dần qua video quay thêm).

**Đợt 1 — xong 20/11/2026:** `thiet-ke-bo-cuc/nguoi-xem-can-gi.md` + `nguyen-ly.json` · `tu-chon.md` viết lại theo nguyên lý (bước 0b yêu cầu, 1b loại nội dung, 4c kho theo nguyên lý) · `soat-canh.mjs` (Loại, Cần · Vì · Làm, Yêu cầu, ảnh thiếu) · `yeu-cau.md` + `them-anh/` trong dự án mới · ảnh mẫu `bo-cuc.md` + `anh-mau/cong-cu/chup-anh-mau.sh` · mục "Dựng video ở máy khác" trong `huong-dan-cho-ai.md`.

**Đợt 2 — đổi nguồn (David, 20/11):** *"không cần dựa trên những nội dung tôi nói, mà hãy dựa trên những hình mẫu đã rất thành công của
cùng thể loại mà tôi đang hướng tới để làm mẫu"* thì thay câu 3: giải mẫu + bài kiểm lấy từ **hình mẫu thành công cùng thể loại** (ba hướng:
trainer phát triển bản thân, giải pháp công nghệ AI, tài chính), chọn theo số liệu kiểm được (`hoc-lien-tuc` Việc 2). Claude đo, trình danh
sách hình mẫu kèm số liệu → David gật → giải mẫu + bài kiểm (khoảng 10 đoạn, đáp án chấp nhận, ít nhất 8/10). Trích lời nguồn chỉ cụm rất ngắn, phần còn lại diễn ý.

**Đợt 2 — xong 20/11/2026:** David gật 8 hình mẫu (đo 23 kênh: theo dõi + trung vị 10 video dài / ngắn) → `thiet-ke-bo-cuc/giai-mau.md`
(19 ca, rút ra theo loại) · `thiet-ke-bo-cuc/bai-kiem/` (`de.json` 10 đoạn, `cham.py`, README) · nối vào `nguoi-xem-can-gi.md`, `huong-dan-cho-ai.md`.
Chưa kiểm: một AI khác (chưa thấy đáp án) làm bài thật — cần chạy ở máy Windows hoặc một phiên mới.
