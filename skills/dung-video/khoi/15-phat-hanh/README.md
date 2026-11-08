# Khối 15-phat-hanh: Phát hành: 3 tiêu đề, mô tả, mốc khung bìa, chương YouTube, teaser, bình luận ghim

**Dùng trong:** cả 4
**Đầu vào:** video-final.mp4 + kịch bản
**Đầu ra:** phat-hanh/{phat-hanh.md, chuong.txt, teaser.json} · dang-bai.md (highlight)
**Tham số hồ sơ:** chung: youtube.*
**Sửa khối này → chạy lại:** teaser.py → chạy lại chapters.py

**File thật (code, một bản duy nhất):**
- `video-style-edit/scripts/chapters.py`
- `video-style-edit/scripts/teaser.py`

## Luật kênh David (05/11/2026 — `ho-so/kenh.json`, áp cho mọi bài lên kênh thương hiệu)
- **Lịch:** thứ Ba + thứ Sáu 20:00 giờ Việt Nam (hẹn giờ bằng chức năng có sẵn của nền tảng).
- **Mô tả / caption:** tóm ý theo lời David + câu hỏi "Vấn đề" / "Kết quả"; bài **Mời** thêm "nhắn mình một chữ 'gỡ'" + link nhắn tin trang
  (`kenh.fanpage.link_nhan_tin`); không nói giá. YouTube thêm chương nếu > 3 phút.
- **Bình luận ghim (mọi kênh):** "Bạn đang ở đâu? Bình luận **Vấn đề** (vì sao chưa làm được) hoặc **Kết quả** (làm được thì kết quả là gì)."
- **Không ghi lên video:** số tập, ngày ghi âm, thông tin phát hành. **Đo:** số người nhắn "gỡ" (khối 16), không lấy lượt xem làm thước đo chính.

## Cách làm (chuyển nguyên văn từ SKILL.md cũ — ngày 2026-11-04)

### 10. Phát hành + giao

Làm bước phát hành theo `../luat-chung.md` mục 7: `phat-hanh/phat-hanh.md` (3 tiêu đề, mô tả, hashtag) + mốc khung bìa đề xuất · **video xuất ngang VÀ
David đăng YouTube** (đã hỏi lúc đầu): 2 thumbnail (`zsh $SKILL/scripts/thumbnail.sh "$P" <giây> "<DÒNG 1>" "<DÒNG 2>" 1|2 …`, xem bản @160). Video dọc: không thumbnail.
Video > 3 phút đăng YouTube: `project.ytEnd = 20` trước render (màn kết), `teaser.py` (> 10 phút) rồi `chapters.py` (luat-chung 7).
Chép `dung-video/khoi/16-so-lieu/mau-so-lieu.md` → `$P/so-lieu.md` (điền phần đầu).
Gửi `video-final.mp4` (+ thumbnail nếu có) (SendUserFile). Báo ngắn gọn bằng tiếng Việt: danh sách cảnh theo mốc thời gian,
nếu có ảnh thì kèm nội dung `nguon-anh.txt` (dán vào mô tả bài đăng), tên riêng/chữ chưa chắc chính tả, đã kiểm tra gì, chưa
kiểm tra gì (ví dụ chưa đăng thử thật).

### 8. Phát hành + giao
Gửi `video-final.mp4` của từng clip (SendUserFile). Ghi `$P/dang-bai.md` (theo `../luat-chung.md` mục 7) và báo cáo tiếng Việt:
0. **Lịch đăng**: thứ tự clip (A mạnh nhất trước), cách nhau 1–2 ngày; mỗi clip: thẻ tít (nguyên văn), **mốc khung bìa đề xuất** (không ghép bìa), độ dài.
   Chép `dung-video/khoi/16-so-lieu/mau-so-lieu.md` → `$P/so-lieu.md`, một bảng cho mỗi clip.
1. **Loại video gốc → loại highlight**, **ý chính + lời kêu gọi chính của cả video**, **kiểu bố trí** + lý do, **tông** từng đoạn,
   **ý được chừa cho bản đầy đủ**.
2. **Bảng cắt** + **tổng độ dài** + kết quả kiểm lời; mọi chữ trên video kèm mốc gốc của nó.
3. **Mô tả bài đăng** ≤ 150 ký tự — ghép từ lời nguyên văn trong clip (không thêm ý), kết bằng lời mời bình luận
   "Vấn đề:" / "Kết quả:", kèm 3–5 hashtag tiếng Việt đúng chủ đề.
4. **Bình luận ghim** (mẫu cố định của người dùng):
   > Làm thử trong 48 giờ rồi quay lại đây:
   > **Vấn đề:** vì sao bạn chưa làm được
   > **Kết quả:** điều đã thay đổi
   > Bản đầy đủ trên YouTube: [link]
5. Câu bị loại vì lằn ranh (nếu có), tên riêng chưa chắc chính tả, đã kiểm gì / chưa kiểm gì.
6. Thẻ tít + thẻ cuối: chữ nào, căn cứ câu gốc nào (mốc), tên tập gốc.

Mục 1–6 làm **cho từng clip**.

Sửa theo góp
ý → như "Sửa theo góp ý" của skill dựng tương ứng; đổi câu/mốc/bố trí → sửa phuong-an.json, cắt lại, tạo lại dự án dựng.

