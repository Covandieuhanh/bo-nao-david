# Sổ thay đổi — dung-podcast (quyết định của người dùng + lý do)

## Tái bản 2 — 10/11/2026: bản luật viết lại từ bảng du-an/tai-cau-truc-2-video.md
- Nhà luật bỏ phóng xen kẽ ở mối cắt là quy-tac-chung mục 2 (kèm lý do); khối 02, ho-so-thuong-hieu/highlight.md, cat-highlight luật 8 trỏ về đó. quy-tac-chung mục 8 trỏ thói quen chung (hỏi, lệnh nền, mật khẩu, báo cáo), chỉ giữ phần riêng video. Bỏ câu chép ở gotchas, phan-phoi-da-kenh; sửa đường trỏ "hình của chính video" về khối 14. Viết lại 6 câu máy đo bắt nhầm ("thay cho", "THAY", tên file có ngày).

## Tái bản 1 — 10/11/2026: bản luật viết lại từ bảng du-an/tai-cau-truc-video-1.md
- Bỏ khỏi bản luật: `hook` đầu tiên, "~1 cảnh / 15–20 s", câu chốt tự sáng tạo (khối 12, podcast-design); hình phủ ~30 % là luật nhịp duy nhất. Phụ đề podcast dọc mọi độ dài = cụm 5–8 chữ (theo code phu-de.jsx).

## 2026-11-02
- Tạo skill: file tiếng / video podcast → video toàn motion graphics, cùng phong cách skill gốc, dùng chung template.
  Lựa chọn của người dùng: nhận cả file tiếng lẫn video; 1–2 người nói; tập tối đa ~15 phút.
- Khung xuất theo nguồn (ngang→ngang, dọc/chỉ tiếng→dọc) trừ khi người dùng yêu cầu.
- **Chỉ nội dung gốc**: bỏ đoạn thử ghép giọng đọc máy làm "người dẫn"; không tự đặt nhãn "Người dẫn/Khách mời"; tên người nói
  chỉ khi có trong lời hoặc người dùng đưa; không tên → chỉ màu sóng âm.
- **Khung ngang = thiết kế toàn khung 16:9**, không chia 3 cột kiểu pillar (bản đầu làm pillar, người dùng bác).
- **Thanh thời gian** ở đáy vùng an toàn (đã chạy · "còn m:ss"), luôn hiện trên mọi cảnh.
- Tên người nói ở khung ngang đặt dưới vòng micro (đặt dưới ý đang bàn thì bị thẻ đè).
- **Thu nhỏ** lớp phủ / cảnh / chữ ~10–15% và **chữ tiếng Việt đủ dấu, không chồng dòng** (`VN` trong khung-podcast.js) — người dùng
  thấy chữ to quá và dấu bị chồng/thiếu ("BỊ" → "BI").
- **Màn hình bìa** ~1 s ghép trước video (ảnh bìa mạng xã hội); tiêu đề hỏi người dùng mỗi video (DJI: "Phương pháp tìm ra năng
  lực của bản thân / dùng cho cả đời"). Ghép trước thay vì đè lên 1 s đầu → lời nói, hook, phụ đề không bị che hay lệch mốc.
- Sửa dấu tiếng Việt (`VN`) bật cho **cả hai skill** (người dùng đồng ý).
- Giữ ô chữ highlight (thẻ, chữ to) như skill gốc — người dùng không ưng bản chỉ-hình-động (thử trên video Haruku).
- Lớp phủ bị chặn cứng ở `PF.contentBottom` để không bao giờ đè phụ đề / thanh thời gian.
- **Tinh gọn**: ~1 cảnh / 15–20 s, ý đang bàn đổi 40–90 s, chữ to ≤ 3–4 lần (người dùng muốn tối giản, chỉ ý chính).
- Khe giữa 2 dòng chữ to (ý đang bàn, chữ to, bìa) nới 0,24 cỡ chữ — người dùng thấy "MỘT NGÀY / RẤT LÀ ĐẶC BIỆT" bị chồng dấu.
- **Không ảnh** là mặc định (biểu tượng vẽ); người dùng chọn bản DJI không ảnh. Ngoại lệ như skill gốc.
- **Mục tiêu video = hiểu + làm theo** (người dùng chốt): câu hành động trong lời → màn `action` tự sinh (biểu tượng + tick + nguyên
  văn câu); MỌI video kết bằng màn chốt `cta` ~4 s ("David rất mong có được sự góp ý của bạn tại phần bình luận!", keu-goi-hanh-dong.js) — hình
  lùi vào khung để vẫn thấy vẫy tay/like. Lý do: đánh giá cho thấy video giúp hiểu nhưng chưa thúc người xem hành động.
- **Câu màn chốt không cố định** (người dùng chốt): Claude tự sáng tạo câu chốt hợp từng video sau khi nắm nội dung — một hành động (bình luận/lưu/theo dõi/chia sẻ, biểu tượng theo kiểu), giọng David, không bịa; câu cố định trong keu-goi-hanh-dong.js chỉ còn là dự phòng.
- **Tick + "ting" ở màn chốt** (người dùng yêu cầu): câu chốt hiện xong → dấu tick nhỏ bật nảy ở góc biểu tượng + tiếng chuông ting (assets/sfx/ting.wav, tự tổng hợp, không bản quyền) để kích thích người xem hành động.

## 2026-11-04
- Bộ nhận diện David chung 4 loại video (xem san-xuat-video/tong-quan.md): đầu sân khấu thành dấu ● DAVID │ tên chương trình; tiếng
  ký hiệu ở đầu video; nhạc kênh rất nhỏ dưới lời (thấp hơn giọng 22 LU); thẻ cuối tên tập + DAVID; bản cuối −14 LUFS.

## 2026-11-04 — NGƯỜI XEM LÀ TRUNG TÂM (David: "các kênh lớn là hình mẫu thành công đã đạt được điều này rồi thì sao chép luôn")
Sau bản đánh giá đối chiếu với kênh lớn (thể loại nói trước camera, highlight, vlog, podcast), David duyệt kế hoạch 5 pha:
- `quy-tac-chung.md` (thư mục san-xuat-video) — một nguồn luật chung; SKILL.md chỉ giữ luật riêng. `so-lieu-mau.md` — vòng số liệu sau 7 ngày.
- **Phát hành** mọi video: 3 tiêu đề + 2 thumbnail 1280×720 (`scripts/anh-thu-nho.sh`, `assets/thumb-template/` — mặt có cảm xúc, ≤ 4
  chữ, nhận diện David; nguồn quay dọc tự thành khung một bên). Video ngắn không ghép bìa trước video.
- **Phụ đề video ngắn** 1–3 chữ to mỗi nhịp ngang ngực (`kieu-phu-de.js` `ShortLine`, chuẩn Hormozi/DOAC) — thay quyết định cũ "giữ
  phụ đề đáy" (bỏ đề xuất K ngày 03/11) vì David đổi kim chỉ nam. Video dài / vlog / podcast giữ hộp tối.
- **Bỏ bìa 1 s ghép trước video** (02/11) → giây đầu là `hook`; bước 2b hỏi chữ thumbnail + ảnh người nói thay tiêu đề bìa;
  thumbnail ở bước phát hành. Podcast dài giữ nhịp tự nhiên + phụ đề hộp tối.
- **Thumbnail chỉ khi video xuất NGANG và đăng YouTube** (David chốt cùng ngày: "chỉ có đăng video youtube thì mới cần ảnh bìa ngang, mà còn phải là video ngang"). Video xuất ngang → hỏi "có đăng YouTube không?" lúc đầu; video dọc chỉ có mốc khung bìa.

## 2026-11-04 (học 80 video Việt)
- Học 20 podcast Việt (David duyệt ưu tiên 1+2): thẻ "PHẦN n" theo TOPICS (san-khau.jsx), chương YouTube (`chuong.py`), teaser (`doan-gioi-thieu.py`), khuôn thumbnail series (`THUMB_BADGE`), nền ảnh chậm `STAGE.bg`, tập > 20 phút thưa cảnh. Chưa áp PO-6 (thẻ lịch phát) — chờ David.
- PO-6 áp (David duyệt): `STAGE.schedule` (lịch phát David đưa) hiện trên thẻ cuối + màn kết YouTube.

## 2026-11-04 — TÁI CẤU TRÚC (David: "tách nhỏ để sửa một chỗ")
- Kiến trúc 5 lớp: nguyen-tac · nhan-dien · ho-so (tham số từ hình mẫu, script + khung dựng đọc) · khoi (18 khối, nội dung SKILL.md cũ chuyển nguyên văn vào) · thu-vien-tai-nguyen (một bộ thành phần hình) + mau-chuan (kiem-mau.py). SKILL.md thành công thức mỏng (thứ tự khối, bảng phụ thuộc, tiêu chí đạt).
- 2 TRẠNG THÁI: cảnh `illus` (single/flow/vs/count/list, nhãn ≤ 3 chữ) ở cả 2 khung dựng; lớp chữ đè người tự vẽ toàn màn hình ≤ 4 s; thẻ/hành động bỏ câu trích dài; tít ghim tắt (hồ sơ highlight `tit_ghim: false`). +11 biểu tượng. Sao lưu trước tái cấu trúc: `~/.claude/skills/san-xuat-video.bak-2026-11-04b`.

## 2026-11-05
- **Học nhịp từ 50 video Hieu Nguyen** (David: học nhịp để chuyển đổi + cách trình bày đơn giản, giữ thẩm mỹ của mình; lời của David nói tự do — không khuôn thu âm). Áp: sơ đồ nói thay lời `diagram` (7 kiểu, có ảnh thật khung bo góc), ít mà sâu cho tập > 5 phút, bản đồ chương tích luỹ + tóm tắt trước màn chốt, thẻ tên tập + số tập, "TẬP n · ngày" ở dải đáy, màn chốt mặc định theo tuyến, mô tả có liên kết tài nguyên. Không áp: bỏ phụ đề in, tắt nhạc (David chỉ muốn học nhịp).
- Không dùng số tập (David 2026-11-05): STAGE.episode chỉ {date}; bỏ "TẬP n" ở thẻ mở, dải đáy, thumbnail.
- Không ghi bất kỳ thông tin phát hành nào lên video (số tập, ngày): bỏ STAGE.episode khỏi công thức (Timeline vẫn hỗ trợ nếu David yêu cầu sau).

## 2026-11-05 — Video dài không cắt gì
- David chốt: video dài (> 3 phút) là bản gốc, để nguyên cả khoảng lặng, tiếng ờ ừm, nói lại, đầu/cuối; cắt ghép chỉ khi trích video ngắn. Lý do: phong cách kể chuyện, giá trị của đoạn đắt nằm trong cả câu chuyện, chỗ kỹ thuật coi là lỗi lại là nét tự nhiên.
- Lằn ranh ở video dài đổi từ chặn cứng sang cảnh báo: phiếu lọc nêu mốc, lý do, rủi ro; David quyết từng video. Chữ đồ hoạ, tiêu đề, thumbnail, mô tả, clip ngắn vẫn không lấy nội dung chạm lằn ranh.
- Đã sửa: quy-tac-chung 2, khối 00, khối 02, tao-podcast.sh (tham số `cat-thua`, chỉ cho highlight), de-xuat-lam-sach.py (video > 3 phút mọi cut `ok: false`). Ca đầu áp dụng: podcast-dji-20261105.
