---
description: "Tách một buổi nói dài (buổi gặp, buổi 1:1, bài giảng) thành nhiều video theo hướng công việc: chọn đoạn, cắt, mỗi video một dự án, dựng, phát hành."
---

# Tách buổi dài thành nhiều video theo hướng (cây quy trình lá B4)

**Khi nào dùng:** David nói "cắt đoạn thừa, phân ra thành các video theo hướng công việc" hoặc gửi một buổi nói dài nhiều chủ đề. Làm thật
lần đầu 22/11/2026 (buổi gặp 37 phút thành 3 video); kế hoạch dùng lại được ở [vi-du-tach-video.json](vi-du-tach-video.json).

**Đầu vào:** video buổi nói (nhận theo lá B2 `phan-phoi-da-kenh/references/nhan-tai-nguyen.md`).
Trong các lệnh dưới: `SKILL=~/Documents/bo-nao-david/ky-nang/san-xuat-video/dung-video-theo-phong-cach` (máy đã cài bộ não thì
`~/.claude/skills/dung-video-theo-phong-cach` trỏ cùng chỗ). Máy Windows: lệnh chạy trong WSL Ubuntu.

**Thứ tự với 4 phần:** bước 1–2 (nhận, làm sạch, chép lời, phân hướng) là phần lọc làm trước khi trình 4 phần, như `phan-phoi-da-kenh`
bước 0–1; bước 3 trở đi (cắt, dựng, phát hành) chỉ làm sau khi David duyệt.

## Các bước

### 1. Làm sạch + chép lời buổi gốc một lần
Công thức "Làm video" bước 1–6 của `SKILL.md` cho cả buổi (một dự án `tap-<buổi>`): làm sạch theo khối 02 (video dài giữ nguyên lời,
`quy-tac-chung.md` mục 2), chép lời và soát chữ ra `chuyen-dong/src/phu-de.js`. Các video tách ra dùng lại đúng phụ đề này, không chép lời lại.

### 2. Phân hướng theo khối 00 mục 0b (bắt buộc)
Chia đoạn, gán hướng, ghép trọn ý, ghi `<thư mục tập>/phan-huong.md` + nhật ký nội dung từng hướng (`du-an/nhat-ky-noi-dung/`), đối chiếu
kho 100 với hướng trainer: làm đúng [khối 00 mục 0b](../../mo-dun/00-sang-loc-noi-dung/README.md). Thêm khi tách từ một buổi dài:
- In lời theo khối 20 giây (mốc + chữ) để đọc hết một lượt; đoạn **thừa** gồm cả đoạn cầm máy cho xem màn hình mà máy quay không thấy.
- Phần đời thường / hành trình của David không thuộc hẳn hướng nào ra được bản riêng "nhân hiệu" (cây nội dung kênh trainer, khối 00 mục 1).
- Mốc mỗi đoạn lấy **đúng đầu / cuối câu** trong phụ đề (in các dòng quanh mốc để chọn).
- **Lằn ranh** (khối 00 mục 3): mặc định giữ lời; liệt kê từng câu trong 4 phần cho David chọn giữ hay cắt. David chọn cắt thì tách đoạn
  bỏ riêng câu đó. Người khác xuất hiện (đối tác, khách): ghi mục "cần họ đồng ý" vào gói phát hành; khách của công ty Veltrix thì
  hỏi David trước (`AGENTS.md`, hai bộ não).
- Trình David bảng "video · hướng · đoạn · dài" + đoạn cắt + lằn ranh + clip ngắn dự kiến (4 phần), có mặc định.

### 3. Cắt + tạo dự án (sau khi duyệt)
Viết `ke-hoach-tach.json` theo mẫu `vi-du-tach-video.json`: mỗi video `doan`, `topic`, `tuyen` (nhạc theo tuyến, khối 09), `ytEnd`
(màn kết YouTube, khối 15 / 08), rồi:
```bash
python3 -I $SKILL/scripts/tach-video.py ke-hoach-tach.json
```
Mỗi video ra `~/Movies/tap-<tên>/2-ban-day-du` có sẵn video gốc đã nối (đệm 0,12 s, fade âm 50 ms), phụ đề dời mốc, `du-an.js`,
`canh.js` khung có hàm `g()`, `ke-hoach-canh.md` khung, `kiem-tra/tach-video.json`.

### 4. Dựng từng video (như "Làm video", từ bước chẩn đoán)
- `canh.js`: viết mốc theo **video gốc** (đối chiếu phụ đề gốc dễ), bọc bằng `g(giây)`; cảnh tự vẽ dùng `ve(id, đầu, cuối, {…})`.
- Chẩn đoán + mở kho hình mẫu chọn cách cho từng ý (`thiet-ke-bo-cuc/tu-chon.md` bước 4d), ghi `Nguồn kho:`; các video cùng buổi được
  phép chung một kiểu hình (máy soát nhắc P1 "giống tập trước" thì bỏ qua được).
- `node $SKILL/scripts/soat-canh.mjs <dự án>`, rồi `bash $SKILL/scripts/anh-kiem-canh.sh <dự án>` (lưới ảnh mỗi cảnh trên khung thật),
  soát bằng mắt: không che ai, chữ đọc được.
- Render: `cd <dự án>/chuyen-dong && node xuat-video.mjs`, rồi `python3 -I $SKILL/scripts/xem-truoc-ban-dung.py <dự án>`; video từ
  khoảng 4 phút trở lên thêm teaser `doan-gioi-thieu.py <dự án> <từ-đến> …` (mốc trong video đã cắt = `g(giây gốc)`); video ngắn bỏ teaser.

### 5. Clip ngắn, phát hành, giao
- Clip ngắn mỗi video theo `phan-phoi-da-kenh` bước 4 (`cat-doan-noi-bat`), trừ khi David nói không cần.
- Ảnh thu nhỏ `anh-thu-nho.sh` (nguồn = giây trong video đã cắt); `phat-hanh/phat-hanh.md`: 3 tiêu đề, mô tả, chương (cộng độ dài teaser
  trong `phat-hanh/doan-gioi-thieu.json`), bình luận ghim, màn kết gắn các video cùng bộ, mục "Cần David quyết trước khi đăng".
- Giao theo cây quy trình lá A6.

## Điểm duyệt
- **Đ1** sau bước 2: bảng video theo hướng, đoạn cắt, lằn ranh (mặc định giữ lời), clip ngắn dự kiến. Chưa duyệt thì không cắt, không dựng.
- **Đ2**: đăng chỉ khi David nói "đăng"; dọn file tạm, đưa dự án lên Drive chỉ sau khi David chốt.
- Chế độ tự chạy (David nói rõ "làm tới khi có kết quả"): bỏ Đ1, lằn ranh theo mặc định giữ lời, ghi lại trong báo cáo; người khác
  xuất hiện (cả khách Veltrix) thì vẫn dựng, ghi "cần họ đồng ý" và hỏi ở Đ2; vẫn giữ Đ2 (`quy-trinh.md` mục 1).

## Xong khi
- Có `phan-huong.md` của tập + mục nhật ký nội dung từng hướng có ý.
- Mỗi video theo hướng là một dự án dựng xong: soát cảnh đạt, lưới ảnh kiểm không che ai, âm lượng −14 LUFS, có clip ngắn (hoặc ghi lý
  do không có), gói phát hành và ảnh thu nhỏ; đã giao theo lá A6.
- Kế hoạch tách đã dùng nằm ở `kiem-tra/tach-video.json` của từng dự án (chạy lại ra đúng video cũ).

## Kiểm gì
- Chạy lại `tach-video.py` với kế hoạch đã lưu ra đúng thời lượng và phụ đề cũ.
- Mỗi mối nối không cắt giữa từ; câu trỏ về trước ("như em nói lúc nãy") có kéo theo đoạn được nhắc hoặc đã bỏ.
