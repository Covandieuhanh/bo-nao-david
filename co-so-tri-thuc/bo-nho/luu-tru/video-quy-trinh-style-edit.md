---
name: video-quy-trinh-style-edit
description: "Người dùng dựng video talking-head dọc theo phong cách mẫu bằng skill ~/.claude/skills/dung-video-theo-phong-cach; muốn đưa 2 video là xong, nhận MP4 đăng ngay"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 34d64c89-1380-4eb1-a174-1c542e5c48fc
  modified: 2026-11-01T08:45:33.835Z
---

Người dùng quay video dọc nói tiếng Việt, muốn Claude tự dựng theo phong cách một video mẫu (motion graphics, thẻ, chữ to, cảnh toàn màn hình, ảnh Openverse). Quy trình đã đóng gói thành skill `dung-video-theo-phong-cach` (2026-11-01); hướng dẫn cho người dùng ở `~/Movies/QUY-TRINH-DUNG-VIDEO.md`.

**Why:** Họ nói rõ chỉ muốn "đưa 2 video lên là tự được edit", bản MP4 cuối đã đủ dùng, không cần mở DaVinci/CapCut. Họ nhắc riêng về vùng an toàn của Reels/TikTok/Shorts (tiêu đề phía dưới, nút bên phải che nội dung).

**How to apply:** Chạy trọn quy trình không dừng hỏi duyệt từng bước; luôn giữ nội dung trong vùng an toàn x 70–900, y 210–1420 (khung 1080×1920); giao `video-final.mp4`; **không làm gói timeline DaVinci/CapCut trừ khi họ yêu cầu** (được hỏi trong lúc làm nếu chưa rõ). Bản Resolve của họ là bản App Store (không có scripting). Họ không tự gõ mật khẩu qua Claude — lệnh cần sudo thì đưa cho họ chạy.

Làm sạch video gốc (thêm 2026-11-01): cắt thừa đầu/cuối và câu nói lại (giữ lần sau cùng), sửa video lộn ngược/nằm ngang/lật gương. ~~Không cắt ngập ngừng~~ → ĐỔI 2026-11-04: mặc định cắt khoảng lặng ≥ 0,45 s + "ờ/ừm" (jump cut chuẩn kênh lớn) cho video nói trước camera và highlight; vlog/podcast dài giữ tự nhiên; bản tự nhiên khi David yêu cầu (`tu-nhien`). Xem [[video-nguoi-xem-trung-tam]].

Đổi khung (thêm 2026-11-01, họ đã duyệt mô tả): gốc dọc → xuất ngang = video giữa nguyên tỉ lệ, trái chủ đề + từ khoá đang nói, phải danh sách ý tích dần; gốc ngang → xuất dọc = khung bám người đang nói, **nhảy cắt qua lại** giữa hai người (không chia đôi màn hình), giữ nguyên thời lượng.

Không có màn hình nguồn ảnh 5 s ở cuối video (họ yêu cầu bỏ, 2026-11-01): ghi nguồn bằng `nguon-anh.txt` để họ dán vào mô tả bài đăng.

Chữ trên màn hình (2026-11-01, họ chọn phương án 2): luôn có **phụ đề đầy đủ** đúng từng chữ lời nói; chữ hiệu ứng chỉ được **trích/bỏ bớt**, không diễn đạt lại (họ phàn nàn khi chữ bị lược và đổi ý, vd. "Haruku" → "đi bộ mỗi ngày").
Bố cục chốt: phụ đề ở đáy vùng an toàn (từ 2026-11-04 video ngắn: 1–3 chữ to mỗi nhịp ngang ngực); thẻ/chữ hiệu ứng thu nhỏ (~78%). Hiệu ứng không toàn màn hình **không được che người nói**, vị trí không cố định (2026-11-02; `face_place.sh` dò mặt).

CapCut (2026-11-02): khi họ yêu cầu thì tạo thẳng dự án CapCut (`build_capcut.py`), phụ đề là chữ CapCut cùng font Be Vietnam Pro (họ thích font mặc định này). CapCut Mac đọc `draft_info.json` — đã mở được.

Podcast (2026-11-02): skill riêng `dung-podcast` — file tiếng/video podcast → video toàn motion graphics cùng phong cách, dùng chung template; khung xuất theo nguồn (ngang→ngang, dọc/chỉ tiếng→dọc) trừ khi họ yêu cầu; tập tối đa ~15 phút, 1–2 người nói. [[video-quy-trinh-style-edit]]

Minh hoạ (2026-11-02, họ đồng ý đề xuất): mặc định biểu tượng nét vẽ dần thay ảnh; ảnh chỉ khi nhắc địa danh/công trình/sản phẩm có thật và có ảnh tốt; họ nói "không dùng ảnh"/"thêm ảnh" thì theo. Chữ to tiếng Việt phải đủ dấu, không chồng dòng; podcast cỡ chữ/hiệu ứng vừa phải (họ bảo thu nhỏ).
So sánh 2026-11-02: họ chọn bản KHÔNG ẢNH (biểu tượng vẽ) cho podcast DJI — xác nhận mặc định không ảnh.
Ngoại lệ dùng ảnh (họ xác nhận): địa danh cụ thể, nhân vật có thật/lịch sử, tư liệu quá khứ, minh chứng xác thực; số liệu vẫn bằng hiệu ứng.
Bìa podcast (2026-11-02, đổi 2026-11-04): KHÔNG ghép bìa 1 s nữa; hỏi chữ thumbnail + ảnh người nói, thumbnail ở bước phát hành. Sửa dấu tiếng Việt bật cho cả hai skill.

Ghép nhiều clip (chốt 2026-11-02): clip chỉ có 2 loại — clip chính (ghép nối) hoặc clip minh hoạ (tắt tiếng, chèn dạng trích dẫn trong khung bo góc trên nền theo phong cách, đúng lúc câu nói liên quan); tự sắp mạch nội dung; **dừng cho họ duyệt kế hoạch + tờ liên kết trước khi render** (ngoại lệ của chạy một mạch).
Ô chữ highlight (2026-11-02): họ thử bản thay hết ô chữ bằng hình động và KHÔNG ưng — giữ thẻ/chữ to tóm ý; đừng đề xuất lại. Lớp phủ không bao giờ được chạm/đè phụ đề.
Thẻ toàn cảnh (2026-11-02): mọi ô thẻ thành màn hình toàn cảnh có hình động + NGUYÊN VĂN đầy đủ câu nói (không tóm tắt), 4–8 s; chữ to/hook/tên vẫn trên video; mặt hiện ~60%.
Tối giản (2026-11-02): một màn = một ý, một hình, một câu; ~1 hiệu ứng / 15–20 s; ẩn phụ đề khi thẻ toàn cảnh hiện câu nguyên văn; khung thẻ có quote chỉ giữ hình + nhãn.
Phụ đề + nâng khung (2026-11-02): một kiểu phụ đề chung cho mọi chế độ (subStyle.js); nhân vật/vật chính tụt nửa dưới → nâng khung (lift.py), đáy lấp hình mờ.
Mục tiêu video = người xem HIỂU rồi LÀM theo (2026-11-02): người dùng tên **David**. Câu hành động trong lời → tự ra màn `action`; MỌI video kết bằng màn chốt `cta` ~4 s; câu chốt KHÔNG cố định — Claude tự sáng tạo theo nội dung từng video (một hành động: bình luận/lưu/theo dõi/chia sẻ, giọng David, không bịa) — ngoại lệ họ cho phép của luật "chỉ trích lời".

Vị trí bộ skill (2026-11-03, David chọn): MỌI thứ ở `~/.claude/skills/san-xuat-video/` (dung-video-theo-phong-cach, dung-podcast, cat-doan-noi-bat + mẫu, nhạc, tiếng); `~/.claude/skills/<tên>` chỉ là lối tắt trỏ về đó. Sửa skill → sửa trong san-xuat-video; đường dẫn chéo giữa các skill để tương đối (`${0:A:h:h:h}`), không ghi cứng.
Highlight (2026-11-03, đổi 2026-11-04): 3–5 clip mỗi video dài (khoảnh khắc khác nhau, không phải biến thể), thẻ tít mở viết như tít báo đúng ý, cắt cứng không chip tua; lời kêu gọi bắt buộc; chừa một ý cho bản đầy đủ; nhịp game show 2 tông sôi động/lắng (đổi giữa chừng), nhạc chỉ 4 bài cố định ở `cat-doan-noi-bat/assets/music` — đừng đề xuất thêm bài hay nhiều lựa chọn nhạc.

Ghép nhiều clip (2026-11-03): thời lượng theo nội dung (không tỉ lệ cố định); tiêu chí giữ/bỏ ở multi-clip.md mục 2c — cảm xúc trước hết, giữ người khác trong khung, đoạn trầm thì tua cho có nhịp, tông bắt buộc khớp cảnh (tâm linh → lắng).
Vlog chuẩn (2026-11-04, David chọn): lấy kênh YouTube Jessie Luong (@jessieluongchannel) làm CHUẨN cho mọi vlog ghép nhiều clip, theo kiểu các video gần đây — mở đầu đoạn ghép cảnh đắt nhất cả chuyến — độ dài KHÔNG cố định, theo chất liệu + cảm xúc, chỉ cảnh thật sự khác nhau (David chê intro dài vì cảnh giống nhau) + tiêu đề trên đó → chào + bối cảnh → hành trình → kết bằng lời tổng kết của người quay; Claude tự chọn kiểu mở đầu theo nội dung (multi-clip.md 2d). David muốn nghiên cứu kênh mẫu KỸ (xem 6 video là "chưa đủ thấu hiểu").
Soát hình (2026-11-04): hình hỏng (trong túi, lật ngang/lộn ngược) thì bỏ kể cả có lời; lớp chữ không bao giờ đè phụ đề (LOW_Y).
Bộ nhận diện David (2026-11-04, David chốt): mọi loại video (làm video, ghép vlog, podcast, highlight) phải nhận ra cùng một người làm — dấu góc ● DAVID │ chủ đề, khuôn tiêu đề chung, tiếng ký hiệu ở tiêu đề, nhạc kênh dưới lời (cả 1 video và podcast, rất nhỏ), thẻ cuối chủ đề + DAVID; một nguồn brand.json (xem san-xuat-video/TONG-QUAN.md). Sửa skill nào cũng giữ đồng bộ cả 4.
Luật chung cả bộ (2026-11-04): `~/.claude/skills/san-xuat-video/quy-tac-chung.md` là một nguồn; mọi video có bước phát hành (3 tiêu đề + thumbnail `thumbnail.sh`) và `so-lieu.md`.
Thumbnail (2026-11-04, David chốt): ảnh thumbnail 1280×720 CHỈ khi video xuất ngang VÀ đăng YouTube; video xuất ngang → hỏi "có đăng YouTube không?" lúc đầu; video dọc chỉ đề xuất mốc khung bìa.
Học 80 video Việt (2026-11-04, David duyệt ưu tiên 1+2): báo cáo ở san-xuat-video/*/references/hoc-tu-20-*-vn.md; video > 3 phút đăng YouTube có màn kết 15–20 s (ytEnd), chương (chapters.py), teaser (teaser.py, > 10 phút); thumbnail kiểu Việt 3 tầng + số khổng lồ + nhãn series; highlight có tít ghim + cảnh phản ứng. Đã áp cả TH-1 (video > 3 phút chỉ cắt lặng ≥ 1,2 s, giữ tiếng đệm), HL-5 (nhãn "XEM BẢN ĐẦY ĐỦ" thẻ cuối highlight), PO-6 (lịch phát David đưa trên thẻ cuối).
Che người → toàn màn hình (2026-11-04, David chốt): lớp chữ/hiệu ứng chạm mặt, đầu, vai, ngực người nói → tự thành cảnh toàn màn hình ≤ 4 s (giữ mặt ≥ 60%); chỉ chạm tay/bụng/nền thì giữ lớp phủ; áp mọi loại có người (face_place.py, overlay_guard.py).
