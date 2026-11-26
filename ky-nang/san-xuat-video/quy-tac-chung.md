---
description: "Luật chung của bộ skill dựng video (một nguồn cho cả 3 skill), đọc trước mọi skill video."
---

# Luật chung — bộ skill dựng video của David (một nguồn cho cả 3 skill, 4 loại video)

Người dựng đọc file này trước khi dùng mọi skill dựng video. Mỗi SKILL.md chỉ ghi luật RIÊNG của skill đó; khi trùng ý thì file này được ưu tiên, trừ khi SKILL.md
ghi rõ là ngoại lệ. Thói quen làm việc chung (hỏi, chạy lệnh, cuối việc) nằm ở `../chuan-muc-lam-viec.md`. Lý do của từng luật: sổ
`<skill>/references/nhat-ky-thay-doi.md`.

## 0. Kim chỉ nam
- **Người xem là trung tâm.** Người dựng học các kênh lớn (DOAC, Hormozi, MrBeast, Ali Abdaal, Jay Shetty, Mel Robbins…) về **nhịp và cách trình bày**
  giữ chân người xem. Mục tiêu mỗi video: người xem **ở lại → HIỂU ý chính → LÀM theo**; đo lại bằng số liệu thực tế (khối 16).
- **Thẩm mỹ chỉ giữ chữ ký nhận diện** (`thu-vien-tai-nguyen/nhan-dien-chung.md` mục 0): người xem xem video nào cũng nhận ra cùng một người làm.
  Ngoài chữ ký nhận diện là phần sáng tạo tự do theo nội dung; học được gì từ mẫu cũng dùng được, và điều học được chỉ bổ sung vào kho, không thay thế cái đã có
  (`thiet-ke-bo-cuc/README.md` mục 4).
- **Mọi lựa chọn được tự thiết lập theo nội dung nguồn**, để phát huy tối đa sức mạnh của AI: mẫu, bố cục, lớp thông tin, kiểu cảnh, thẩm mỹ,
  nhạc, khung đều do người dựng (AI nào cũng vậy) lập luận từ chính tài nguyên (`thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md` → `huong-dan-lua-chon.md`), không sao chép từ tập trước, không chờ
  David chỉ định. Công cụ kiểm tra chặn render khi chưa chẩn đoán (`soat-canh.mjs`).
- **Tận dụng tối đa kho đã học, tự do.** Mọi hiệu ứng, motion graphic, chuyển cảnh (kể cả 3D) đã học hoặc tự viết đều dùng được ở
  mọi video, không chờ nội dung "đúng loại" — nội dung kênh chủ yếu là cung cấp thông tin và trò chuyện, nếu chờ thì không bao giờ dùng tới.
  Đa dạng nghĩa là **đổi hiệu ứng qua các cảnh** để gây ấn tượng, không phải chồng nhiều thành phần trong một khung hình: mỗi thời điểm một điểm nhìn,
  gọn gàng, rối thì giảm bớt. Không có kiểu nào bắt buộc phải dùng hay cấm dùng, trừ việc che nội dung chính (mục 4).
  Mỗi lần chọn hình, người dựng phải mở **kho hình mẫu** (8 kênh hình mẫu + các phiếu học motion graphics) làm danh mục lựa chọn và chọn cách phù hợp ý nhất,
  ghi nguồn từng cảnh (`thiet-ke-bo-cuc/huong-dan-lua-chon.md` bước 4d) — học mà không mở ra dùng là lãng phí.
  Ý nào cần hình và mỗi hình phải đạt gì: `thiet-ke-bo-cuc/huong-dan-lua-chon.md` bước 4a–4b (nguyên lý: `nhu-cau-nguoi-xem.md`).

## 1. Nội dung
- **Không bịa đặt.** Phụ đề, chữ to, thẻ, màn hành động, màn chốt phải là **trích hoặc bỏ bớt lời người nói**, không diễn đạt lại. Tên riêng, con
  số, vế đối lập, từ phủ định giữ nguyên. Tên chưa chắc chính tả thì xử lý theo khối 01.
- **Chữ trên video là nguyên văn lời David.** Motion graphics loại nào cũng được nhưng không sáng tạo sai lời. Chữ là cụm nguyên văn
  liền mạch, được tách mảnh, không bỏ chữ làm đổi nghĩa ("không **muốn** làm một mình"). Hiệu ứng số chạy không hiện số David không nói.
- **Câu Claude tự viết chỉ ở bài đăng**: tiêu đề, thumbnail, mô tả, bình luận ghim — viết đúng ý người nói, không thêm thông tin hay
  lời hứa ngoài video, không đặt tiêu đề câu khách sai sự thật.
- **Nhãn cố định của khung** (không phải lời): "Bản đầy đủ trên kênh …" ở thẻ cuối dẫn về bản đầy đủ, và **lịch phát hành do David cung cấp**
  ("Tập mới mỗi thứ 6") — `project.schedule` (1 video), `STAGE.schedule` (podcast), ke-hoach.json `"schedule"` (vlog),
  `"endcard": {"schedule"}` (highlight). Claude không tự đặt lịch.
- **Lằn ranh** (danh sách theo từng hướng: khối 00 mục 3; gốc `chien-luoc-nghe-nghiep.md` 4.7): loại khỏi mọi chữ / clip. Câu chủ chốt liên quan tới
  lằn ranh thì báo David, không tự sửa lời. Ở video dài: cảnh báo trong phiếu lọc và báo cáo, mặc định giữ lời, David quyết định ở bản cuối (khối 00 mục 3).
- Câu do Whisper bịa đặt ở đoạn không có lời ("Hãy subscribe cho kênh…", "Cảm ơn các bạn đã xem") thì bỏ.

## 2. Nhịp
- **Mở đầu 0–3 s** nói ngay video nói về điều gì / đang đặt cược gì, bằng lời thật của David. Thẻ tiêu đề mở đầu: khối 06.
- **Video dài (trên 3 phút) không cắt gì**: podcast, tâm sự, thực tế, nói trước camera là BẢN GỐC, để nguyên cả khoảng lặng, "ờ/ừm",
  ngập ngừng, nói lại, đoạn dẫn dắt, phần đầu/cuối. Những chỗ góc nhìn kỹ thuật coi là lỗi lại là nét tự nhiên của người kể; giá trị của đoạn hay
  nằm trong cả câu chuyện dẫn tới đoạn đó. Không rút gọn video dài thành các đoạn hay.
  Riêng khi **tập liên quan tới nhiều hướng nghề** (mỗi hướng một bản, khối 00 mục 0b) hoặc **David yêu cầu bỏ ý** cụ thể ("cắt ý X", "ý chưa
  trọn thì cắt"): bỏ trọn các đoạn ngoài hướng hoặc các đoạn nói ý đó, phần còn lại giữ theo thứ tự buổi nói và vẫn để nguyên trong từng đoạn
  (`dung-video-theo-phong-cach/references/nhieu-doan-video.md` mục 11).
  Riêng khi **làm lại video cũ**: cắt màn tiêu đề và lời chào hoặc lời giới thiệu kênh cũ (tên kênh cũ, nghề cũ, kinh doanh) và chữ, viền kênh cũ in
  trong hình — chỉ đúng các đoạn đó (khối 02). Phần lằn ranh David chọn cắt thì chỉ cắt đúng đoạn đó.
- **Chỉ cắt với video tối đa 3 phút và highlight**: khoảng lặng ít nhất 0,45 s thì rút còn khoảng 0,24 s, và cắt tiếng đệm "ờ/ừm" đứng riêng (cắt cứng); **không dùng hiệu ứng zoom vào / zoom ra trên hình quay** (video người nói, clip gốc) ở bất kỳ video nào
  (không thẩm mỹ) — ảnh minh hoạ trôi chậm (Ken Burns) và chuyển động bên trong motion graphic (đẩy khung) vẫn được dùng; giữ 1 s lặng sau câu hỏi kêu gọi. Clip ngắn luôn trích từ bản gốc, ưu tiên dẫn người xem về video dài trên YouTube; người xem không
  chuyển sang thì clip vẫn cần tạo tương tác / tin nhắn trên Facebook, TikTok. **Vlog ghép** giữ nhịp tự nhiên.
- Video ngắn thay đổi một yếu tố mỗi 1–3 s (nhịp chữ phụ đề, chữ to, cảnh, cắt), không để 5–8 s trôi qua mà không có thay đổi. Video dài nhịp thưa hơn, nhịp
  xuất phát từ nội dung.
- Mỗi màn gồm một ý, một hình, một câu. Không chồng 2 lớp phủ.
- **Đường cảm xúc và một đỉnh** (mọi loại video): trước khi lên cảnh, viết cảm xúc từng đoạn (với mỗi cảm xúc, ghi yếu tố nào trên màn hình gây ra
  cảm xúc đó) và chọn **một** đỉnh. Đỉnh nhận motion graphic lớn nhất; đoạn ngay trước đỉnh để ít hình (phụ đề vẫn chạy). Video dài vẫn không
  cắt: đường cảm xúc chỉ dùng để đặt motion graphic. Vlog ghép: hai đoạn liền nhau cùng cảm xúc thì bỏ hoặc đổi một đoạn. Highlight vẫn chọn
  theo 4 câu (khối 13). Cách làm: khối 07; kiểm cảm nhận: khối 17.

## 3. Phụ đề (một nguồn: `thu-vien-tai-nguyen/kieu-phu-de.js`; cách làm: khối 03)
- **Video ngắn** — highlight, podcast dọc (mọi độ dài), video 1 người dọc tối đa 90 s: mỗi lần hiện **một cụm trọn ý khoảng 5–8 chữ** (tối đa
  2 dòng), **cỡ bằng chữ trong thẻ motion graphic** (`ngan_co` 58), chữ thường, viền đen mảnh, không hộp nền, từ khoá màu cam, ngay trên
  thanh thời gian (`ShortLine`). Chế độ này tự bật; chỉ định thủ công `project.short = true|false` (1 video) hoặc `SHORT` trong danh-sach-cat.js (ghép).
- **Video dài, vlog, podcast ngang**: hộp tối, đầy đủ câu, ở đáy vùng an toàn (`SUB`).
- **Podcast đồ hoạ dọc trích ngắn**: không có dải phụ đề; cả câu đang nói hiện to giữa khung làm đồ hoạ (`chu_chinh`).
- **Mỗi thời điểm một vị trí chữ** (mọi loại, mọi khung): lớp motion graphic có chữ (chữ to, thẻ, nhãn, ô liệt kê, sơ đồ, màn hành động, thẻ
  tiêu đề, màn chốt) đang hiện thì **phụ đề nhường**; hết lớp đó thì phụ đề hiện tiếp đúng cụm đang nói. Không tính dấu góc, tiêu đề ghim, thanh
  thời gian. Cảnh không có chữ: `props.giuPhuDe = true` để giữ phụ đề. Lý do: người xem không đọc được hai vị trí cùng lúc.
- **Màu theo nghĩa**: trong `hl`, mục bắt đầu bằng `+` là nên làm (xanh lá), `-` là tránh (đỏ), còn lại màu cam — chỉ khi lời có cặp nên/tránh.
- Phụ đề luôn đầy đủ, đúng từng chữ. Không gắn cố định phụ đề vào hình (burn-in) bằng ffmpeg (không có libass).

## 4. Hình
- **Mọi video đều có điểm nhấn** (motion graphics hiểu theo nghĩa rộng: yếu tố thu hút ánh nhìn người xem vào ý đang nói) — "dựng nhẹ" vẫn có. Có nhiều
  loại: hình vẽ, chữ nhấn cụm then chốt, làm nổi người đang nói (`nhan`), sơ đồ, thẻ lật 3D, đường vẽ tiếp, cảnh toàn màn hình. Thay đổi kiểu
  và chuyển cảnh qua các cảnh, giữ gọn (mục 0). Cách chọn: khối 07.
- **Bố cục tự cân đối** theo thước đo ở `thiet-ke-bo-cuc/README.md` mục 2, chọn từ `thiet-ke-bo-cuc/bo-cuc.md`.
- **Tự chọn trước kế hoạch cảnh** (cả 3 skill dựng): yêu cầu người dùng → chẩn đoán → loại nội dung → bố cục nền, lớp thông tin → mỗi cảnh
  "Cần · Vì · Làm" theo `thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md` + `huong-dan-lua-chon.md` (`chan-doan.py`); ghi vào `ke-hoach-canh.md`.
- **Không che nội dung chính, không chồng lên phụ đề** — đây là điều duy nhất phải giữ, còn motion graphic được tuỳ biến tự do. Nội dung chính là
  **người đang nói / những người đang trao đổi** và **thứ đang được nói tới** (màn hình sản phẩm, vật, tài liệu). Hình đặt vào khoảng trống
  thực tế của khung hình (trần, cửa kính, tường, khoảng trên đầu — xét ảnh đầu / giữa / cuối cảnh). Cảnh toàn khung, nền làm mờ chỉ dùng ở đoạn không
  có nội dung chính cần thấy. Khung nhiều người thì mọi người luôn hiện, không thu riêng một người vào ô — người xem cần thấy đang nói
  với ai; khung một người thì thu vào ô bo góc không tính là che. Cách tránh: khối 05. Công cụ kiểm tra chặn các trường hợp đo được.
- Chữ tiếng Việt đủ dấu, không chồng dòng (`VN`, chừa 0,5 em trên / 0,32 em dưới).
- **Nhiều ảnh thật minh hoạ**: mỗi khi lời nhắc tới một nơi, người, vật, việc cụ thể thì ưu tiên ảnh thật, dùng biểu tượng vẽ
  cho ý trừu tượng. **Ảnh chỉ được chụp tại Việt Nam, liên quan người Việt Nam** (đọc mô tả / danh mục ảnh để chắc chắn; tìm kèm
  "Vietnam" / tên tiếng Việt). Không có ảnh Việt Nam hợp giấy phép thì dùng biểu tượng vẽ, không dùng ảnh nước ngoài. Nguồn ghi vào `nguon-anh.txt`.
  Số liệu luôn thể hiện bằng hiệu ứng, đúng con số người nói. Kết quả, con số mà clip gốc có bằng chứng thật (ảnh giá, hoá đơn) thì ưu tiên trình chiếu.
- Không ghi chú kỹ thuật trên video (×1,6, slow-mo…). Không đặt màn nguồn ảnh ở cuối video; nguồn ghi vào `nguon-anh.txt`.
- Khung xuất giống khung gốc trừ khi David yêu cầu khác (highlight mặc định dọc 9:16, ngang khi David yêu cầu).

## 5. Bộ nhận diện
Một nguồn: `thu-vien-tai-nguyen/nhan-dien-chung.md` — chữ ký nhận diện, vị trí và luật của thành phần cố định (vùng an toàn, dấu góc, thanh
thời gian, phụ đề, màn chốt, thẻ cuối, màn kết YouTube), video dọc ngắn. Âm thanh nhận diện (tiếng ký hiệu, nhạc kênh, mức âm lượng):
khối 09. Khi sửa nhận diện thì giữ đồng bộ cả 4 loại.

## 6. Lời kêu gọi
- Ưu tiên **câu mệnh lệnh nằm sẵn trong lời** ("Hãy chọn…", "thử làm…") — các video dẫn đầu gần như không có câu "hãy bình luận".
- Màn hành động (`action`) xuất hiện đúng lúc người nói giao một việc làm được; 1–2 lần / video.
- Màn chốt nằm ở khoảng 4 s cuối mọi video, câu là nguyên văn lời người nói (khối 08). Câu mời bình luận / "gỡ" theo luật kênh nằm ở mô tả và bình
  luận ghim, chỉ đưa lên video khi David tự nói trong video.

## 7. Phát hành (bước cuối của MỌI skill — chuẩn MrBeast / Paddy Galloway; cách làm: khối 15)
Ghi `<dự án>/phat-hanh/phat-hanh.md`:
- **3 tiêu đề** (tối đa 60 ký tự, một ý, gây tò mò nhưng đúng ý video) xếp theo độ mạnh; tiêu đề và thumbnail **bổ sung** cho nhau, không lặp chữ.
- **Thumbnail** chỉ làm khi video xuất ngang VÀ đăng YouTube; luật và mẫu ở khối 14. **Video dọc**: không ghép bìa trước video (giây đầu
  dành cho câu mở); ghi **mốc khung bìa đề xuất** (giây) để David chọn khi đăng.
- **Video trên 3 phút đăng YouTube** (với mọi video trên 3 phút, ngang hay dọc, Claude tự quyết theo hướng nội dung và `ho-so-thuong-hieu/kenh.json`, ghi trong báo cáo):
  - **Màn kết YouTube 15–20 s**: 1 video/podcast `project.ytEnd = 20` (ghi sau bước làm sạch — ap-dung-lam-sach.py viết lại du-an.js);
    vlog ghép `"ytEnd": 20` trong ke-hoach.json. Ghi vào phat-hanh.md: "gắn màn kết trong YouTube Studio: 2 video (trái/phải hoặc
    trên/dưới) + nút đăng ký (tròn giữa dưới)".
  - **Chương YouTube**: `python3 -I dung-video-theo-phong-cach/scripts/chuong.py <dự án>` → `phat-hanh/chuong.txt` dán vào mô tả.
  - **Teaser** (câu then chốt, trọn câu, nguyên văn; số câu và độ dài do Claude tự chọn theo nội dung) khi video đủ dài để người xem cần một lời mời xem tiếp (podcast, nói trước camera, vlog nói chuyện): sau render, chọn các câu then chốt (trọn câu,
    nguyên văn) → `python3 -I dung-video-theo-phong-cach/scripts/doan-gioi-thieu.py <dự án> <từ-đến> …` (chạy TRƯỚC chuong.py).
- Mô tả bài đăng và bình luận ghim theo luật kênh (khối 15), hashtag theo `ho-so-thuong-hieu/giong-thuong-hieu-david.md`.
- Gửi David: video, thumbnail (SendUserFile), tiêu đề.

## 8. Quy trình chung
- **Cách chạy một công thức** (mọi skill dựng: `dung-video-theo-phong-cach`, `dung-podcast`, `cat-doan-noi-bat`):
  - SKILL.md là **công thức**: thứ tự khối, quyết định riêng của loại, tiêu chí đạt. Cách làm từng bước ở README của khối; sửa cách
    làm thì sửa khối, không sửa công thức. Con số lấy ở hồ sơ `ho-so-thuong-hieu/`, không ghi cố định.
  - Đọc trước: `../chuan-muc-lam-viec.md` · file này · hồ sơ của loại; `references/loi-thuong-gap.md` của skill (và của skill gốc khi
    dùng chung template) đọc một lần ở đầu phiên. File khác chỉ đọc ở đúng bước cần (cột "Khối" của công thức).
  - Bước đánh dấu *(bước nhẹ)*: nhắc đổi sang mô hình chi phí thấp hơn theo `../chuan-muc-lam-viec.md` mục 3.
  - Ghi góp ý đúng một chỗ: khối / skill bị ảnh hưởng, kèm một dòng ở sổ `references/nhat-ky-thay-doi.md` của skill.
- Hỏi, chạy liên tục, lệnh nền, báo cáo cuối: `../chuan-muc-lam-viec.md` mục 2–4; mật khẩu: `AGENTS.md` luật 4. Riêng video: đã có quy trình nên không có điểm dừng duyệt
  giữa chừng trừ Đ2 (`quy-trinh.md` mục 1) (kể cả kế hoạch ghép vlog); báo cáo cuối thêm "đã chọn X vì Y" và tên riêng cần xác nhận.
- Không tải video từ YouTube/TikTok để dựng (đề nghị David gửi file); tải để học mẫu: `thiet-ke-bo-cuc/README.md` mục 4.
- Chụp thử (stills) trước khi render để Claude tự rà soát, không gửi David chốt; kiểm bản cuối theo khối 17 và 09. **Chụp có giới hạn:** chụp đúng mốc dễ lỗi (khung mới lần
  đầu, chỗ chồng lớp, điểm cắt, màn chốt, thẻ cuối, chỗ David góp ý), không chụp từng cảnh; xem bố cục thì dùng ảnh thu nhỏ.
- **Khi có góp ý, Claude sửa rồi render lại toàn bộ ngay**, không chờ chữ "render"; bàn giao lại như lần đầu (Drive + trang xem
  kết quả). Render nối tiếp, không song song. Claude không dừng chờ ở bước nào trước khi xong; chỉ việc đăng mạng xã hội và dọn dẹp mới chờ David (Đ2).
- **Phần cố định: không hỏi, không đổi** (`../chuan-muc-lam-viec.md` mục 2): nhận diện, dấu góc, màn chốt, thẻ cuối, nhạc theo tuyến, mức
  motion graphics, phụ đề, chuẩn âm lượng, nơi giao file; tên riêng chưa chắc chắn thì dùng cách Whisper nhận dạng và nêu ở báo cáo.
- **Thử skill bằng đoạn ngắn trọn một ý:** cắt từ đầu tới cuối một ý của video nguồn (không cố định số giây, không chạy cả video dài)
  vào thư mục thử riêng `tap-thu-…`, chạy theo skill, cho David xem bản cuối, xong thì dọn dẹp. Đoạn ngắn trọn ý cho kết quả tốt thì video dài cũng tốt.
- **Dựng ngay trong phiên Claude** theo skill (`phan-phoi-da-kenh` → skill dựng). Không đề xuất dựng app hay công cụ tự động dựng video
  trừ khi David yêu cầu, vì chạy app tốn nhiều token hơn.
- **Mọi sản phẩm làm ra đều tải đủ lên Drive** (lời David: "khi quy trình đã làm ra sản phẩm gì thì đều tải lên drive đầy đủ hết"): làm xong thì chạy `cho-dang.sh gui <tập>` (bản dài, bản xem nhẹ, clip,
  ảnh thu nhỏ, bài đăng, chương, số liệu) và, khi tách buổi theo hướng, `cho-dang.sh buoi <buổi>`; so khớp từng tệp rồi mới báo. Chỉ video gốc dung lượng quá lớn thì không tải, ghi vị trí lưu.
- **Xoá bản gốc chỉ sau khi duyệt**: kết quả đã đúng tiêu chí và David đã duyệt thì xoá bản gốc (video gốc, dự án, trung gian) trên Drive và mọi thiết bị để giải phóng dung lượng; chưa duyệt thì vẫn tải đủ lên Drive để David xem từ xa, **chưa xoá bản gốc**. Thiết bị Windows không truy vấn được trạng thái đồng bộ lên đám mây: chỉ xoá khi David đã xác nhận Drive đồng bộ xong. Khi làm lại cùng một tài nguyên thì bản mới nhất thay bản cũ: bỏ kết quả cũ của đúng tài nguyên đó sau khi bản mới đã lên Drive đủ, kiểm nguồn trước, không bỏ nhầm kết quả của buổi khác.
- Video đã chốt (David nói chốt là duyệt Đ2 cho việc dọn dẹp): bản cuối vào `~/Movies/cho-dang/<tập>/` + `cho-dang.sh gui` (Drive `thanh-pham/` giống hệt), dọn file tạm rồi đưa dự án lên Drive, xoá trên Mac theo khối 17 (`don-tap.py --xoa` → `luu-drive.sh`, không hỏi lại; chỉ hỏi phần ⏸ đang làm chưa xong). Đăng xong: `cho-dang.sh xong <tập>`. Mac chỉ giữ việc đang làm và bản cuối chưa đăng: ghi nhớ `video-chuyen-qua-drive`.
