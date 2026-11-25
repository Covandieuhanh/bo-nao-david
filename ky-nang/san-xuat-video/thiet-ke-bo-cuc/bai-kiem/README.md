---
description: "Bài kiểm suy luận dựng video: 10 đoạn từ hình mẫu, AI máy mới tự làm rồi chấm bằng cham.py (≥ 8/10 là lập luận được); chạy khi cài máy mới và mỗi lần đổi luật dựng."
---

# Bài kiểm suy luận dựng video

Đo xem một AI (ở máy nào cũng vậy) **đọc file rồi có tự lập luận đúng** cách dựng không. Đề: [de.json](de.json), 10 đoạn diễn ý từ các
hình mẫu ở [giai-mau.md](../giai-mau.md) (không trùng các trường hợp đã giải). Chấm: [cham.py](cham.py).

## Khi nào chạy
- Máy mới, sau `tu-dong-hoa/may-khac/kiem-may.sh` (máy công cụ) — bài này kiểm phần **suy nghĩ**.
- Mỗi lần sửa `nguoi-xem-can-gi.md`, `tu-chon.md`, `giai-mau.md`.

## Cách làm (AI tự làm, không hỏi)
1. Đọc `../nguoi-xem-can-gi.md`, `../tu-chon.md` (bảng 4c), `../giai-mau.md`. **Không mở `dap_an` trong de.json** khi làm bài.
2. Với mỗi đoạn trong `de.json` (đọc `id`, `loai`, `khung`, `doan`), viết một dòng vào `bai-lam.json`:
   `{"id": "d01", "can": "<tên nguyên lý ở nguyen-ly.json>", "lam": "<cách làm: tên kiểu trong kho, hoặc 'giữ người' / 'cảnh thật' / 'cắt chờ'>", "vi": "<cái khó của người xem>"}`.
3. Chấm: `python3 -I cham.py bai-lam.json` → mỗi đoạn ✓ / ✗ kèm lý do; **đạt ít nhất 8/10** = máy này lập luận được.
4. Chưa đạt thì đọc lại `giai-mau.md` phần "Rút ra theo loại", làm lại một lần; vẫn chưa đạt thì gửi các đoạn ✗ (kèm dòng `vi`) cho David chấm.
   David thấy đáp án sai thì sửa `de.json` (đáp án là cách nghĩ, không phải chân lý).
5. **Bộ kiểm lớn dần:** lỗi dựng nào David phải sửa (sai nguyên lý, sai cách thể hiện) thì thêm một đoạn vào `de.json` từ chính trường hợp đó
   (trục `co-so-tri-thuc/truc-tri-thuc.md` mục 4). Không bỏ đoạn cũ khi chưa ghi lý do vào sổ.

Thử công cụ chấm: `python3 -I cham.py --mau > /tmp/mau.json && python3 -I cham.py /tmp/mau.json` phải ra 10/10.
