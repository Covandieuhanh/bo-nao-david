---
name: hoc-video-mau
description: Học cách trình bày từ một video mẫu David gửi (link YouTube/TikTok hoặc file) để BỔ SUNG vào bộ skill dựng video — chỉ học bố cục, thứ tự hiện, cách nối cảnh, nhịp, hiệu ứng âm thanh; GIỮ NGUYÊN thẩm mỹ, bố cục và thành phần đang có của David. Ra phiếu học cho David duyệt trước khi sửa skill, rồi kiểm không phá (mặt, phụ đề, dấu góc, thanh thời gian, cả khung ngang và dọc). Dùng khi David gửi video và nói "học cái này", "học video này", "học mẫu này", "học cách họ làm", "học bố cục", "học hiệu ứng", "/hoc-video-mau" — kể cả khi chỉ gửi link kèm chữ "học".
---

# Học video mẫu

Skill này chỉ là **cửa vào**. Toàn bộ luật và quy trình nằm ở `../trinh-bay/README.md` (mục 4) — đọc file đó trước rồi làm theo
đúng thứ tự. Không ghi luật riêng ở đây để chỉ có một chỗ phải sửa.

## Ba điều không được quên
1. **Học là bổ sung, không thay thế** (bộ nhớ `luat-hoc-la-bo-sung`). Không đổi màu, font, nét vẽ, kiểu chuyển động, nhạc kênh.
   Không xoá hay sửa nghĩa thành phần cũ.
2. **Phiếu học trước, sửa skill sau.** Điền `../trinh-bay/phieu-hoc-mau.md` thành `../trinh-bay/nguon-hoc/<ten-nguon>-<ngay>.md`,
   gửi David. Chờ "ok". Đây là cổng hỏi của skill `hoi-chuyen-gia` cho việc này.
3. **Kiểm không phá** trước khi dùng vào video thật: chụp đủ lớp ở cả khung ngang lẫn dọc, phần cũ phải y nguyên.

## Đọc kèm
- `../trinh-bay/bo-cuc.md`, `../trinh-bay/am-thanh.md`: kho đã có, để biết điều mới có trùng cái cũ không.
- `../luat-chung.md`, `../video-style-edit/references/gotchas.md`: các chặn cũ phải giữ.
- `../trinh-bay/nguon-hoc/`: các nguồn đã học (ví dụ `sang-huynh-claude-motion-2026-11-07.md`).

## Xong khi
- Phiếu học đã được David duyệt và nằm trong `nguon-hoc/`.
- Danh mục `bo-cuc.md` / `am-thanh.md` có dòng mới, ghi rõ "đã có code" hay "chưa có code".
- Ảnh kiểm không phá (ngang + dọc) đã xem. Đã đẩy GitHub (`bash scripts/sync.sh --push`).
- Báo David: thêm gì, đã kiểm gì, chưa kiểm gì.
