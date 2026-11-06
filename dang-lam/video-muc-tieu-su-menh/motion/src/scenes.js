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
  {id: 'giup-do', type: 'illus', start: 10.9, end: 15.4, props: {mode: 'single', items: [{icon: 'heart', at: 11.3}], label: 'GIÚP ĐỠ NHAU'}},
  {id: 'trao-co-hoi', type: 'illus', start: 33.4, end: 38.0, props: {mode: 'single', items: [{icon: 'chat', at: 33.8}], label: 'TRAO CƠ HỘI'}},
  {id: 'dia-gioi', type: 'illus', start: 67.9, end: 71.9, props: {mode: 'single', items: [{icon: 'pin', at: 68.3}], label: 'KHÔNG ĐỊA GIỚI'}},
  {id: 'khai-hoang', type: 'diagram', start: 72.1, end: 79.0, props: {mode: 'tu-thanh', items: [{icon: 'people', at: 74.0, label: 'DÂN LÀNG Ở ĐÂU'}, {icon: 'house', at: 76.4, label: 'LÀNG CÓ MẶT Ở ĐẤY'}]}},
  {id: 'xa-xu', type: 'illus', start: 80.4, end: 85.0, props: {mode: 'single', items: [{icon: 'road', at: 80.8}], label: 'XA QUÊ'}},
  {id: 'viet-kieu', type: 'illus', start: 106.6, end: 112.4, props: {mode: 'list', label: 'VIỆT KIỀU', items: [{icon: 'globe', at: 107.7, label: 'ĐỨC'}, {icon: 'globe', at: 108.7, label: 'MỸ'}, {icon: 'globe', at: 109.6, label: 'PHÁP'}]}},
  {id: 'co-van', type: 'illus', start: 143.2, end: 148.0, props: {mode: 'single', items: [{icon: 'person', at: 143.6}], label: 'NGƯỜI CỐ VẤN'}},
  {id: 'lang', type: 'diagram', start: 43.4, end: 49.8, props: {mode: 'tu-thanh', label: 'NÂNG CẤP LÊN', items: [{at: 43.67, icon: 'people', label: 'CỘNG ĐỒNG', sub: 'giúp đỡ nhau vô điều kiện'}, {at: 47.79, icon: 'house', label: 'LÀNG', sub: 'không bị giới hạn ở đâu cả'}]}},
  {id: 'muoi-nghin', type: 'illus', start: 155.4, end: 159.0, props: {mode: 'count', num: {to: 10800, at: 155.88, unit: 'THÀNH VIÊN', dur: 1.4}, items: [{icon: 'people', at: 155.6, label: ''}]}},
  {id: 'trieu-do', type: 'illus', start: 172.8, end: 177.9, props: {mode: 'count', num: {to: 1000000, at: 175.5, unit: 'ĐÔ', dur: 1.6}, items: [{icon: 'coins', at: 173.04, label: 'THU NHẬP TỐI THIỂU'}]}},
  {id: 'bac-ho', type: 'diagram', start: 195.6, end: 201.0, props: {mode: 'anh', items: [{at: 195.75, photo: 'bac-ho.jpg', ratio: 0.75, pos: '50% 28%', label: 'DÂN GIÀU THÌ NƯỚC MẠNH', credit: 'Wikimedia Commons · Public Domain'}]}},
  {id: 'lanh-dao', type: 'diagram', start: 209.4, end: 215.6, props: {mode: 'tang', label: 'TRONG LÀNG', items: [{at: 213.06, value: '108', label: 'VỊ LÃNH ĐẠO'}, {at: 209.72, value: '10.800', label: 'THÀNH VIÊN'}]}},
  {id: 'cho-con', type: 'diagram', start: 266.0, end: 272.5, props: {mode: 'tu-thanh', label: 'BỐ CHO CON', items: [{at: 266.34, icon: 'money', label: 'TÀI SẢN', sub: 'vật chất'}, {at: 270.52, icon: 'book', label: 'TRI THỨC', sub: 'và mối quan hệ'}]}},
  {id: 'trainer', type: 'illus', start: 295.0, end: 300.8, props: {mode: 'single', label: 'TỪ 2016', items: [{icon: 'megaphone', at: 295.53, label: 'TRAINER'}]}},
  {id: 'ccl', type: 'diagram', start: 356.4, end: 362.6, props: {mode: 'anh', items: [{at: 356.72, photo: 'ccl.jpg', label: 'CCL', sub: 'ĐÀO TẠO LÃNH ĐẠO CẤP CAO', credit: 'Cooleye · Wikimedia Commons · Public Domain'}]}},
  {id: 'singapore', type: 'diagram', start: 381.4, end: 386.4, props: {mode: 'anh', items: [{at: 381.86, photo: 'singapore.jpg', label: 'SINGAPORE', sub: 'APAC', credit: 'Bijay Chaurasia · CC BY-SA 4.0'}]}},
  {id: 'su-menh', type: 'diagram', start: 417.0, end: 423.6, props: {mode: 'vong', items: [{at: 421.6, label: 'SỨ MỆNH'}, {at: 418.4, label: 'BÊN TRONG'}, {at: 417.0, label: 'BÊN NGOÀI'}]}},
  {id: 'vung-tin', type: 'illus', start: 448.4, end: 452.4, props: {mode: 'single', label: 'CỨ VỮNG TIN', items: [{icon: 'check', at: 449.87, label: ''}]}},
  {id: 'quan-tri', type: 'illus', start: 228.3, end: 234.2, props: {mode: 'list', label: 'QUẢN TRỊ', items: [{icon: 'person', at: 228.7, label: 'TRƯỞNG LÀNG'}, {icon: 'person', at: 229.9, label: 'TRƯỞNG THÔN'}, {icon: 'person', at: 230.6, label: 'TRƯỞNG ẤP'}, {icon: 'money', at: 231.8, label: 'KẾ TOÁN'}]}},
  {id: 'ra-ngoai', type: 'illus', start: 247.8, end: 252.6, props: {mode: 'single', items: [{icon: 'globe', at: 248.2}], label: 'BÊN NGOÀI'}},
  {id: 'vao-trong', type: 'card', start: 285.4, end: 294.6, props: {variant: 'steps', eyebrow: 'NHÌN VÀO BÊN TRONG', steps: [{text: 'Mình muốn làm gì', at: 288.9}, {text: 'Mình muốn trở thành ai', at: 290.3}, {text: 'Mình muốn như thế nào', at: 291.5}]}},
  {id: 'huong-dan', type: 'illus', start: 312.6, end: 324.6, props: {mode: 'list', label: 'HƯỚNG DẪN HỌ', items: [{icon: 'brain', at: 313.2, label: 'BẢN THÂN'}, {icon: 'write', at: 316.4, label: 'QUY TRÌNH'}, {icon: 'mic', at: 320.8, label: 'CÔNG CHÚNG'}]}},
  {id: 'le-thuoc', type: 'kinetic', start: 325.6, end: 330.0, props: {lines: ['KHÔNG CÒN PHẢI', 'LỆ THUỘC VÀO MÌNH']}},
  {id: 'lo-trinh', type: 'illus', start: 389.9, end: 398.0, props: {mode: 'flow', items: [{icon: 'book', at: 390.4, label: 'TIẾNG ANH'}, {icon: 'check', at: 393.6, label: 'CHỨNG CHỈ'}, {icon: 'pin', at: 395.3, label: 'VỀ VIỆT NAM'}]}},
  {id: 'ccl-vn', type: 'kinetic', start: 398.1, end: 403.4, props: {lines: ['MỘT CÁI CCL', 'Ở VIỆT NAM']}},
  {id: 'ngau-nhien', type: 'kinetic', start: 460.8, end: 465.0, props: {lines: ['KHÔNG HỀ', 'NGẪU NHIÊN']}},
  {id: 'goi-ten', type: 'card', start: 474.2, end: 481.4, props: {variant: 'steps', eyebrow: 'CÓ NGƯỜI GỌI TÊN CHO MÌNH', steps: [{text: 'Biết được mục tiêu', at: 476.6}, {text: 'Biết được năng lực', at: 477.6}, {text: 'Biết được kỹ năng', at: 478.6}]}},
  {id: 'toi-la-ai', type: 'kinetic', start: 482.3, end: 486.4, props: {lines: ['TÔI LÀ AI', 'TRÊN CUỘC ĐỜI NÀY']}},
  {id: 'chot', type: 'cta', start: project.duration - 4, end: project.duration,
    props: {text: 'Mục tiêu của bạn đã có tên chưa? Bình luận **Vấn đề** nhé', kind: 'comment'}},
].sort((a, b) => a.start - b.start);

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
