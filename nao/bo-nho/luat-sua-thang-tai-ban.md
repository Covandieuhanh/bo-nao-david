---
name: luat-sua-thang-tai-ban
description: "Đổi luật thì sửa thẳng câu cũ (không chồng câu \"bổ sung/thay luật\", không ngày trong bản luật); định kỳ tái bản TOÀN BỘ bộ não một đợt khi máy đo chồng chéo báo (2026-11-10)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 39383a2e-bf70-432e-8fcc-63c950a840d4
  modified: 2026-11-10T12:10:53.688Z
---

Mỗi lần học mẫu, sửa góp ý hay có quyết định mới: viết lại chính câu luật thành trạng thái mới, xoá câu cũ; ngày + lời David + lý do vào sổ quyết định. Khi luật vẫn đã chồng nhiều lớp (máy đo `skills/tai-ban/do_chong_cheo.py` báo "NÊN TÁI BẢN"), nhắc David một dòng; David đồng ý thì tái bản **toàn bộ** một đợt bằng skill `tai-ban`: cả ba bộ (video, hoi, nao) + dọn ghi nhớ, một mốc chung `tai-ban-<n>`, mỗi bộ một phiên con chạy cùng lúc. Một bộ vượt ngưỡng là đủ để tái bản cả đợt.

**Why:** 10/11/2026 David rút kinh nghiệm từ các dự án code bằng Claude: học lớp 1, lớp 2, lớp 3 chồng lên nhau làm AI đọc luật cũ lẫn mới bị rối. Khảo sát cùng ngày thấy bộ video có 165 dấu ngày, 81 câu ghi đè và luật cãi nhau thật (khối 07 "cảnh đầu luôn là hook" vs luat-chung "không thẻ tít mở đầu mặc định"). David chốt 5 điểm: sửa thẳng · máy đo nhắc, David quyết · kiểm mẫu chuẩn + việc thật · skill riêng. Sau tái bản video lần 1 (David chấm "bản mới tốt hơn bản cũ"), David đổi "từng bộ một" thành: "khi tái bản thì cứ tái bản hết toàn bộ mọi thứ để tối ưu nhất" — vì học tài nguyên mới sẽ còn bỏ/đổi luật ở nhiều nơi.

**How to apply:** nhà của luật là `skills/thoi-quen-lam-viec.md` mục 4 và skill `skills/tai-ban/SKILL.md`. Liên quan [[luat-hoc-la-bo-sung]], [[video-hieu-hon-cau-ki]].
