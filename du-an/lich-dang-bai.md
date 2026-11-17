---
description: "Hệ thống lịch đăng bài Facebook cá nhân: tuần nào cũng 4 bài kể cả không có video — luôn sẵn 2 tuần bài có ảnh trên trang localhost:8765/bai-dang (chép bài, tải ảnh một chạm), kho 8 bài nền, lịch tự soạn sáng thứ 6, ảnh ChatGPT, nhắc 19:45, David tự bấm; kèm sổ lịch."
---

# Hệ thống lịch đăng bài — Facebook cá nhân

Hồ sơ hình ảnh (định vị, 4 trụ, 5 kiểu bài nền, luật ảnh): [hinh-anh-facebook-ca-nhan.md](hinh-anh-facebook-ca-nhan.md) · khung lịch: `kenh.json` → `lich.facebook_ca_nhan`.
**Trang đăng bài: http://localhost:8765/bai-dang** (cùng máy chủ trang Kết quả video `tu-dong-hoa/xem-ket-qua.py`; tự bật khi mở máy bằng launchd `com.david.xem-ket-qua`, cài bằng `bash tu-dong-hoa/cai-trang-xem.sh`): mỗi bài một thẻ có giờ đăng, chữ đăng + nút **Chép bài**, ảnh hay video + nút **Tải**, nút **Đã đăng** (ghi `.da-dang` trong thư mục ngày).
**Bài và ảnh** (sản phẩm, không lên GitHub): `~/Documents/1-nghe-nghiep/bai-dang/` — mỗi ngày đăng một thư mục `YYYY-MM-DD/` (`bai.md`, `anh.png`), kho ở `kho-bai-nen/`, bản tóm tuần `tuan-YYYY-MM-DD.md`.

## Mục tiêu
Không tuần nào trống: **4 bài/tuần** (T3 video · T5 bài viết công nghệ · T6 video · CN bài viết con người / đời thường, 20:00 giờ Việt Nam). Đo bằng: số tuần đủ bài, số người kể chuyện của họ (bình luận, tin nhắn).

## Cách chạy
| Khi | Ai | Làm gì |
|---|---|---|
| **Thứ 6 07:30** | lịch tự chạy `lich-dang-tuan` (`tu-dong-hoa/lich/`) | bù cho **luôn đủ 2 tuần phía trước** (mọi ô CN, T3, T5, T6 trong 14 ngày tới; giữ bài đã có), làm ảnh, bù kho đủ 8, ghi sổ, báo Telegram một tin ngắn kèm link trang, đặt nhắc 19:45 |
| Bất kỳ lúc nào | David | xem trang đăng bài; muốn sửa thì nhắn "sửa bài <ngày>: …" |
| **19:45 ngày đăng** | bot Sổ nhớ (`nhac-viec.md`) | nhắc David đăng, kèm link trang |
| 20:00 | David | mở trang, Chép bài, Tải ảnh, tự bấm đăng trên Facebook cá nhân (trang cá nhân không hẹn giờ được), bấm Đã đăng |
| Đóng gói tuần | skill `san-pham-hoa` | đếm người bình luận kể chuyện, nhắn riêng; ghi câu chuyện nào kéo được người kể |

**Chọn bài cho từng ô:**
- **Ô video (T3, T6):** video David đã duyệt trong `du-an/danh-muc-noi-dung.md` chưa lên Facebook cá nhân; chữ lấy nguyên văn lời David (luật 3). Không có → bài nền từ kho.
- **Ô bài viết (T5, CN):** soạn mới từ lời David tuần qua (`~/Documents/2-ca-nhan/so-tay/kho-du-lieu/`, sổ nhớ) đúng trụ của ngày; chưa đủ nguyên liệu → bài nền từ kho.
- **Kho bài nền:** luôn **8 bài đã soạn**, đủ 5 kiểu (hồ sơ mục 4); lấy ra bao nhiêu soạn bù bấy nhiêu. Bài nền dùng rồi chuyển sang thư mục ngày đăng.
- **Ảnh:** theo hồ sơ mục 5 (ảnh của David trước, ChatGPT trên Chrome khi không có gì).

**Lọc trùng với bài David tự đăng** (chạy đầu lịch thứ 6, và khi David nhắn "lọc lại"):
- Chỉ đọc trang https://www.facebook.com/davidsuckhoe108 trên Chrome David đã đăng nhập: cuộn, bấm "Xem thêm" để đọc trọn bài, đọc bài 30 ngày gần nhất. Không thích, bình luận, chia sẻ, sửa, đăng; chưa đăng nhập thì báo David, không đăng nhập thay.
- So mỗi bài chưa đăng trong `bai-dang/` (và kho bài nền):
  - **Trùng hẳn** (cùng video, hoặc cùng câu chuyện / cảnh mở bài): bài video → ghi `.da-dang` nội dung "David tự đăng <ngày>"; bài viết → trả về chỗ cũ không được, nên bỏ thư mục ngày đó và lấy bài khác cùng trụ từ kho vào thay (kho soạn bù).
  - **Trùng ý** (cùng nỗi đau, khác cách kể): viết lại theo góc khác, hoặc dời xa bài David đã đăng ít nhất 2 tuần.
  - **Không trùng:** giữ.
- Ghi kết quả vào `bai-dang/loc-trung.md` (lần lọc, bài David đã đăng: ngày · tóm một dòng · trùng với bài nào · đã xử lý gì) và vào dòng `Lọc:` đầu `bai.md` của bài liên quan; trang đăng bài hiện nhãn lọc. Bài David tự đăng ghi vào Sổ lịch (nguồn "David tự đăng") và là nguyên liệu cho bài sau.
- Giới hạn: so bằng chữ trong bài và nội dung chính video, không so từng khung hình.

## Sổ lịch
Trạng thái: nháp · đã gửi duyệt · duyệt · đã đăng · thay (ghi lý do).

| Ngày | Ô | Trụ | Bài | Nguồn | Trạng thái |
|---|---|---|---|---|---|
| CN 08/11 | video | 3 | "Đi bộ hằng ngày" bản đầy đủ | David tự đăng | đã đăng (thấy khi lọc 17/11) |
| T5 19/11 | bài viết | 1 | 10 giờ tối vẫn trả tin nhắn khách → gom về một bảng mỗi sáng | bài nền #1 | sẵn trên trang |
| T6 20/11 | video | 2 | "Bận cả ngày mà không ra kết quả" (bản đầy đủ) · video chưa duyệt kịp thì bài nền #7 | `~/Movies/tap-ban-ca-ngay` | sẵn trên trang · chờ duyệt video |
| CN 22/11 | bài viết | 2 | Tháng đầu lên quản lý: làm thay cả đội | soạn mới | sẵn trên trang |
| T3 24/11 | video | 2 | Clip 76 s "Mục tiêu và sứ mệnh" | David ok 07/11 | sẵn trên trang |
| T5 26/11 | bài viết | 4 | Bận cả tuần không rõ đi tới đâu → báo cáo tuần tự gom | bài nền #9 (lọc 17/11: thay #2) | sẵn trên trang |
| T6 27/11 | video | 2 | Clip "Người thân quen kéo hết nhân sự" (Đi trainer A) | David duyệt 06/11 (lọc 17/11: thay Đi bộ) | sẵn trên trang |
| CN 29/11 | bài viết | 3 | Ngồi lâu mới là chăm → làm theo đợt năng lượng | bài nền #6 | sẵn trên trang |
| T3 01/12 | video | 2 | Clip "Không phải sai, mà là chưa phù hợp" (Đi trainer B) | David duyệt 06/11 | sẵn trên trang |
| T5 03/12 | bài viết | 1 | Phần mềm mua về nằm im → kèm đào tạo tới khi đội dùng được | bài nền #5 | sẵn trên trang |
| T6 04/12 | video | 3 | Vlog The View Vũng Tàu | David chốt 08/11 | sẵn trên trang |
| CN 06/12 | bài viết | 2 | Cả ngày trả lời câu hỏi của đội → trao quyền | bài nền #4 | sẵn trên trang |
| T5 10/12 | bài viết | 4 | Thư mục video quay rồi mà chưa đăng → mình chỉ quay và nói ý | bài nền #2 (lọc 17/11: dời từ 26/11) | sẵn trên trang |

## Kho bài nền (8)
| # | Kiểu | Trụ | Bài |
|---|---|---|---|
| 3 | Cách mình làm việc | 1 | Họp xong không ai rõ làm gì → bốn bước trước mọi việc |
| 7 | Bài học dẫn người | 2 | "Làm sao để đội nghe mình?" → ba tầng làm chủ |
| 8 | Vấn đề → cách giải | 1 | Một trợ lý trên Telegram nhắc việc, ghi nhớ thay mình |
| 10 | Câu hỏi cho người xem | 1 | Những việc nhỏ lặp lại ăn mất một buổi mỗi tuần |
| 11 | Kết quả thật | 4 | "Hôm nay đăng gì?" → bài soạn sẵn hai tuần, tối chỉ chép và đăng |
| 12 | Bài học dẫn người | 2 | "Sao em này làm mãi không được?" → mảnh ghép đặt chưa đúng chỗ |
| 13 | Cách mình làm việc | 3 | Các tuần trôi qua không đọng lại gì → buổi nhìn lại cuối tuần |
| 14 | Kết quả thật | 4 | Nói hay mà ngại lên hình → podcast chỉ giọng thành video |

## Nhật ký
- 17/11/2026: David duyệt hệ thống (kho 8 bài nền, lịch thứ 6 07:30, duyệt cả tuần qua Telegram, nhắc 19:45, David tự bấm, làm Facebook cá nhân trước) và giao dùng ChatGPT trên Chrome tạo ảnh khi không có nội dung David chuẩn bị.
- 17/11/2026: David: "tạo riêng 1 trang trên localhost:8765 đang có với đầy đủ mọi thứ trong 1 bài đăng để tôi lên copy nội dung và tự tải ảnh khi cần… chuẩn bị sẵn 1 số lượng đủ cho hàng tuần luôn" → trang `/bai-dang`, luôn sẵn 2 tuần (David duyệt đề xuất 2 tuần); Telegram chỉ còn tin ngắn kèm link. Cùng ngày David không chọn để Claude tự đăng Facebook.
- 17/11/2026: David: "cần chức năng tự lên trang facebook cá nhân của tôi để đọc và lọc lại các nội dung… nội dung nào trùng thì bỏ qua khỏi bài đăng chuẩn bị hoặc chỉnh lại" → thêm bước lọc trùng chỉ đọc, chạy mỗi thứ 6 và khi David nhắn "lọc lại" (David duyệt đề xuất).
