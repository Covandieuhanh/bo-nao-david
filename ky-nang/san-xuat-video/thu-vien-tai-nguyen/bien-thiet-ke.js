// TOKEN NHẬN DIỆN DAVID — một nguồn cho mọi khung dựng (1 video, podcast, ghép, highlight). chu-de.js (remotion) và thuong-hieu.js (ghép)
// đọc lại từ đây. Đổi màu/font của kênh → sửa ở đây (khối 10).
import {Easing, interpolate} from 'remotion';
// *Rgb: bộ ba số để ghép độ trong `rgba(${C.xRgb}, a)` — accentRgb màu nhấn · sangRgb mặt / viền mờ (trắng trên nền tối, nâu đen trên nền sáng)
// · bongRgb bóng đổ · theRgb nền thẻ đặt đè lên video.
export const C = {
  bg: '#0D0D10', card: '#18181C', nen: '#141418', line: 'rgba(255, 255, 255, 0.09)',
  text: '#F4F4F5', muted: '#A1A1AA', dim: '#52525B', accent: '#FF7A45', accentSoft: 'rgba(255, 122, 69, 0.16)',
  accentRgb: '255,122,69', sangRgb: '255,255,255', bongRgb: '0,0,0', theRgb: '13,13,16', trenNhan: '#120C09', khungNguoi: '#FF7A45', giay: false,
};
// GIAO DIỆN THEO MẪU (nhan-dien-chung.md mục 0 điều 2, David 28/11/2026): hiệu ứng học từ hình mẫu giữ trọn thẩm mỹ của mẫu.
// Màu đo từ khung hình gốc (thiet-ke-bo-cuc/nguon-tham-khao/sang-huynh-claude-do-hoa-2026-11-07.md mục "Giao diện đo"); cam của kênh thay chỗ nhấn của mẫu.
export const GIAO_DIEN = {
  kenh: {...C},
  'sang-huynh-sang': {   // màn đồ hoạ: nền giấy #EEEBE8 → #E5E1DB, thẻ trắng bóng mềm, chữ đen than, chip đen, dấu tích xanh
    bg: '#ECE9E5', card: '#FFFFFF', nen: '#E5E1DB', line: 'rgba(30,24,20,0.10)', text: '#1C1B1A', muted: '#6E6A66', dim: '#BDB7B0',
    accent: '#E0612F', accentSoft: 'rgba(224,97,47,0.13)', accentRgb: '224,97,47', sangRgb: '30,24,20', bongRgb: '70,50,35',
    theRgb: '255,255,255', trenNhan: '#FFFFFF', khungNguoi: '#FFFFFF', xanh: '#49725D', chip: '#201D1A', giay: true},
  'sang-huynh-toi': {   // thẻ đè lên video và màn chương: nền #111111, thẻ #30302D, nhãn xám #B0B0AB, chữ kem
    bg: '#111111', card: '#30302D', nen: '#1A1A18', line: 'rgba(255,255,255,0.08)', text: '#F4F2EE', muted: '#B0B0AB', dim: '#55534F',
    accent: '#FF7A45', accentSoft: 'rgba(255,122,69,0.16)', accentRgb: '255,122,69', sangRgb: '255,255,255', bongRgb: '0,0,0',
    theRgb: '46,46,43', trenNhan: '#120C09', khungNguoi: '#F4F2EE', xanh: '#49725D', chip: '#201D1A'},
};
// Mẫu gốc của từng loại cảnh (loại · kiểu → giao diện). Loại không có trong bảng là cảnh tự vẽ của kênh (điều 3): giữ `kenh`.
export const MAU_CUA = {'bocuc:o-nguoi': 'sang-huynh-sang', 'bocuc:the-canh': 'sang-huynh-toi', 'bocuc:chuong': 'sang-huynh-toi',
  'DuongMay:thay': 'sang-huynh-toi', 'DuongMay:so': 'sang-huynh-toi', 'DuongMay:nhac': 'sang-huynh-toi'};
export const HEAD = '"Barlow Condensed", sans-serif';
export const BODY = '"Be Vietnam Pro", sans-serif';
// Font phụ — CHỈ cho một từ nhấn trong cụm (`*từ*` trong ChuHien), không thay HEAD/BODY (chữ ký nhận diện, nhan-dien-chung.md mục 0)
export const NHAN = '"Playfair Display", serif';
export const ease = (f, a, b, o0 = 0, o1 = 1, e = Easing.out(Easing.cubic)) =>
  interpolate(f, [a, b], [o0, o1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: e});
