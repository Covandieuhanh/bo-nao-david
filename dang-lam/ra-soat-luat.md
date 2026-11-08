# Rà soát luật — bước 1 của chuẩn hoá skill

Ngày 08/11/2026. Phạm vi: 5 skill video + `hoi-chuyen-gia` + khối dùng chung (`luat-chung`, `nguyen-tac`, `nhan-dien`, khối, hồ sơ) + `David.md`, `AGENTS.md`, bộ nhớ.
Cách đọc: mỗi dòng có **đề xuất**. David trả lời "đồng ý hết" hoặc sửa theo số (vd. "N4 chọn khác: …"). Chưa sửa file nào; sửa ở bước 2–3.
Nguyên tắc khi lệch: lời David mới nhất thắng (theo ngày chốt).

## David đã duyệt (08/11/2026)
- **Luật gỡ ngược:** chỗ nào ngược nhau thì lấy bên có ngày gần hiện tại nhất. Lý do: trước đây các skill không nối với nhau, sửa phần nào chỉ phần đó được cập nhật.
- **N4:** chữ trên video chỉ lấy những gì David nói chính xác trong video, không sáng tạo thêm. "Gỡ" chỉ lên video khi David nói câu đó.
- **N15:** lịch phát chỉ ghi khi David đưa cho đúng video đó.
- **C6:** tên trang Facebook, TikTok để sau; giữ nguyên trong `kenh.json`.
- **Đối chiếu sản phẩm mới nhất** (`~/Movies/tap-cuoc-song-giau-co`, render 08/11 13:40): bản dài không thẻ tít; màn chốt nguyên văn ("Bạn cứ chia sẻ với mình nhá"); bố cục `bocuc` / `nhan` / `the` (không 2 trạng thái); nhạc theo tuyến (`tam_su`). Clip highlight: tít nguyên văn ("Tại sao anh vẫn còn đi làm" có trong lời), câu kêu gọi nguyên văn, phụ đề `SHORT`, nhạc kho `soi` / `lang`, thẻ cuối không nút phát. **Khớp mọi đề xuất bên dưới** → mọi dòng N, T, C coi như đã duyệt theo đề xuất.

## A. Ngược nhau (cần David chốt)

| # | Chuyện | Bên này | Bên kia (mới hơn) | Đề xuất |
|---|---|---|---|---|
| N1 | Hỏi hay chạy một mạch | `video-style-edit` dòng 16, `podcast-style-edit` dòng 184, ghi nhớ `video-quy-trinh-style-edit`: "chạy một mạch, không dừng hỏi" | `luat-goi-y-de-david-chon` (liệt kê điểm cần chọn, chờ David chọn), `video-podcast-phu-hinh-30` (chụp thử, David chốt rồi mới render) | Một luật ở file thói quen chung: **hỏi một lần đầu, gộp mọi điểm cần chọn** (chữ bìa, câu chốt, cảnh…), sau đó chạy một mạch. Ngoại lệ tự chọn: cắt highlight, làm lại video cũ. Bỏ câu "không dừng hỏi" ở 2 skill |
| N2 | Thẻ tít mở đầu video thường | `luat-chung` mục 2, `nguyen-tac` 1, khối 06, tiêu chí đạt `video-style-edit`, luật 8 "thẻ tít 0–2 s", podcast "mở 0–3 s = thẻ tên tập", mô tả skill "mở đầu 3 giây có tiêu đề" | `luat-chung` mục 1 + `video-chu-nguyen-van` (07/11): không thẻ tít mặc định; `video-style-edit` luật 2: "tạm bỏ" | **Không thẻ tít mặc định**, chỉ khi David yêu cầu, chữ nguyên văn. Sửa mọi chỗ còn lại |
| N3 | Thẻ tít highlight: tít báo hay nguyên văn | `cat-highlight-video` luật 3, thân luật 7, 7A, 7B, tiêu chí; `luat-chung` 1(b); ghi nhớ `luat-goi-y` (tự chọn tít) | Đầu luật 7 + `luat-chung` 1 (07/11): chữ trên video nguyên văn, tít = cụm đắt nhất của clip | **Tít = cụm nguyên văn đắt nhất**, Claude tự chọn. "Viết như tít báo" chỉ còn cho tiêu đề bài đăng |
| N4 | Câu màn chốt | `luat-chung` 1(a) + mục 6, podcast dòng 205, ghi nhớ `video-quy-trinh`: Claude tự viết; podcast + khối 08: màn chốt ghi "Vấn đề / Kết quả", "gỡ" | `luat-chung` 1, `video-style-edit` luật 4, `video-chu-nguyen-van`: nguyên văn câu David nói cuối; "Vấn đề / Kết quả" chỉ ở bài đăng | **Màn chốt = nguyên văn lời David.** "Vấn đề / Kết quả" chỉ ở bài đăng, bình luận ghim. Lời mời "gỡ": lên video chỉ khi David nói trong video, không thì để bài đăng (**David xác nhận**) |
| N5 | Cỡ phụ đề video ngắn | Ghi nhớ `video-nguoi-xem-trung-tam`, `video-quy-trinh`: 1–3 chữ to; `cat-highlight` 7B: "nhịp 1–3 chữ" | `video-phu-de-mot-cho-chu` (08/11): cụm 5–8 chữ, cỡ 58 | Theo 08/11, sửa các chỗ cũ |
| N6 | Con số cố định về nhịp, mật độ, độ dài cảnh | `video-style-edit` luật 1, 3, 4 (~1 hiệu ứng/15–20 s, chữ to ≤ 3–4 lần, ~8–10 điểm nhấn/4 phút, cảnh 2–5 s, 3–5 s); `luat-chung` 2 (5–8 s, 15–20 s); `nguyen-tac` 7 (1–3 s); `cat-highlight` 7A (1/5–8 s); podcast (60–120 s, 40–60 s); ghi nhớ `video-quy-trinh` (thẻ 4–8 s, mặt ~60%, toàn màn ≤ 4 s) | `video-bo-cuc-tu-can` (07/11): bỏ hết số cố định về bố cục | **Bỏ số về nhịp, mật độ, độ dài cảnh.** Giữ số kỹ thuật: vùng an toàn, âm lượng, cỡ chữ podcast David đã chốt ("đừng phóng to lại") |
| N7 | Nhạc | `luat-chung` 5, khối 09 dòng 16, `cat-highlight` luật 9, ghi nhớ `video-quy-trinh`: chỉ 4 bài cố định, không đề xuất thêm | `video-nhac-theo-tuyen`: chọn theo 5 tuyến, tuyến kiến thức chờ tải bài; khối 09 dòng 30 | **Một kho nhạc kênh chia theo tuyến**; chỉ dùng bài trong kho, thiếu thì báo David |
| N8 | Mức nhạc | Ghi nhớ `video-nhac-theo-tuyen`: "nhẹ 1 xíu, tắt hẳn cũng được" | `video-chuan-am-luong` (06/11): thấp hơn giọng ~23 dB | Theo 23 dB; sửa câu cũ trong ghi nhớ nhạc |
| N9 | Kim chỉ nam học kênh lớn | `luat-chung` 0, `nguyen-tac`, ghi nhớ `video-nguoi-xem-trung-tam`: "sao chép luôn chuẩn kênh lớn, trái gu riêng thì theo kênh lớn" | `luat-noi-dung-cua-david`, `video-bo-cuc-tu-can`, `luat-hoc-la-bo-sung`: chỉ học trình bày, giữ thẩm mỹ, chỉ bổ sung | Viết lại: **người xem là trung tâm; học kênh lớn ở nhịp và trình bày; không chép thẩm mỹ; chỉ thêm, không thay cái David đã chốt** |
| N10 | Mặt trên thumbnail | `nguyen-tac` 5 "thumbnail = mặt có cảm xúc"; `nhan-dien.md` + ghi nhớ `video-quy-trinh`: podcast hỏi "ảnh người nói" | `video-podcast-bia-khong-mat` (06/11) | Mặt chỉ cho video quay hình; podcast theo công thức bìa không mặt; bỏ câu hỏi ảnh người nói |
| N11 | Cắt lặng video > 3 phút | Ghi nhớ `video-quy-trinh` (TH-1): "video > 3 phút cắt lặng ≥ 1,2 s" | `video-dai-khong-cat` (05/11) | Bỏ TH-1 |
| N12 | Số clip highlight | `MEMORY.md` + ghi nhớ `video-quy-trinh`: 3–5 clip | `video-clip-ngan-dung-doc-lap`, `cat-highlight` luật 2 (07/11): theo số ý đạt 4 câu | Theo 07/11, sửa chỗ cũ |
| N13 | Lời kêu gọi highlight | `cat-highlight` luật 4: bắt buộc, không có thì dừng báo David | Bốn câu chọn ý (07/11): "không bắt buộc câu giao việc"; khuôn podcast dọc bỏ luật 4 | Lời kêu gọi **chỉ khi có trong lời**; không có thì không dừng, clip vẫn phải đạt `mang_ve` |
| N14 | Thẻ cuối highlight | `cat-highlight` 7B: "nút phát + tên tập"; `luat-chung` 1(c) + tiêu chí: "XEM BẢN ĐẦY ĐỦ" | Luật 11 + `video-nhan-dien-chung` (08/11): không nút phát, "Bản đầy đủ trên kênh …" | Một chữ: "Bản đầy đủ trên kênh <tên kênh>", không nút phát |
| N15 | Lịch phát trên video | `luat-chung` 1(c): lịch phát David đưa được ghi trên thẻ cuối | Podcast (05/11): không ghi thông tin phát hành nào lên video | Chỉ ghi khi David đưa cho đúng video đó (**David xác nhận** hay bỏ hẳn) |

## B. Trùng (một luật nằm nhiều chỗ) → giữ một nhà, chỗ khác một dòng trỏ

| # | Luật | Đang nằm ở | Nhà đề xuất |
|---|---|---|---|
| T1 | Hỏi trước khi làm | `~/.claude/CLAUDE.md`, `David.md` 3.1, `AGENTS.md` luật 2, `hoi-chuyen-gia`, ghi nhớ `luat-tu-hoi-khi-mo-ho` + `luat-goi-y-de-david-chon`, `luat-chung` 8, `dang-da-kenh` | `hoi-chuyen-gia` (cách hỏi) + file thói quen chung (khi nào hỏi) |
| T2 | Đẩy GitHub / sync | `David.md` 3.8, `AGENTS.md` (2 chỗ), ghi nhớ `nao-github-ban-goc` + `nao-repo-david-claude`, `hoc-video-mau` | Ghi nhớ `nao-github-ban-goc` (gộp `nao-repo-david-claude` vào) + file thói quen chung (cuối việc) |
| T3 | Luật kênh (lịch, 4·4·2, "Vấn đề / Kết quả", "gỡ") | `David.md` mục 5, `ho-so/kenh.json`, ghi nhớ `nao-ho-so-va-bo-loc` | `kenh.json`; `David.md` giữ định hướng, bỏ chi tiết lặp |
| T4 | Video dài không cắt | `luat-chung` 2, ghi nhớ, podcast, `video-style-edit` luật 5 + bước 3, `dang-da-kenh` | `luat-chung` 2 |
| T5 | Chữ nguyên văn | `luat-chung` 1, ghi nhớ `video-chu-nguyen-van`, `cat-highlight` 3/7, `video-style-edit` 4 | `luat-chung` 1 |
| T6 | Chỉ hình của chính video | `luat-chung` 7, ghi nhớ, `dang-da-kenh`, khối 14 | `luat-chung` 7 |
| T7 | Không ghi chú kỹ thuật | `luat-chung` 4, `video-style-edit` (Đầu vào), ghi nhớ | `luat-chung` 4 |
| T8 | Học là bổ sung | Ghi nhớ `luat-hoc-la-bo-sung` + `luat-noi-dung-cua-david` + `video-bo-cuc-tu-can`, `hoc-video-mau`, `trinh-bay/README`, `luat-chung` 4 | `trinh-bay/README`; ghi nhớ chỉ giữ một |
| T9 | Không tự render lại | Ghi nhớ `video-khong-tu-render`, `dang-da-kenh`, `luat-hoc-la-bo-sung` | File thói quen chung |
| T10 | Chạy nền, báo cáo, chụp thử trước render | `luat-chung` 8, podcast, `cat-highlight`, từng khối | File thói quen chung (cách làm) + khối 17 (chi tiết) |
| T11 | "Đọc luat-chung trước" | Mỗi skill nhắc 2–4 lần (Đọc trước · Luật · Tài liệu kèm) | Một khối "Đọc trước" duy nhất ở đầu mỗi skill — **tiết kiệm token** |
| T12 | Ghi nhớ `video-quy-trinh-style-edit` | 30 dòng nhật ký 01–04/11, gần hết đã vào `luat-chung` / changelog, nhiều dòng đã bị thay (N1, N4, N5, N6, N7, N10, N11, N12) | **Chuyển vào `luu-tru/`**, phần còn đúng đã có nhà ở `luat-chung` |

## C. Cũ (lỗi thời, sửa chữ là xong)

| # | Ở đâu | Cũ | Đề xuất |
|---|---|---|---|
| C1 | `hoi-chuyen-gia` dòng 8, 37 | "Khách của David = người thuê David làm nội dung"; "quyết định kinh doanh" | Khách = người lần đầu dẫn người + người xem video; bỏ "kinh doanh" |
| C2 | `GIOI-THIEU.md`, ghi nhớ `video-kien-truc-skill` | "18 khối", "khoi/01…18", "4 dự án mẫu", "4 skill", "2 trạng thái là mặc định" | 21 khối (00–20), 5 video chuẩn, bỏ "2 trạng thái" |
| C3 | `video-style-edit` bước 8, `multi-clip.md` dòng 11, `scene-design.md` dòng 13 ("MẶC ĐỊNH"), `khoi/README` dòng 14, khối 06 dòng 17, `ho-so/highlight.md`, `thu-vien-hinh/README`, chú thích trong `Illus.jsx` | Còn ghi "2 trạng thái" (code đã tắt qua `hai_trang_thai: false`) | Sửa chữ thành "bố cục tự cân" |
| C4 | Ghi nhớ `video-ban-chuan`, `video-doc-khuon-chu-chinh`, `video-podcast-phu-hinh-30` | Đường dẫn `~/Movies/podcast-hl-di-trainer-A|B|C`, `podcast-dji-20261105`, `podcast-muc-tieu-su-menh-v2` (không còn trên máy) | Đổi sang `~/Movies/tap-…` theo sổ chuyển file 07/11 |
| C5 | Ghi nhớ `video-quy-trinh-style-edit` | Trỏ `~/Movies/QUY-TRINH-DUNG-VIDEO.md` (không còn); gọi David là "người dùng / họ" | Xử lý cùng T12 |
| C6 | `ho-so/kenh.json`, ghi nhớ `nao-ho-so-va-bo-loc` | Trang "David Sức khoẻ", `@davidsuckhoe` (hướng sức khoẻ đã bỏ); ghi nhớ `video-lam-lai-video-cu` ghi kênh "David Trần - Trainer định hướng" | **David xác nhận** tên và link trang, TikTok hiện tại |
| C7 | Ghi nhớ `nao-ho-so-va-bo-loc` | "Hồ sơ gốc bản 05/11" | Bỏ ngày, chỉ trỏ `David.md` |
| C8 | `David.md` 3.1 | "Hỏi 3–5 câu, mỗi câu 2–3 gợi ý" (skill hiện: mỗi câu một đề xuất "đồng ý" được, việc lớn nhiều vòng) | `David.md` một dòng trỏ `hoi-chuyen-gia` (gộp vào T1) |

## Ba câu chỉ David trả lời được
1. **N4** — lời mời "nhắn mình một chữ 'gỡ'": lên màn chốt chỉ khi David nói trong video? ➡️ Đề xuất: đúng vậy, không thì để ở bài đăng.
2. **N15** — lịch phát trên thẻ cuối: giữ khi David đưa, hay bỏ hẳn khỏi video? ➡️ Đề xuất: giữ khi David đưa cho đúng video đó.
3. **C6** — trang Facebook và TikTok hiện tại tên gì, link gì? ➡️ Đề xuất: nếu chưa đổi thì giữ link, ghi chú "tên trang cũ, chờ đổi".
