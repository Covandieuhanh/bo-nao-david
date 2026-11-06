// Kịch bản cảnh của dự án — Claude viết lại file này cho mỗi video.
// Mốc thời gian (giây) lấy từ transcript.srt của video gốc.
// type: hook (3 s mở đầu, bắt buộc) · lower · kinetic · card · montage · recap · converge · master (xem references/scene-design.md)
import project from './project.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

export const SCENES = [
  // Bản 'ít mà sâu' (học nhịp Hieu Nguyen 2026-11-05): sơ đồ nói thay lời + ảnh thật khung bo góc. Chữ trích lời David.
  {id: 'hook', type: 'hook', start: 0, end: 3.6, props: {eyebrow: 'HÌNH HOÁ', lines: ['MỤC TIÊU', 'VÀ SỨ MỆNH']}},
  {id: 'lang', type: 'diagram', start: 43.4, end: 49.5, props: {mode: 'tu-thanh', label: 'NÂNG CẤP LÊN', items: [{at: 43.67, icon: 'people', label: 'CỘNG ĐỒNG', sub: 'giúp đỡ nhau vô điều kiện'}, {at: 47.79, icon: 'house', label: 'LÀNG', sub: 'không bị giới hạn ở đâu cả'}]}},
  {id: 'muoi-nghin', type: 'illus', start: 155.4, end: 159.0, props: {mode: 'count', num: {to: 10800, at: 155.88, unit: 'THÀNH VIÊN', dur: 1.4}, items: [{icon: 'people', at: 155.6, label: ''}]}},
  {id: 'trieu-do', type: 'illus', start: 173.5, end: 177.9, props: {mode: 'count', num: {to: 1000000, at: 175.5, unit: 'ĐÔ', dur: 1.6}, items: [{icon: 'coins', at: 173.04, label: 'THU NHẬP TỐI THIỂU'}]}},
  {id: 'bac-ho', type: 'diagram', start: 195.6, end: 201.0, props: {mode: 'anh', items: [{at: 195.75, photo: 'bac-ho.jpg', ratio: 0.75, pos: '50% 28%', label: 'DÂN GIÀU THÌ NƯỚC MẠNH', credit: 'Wikimedia Commons · Public Domain'}]}},
  {id: 'lanh-dao', type: 'diagram', start: 209.4, end: 215.6, props: {mode: 'tang', label: 'TRONG LÀNG', items: [{at: 213.06, value: '108', label: 'VỊ LÃNH ĐẠO'}, {at: 209.72, value: '10.800', label: 'THÀNH VIÊN'}]}},
  {id: 'cho-con', type: 'diagram', start: 266.0, end: 272.0, props: {mode: 'tu-thanh', label: 'BỐ CHO CON', items: [{at: 266.34, icon: 'money', label: 'TÀI SẢN', sub: 'vật chất'}, {at: 270.52, icon: 'book', label: 'TRI THỨC', sub: 'và mối quan hệ'}]}},
  {id: 'trainer', type: 'illus', start: 295.0, end: 302.6, props: {mode: 'single', label: 'TỪ 2016', items: [{icon: 'megaphone', at: 295.53, label: 'TRAINER'}]}},
  {id: 'ccl', type: 'diagram', start: 356.4, end: 362.6, props: {mode: 'anh', items: [{at: 356.72, photo: 'ccl.jpg', label: 'CCL', sub: 'ĐÀO TẠO LÃNH ĐẠO CẤP CAO', credit: 'Cooleye · Wikimedia Commons · Public Domain'}]}},
  {id: 'singapore', type: 'diagram', start: 381.4, end: 386.4, props: {mode: 'anh', items: [{at: 381.86, photo: 'singapore.jpg', label: 'SINGAPORE', sub: 'APAC', credit: 'Bijay Chaurasia · CC BY-SA 4.0'}]}},
  {id: 'su-menh', type: 'diagram', start: 417.0, end: 423.4, props: {mode: 'vong', items: [{at: 421.6, label: 'SỨ MỆNH'}, {at: 418.4, label: 'BÊN TRONG'}, {at: 417.0, label: 'BÊN NGOÀI'}]}},
  {id: 'vung-tin', type: 'illus', start: 448.4, end: 452.4, props: {mode: 'single', label: 'CỨ VỮNG TIN', items: [{icon: 'check', at: 449.87, label: ''}]}},
  {id: 'chot', type: 'cta', start: project.duration - 4, end: project.duration,
    props: {text: 'Nếu thấy hữu ích, **gửi cho một người thân** đang đi tìm mục tiêu nhé!', kind: 'share'}},
];

export const COVER = null;
export const STAGE = {show: '', title: 'Mục tiêu và sứ mệnh', speakers: [{name: 'David', role: ''}]};
export const TOPICS = [
  {at: 0, text: 'Hình hoá\nmục tiêu'},
  {at: 13.7, text: 'Học từ\nBNI'},
  {at: 44.34, text: 'Gọi tên\nlà làng'},
  {at: 131.78, text: 'Con số\ncố định'},
  {at: 203.24, text: 'Ban bệ\nquản trị'},
  {at: 236.64, text: 'Truyền cho\ncon cháu'},
  {at: 284.9, text: 'Nhìn vào\nbên trong'},
  {at: 350.3, text: 'Tổ chức\nhình mẫu'},
  {at: 413.4, text: 'Mục tiêu\nvà sứ mệnh'},
  {at: 439.36, text: 'Cứ\nvững tin'},
];
// CHƯƠNG YOUTUBE (David duyệt 2026-11-04): [{at: giây, text: 'Tên chương — trích lời'}] cho video dài; trống → chapters.py lấy TOPICS
export const CHAPTERS = [];

// Chỉ dùng khi xuất ngang từ gốc dọc (output.js layout 'pillar'): chữ hai bên khung, chạy suốt video.
// keywords: từ khoá của ý đang nói (đổi theo từng đoạn, ≤ 3 từ); points: danh sách ý, tích dần theo lời (≤ 9 mục, ≤ 4 từ/mục)
export const SIDES = null;
// export const SIDES = {eyebrow: 'CHỦ ĐỀ', title: 'Tiêu đề video', speaker: 'Tên · vai trò',
//   keywords: [{at: 0.3, text: 'MỞ ĐẦU'}], points: [{at: 14, label: 'Ý thứ nhất'}]};
