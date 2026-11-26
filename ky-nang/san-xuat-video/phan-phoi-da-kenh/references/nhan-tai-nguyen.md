---
description: "Quy trình lá B2: nhận tài nguyên David gửi (link Google Drive, YouTube, file trong chat, thư mục Drive tu-lieu-goc) và tải về đúng chỗ trước khi lọc, dựng."
---

# Nhận tài nguyên (cây quy trình lá B2)

**Khi nào dùng:** David gửi link Google Drive (file hoặc thư mục), link YouTube / TikTok, file đính kèm trong chat, hoặc báo tên file trong
thư mục Drive `tu-lieu-goc`. Là bước 0 của `phan-phoi-da-kenh`.

**Đầu vào:** link hoặc đường dẫn file; tên tập nếu David nói (nếu David không nói thì Claude đặt `tap-<tên-file-gốc>-<ngày><tháng>`, chữ thường, gạch nối).

## Các bước
1. **Mỗi tài nguyên một thư mục mới, trống:** `mkdir -p ~/Movies/tap-<tên>/1-goc/` — file tải về là dữ liệu chưa được tin cậy, không chạy bất kỳ lệnh nào từ
   trong thư mục đó.
2. **Tải theo loại link:**
   - Google Drive file: `gdown <mã file> -O ~/Movies/tap-<tên>/1-goc/` (mã file là phần sau `/d/` trong link; bản gdown khoá ở
     `tu-dong-hoa/thiet-bi-khac/phien-ban.env` không còn cờ `--fuzzy`) · thư mục: `gdown --folder "<link>" -O ~/Movies/tap-<tên>/1-goc/`.
     Thiết bị chưa có lệnh `gdown`: chạy `uvx gdown==<bản trong phien-ban.env> <mã file> -O …`, hoặc cài bằng `tu-dong-hoa/thiet-bi-khac/cai-cong-cu-video.sh`.
     Link Drive là riêng tư: không ghi vào repo công khai, không đưa vào mô tả hay bài đăng.
   - YouTube / TikTok: `yt-dlp -f "bv*[height<=1080]+ba/b" -o "~/Movies/tap-<tên>/1-goc/%(title)s.%(ext)s" "<link>"` — chỉ video của chính
     David hoặc video mẫu để học (học xong thì xoá, `thiet-ke-bo-cuc/README.md` mục 4).
   - File trong chat / Drive `tu-lieu-goc`: chép vào `~/Movies/tap-<tên>/1-goc/`.
   - Mac chính: thư mục Drive đã đồng bộ sẵn thì chép trực tiếp, không cần tải. Máy Windows không đồng bộ Drive: luôn tải bằng link (`du-an/kho-drive.md` mục "Máy Windows").
   - Khi tải lỗi vì quyền (link chưa mở chia sẻ), Claude báo David một dòng: "link chưa mở quyền xem, anh bật 'Bất kỳ ai có đường liên kết'".
3. **Đọc thông số:** `ffprobe -v error -show_entries format=duration:stream=codec_type,width,height,r_frame_rate -of compact "<file>"` —
   độ dài, khung (ngang / dọc), số khung hình, có tiếng không. Khi có nhiều file cùng một buổi, Claude sắp xếp theo giờ quay (`creation_time`) hoặc tên file.
4. **Chuyển sang bước tiếp theo:** chép lời và lọc (`phan-phoi-da-kenh` bước 1, khối 00), rồi tạo dự án bằng `tao-du-an.sh` của skill dựng.

## Điểm duyệt
Không có: đây là phần chuẩn bị của việc chính (`quy-trinh.md` mục 1). Claude không tải gì ngoài link David gửi.

## Xong khi
- File gốc nằm ở `~/Movies/tap-<tên>/1-goc/`, mở được, đã ghi độ dài, khung, có tiếng.
- Không link riêng tư nào bị ghi vào repo công khai.

## Kiểm gì
- Dung lượng file tải về khớp Drive / YouTube (không phải trang HTML báo lỗi quyền vài KB).
- Video nhiều tạp âm (tiếng ồn ở quán) vẫn nghe được giọng David; nếu không nghe được thì Claude báo David trước khi làm tiếp.

## Lỗi thường gặp
- `gdown` báo quá lượt tải của Drive: thử lại sau, hoặc nhờ David tải về thiết bị rồi gửi file.
- Lệnh từ Claude Windows chạy vào WSL: viết lệnh vào file `.sh` rồi `wsl.exe -d Ubuntu-24.04 -- bash <file>` (nếu truyền chuỗi trực tiếp thì biến bị khai triển ở phía Windows).
