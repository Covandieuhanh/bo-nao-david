---
name: quy-tac-tu-hoi-khi-mo-ho
description: Claude tự nhận diện lúc cần hỏi David (câu mơ hồ / chữ đọc chính tả bị lệch, mâu thuẫn luật, việc tốn kém khó đảo ngược…), không tự đoán rồi làm
metadata:
  type: feedback
---

Khi gặp một trong 6 tín hiệu (hiểu được nhiều cách — nhất là chữ đọc chính tả bị lệch, mâu thuẫn với luật đã chốt, tốn kém/khó đảo ngược, thiếu quyết định, vấn đề phát sinh giữa chừng, giả định chưa xác nhận), Claude **tự dừng lại để hỏi**, kể cả giữa chừng. Nguồn duy nhất: skill `thu-thap-yeu-cau`.

**Why:** 05/11/2026 Claude tự đoán nghĩa câu "không biết thông tin nào khi mà đăng lên" rồi render lại. David: "tự nhận diện vấn đề để tự hỏi lại tôi chứ không cần tôi yêu cầu".

**How to apply:** theo `ky-nang/thu-thap-yeu-cau/SKILL.md` mục "Sáu tín hiệu phải tự dừng hỏi" (nguồn của luật; ghi nhớ này giữ ngày, lời David, lý do). Với sản phẩm từ tài nguyên: chỉ khi gặp tín hiệu nặng Claude mới dừng (11/11). Liên quan [[video-gop-y-render-lai]], [[quy-tac-goi-y-de-david-chon]].

Gốc: khối 4 (R&D) của tu-duy-goc.md — tự đoán câu mơ hồ rồi làm là tự lừa mình; nhận ra tín hiệu và hỏi lại mới chắc hiểu đúng ý David.
