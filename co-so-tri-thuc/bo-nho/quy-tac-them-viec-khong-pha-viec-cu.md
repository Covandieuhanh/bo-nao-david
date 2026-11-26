---
name: quy-tac-them-viec-khong-pha-viec-cu
description: Việc / tính năng mới được thêm vào không được làm hỏng việc cũ đang chạy; Claude chỉ sửa phần cũ khi kế hoạch (hoặc lý do sửa quy trình) ghi rõ là sửa phần cũ; mọi thứ phải tự động (19/11/2026)
metadata:
  type: feedback
---

Khi thêm việc mới (tính năng, cờ, thư mục, bước) vào hệ thống đang chạy, **việc cũ phải chạy giống hệt như trước**. Claude chỉ được đổi cách việc cũ chạy khi kế hoạch hoặc lý do sửa quy trình ghi rõ "sửa cả phần cũ". Sau khi sửa, Claude phải **tự thử chính việc cũ** (chạy thật hoặc công cụ tự thử) trước khi coi là xong. Mọi thứ phải tự động, không phụ thuộc vào việc David bấm thủ công.

**Why:** ngày 18/11/2026 Claude thêm thư mục công ty (`--add-dir bo-nao-veltrix`) vào lệnh mở phiên lịch để ghi mục 🏢. Từ đó mọi phiên lịch bị dừng ở hộp thoại hỏi "tin cậy thư mục", không có ai bấm. Hậu quả: ngày 19/11 không có bản tổng hợp tin, việc tổng hợp đêm 18/11 cũng không chạy. David (19/11, việc #30): "mọi thứ phải tự động, những gì đã làm rồi thì sau này có bổ sung thêm việc khác thì cũng không được ảnh hưởng việc cũ chứ, trừ khi có yêu cầu duyệt theo kế hoạch có sửa cả các phần cũ".

**How to apply:**
- Khi sửa script dùng chung (lệnh mở phiên, công cụ giám sát bot, hook), các bước sửa phải có bước "thử lại việc cũ".
- Lệnh mở phiên lịch có công cụ tự thử: `tu-dong-hoa/lich/thu-mo-phien.sh`. Công cụ giám sát bot tự chạy công cụ này mỗi khi `chay-lich.sh` thay đổi; nếu hỏng thì nhắn David.
- Phiên chạy ngầm không được để bị dừng ở hộp thoại hỏi: công cụ giám sát chạy trước giờ của phiên theo lịch 3 phút để phát hiện hộp thoại hỏi (`lich-chay.md`). Bổ sung cho [[quy-tac-hoc-la-bo-sung]], [[quy-tac-duyet-ke-hoach-4-phan]].

Gốc: khối 2 (Hành động) của tu-duy-goc.md — thêm việc mới phải có bước tự thử chính việc cũ trước khi coi là xong, vì một thay đổi nhỏ đã từng làm cả lịch tự chạy đứng.
