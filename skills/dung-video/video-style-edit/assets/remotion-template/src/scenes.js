// Kịch bản cảnh của dự án — Claude viết lại file này cho mỗi video.
// Mốc thời gian (giây) lấy từ transcript.srt của video gốc.
// type: hook (3 s mở đầu, bắt buộc) · lower · kinetic · card · montage · recap · converge · master (xem references/scene-design.md)
import project from './project.js';

export const FPS = project.fpsNum / project.fpsDen;
export const W = project.width;
export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);

export const SCENES = [
  // {id: 's01-gioi-thieu', type: 'lower', start: 0.3, end: 5.6, props: {name: 'TÊN', role: 'Chủ đề video'}},
];

// Chỉ dùng cho PODCAST (project.podcast — skill podcast-style-edit): sân khấu nền chạy suốt video (components/Stage.jsx).
// show: tên chương trình; title: tên tập; speakers: [{name, role}] theo thứ tự người nói 0, 1 trong speakers.js
// TOPICS: ý đang bàn ở giữa khung (trích lời, ≤ 5 từ/dòng, '\n' tách 2 dòng; mốc = lúc bắt đầu ý) — tự ẩn khi có lớp phủ
// COVER: màn hình bìa ~1 s ghép TRƯỚC video (ảnh bìa cho mạng xã hội). title = tiêu đề NGƯỜI DÙNG đưa (mỗi video hỏi lại),
// '\n' xuống dòng, dòng cuối tô màu nhấn; eyebrow (tuỳ chọn) — mặc định STAGE.show. null = không có bìa.
export const COVER = null;
export const STAGE = null;
export const TOPICS = [];
// CHƯƠNG YOUTUBE (David duyệt 2026-11-04): [{at: giây, text: 'Tên chương — trích lời'}] cho video dài; trống → chapters.py lấy TOPICS
export const CHAPTERS = [];
// Bảng ghi chú chạy (video dày thông tin — trinh-bay/tu-chon.md): tên phần + ý chính nguyên văn cộng dồn theo lời
// export const GHI_CHU = [{phan: 'Tự ra quyết định', at: 0, y: [{text: 'một tuần đào tạo từ A đến Z', at: 12.4}]}];
export const GHI_CHU = [];
export const GHI_CHU_O = null;   // {x, y, w, h} 0–1 khi không có khung chủ thể và muốn ép chỗ

// Chỉ dùng khi xuất ngang từ gốc dọc (output.js layout 'pillar'): chữ hai bên khung, chạy suốt video.
// keywords: từ khoá của ý đang nói (đổi theo từng đoạn, ≤ 3 từ); points: danh sách ý, tích dần theo lời (≤ 9 mục, ≤ 4 từ/mục)
export const SIDES = null;
// export const SIDES = {eyebrow: 'CHỦ ĐỀ', title: 'Tiêu đề video', speaker: 'Tên · vai trò',
//   keywords: [{at: 0.3, text: 'MỞ ĐẦU'}], points: [{at: 14, label: 'Ý thứ nhất'}]};
