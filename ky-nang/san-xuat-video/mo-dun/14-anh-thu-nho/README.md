---
description: "Khối 14 thumbnail YouTube 1280×720 cho video ngang, chỉ dùng hình của chính video đó."
---

# Khối 14-anh-thu-nho: Thumbnail YouTube 1280×720 (chỉ video ngang đăng YouTube): quay hình = mặt + tối đa 3 tầng chữ; podcast = nền hoạ tiết + hình + tiêu đề

**Dùng trong:** làm video, ghép vlog, podcast
**Đầu vào:** quay hình: khung của CHÍNH video này / ảnh David gửi riêng cho video này · podcast không mặt: tiêu đề + tên hình
**Đầu ra:** phat-hanh/thumb-N.jpg (+ @160)
**Tham số hồ sơ:** chung: thumbnail.*
**Sửa khối này thì chạy lại:** —

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/anh-thu-nho.sh`
- `dung-video-theo-phong-cach/assets/mau-anh-thu-nho/`

## Luật
- Skill chỉ làm thumbnail khi video xuất **ngang** và đăng YouTube (điểm chốt trong 4 phần lúc đầu). Video dọc: chỉ ghi mốc khung bìa đề xuất.
- Mặt có cảm xúc rõ + 2–3 tầng chữ (tối đa `thumbnail.max_chu`), dòng màu cam là từ khoá to nhất; `THUMB_NUM` số khổng lồ; `THUMB_BADGE` nhãn series/số tập; `THUMB_L3` dòng 3.
- Chuẩn: một khuôn mặt có cảm xúc rõ (mắt mở, miệng/biểu cảm), chữ gọn (tối đa `thumbnail.max_chu` trong hồ sơ, càng ít càng mạnh), một ý. Chọn khung: xem `bang-khung-hinh.jpg`/`half_XX.jpg`, lấy
  khoảnh khắc cảm xúc mạnh nhất. Video ngang thì điểm cần chốt trong 4 phần lúc đầu (`thu-thap-yeu-cau`): "Video này có đăng YouTube
  không?"; nếu có thì skill làm 2 thumbnail, nếu không thì bỏ qua.
- Tiêu đề và thumbnail bổ sung cho nhau, không lặp chữ. Người dựng rà soát bản @160 (cỡ điện thoại); nếu không đọc được chữ thì giảm bớt chữ.
- **Chỉ hình của chính video đang làm:** thumbnail / ảnh bìa / khung bìa lấy từ khung của chính video này (hoặc ảnh David gửi RIÊNG
  cho video này) — không bao giờ lấy mặt, cảnh, ảnh từ video / dự án khác, kể cả khi "đẹp hơn" hay thuận tiện (trường hợp thumbnail podcast từng
  lấy mặt từ vlog Miếu Bà Cam là sai). AI không hỏi "lấy ảnh từ video cũ" như một lựa chọn. Podcast không mặt: theo mẫu dưới (hình vẽ
  theo nội dung là ngoại lệ duy nhất của luật lấy khung từ video).
- Lệnh: `zsh dung-video-theo-phong-cach/scripts/anh-thu-nho.sh "$P" <giây | cN@giây | ảnh> "<DÒNG 1>" "<DÒNG 2>" <số> [left|right] [vị trí] [phóng]`.

## Mẫu ảnh bìa podcast không mặt (mẫu: `mau-chuan/anh-thu-nho-podcast/chuan.jpg`)
Video chỉ có tiếng thì bìa **không có mặt người**, kể cả ảnh chụp riêng: bìa phải khớp thứ có trong video. Luật mặt người ở trên chỉ dùng cho video quay hình.

**Công thức:** nền hoạ tiết + một hình đại diện cho ý + tiêu đề ngắn + góc "DAVID · PODCAST".
- **Tiêu đề 2–6 từ:** ưu tiên câu hỏi người xem đang tự hỏi hoặc giải pháp ở mức gợi; có góc nhìn ngược số đông thì dùng câu đảo niềm tin. Nỗi đau dùng ít, nên kèm hướng gỡ. Không chép lại tiêu đề video.
- **Hình:** một hình vẽ theo ý của tập, không chữ. Hình nói về nội dung, không nói về định dạng: **không dùng micro, sóng âm làm hình chính**.
- **Không lộ giải pháp:** không liệt kê các bước lên bìa. Nếu bìa lộ hết giải pháp thì người xem không xem video nữa.
- **Chữ "PODCAST":** chỉ ghi nhỏ ở góc. Không ghi số tập. Giữ cùng mẫu ở mọi tập, chỉ đổi chữ + hình.
- **Đúng nội dung:** điều trên bìa phải có thật trong video. Không giật gân.
- Rà soát bản @160: người xem đọc được tiêu đề và nhận ra hình.

```bash
THUMB_HINH=danh-sach THUMB_TAG=PODCAST zsh dung-video-theo-phong-cach/scripts/anh-thu-nho.sh "$P" - "MÌNH GIỎI" "CÁI GÌ?" 1
```
`THUMB_HINH` = `danh-sach` hoặc tên trong `ICONS` của `thu-vien-tai-nguyen/bieu-tuong.jsx` (puzzle, target, people, tree...). Khi thiếu hình phù hợp, người dựng vẽ thêm vào `ICONS`. Nền và hình nằm ở `assets/mau-anh-thu-nho/hinh-podcast.jsx`.

**Căn cứ:** 5 kênh podcast không mặt có lượt xem cao (Better Version, Tri Kỷ Cảm Xúc, Hieu Nguyen, Vì sao thế nhỉ!, Tư Duy Và Sách) đều dùng hình theo nội dung cộng câu ngắn. Chỉ là mẫu nhỏ, có thể thử thêm bằng Test & Compare của YouTube.