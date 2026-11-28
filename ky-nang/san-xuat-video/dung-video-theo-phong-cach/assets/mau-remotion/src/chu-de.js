import {Easing, interpolate, spring} from 'remotion';
import project from './du-an.js';
import {FPS, fr} from './canh';

// ===== Phong cách — Claude điền từ phong-cach.md (phân tích video mẫu) =====
import {C as _C, HEAD as _H, BODY as _B, NHAN as _N, GIAO_DIEN, MAU_CUA} from './thu-vien/bien-thiet-ke';   // màu/font: MỘT NGUỒN thư viện hình (khối 10)
export const C = {..._C};
// Giao diện theo mẫu của từng cảnh (nhan-dien-chung.md mục 0 điều 2). `props.giao_dien` ghi đè; không có thì tra MAU_CUA theo loại cảnh.
// goc.jsx gọi apDungGiaoDien trước khi vẽ mỗi khung, nên mọi thành phần đọc C đều theo đúng giao diện của cảnh đang vẽ (phụ đề, dấu góc: kenh).
export const giaoDienCua = (type, p = {}) => {
  if (p.giao_dien) return p.giao_dien;
  const kieu = type === 'bocuc' ? (p.kieu || 'o-nguoi') : type === 've' && p.ve === 'DuongMay'
    ? (p.thay ? 'thay' : p.so != null && p.lon ? 'so' : p.nhac ? 'nhac' : '') : '';
  const ten = type === 've' ? p.ve : type;
  return MAU_CUA[`${ten}:${kieu}`] || 'kenh';
};
export const apDungGiaoDien = (ten) => Object.assign(C, GIAO_DIEN.kenh, GIAO_DIEN[ten] || {});
export const HEAD = _H;   // chữ to, tiêu đề
export const NHAN = _N;   // một từ nhấn (chữ có chân, nghiêng) — `*từ*` trong chữ
export const BODY = _B;     // chữ thường trong thẻ

// ===== Vùng an toàn =====
// Dọc (Reels/TikTok/Shorts): tránh thanh trên, cột nút bên phải, tiêu đề/mô tả phía dưới.
// Ngang (YouTube): lề 5% mọi phía (title safe SMPTE 90%); thanh thời gian + phụ đề nằm sát đáy, nội dung dùng tới ~82%.
// overlayTop: nơi bắt đầu dải lớp phủ, ngay dưới mặt người nói — chỉnh theo khung hình video gốc.
const V = project.height > project.width || !!project.podcast;   // podcast ngang: lớp phủ vẫn vẽ trên dải dọc, Place phóng ra giữa khung
import {khung} from './thu-vien/nhan-dien-thuong-hieu';
export const SAFE = V
  ? {left: 70, right: 180, top: 210, bottom: 1420, overlayTop: 985}         // khung dọc 1080×1920 (= khung thiết kế)
  : {left: Math.round(project.width * 0.05), right: Math.round(project.width * 0.05),
    top: Math.round(project.height * 0.05), bottom: Math.round(project.height * 0.95), overlayTop: Math.round(project.height * 0.55)};
// DẤU GÓC KÊNH ● DAVID │ chủ đề (phu-de.jsx): khung dọc 228 px (dưới thanh trạng thái Reels/TikTok); khung NGANG sát mép trên vùng an toàn
// (lỗi 08/11/2026: dùng số 228 của khung dọc cho khung ngang → dấu góc thấp, đè thẻ). Mọi lớp phủ góc trên trái phải nằm dưới BRAND_BOT.
export const BRAND_TOP = khung(project.width, project.height).brand.top;   // một nguồn: thu-vien-tai-nguyen/nhan-dien-thuong-hieu.js
export const BRAND_BOT = BRAND_TOP + 64;   // ô nền sẫm: chữ 38 px + đệm
export const SAFE_W = (V ? 1080 : project.width) - SAFE.left - SAFE.right;

// Đổi mốc thời gian tuyệt đối (giây trong video gốc) sang khung tính từ đầu cảnh
export const rel = (abs, sceneStart) => fr(abs) - fr(sceneStart);

export const pop = (frame, at = 0, config = {damping: 16, stiffness: 140, mass: 0.7}) =>
  spring({frame: frame - at, fps: FPS, config});

export const ease = (frame, from, to, outFrom = 0, outTo = 1, easing = Easing.out(Easing.cubic)) =>
  interpolate(frame, [from, to], [outFrom, outTo], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing});

// Vào/ra chung cho mọi clip: mờ + trượt nhẹ
export const inOut = (frame, total, inLen = 10, outLen = 8) => {
  const a = ease(frame, 0, inLen);
  const b = ease(frame, total - outLen, total, 1, 0, Easing.in(Easing.cubic));
  return Math.min(a, b);
};
