// TOKEN NHẬN DIỆN DAVID — một nguồn cho mọi khung dựng (1 video, podcast, ghép, highlight). chu-de.js (remotion) và thuong-hieu.js (ghép)
// đọc lại từ đây. Đổi màu/font của kênh → sửa ở đây (khối 10).
import {Easing, interpolate} from 'remotion';
export const C = {
  bg: '#0D0D10', card: '#18181C', nen: '#141418', line: 'rgba(255, 255, 255, 0.09)',
  text: '#F4F4F5', muted: '#A1A1AA', dim: '#52525B', accent: '#FF7A45', accentSoft: 'rgba(255, 122, 69, 0.16)',
};
export const HEAD = '"Barlow Condensed", sans-serif';
export const BODY = '"Be Vietnam Pro", sans-serif';
// Font phụ — CHỈ cho một từ nhấn trong cụm (`*từ*` trong ChuHien), không thay HEAD/BODY (chữ ký nhận diện, nhan-dien-chung.md mục 0)
export const NHAN = '"Playfair Display", serif';
export const ease = (f, a, b, o0 = 0, o1 = 1, e = Easing.out(Easing.cubic)) =>
  interpolate(f, [a, b], [o0, o1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: e});
