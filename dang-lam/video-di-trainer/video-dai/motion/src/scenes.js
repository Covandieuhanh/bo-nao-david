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
  {id: 'cung-lam', type: 'illus', start: 167.5, end: 173.6, props: {mode: 'flow', items: [{icon: 'people', at: 167.9, label: 'CÙNG LÀM'}, {icon: 'gear', at: 169.6, label: 'CÙNG SỬA'}, {icon: 'target', at: 171.6, label: 'CÙNG NHẬN'}], label: 'KẾT QUẢ'}},
  {id: 'con-may-nguoi', type: 'diagram', start: 233.9, end: 240.4, props: {mode: 'tu-thanh', items: [{icon: 'people', at: 234.6, label: '20 MẤY NGƯỜI'}, {icon: 'person', at: 237.5, label: 'CÒN CÓ MẤY NGƯỜI'}]}},
  {id: 'moi-ca-nhan', type: 'illus', start: 288.8, end: 298.2, props: {mode: 'list', label: 'ĐỀU CÓ VAI TRÒ RIÊNG', items: [{icon: 'person', at: 289.1, label: 'MỖI CÁ NHÂN'}, {icon: 'building', at: 290.9, label: 'MỖI TỔ CHỨC'}, {icon: 'people', at: 291.8, label: 'MỖI ĐỘI NHÓM'}, {icon: 'globe', at: 293.9, label: 'XÃ HỘI'}]}},
  {id: 'manh-ghep', type: 'illus', start: 300.8, end: 306.2, props: {mode: 'single', items: [{icon: 'puzzle', at: 301.2}], label: 'MỘT MẢNH GHÉP'}},
  {id: 'khong-sai', type: 'kinetic', start: 317.4, end: 322.6, props: {lines: ['KHÔNG PHẢI ANH ẤY SAI', 'MÀ LÀ CHƯA PHÙ HỢP.']}},
  {id: 'tu-hoi', type: 'card', start: 337.0, end: 348.2, props: {variant: 'steps', eyebrow: 'CÁI VAI TRÒ CỦA MÌNH LÀ GÌ', steps: [{text: 'Trong xã hội', at: 340.6}, {text: 'Trong công ty và doanh nghiệp', at: 342.4}, {text: 'Không bị lấn sân', at: 346.0}]}},
  {id: 'ba-thang', type: 'diagram', start: 367.0, end: 373.4, props: {mode: 'moc', label: 'ĐỂ ANH GỌI LÀ BUỒN', items: [{at: 367.6, value: '1', label: 'THÁNG'}, {at: 368.6, value: '2', label: 'THÁNG'}, {at: 369.2, value: '3', label: 'THÁNG'}]}},
  {id: 'o-ga', type: 'illus', start: 421.0, end: 426.4, props: {mode: 'single', items: [{icon: 'road', at: 421.6}], label: 'ĐI VÀO Ổ GÀ'}},
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
