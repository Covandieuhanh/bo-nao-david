---
name: quy-tac-sua-thang-tai-ban
description: "Khi đổi luật, Claude sửa trực tiếp câu cũ (không thêm câu chồng kiểu \"bổ sung/thay luật\", không ghi ngày trong bản luật); định kỳ NÂNG CẤP cả bộ não trong một đợt (đo trước/sau, chưng cất, cắt giảm, dọn dẹp) — 2026-11-10, đổi tên 2026-11-20"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 39383a2e-bf70-432e-8fcc-63c950a840d4
  modified: 2026-11-20T23:30:00.000Z
---

Mỗi lần học mẫu, sửa theo góp ý hay có quyết định mới, Claude viết lại chính câu luật thành trạng thái mới và xoá câu cũ; ngày, lời David và lý do được ghi vào sổ quyết định. Khi luật vẫn đã chồng nhiều lớp (công cụ đo `ky-nang/tai-cau-truc/do-chong-cheo.py` báo "NÊN TÁI BẢN"), Claude nhắc David một dòng; David đồng ý thì Claude **nâng cấp** cả bộ não trong một đợt (`hoc-lien-tuc` Việc 4: đo trước, chưng cất, cắt giảm, tái cấu trúc bằng `tai-cau-truc`, đo sau, chỉ ra bản khi bằng hoặc tốt hơn), với một mốc chung `nang-cap-<n>`. Chỉ cần một bộ vượt ngưỡng là đủ để tái bản cả đợt. Công cụ đo chỉ cảnh báo khi có trùng lặp hoặc rối (dấu ngày, câu ghi đè, câu trùng, dòng gần trùng), **không cảnh báo vì bộ não dài ra**.

**Why:** 10/11/2026 David rút kinh nghiệm từ các dự án code bằng Claude: học lớp 1, lớp 2, lớp 3 chồng lên nhau làm AI đọc lẫn luật cũ và mới nên bị rối. Khảo sát cùng ngày cho thấy bộ video có 165 dấu ngày, 81 câu ghi đè và luật mâu thuẫn nhau thật (khối 07 "cảnh đầu luôn là hook" so với quy-tac-chung "không thẻ tít mở đầu mặc định"). David chốt 5 điểm: sửa thẳng · công cụ đo nhắc, David quyết · kiểm mẫu chuẩn và việc thật · skill riêng. Sau lần tái bản video thứ 1 (David chấm "bản mới tốt hơn bản cũ"), David đổi "từng bộ một" thành: "khi tái bản thì cứ tái bản hết toàn bộ mọi thứ để tối ưu nhất" — vì việc học tài nguyên mới sẽ còn bỏ hoặc đổi luật ở nhiều nơi. 20/11/2026, khi công cụ kiểm tra báo vượt ngưỡng số dòng: "bộ não và các phần cần học chắc chắn sẽ ngày càng tăng lên, tái bản chỉ là gom các bản trùng hay ý trùng theo nhiều cách khác nhau về một hoặc là gỡ rối" nên Claude bỏ ngưỡng số dòng, thêm phép đo dòng gần trùng. Cùng ngày: "nên sử dụng từ cải tiến hoặc nâng cấp thì đúng hơn. giống kiểu r&d trong kinh doanh" nên Claude đổi "tái bản" thành vòng Nâng cấp, thước đo chính là bài kiểm và số liệu người xem.

**How to apply:** sổ quyết định là nhật ký đặt cạnh bản luật (ví dụ: `ky-nang/san-xuat-video/ho-so-thuong-hieu/nhat-ky-thay-doi.md` cho hồ sơ tham số video; ghi nhớ này cho lời David). Nguồn của luật là `ky-nang/chuan-muc-lam-viec.md` mục 4, `ky-nang/hoc-lien-tuc/SKILL.md` Việc 4 và skill `ky-nang/tai-cau-truc/SKILL.md`. Liên quan [[quy-tac-hoc-la-bo-sung]], [[video-tham-my-chi-giu-nhan-dien]].

Gốc: khối 3 (Học và thay đổi) của tu-duy-goc.md — thay đổi phải sửa đúng câu nguồn để mỗi ý chỉ có một bản; chồng lớp luật cũ lên luật mới làm AI đọc rối.
