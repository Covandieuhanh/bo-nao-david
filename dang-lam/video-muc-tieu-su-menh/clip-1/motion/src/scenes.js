// Kịch bản cảnh của dự án — Claude viết lại file này cho mỗi video.
// Mốc thời gian (giây) lấy từ transcript.srt của video gốc.
// type: hook (3 s mở đầu, bắt buộc) · lower · kinetic · card · montage · recap · converge · master (xem references/scene-design.md)
import project from './project.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

export const SCENES = [
  {id: 'mo', type: 'hook', start: 0, end: 2.5, props: {lines: ['HƯỚNG DẪN ĐẾN KHI', 'HỌ KHÔNG CẦN MÌNH']}},
  {id: 'tro-thanh', type: 'illus', start: 4.17, end: 6.17, props: {mode: 'single', compact: true, items: [{icon: 'person', at: 4.27}]}},
  {id: 'vi-tri', type: 'illus', start: 7.14, end: 9.54, props: {mode: 'single', compact: true, items: [{icon: 'target', at: 7.24}]}},
  {id: 'nam-2016', type: 'illus', start: 10.39, end: 12.79, props: {mode: 'single', compact: true, items: [{icon: 'calendar', at: 10.49}]}},
  {id: 'ban-than', type: 'illus', start: 20.14, end: 22.34, props: {mode: 'single', compact: true, items: [{icon: 'brain', at: 20.24}]}},
  {id: 'quy-trinh', type: 'illus', start: 23.24, end: 25.24, props: {mode: 'single', compact: true, items: [{icon: 'write', at: 23.34}]}},
  {id: 'cong-chung', type: 'illus', start: 27.28, end: 29.48, props: {mode: 'single', compact: true, items: [{icon: 'mic', at: 27.38}]}},
  {id: 'le-thuoc', type: 'illus', start: 32.57, end: 34.87, props: {mode: 'single', compact: true, items: [{icon: 'up', at: 32.67}]}},
  {id: 'tam-can', type: 'illus', start: 36.16, end: 38.56, props: {mode: 'single', compact: true, items: [{icon: 'heart', at: 36.26}]}},
];

// Chỉ dùng cho PODCAST (project.podcast — skill podcast-style-edit): sân khấu nền chạy suốt video (components/Stage.jsx).
// show: tên chương trình; title: tên tập; speakers: [{name, role}] theo thứ tự người nói 0, 1 trong speakers.js
// TOPICS: ý đang bàn ở giữa khung (trích lời, ≤ 5 từ/dòng, '\n' tách 2 dòng; mốc = lúc bắt đầu ý) — tự ẩn khi có lớp phủ
// COVER: màn hình bìa ~1 s ghép TRƯỚC video (ảnh bìa cho mạng xã hội). title = tiêu đề NGƯỜI DÙNG đưa (mỗi video hỏi lại),
// '\n' xuống dòng, dòng cuối tô màu nhấn; eyebrow (tuỳ chọn) — mặc định STAGE.show. null = không có bìa.
export const COVER = null;
export const STAGE = {title: 'Mục tiêu và sứ mệnh', speakers: [{name: 'David'}]};
export const TOPICS = [
  {at: 0, text: 'NHÌN VÀO\nBÊN TRONG'},
  {at: 16.42, text: 'MÌNH HƯỚNG DẪN HỌ'},
  {at: 31.35, text: 'KHÔNG CÒN\nLỆ THUỘC VÀO MÌNH'},
];
// CHƯƠNG YOUTUBE (David duyệt 2026-11-04): [{at: giây, text: 'Tên chương — trích lời'}] cho video dài; trống → chapters.py lấy TOPICS
export const CHAPTERS = [];

// Chỉ dùng khi xuất ngang từ gốc dọc (output.js layout 'pillar'): chữ hai bên khung, chạy suốt video.
// keywords: từ khoá của ý đang nói (đổi theo từng đoạn, ≤ 3 từ); points: danh sách ý, tích dần theo lời (≤ 9 mục, ≤ 4 từ/mục)
export const SIDES = null;
// export const SIDES = {eyebrow: 'CHỦ ĐỀ', title: 'Tiêu đề video', speaker: 'Tên · vai trò',
//   keywords: [{at: 0.3, text: 'MỞ ĐẦU'}], points: [{at: 14, label: 'Ý thứ nhất'}]};
