---
description: "Gói 2 trainer dựng bộ não bằng file cho trí tuệ nhân tạo (hướng 3 gói công nghệ): người mới bắt đầu tự tạo cơ sở tri thức cá nhân, học và lưu lại sau mỗi dự án; tổng quan, cấu trúc, các file thành phần."
---

# Gói 2: Trainer dựng bộ não bằng file cho trí tuệ nhân tạo

Gói công nghệ thứ hai của hướng 3 (`co-so-tri-thuc/david.md` mục 4.1), David duyệt 21/11/2026. Quy trình bán hàng: `../pheu-ban-hang-goi-cong-nghe.md`.

**Luật của gói:** gói chỉ dạy **một kỹ năng duy nhất**: dựng và duy trì một cơ sở tri thức cá nhân bằng file, để trí tuệ nhân tạo (gọi tắt trong gói là "AI") đọc là hiểu người dùng và lần sau làm tốt hơn lần trước. Học viên dùng AI nào (ChatGPT, Claude, Gemini…), thiết bị nào cũng làm được. Gói không dạy cách dựng video, cách làm nội dung hay chiến lược kinh doanh. Gói không chứa thông tin chi tiết riêng của David; bộ não của David chỉ là kết quả mẫu để trainer demo.

**Cam kết với khách hàng:** sau gói, học viên có một bộ não bằng file của chính mình. Khi mở một AI mới hoàn toàn và nạp bộ não vào, AI trả lời đúng ít nhất 90% bài kiểm (ít nhất 10 câu) về người đó và cách người đó muốn được làm việc. Mỗi dự án làm xong để lại bài học ở đúng vị trí; lỗi đã sửa một lần trở thành câu kiểm, để AI không lặp lại. Trainer kèm riêng tới khi học viên **tự hoàn thành trọn một vòng học (làm dự án, lưu, kiểm) mà không cần trainer, và bộ não đã trải qua ít nhất 3 dự án thực tế**.

| File | Nội dung |
|---|---|
| [1-quy-trinh.md](1-quy-trinh.md) | cách bộ não hoạt động, bốn tầng, cấu trúc thư mục phẳng, 10 bước dựng và duy trì bộ não, luật an toàn, yêu cầu thiết bị |
| [2-lo-trinh.md](2-lo-trinh.md) | 4 buổi, quy trình cho một học viên, việc trainer chuẩn bị |
| [3-giao-trinh.md](3-giao-trinh.md) | 8 bài |
| [4-phieu-khao-sat-va-nghiem-thu.md](4-phieu-khao-sat-va-nghiem-thu.md) | phiếu khảo sát đầu vào, trước và sau, nghiệm thu |
| [bo-bieu-mau/](bo-bieu-mau/README.md) | từ mới và thao tác thủ công cho người mới bắt đầu, mẫu các file, câu lệnh mẫu, mẫu bài kiểm, danh sách kiểm soát chất lượng |

## Hai mức
| Mức | Cần gì | AI ghi file thế nào |
|---|---|---|
| **Cơ bản** | máy tính; một AI có chức năng Projects (ChatGPT, Claude; trên Gemini gọi là Gems); Google Drive (khuyên dùng) | AI tạo file cho học viên tải về, học viên thay file trong Projects |
| **Nâng cao** | trợ lý AI chạy trên máy (Claude Code, Codex, Gemini CLI) và tài khoản GitHub | AI tự đọc, tự sửa file trong thư mục; GitHub sao lưu và đồng bộ sang thiết bị khác |

Học viên bắt đầu ở mức cơ bản. Học viên chuyển lên mức nâng cao khi thấy thay file thủ công mất thời gian, khi Projects gần đạt giới hạn số file, hoặc khi muốn ghi lại mọi lần sửa.

## Thuật ngữ dùng thống nhất trong gói
| Tiếng Anh | Tiếng Việt | Trong gói là |
|---|---|---|
| Knowledge Base | Cơ sở tri thức | toàn bộ thư mục bộ não của học viên |
| Knowledge Axis | Trục tri thức | file `truc-hoc.md`: cách bộ não nhận, lưu, nâng cấp mọi thông tin; gần như không thay đổi |
| Entry File | File cửa vào | `doc-truoc.md`: AI đọc file này đầu tiên; có bảng mọi file |
| Principle | Nguyên lý | lý do làm như vậy; áp dụng được cho nhiều việc (file `nguyen-ly-<ten>.md`) |
| Procedure | Quy trình | các bước của một loại việc (file `quy-trinh-<ten-viec>.md`) |
| Log | Sổ | ghi theo ngày: đã làm gì, học được gì (`du-an-<ten>.md`, `bai-hoc.md`) |
| Evals | Bài kiểm | `bai-kiem.md` (câu hỏi) và `dap-an.md` (để ngoài bộ não): kiểm tra xem AI mới có hiểu đúng không |
| Cold Reader | Người đọc mới | một AI mới hoàn toàn, chưa biết gì về học viên, chỉ đọc bộ não |
| Distillation | Chưng cất | gộp nhiều bài học cùng gốc thành một nguyên lý |
| Versioned Release | Ra bản có số hiệu | sau mỗi đợt nâng cấp, chỉ giữ phiên bản mới khi bài kiểm bằng hoặc tốt hơn |
| Intake Form | Phiếu khảo sát đầu vào | phần A file 4 |
| Acceptance | Nghiệm thu | phần C file 4 |
| Template Kit | Bộ biểu mẫu | thư mục `bo-bieu-mau/` |

**Chờ David chốt:** giá gói · thời gian kèm cặp tiếp tối đa · bán riêng hay kèm gói 1.
