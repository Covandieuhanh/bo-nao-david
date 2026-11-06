// Kịch bản cảnh của dự án — Claude viết lại file này cho mỗi video.
// Mốc thời gian (giây) lấy từ transcript.srt của video gốc.
// type: hook (3 s mở đầu, bắt buộc) · lower · kinetic · card · montage · recap · converge · master (xem references/scene-design.md)
import project from './project.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

export const SCENES = [
  {id: 'mo', type: 'hook', start: 0, end: 2.5, props: {lines: ['BỊ RÚT ĐI NHÂN SỰ', 'HÃY HIỂU VAI TRÒ']}},
  {id: 'nguoi-ban', type: 'illus', start: 2.6, end: 4.0, props: {mode: 'single', compact: true, items: [{icon: 'people', at: 2.7}]}},
  {id: 'xa-hoi', type: 'illus', start: 7.0, end: 10.3, props: {mode: 'single', compact: true, items: [{icon: 'globe', at: 7.1}]}},
  {id: 'cong-ty', type: 'illus', start: 10.5, end: 14.1, props: {mode: 'single', compact: true, items: [{icon: 'building', at: 10.6}]}},
  {id: 'lan-san', type: 'illus', start: 14.3, end: 16.2, props: {mode: 'single', compact: true, items: [{icon: 'warning', at: 14.4}]}},
  {id: 'ky-nang', type: 'illus', start: 20.2, end: 23.8, props: {mode: 'single', compact: true, items: [{icon: 'gear', at: 20.3}]}},
  {id: 'binh-thuong', type: 'illus', start: 23.95, end: 25.3, props: {mode: 'single', compact: true, items: [{icon: 'check', at: 24.1}]}},
  {id: 'thoi-gian', type: 'illus', start: 28.2, end: 31.8, props: {mode: 'single', compact: true, items: [{icon: 'clock', at: 28.3}]}},
];

// Chỉ dùng cho PODCAST (project.podcast — skill podcast-style-edit): sân khấu nền chạy suốt video (components/Stage.jsx).
// show: tên chương trình; title: tên tập; speakers: [{name, role}] theo thứ tự người nói 0, 1 trong speakers.js
// TOPICS: ý đang bàn ở giữa khung (trích lời, ≤ 5 từ/dòng, '\n' tách 2 dòng; mốc = lúc bắt đầu ý) — tự ẩn khi có lớp phủ
// COVER: màn hình bìa ~1 s ghép TRƯỚC video (ảnh bìa cho mạng xã hội). title = tiêu đề NGƯỜI DÙNG đưa (mỗi video hỏi lại),
// '\n' xuống dòng, dòng cuối tô màu nhấn; eyebrow (tuỳ chọn) — mặc định STAGE.show. null = không có bìa.
export const COVER = null;
export const STAGE = {title: 'Đi trainer cho người làm trainer', speakers: [{name: 'David'}]};
export const TOPICS = [];
// CHƯƠNG YOUTUBE (David duyệt 2026-11-04): [{at: giây, text: 'Tên chương — trích lời'}] cho video dài; trống → chapters.py lấy TOPICS
export const CHAPTERS = [];

// Chỉ dùng khi xuất ngang từ gốc dọc (output.js layout 'pillar'): chữ hai bên khung, chạy suốt video.
// keywords: từ khoá của ý đang nói (đổi theo từng đoạn, ≤ 3 từ); points: danh sách ý, tích dần theo lời (≤ 9 mục, ≤ 4 từ/mục)
export const SIDES = null;
// export const SIDES = {eyebrow: 'CHỦ ĐỀ', title: 'Tiêu đề video', speaker: 'Tên · vai trò',
//   keywords: [{at: 0.3, text: 'MỞ ĐẦU'}], points: [{at: 14, label: 'Ý thứ nhất'}]};
