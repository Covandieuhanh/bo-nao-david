---
description: "Khối 15 phát hành: 3 tiêu đề, mô tả, khung bìa, chương, bài đăng."
---

# Khối 15-xuat-ban: Phát hành: 3 tiêu đề, mô tả, mốc khung bìa, chương YouTube, teaser, bình luận ghim

**Dùng trong:** cả 4
**Đầu vào:** video-hoan-chinh.mp4 + kịch bản
**Đầu ra:** phat-hanh/{phat-hanh.md, chuong.txt, doan-gioi-thieu.json} · dang-bai.md (highlight)
**Tham số hồ sơ:** chung: youtube.*
**Sửa khối này thì chạy lại:** doan-gioi-thieu.py → chạy lại chuong.py

**File thật (code, một bản duy nhất):**
- `dung-video-theo-phong-cach/scripts/chuong.py`
- `dung-video-theo-phong-cach/scripts/doan-gioi-thieu.py`

Luật phát hành chung (3 tiêu đề, thumbnail, khung bìa, màn kết, chương, teaser): `../../quy-tac-chung.md` mục 7.

## Luật kênh David (`ho-so-thuong-hieu/kenh.json`, áp cho mọi bài lên kênh thương hiệu)
- **Lịch:** thứ Ba + thứ Sáu 20:00 giờ Việt Nam (hẹn giờ bằng chức năng có sẵn của nền tảng).
- **Mô tả / caption:** tóm ý theo lời David + câu kết theo kiểu dẫn dắt của bài (khối 08); bài **Mời** thêm link nhắn tin trang
  (`kenh.fanpage.link_nhan_tin`). YouTube thêm chương nếu > 3 phút. Giọng văn + hashtag: `ho-so-thuong-hieu/giong-thuong-hieu-david.md`.
- **Bình luận ghim (mọi kênh)** theo kiểu dẫn dắt của bài (khối 08); câu mẫu bài Không: "Bạn đang ở đâu? Bình luận **Vấn đề** (vì sao
  chưa làm được) hoặc **Kết quả** (làm được thì kết quả là gì)." Clip ngắn thêm cuối: "Bản đầy đủ: [link YouTube]". Mẫu đã duyệt: `../19-dang-bai/mau-ke-hoach-dang.md`.
- **Không ghi lên video:** số tập, ngày ghi âm, thông tin phát hành. **Đo:** số người nhắn "gỡ" (khối 16), không lấy lượt xem làm thước đo chính.

## Cách làm — video thường (làm video, podcast, vlog)
Ghi `phat-hanh/phat-hanh.md` (3 tiêu đề, mô tả, hashtag) + mốc khung bìa đề xuất · **video xuất ngang VÀ David đăng YouTube** (đã hỏi
lúc đầu): 2 thumbnail (`zsh $SKILL/scripts/anh-thu-nho.sh "$P" <giây> "<DÒNG 1>" "<DÒNG 2>" 1|2 …`, xem bản @160, khối 14). Video dọc:
không thumbnail. Video > 3 phút đăng YouTube: `project.ytEnd = 20` trước render (màn kết), `doan-gioi-thieu.py` (> 10 phút) rồi `chuong.py`.
Chép `san-xuat-video/mo-dun/16-phan-tich-so-lieu/mau-so-lieu.md` → `$P/so-lieu.md` (điền phần đầu).
Gửi `video-hoan-chinh.mp4` (+ thumbnail nếu có) (SendUserFile). Báo ngắn gọn bằng tiếng Việt: danh sách cảnh theo mốc thời gian, nếu có ảnh
thì kèm nội dung `nguon-anh.txt` (dán vào mô tả bài đăng), tên riêng/chữ chưa chắc chính tả, đã kiểm tra gì, chưa kiểm tra gì (ví dụ
chưa đăng thử thật). Mẫu báo cáo: `dung-video-theo-phong-cach/references/ban-giao.md`.

## Cách làm — highlight
Gửi `video-hoan-chinh.mp4` của từng clip (SendUserFile). Ghi `$P/dang-bai.md` và báo cáo tiếng Việt, **cho từng clip**:
0. **Lịch đăng**: thứ tự clip (A mạnh nhất trước), cách nhau 1–2 ngày, đăng sau video dài; mỗi clip: thẻ tít (nguyên văn), **mốc khung
   bìa đề xuất** (0,3 s, không ghép bìa), độ dài. Chép `san-xuat-video/mo-dun/16-phan-tich-so-lieu/mau-so-lieu.md` → `$P/so-lieu.md`, một bảng cho mỗi clip.
1. **Loại video gốc thì loại highlight**, **ý chính + lời kêu gọi chính của cả video**, **kiểu bố trí** + lý do, **tông** từng đoạn,
   **ý được chừa cho bản đầy đủ**, bốn câu chọn ý + lời đọc nối.
2. **Bảng cắt** + **tổng độ dài** + kết quả kiểm lời; mọi chữ trên video kèm mốc gốc của nó.
3. **Mô tả bài đăng** tối đa 150 ký tự — ghép từ lời nguyên văn trong clip (không thêm ý), kết bằng lời mời bình luận "Vấn đề" / "Kết quả"
   theo kiểu dẫn dắt, kèm hashtag (giọng văn David).
4. **Bình luận ghim** theo luật kênh ở trên, có "Bản đầy đủ: [link YouTube]".
5. Câu bị loại vì lằn ranh (nếu có), tên riêng chưa chắc chính tả, đã kiểm gì / chưa kiểm gì.
6. Thẻ tít + màn chốt: chữ nào, căn cứ câu gốc nào (mốc), tên tập gốc.

Sửa theo góp ý thì làm như "Sửa theo góp ý" của skill dựng tương ứng; đổi câu/mốc/bố trí thì sửa phuong-an.json, cắt lại, tạo lại dự án dựng.
