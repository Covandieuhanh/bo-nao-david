---
description: "Dự án máy gom và đóng gói: mọi nguồn hằng ngày → phân loại theo hướng nghề → sản phẩm bán được; kế hoạch và lịch chạy."
---

# Máy gom và đóng gói: mọi thứ hằng ngày thành sản phẩm bán được

Skill: `ky-nang/san-pham-hoa/SKILL.md` (chỉ Mac chính). Script gom: `tu-dong-hoa/thu-thap-du-lieu/gom.py` (chỉ Mac chính).

## Mục tiêu
Không ý nào, nỗi đau nào, bài học nào bị trôi mất. Mọi thứ phát sinh mỗi ngày (phiên Claude, tin nhắn, việc qua bot, lời trong video,
bài đăng, số liệu) tự được gom, phân loại theo ba hướng nghề (`co-so-tri-thuc/david.md` 4.1) và đổ dần vào **sản phẩm bán được** và **gói có
các bước để trainer lại**.

## Kế hoạch
| Nhịp | Làm gì | Ra gì |
|---|---|---|
| **Mỗi đêm 23:00** | Script gom phần mới (không tốn token) → Claude phân loại | `kho-du-lieu/ngay/<ngày>.md`, thêm dòng vào `nguyen-lieu.md`, cộng `noi-dau.md` |
| **Sáng thứ 6 06:30** (ngày tổng kết tuần) | Claude đóng gói từ nguyên liệu tuần | bổ sung gói đang chạy, bài phễu nháp, đề xuất gói mới khi ít nhất 5 người cùng gặp một nỗi đau, phiếu tuần, tin Telegram |

David chốt 14/11/2026: nhịp đêm + tuần; gói đang chạy tự bổ sung, gói mới chỉ đề xuất khi ít nhất 5 người cùng gặp một nỗi đau (khớp mốc phễu); kho thô chỉ ở máy.

## Quy trình
1. **Gom** (`gom.py`): đọc phần mới kể từ lần trước ở mọi nguồn, ghi một file ngày trong `~/Documents/2-ca-nhan/so-tay/kho-du-lieu/`.
2. **Phân loại** (skill, việc 1): mỗi ý một dòng: hướng · tầng / mục tiêu · nỗi đau · bán được gì · dạng sản phẩm.
3. **Đếm nỗi đau**: cùng một nỗi đau gộp một dòng, đếm số người khác nhau gặp nó.
4. **Đóng gói** (skill, việc 2): nguyên liệu thuộc gói đang chạy → bổ sung bài học, ví dụ, câu hỏi thường gặp; nguyên liệu kể chuyện thật → bài phễu nháp; nỗi đau ít nhất 5 người → phiếu đề xuất gói mới.
5. **Báo** David qua Telegram; David chọn gói mới, duyệt bài trước khi đăng.

## Thực thi
- [x] David duyệt thiết kế (14/11)
- [x] Script gom + skill + lịch đêm và tuần (14/11)
- [x] Chạy thử lượt đầu (14/11)
- [ ] Chạy thử đóng gói lần 1 (CN 15/11 06:30, dòng `chỉ ngày` trong `tu-dong-hoa/lich/lich-chay.md`); lần 2 thứ 6 20/11 06:30
- [ ] Sau 2 tuần: rà xem phân loại có đúng hướng không, nỗi đau nào lên ngưỡng, sửa skill theo `hoc-lien-tuc`
