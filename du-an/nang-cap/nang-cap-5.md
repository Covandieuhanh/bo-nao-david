---
description: "Nâng cấp 5 (20/11/2026): trục tri thức, gắn tầng cho mọi file, bộ kiểm toàn bộ não xây từ chính những lần David đã sửa, luật viết đủ từ, chưng cất ghi nhớ; đo trước và sau bằng một trí tuệ nhân tạo chưa đọc gì."
---

# Nâng cấp 5 — 20/11/2026

Claude làm theo trục [co-so-tri-thuc/truc-tri-thuc.md](../../co-so-tri-thuc/truc-tri-thuc.md) và vòng Nâng cấp ([ky-nang/hoc-lien-tuc/SKILL.md](../../ky-nang/hoc-lien-tuc/SKILL.md) Việc 4).
Mốc so sánh trước: tag `nang-cap-5-truoc`. David duyệt 4 phần với ba đề xuất: gắn nhãn tầng, không di chuyển file · một trí tuệ nhân tạo con chưa đọc gì
làm bài ngay trong phiên · chuyển phần định hướng nghề cũ của hồ sơ cá nhân sang lưu trữ.

Lời David khi duyệt (luật mới, áp dụng ngay đợt này): *"bộ não hay bất kì cái gì tương tác với tôi đều phải sử dụng từ ngữ đầy đủ … nếu
file này đột ngột cho bất kì ai đọc hay ai nào đọc thì cũng phải hiểu, không được phép lấy bất kì ai … làm tiêu chuẩn để viết tắt hay viết ngắn lại"*.

## 1. Đã làm
| Bước | Việc | File |
|---|---|---|
| Bộ đánh giá | Bộ kiểm toàn bộ não: 16 tình huống, mỗi câu lấy từ một lần David đã sửa hoặc một luật David đã chốt; câu hỏi và đáp án tách thành hai file; có công cụ chấm | `co-so-tri-thuc/bai-kiem/` |
| Luật mới | Viết đủ từ, đủ nghĩa, không viết tắt: sáu luật (luật 1), tóm tắt ở chỉ dẫn toàn cục, trục mục 0, ghi nhớ `quy-tac-viet-du-tu` | `AGENTS.md`, `co-so-tri-thuc/chi-dan-toan-cuc.md` |
| Áp dụng luật mới | 109 file: "vd." → "ví dụ" (26 chỗ), "TB" → "trung bình" (5), "&" giữa chữ tiếng Việt → "và" (7), "~số" → "khoảng số" (195), "≥" → "ít nhất" (101), "≤" → "tối đa" (121); không sửa code, tên riêng, đường dẫn | toàn bộ `.md` |
| Công cụ đo | Thêm chỉ số `viet_tat` (ngưỡng 0); bỏ qua file tầng 3 khi đo "mỗi ý một nguồn duy nhất" | `ky-nang/tai-cau-truc/do-chong-cheo.py`, `bo.json` |
| Gắn tầng | Bảng mẫu đường dẫn → tầng (không thêm dòng vào đầu file: phần đầu `SKILL.md` là nơi Claude nhận diện skill, thêm khoá lạ dễ làm hỏng việc nạp skill). Kết quả: tầng 0 có 7 file, tầng 1 có 10, tầng 2 có 86, tầng 3 có 149. Chỉ mục hiển thị tầng của từng file | `co-so-tri-thuc/tang.json`, `tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py` |
| Chưng cất (sửa chỗ hướng dẫn chưa rõ) | Bài kiểm video đo trước sai đoạn d04: ranh giới giữa "Biết trước" và "Báo hiệu" chưa rõ → viết rõ ở nguồn của nguyên lý | `ky-nang/san-xuat-video/thiet-ke-bo-cuc/nhu-cau-nguoi-xem.md` |
| Chưng cất ghi nhớ | 20 đường dẫn viết tắt trong ghi nhớ được đổi thành đường dẫn đầy đủ từ gốc bộ não; 3 ghi nhớ chưa trỏ về nguồn nào được thêm dòng "Nguồn của luật" | `co-so-tri-thuc/bo-nho/` |
| Gộp sổ | Gộp 12 sổ của các đợt tái bản 1–4 vào `du-an/nang-cap/` (đổi `tai-ban-4.md` thành `nang-cap-4.md`), sửa mọi liên kết | `du-an/nang-cap/` |
| Hồ sơ cá nhân | Mục "Nghề nghiệp" và "Định hướng hình tượng cốt lõi" (đã lỗi thời so với ba hướng nghề) được chuyển sang lưu trữ; phần tính cách, năng lực giữ nguyên | `co-so-tri-thuc/ho-so-ca-nhan.md`, `co-so-tri-thuc/luu-tru/ho-so-ca-nhan-dinh-huong-nghe-cu.md` |

**Cắt giảm (chỉ đề xuất, không bỏ gì):** công cụ đếm báo 8 skill không được dùng trong 30 ngày (cắt đoạn nổi bật, podcast, điều khiển trình duyệt,
học liên tục, sản phẩm hoá, tái cấu trúc, thiết kế trang cuộn, tổng hợp tin nhắn). Một số skill chạy theo lịch hoặc vừa được dùng trong phiên này
mà công cụ đếm không ghi nhận, nên công cụ đếm đang đếm thiếu — cần sửa công cụ đếm trước khi dựa vào kết quả để cắt giảm.

## 2. Thước đo trước và sau
Đo bằng một trí tuệ nhân tạo con chưa đọc gì: lần 1 đọc bản chụp ở mốc `nang-cap-5-truoc`, lần 2 đọc bản sau khi sửa (đáp án đã được gỡ khỏi bản chụp).

| # | Thước đo | Trước | Sau |
|---|---|---|---|
| 1 | Người xem thực tế | chưa đo: trên máy chưa có `so-lieu.md` nào | chưa đo (giả thuyết: bộ não dễ hiểu hơn → David phải sửa ít hơn; đo lại sau 10 video có số liệu) |
| 2a | Bài kiểm toàn bộ não (16 câu) | 16/16, nhưng có 2 câu người làm bài phải tự suy luận vì file chưa nói rõ (c05 tên file, c06 viết tắt) | 16/16, không câu nào thiếu thông tin |
| 2b | Bài kiểm dựng video (10 đoạn) | 9/10 (sai d04: nhầm "Biết trước" với "Báo hiệu") | 10/10 |
| 3 | Hình mẫu chuẩn | không chạy được: 5 dự án mẫu không còn trên máy | không đổi dòng code dựng nào, nên hình ảnh không thể thay đổi; `kiem-mau.py` vẫn cần tải dự án mẫu về |
| 4 | Số lần David phải sửa | 31/94 phiên có lời sửa | đo ở lần nhìn lại tuần sau |
| 5 | Trùng lặp / chồng chéo (công cụ đo) | video 16/30, hỏi 0, não 2/6; chưa đo viết tắt | video 16/30, hỏi 0, não 1/6; viết tắt 0 ở cả ba bộ → "Chưa cần nâng cấp" |

Kết quả bằng hoặc tốt hơn ở mọi thước đo đã đo được nên Claude ra bản `nang-cap-5`.

## 3. Bài học cho đợt sau
- Bài kiểm toàn bộ não đạt tối đa ngay từ lần đầu nghĩa là các câu còn dễ. Đợt sau cần thêm câu khó hơn từ chính các lỗi David đã sửa (luật thăng cấp, trục mục 4).
- Người làm bài lần 2 nhận xét luật "không làm bản cho CapCut / DaVinci" nằm ở skill dựng và tổng quan, chưa có trong luật chung — cần xem xét ở bước chưng cất đợt sau.
- Ký hiệu "→" (21/11, David chốt "Giữ trong bảng, câu viết chữ"): giữ trong bảng và chuỗi bước; trong câu văn đã đổi thành chữ theo nghĩa của từng vị trí ("thì", "nên", "thành", "sang", "rồi"), khoảng 800 vị trí đổi tự động có kiểm tra và 415 vị trí đọc từng câu. Công cụ đo thêm chỉ số `mui_ten` (ngưỡng 0); đo lại: cả ba bộ đều 0, "Chưa cần nâng cấp"; hai bài kiểm vẫn đạt 16/16 và 10/10.
