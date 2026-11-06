// Kịch bản cảnh của dự án — Claude viết lại file này cho mỗi video.
// Mốc thời gian (giây) lấy từ transcript.srt của video gốc.
// type: hook (3 s mở đầu, bắt buộc) · lower · kinetic · card · montage · recap · converge · master (xem references/scene-design.md)
import project from './project.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

export const SCENES = [
  {id: 'mo', type: 'hook', start: 0, end: 2.5, props: {lines: ['LÀM TỪ 2016', 'GIỜ MỚI GỌI ĐƯỢC TÊN']}},
  {id: 'tro-thanh', type: 'illus', start: 3.05, end: 5.05, props: {mode: 'single', compact: true, items: [{icon: 'person', at: 3.15}]}},
  {id: 'vi-tri', type: 'illus', start: 6.02, end: 8.42, props: {mode: 'single', compact: true, items: [{icon: 'target', at: 6.12}]}},
  {id: 'nam-2016', type: 'illus', start: 12.47, end: 14.87, props: {mode: 'single', compact: true, items: [{icon: 'calendar', at: 12.57}]}},
  {id: 'ban-than', type: 'illus', start: 24.02, end: 26.22, props: {mode: 'single', compact: true, items: [{icon: 'brain', at: 24.12}]}},
  {id: 'quy-trinh', type: 'illus', start: 27.12, end: 29.12, props: {mode: 'single', compact: true, items: [{icon: 'write', at: 27.22}]}},
  {id: 'cong-chung', type: 'illus', start: 31.16, end: 33.36, props: {mode: 'single', compact: true, items: [{icon: 'mic', at: 31.26}]}},
  {id: 'le-thuoc', type: 'illus', start: 36.45, end: 38.75, props: {mode: 'single', compact: true, items: [{icon: 'up', at: 36.55}]}},
  {id: 'tam-can', type: 'illus', start: 40.04, end: 42.44, props: {mode: 'single', compact: true, items: [{icon: 'heart', at: 40.14}]}},
  {id: 'goi-ten', type: 'illus', start: 44.81, end: 47.01, props: {mode: 'single', compact: true, items: [{icon: 'chat', at: 44.91}]}},
  {id: 'nghe', type: 'illus', start: 47.22, end: 49.42, props: {mode: 'single', compact: true, items: [{icon: 'megaphone', at: 47.32}]}},
  {id: 'nhen-nhom', type: 'illus', start: 53.7, end: 55.9, props: {mode: 'single', compact: true, items: [{icon: 'leaf', at: 53.8}]}},
  {id: 'lam-gi', type: 'illus', start: 59.54, end: 61.74, props: {mode: 'single', compact: true, items: [{icon: 'footsteps', at: 59.64}]}},
  {id: 'da-hoc', type: 'illus', start: 64.73, end: 66.93, props: {mode: 'single', compact: true, items: [{icon: 'book', at: 64.83}]}},
  {id: 'ngau-nhien', type: 'illus', start: 69.56, end: 71.96, props: {mode: 'single', compact: true, items: [{icon: 'puzzle', at: 69.66}]}},
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
  {at: 43.02, text: 'GỌI TÊN ĐƯỢC NGHỀ'},
  {at: 49.97, text: 'CỨ VỮNG TIN'},
];
// CHƯƠNG YOUTUBE (David duyệt 2026-11-04): [{at: giây, text: 'Tên chương — trích lời'}] cho video dài; trống → chapters.py lấy TOPICS
export const CHAPTERS = [];

// Chỉ dùng khi xuất ngang từ gốc dọc (output.js layout 'pillar'): chữ hai bên khung, chạy suốt video.
// keywords: từ khoá của ý đang nói (đổi theo từng đoạn, ≤ 3 từ); points: danh sách ý, tích dần theo lời (≤ 9 mục, ≤ 4 từ/mục)
export const SIDES = null;
// export const SIDES = {eyebrow: 'CHỦ ĐỀ', title: 'Tiêu đề video', speaker: 'Tên · vai trò',
//   keywords: [{at: 0.3, text: 'MỞ ĐẦU'}], points: [{at: 14, label: 'Ý thứ nhất'}]};
