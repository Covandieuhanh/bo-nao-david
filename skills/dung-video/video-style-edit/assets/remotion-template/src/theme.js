import {Easing, interpolate, spring} from 'remotion';
import project from './project.js';
import {FPS, fr} from './scenes';

// ===== Phong cách — Claude điền từ style.md (phân tích video mẫu) =====
import {C as _C, HEAD as _H, BODY as _B} from './lib/tokens';   // màu/font: MỘT NGUỒN thư viện hình (khối 10)
export const C = {..._C};
export const HEAD = _H;   // chữ to, tiêu đề
export const BODY = _B;     // chữ thường trong thẻ

// ===== Vùng an toàn =====
// Dọc (Reels/TikTok/Shorts): tránh thanh trên, cột nút bên phải, tiêu đề/mô tả phía dưới.
// Ngang (YouTube): chừa lề 5% (title safe) + thanh điều khiển phía dưới.
// overlayTop: nơi bắt đầu dải lớp phủ, ngay dưới mặt người nói — chỉnh theo khung hình video gốc.
const V = project.height > project.width || !!project.podcast;   // podcast ngang: lớp phủ vẫn vẽ trên dải dọc, Place phóng ra giữa khung
export const SAFE = V
  ? {left: 70, right: 180, top: 210, bottom: 1420, overlayTop: 985}         // khung dọc 1080×1920 (= khung thiết kế)
  : {left: Math.round(project.width * 0.05), right: Math.round(project.width * 0.05),
    top: Math.round(project.height * 0.05), bottom: Math.round(project.height * 0.85), overlayTop: Math.round(project.height * 0.55)};
// DẤU GÓC KÊNH ● DAVID │ chủ đề (Captions.jsx): khung dọc 228 px (dưới thanh trạng thái Reels/TikTok); khung NGANG sát mép trên vùng an toàn
// (lỗi 08/11/2026: dùng số 228 của khung dọc cho khung ngang → dấu góc thấp, đè thẻ). Mọi lớp phủ góc trên trái phải nằm dưới BRAND_BOT.
export const BRAND_TOP = V && !project.podcast ? 228 : SAFE.top;
export const BRAND_BOT = BRAND_TOP + 56;   // chữ 38 px + bóng
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
