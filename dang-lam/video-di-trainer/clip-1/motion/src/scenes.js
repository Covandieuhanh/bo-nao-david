// Kịch bản cảnh của dự án — Claude viết lại file này cho mỗi video.
// Mốc thời gian (giây) lấy từ transcript.srt của video gốc.
// type: hook (3 s mở đầu, bắt buộc) · lower · kinetic · card · montage · recap · converge · master (xem references/scene-design.md)
import project from './project.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

export const SCENES = [
  {id: 'mo', type: 'hook', start: 0, end: 2.5, props: {lines: ['NGƯỜI THÂN QUEN', 'KÉO HẾT NHÂN SỰ']}},
  {id: 'cua-sau', type: 'illus', start: 3.6, end: 6.0, props: {mode: 'single', compact: true, items: [{icon: 'warning', at: 3.7}]}},
  {id: 'nhat-het', type: 'illus', start: 6.2, end: 9.2, props: {mode: 'single', compact: true, items: [{icon: 'people', at: 6.3}]}},
  {id: 'doanh-nghiep', type: 'illus', start: 13.6, end: 16.7, props: {mode: 'single', compact: true, items: [{icon: 'building', at: 13.7}]}},
  {id: 'mot-cu', type: 'illus', start: 19.3, end: 21.0, props: {mode: 'single', compact: true, items: [{icon: 'sad', at: 19.4}]}},
  {id: 'hai-muoi', type: 'illus', start: 25.6, end: 27.8, props: {mode: 'single', compact: true, items: [{icon: 'people', at: 25.7}]}},
  {id: 'con-may', type: 'illus', start: 27.9, end: 29.8, props: {mode: 'single', compact: true, items: [{icon: 'person', at: 28.0}]}},
  {id: 'cu-soc', type: 'illus', start: 37.3, end: 39.0, props: {mode: 'single', compact: true, items: [{icon: 'warning', at: 37.4}]}},
];

// Chỉ dùng cho PODCAST (project.podcast — skill podcast-style-edit): sân khấu nền chạy suốt video (components/Stage.jsx).
// show: tên chương trình; title: tên tập; speakers: [{name, role}] theo thứ tự người nói 0, 1 trong speakers.js
// TOPICS: ý đang bàn ở giữa khung (trích lời, ≤ 5 từ/dòng, '\n' tách 2 dòng; mốc = lúc bắt đầu ý) — tự ẩn khi có lớp phủ
// COVER: màn hình bìa ~1 s ghép TRƯỚC video (ảnh bìa cho mạng xã hội). title = tiêu đề NGƯỜI DÙNG đưa (mỗi video hỏi lại),
// '\n' xuống dòng, dòng cuối tô màu nhấn; eyebrow (tuỳ chọn) — mặc định STAGE.show. null = không có bìa.
export const COVER = null;
export const STAGE = {title: 'Đi trainer cho người làm trainer', speakers: [{name: 'David'}]};
export const TOPICS = [
  {at: 0, text: 'NGƯỜI RẤT THÂN QUEN\nLẠI ĐI CỬA SAU'},
  {at: 9.3, text: 'TƯỞNG CHỪNG MỌI THỨ\nĐÃ ỔN HẾT'},
  {at: 25.6, text: '20 MẤY NGƯỜI\nCHỈ CÒN CÓ MẤY NGƯỜI'},
];
// CHƯƠNG YOUTUBE (David duyệt 2026-11-04): [{at: giây, text: 'Tên chương — trích lời'}] cho video dài; trống → chapters.py lấy TOPICS
export const CHAPTERS = [];

// Chỉ dùng khi xuất ngang từ gốc dọc (output.js layout 'pillar'): chữ hai bên khung, chạy suốt video.
// keywords: từ khoá của ý đang nói (đổi theo từng đoạn, ≤ 3 từ); points: danh sách ý, tích dần theo lời (≤ 9 mục, ≤ 4 từ/mục)
export const SIDES = null;
// export const SIDES = {eyebrow: 'CHỦ ĐỀ', title: 'Tiêu đề video', speaker: 'Tên · vai trò',
//   keywords: [{at: 0.3, text: 'MỞ ĐẦU'}], points: [{at: 14, label: 'Ý thứ nhất'}]};
