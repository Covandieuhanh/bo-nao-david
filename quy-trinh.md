---
description: "Cây quy trình của bộ não — việc gì cũng đi từ quy trình gốc, xuống nhánh, tới quy trình lá; bảng tra duy nhất: câu David hay nói, quy trình, điểm duyệt, xong khi."
---

# Cây quy trình — việc gì cũng có quy trình, đi từ gốc lên

Cách **nghĩ** trong mọi bước (bóc tách, vòng kết quả hoặc vấn đề, học và thay đổi, kiểm sai): [tu-duy-goc.md](co-so-tri-thuc/tu-duy-goc.md)
(mục 5 chỉ rõ khối nào dùng ở bước nào). Mọi phiên, mọi thiết bị, mọi AI đi cùng một đường để ra cùng một kết quả: đi từ **gốc** (cách làm mọi việc), lên **nhánh** (một mảng việc),
tới **lá** (một việc cụ thể, có file quy trình, điểm duyệt và tiêu chí hoàn thành). Đây là bảng tra duy nhất; `AGENTS.md`
chỉ trỏ về đây.

## 0. Gốc — mọi việc đều đi đủ 7 bước

Bảy bước vận hành triển khai khung bốn bước của [tư duy gốc](co-so-tri-thuc/tu-duy-goc.md#2-khối-hành-động--vòng-kết-quả-hoặc-vấn-đề). Khi đầu ra David yêu cầu là kế hoạch, giao bản bốn phần theo [luật 2](AGENTS.md#sáu-luật-không-được-phá). Điểm Đ1 quyết định lúc được bắt đầu thực hiện.

| # | Bước | Làm theo |
|---|---|---|
| 1 | **Nhận yêu cầu, tra cây:** tra quy trình trước khi làm; việc có tài nguyên thì tra sổ danh mục (đã làm chưa → làm lại thì bản mới thay bản cũ); tìm lá khớp ở mục 3 (David chỉ gửi video hoặc ghi âm không kèm lời thì là lá B1); có lá thì làm tự động hoàn toàn (mục 1) | file này |
| 2 | **Đọc đúng phần cần, tra hình mẫu:** tra [bản đồ hình mẫu](co-so-tri-thuc/hinh-mau/README.md) cho mục nhỏ của việc; chưa có hoặc chưa đủ (ít nhất 5, việc lớn 10) thì nghiên cứu theo lá A8 trước khi làm, kết luận đưa vào kế hoạch; file quy trình của lá → chỉ những khối, hồ sơ mà bước đang làm cần; đặt Mục tiêu và Xong khi; được phép làm phần chuẩn bị (mục 1). Thiết bị chưa từng dựng video (chưa có `kiem-tra-thiet-bi.sh` đạt và bài kiểm suy luận đạt ít nhất 8/10) thì làm lá A2 trước khi dựng thật | `ky-nang/chuan-muc-lam-viec.md` mục 1 |
| 3 | **Điểm duyệt Đ1, chỉ cho việc chưa có lá: trình 4 phần, dừng chờ "duyệt"**; việc đã có lá thì bỏ bước này, tự làm trọn (mục 1) | `chuan-muc-lam-viec.md` mục 2 · `ky-nang/thu-thap-yeu-cau/SKILL.md` |
| 4 | **Làm đúng từng bước của lá theo thứ tự**, liên tục không ngắt quãng, không thêm, không bớt, không đổi bước; chỉ dừng ở Đ2, Đ3 hoặc chỗ lá ghi David cần xem. Gặp vấn đề: ở cách làm thì xử lý ngay; quy trình sai hay thiếu thì sửa quy trình rồi làm tiếp (mục 1); giả định của kế hoạch sai ở việc chưa có lá thì trình lại kế hoạch (`tu-duy-goc.md` khối 2) | file quy trình của lá · `chuan-muc-lam-viec.md` mục 3 |
| 5 | **Tự rà soát** theo "Xong khi" của lá, gồm câu "một phiên mới chỉ đọc GitHub có làm ra đúng kết quả này không?" | `chuan-muc-lam-viec.md` mục 4 |
| 6 | **Giao kết quả kèm báo cáo ngắn:** đã làm gì · đã kiểm gì · chưa kiểm gì · cần David xác nhận gì · đã sửa quy trình chỗ nào · 2–3 dòng so với hình mẫu (giống ở đâu, khác ở đâu, nên chỉnh gì) | lá A6 · `chuan-muc-lam-viec.md` mục 4 |
| 7 | **Ghi lại, đẩy GitHub:** góp ý thì sửa đúng một chỗ và ghi nhật ký, việc mới thì viết thành lá (mục 2), `bash tu-dong-hoa/dong-bo.sh --push` | `chuan-muc-lam-viec.md` mục 4 · `AGENTS.md` luật 6 |

## 1. Điểm duyệt, chế độ tự chạy, không lệch quy trình

**Ba điểm duyệt** (mỗi lá ghi rõ lá đó dừng ở điểm nào, mục 3):
- **Đ1 — duyệt 4 phần trước khi làm, chỉ cho việc chưa có lá.** Việc đã có lá thì không có Đ1. Trước Đ1 Claude chỉ được làm **phần chuẩn bị**, không thay đổi gì của David hay của bộ não: đọc, tải
  tài nguyên về thư mục dự án, chép lời, đo, ghi phiếu lọc hoặc `phan-huong.md` trong thư mục dự án, ghi mục nhật ký nội dung
  (`du-an/nhat-ky-noi-dung/`) và dòng "lọc" trong sổ danh mục (đây là ghi chép, không đổi luật). Không sửa skill, luật, hồ sơ; không
  dựng, không render bản thật trước Đ1.
- **Đ2 — duyệt trước khi gửi tin, thao tác tài khoản, xoá ngoài quy trình dọn sau khi David chốt (`ky-nang/san-xuat-video/quy-tac-chung.md` mục 8)** (tin nhắn, trả lời bình luận, tài khoản mạng xã hội): Claude chỉ làm khi
  David nói đúng việc đó. **Không bao giờ bỏ** (`AGENTS.md` luật 4).
  - **Đăng:** Claude không đăng lên mạng xã hội: Claude chuẩn bị đủ gói đăng (bản cuối, tiêu đề, mô tả, bài theo từng kênh, bình luận ghim, ảnh bìa, lịch và thứ tự đăng gợi ý) ở nơi giao và Drive; David tự đăng khi muốn, không cần hỏi hay duyệt. Không kết thúc báo cáo bằng câu hỏi "đăng bản này?". Khi David báo "đã đăng <tập>" thì Claude ghi sổ danh mục và dọn bản chờ đăng (lá B11).
  - **Lên Drive, thay bản cũ, xoá bản gốc:** làm ra kết quả là lên Drive ngay, đủ hết; sửa thì tải bản mới nhất lên và xoá bản cũ; David chốt bản cuối thì Claude xoá bản gốc theo quy trình, không hỏi lại. Nguồn duy nhất: `ky-nang/san-xuat-video/quy-tac-chung.md` mục 8.
  - **Người khác xuất hiện** (đối tác, khách; khách của công ty Veltrix): Claude dựng được, giữ nguyên lời nói; ghi vào mục "Ghi chú đăng" của gói phát hành
    (ai xuất hiện, lằn ranh) để David biết, không hỏi.
- **Đ3 — duyệt trước khi sửa thông tin về David** (`david.md`, hồ sơ, ghi nhớ David đã chốt), màu chủ đạo, chữ ký nhận diện: Claude luôn trình
  lại, chờ "duyệt". Không bỏ ở chế độ tự chạy.

**Chế độ tự chạy:** là mặc định của **mọi việc đã có lá**. Với việc chưa có lá, Claude chỉ bật khi chính lời David trong yêu cầu đó nói rõ, ví dụ "làm tới khi có kết quả, không cần hỏi lại", "tự làm
luôn, bỏ qua duyệt". Khi chạy, chế độ này: bỏ Đ1 và các lần dừng chờ giữa
chừng (chốt phương án; riêng đoạn thử B5 khi David yêu cầu xem trước thì vẫn dừng); điểm nào cần chọn thì theo mặc định của skill, chưa có mặc định thì theo tiêu chí của skill, ghi
"đã chọn X vì Y" trong báo cáo; câu chạm lằn ranh thì theo mặc định giữ nguyên lời nói (không dùng làm chữ đồ hoạ, tiêu đề, mô tả) và liệt kê trong
báo cáo. **Vẫn giữ Đ2, Đ3.** Không làm tiếp được (thiếu file, nguồn hỏng, không có mặc định cho một lựa chọn làm đổi hẳn kết quả) thì dừng
lại và báo David. Render lâu không phải lý do dừng (chạy nền). Báo cáo cuối ghi đã chọn gì, đã sửa quy trình chỗ nào.

**Góp ý của David là lời duyệt** cho đúng thay đổi đó, gồm cả việc ghi thay đổi vào skill (lá B13): Claude sửa, render lại, giao lại mà không hỏi. Chỉ
Claude tự thấy cần đổi quy trình ngoài lời góp ý thì sửa và báo trong kết quả, không qua Đ1 (trừ Đ3; tầng 0–1 đổi theo luật thăng cấp của trục).

**Không lệch quy trình:** Claude làm đúng từng bước của lá theo thứ tự. Giữa chừng thấy quy trình sai, thiếu, hay hai chỗ ngược nhau thì
**sửa đúng chỗ đó của quy trình** (chọn theo luật ưu tiên `chuan-muc-lam-viec.md` mục 0), ghi nhật ký thay đổi, rồi làm tiếp theo bản đã sửa và báo trong kết quả;
không làm khác quy trình mà không sửa quy trình.

## 2. Việc chưa có lá trong cây

Claude làm theo gốc với khung lá dưới đây (Đ1 áp dụng vì việc chưa có quy trình); xong việc, **trước khi báo xong**, viết cách vừa làm thành một lá (file quy trình đặt đúng
nhánh, script đã dùng để ra kết quả đưa vào repo) và thêm một dòng vào mục 3 — cách viết thành skill: `ky-nang/hoc-lien-tuc/SKILL.md` Việc 3.
Lần sau việc đó đã có quy trình, phiên nào cũng làm giống nhau.

**Khung một quy trình lá** (mọi file quy trình có đủ): **Khi nào dùng** · **Đầu vào** · **Các bước** (lệnh, script có trong repo, không
ghi cố định công cụ chỉ một thiết bị có) · **Điểm duyệt** (Đ2 / Đ3 ở bước nào, chỗ David cần xem nếu có, hoặc "không có"; lá đã có thì không có Đ1) · **Xong khi** (đo được) · **Kiểm gì** ·
**Lỗi hay gặp** (nếu có). Công cụ kiểm tra `tu-dong-hoa/kiem-quy-trinh.py` chạy mỗi lần đẩy GitHub: mọi lá trỏ tới file có thật, có điểm duyệt và
"Xong khi"; mọi `SKILL.md` dùng chung có mục "Xong khi" và có lá trong cây.

## 3. Nhánh và lá

### A. Bộ não (cách làm việc, lưu, đồng bộ, học)
| Lá | Việc (David hay nói) | Quy trình | Điểm duyệt | Xong khi |
|---|---|---|---|---|
| A1 | "cập nhật não", đẩy hoặc kéo GitHub | [AGENTS.md luật 6](AGENTS.md) · `tu-dong-hoa/dong-bo.sh` | không có (lời David là lệnh) | lệnh báo "Đã đẩy lên GitHub", `git status` sạch |
| A2 | cài bộ não lên thiết bị mới (Mac, Windows qua WSL, Linux) | [huong-dan-cai-dat.md](huong-dan-cai-dat.md) · [tu-dong-hoa/thiet-bi-khac/README.md](tu-dong-hoa/thiet-bi-khac/README.md) | không có Đ1; mật khẩu thiết bị thì David tự gõ | `kiem-tra-thiet-bi.sh` ra "MÁY NÀY DỰNG GIỐNG MAC CHÍNH" |
| A3 | "nhìn lại tuần", "tự học", "học từ kênh X", "học cái này thành quy trình" | [ky-nang/hoc-lien-tuc/SKILL.md](ky-nang/hoc-lien-tuc/SKILL.md) | không có Đ1: phân tích và sửa tự chạy, báo sau; Đ3 khi sửa thông tin về David, màu, nhận diện | theo mục "Xong khi" của skill |
| A4 | "nâng cấp", "tái bản", luật chồng chéo, gom luật trùng | [hoc-lien-tuc Việc 4](ky-nang/hoc-lien-tuc/SKILL.md) · [ky-nang/tai-cau-truc/SKILL.md](ky-nang/tai-cau-truc/SKILL.md) | không có Đ1: đo, chưng cất, dọn tự chạy, báo số đo trước và sau khi sửa; cắt giảm (chuyển vào lưu trữ), đưa lên tầng 1, cập nhật dần tầng 0 đều tự chạy theo luật thăng cấp (`truc-tri-thuc.md` mục 4) | `do-chong-cheo.py` dưới ngưỡng ở mọi bộ, bản luật không còn câu trùng hay ngược nhau |
| A5 | học, sửa, lưu thông tin mới vào bộ não (ghi nhớ, kiến thức, hồ sơ) | [co-so-tri-thuc/truc-tri-thuc.md](co-so-tri-thuc/truc-tri-thuc.md) · [quy ước liên kết](co-so-tri-thuc/quy-uoc-lien-ket.md) | không có Đ1; thông tin về David thì Đ3; thăng cấp tầng theo luật của trục, tự chạy | mỗi ý ở đúng một nguồn duy nhất, có dòng ở `ban-do/`, công cụ kiểm tra liên kết đạt |
| A6 | giao kết quả cho David | [phan-phoi-da-kenh bước 5](ky-nang/san-xuat-video/phan-phoi-da-kenh/SKILL.md) | không có: giao, lên Drive ngay; David chốt thì tự dọn, đưa dự án lên Drive, xoá bản gốc theo quy trình | bản cuối ở nơi giao của thiết bị (Mac: trang Chờ đăng và Drive; thiết bị chỉ dựng video: Drive); David theo dõi từ xa thì gửi thêm bản nhẹ dưới 30 MB qua tệp đính kèm |
| A7 | việc chưa có lá: hỏi lại khi chưa rõ yêu cầu, trình 4 phần | [ky-nang/thu-thap-yeu-cau/SKILL.md](ky-nang/thu-thap-yeu-cau/SKILL.md) | chính là Đ1 | theo mục "Xong khi" của skill |
| A8 | trước mọi việc chưa có đủ hình mẫu; "nghiên cứu hình mẫu", "xem người ta làm thế nào", "học từ người đã thành công" | [co-so-tri-thuc/hinh-mau/quy-trinh-nghien-cuu.md](co-so-tri-thuc/hinh-mau/quy-trinh-nghien-cuu.md) | không có cho phần nghiên cứu và ghi bản đồ (phần chuẩn bị); đưa vào skill, luật: theo việc chính | mục nhỏ có ít nhất 5 hình mẫu (việc lớn 10) đủ bốn cột, có ngày đo; nhật ký có mục mới; tin giao có 2–3 dòng đối chiếu |

| A9 | lập bảng giao việc, bóc bước thực thi cho các ban | [Lập bảng giao việc](ky-nang/quy-trinh-van-hanh-chung.md#2a-lập-bảng-giao-việc) | lập bảng theo quy trình này; quyết định nghiệp vụ chưa chốt được đưa thành việc cần duyệt | mỗi dòng có hành động, ban, hạn và đầu ra kiểm được; thứ tự đúng phụ thuộc; Kết quả và Vấn đề trống |

### B. Sản xuất video (gốc nhánh: `phan-phoi-da-kenh` — một tài nguyên vào, đủ bản dài, clip, bài đăng ra)
| Lá | Việc (David hay nói) | Quy trình | Điểm duyệt | Xong khi |
|---|---|---|---|---|
| B1 | gửi video hoặc ghi âm (có hay không kèm lời), "làm video này", "làm bài đăng" | [phan-phoi-da-kenh](ky-nang/san-xuat-video/phan-phoi-da-kenh/SKILL.md) | không có (Claude không đăng, chỉ chuẩn bị gói đăng; David chốt thì tự dọn); lá dựng: có hình người nói thì B6, chỉ có tiếng hoặc David gọi là podcast thì B7 | theo mục "Xong khi" của skill |
| B2 | gửi liên kết Drive, YouTube, file hoặc thư mục | [nhan-tai-nguyen.md](ky-nang/san-xuat-video/phan-phoi-da-kenh/references/nhan-tai-nguyen.md) | không có (phần chuẩn bị) | file gốc ở `~/Movies/tap-<tên>/1-goc/`, đọc được khung, độ dài, tiếng |
| B3 | lọc có đáng làm không, phân theo ba hướng nghề, ghi nhật ký nội dung | [khối 00 mục 0b](ky-nang/san-xuat-video/mo-dun/00-sang-loc-noi-dung/README.md) | không có (phần chuẩn bị); kết quả lọc đưa vào kế hoạch của B1 hoặc B4 | có `phan-huong.md` của tập và mục nhật ký của từng hướng có ý |
| B4 | "cắt đoạn thừa, tách thành các video theo hướng công việc" | [tach-theo-huong.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/tach-theo-huong.md) | không có (gói đăng chuẩn bị sẵn, David tự đăng; David chốt thì tự dọn) | mỗi hướng một dự án dựng xong kèm clip ngắn và gói phát hành, đã giao |
| B5 | "render một đoạn ngắn cho tôi xem trước" | [doan-thu.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/doan-thu.md) | sau bước 6 dừng chờ David xem đoạn thử rồi mới dựng cả video (đây là việc David yêu cầu) | David nhận đoạn thử, nói duyệt hay sửa trước khi dựng cả video |
| B6 | dựng video tự quay (một video, nhiều file một buổi), ghép vlog | [dung-video-theo-phong-cach](ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md) | không có (David chốt thì tự dọn) | theo mục "Xong khi" của skill |
| B7 | podcast hoặc ghi âm thành video đồ hoạ | [dung-podcast](ky-nang/san-xuat-video/dung-podcast/SKILL.md) | không có (David chốt thì tự dọn) | theo mục "Xong khi" của skill |
| B8 | cắt highlight, clip ngắn | [cat-doan-noi-bat](ky-nang/san-xuat-video/cat-doan-noi-bat/SKILL.md) | không có (David chốt thì tự dọn) | theo mục "Xong khi" của skill |
| B9 | học cách trình bày từ video mẫu David gửi | [phan-tich-video-mau](ky-nang/san-xuat-video/phan-tich-video-mau/SKILL.md) | không có Đ1: phân tích, phiếu học, đưa vào skill tự chạy, báo sau; đụng màu chủ đạo, chữ ký nhận diện: Đ3 | theo mục "Xong khi" của skill |
| B10 | tiêu đề, mô tả, chương, teaser, bài đăng theo giọng David | [khối 15](ky-nang/san-xuat-video/mo-dun/15-xuat-ban/README.md) · [giọng David](ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md) | không có riêng (nằm trong việc chính) | `phat-hanh/phat-hanh.md` đủ mục, đúng giọng, chữ nguyên văn lời David |
| B11 | "đã đăng <tập>" (David tự đăng) | [khối 15](ky-nang/san-xuat-video/mo-dun/15-xuat-ban/README.md) (gói đăng) · [khối 19](ky-nang/san-xuat-video/mo-dun/19-dang-bai/README.md) (tạm ngưng: Claude không đăng) | không có | sổ danh mục ghi "đã đăng" kèm liên kết David gửi; bản chờ đăng đã dọn (`cho-dang.sh xong`) |
| B12 | số liệu sau 24 giờ hoặc 7 ngày, hộp thư | [khối 20](ky-nang/san-xuat-video/mo-dun/20-hop-thu-so-lieu/README.md) · [khối 16](ky-nang/san-xuat-video/mo-dun/16-phan-tich-so-lieu/README.md) | đọc số liệu thì không có; trả lời bình luận, tin nhắn: Đ2; sửa skill theo số liệu: tự sửa, báo sau | `so-lieu.md` cập nhật kèm 1–3 đề xuất |
| B13 | góp ý trên video đã dựng ("cảnh 2:08 chữ to quá", "bỏ cảnh X") | [dung-video-theo-phong-cach mục "Sửa theo góp ý"](ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md) | không có: góp ý là lời duyệt cho chính thay đổi đó, kể cả ghi vào skill (mục 1); Claude tự thấy cần đổi thêm: sửa quy trình, báo sau | sửa đúng chỗ và sửa skill, render lại toàn bộ, giao lại |
| B14 | intro thương hiệu DAVID TRẦN, đoạn mở đầu kênh, thay cảnh mới vào intro | [intro-thuong-hieu.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/intro-thuong-hieu.md) | không có Đ1: chữ, độ dài, khung, logo, nguồn nhạc theo mặc định của quy trình; góp ý sau giao: B13 | bản ngang 1920×1080, 10–13 giây kể cả 2 giây nhạc nhỏ dần, ở Chờ đăng và Drive kèm ghi nguồn nhạc, khoảng −14 LUFS, cảnh đẹp nhất, không lộ logo, tên hiện đúng chữ then chốt của câu hát trọn vẹn |

### C. Trang web, trình duyệt
| Lá | Việc (David hay nói) | Quy trình | Điểm duyệt | Xong khi |
|---|---|---|---|---|
| C1 | làm trang cuộn, trang giới thiệu | [thiet-ke-trang-cuon](ky-nang/thiet-ke-trang-cuon/SKILL.md) | không có Đ1; Bước 0 chỉ hỏi phần brief còn thiếu mà chỉ David đưa được | theo mục "Xong khi" của skill |
| C2 | điều khiển trình duyệt, thử trang web | [dieu-khien-trinh-duyet](ky-nang/dieu-khien-trinh-duyet/SKILL.md) | Đ2 trước khi gửi biểu mẫu, xoá, nhập dữ liệu cá nhân; không đăng bài | theo mục "Xong khi" của skill |

### D. Hướng tài chính
Nhánh này chưa có việc nào. Việc đầu tiên đi theo mục 2 (chưa có lá nên làm theo gốc, qua Đ1, xong thì viết thành lá D1 để lần sau tự động).

### Chỉ Mac chính (repo riêng `bo-nao-david-mac`, không có ở thiết bị khác)
Gom và đóng thành sản phẩm (`ky-nang/san-pham-hoa/SKILL.md`) · tổng hợp tin nhắn 7:00 sáng (`ky-nang/tong-hop-tin-nhan/SKILL.md`) ·
bot Telegram, lịch tự chạy (`tu-dong-hoa/so-tay/`, `tu-dong-hoa/lich/`).
