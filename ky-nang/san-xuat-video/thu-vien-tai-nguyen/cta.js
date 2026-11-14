// MÀN CHỐT (cảnh `cta`, ~4 s cuối MỌI video) — câu chốt do Claude TỰ SÁNG TẠO cho từng video sau khi nắm toàn bộ nội dung
// (người dùng chốt 2026-11-02, xem luật "Màn chốt" trong SKILL.md) → props {text, kind} của cảnh cta (chế độ ghép: CTA trong edl.js).
// File này chỉ là dự phòng khi thiếu props, và bộ biểu tượng theo kiểu hành động.
// kind: 'comment' (bình luận — có ba chấm đang gõ) · 'save' (lưu lại) · 'follow' (theo dõi) · 'share' (gửi cho người khác)
// · 'moi' (MỜI nhắn "gỡ" — kiểu dẫn dắt Mời của kênh David, ho-so-thuong-hieu/kenh.json; không nói giá)
export default {text: 'David rất mong có được sự góp ý của bạn **tại phần bình luận**!', kind: 'comment'};
// Dấu tick nhỏ bật lên trên biểu tượng + tiếng "ting" (assets/sfx/ting.wav — render_preview.py / Show.jsx tự trộn) ở giây
// thứ CTA_TICK tính từ đầu màn chốt, ngay sau khi câu chốt hiện xong → báo người xem "đến lượt bạn".
export const CTA_TICK = 1.6;
export const CTA_ICONS = {
  comment: ['M4 5h16v11H9l-5 4z'],
  save: ['M6 3h12v18l-6-4.5L6 21z'],
  follow: ['M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z', 'M2 21v-1a7 7 0 0 1 14 0v1', 'M19 7v7M15.5 10.5h7'],
  share: ['M4 13v7h16v-7', 'M12 3v12', 'M7 8l5-5 5 5'],
  moi: ['M22 2L11 13', 'M22 2l-7 20-4-9-9-4z'],
};
