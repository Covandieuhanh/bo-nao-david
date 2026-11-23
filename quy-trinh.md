---
description: "Cây quy trình của bộ não — việc gì cũng đi từ quy trình gốc, xuống nhánh, tới quy trình lá; bảng tra duy nhất: câu David hay nói, quy trình, điểm duyệt, xong khi."
---

# Cây quy trình — việc gì cũng có quy trình, đi từ gốc lên

Cách **nghĩ** trong mọi bước (bóc tách, vòng kết quả hoặc vấn đề, học và thay đổi, kiểm sai): [tu-duy-goc.md](co-so-tri-thuc/tu-duy-goc.md)
(mục 5 chỉ khối nào dùng ở bước nào). Mọi phiên, mọi máy, mọi AI làm cùng một đường để ra cùng một kết quả: đi từ **gốc** (cách làm mọi việc), lên **nhánh** (một mảng việc),
tới **lá** (một việc cụ thể, có file quy trình, điểm duyệt và tiêu chí xong). Đây là bảng tra duy nhất; `AGENTS.md`, `huong-dan-cho-ai.md`
chỉ trỏ về đây.

## 0. Gốc — mọi việc đều đi đủ 7 bước

| # | Bước | Làm theo |
|---|---|---|
| 1 | **Nhận yêu cầu, tra cây:** tìm lá khớp ở mục 3 (David chỉ gửi video / ghi âm không kèm lời thì là lá B1); xem lời David có bật chế độ tự chạy không (mục 1) | file này |
| 2 | **Đọc đúng phần cần, tra hình mẫu:** tra [bản đồ hình mẫu](co-so-tri-thuc/hinh-mau/README.md) cho mục nhỏ của việc; chưa có hoặc chưa đủ (ít nhất 5, việc lớn 10) thì nghiên cứu theo lá A8 trước Đ1, kết luận đưa vào 4 phần; file quy trình của lá → chỉ những khối, hồ sơ bước đang làm cần; đặt Mục tiêu + Xong khi; được làm phần chuẩn bị (mục 1). Máy chưa từng dựng video (chưa có `kiem-may.sh` đạt và bài kiểm suy luận ≥ 8/10) thì làm lá A2 trước khi dựng thật | `ky-nang/chuan-muc-lam-viec.md` mục 1 |
| 3 | **Điểm duyệt Đ1: trình 4 phần, dừng chờ "duyệt"** (trừ phần miễn và chế độ tự chạy, mục 1) | `chuan-muc-lam-viec.md` mục 2 · `ky-nang/thu-thap-yeu-cau/SKILL.md` |
| 4 | **Làm đúng từng bước của lá theo thứ tự**, một mạch, không thêm, không bớt, không đổi bước; tới điểm duyệt của lá thì dừng chờ. Ra vấn đề: ở cách làm thì xử lý ngay; ở giả định của kế hoạch thì dừng, trình lại kế hoạch (`tu-duy-goc.md` khối 2) | file quy trình của lá · `chuan-muc-lam-viec.md` mục 3 |
| 5 | **Tự soát** theo "Xong khi" của lá, gồm câu "một phiên mới chỉ đọc GitHub có làm ra đúng kết quả này không?" | `chuan-muc-lam-viec.md` mục 4 |
| 6 | **Giao kết quả + báo cáo ngắn:** đã làm gì · đã kiểm gì · chưa kiểm gì · cần David xác nhận gì · có chạy chế độ tự chạy không · 2–3 dòng so với hình mẫu (giống ở đâu, khác ở đâu, nên chỉnh gì) | lá A6 · `chuan-muc-lam-viec.md` mục 4 |
| 7 | **Ghi lại, đẩy GitHub:** góp ý sửa đúng một chỗ + nhật ký, việc mới thì viết thành lá (mục 2), `bash tu-dong-hoa/dong-bo.sh --push` | `chuan-muc-lam-viec.md` mục 4 · `AGENTS.md` luật 6 |

## 1. Điểm duyệt, chế độ tự chạy, không lệch quy trình

**Ba điểm duyệt** (mỗi lá ghi rõ mình dừng ở điểm nào, mục 3):
- **Đ1 — duyệt 4 phần trước khi làm.** Trước Đ1 chỉ được làm **phần chuẩn bị**, không thay đổi gì của David hay của bộ não: đọc, tải tài
  nguyên về thư mục dự án, chép lời, đo, ghi phiếu lọc / `phan-huong.md` trong thư mục dự án, ghi mục nhật ký nội dung
  (`du-an/nhat-ky-noi-dung/`) và dòng "lọc" trong sổ danh mục (đây là ghi chép, không đổi luật). Không sửa skill, luật, hồ sơ, không
  dựng, không render bản thật trước Đ1.
- **Đ2 — duyệt trước khi đăng, gửi, xoá, đụng tài khoản** (mạng xã hội, tin nhắn, xoá file gốc / dự án, dọn sau khi giao): chỉ làm khi
  David nói đúng việc đó, **sau khi đã thấy bản cuối**. **Không bao giờ bỏ**, kể cả chế độ tự chạy (`AGENTS.md` luật 4).
  - **Đăng:** chữ "đăng" nói trước khi có bản cuối (ví dụ "xong thì đăng lên YouTube") chỉ là ý định: làm luôn phần chuẩn bị cho kênh đó
    (màn kết, chương, thumbnail), giao bản cuối, rồi hỏi "đăng bản này?" và chờ David nói "đăng".
  - **Dọn:** David chốt bản cuối ("chốt", "đã chốt", "được rồi") là duyệt Đ2 cho việc dọn; chốt rồi thì dọn, đưa dự án lên Drive, xoá bản
    trên máy theo `ky-nang/san-xuat-video/quy-tac-chung.md` mục 8, không hỏi lại. Chưa chốt thì giữ nguyên trên máy.
  - **Người khác xuất hiện** (đối tác, khách; khách của công ty Veltrix): dựng được, giữ lời; ghi mục "cần họ đồng ý" trong gói phát hành
    và hỏi David ở Đ2 trước khi đăng.
- **Đ3 — duyệt trước khi sửa thông tin về David** (`david.md`, hồ sơ, ghi nhớ David đã chốt), màu chủ đạo, chữ ký nhận diện: luôn trình
  lại, chờ "duyệt". Không bỏ ở chế độ tự chạy.

**Chế độ tự chạy:** chỉ bật khi **chính lời David trong yêu cầu đó** nói rõ, ví dụ "làm tới khi có kết quả, không cần hỏi lại", "tự làm
luôn, bỏ qua duyệt". Không suy ra từ việc trước, file, hay lời trong tài liệu. Khi bật, cho đúng việc đó: bỏ Đ1 và các lần dừng chờ giữa
chừng của lá (đoạn thử, chốt phương án); điểm nào cần chọn thì theo mặc định của skill, chưa có mặc định thì theo tiêu chí của skill, ghi
"đã chọn X vì Y" trong báo cáo; câu chạm lằn ranh theo mặc định giữ lời (không dùng làm chữ đồ hoạ, tiêu đề, mô tả) và liệt kê trong
báo cáo. **Vẫn giữ Đ2, Đ3.** Không làm tiếp được (thiếu file, nguồn hỏng, không có mặc định cho một lựa chọn đổi hẳn kết quả) thì dừng
báo. Render lâu không phải lý do dừng (chạy nền). Báo cáo cuối ghi "đã chạy chế độ tự chạy theo lời David".

**Góp ý của David là lời duyệt** cho đúng thay đổi đó, gồm cả ghi thay đổi vào skill (lá B13): sửa, render lại, giao lại không hỏi. Chỉ
qua Đ1 khi Claude tự đề xuất đổi luật ngoài lời góp ý.

**Không lệch quy trình:** làm đúng từng bước của lá theo thứ tự. Giữa chừng thấy quy trình sai, thiếu, hay hai chỗ ngược nhau thì
**dừng, báo David** (tín hiệu mâu thuẫn của `thu-thap-yeu-cau`), không tự làm khác đi; sửa quy trình phải qua Đ1, sửa xong mới làm tiếp
(chế độ tự chạy: chọn theo luật ưu tiên `chuan-muc-lam-viec.md` mục 0, ghi lại để sửa quy trình sau).

## 2. Việc chưa có lá trong cây

Làm theo gốc với khung lá dưới đây (Đ1 vẫn áp); xong việc, **trước khi báo xong**, viết cách vừa làm thành một lá (file quy trình đặt đúng
nhánh, script dùng ra kết quả đưa vào repo) và thêm một dòng vào mục 3 — cách viết thành skill: `ky-nang/hoc-lien-tuc/SKILL.md` Việc 3.
Lần sau việc đó đã có quy trình, phiên nào cũng làm giống nhau.

**Khung một quy trình lá** (mọi file quy trình có đủ): **Khi nào dùng** · **Đầu vào** · **Các bước** (lệnh, script có trong repo, không
ghi cứng công cụ chỉ một máy có) · **Điểm duyệt** (Đ1 / Đ2 / Đ3 ở bước nào, hoặc "không có") · **Xong khi** (đo được) · **Kiểm gì** ·
**Lỗi hay gặp** (nếu có). Máy kiểm `tu-dong-hoa/kiem-quy-trinh.py` chạy mỗi lần đẩy GitHub: mọi lá trỏ tới file có thật, có điểm duyệt và
"Xong khi"; mọi `SKILL.md` dùng chung có mục "Xong khi" và có lá trong cây.

## 3. Nhánh và lá

### A. Bộ não (cách làm việc, lưu, đồng bộ, học)
| Lá | Việc (David hay nói) | Quy trình | Điểm duyệt | Xong khi |
|---|---|---|---|---|
| A1 | "cập nhật não", đẩy / kéo GitHub | [AGENTS.md luật 6](AGENTS.md) · `tu-dong-hoa/dong-bo.sh` | không có (lời David là lệnh) | lệnh báo "Đã đẩy lên GitHub", `git status` sạch |
| A2 | cài bộ não lên máy mới (Mac, Windows qua WSL, Linux) | [huong-dan-cai-dat.md](huong-dan-cai-dat.md) · [tu-dong-hoa/may-khac/README.md](tu-dong-hoa/may-khac/README.md) | Đ1 trước khi cài; mật khẩu máy David tự gõ | `kiem-may.sh` ra "MÁY NÀY DỰNG GIỐNG MAC CHÍNH" |
| A3 | "nhìn lại tuần", "tự học", "học từ kênh X", "học cái này thành quy trình" | [ky-nang/hoc-lien-tuc/SKILL.md](ky-nang/hoc-lien-tuc/SKILL.md) | phân tích không có; Đ1 trước khi sửa skill, giọng văn, luật kênh | theo mục "Xong khi" của skill |
| A4 | "nâng cấp", "tái bản", luật chồng chéo, gom luật trùng | [hoc-lien-tuc Việc 4](ky-nang/hoc-lien-tuc/SKILL.md) · [ky-nang/tai-cau-truc/SKILL.md](ky-nang/tai-cau-truc/SKILL.md) | đo không có; Đ1 trước khi sửa (một bộ 4 phần cho cả đợt) | `do-chong-cheo.py` dưới ngưỡng mọi bộ, bản luật không còn câu trùng / ngược |
| A5 | học, sửa, lưu thông tin mới vào bộ não (ghi nhớ, kiến thức, hồ sơ) | [co-so-tri-thuc/truc-tri-thuc.md](co-so-tri-thuc/truc-tri-thuc.md) · [quy ước liên kết](co-so-tri-thuc/quy-uoc-lien-ket.md) | Đ1; thông tin về David thêm Đ3 | ý ở đúng một nhà, có dòng ở `ban-do/`, máy kiểm link đạt |
| A6 | giao kết quả cho David | [phan-phoi-da-kenh bước 5](ky-nang/san-xuat-video/phan-phoi-da-kenh/SKILL.md) | giao không có; dọn / xoá file tạm, đưa dự án lên Drive: Đ2 (sau khi David chốt) | bản cuối ở nơi giao của máy (Mac: trang Chờ đăng + Drive; máy chỉ dựng video: Drive); David theo dõi từ xa thì gửi thêm bản nhẹ dưới 30 MB qua tệp đính kèm |
| A7 | hỏi lại khi chưa rõ yêu cầu, trình 4 phần | [ky-nang/thu-thap-yeu-cau/SKILL.md](ky-nang/thu-thap-yeu-cau/SKILL.md) | chính là Đ1 | theo mục "Xong khi" của skill |
| A8 | trước mọi việc chưa có đủ hình mẫu; "nghiên cứu hình mẫu", "xem người ta làm thế nào", "học từ người đã thành công" | [co-so-tri-thuc/hinh-mau/quy-trinh-nghien-cuu.md](co-so-tri-thuc/hinh-mau/quy-trinh-nghien-cuu.md) | không có cho phần nghiên cứu, ghi bản đồ (phần chuẩn bị); đưa vào skill, luật: Đ1 của việc chính | mục nhỏ có ít nhất 5 hình mẫu (việc lớn 10) đủ bốn cột, có ngày đo; nhật ký có mục mới; tin giao có 2–3 dòng đối chiếu |

### B. Sản xuất video (gốc nhánh: `phan-phoi-da-kenh` — một tài nguyên vào, đủ bản dài, clip, bài đăng ra)
| Lá | Việc (David hay nói) | Quy trình | Điểm duyệt | Xong khi |
|---|---|---|---|---|
| B1 | gửi video / ghi âm (có hay không kèm lời), "làm video này", "đăng bài" | [phan-phoi-da-kenh](ky-nang/san-xuat-video/phan-phoi-da-kenh/SKILL.md) | Đ1 sau bước 0–1 (nhận, lọc); Đ2 ở bước 7 (đăng) và khi dọn; lá dựng: có hình người nói thì B6, chỉ có tiếng hoặc David gọi là podcast thì B7 | theo mục "Xong khi" của skill |
| B2 | gửi link Drive / YouTube / file / thư mục | [nhan-tai-nguyen.md](ky-nang/san-xuat-video/phan-phoi-da-kenh/references/nhan-tai-nguyen.md) | không có (phần chuẩn bị, trước Đ1) | file gốc ở `~/Movies/tap-<tên>/1-goc/`, đọc được khung, độ dài, tiếng |
| B3 | lọc có đáng làm không, phân theo ba hướng nghề, ghi nhật ký nội dung | [khối 00 mục 0b](ky-nang/san-xuat-video/mo-dun/00-sang-loc-noi-dung/README.md) | không có (phần chuẩn bị); kết quả lọc đưa vào Đ1 của B1 / B4 | có `phan-huong.md` của tập + mục nhật ký từng hướng có ý |
| B4 | "cắt đoạn thừa, tách thành các video theo hướng công việc" | [tach-theo-huong.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/tach-theo-huong.md) | Đ1 sau bước 2 (phân hướng, lằn ranh); Đ2 khi đăng, dọn | mỗi hướng một dự án dựng xong + clip ngắn + gói phát hành, đã giao |
| B5 | "render một đoạn ngắn cho tôi xem trước" | [doan-thu.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/doan-thu.md) | Đ1 trước khi làm; sau bước 6 dừng chờ David duyệt đoạn thử mới dựng cả video | David nhận đoạn thử, nói duyệt hay sửa trước khi dựng cả video |
| B6 | dựng video tự quay (một video, nhiều file một buổi), ghép vlog | [dung-video-theo-phong-cach](ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md) | Đ1 (của B1 nếu đi từ B1); Đ2 khi dọn sau giao | theo mục "Xong khi" của skill |
| B7 | podcast / ghi âm thành video đồ hoạ | [dung-podcast](ky-nang/san-xuat-video/dung-podcast/SKILL.md) | Đ1 (của B1 nếu đi từ B1); Đ2 khi dọn sau giao | theo mục "Xong khi" của skill |
| B8 | cắt highlight, clip ngắn | [cat-doan-noi-bat](ky-nang/san-xuat-video/cat-doan-noi-bat/SKILL.md) | Đ1 (của B1 nếu đi từ B1); Đ2 khi dọn sau giao | theo mục "Xong khi" của skill |
| B9 | học cách trình bày từ video mẫu David gửi | [phan-tich-video-mau](ky-nang/san-xuat-video/phan-tich-video-mau/SKILL.md) | phân tích không có; Đ1 (phiếu học) trước khi sửa skill | theo mục "Xong khi" của skill |
| B10 | tiêu đề, mô tả, chương, teaser, bài đăng theo giọng David | [khối 15](ky-nang/san-xuat-video/mo-dun/15-xuat-ban/README.md) · [giọng David](ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md) | không có riêng (nằm trong việc đã qua Đ1) | `phat-hanh/phat-hanh.md` đủ mục, đúng giọng, chữ nguyên văn lời David |
| B11 | "đăng" | [khối 19](ky-nang/san-xuat-video/mo-dun/19-dang-bai/README.md) | Đ2: chỉ khi David nói "đăng" đúng bản đó, không bao giờ bỏ | đăng đúng bản David bảo, có ảnh chụp xác nhận, sổ danh mục ghi link |
| B12 | số liệu sau 24 giờ / 7 ngày, hộp thư | [khối 20](ky-nang/san-xuat-video/mo-dun/20-hop-thu-so-lieu/README.md) · [khối 16](ky-nang/san-xuat-video/mo-dun/16-phan-tich-so-lieu/README.md) | đọc số liệu không có; trả lời bình luận, tin nhắn: Đ2; sửa skill theo số liệu: Đ1 | `so-lieu.md` cập nhật + 1–3 đề xuất |
| B13 | góp ý trên video đã dựng ("cảnh 2:08 chữ to quá", "bỏ cảnh X") | [dung-video-theo-phong-cach mục "Sửa theo góp ý"](ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md) | không có: góp ý là lời duyệt cho chính thay đổi đó, kể cả ghi vào skill (mục 1); Claude tự đề xuất đổi luật thêm: Đ1 | sửa đúng chỗ + skill, render lại toàn bộ, giao lại |
| B14 | intro thương hiệu DAVID TRẦN, đoạn mở đầu kênh, thay cảnh mới vào intro | [intro-thuong-hieu.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/intro-thuong-hieu.md) | Đ1 trước khi chọn cảnh (chữ, độ dài, khung, logo, nguồn nhạc); góp ý sau giao: B13 | bản ngang 1920×1080, 10–13 giây kể cả 2 giây nhạc nhỏ dần, ở Chờ đăng + Drive kèm ghi nguồn nhạc, khoảng −14 LUFS, cảnh đẹp nhất, không lộ logo, tên hiện đúng chữ đắt của câu hát trọn vẹn |

### C. Trang web, trình duyệt
| Lá | Việc (David hay nói) | Quy trình | Điểm duyệt | Xong khi |
|---|---|---|---|---|
| C1 | làm trang cuộn, trang giới thiệu | [thiet-ke-trang-cuon](ky-nang/thiet-ke-trang-cuon/SKILL.md) | Đ1 sau Step 0 (brief) | theo mục "Xong khi" của skill |
| C2 | điều khiển trình duyệt, thử trang web | [dieu-khien-trinh-duyet](ky-nang/dieu-khien-trinh-duyet/SKILL.md) | Đ1 trước việc; Đ2 trước khi gửi biểu mẫu, đăng, xoá, nhập dữ liệu cá nhân | theo mục "Xong khi" của skill |

### D. Hướng tài chính
Chưa có việc nào. Việc đầu tiên đi theo mục 2 (làm theo gốc, qua Đ1, xong viết thành lá D1).

### Chỉ Mac chính (repo riêng `bo-nao-david-mac`, không có ở máy khác)
Gom và đóng thành sản phẩm (`ky-nang/san-pham-hoa/SKILL.md`) · tổng hợp tin nhắn 7:00 sáng (`ky-nang/tong-hop-tin-nhan/SKILL.md`) ·
bot Telegram, lịch tự chạy (`tu-dong-hoa/so-tay/`, `tu-dong-hoa/lich/`).
