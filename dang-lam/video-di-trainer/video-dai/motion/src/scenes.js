// Kịch bản cảnh của dự án — Claude viết lại file này cho mỗi video.
// Mốc thời gian (giây) lấy từ transcript.srt của video gốc.
// type: hook (3 s mở đầu, bắt buộc) · lower · kinetic · card · montage · recap · converge · master (xem references/scene-design.md)
import project from './project.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

export const SCENES = [
  {id: 'mo', type: 'hook', start: 0, end: 3.2, props: {lines: ['KHÔNG PHẢI ANH ẤY SAI', 'MÀ LÀ CHƯA PHÙ HỢP']}},
  {id: 'lai-xe', type: 'illus', start: 10.6, end: 15.0, props: {mode: 'single', items: [{icon: 'car', at: 11.0}], label: 'LÁI XE VỀ'}},
  {id: 'xin-phep', type: 'illus', start: 21.6, end: 26.0, props: {mode: 'single', items: [{icon: 'chat', at: 22.0}], label: 'XIN PHÉP'}},
  {id: 'rieng-tu', type: 'illus', start: 35.2, end: 40.0, props: {mode: 'single', items: [{icon: 'person', at: 35.6}], label: 'RIÊNG TƯ'}},
  {id: 'di-dao-tao', type: 'illus', start: 70.3, end: 75.1, props: {mode: 'single', items: [{icon: 'book', at: 70.7}], label: 'ĐI ĐÀO TẠO'}},
  {id: 'dao-tao', type: 'diagram', start: 92.4, end: 100.4, props: {mode: 'tu-thanh', items: [{icon: 'book', at: 92.9, label: 'ĐÀO TẠO'}, {icon: 'people', at: 96.6, label: 'ĐỒNG HÀNH'}]}},
  {id: 'hai-nam', type: 'diagram', start: 106.4, end: 113.1, props: {mode: 'moc', label: '2 NĂM', items: [{at: 107.6, value: '2024', label: 'NĂM'}, {at: 110.3, value: '2025', label: 'NĂM'}]}},
  {id: 'dong-goi', type: 'illus', start: 123.2, end: 128.5, props: {mode: 'single', items: [{icon: 'write', at: 123.6}], label: 'QUY TRÌNH'}},
  {id: 'cung-lam', type: 'illus', start: 167.5, end: 173.6, props: {mode: 'flow', items: [{icon: 'people', at: 167.9, label: 'CÙNG LÀM'}, {icon: 'gear', at: 169.6, label: 'CÙNG SỬA'}, {icon: 'target', at: 171.6, label: 'CÙNG NHẬN'}], label: 'KẾT QUẢ'}},
  {id: 'cua-sau', type: 'diagram', start: 209.2, end: 216.4, props: {mode: 'chuyen-giao', items: [{icon: 'person', label: 'ANH ẤY'}, {icon: 'people', at: 211.8, label: 'NHÂN SỰ'}, {icon: 'person', label: 'NGƯỜI THÂN'}]}},
  {id: 'cu-dau', type: 'illus', start: 227.0, end: 231.5, props: {mode: 'single', items: [{icon: 'warning', at: 227.4}], label: 'RẤT LÀ ĐAU'}},
  {id: 'con-may-nguoi', type: 'diagram', start: 233.9, end: 240.4, props: {mode: 'tu-thanh', items: [{icon: 'people', at: 234.6, label: '20 MẤY NGƯỜI'}, {icon: 'person', at: 237.5, label: 'CÒN CÓ MẤY NGƯỜI'}]}},
  {id: 'lam-goc', type: 'diagram', start: 272.0, end: 282.0, props: {mode: 'xay-tang', items: [{at: 272.6, label: 'BẢN THÂN'}, {at: 279.4, label: 'CÔNG VIỆC'}]}},
  {id: 'moi-ca-nhan', type: 'illus', start: 288.8, end: 298.2, props: {mode: 'list', label: 'VAI TRÒ RIÊNG', items: [{icon: 'person', at: 289.1, label: 'MỖI CÁ NHÂN'}, {icon: 'building', at: 290.9, label: 'MỖI TỔ CHỨC'}, {icon: 'people', at: 291.8, label: 'MỖI ĐỘI NHÓM'}, {icon: 'globe', at: 293.9, label: 'XÃ HỘI'}]}},
  {id: 'manh-ghep', type: 'illus', start: 300.8, end: 306.2, props: {mode: 'single', items: [{icon: 'puzzle', at: 301.2}], label: 'MỘT MẢNH GHÉP'}},
  {id: 'tu-tin', type: 'illus', start: 313.6, end: 317.3, props: {mode: 'single', items: [{icon: 'star', at: 314.0}], label: 'TỰ TIN'}},
  {id: 'khong-sai', type: 'kinetic', start: 317.4, end: 322.6, props: {lines: ['KHÔNG PHẢI ANH ẤY SAI', 'MÀ LÀ CHƯA PHÙ HỢP.']}},
  {id: 'tu-hoi', type: 'card', start: 337.0, end: 348.2, props: {variant: 'steps', eyebrow: 'CÁI VAI TRÒ CỦA MÌNH LÀ GÌ', steps: [{text: 'Trong xã hội', at: 340.6}, {text: 'Trong công ty và doanh nghiệp', at: 342.4}, {text: 'Không bị lấn sân', at: 346.0}]}},
  {id: 'ky-nang', type: 'card', start: 353.8, end: 359.6, props: {variant: 'steps', eyebrow: 'NÓ ĐÂU PHẢI LÀ', steps: [{text: 'Cái kỹ năng', at: 354.7}, {text: 'Cái năng lực của anh', at: 356.7}]}},
  {id: 'thoi-gian', type: 'illus', start: 362.3, end: 366.8, props: {mode: 'single', items: [{icon: 'clock', at: 362.7}], label: 'THỜI GIAN'}},
  {id: 'ba-thang', type: 'diagram', start: 367.0, end: 373.4, props: {mode: 'moc', label: 'ĐỂ ANH GỌI LÀ BUỒN', items: [{at: 367.6, value: '1', label: 'THÁNG'}, {at: 368.6, value: '2', label: 'THÁNG'}, {at: 369.2, value: '3', label: 'THÁNG'}]}},
  {id: 'mot-ngay', type: 'diagram', start: 389.4, end: 397.4, props: {mode: 'tu-thanh', items: [{icon: 'hourglass', at: 389.9, label: 'BA THÁNG'}, {icon: 'sun', at: 393.1, label: 'MỘT NGÀY'}]}},
  {id: 'noi-dau', type: 'illus', start: 413.6, end: 420.2, props: {mode: 'single', items: [{icon: 'heart', at: 414.0}], label: 'NỖI ĐAU'}},
  {id: 'o-ga', type: 'illus', start: 421.0, end: 426.4, props: {mode: 'single', items: [{icon: 'road', at: 421.6}], label: 'Ổ GÀ'}},
  {id: 'xoc', type: 'card', start: 428.0, end: 440.6, props: {variant: 'steps', eyebrow: 'ĐI VÀO Ổ GÀ', steps: [{text: 'Sẽ xóc như thế nào', at: 428.4}, {text: 'Tổn hại cái phương tiện', at: 431.1}, {text: 'Nguy hiểm như thế nào', at: 437.2}]}},
  {id: 'kham-benh', type: 'illus', start: 467.6, end: 472.0, props: {mode: 'single', items: [{icon: 'heart', at: 468.0}], label: 'KHÁM BỆNH'}},
  {id: 'thu-am', type: 'illus', start: 485.6, end: 490.0, props: {mode: 'single', items: [{icon: 'mic', at: 486.0}], label: 'THU ÂM NGAY'}},
  {id: 'vuc-day', type: 'illus', start: 508.0, end: 513.5, props: {mode: 'single', items: [{icon: 'up', at: 508.4}], label: 'VỰC DẬY'}},
  {id: 'binh-luan', type: 'illus', start: 521.2, end: 525.0, props: {mode: 'single', items: [{icon: 'chat', at: 521.6}], label: 'BÌNH LUẬN'}},
  {id: 'chot', type: 'cta', start: 533.7, end: 537.7, props: {text: 'Bạn đang kẹt ở vai trò nào? Bình luận **Vấn đề** nhé', kind: 'comment'}},
];

// Chỉ dùng cho PODCAST (project.podcast — skill podcast-style-edit): sân khấu nền chạy suốt video (components/Stage.jsx).
// show: tên chương trình; title: tên tập; speakers: [{name, role}] theo thứ tự người nói 0, 1 trong speakers.js
// TOPICS: ý đang bàn ở giữa khung (trích lời, ≤ 5 từ/dòng, '\n' tách 2 dòng; mốc = lúc bắt đầu ý) — tự ẩn khi có lớp phủ
// COVER: màn hình bìa ~1 s ghép TRƯỚC video (ảnh bìa cho mạng xã hội). title = tiêu đề NGƯỜI DÙNG đưa (mỗi video hỏi lại),
// '\n' xuống dòng, dòng cuối tô màu nhấn; eyebrow (tuỳ chọn) — mặc định STAGE.show. null = không có bìa.
export const COVER = null;
export const STAGE = {title: 'Đi trainer cho người làm trainer', speakers: [{name: 'David'}]};
export const TOPICS = [
  {at: 3.2, text: 'TẠI SAO LẠI\nGẤP RÚT NHƯ VẬY'},
  {at: 51.1, text: 'TRAINER CHO CÁI NGƯỜI\nĐANG ĐI TRAINER'},
  {at: 161.5, text: 'SAI THÌ CÙNG SỬA\nĐÚNG THÌ CÙNG NHẬN'},
  {at: 202.3, text: 'NGƯỜI RẤT THÂN QUEN\nLẠI ĐI CỬA SAU'},
  {at: 282.5, text: 'MỖI NGƯỜI\nLÀ MỘT MẢNH GHÉP'},
  {at: 390.7, text: 'CHỈ CÒN MỘT TUẦN\nHAY MỘT NGÀY'},
  {at: 413.7, text: 'AI CÓ NỖI ĐAU ĐẤY\nMỚI THẤM ĐƯỢC'},
  {at: 502.9, text: 'NẾU BẠN CÓ CÙNG\nCÁI NỖI ĐAU ĐẤY'},
];
// CHƯƠNG YOUTUBE (David duyệt 2026-11-04): [{at: giây, text: 'Tên chương — trích lời'}] cho video dài; trống → chapters.py lấy TOPICS
export const CHAPTERS = [];

// Chỉ dùng khi xuất ngang từ gốc dọc (output.js layout 'pillar'): chữ hai bên khung, chạy suốt video.
// keywords: từ khoá của ý đang nói (đổi theo từng đoạn, ≤ 3 từ); points: danh sách ý, tích dần theo lời (≤ 9 mục, ≤ 4 từ/mục)
export const SIDES = null;
// export const SIDES = {eyebrow: 'CHỦ ĐỀ', title: 'Tiêu đề video', speaker: 'Tên · vai trò',
//   keywords: [{at: 0.3, text: 'MỞ ĐẦU'}], points: [{at: 14, label: 'Ý thứ nhất'}]};
