// TOKEN NHẬN DIỆN DAVID — một nguồn cho mọi khung dựng (1 video, podcast, ghép, highlight). chu-de.js (remotion) và thuong-hieu.js (ghép)
// đọc lại từ đây. Đổi màu/font của kênh → sửa ở đây (khối 10).
import {Easing, interpolate} from 'remotion';
// *Rgb: bộ ba số để ghép độ trong `rgba(${C.xRgb}, a)` — accentRgb màu nhấn · sangRgb mặt / viền mờ (trắng trên nền tối, nâu đen trên nền sáng)
// · bongRgb bóng đổ · theRgb nền thẻ đặt đè lên video.
export const C = {
  bg: '#0D0D10', card: '#18181C', nen: '#141418', line: 'rgba(255, 255, 255, 0.09)',
  text: '#F4F4F5', muted: '#A1A1AA', dim: '#52525B', accent: '#FF7A45', accentSoft: 'rgba(255, 122, 69, 0.16)',
  accentRgb: '255,122,69', sangRgb: '255,255,255', bongRgb: '0,0,0', theRgb: '13,13,16', trenNhan: '#120C09', khungNguoi: '#FF7A45', khungSang: null, giay: false, bongDo: 0.45, vienThe: true, moCu: true,
  head: '"Barlow Condensed", sans-serif', body: '"Be Vietnam Pro", sans-serif', hoa: 'uppercase',
};
// head / body / hoa: font chữ to, font chữ thường, kiểu chữ hoa của giao diện đang vẽ (mẫu có font riêng thì giao diện đổi; font gần nhất cùng họ
// khi máy không có font của mẫu). bongDo: độ đậm bóng thẻ · vienThe: thẻ có viền mảnh · khungSang: vòng sáng ngoài viền khung người.
// giay: true = nền giấy Sang Huỳnh (sáng giữa, chấm lưới) · 'luoi' = nền giấy Ali Abdaal (phẳng, lưới ô vuông rất mờ).
// GIAO DIỆN THEO MẪU (nhan-dien-chung.md mục 0 điều 2, David 28/11/2026): hiệu ứng học từ hình mẫu giữ trọn thẩm mỹ của mẫu.
// Màu đo từ khung hình gốc (thiet-ke-bo-cuc/nguon-tham-khao/sang-huynh-claude-do-hoa-2026-11-07.md mục "Giao diện đo"). Lấy CHÍNH XÁC màu của mẫu, kể cả màu nhấn — không phối lại
// (David 28/11/2026: "học được mẫu nào thì có thể lấy chính xác từ mẫu đấy … không cần học để phối lại vì tôi thấy phối lại gặp rất nhiều lỗi").
export const GIAO_DIEN = {
  kenh: {...C},
  'sang-huynh-sang': {   // màn đồ hoạ: nền giấy #EEEBE8 → #E5E1DB, thẻ trắng bóng mềm, chữ đen than, chip đen, dấu tích xanh
    bg: '#ECE9E5', card: '#FFFFFF', nen: '#E5E1DB', line: 'rgba(30,24,20,0.10)', text: '#1C1B1A', muted: '#6E6A66', dim: '#BDB7B0',
    accent: '#B5604A', accentSoft: 'rgba(181,96,74,0.13)', accentRgb: '181,96,74', sangRgb: '30,24,20', bongRgb: '70,50,35',
    theRgb: '255,255,255', trenNhan: '#FFFFFF', khungNguoi: '#FFFFFF', xanh: '#49725D', chip: '#201D1A', giay: true, bongDo: 0.16},
  'sang-huynh-the': {   // thẻ trắng đè lên video (đa số khung mẫu: "TẠO SKILL", "Card wall", "MÃ HÃY CHỈ"): thẻ #FFFFFF bóng mềm, chữ đen than,
    // nhãn nhỏ in hoa màu nhấn, viên thuốc trắng chấm nhấn
    bg: '#ECE9E5', card: '#FFFFFF', nen: '#F3F1EE', line: 'rgba(30,24,20,0.10)', text: '#1C1B1A', muted: '#6E6A66', dim: '#BDB7B0',
    accent: '#B5604A', accentSoft: 'rgba(181,96,74,0.12)', accentRgb: '181,96,74', sangRgb: '30,24,20', bongRgb: '40,28,18',
    theRgb: '255,255,255', trenNhan: '#FFFFFF', khungNguoi: '#FFFFFF', xanh: '#49725D', chip: '#201D1A', bongDo: 0.22},
  'sang-huynh-toi': {   // thẻ đè lên video và màn chương: nền #111111, thẻ #30302D, nhãn xám #B0B0AB, chữ kem
    bg: '#111111', card: '#30302D', nen: '#1A1A18', line: 'rgba(255,255,255,0.08)', text: '#F4F2EE', muted: '#B0B0AB', dim: '#55534F',
    accent: '#E79377', accentSoft: 'rgba(231,147,119,0.16)', accentRgb: '231,147,119', sangRgb: '255,255,255', bongRgb: '0,0,0',
    theRgb: '46,46,43', trenNhan: '#120C09', khungNguoi: '#F4F2EE', xanh: '#49725D', chip: '#201D1A'},
  'ali-phan': {   // Ali Abdaal hình cạnh người (1:00–4:00): nét phấn trắng vẽ thẳng lên mảng tối của video, không thẻ nền; chỗ nhấn phấn xanh bạc hà #66F2B6
    accent: '#66F2B6', accentSoft: 'rgba(102,242,182,0.16)', accentRgb: '102,242,182', trenNhan: '#0E2A1F',
    card: 'rgba(255,255,255,0)', nen: 'rgba(255,255,255,0)', line: 'rgba(255,255,255,0.55)', text: '#FFFFFF', muted: 'rgba(255,255,255,0.82)',
    dim: 'rgba(255,255,255,0.45)', theRgb: '0,0,0', sangRgb: '255,255,255', vienThe: false, bongDo: 0},
  'joseph-giay': {   // Joseph minimal (đo khung 4:34): giấy xám #DCDAD7 lấm tấm hạt sẫm, mực xanh coban #1B24B1 một màu, chữ đen than,
    // từ nhấn chữ có chân nghiêng màu mực; cảnh lắng, trích câu (phong 'hat')
    bg: '#DCDAD7', card: '#E8E6E3', nen: '#D2D0CE', line: 'rgba(20,20,40,0.12)', text: '#141416', muted: '#55555C', dim: '#A9A7A4',
    accent: '#1B24B1', accentSoft: 'rgba(27,36,177,0.12)', accentRgb: '27,36,177', sangRgb: '20,20,40', bongRgb: '20,20,40',
    theRgb: '232,230,227', trenNhan: '#FFFFFF', khungNguoi: '#1B24B1', giay: 'hat', bongDo: 0.12, vienThe: false, hoa: 'none',
    head: '"Be Vietnam Pro", sans-serif'},
  'joseph-mo': {   // Joseph (cả ba video): người làm mờ phía sau, đồ hoạ nổi giữa khung; chữ trắng, nhấn xanh coban sáng (phong 'nguoi-mo')
    text: '#FFFFFF', muted: 'rgba(255,255,255,0.78)', dim: 'rgba(255,255,255,0.4)', accent: '#3B5BFF', accentSoft: 'rgba(59,91,255,0.18)',
    accentRgb: '59,91,255', trenNhan: '#FFFFFF', khungNguoi: '#FFFFFF', hoa: 'none', head: '"Be Vietnam Pro", sans-serif'},
  'ali-giay': {   // Ali Abdaal mục lục (đo khung 0:27,5): nền giấy phẳng #FAF5F2 lưới ô rất mờ, thẻ trắng bo 36 px không viền bóng rất nhẹ,
    // chấm số san hô #FF9868 số trắng, chữ có chân đậm đen #0E0E0E viết thường, khung người bo góc viền xanh tím #505D91 + vòng sáng #BCC6ED
    bg: '#FAF5F2', card: '#FFFFFF', nen: '#F5F0ED', line: 'rgba(60,40,30,0.07)', text: '#0E0E0E', muted: '#8A837E', dim: '#D9D2CC',
    accent: '#FF9868', accentSoft: 'rgba(255,152,104,0.16)', accentRgb: '255,152,104', sangRgb: '30,24,20', bongRgb: '90,60,40',
    theRgb: '255,255,255', trenNhan: '#FFFFFF', khungNguoi: '#505D91', khungSang: '#BCC6ED', giay: 'luoi', bongDo: 0.07, vienThe: false, moCu: false,
    head: '"Playfair Display", serif', body: '"Playfair Display", serif', hoa: 'none'},
};
// Mẫu gốc của từng loại cảnh (loại · kiểu → giao diện). Loại không có trong bảng là cảnh tự vẽ của kênh (điều 3): giữ `kenh`.
export const MAU_CUA = {'bocuc:o-nguoi': 'sang-huynh-sang', 'bocuc:the-canh': 'sang-huynh-the', 'bocuc:chuong': 'sang-huynh-toi',
  'DuongMay:thay': 'sang-huynh-the', 'DuongMay:so': 'sang-huynh-toi', 'DuongMay:nhac': 'sang-huynh-the', 'DuongMay:lat': 'sang-huynh-the',
  'bocuc:muc-luc': 'ali-giay', 'bocuc:tien-trinh': 'ali-giay',
  'bocuc:canh-nguoi': 'ali-phan', 'bocuc:cau-hoi': 'sang-huynh-the', 'NhanTram:the': 'sang-huynh-the', 'NhanTram:nhan': 'sang-huynh-the',
  'phong:hat': 'joseph-giay', 'phong:nguoi-mo': 'joseph-mo'};
// HEAD / BODY là liên kết sống: apDungGiaoDien (chu-de.js) gọi datChu khi đổi giao diện, mọi thành phần import HEAD đọc đúng font của cảnh.
export let HEAD = C.head;
export let BODY = C.body;
export const datChu = (t) => { HEAD = t.head; BODY = t.body; };
// Font phụ — CHỈ cho một từ nhấn trong cụm (`*từ*` trong ChuHien), không thay HEAD/BODY (chữ ký nhận diện, nhan-dien-chung.md mục 0)
export const NHAN = '"Playfair Display", serif';
export const ease = (f, a, b, o0 = 0, o1 = 1, e = Easing.out(Easing.cubic)) =>
  interpolate(f, [a, b], [o0, o1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: e});
