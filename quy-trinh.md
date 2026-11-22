---
description: "Cây quy trình của bộ não — việc gì cũng đi từ quy trình gốc, xuống nhánh, tới quy trình lá; bảng tra duy nhất: câu David hay nói, quy trình, xong khi."
---

# Cây quy trình — việc gì cũng có quy trình, đi từ gốc lên

Mọi phiên, mọi máy, mọi AI làm cùng một đường để ra cùng một kết quả: đi từ **gốc** (cách làm mọi việc), lên **nhánh** (một mảng việc),
tới **lá** (một việc cụ thể, có file quy trình và tiêu chí xong). Đây là bảng tra duy nhất; `AGENTS.md`, `huong-dan-cho-ai.md` chỉ trỏ về đây.

## 0. Gốc — mọi việc đều đi đủ 7 bước

| # | Bước | Làm theo |
|---|---|---|
| 1 | **Nhận yêu cầu, tra cây:** tìm lá khớp ở mục 2 (David chỉ gửi video / ghi âm không kèm lời thì là lá B1) | file này |
| 2 | **Đọc đúng phần cần:** file quy trình của lá → chỉ những khối, hồ sơ bước đang làm cần; đặt Mục tiêu + Xong khi | `ky-nang/chuan-muc-lam-viec.md` mục 1 |
| 3 | **Trình 4 phần, chờ "duyệt"** (trừ phần miễn: hỏi nhanh, tra cứu, lịch tự chạy đã duyệt) | `chuan-muc-lam-viec.md` mục 2 · `ky-nang/thu-thap-yeu-cau/SKILL.md` |
| 4 | **Làm trọn theo đúng các bước của lá**, một mạch, không dừng giữa chừng trừ tín hiệu nặng | file quy trình của lá · `chuan-muc-lam-viec.md` mục 3 |
| 5 | **Tự soát** theo "Xong khi" của lá, gồm câu "một phiên mới chỉ đọc GitHub có làm ra đúng kết quả này không?" | `chuan-muc-lam-viec.md` mục 4 |
| 6 | **Giao kết quả + báo cáo ngắn:** đã làm gì · đã kiểm gì · chưa kiểm gì · cần David xác nhận gì | lá A6 · `chuan-muc-lam-viec.md` mục 4 |
| 7 | **Ghi lại, đẩy GitHub:** góp ý sửa đúng một chỗ + nhật ký, việc mới thì viết thành lá (mục 1), `bash tu-dong-hoa/dong-bo.sh --push` | `chuan-muc-lam-viec.md` mục 4 · `AGENTS.md` luật 6 |

## 1. Việc chưa có lá trong cây

Làm theo gốc với khung lá dưới đây; xong việc, **trước khi báo xong**, viết cách vừa làm thành một lá (file quy trình đặt đúng nhánh, script
dùng ra kết quả đưa vào repo) và thêm một dòng vào mục 2 — cách viết thành skill: `ky-nang/hoc-lien-tuc/SKILL.md` Việc 3. Lần sau việc đó
đã có quy trình, phiên nào cũng làm giống nhau.

**Khung một quy trình lá** (mọi file quy trình có đủ): **Khi nào dùng** · **Đầu vào** · **Các bước** (lệnh, script có trong repo, không
ghi cứng công cụ chỉ một máy có) · **Xong khi** (đo được) · **Kiểm gì** · **Lỗi hay gặp** (nếu có). Máy kiểm
`tu-dong-hoa/kiem-quy-trinh.py` chạy mỗi lần đẩy GitHub: mọi lá trỏ tới file có thật và có "Xong khi", mọi `SKILL.md` có mục "Xong khi".

## 2. Nhánh và lá

### A. Bộ não (cách làm việc, lưu, đồng bộ, học)
| Lá | Việc (David hay nói) | Quy trình | Xong khi |
|---|---|---|---|
| A1 | "cập nhật não", đẩy / kéo GitHub | [AGENTS.md luật 6](AGENTS.md) · `tu-dong-hoa/dong-bo.sh` | lệnh báo "Đã đẩy lên GitHub", `git status` sạch |
| A2 | cài bộ não lên máy mới (Mac, Windows qua WSL, Linux) | [huong-dan-cai-dat.md](huong-dan-cai-dat.md) · [tu-dong-hoa/may-khac/README.md](tu-dong-hoa/may-khac/README.md) | `kiem-may.sh` ra "MÁY NÀY DỰNG GIỐNG MAC CHÍNH" |
| A3 | "nhìn lại tuần", "tự học", "học từ kênh X", "học cái này thành quy trình" | [ky-nang/hoc-lien-tuc/SKILL.md](ky-nang/hoc-lien-tuc/SKILL.md) | theo mục "Xong khi" của skill |
| A4 | "nâng cấp", "tái bản", luật chồng chéo, gom luật trùng | [hoc-lien-tuc Việc 4](ky-nang/hoc-lien-tuc/SKILL.md) · [ky-nang/tai-cau-truc/SKILL.md](ky-nang/tai-cau-truc/SKILL.md) | `do-chong-cheo.py` dưới ngưỡng mọi bộ, bản luật không còn câu trùng / ngược |
| A5 | học, sửa, lưu thông tin mới vào bộ não (ghi nhớ, kiến thức, hồ sơ) | [co-so-tri-thuc/truc-tri-thuc.md](co-so-tri-thuc/truc-tri-thuc.md) · [quy ước liên kết](co-so-tri-thuc/quy-uoc-lien-ket.md) | ý ở đúng một nhà, có dòng ở `ban-do/`, máy kiểm link đạt |
| A6 | giao kết quả cho David | [phan-phoi-da-kenh bước 5](ky-nang/san-xuat-video/phan-phoi-da-kenh/SKILL.md) | bản cuối ở nơi giao của máy (Mac: trang Chờ đăng + Drive; máy chỉ dựng video: Drive); David theo dõi từ xa thì gửi thêm bản nhẹ dưới 30 MB qua tệp đính kèm |
| A7 | hỏi lại khi chưa rõ yêu cầu, trình 4 phần | [ky-nang/thu-thap-yeu-cau/SKILL.md](ky-nang/thu-thap-yeu-cau/SKILL.md) | theo mục "Xong khi" của skill |

### B. Sản xuất video (gốc nhánh: `phan-phoi-da-kenh` — một tài nguyên vào, đủ bản dài, clip, bài đăng ra)
| Lá | Việc (David hay nói) | Quy trình | Xong khi |
|---|---|---|---|
| B1 | gửi video / ghi âm (có hay không kèm lời), "làm video này", "đăng bài" | [phan-phoi-da-kenh](ky-nang/san-xuat-video/phan-phoi-da-kenh/SKILL.md) | theo mục "Xong khi" của skill |
| B2 | gửi link Drive / YouTube / file / thư mục | [nhan-tai-nguyen.md](ky-nang/san-xuat-video/phan-phoi-da-kenh/references/nhan-tai-nguyen.md) | file gốc ở `~/Movies/tap-<tên>/1-goc/`, đọc được khung, độ dài, tiếng |
| B3 | lọc có đáng làm không, phân theo ba hướng nghề, ghi nhật ký nội dung | [khối 00 mục 0b](ky-nang/san-xuat-video/mo-dun/00-sang-loc-noi-dung/README.md) | có `phan-huong.md` của tập + mục nhật ký từng hướng có ý |
| B4 | "cắt đoạn thừa, tách thành các video theo hướng công việc" | [tach-theo-huong.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/tach-theo-huong.md) | mỗi hướng một dự án dựng xong + gói phát hành |
| B5 | "render một đoạn ngắn cho tôi xem trước" | [doan-thu.md](ky-nang/san-xuat-video/dung-video-theo-phong-cach/references/doan-thu.md) | David nhận đoạn thử, nói duyệt hay sửa trước khi dựng cả video |
| B6 | dựng video tự quay (một video, nhiều file một buổi), ghép vlog | [dung-video-theo-phong-cach](ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md) | theo mục "Xong khi" của skill |
| B7 | podcast / ghi âm thành video đồ hoạ | [dung-podcast](ky-nang/san-xuat-video/dung-podcast/SKILL.md) | theo mục "Xong khi" của skill |
| B8 | cắt highlight, clip ngắn | [cat-doan-noi-bat](ky-nang/san-xuat-video/cat-doan-noi-bat/SKILL.md) | theo mục "Xong khi" của skill |
| B9 | học cách trình bày từ video mẫu David gửi | [phan-tich-video-mau](ky-nang/san-xuat-video/phan-tich-video-mau/SKILL.md) | theo mục "Xong khi" của skill |
| B10 | tiêu đề, mô tả, chương, teaser, bài đăng theo giọng David | [khối 15](ky-nang/san-xuat-video/mo-dun/15-xuat-ban/README.md) · [giọng David](ky-nang/san-xuat-video/ho-so-thuong-hieu/giong-thuong-hieu-david.md) | `phat-hanh/phat-hanh.md` đủ mục, đúng giọng, chữ nguyên văn lời David |
| B11 | "đăng" | [khối 19](ky-nang/san-xuat-video/mo-dun/19-dang-bai/README.md) | đăng đúng bản David bảo, có ảnh chụp xác nhận, sổ danh mục ghi link |
| B12 | số liệu sau 24 giờ / 7 ngày, hộp thư | [khối 20](ky-nang/san-xuat-video/mo-dun/20-hop-thu-so-lieu/README.md) · [khối 16](ky-nang/san-xuat-video/mo-dun/16-phan-tich-so-lieu/README.md) | `so-lieu.md` cập nhật + 1–3 đề xuất |
| B13 | góp ý trên video đã dựng ("cảnh 2:08 chữ to quá", "bỏ cảnh X") | [dung-video-theo-phong-cach mục "Sửa theo góp ý"](ky-nang/san-xuat-video/dung-video-theo-phong-cach/SKILL.md) | sửa đúng chỗ + skill, render lại toàn bộ, giao lại |

### C. Trang web, trình duyệt
| Lá | Việc (David hay nói) | Quy trình | Xong khi |
|---|---|---|---|
| C1 | làm trang cuộn, trang giới thiệu | [thiet-ke-trang-cuon](ky-nang/thiet-ke-trang-cuon/SKILL.md) | theo mục "Xong khi" của skill |
| C2 | điều khiển trình duyệt, thử trang web | [dieu-khien-trinh-duyet](ky-nang/dieu-khien-trinh-duyet/SKILL.md) | theo mục "Xong khi" của skill |

### D. Hướng tài chính
Chưa có việc nào. Việc đầu tiên đi theo mục 1 (làm theo gốc, xong viết thành lá D1).

### Chỉ Mac chính (repo riêng `bo-nao-david-mac`, không có ở máy khác)
Gom và đóng thành sản phẩm (`ky-nang/san-pham-hoa/SKILL.md`) · tổng hợp tin nhắn 7:00 sáng (`ky-nang/tong-hop-tin-nhan/SKILL.md`) ·
bot Telegram, lịch tự chạy (`tu-dong-hoa/so-tay/`, `tu-dong-hoa/lich/`).
