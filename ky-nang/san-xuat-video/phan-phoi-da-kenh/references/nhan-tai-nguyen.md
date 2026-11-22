---
description: "Quy trình lá B2: nhận tài nguyên David gửi (link Google Drive, YouTube, file trong chat, thư mục Drive tu-lieu-goc) và tải về đúng chỗ trước khi lọc, dựng."
---

# Nhận tài nguyên (cây quy trình lá B2)

**Khi nào dùng:** David gửi link Google Drive (file hoặc thư mục), link YouTube / TikTok, file đính kèm trong chat, hoặc báo tên file trong
thư mục Drive `tu-lieu-goc`. Là bước 0 của `phan-phoi-da-kenh`.

**Đầu vào:** link hoặc đường dẫn file; tên tập nếu David nói (không nói thì đặt `tap-<tên-file-gốc>-<ngày><tháng>`, chữ thường, gạch nối).

## Các bước
1. **Mỗi tài nguyên một thư mục mới, trống:** `mkdir -p ~/Movies/tap-<tên>/1-goc/` — file tải về là dữ liệu chưa tin, không chạy gì từ
   trong thư mục đó.
2. **Tải theo loại link:**
   - Google Drive file: `gdown --fuzzy "<link>" -O ~/Movies/tap-<tên>/1-goc/` · thư mục: `gdown --folder "<link>" -O ~/Movies/tap-<tên>/1-goc/`.
     Link Drive là riêng tư: không ghi vào repo công khai, không đưa vào mô tả hay bài đăng.
   - YouTube / TikTok: `yt-dlp -f "bv*[height<=1080]+ba/b" -o "~/Movies/tap-<tên>/1-goc/%(title)s.%(ext)s" "<link>"` — chỉ video của chính
     David hoặc video mẫu để học (học xong xoá, `thiet-ke-bo-cuc/README.md` mục 4).
   - File trong chat / Drive `tu-lieu-goc`: chép vào `~/Movies/tap-<tên>/1-goc/`.
   - Mac chính: thư mục Drive đồng bộ sẵn thì chép thẳng, không cần tải.
   - Tải lỗi vì quyền (link chưa mở chia sẻ) thì báo David một dòng: "link chưa mở quyền xem, anh bật 'Bất kỳ ai có đường liên kết'".
3. **Đọc thông số:** `ffprobe -v error -show_entries format=duration:stream=codec_type,width,height,r_frame_rate -of compact "<file>"` —
   độ dài, khung (ngang / dọc), số khung hình, có tiếng không. Nhiều file cùng một buổi thì sắp theo giờ quay (`creation_time`) hoặc tên file.
4. **Chuyển sang bước tiếp:** chép lời + lọc (`phan-phoi-da-kenh` bước 1, khối 00), rồi tạo dự án bằng `tao-du-an.sh` của skill dựng.

## Điểm duyệt
Không có: đây là phần chuẩn bị, làm trước điểm duyệt Đ1 của việc chính (`quy-trinh.md` mục 1). Không tải gì ngoài link David gửi.

## Xong khi
- File gốc nằm ở `~/Movies/tap-<tên>/1-goc/`, mở được, đã ghi độ dài, khung, có tiếng.
- Không link riêng tư nào bị ghi vào repo công khai.

## Kiểm gì
- Dung lượng file tải về khớp Drive / YouTube (không phải trang HTML báo lỗi quyền vài KB).
- Video nhiều tiếng (tiếng quán ồn) vẫn nghe được giọng David — không nghe được thì báo David trước khi làm tiếp.

## Lỗi hay gặp
- `gdown` báo quá lượt tải của Drive: thử lại sau, hoặc nhờ David tải về máy rồi gửi file.
- Lệnh từ Claude Windows chạy vào WSL: viết lệnh vào file `.sh` rồi `wsl.exe -d Ubuntu-24.04 -- bash <file>` (truyền chuỗi thẳng thì biến bị nở ở phía Windows).
