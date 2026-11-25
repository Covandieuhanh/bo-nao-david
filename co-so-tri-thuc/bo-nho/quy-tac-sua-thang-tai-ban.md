---
name: quy-tac-sua-thang-tai-ban
description: "Đổi luật thì sửa thẳng câu cũ (không chồng câu \"bổ sung/thay luật\", không ngày trong bản luật); định kỳ NÂNG CẤP cả bộ não một đợt (đo trước/sau, chưng cất, cắt giảm, dọn) — 2026-11-10, đổi tên 2026-11-20"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 39383a2e-bf70-432e-8fcc-63c950a840d4
  modified: 2026-11-20T23:30:00.000Z
---

Mỗi lần học mẫu, sửa góp ý hay có quyết định mới: viết lại chính câu luật thành trạng thái mới, xoá câu cũ; ngày + lời David + lý do vào sổ quyết định. Khi luật vẫn đã chồng nhiều lớp (công cụ đo `ky-nang/tai-cau-truc/do-chong-cheo.py` báo "NÊN TÁI BẢN"), nhắc David một dòng; David đồng ý thì **nâng cấp** cả bộ não một đợt (`hoc-lien-tuc` Việc 4: đo trước, chưng cất, cắt giảm, tái cấu trúc bằng `tai-cau-truc`, đo sau, chỉ ra bản khi bằng hoặc tốt hơn), một mốc chung `nang-cap-<n>`. Một bộ vượt ngưỡng là đủ để tái bản cả đợt. Công cụ đo chỉ kêu vì trùng / rối (dấu ngày, câu ghi đè, câu trùng, dòng gần trùng), **không kêu vì bộ não dài ra**.

**Why:** 10/11/2026 David rút kinh nghiệm từ các dự án code bằng Claude: học lớp 1, lớp 2, lớp 3 chồng lên nhau làm AI đọc luật cũ lẫn mới bị rối. Khảo sát cùng ngày thấy bộ video có 165 dấu ngày, 81 câu ghi đè và luật cãi nhau thật (khối 07 "cảnh đầu luôn là hook" vs quy-tac-chung "không thẻ tít mở đầu mặc định"). David chốt 5 điểm: sửa thẳng · công cụ đo nhắc, David quyết · kiểm mẫu chuẩn + việc thật · skill riêng. Sau tái bản video lần 1 (David chấm "bản mới tốt hơn bản cũ"), David đổi "từng bộ một" thành: "khi tái bản thì cứ tái bản hết toàn bộ mọi thứ để tối ưu nhất" — vì học tài nguyên mới sẽ còn bỏ/đổi luật ở nhiều nơi. 20/11/2026, khi máy báo vượt ngưỡng số dòng: "bộ não và các phần cần học chắc chắn sẽ ngày càng tăng lên, tái bản chỉ là gom các bản trùng hay ý trùng theo nhiều cách khác nhau về một hoặc là gỡ rối" nên bỏ ngưỡng số dòng, thêm đo gần trùng. Cùng ngày: "nên sử dụng từ cải tiến hoặc nâng cấp thì đúng hơn. giống kiểu r&d trong kinh doanh" nên đổi "tái bản" thành vòng Nâng cấp, thước đo chính là bài kiểm + số liệu người xem.

**How to apply:** sổ quyết định là nhật ký cạnh bản luật (ví dụ: `ky-nang/san-xuat-video/ho-so-thuong-hieu/nhat-ky-thay-doi.md` cho hồ sơ tham số video; ghi nhớ này cho lời David). Nguồn của luật là `ky-nang/chuan-muc-lam-viec.md` mục 4, `ky-nang/hoc-lien-tuc/SKILL.md` Việc 4 và skill `ky-nang/tai-cau-truc/SKILL.md`. Liên quan [[quy-tac-hoc-la-bo-sung]], [[video-tham-my-chi-giu-nhan-dien]].
