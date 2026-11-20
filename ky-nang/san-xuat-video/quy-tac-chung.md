---
description: "Luật chung bộ skill dựng video (một nguồn cho cả 3 skill), đọc trước mọi skill video."
---

# Luật chung — bộ skill dựng video của David (một nguồn cho cả 3 skill, 4 loại video)

Đọc file này trước mọi skill dựng video. Mỗi SKILL.md chỉ ghi luật RIÊNG của nó; trùng ý thì file này thắng, trừ khi SKILL.md
ghi rõ là ngoại lệ. Thói quen làm việc chung (hỏi, chạy lệnh, cuối việc) ở `../chuan-muc-lam-viec.md`. Lý do từng luật: sổ
`<skill>/references/nhat-ky-thay-doi.md`.

## 0. Kim chỉ nam
- **Người xem là trung tâm.** Học kênh lớn (DOAC, Hormozi, MrBeast, Ali Abdaal, Jay Shetty, Mel Robbins…) ở **nhịp và cách trình bày**
  giữ người xem. Mục tiêu mỗi video: người xem **ở lại → HIỂU ý chính → LÀM theo**; đo lại bằng số thật (khối 16).
- **Thẩm mỹ chỉ giữ chữ ký nhận diện** (`thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0): xem video nào cũng nhận ra cùng một người làm.
  Ngoài chữ ký là sáng tạo tự do theo nội dung; học được gì từ mẫu cũng dùng được, và học chỉ thêm vào kho, không thay cái đã có
  (`thiet-ke-bo-cuc/README.md` mục 4).
- **Mọi lựa chọn tự setup theo nội dung nguồn** (David chốt 19/11/2026: *"mọi thứ cần phát huy tối đa được sức mạnh của AI, mọi lựa
  chọn đều phải được tự động setup phù hợp với nội dung của tài nguyên nguồn"*): khuôn, bố cục, lớp thông tin, kiểu cảnh, thẩm mỹ,
  nhạc, khung đều do Claude chọn theo dấu hiệu của chính tài nguyên (`thiet-ke-bo-cuc/tu-chon.md`), không chép từ tập trước, không chờ
  David chỉ. Máy chặn render khi chưa chẩn đoán (`soat-canh.mjs`).
- **Hiểu hơn cầu kì.** Kho học được là để chọn cho hợp từng loại nội dung, không nhét hết vào một video. Mỗi video chỉ dùng vài kiểu
  hợp nhất, tự cân; hiệu ứng nào không giúp người xem hiểu nhanh hơn thì bỏ. Rối hay lỗi hình → bớt, không thêm.
  Ý nào cần hình và năm nguyên lý cho hình dễ hiểu: `thiet-ke-bo-cuc/tu-chon.md` bước 4a.

## 1. Nội dung
- **Không bịa.** Phụ đề, chữ to, thẻ, màn hành động, màn chốt = **trích / bỏ bớt lời người nói**, không diễn đạt lại. Tên riêng, con
  số, vế đối lập, từ phủ định giữ nguyên. Tên chưa chắc chính tả → khối 01.
- **Chữ trên video là nguyên văn lời David.** Motion graphics loại nào cũng được nhưng không sáng tạo sai lời. Chữ = cụm nguyên văn
  liền mạch, được tách mảnh, không bỏ chữ làm đổi nghĩa ("không **muốn** làm một mình"). Không số chạy hiện số David không nói.
- **Câu Claude tự viết chỉ ở bài đăng**: tiêu đề, thumbnail, mô tả, bình luận ghim — viết đúng ý người nói, không thêm thông tin hay
  lời hứa ngoài video, không giật tít sai sự thật.
- **Nhãn cố định của khung** (không phải lời): "Bản đầy đủ trên kênh …" ở thẻ cuối dẫn bản đầy đủ, và **lịch phát do David đưa**
  ("Tập mới mỗi thứ 6") — `project.schedule` (1 video), `STAGE.schedule` (podcast), ke-hoach.json `"schedule"` (vlog),
  `"endcard": {"schedule"}` (highlight). Không tự đặt lịch.
- **Lằn ranh kênh trainer** (kênh khác theo hồ sơ kênh đó; loại khỏi mọi chữ/clip): đọc số của người thật khi họ chưa đồng ý, hứa tiền hay kết quả nhờ con số, nghi thức cầu xin / phóng sinh (còn nội dung từ trường số (kèm dẫn chứng thần số học, thiền, "nghiệp"…) thuộc hướng trainer, được nói công khai, `chien-luoc-nghe-nghiep.md` 4.7) · "chữa lành", công dụng sức khoẻ của sản phẩm ·
  tư vấn thuế/pháp lý · tên thật/nơi làm/chi tiết lộ danh tính khách, học viên, nhân viên · giá, tên gói dịch vụ. Câu chủ chốt dính
  lằn ranh → báo David, không tự sửa lời. Ở video dài: cảnh báo trong phiếu lọc và báo cáo, mặc định giữ lời, David quyết ở bản cuối (khối 00 mục 3).
- Whisper bịa câu ở đoạn không lời ("Hãy subscribe cho kênh…", "Cảm ơn các bạn đã xem") → bỏ.

## 2. Nhịp
- **Mở đầu 0–3 s** nói ngay video về cái gì / đang đặt cược gì, bằng lời thật của David. Thẻ tít mở đầu: khối 06.
- **Video dài (> 3 phút) không cắt gì**: podcast, tâm sự, thực tế, nói trước camera là BẢN GỐC, để nguyên cả khoảng lặng, "ờ/ừm",
  ngập ngừng, nói lại, đoạn dẫn dắt, phần đầu/cuối. Những chỗ kỹ thuật coi là lỗi là nét tự nhiên của người kể; giá trị của đoạn hay
  nằm trong cả câu chuyện dẫn tới nó. Không rút video dài thành đoạn hay.
  Riêng khi **tập chạm nhiều hướng nghề** (mỗi hướng một bản, khối 00 mục 0b) hoặc **David yêu cầu bỏ ý** cụ thể ("cắt ý X", "ý chưa
  trọn thì cắt"): bỏ trọn các đoạn ngoài hướng / nói ý đó, phần còn lại giữ theo thứ tự buổi nói và vẫn để nguyên trong từng đoạn
  (`dung-video-theo-phong-cach/references/nhieu-doan-video.md` mục 11).
  Riêng **làm lại video cũ**: cắt màn tít + lời chào / giới thiệu kênh cũ (tên kênh cũ, nghề cũ, kinh doanh) và chữ/viền kênh cũ in
  trong hình — chỉ đúng các đoạn đó (khối 02). Lằn ranh David chọn cắt thì chỉ cắt đúng đoạn đó.
- **Cắt chỉ cho video ≤ 3 phút và highlight**: lặng ≥ 0,45 s còn ~0,24 s + tiếng đệm "ờ/ừm" đứng riêng (cắt cứng); **không dùng hiệu ứng zoom vào / zoom ra trên hình quay** (video người nói, clip gốc) ở bất kỳ video nào
  (không thẩm mỹ) — ảnh minh hoạ trôi chậm (Ken Burns) và chuyển động bên trong motion graphic (đẩy khung) vẫn được; giữ 1 s lặng sau câu hỏi kêu gọi. Clip ngắn luôn trích từ bản gốc, ưu tiên kéo người xem về video dài trên YouTube; không
  về thì vẫn cần tương tác / nhắn tin trên Facebook, TikTok. **Vlog ghép** giữ nhịp tự nhiên.
- Video ngắn đổi gì đó mỗi 1–3 s (nhịp chữ phụ đề, chữ to, cảnh, cắt), không để 5–8 s trôi qua không đổi gì. Video dài thưa, nhịp
  từ nội dung.
- Một màn = một ý, một hình, một câu. Không chồng 2 lớp phủ.
- **Đường cảm xúc + một đỉnh** (mọi loại video): trước khi lên cảnh, viết cảm xúc từng đoạn (cảm xúc → cái gì trên màn hình gây ra
  nó) và chọn **một** đỉnh. Đỉnh nhận motion graphic lớn nhất; đoạn ngay trước đỉnh để ít hình (phụ đề vẫn chạy). Video dài vẫn không
  cắt: đường cảm xúc chỉ để đặt motion graphic. Vlog ghép: hai đoạn liền nhau cùng cảm xúc thì bỏ hoặc đổi một. Highlight vẫn chọn
  theo 4 câu (khối 13). Cách làm: khối 07; kiểm cảm nhận: khối 17.

## 3. Phụ đề (một nguồn: `thu-vien-tai-nguyen/kieu-phu-de.js`; cách làm: khối 03)
- **Video ngắn** — highlight, podcast dọc (mọi độ dài), video 1 người dọc ≤ 90 s: mỗi lần hiện **một cụm trọn ý ~5–8 chữ** (tối đa
  2 dòng), **cỡ bằng chữ trong thẻ motion graphic** (`ngan_co` 58), chữ thường, viền đen mảnh, không hộp nền, từ khoá cam, ngay trên
  thanh thời gian (`ShortLine`). Tự bật; ép tay `project.short = true|false` (1 video) hoặc `SHORT` trong danh-sach-cat.js (ghép).
- **Video dài, vlog, podcast ngang**: hộp tối, đầy đủ câu, đáy vùng an toàn (`SUB`).
- **Podcast đồ hoạ dọc trích ngắn**: không dải phụ đề; cả câu đang nói hiện to giữa khung làm đồ hoạ (`chu_chinh`).
- **Mỗi lúc một chỗ chữ** (mọi loại, mọi khung): lớp motion graphic có chữ (chữ to, thẻ, nhãn, ô liệt kê, sơ đồ, màn hành động, thẻ
  tít, màn chốt) đang hiện thì **phụ đề nhường**; hết lớp đó phụ đề hiện tiếp đúng cụm đang nói. Không tính dấu góc, tít ghim, thanh
  thời gian. Cảnh không có chữ: `props.giuPhuDe = true` để giữ phụ đề. Vì người xem không đọc được hai chỗ cùng lúc.
- **Màu theo nghĩa**: trong `hl`, mục bắt đầu `+` = nên làm (xanh lá), `-` = tránh (đỏ), còn lại cam — chỉ khi lời có cặp nên/tránh.
- Luôn đầy đủ, đúng từng chữ. Không đốt phụ đề bằng ffmpeg (không có libass).

## 4. Hình
- **Mọi video đều có điểm nhấn** (motion graphics hiểu rộng: thứ kéo mắt người xem vào ý đang nói) — "dựng nhẹ" vẫn có. Có nhiều
  loại: hình vẽ, chữ nhấn cụm đắt, làm nổi người đang nói (`nhan`), sơ đồ, cảnh toàn màn hình. Mỗi video chỉ dùng vài kiểu hợp nội
  dung nhất (mục 0). Cách chọn: khối 07.
- **Bố cục tự cân**: không con số bắt buộc về độ dài cảnh, tỷ lệ mặt / đồ hoạ, số cảnh; chọn từ `thiet-ke-bo-cuc/bo-cuc.md` theo 4 câu hỏi
  ở `thiet-ke-bo-cuc/README.md` mục 2. Ngang tự do; dọc mỗi lúc ít thứ.
- **Tự chọn trước kế hoạch cảnh** (cả 3 skill dựng): chẩn đoán rồi chọn bố cục nền, lớp thông tin, kiểu cảnh theo
  `thiet-ke-bo-cuc/tu-chon.md` (`chan-doan.py`); ghi "đã chọn X vì Y" vào `ke-hoach-canh.md`.
- **Không che người nói, không đè phụ đề** (chặn cứng ở mọi template). Khung có nhiều người: graphic không đè hay làm mờ bất kỳ ai;
  khung cắt, chuyển cảnh, ô thu nhỏ bám đúng người đang nói. Thu người vào ô bo góc không tính là che. Che mặt / thân trên → tự toàn màn
  hình: khối 05.
- Chữ tiếng Việt đủ dấu, không chồng dòng (`VN`, chừa 0,5 em trên / 0,32 em dưới).
- **Nhiều ảnh thật minh hoạ**: mỗi khi lời nhắc một nơi, người, vật, việc cụ thể thì ưu tiên ảnh thật, biểu tượng vẽ
  cho ý trừu tượng. **Ảnh chỉ được chụp tại Việt Nam, liên quan người Việt Nam** (đọc mô tả / danh mục ảnh để chắc; tìm kèm
  "Vietnam" / tên tiếng Việt). Không có ảnh Việt Nam hợp giấy phép → biểu tượng vẽ, không dùng ảnh nước ngoài. Nguồn ghi `nguon-anh.txt`.
  Số liệu luôn bằng hiệu ứng, đúng con số người nói. Kết quả/con số mà clip gốc có bằng chứng thật (ảnh giá, hoá đơn) → ưu tiên chiếu.
- Không ghi chú kỹ thuật trên video (×1,6, slow-mo…). Không màn nguồn ảnh cuối video → `nguon-anh.txt`.
- Khung xuất = khung gốc trừ khi David yêu cầu (highlight mặc định dọc 9:16, ngang khi David yêu cầu).

## 5. Bộ nhận diện
Một nguồn: `thu-vien-tai-nguyen/nhan-dien-chung.md` — chữ ký nhận diện, vị trí và luật của thành phần cố định (vùng an toàn, dấu góc, thanh
thời gian, phụ đề, màn chốt, thẻ cuối, màn kết YouTube), video dọc ngắn. Âm thanh nhận diện (tiếng ký hiệu, nhạc kênh, mức âm lượng):
khối 09. Sửa nhận diện → giữ đồng bộ cả 4 loại.

## 6. Lời kêu gọi
- Ưu tiên **câu mệnh lệnh nằm sẵn trong lời** ("Hãy chọn…", "thử làm…") — top video gần như không có câu "hãy bình luận".
- Màn hành động (`action`) đúng lúc người nói giao một việc làm được; 1–2 lần / video.
- Màn chốt ~4 s cuối mọi video, câu = nguyên văn lời người nói (khối 08). Câu mời bình luận / "gỡ" theo luật kênh nằm ở mô tả + bình
  luận ghim, chỉ lên video khi David tự nói trong video.

## 7. Phát hành (bước cuối của MỌI skill — chuẩn MrBeast / Paddy Galloway; cách làm: khối 15)
Ghi `<dự án>/phat-hanh/phat-hanh.md`:
- **3 tiêu đề** (≤ 60 ký tự, một ý, gây tò mò nhưng đúng ý video) xếp theo độ mạnh; tiêu đề và thumbnail **bổ sung**, không lặp chữ.
- **Thumbnail** chỉ khi video xuất ngang VÀ đăng YouTube; luật và mẫu ở khối 14. **Video dọc**: không ghép bìa trước video (giây đầu
  dành cho câu mở); ghi **mốc khung bìa đề xuất** (giây) để David chọn khi đăng.
- **Video > 3 phút đăng YouTube** ("có đăng YouTube không?" là điểm cần chốt trong 4 phần lúc đầu, với mọi video > 3 phút, ngang hay dọc):
  - **Màn kết YouTube 15–20 s**: 1 video/podcast `project.ytEnd = 20` (ghi sau bước làm sạch — clean_apply viết lại du-an.js);
    vlog ghép `"ytEnd": 20` trong ke-hoach.json. Ghi vào phat-hanh.md: "gắn màn kết trong YouTube Studio: 2 video (trái/phải hoặc
    trên/dưới) + nút đăng ký (tròn giữa dưới)".
  - **Chương YouTube**: `python3 -I dung-video-theo-phong-cach/scripts/chuong.py <dự án>` → `phat-hanh/chuong.txt` dán vào mô tả.
  - **Teaser 15–25 s** cho video > 10 phút (podcast, nói trước camera, vlog nói chuyện): sau render, chọn 2–3 câu đắt nhất (trọn câu,
    nguyên văn) → `python3 -I dung-video-theo-phong-cach/scripts/doan-gioi-thieu.py <dự án> <từ-đến> …` (chạy TRƯỚC chuong.py).
- Mô tả bài đăng + bình luận ghim theo luật kênh (khối 15), hashtag theo `ho-so-thuong-hieu/giong-thuong-hieu-david.md`.
- Gửi David: video + thumbnail (SendUserFile) + tiêu đề.

## 8. Quy trình chung
- Hỏi, chạy một mạch, lệnh nền, báo cáo cuối: `../chuan-muc-lam-viec.md` mục 2–4; mật khẩu: `AGENTS.md` luật 5. Riêng video: duyệt 4 phần ở đầu việc, sau đó không có điểm dừng duyệt
  giữa chừng (kể cả kế hoạch ghép vlog); báo cáo cuối thêm "đã chọn X vì Y" và tên riêng cần xác nhận.
- Không tải video từ YouTube/TikTok để dựng (nhờ David gửi file); tải để học mẫu: `thiet-ke-bo-cuc/README.md` mục 4.
- Chụp thử (stills) trước khi render để Claude tự soát, không gửi David chốt; kiểm bản cuối theo khối 17 + 09. **Chụp có giới hạn:** chụp đúng mốc dễ lỗi (khung mới lần
  đầu, chỗ chồng lớp, mối cắt, màn chốt, thẻ cuối, chỗ David góp ý), không chụp từng cảnh; xem bố cục thì dùng ảnh thu nhỏ.
- **Góp ý → sửa rồi render lại toàn bộ luôn**, không chờ chữ "render"; giao lại như lần đầu (Drive + trang xem
  kết quả). Render nối tiếp, không song song. Không cổng duyệt nào trước khi xong; chỉ việc đăng mạng xã hội chờ David nói "đăng".
- **Phần cứng không hỏi, không đổi** (`../chuan-muc-lam-viec.md` mục 2): nhận diện, dấu góc, màn chốt, thẻ cuối, nhạc theo tuyến, mức
  motion graphics, phụ đề, chuẩn âm lượng, nơi giao file; tên riêng chưa chắc → dùng cách Whisper nghe và nêu ở báo cáo.
- **Thử skill bằng đoạn ngắn trọn một ý:** cắt từ đầu tới cuối một ý của video nguồn (không cố định số giây, không chạy cả video dài)
  vào thư mục thử riêng `tap-thu-…`, chạy theo skill, cho David xem bản cuối, xong thì dọn. Đoạn ngắn trọn ý ra tốt thì video dài cũng tốt.
- **Dựng ngay trong phiên Claude** theo skill (`phan-phoi-da-kenh` → skill dựng). Không đề xuất dựng app hay công cụ tự động dựng video
  trừ khi David yêu cầu, vì chạy app tốn token hơn.
- Video đã chốt hoặc đã đăng: dọn file tạm rồi đưa tập lên Drive, xoá trên Mac theo khối 17 (`don-tap.py --xoa` → `luu-drive.sh`, không hỏi lại; chỉ hỏi phần ⏸ đang dở). Mac chỉ giữ việc đang làm: ghi nhớ `video-chuyen-qua-drive`.
