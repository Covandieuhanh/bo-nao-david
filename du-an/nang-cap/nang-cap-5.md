---
description: "Nâng cấp 5 (20/11/2026): trục tri thức, gắn tầng cho mọi file, bộ kiểm toàn bộ não từ chính lời David đã sửa, luật viết đủ từ, chưng cất ghi nhớ; đo trước và sau bằng trí tuệ nhân tạo chưa đọc gì."
---

# Nâng cấp 5 — 20/11/2026

Làm theo trục [co-so-tri-thuc/truc-tri-thuc.md](../../co-so-tri-thuc/truc-tri-thuc.md) và vòng Nâng cấp ([ky-nang/hoc-lien-tuc/SKILL.md](../../ky-nang/hoc-lien-tuc/SKILL.md) Việc 4).
Mốc trước: tag `nang-cap-5-truoc`. David duyệt 4 phần với ba đề xuất: gắn nhãn tầng, không dời file · một trí tuệ nhân tạo con chưa đọc gì
làm bài ngay trong phiên · chuyển phần định hướng nghề cũ của hồ sơ cá nhân sang lưu trữ.

Lời David khi duyệt (luật mới, đưa vào ngay đợt này): *"bộ não hay bất kì cái gì tương tác với tôi đều phải sử dụng từ ngữ đầy đủ … nếu
file này đột ngột cho bất kì ai đọc hay ai nào đọc thì cũng phải hiểu, không được phép lấy bất kì ai … làm tiêu chuẩn để viết tắt hay viết ngắn lại"*.

## 1. Đã làm
| Bước | Việc | File |
|---|---|---|
| Bộ đánh giá | Bộ kiểm toàn bộ não: 16 tình huống, mỗi câu từ một lần David đã sửa hoặc một luật David đã chốt; câu hỏi và đáp án tách hai file; công cụ chấm | `co-so-tri-thuc/bai-kiem/` |
| Luật mới | Viết đủ từ, đủ nghĩa, không viết tắt: sáu luật (luật 1), tóm ở chỉ dẫn toàn cục, trục mục 0, ghi nhớ `quy-tac-viet-du-tu` | `AGENTS.md`, `co-so-tri-thuc/chi-dan-toan-cuc.md` |
| Áp luật mới | 109 file: "vd." → "ví dụ" (26 chỗ), "TB" → "trung bình" (5), "&" giữa chữ tiếng Việt → "và" (7), "~số" → "khoảng số" (195), "≥" → "ít nhất" (101), "≤" → "tối đa" (121); không đụng code, tên riêng, đường dẫn | toàn bộ `.md` |
| Công cụ đo | Thêm chỉ số `viet_tat` (ngưỡng 0); bỏ qua file tầng 3 khi đo "mỗi ý một nguồn duy nhất" | `ky-nang/tai-cau-truc/do-chong-cheo.py`, `bo.json` |
| Gắn tầng | Bảng mẫu đường dẫn → tầng (không thêm dòng vào đầu file: phần đầu `SKILL.md` là chỗ Claude nhận skill, thêm khoá lạ dễ hỏng việc nạp skill). Kết quả: tầng 0 có 7 file, tầng 1 có 10, tầng 2 có 86, tầng 3 có 149. Chỉ mục hiện tầng từng file | `co-so-tri-thuc/tang.json`, `tu-dong-hoa/lien-ket/kiem-tra-lien-ket.py` |
| Chưng cất (sửa chỗ dạy chưa rõ) | Bài kiểm video đo trước sai đoạn d04: ranh giới "Biết trước" và "Báo hiệu" chưa rõ → viết rõ ở nguồn của nguyên lý | `ky-nang/san-xuat-video/thiet-ke-bo-cuc/nguoi-xem-can-gi.md` |
| Chưng cất ghi nhớ | 20 đường dẫn viết tắt trong ghi nhớ đổi thành đường dẫn đầy đủ từ gốc bộ não; 3 ghi nhớ chưa trỏ về nguồn nào được thêm dòng "Nguồn của luật" | `co-so-tri-thuc/bo-nho/` |
| Gom sổ | 12 sổ của các đợt tái bản 1–4 vào `du-an/nang-cap/` (đổi `tai-ban-4.md` thành `nang-cap-4.md`), sửa mọi đường nối | `du-an/nang-cap/` |
| Hồ sơ cá nhân | Mục "Nghề nghiệp" và "Định hướng hình tượng cốt lõi" (đã lỗi thời so với ba hướng nghề) chuyển sang lưu trữ; phần tính cách, năng lực giữ nguyên | `co-so-tri-thuc/ho-so-ca-nhan.md`, `co-so-tri-thuc/luu-tru/ho-so-ca-nhan-dinh-huong-nghe-cu.md` |

**Tỉa (chỉ đề xuất, không bỏ gì):** máy đếm báo 8 skill không dùng trong 30 ngày (cắt đoạn nổi bật, podcast, điều khiển trình duyệt,
học liên tục, sản phẩm hoá, tái cấu trúc, thiết kế trang cuộn, tổng hợp tin nhắn). Một số chạy theo lịch hoặc vừa được dùng trong phiên này
mà máy đếm không thấy, nên máy đếm đang đếm thiếu — cần sửa máy đếm trước khi dựa vào nó để tỉa.

## 2. Thước đo trước và sau
Đo bằng trí tuệ nhân tạo con chưa đọc gì: lần 1 đọc bản chụp ở mốc `nang-cap-5-truoc`, lần 2 đọc bản sau khi sửa (đáp án đã gỡ khỏi bản chụp).

| # | Thước | Trước | Sau |
|---|---|---|---|
| 1 | Người xem thật | chưa đo: trên máy chưa có `so-lieu.md` nào | chưa đo (giả thuyết: bộ não dễ hiểu hơn → David phải sửa ít hơn; đo lại sau 10 video có số liệu) |
| 2a | Bài kiểm toàn bộ não (16 câu) | 16/16, nhưng 2 câu người làm bài phải tự suy vì file chưa nói rõ (c05 tên file, c06 viết tắt) | 16/16, không câu nào thiếu thông tin |
| 2b | Bài kiểm dựng video (10 đoạn) | 9/10 (sai d04: lẫn "Biết trước" với "Báo hiệu") | 10/10 |
| 3 | Hình mẫu chuẩn | không chạy được: 5 dự án mẫu không còn trên máy | không đổi dòng code dựng nào, nên hình không thể đổi; `kiem-mau.py` vẫn cần kéo dự án mẫu về |
| 4 | David phải sửa | 31/94 phiên có lời sửa | đo ở lần nhìn lại tuần sau |
| 5 | Trùng / rối (công cụ đo) | video 16/30, hỏi 0, não 2/6; chưa đo viết tắt | video 16/30, hỏi 0, não 1/6; viết tắt 0 ở cả ba bộ → "Chưa cần nâng cấp" |

Bằng hoặc tốt hơn ở mọi thước đã đo được nên ra bản `nang-cap-5`.

## 3. Bài học cho đợt sau
- Bài kiểm toàn bộ não đạt tối đa ngay từ lần đầu thì câu còn dễ. Đợt sau thêm câu khó hơn từ chính lỗi David sửa (luật thăng cấp, trục mục 4).
- Người làm bài lần 2 nhận xét luật "không làm bản cho CapCut / DaVinci" nằm ở skill dựng và tổng quan, chưa có trong luật chung — xem xét ở bước chưng cất đợt sau.
- Ký hiệu "→" (21/11, David chốt "Giữ trong bảng, câu viết chữ"): giữ trong bảng và chuỗi bước; trong câu văn đã đổi thành chữ theo nghĩa từng chỗ ("thì", "nên", "thành", "sang", "rồi"), khoảng 800 chỗ tự động có kiểm và 415 chỗ đọc từng câu. Công cụ đo thêm chỉ số `mui_ten` (ngưỡng 0); đo lại: cả ba bộ 0, "Chưa cần nâng cấp"; hai bài kiểm vẫn 16/16 và 10/10.
