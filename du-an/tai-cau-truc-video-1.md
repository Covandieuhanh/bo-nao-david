---
description: "Tái bản bộ skill video lần 1 (10/11): bảng 164 luật, mỗi luật một nhà."
---

# Tái bản bộ video — lần 1 (10/11/2026)

**Mục tiêu:** bộ skill video chỉ còn một bản luật hiện hành: mỗi luật một nhà, không ngày, không "thay luật cũ", không câu tự mâu thuẫn.
**Xong khi** (skill `tai-cau-truc`): (1) bảng dưới đủ, mỗi dòng có nhà trong bản mới · (2) máy đo "Chưa cần tái bản", câu trùng 0 ·
(3) `kiem-mau.py` y nguyên + một việc thật David chấm đạt · (4) tag `tai-ban-video-1`, dòng `lich-su.md`, đã đẩy GitHub.

Mốc trước: tag `tai-ban-video-1-truoc` (commit 8fb5b77).

## Bước 1 — Máy đo trước tái bản
```
## Bộ video — 50 file bản luật · mốc tái bản gần nhất: chưa có
  dau_ngay 165/30 · ghi_de 81/15 · trung 5/8 · sua 42/40 · dong 3292/4000
  Chồng nhiều nhất: quy-tac-chung.md (28 dấu ngày · 8 ghi đè) · khối 07 (13 · 9) · loi-thuong-gap.md (12 · 4) · thiet-ke-canh.md (6 · 6)
  · nhieu-doan-video.md (7 · 4) · cat-highlight SKILL (5 · 4) · ho-so-thuong-hieu/chung.md (8 · 3) · giong-van (6 · 3) · khối 09 (5 · 3) · khối 13 (2 · 4) …
  Câu trùng (5): "bước nhẹ…" ở 4 SKILL.md · 4 câu "video dọc ngắn…" ở cả quy-tac-chung §5 và nhan-dien-chung §1
  ⇒ NÊN TÁI BẢN: dau_ngay 165 > 30; ghi_de 81 > 15; sua 42 > 40
```

## Bước 2 — Bảng luật đang sống

Trạng thái: **sống** · **trùng** (một luật nhiều nhà → giữ một, nơi khác trỏ) · **ngược** (hai câu cãi nhau → ghi bên thắng) · **cũ** (đã bị luật mới hơn thay, bỏ).
Phân xử theo `chuan-muc-lam-viec.md` mục 0: lời David > ngày chốt gần nhất > cũ; còn mơ hồ → sản phẩm mới nhất David duyệt.

### A. Nền chung (quy-tac-chung, nguyen-tac, nhan-dien)
| # | Luật | Nhà mới | Nguồn hiện tại | Ngày | Trạng thái |
|---|---|---|---|---|---|
| A1 | Người xem là trung tâm; học kênh lớn ở nhịp + cách trình bày; mục tiêu ở lại → hiểu → làm theo | quy-tac-chung §0 | quy-tac-chung §0, nguyen-tac, tong-quan | 04/11, 08/11 | trùng → quy-tac-chung; nguyen-tac/tong-quan trỏ |
| A2 | Thẩm mỹ chỉ giữ chữ ký nhận diện; ngoài chữ ký sáng tạo tự do | nhan-dien-chung §0 (quy-tac-chung §0 trỏ) | quy-tac-chung §0, nhan-dien-chung §0, khối 07, phan-tich-video-mau | 10/11 | sống |
| A3 | Học mẫu chỉ thêm, không thay chặn cũ | thiet-ke-bo-cuc/README §4 (quy-tac-chung §0 trỏ) | quy-tac-chung §0, thiet-ke-bo-cuc, phan-tich-video-mau | 08/11 | trùng |
| A4 | Hiểu hơn cầu kì: mỗi video vài kiểu hợp nội dung; rối → bớt | quy-tac-chung §0 | quy-tac-chung §0, khối 07, khối 17 | 10/11 | sống (xem câu hỏi 1) |
| A5 | Không bịa: chữ = trích/bỏ bớt lời; giữ tên riêng, số, vế đối lập, phủ định | quy-tac-chung §1 | quy-tac-chung §1, scene-design, khối 01 | 04/11 | trùng |
| A6 | Chữ trên video nguyên văn lời David, không bỏ chữ đổi nghĩa, không số chạy số không nói | quy-tac-chung §1 | quy-tac-chung §1, thiet-ke-bo-cuc §3, 3 SKILL | 07/11 | sống |
| A7 | Câu Claude viết chỉ ở bài đăng (tiêu đề, thumbnail, mô tả, ghim) | quy-tac-chung §1 | quy-tac-chung §1 | 07/11 | sống |
| A8 | Ngoại lệ (a) câu màn chốt Claude tự viết ≤ 55 ký tự | — | quy-tac-chung §1, khối 07, khối 12, scene-design, multi-clip 4b | 04/11 | **cũ** (07/11: màn chốt nguyên văn) |
| A9 | Ngoại lệ (b) thẻ tít highlight viết như tít báo | — | quy-tac-chung §1 | 04/11 | **cũ** (08/11: tít = cụm nguyên văn) |
| A10 | Nhãn cố định của khung: lịch phát David đưa (`project.schedule`, `STAGE.schedule`, ke-hoach.json, endcard) — không tự đặt lịch | quy-tac-chung §1 | quy-tac-chung §1, khối 08 | 04/11 | trùng → quy-tac-chung; khối 08 trỏ |
| A11 | Lằn ranh nội dung (danh sách) — loại khỏi mọi chữ/clip; câu chủ chốt dính → báo David | quy-tac-chung §1 | quy-tac-chung §1, khối 00 §3, khối 13 | 04–05/11 | trùng |
| A12 | Whisper bịa câu ở đoạn không lời → bỏ | quy-tac-chung §1 | quy-tac-chung, khối 03, 13, gotchas, multi-clip | 04/11 | trùng |
| A13 | Tên riêng chưa chắc → dùng cách Whisper nghe, hỏi ở báo cáo; không thay bằng cụm chung | khối 01 (quy-tac-chung §1 trỏ) | quy-tac-chung, khối 01, gotchas | 04/11 | trùng |
| A14 | Mở đầu 0–3 s nói ngay video về gì / đặt cược gì | quy-tac-chung §2 | quy-tac-chung §2, nguyen-tac 1, khối 06 | 04/11 | sống |
| A15 | "Thẻ tiêu đề chữ to nửa trên, hiện từ giây 0" ở mọi video | — | quy-tac-chung §2 | 04/11 | **cũ** (07/11 không thẻ tít mặc định; còn ở highlight) |
| A16 | Video dài (> 3 phút) không cắt gì | quy-tac-chung §2 | quy-tac-chung §2, khối 02, khối 00, podcast SKILL | 05/11 | sống |
| A17 | Làm lại video cũ: cắt màn tít + lời chào/giới thiệu kênh cũ + chữ/viền kênh cũ in trong hình | quy-tac-chung §2 (cách làm: khối 02 + gotchas) | quy-tac-chung §2, khối 02, gotchas | 08/11 | trùng |
| A18 | Lằn ranh ở video dài: cảnh báo, David quyết; chữ đồ hoạ/tiêu đề/clip vẫn không lấy | khối 00 §3 (quy-tac-chung §2 trỏ) | quy-tac-chung §2, khối 00 §3 | 05/11 | trùng |
| A19 | Cắt lặng ≥ 0,45 s còn ~0,24 s + "ờ/ừm" chỉ cho video ≤ 3 phút và highlight; 1 s lặng sau câu hỏi kêu gọi | quy-tac-chung §2 | quy-tac-chung §2, khối 02, highlight luật 8 | 04/11 | sống |
| A20 | Video > 3 phút cắt lặng ≥ 1,2 s, giữ tiếng đệm | — | khối 02, ho-so-thuong-hieu/lam-video.md | 04/11 | **cũ** (05/11 không cắt) |
| A21 | Clip trích từ bản gốc, ưu tiên kéo về video dài; vlog ghép giữ nhịp tự nhiên | quy-tac-chung §2 | quy-tac-chung §2 | 04/11 | sống |
| A22 | Video ngắn không để 5–8 s không đổi gì; video ngắn đổi gì đó mỗi 1–3 s | quy-tac-chung §2 | quy-tac-chung §2, nguyen-tac 7 | 04/11 | trùng |
| A23 | Video dài ~1 điểm nhấn / 15–20 s; tối giản ~1 hiệu ứng / 15–20 s; mặt ≥ 60 %; card 4–8 s; toàn màn hình ≤ 15 s; mật độ 3–5 s (vlog) | — | quy-tac-chung §2, scene-design, podcast-design, khối 12, multi-clip | 02–04/11 | **cũ** (07/11 bỏ mọi con số bố cục) |
| A24 | Một màn = một ý, một hình, một câu; không chồng 2 lớp phủ | quy-tac-chung §2 | quy-tac-chung §2, scene-design, podcast-design | 04/11 | trùng |
| A25 | Đường cảm xúc + một đỉnh (mọi loại); vlog: hai đoạn liền cùng cảm xúc thì bỏ/đổi một | quy-tac-chung §2 (cách làm khối 07, kiểm khối 17) | quy-tac-chung §2, khối 07, khối 17 | 10/11 | sống |
| A26 | Phụ đề một nguồn `kieu-phu-de.js` | quy-tac-chung §3 | quy-tac-chung §3, khối 03, multi-clip 4b | 04/11 | trùng |
| A27 | Video ngắn (highlight, podcast dọc mọi độ dài, video 1 người dọc ≤ 90 s): cụm 5–8 chữ, cỡ 58, ngay trên thanh/đáy; ép tay `project.short` / `SHORT` | quy-tac-chung §3 | quy-tac-chung §3, khối 03, podcast SKILL, highlight luật 8, ho-so-thuong-hieu/chung.md, code phu-de.jsx | 08/11 | sống (thêm "podcast dọc mọi độ dài" theo code) |
| A28 | Phụ đề 1–3 chữ to mỗi nhịp | — | tong-quan | 04/11 | **cũ** |
| A29 | Mỗi lúc một chỗ chữ: lớp có chữ hiện thì phụ đề nhường; `giuPhuDe` | quy-tac-chung §3 | quy-tac-chung §3, khối 03, memory | 08/11 | sống |
| A30 | Video dài, vlog, podcast ngang: hộp tối đầy câu ở đáy | quy-tac-chung §3 | quy-tac-chung §3, khối 03 | 04/11 | sống (podcast dọc theo A27) |
| A31 | Podcast đồ hoạ dọc trích ngắn: chữ chính thay phụ đề | quy-tac-chung §3 (cách làm highlight 7B) | quy-tac-chung §3, highlight 7B | 06/11 | trùng |
| A32 | Màu theo nghĩa `+`/`-` trong `hl` | quy-tac-chung §3 | quy-tac-chung §3 | 04/11 | sống |
| A33 | Phụ đề đầy đủ, đúng từng chữ; không đốt bằng ffmpeg | quy-tac-chung §3 | quy-tac-chung §3, khối 03, highlight "không làm" | 04/11 | trùng |
| A34 | Mọi video có motion graphics = điểm nhấn kéo mắt, nhiều loại, dựng nhẹ vẫn có | quy-tac-chung §4 | quy-tac-chung §4, khối 07, dung-video-theo-phong-cach luật 3, memory | 07/11 | **ngược một phần với A4** → câu hỏi 1 |
| A35 | Bố cục tự cân: không con số bố cục; chọn từ `thiet-ke-bo-cuc/bo-cuc.md`; ngang tự do, dọc mỗi lúc ít thứ | thiet-ke-bo-cuc/README §2 (quy-tac-chung §4 trỏ) | quy-tac-chung §4, nguyen-tac 2, thiet-ke-bo-cuc, khối 07, scene-design | 07/11 | trùng |
| A36 | Không che người nói, không đè phụ đề; nhiều người: không đè ai, bám người đang nói | quy-tac-chung §4 (cách làm khối 05) | quy-tac-chung §4, khối 05, khối 07, thiet-ke-bo-cuc §3, memory | 04–08/11 | trùng |
| A37 | Che mặt/thân trên → tự toàn màn hình, dài theo nội dung; chỉ chạm tay/bụng/nền thì giữ | khối 05 (quy-tac-chung §4 trỏ) | quy-tac-chung §4, khối 05, khối 07, multi-clip | 04/11, 07/11 | trùng; "≤ 4 s" ở mo-dun/README, multi-clip **cũ** |
| A38 | Vùng an toàn dọc x 70–900, y 210–1420; ngang lề 5 %, dưới 15 % | nhan-dien-chung §1 | quy-tac-chung §4, nhan-dien-chung, scene-design, podcast-design | 04/11 | trùng |
| A39 | Chữ tiếng Việt đủ dấu, không chồng dòng (`VN`) | quy-tac-chung §4 | quy-tac-chung §4, gotchas | 04/11 | trùng |
| A40 | Minh hoạ mặc định biểu tượng vẽ; ảnh thật chỉ cho cái thật; số liệu bằng hiệu ứng đúng số; bằng chứng thật trong clip → ưu tiên chiếu | quy-tac-chung §4 | quy-tac-chung §4, khối 07, scene-design, podcast SKILL | 04/11 | trùng |
| A41 | Không ghi chú kỹ thuật trên video; không màn nguồn ảnh cuối → `nguon-anh.txt` | quy-tac-chung §4 | quy-tac-chung §4, multi-clip §3, handoff | 04/11 | trùng |
| A42 | Khung xuất = khung gốc trừ khi David yêu cầu; highlight luôn dọc | quy-tac-chung §4 | quy-tac-chung §4, khối 04, highlight luật 1 | 04/11 | trùng |
| A43 | Bộ nhận diện một nguồn (thuong-hieu.json, tokens/theme, subStyle, cta, Icons); sửa thì đồng bộ 4 loại | nhan-dien-chung (quy-tac-chung §5 trỏ) | quy-tac-chung §5, tong-quan, khối 10 | 04/11 | trùng |
| A44 | Thành phần cố định cùng vị trí mọi loại (dấu góc, thanh, phụ đề, màn chốt, thẻ cuối) | nhan-dien-chung §1 | quy-tac-chung §5, nhan-dien-chung | 08/11 | trùng |
| A45 | Dấu góc: dọc 228, ngang sát mép trên; lớp phủ góc trên dưới `BRAND_BOT`; màn chốt ngang ẩn dấu góc | nhan-dien-chung §1 | quy-tac-chung §5, nhan-dien-chung, gotchas | 08/11 | trùng |
| A46 | Thanh thời gian: video ngang + dọc dài | nhan-dien-chung §1 | quy-tac-chung §5, nhan-dien-chung, podcast SKILL | 08/11 | trùng |
| A47 | Video dọc ngắn: không thanh, không thẻ cuối, màn chốt trên hình, tự lặp; ép tay `thanh`/`theCuoi`/`THANH`/`THE_CUOI` | nhan-dien-chung §1 | quy-tac-chung §5 + nhan-dien-chung (4 câu trùng), khối 08, highlight, podcast | 10/11 | trùng → chỉ còn nhan-dien-chung |
| A48 | Clip ngắn cũng có thanh thời gian | — | cat-highlight SKILL | 08/11 | **cũ** (10/11) |
| A49 | Âm thanh nhận diện: `sting.wav` lúc tiêu đề, "ting" ở màn chốt, giọng −20 LUFS, bản cuối −14 LUFS | khối 09 (quy-tac-chung §5 trỏ) | quy-tac-chung §5, tong-quan, khối 09 | 04/11 | trùng |
| A50 | Ưu tiên câu mệnh lệnh nằm sẵn trong lời; màn hành động 1–2 lần/video đúng lúc giao việc | quy-tac-chung §6 | quy-tac-chung §6, dung-video-theo-phong-cach luật 4 | 04/11 | trùng |
| A51 | Màn chốt ~4 s cuối mọi video = nguyên văn; mời bình luận/"gỡ" ở mô tả + ghim, không lên video (trừ khi David tự nói) | quy-tac-chung §6 (chi tiết khối 08) | quy-tac-chung §6, khối 08, 3 SKILL | 07–08/11 | trùng |
| A52 | Phát hành ghi `phat-hanh/phat-hanh.md`: 3 tiêu đề ≤ 60 ký tự, bổ sung thumbnail | quy-tac-chung §7 | quy-tac-chung §7, khối 15 | 04/11 | trùng |
| A53 | Thumbnail chỉ khi ngang + YouTube; hỏi "có đăng YouTube không?" | khối 14 (quy-tac-chung §7 trỏ) | quy-tac-chung §7, khối 14, khối 15, tong-quan, nhan-dien-thuong-hieu.md | 04/11 | trùng |
| A54 | Chỉ hình của chính video (thumbnail, bìa); không hỏi "lấy ảnh video cũ" | khối 14 | quy-tac-chung §7, khối 14 | 05/11 | trùng |
| A55 | Podcast không mặt: bìa = nền hoạ tiết + hình vẽ theo ý + tiêu đề ngắn + "DAVID · PODCAST", không lộ bước | khối 14 | quy-tac-chung §7, khối 14, podcast SKILL | 06/11 | trùng |
| A56 | Bìa podcast = khung cảnh minh hoạ của chính video-hoan-chinh | — | khối 14 luật | 06/11 (sớm hơn mẫu) | **cũ** (mẫu bìa không mặt cùng ngày, sau) |
| A57 | Video dọc: không ghép bìa trước video; ghi mốc khung bìa đề xuất | quy-tac-chung §7 | quy-tac-chung §7, khối 14, podcast SKILL | 04/11 | trùng |
| A58 | Thumbnail kiểu Việt: mặt + 2–3 tầng chữ, `THUMB_NUM/BADGE/L3` | khối 14 | quy-tac-chung §7, khối 14 | 04/11 | trùng |
| A59 | Video > 3 phút đăng YouTube: màn kết 15–20 s (`ytEnd`), chương (`chuong.py`), teaser 15–25 s khi > 10 phút (chạy trước chapters) | quy-tac-chung §7 (lệnh ở khối 15, 08) | quy-tac-chung §7, khối 08, 15, 3 SKILL | 04/11 | trùng |
| A60 | Hashtag 3–5 tiếng Việt | — | quy-tac-chung §7, khối 15 | 04/11 | **ngược với A112 (2–3)** → thắng: 2–3 (05/11 + mẫu đăng đã duyệt) |
| A61 | Gửi David video + thumbnail (SendUserFile) + tiêu đề | quy-tac-chung §7 | quy-tac-chung §7, khối 15 | 04/11 | trùng |
| A62 | Hỏi một lần đầu; ngoại lệ dừng duyệt: kế hoạch ghép vlog | quy-tac-chung §8 (thói quen chung: thoi-quen mục 2) | quy-tac-chung §8, 3 SKILL | 08/11 | trùng |
| A63 | Lệnh > 2 phút chạy nền; không nhập mật khẩu máy; không tải video từ YouTube/TikTok để dựng | quy-tac-chung §8 | quy-tac-chung §8, gotchas, highlight | 04/11 | trùng |
| A64 | Chụp thử trước render; kiểm bản cuối (−14 LUFS, đỉnh ≤ −1,5, rè ≤ +1 dB so giọng, nhạc ~23 dB dưới giọng, thời lượng) | khối 17 + 09 (quy-tac-chung §8 trỏ) | quy-tac-chung §8, khối 09, 17, 3 SKILL | 06–10/11 | trùng |
| A65 | Báo cáo tiếng Việt: làm gì, kiểm gì, chưa kiểm, tên riêng cần xác nhận | quy-tac-chung §8 | quy-tac-chung §8, khối 15, handoff | 04/11 | trùng |
| A66 | Vòng số liệu: `so-lieu.md` mỗi video; 7 ngày; một đề xuất có bằng chứng, David duyệt | khối 16 (quy-tac-chung §9 trỏ) | quy-tac-chung §9, khối 16, 15 | 04/11 | trùng |
| A67 | 7 nguyên tắc cốt lõi (hiếm đổi) | nguyen-tac.md | nguyen-tac | 04/11 | sống (bỏ chữ "Thay luật 2 trạng thái") |
| A68 | Bộ định tuyến: lọc trước (khối 00), ⛔/👤/🗂 không dựng; bảng đầu vào → loại → skill → hồ sơ; câu hỏi lúc đầu | nhan-dien-thuong-hieu.md | nhan-dien-thuong-hieu.md, khối 00 | 05/11 | sống |

### B. Khối (mo-dun/*)
| # | Luật | Nhà mới | Nguồn hiện tại | Ngày | Trạng thái |
|---|---|---|---|---|---|
| B1 | David chỉ đưa tài nguyên; Claude phân tích, đề xuất, hỏi lại một vòng; David chốt | khối 00 | khối 00, phan-phoi-da-kenh | 05/11 | sống |
| B2 | Câu hỏi gốc + cây nội dung | khối 00 §1 | khối 00 | 05/11 | sống |
| B3 | Đối chiếu kho 100 video (khớp / ⚠️ lệch / giai đoạn 3 / ý kế tiếp / đổi trạng thái) | khối 00 §1b | khối 00, phan-phoi-da-kenh | 10/11 | sống |
| B4 | Chấm 5 tiêu chí; khung 3 phần được sắp lại thứ tự, thiếu thì báo | khối 00 §2 | khối 00 | 05/11 | sống |
| B5 | Chấm cả câu chuyện, không chấm từng đoạn | khối 00 §2 | khối 00 | 05/11 | sống |
| B6 | 7 kết luận; phân phối kênh; phiếu lọc; sổ danh mục + cảnh báo | khối 00 §4–7 | khối 00 | 05/11 | sống |
| B7 | Chép lời, kiểm môi trường; Whisper 1,5 GB hỏi trước khi tải | khối 01 | khối 01 | 04/11 | sống (bỏ "chuyển nguyên văn") |
| B8 | Làm sạch luôn chạy; chiều hình; đầu/cuối; nói lại giữ lần sau cùng, nghi thì giữ; jump cut 1,08×; "giữ ngập ngừng" → `tu-nhien` | khối 02 | khối 02, dung-video-theo-phong-cach luật 5 | 04/11 | sống |
| B9 | Làm lại video cũ: cut tay `ok: true`, `zoom: "none"`, `doi-moc-loi.py` | khối 02 | khối 02 | 08/11 | sống |
| B10 | Sửa phụ đề từng dòng: chính tả, câu mất/bịa, ngắt dòng | khối 03 | khối 03 | 04/11 | sống |
| B11 | Lớp phủ thu 78 %, đặt tránh mặt; cảnh toàn màn hình chừa ~140 px đáy | khối 03 → chuyển khối 05 | khối 03, scene-design | 04/11 | sống (đổi nhà cho đúng việc) |
| B12 | Bảng tự sửa chữ `chu-tren-man.mjs` | khối 03 | khối 03 | 06/11 | sống |
| B13 | Đổi khung ngang↔dọc, nâng khung (`nang-lop.py`), khung xuất mặc định; ngang là thiết kế toàn khung (podcast) | khối 04 | khối 04, dung-video-theo-phong-cach | 04/11 | sống |
| B14 | Tít ghim che đầu → tự ẩn; `place` / `keep`; lệnh face_place / overlay_guard; `nhan`/`bocuc` qua `vi-tri-nhan.py` + `cho.js` | khối 05 | khối 05, khối 07, quy-tac-chung §4 | 04–08/11 | sống |
| B15 | Không thẻ tít mở đầu mặc định (làm video, podcast); chỉ khi David yêu cầu, nguyên văn | khối 06 | khối 06, quy-tac-chung §1, 3 SKILL | 07/11 | sống |
| B16 | "Cảnh đầu tiên luôn là hook" (rút ý cả video) | — | khối 07 dòng 112, scene-design, khối 12 | 04/11 | **cũ** (07/11, thắng theo ngày) |
| B17 | Lỗi `hook` 2 dòng bị cắt ở khung ngang → sửa trước khi dùng lại | khối 06 | khối 06 | 07/11 | sống |
| B18 | Highlight: thẻ tít = cụm nguyên văn đắt nhất, 2 dòng, pow 0–2,5 s; khung 0,3 s = bìa | khối 06 (chi tiết highlight luật 7) | khối 06, highlight luật 7, 13 | 08/11 | trùng |
| B19 | Vlog: đoạn ghép mở đầu (kiểu 1/2/3) | multi-clip 2d (khối 06 trỏ) | khối 06, multi-clip | 04/11 | trùng; thẻ tiêu đề vlog → câu hỏi 3 |
| B20 | Motion graphic kể chuyện; mạch hình; vẽ tiếp; cảnh tự vẽ `ve`; ghi `ke-hoach-canh.md` | khối 07 | khối 07, dung-video-theo-phong-cach luật 1 | 09/11 | sống |
| B21 | "Giữ nền, màu chủ đạo, kiểu vẽ biểu tượng" khi sáng tạo | — | dung-video-theo-phong-cach luật 1 | 09/11 | **cũ** (10/11 chỉ giữ chữ ký) |
| B22 | Câu cảm xúc, chuyện riêng thì để thấy mặt; đã vào là đứng yên | khối 07 | khối 07 | 09/11 | sống |
| B23 | Đường cảm xúc: mẫu ghi, gợi ý cảm xúc, một đỉnh, cột "cảm xúc" | khối 07 | khối 07 | 10/11 | sống |
| B24 | Kho mới: `muc-luc`, `tien-trinh`, `canh-nguoi`, `phong`, `*từ*`; mỗi khung một tiêu điểm; cam ~10 % | khối 07 (kho ở bo-cuc.md) | khối 07 | 10/11 | sống |
| B25 | Không hai cảnh cùng kiểu liền nhau (trừ vẽ tiếp); giữ cùng kiểu có lý do thì ghi | khối 07 | khối 07, khối 17 | 10/11 | sống |
| B26 | "Không dùng 1 loại cảnh quá 3 lần liên tiếp" | — | scene-design, podcast-design | 02/11 | **cũ** (B25 chặt hơn) |
| B27 | 4 câu hỏi chọn bố cục; ghi lý do mỗi cảnh; bố cục đã có code | thiet-ke-bo-cuc §2 + khối 07 | khối 07, thiet-ke-bo-cuc | 07/11 | trùng |
| B28 | `nhan`: 4 kiểu (zoom/toi/text/icon), ví dụ, không chồng, đoạn lằn ranh không dùng; khung ghép dùng zoom + pow | khối 07 | khối 07, scene-design | 07/11 | sống |
| B29 | "Dựng nhẹ" vẫn có (~3 illus + ~4 nhan + chốt cho video ~4 phút); trộn loại để mắt không quen | khối 07 | khối 07 | 07/11 | → câu hỏi 1 |
| B30 | `illus` 5 mode + cách viết ở 3 khung dựng; biểu tượng `bieu-tuong.jsx`, thiếu thì vẽ thêm | khối 07 | khối 07, scene-design | 04/11 | sống |
| B31 | Lớp chữ cũ tự chuyển toàn màn hình khi che người; card/action bỏ câu trích dài; ưu tiên `illus` | khối 07 | khối 07, scene-design | 04/11 | sống |
| B32 | Card: `quote` NGUYÊN VĂN ĐẦY ĐỦ câu, không bỏ bớt; 4–8 s | scene-design (ý nguyên văn còn) | scene-design | 02/11 | **ngược** với B31 (04/11): câu trích dài bị bỏ; giữ "nếu có quote thì nguyên văn" |
| B33 | Ô chữ tóm ý được ưa; biểu tượng chỉ thay ảnh, không thay hết chữ | scene-design | scene-design | 02/11 | sống |
| B34 | Màn chốt cuối luôn (cảnh `cta`, thời lượng − 4); quét câu hành động → `action` | khối 08 (khối 07 trỏ) | khối 07, 08, 12 | 04/11 | trùng |
| B35 | `SIDES` khi xuất ngang từ gốc dọc | khối 07 | khối 07 | 04/11 | sống |
| B36 | Ảnh: khi nào, openverse, loại bỏ gì, "không dùng ảnh"/"thêm ảnh" | khối 07 | khối 07, scene-design, gotchas | 04/11 | trùng |
| B37 | Giữ cảnh sau chữ cuối (`giu_sau_s`, `giu.js`, `keepEnd`) | khối 07 | khối 07, ho-so-thuong-hieu/chung.md | 05/11 | sống |
| B38 | Sơ đồ nói thay lời (`diagram` 10 mode) + ảnh khung bo góc; podcast dài ưu tiên diagram | khối 07 | khối 07, podcast SKILL | 05/11 | sống |
| B39 | Luật chuyển động (đứng yên, vào dài ra gọn, kiểu vào theo ý, chỉ vị trí/cỡ nảy, vào qua vật, không cắt theo nhạc) + bản nâng (easing theo vai, so le, ChuHien, thoát, docDu, loXo, chuyển cảnh 3–5 kiểu, soát "máy làm") | khối 07 (gộp một mục) | khối 07 | 06/11, 09/11 | sống (gộp, bỏ "Bổ sung 09/11") |
| B40 | Podcast dọc trích ngắn: màn chốt/kết theo luật highlight | khối 08 | khối 08 | 08/11 | sống |
| B41 | Dẫn dắt theo luật kênh (4·4·2): Không / Gợi mở / Mời → mô tả + ghim; David tự nói thì màn chốt dùng câu đó | khối 08 | khối 08, khối 15, giong-van | 05/11, 08/11 | sống |
| B42 | Màn chốt: video lùi vào khung bo góc + câu + biểu tượng + tick + "ting"; `kind` theo ý câu | khối 08 | khối 08, scene-design | 07/11 | sống |
| B43 | Thẻ cuối: nhận diện (chủ đề + DAVID) cho video ngang / dọc dài; không nút phát, không logo nền tảng | nhan-dien-chung §1 + khối 08 | khối 08, nhan-dien-chung, tong-quan, multi-clip §10 | 06/11, 10/11 | sống; "nút phát đỏ" (multi-clip, tong-quan) **cũ** |
| B44 | Kho nhạc kênh, Claude tự chọn theo tuyến, không hỏi; bài mới → đặt tên, đo, ghi `nhac.muc` | khối 09 | khối 09, multi-clip §8 | 08/11 | sống |
| B45 | Chuẩn âm lượng chung: nhạc ~23 dB dưới giọng, cả bài −14 LUFS ±0,5, đỉnh −1,5, `chuan-am.py` | khối 09 | khối 09, thiet-ke-bo-cuc, highlight luật 9 | 06/11 | sống |
| B46 | Nhạc 20 LU (vlog) / 22 LU / 30–33 LU; "highlight giữ mức cũ" | — | tong-quan, khối 09 §3, multi-clip 3b, ho-so-thuong-hieu/chung.md | 04–05/11 | **cũ** (06/11 chuẩn chung mọi đầu ra) |
| B47 | Tuyến nội dung bắt buộc (`project.tuyen`, ghi sau clean_apply; thiếu → dừng); ép bài `nhac` | khối 09 | khối 09, 3 SKILL | 05/11 | sống |
| B48 | Không so dB thô với nguồn khi kiểm | khối 09 | khối 09, 17, podcast SKILL | 10/11 | trùng |
| B49 | Rút phong cách từ video mẫu → phong-cach.md; mẫu ngang mà gốc dọc thì giữ tinh thần | khối 10 | khối 10, style-analysis | 04/11 | sống, nhưng **ngược** phần "áp màu, font vào chu-de.js" với A2 → thắng A2: màu nhấn cam + 2 font không đổi |
| B50 | Ghép cảnh: chi tiết ở multi-clip | khối 11 | khối 11 | 04/11 | sống |
| B51 | Sân khấu podcast: speakers (pyannote), sóng âm, tên người nói chỉ khi có; STAGE, TOPICS phủ kín, đổi thưa | khối 12 | khối 12, podcast-design | 04/11, 07/11 | sống |
| B52 | Podcast: SCENES "hook đầu tiên"; "~1 cảnh / 15–20 s, mỗi cảnh ≤ 15 s"; cta "Claude tự sáng tạo" | — | khối 12 | 04/11 | **cũ** (07/11 không hook; 06/11 phủ ~30 %; 07/11 cta nguyên văn) |
| B53 | Highlight bước 0–6: nhận loại nguồn, dự án, bản đồ cả video, vai câu, tự chọn ý theo 4 câu, câu mở, chừa lại, thẻ tít, bố trí kêu gọi (4 kiểu), kiểm tự đứng + lằn ranh, cắt + kiểm lời | khối 13 | khối 13, highlight SKILL | 03–07/11 | sống |
| B54 | Vòng lặp: "thẻ cuối bỏ ở kiểu này" | — | khối 13 | 04/11 | **cũ** (mọi clip dọc không thẻ cuối) |
| B55 | Không có HANHDONG/KEUGOI → "dừng, báo người dùng" | — | khối 13 bước 5 | 03/11 | **cũ** (08/11: không dừng, kết ở câu chốt ý) |
| B56 | Thumbnail: lệnh, mẫu podcast không mặt, căn cứ | khối 14 | khối 14 | 06/11 | sống |
| B57 | Luật kênh: lịch T3 + T6 20:00, mô tả/caption, ghim, không ghi lên video số tập…; đo bằng "gỡ" | khối 15 (dữ liệu `kenh.json`) | khối 15, khối 16, 20, phan-phoi-da-kenh | 05/11 | sống |
| B58 | Ghim highlight "Làm thử trong 48 giờ… Vấn đề/Kết quả… Bản đầy đủ" | — | khối 15 §8 | 03/11 | **ngược** với B57 (05/11) → thắng B57 + mẫu đăng đã duyệt (câu hỏi theo kiểu dẫn dắt + "Vấn đề"/"Kết quả" + link bản đầy đủ) |
| B59 | Giao bản video thường (mục 10) và highlight (mục 8: lịch đăng, báo cáo 1–6 từng clip, mô tả ≤ 150 ký tự từ lời nguyên văn) | khối 15 | khối 15 | 04/11 | sống (bỏ "thẻ cuối" ở mục 6) |
| B60 | Số liệu báo lỗi, không quyết định; thước đo chính "gỡ" | khối 16 | khối 16 | 05/11 | sống |
| B61 | Chụp thử từng cảnh + composite, pillar, render, kiểm bản cuối | khối 17 | khối 17 | 04/11 | sống |
| B62 | Soát cảnh tự động `soat-canh.mjs` P0/P1/P2; xem tờ ảnh đúng cỡ; câu hỏi "video có rối không" | khối 17 | khối 17 | 06/11, 10/11 | sống |
| B63 | Kiểm cảm nhận (xem lạnh → so → sửa video) | khối 17 | khối 17 | 10/11 | sống |
| B64 | Dọn file tạm khi David chốt / đã đăng: `don-tap.py --xoa`, không hỏi; chỉ hỏi ⏸; giữ/xoá/Thùng rác | khối 17 (thói quen chung trỏ) | khối 17, 3 SKILL, thoi-quen | 08/11 | trùng |
| B65 | Đăng bài: luật an toàn, thứ tự hẹn giờ, trình duyệt, từng nền tảng | khối 19 | khối 19 | 05–06/11 | sống (ngày quan sát → bỏ ngày) |
| B66 | Hộp thư + số liệu chỉ đọc; ẩn danh | khối 20 | khối 20 | 05/11 | sống |

### C. Công thức (SKILL.md), hồ sơ, tài liệu kèm
| # | Luật | Nhà mới | Nguồn hiện tại | Ngày | Trạng thái |
|---|---|---|---|---|---|
| C1 | dung-video-theo-phong-cach: hỏi một lần đầu gồm "chữ bìa, câu chốt, cảnh chính, khung xuất" | dung-video-theo-phong-cach | dung-video-theo-phong-cach, phan-phoi-da-kenh cổng 1 | 08/11 | **ngược một phần** với thoi-quen mục 2 "phần cứng không hỏi (màn chốt)" 10/11 → thắng 10/11: không hỏi câu chốt |
| C2 | dung-video-theo-phong-cach luật riêng 2–8 (topic ≤ 3 chữ, bố cục, action/cta, làm sạch, face_place, không bản DaVinci, học 20 video: listItem, thẻ tóm tắt, CHAPTERS) | dung-video-theo-phong-cach | dung-video-theo-phong-cach | 04–08/11 | sống |
| C3 | Chọn chế độ, đầu vào, khung xuất, công thức 12 bước, bảng phụ thuộc, tiêu chí đạt, sửa góp ý, cấu trúc, Xong khi | dung-video-theo-phong-cach | dung-video-theo-phong-cach | 08/11 | sống |
| C4 | podcast: chỉ nội dung gốc, không cắt, cỡ vừa phải, không thẻ tít/bìa, không số tập, thanh thời gian, màn chốt nguyên văn, học Hieu Nguyen (30 %), học 20 podcast | podcast SKILL | podcast SKILL | 04–10/11 | sống |
| C5 | podcast: "thumbnail khuôn cố định câu hỏi/câu trích 2–3 tầng" | khối 14 (mẫu không mặt) | podcast SKILL | 04/11 | **cũ** phần chữ (06/11 mẫu không mặt: tiêu đề 2–6 từ) |
| C6 | podcast: hỏi một lần (chữ thumbnail, TOPICS, nền) + cổng chụp thử | podcast SKILL | podcast SKILL | 06/11 | sống |
| C7 | highlight: hai mục tiêu, bốn câu chọn ý (thắng mọi luật khác), không con số cố định | highlight SKILL | highlight SKILL, khối 13 | 07/11 | sống |
| C8 | highlight luật 1–13 | highlight SKILL | highlight SKILL | 04–10/11 | sống, trừ: luật 11 thẻ cuối **cũ** (giữ một dòng "không thẻ cuối"), luật 13 tít ghim → mặc định **tắt** (hồ sơ `tit_ghim: false`, bật từng clip `"pin": true`) |
| C9 | highlight 7A/7B: lệnh, danh-sach-cat.js, ENDCARD, tông, nhạc | highlight SKILL | highlight SKILL | 04–10/11 | sống, bỏ phần dựng thẻ cuối (khuôn tự bỏ ở dọc ngắn) |
| C10 | highlight 7B "hình dày theo lời — mỗi cụm lời một biểu tượng ở đoạn không có cảnh" (học Pháp Hoà) | highlight SKILL | highlight SKILL | 04/11 | **ngược một phần** với A4 (10/11) → câu hỏi 2 |
| C11 | Mô tả skill + tiêu chí đạt highlight còn ghi "thẻ cuối 'Bản đầy đủ trên kênh …'" | highlight SKILL | highlight SKILL | 08/11 | **cũ** (10/11) |
| C12 | phan-tich-video-mau: cửa vào, 3 điều, Xong khi 6 dòng | phan-tich-video-mau | phan-tich-video-mau | 08/11 | sống; Xong khi #2 "màu, font, nét vẽ, chuyển động, nhạc không đổi" **ngược** với A2 → câu hỏi 4 |
| C13 | thiet-ke-bo-cuc §1 "Thẩm mỹ không đổi, không chép màu, font, chuyển động" | thiet-ke-bo-cuc | thiet-ke-bo-cuc §1 | 07/11 | **cũ** (10/11 chỉ giữ chữ ký) |
| C14 | phan-phoi-da-kenh: vai trò, 8 bước 2 cổng, làm song song, luật riêng, Xong khi | phan-phoi-da-kenh | phan-phoi-da-kenh | 05–10/11 | sống |
| C15 | Hồ sơ: đổi số → sửa hồ sơ + nhật ký; hai hình mẫu mâu thuẫn → hình mẫu chính | ho-so-thuong-hieu/README | ho-so-thuong-hieu/README, tong-quan | 04/11 | sống |
| C16 | ho-so-thuong-hieu/chung.md: khoá đã bỏ (gạch), `nhac.*` mức 30–33 LU | ho-so-thuong-hieu/chung.md | ho-so-thuong-hieu/chung.md | 05–07/11 | **cũ** phần mức nhạc (06/11) và dòng khoá đã bỏ |
| C17 | Giọng văn David: quan sát, giữ/bỏ, nâng cấp giọng, 8 luật khi viết, ví dụ | ho-so-thuong-hieu/giong-thuong-hieu-david.md | giong-van | 05–06/11 | sống (bỏ ngày đọc) |
| C18 | Kiến trúc bộ: sửa đúng một chỗ; bảng "muốn → sửa ở đâu"; nơi lưu tập; công cụ phụ đừng xoá | tong-quan | tong-quan | 04–07/11 | sống; phần "Luật đã chốt" + "Bộ nhận diện" chép lại luật → **trùng**, đổi thành trỏ |
| C19 | Thư viện hình dùng chung + cách nối (lối tắt, `cp -RL`) | thu-vien-tai-nguyen/README | thu-vien-tai-nguyen/README, gotchas | 04/11 | sống |
| C20 | Nhận diện chung: sửa đúng một chỗ, chụp kiểm ngang + dọc; còn thiếu (vlog ngang, pow lề) | nhan-dien-chung §3–4 | nhan-dien-chung | 08/11 | sống |
| C21 | multi-clip: quy trình 1–10, bản đồ + liên kết, giữ/bỏ (Murch), khung vlog, hộp đồ nghề, danh-sach-cat.js, ảnh tĩnh, render, phát hành, dùng cho highlight | multi-clip | multi-clip | 03–08/11 | sống; con số mật độ (3–5 s, 15–20 s, 20–30 s) **cũ**; "nhạc 20 LU" **cũ**; cta "tự sáng tạo" **cũ**; "chép màu, font từ dự án cũ / mẫu" → chỉ ngoài chữ ký; ENDCARD nút phát **cũ** |
| C22 | multi-clip §3 teaser "TẬP NÀY CÓ GÌ?" + tiêu đề tên chương trình + outro lời mời theo dõi | multi-clip | multi-clip | 03–04/11 | → câu hỏi 3 |
| C23 | scene-design: bảng loại cảnh, chọn loại theo lời, chữ = trích, vùng an toàn chi tiết, card toàn cảnh, minh hoạ | scene-design | scene-design | 02–07/11 | sống; "hook bắt buộc", "cta tự sáng tạo", "tối giản / 60 % / 4–8 s / ≤ 15 s" **cũ** |
| C24 | style-analysis: đọc mẫu thành token; chọn font có tiếng Việt | style-analysis | style-analysis | 04/11 | sống; thêm giới hạn chữ ký (không đổi cam + 2 font) theo A2 |
| C25 | gotchas (dung-video-theo-phong-cach, podcast): lỗi đã gặp + cách tránh | gotchas | gotchas | 02–08/11 | sống (bỏ ngày, giữ bài học) |
| C26 | handoff: mẫu báo cáo | handoff | handoff | 04/11 | sống |
| C27 | podcast-design: sân khấu, lớp phủ, chọn cảnh, nhịp | podcast-design | podcast-design | 04/11 | sống; "tối giản ~1 cảnh / 15–20 s, ≤ 15 s" **cũ** → ~30 % |
| C28 | podcast-quay-nguoi: tài liệu cho sau này | podcast-quay-nguoi | podcast-quay-nguoi | 04/11 | sống (tài liệu, không phải luật hiện hành) |
| C29 | mau-ke-hoach-dang: mẫu đợt Đi trainer | khối 19 | mau-ke-hoach-dang | 06/11 | sống (mẫu, chỉ bỏ dấu ngày ngoài nội dung) |
| C30 | mau-so-lieu: mẫu | khối 16 | mau-so-lieu | 04/11 | sống |

### D. Đã tự phân xử theo ngày (không cần hỏi)
A8, A9, A15, A20, A23, A28, A48, A56, A60 (hashtag 2–3), B16, B21, B26, B32, B46, B49, B52, B54, B55, B58 (ghim theo kiểu dẫn dắt), C1 (không hỏi câu chốt), C5, C8 (tít ghim tắt mặc định), C11, C13, C16, C21–C27 phần cũ.

## Câu hỏi cho David (gửi một lần — trả lời gộp được)
1. **Motion graphics (Biên tập viên video):** "mọi video phải có motion graphics, trộn nhiều loại để mắt không quen" (07/11) đụng "hiểu hơn cầu kì: mỗi video vài kiểu" (10/11).
   ➡️ Đề xuất: viết thành một luật — *mọi video đều có điểm nhấn (dựng nhẹ vẫn có); chỉ dùng vài kiểu hợp nội dung nhất*; bỏ "trộn nhiều loại", bỏ ví dụ số "~3 illus + ~4 nhan". · Khác: giữ "trộn nhiều loại" song song.
2. **Highlight podcast dọc (mẫu "Đi trainer"):** khuôn 7B có "hình dày theo lời — mỗi cụm lời một biểu tượng ở đoạn không có cảnh".
   ➡️ Đề xuất: đổi thành *hình theo ý cần hiểu, không lấp từng cụm*; 3 clip Đi trainer vẫn là mẫu về khuôn (chữ chính, nhạc, màn chốt). · Khác: giữ dày như mẫu.
3. **Vlog ghép:** khuôn còn thẻ tiêu đề trên đoạn ghép mở đầu, teaser "TẬP NÀY CÓ GÌ?", kết "lời mời theo dõi" — đụng "không thẻ tít mặc định, chữ trên video nguyên văn".
   ➡️ Đề xuất: giữ đoạn ghép mở đầu; thẻ tiêu đề chỉ ghi tên chương trình / tên nơi (nhãn cố định) hoặc lời nguyên văn; bỏ "TẬP NÀY CÓ GÌ?" và lời mời tự viết. · Khác: giữ nguyên khuôn vlog như cũ.
4. **Học video mẫu — "Xong khi" số 2** còn ghi "màu, font, nét vẽ, chuyển động, nhạc kênh không đổi", trái với "thẩm mỹ chỉ giữ chữ ký".
   ➡️ Đề xuất: sửa thành *"chữ ký nhận diện (cam, hai font, thành phần cố định) không đổi"*. · Khác: giữ nguyên.
5. **Việc thật để chấm (bước 5):** ➡️ Đề xuất: làm một đoạn ~30–60 s trọn một ý từ `tap-5-nguyen-tac-tien` (video người nói ngang, đã có dự án) theo bản luật mới, chỉ render khi bạn đồng ý. · Khác: một clip highlight dọc.

## Trả lời của David
"Đồng ý cả 5" — áp đúng 5 đề xuất ở trên.

## Bước 3 — Đã viết lại
- Viết lại hẳn: `quy-tac-chung.md`, `nguyen-tac.md`, `nhan-dien-thuong-hieu.md`, `tong-quan.md`, `thu-vien-tai-nguyen/nhan-dien-chung.md`, khối 07, 08, 09, 10, 15.
- Sửa theo bảng (bỏ dấu ngày, "chuyển nguyên văn", luật cũ; áp bên thắng): khối README, 00, 01, 02, 03, 04, 05, 06, 12, 13, 14, 16, 17, 19;
  3 SKILL.md công thức + phan-tich-video-mau + phan-phoi-da-kenh; thiet-ke-bo-cuc/README; ho-so chung/lam-video/podcast/highlight/giong-van;
  references scene-design, multi-clip, style-analysis, gotchas (2 skill), podcast-design.
- Không đổi code. `bo.json`: `mau-ke-hoach-dang.md` chuyển sang kho (mẫu của một đợt đăng, không phải luật).
- Gộp nhà: 4 câu "video dọc ngắn" chỉ còn ở nhan-dien-chung; câu "bước nhẹ" của 4 SKILL trỏ về thoi-quen mục 3; quy-tac-chung §5, §9
  thành dòng trỏ (nhận diện → nhan-dien-chung, số liệu → khối 16); tong-quan bỏ phần chép lại luật.

## Bước 4 — Đóng sổ
Thêm "## Tái bản 1" vào đầu 3 changelog (dung-video-theo-phong-cach, cat-doan-noi-bat, dung-podcast). Cả 3 < 400 dòng, không cần lưu trữ.

## Bước 5 — Kiểm
- **Đủ luật:** soát bằng grep từng luật "sống" trong nhà mới (A1–A66, B8–B66, C8–C27): đủ.
- **Máy đo sau tái bản:** dấu ngày 165 → 3 (2 trong file mẫu đã chuyển kho, 1 là tên file nguồn học) · trùng 5 → 0 · dòng 3292 → 3236.
  "Câu ghi đè" 81 → 33, nhưng **cả 33 là chữ "thay" thường** ("chữ chính thay phụ đề", "nói thay lời"): regex `\bTHAY\b` trong
  `do-chong-cheo.py` chạy với `re.I` nên bắt mọi chữ "thay". Câu ghi đè thật = 0. Cần sửa máy đo (ngoài phạm vi tái bản bộ video).
- **Mẫu chuẩn:** `kiem-mau.py` 5/5 ✓ giữ nguyên (SSIM 0,982–0,990); node_modules nối tạm từ tap-5-nguyen-tac-tien rồi đã gỡ.
- **Việc thật:** David đồng ý → dựng `~/Movies/tap-thu-tai-ban-video-1/2-ban-day-du/video-hoan-chinh.mp4` (43,3 s, ngang) từ bản sạch
  `tap-5-nguyen-tac-tien` 4:10–4:56 theo bản luật mới: không thẻ tít, 3 kiểu (nhan · diagram tu-thanh ở đỉnh · cta nguyên văn), đường
  cảm xúc trong `ke-hoach-canh.md`. Soát cảnh P0/P1/P2 = 0; âm −14,2 LUFS, đỉnh −1,9 dB, rè +0,3 dB. **Chờ David chấm.**
  Gặp 2 lỗi code có sẵn (không do tái bản): (a) `xuat-video.mjs` dừng ở bước thẻ cuối trên Node 24 vì `man-ket.js → thanh.js` import
  `ho-so.json` không có `with {type: 'json'}` — đã render tạm thẻ cuối bằng script riêng trong dự án thử; (b) `chuan-am.py` tự chạy
  trong render_preview ra −14,8 LUFS, phải chạy lại lần 2 mới đạt.

## Bước 6 — Đóng mốc
Tag `tai-ban-video-1`, dòng trong `ky-nang/tai-cau-truc/lich-su.md`, đẩy GitHub. Ngưỡng `bo.json` giữ nguyên (sau khi sửa máy đo mới biết có lệch không).

## Đối chiếu "Xong khi"
1. Bảng đủ, mỗi dòng có nhà — **đạt**.
2. Máy đo "Chưa cần tái bản" — **đạt** sau khi sửa máy đo (`\bTHAY\b` chỉ bắt chữ in hoa): dấu ngày 1 · ghi đè 5 (đều là "thay cho" thường) · trùng 0 · dòng 3081.
3. Mẫu chuẩn y nguyên — **đạt**; việc thật — đã gửi, **chờ David chấm**.
4. Tag, lịch sử, GitHub — **đạt**.

## Bước tiếp
- David chấm đoạn thử; đạt thì đóng hẳn đợt này.
- ~~Sửa 2 lỗi code ở trên~~ — **xong 10/11**: `thanh.js` nạp json có `with {type: 'json'}` + `./khung-podcast.js`; `chuan-am.py` đo lại và bù tối đa 3 lượt từ bản trước khi chỉnh. Dự án thử: xuat-video.mjs chạy trọn, −14,2 LUFS ngay lần đầu; kiem-mau 5/5 ✓ (changelog dung-video-theo-phong-cach).
- Máy đo cũng báo bộ `nao` NÊN TÁI BẢN (dấu ngày 17/15) — việc của phiên khác.
