// CHUYỂN ĐỘNG DÙNG CHUNG (khối 07 · học 09/11/2026 từ luật chuyển động của HyperFrames `references/motion.md` — học ý, tự viết lại,
// không cài HyperFrames: ghi nhớ video-bo-ung-dung). Mọi thành phần lấy easing / kiểu chữ hiện / thoát ở đây, để cả
// 4 loại video cùng một "tay nghề". Không đổi màu, font, bố cục — chỉ cách VÀO, ĐỨNG, RA.
//
// Luật (giá trị mặc định; cảnh nào cố ý làm khác thì ghi lý do trong ke-hoach-canh.md):
// 1. Easing theo VAI, không một kiểu cho mọi thứ: vào = đuôi dài (exp/quart out) · camera, đổi nền = inOut · ra / zoom xuyên = tăng tốc (in).
// 2. Vào chậm, ra gọn: ra ngắn hơn vào 40–50 %, một chuyển động liền (không trượt–dừng–đi).
// 3. Nối gối: phần sau bắt đầu khi phần trước xong 30–50 %. So le: chữ cái 1 khung · từ 60–120 ms · mục danh sách 40–80 ms.
// 4. Chữ đã vào là ĐỨNG YÊN (khối 07); chuyển động dời sang phần tử kế tiếp. Đổi kiểu vào trong một video, không phải lúc nào cũng mờ + trượt lên.
// 5. Giữ đủ đọc: 0,5 s + 0,3 s mỗi từ; câu cuối video ≥ 2 s. Thoát bằng mờ nhoè + tan 0,13–0,25 s.
// 6. Lò xo theo độ tắt dần ζ: 1 không nảy · 0,7–0,85 sang · 0,4–0,6 vui · < 0,3 hoạt hình. Vị trí/cỡ được nảy; độ mờ, màu thì không.
// 7. Dấu hiệu "máy làm" — tránh: thở/trôi/nhấp nháy lặp thay cho chuyển động; chữ còn trượt/phóng sau khi đã vào; mọi cảnh vào
//    giống nhau; mọi phần tử mờ dần + trượt lên.
import {Easing, interpolate} from 'remotion';

export const EASE = {
  vao: Easing.out(Easing.exp),            // đến nơi: đuôi dài
  vaoMem: Easing.out(Easing.poly(4)),     // đến nơi, êm hơn (quart)
  camera: Easing.inOut(Easing.quad),      // zoom/đẩy khung, đổi màu nền
  ra: Easing.in(Easing.cubic),            // rời đi / zoom xuyên: tăng tốc
};

// giây → khung
export const k = (giay, fps) => Math.round(giay * fps);

const kep = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
export const tien = (f, a, dai, e = EASE.vao) => interpolate(f, [a, a + Math.max(1, dai)], [0, 1], {...kep, easing: e});

// Lò xo theo ζ (độ tắt dần) thay vì số damping trần: cau_hinh(0.8) → {damping, stiffness, mass} cho spring() của Remotion.
export const loXo = (zeta = 0.8, stiffness = 140, mass = 0.7) => ({damping: 2 * zeta * Math.sqrt(stiffness * mass), stiffness, mass});

// VÀO + RA của một khối: trả {opacity, filter, scale} cho style. vao/ra tính bằng khung. kieu: 'mo' (mờ nhoè → nét) · 'phong' (hơi to → vừa).
export const vaoRa = (f, d, {vao = 9, ra = 5, mo = 10, kieu = 'mo'} = {}) => {
  const i = tien(f, 0, vao), o = 1 - tien(f, d - ra, ra, EASE.ra);
  const blur = mo * (1 - i) + mo * 0.8 * (1 - o);
  return {opacity: Math.min(i, o), filter: blur > 0.05 ? `blur(${blur.toFixed(2)}px)` : undefined,
    scale: kieu === 'phong' ? 1.04 - 0.04 * i : 1};
};

// CHỮ HIỆN TỪNG TỪ — ba kiểu, đổi kiểu giữa các cảnh để không lặp:
//  'mo'   từng từ: mờ 6 px → nét, trong suốt → rõ, 0,13 s, cách nhau ~0,067 s, không dịch chỗ
//  'muc'  từng từ: xám nhạt → màu chữ, cách nhau 0,07–0,1 s, không dịch chỗ
//  'dong' cả dòng: mờ 8 px → nét trong 0,13–0,2 s
// tu(f, a, i, fps, kieu) → style cho từ thứ i (a = khung bắt đầu của cả dòng).
export const tu = (f, a, i, fps, kieu = 'mo') => {
  if (kieu === 'dong') {
    const p = tien(f, a, k(0.18, fps));
    return {opacity: p, filter: p < 1 ? `blur(${(8 * (1 - p)).toFixed(2)}px)` : undefined};
  }
  if (kieu === 'muc') {
    const p = tien(f, a + i * k(0.085, fps), k(0.2, fps), EASE.vaoMem);
    return {opacity: 0.22 + 0.78 * p};
  }
  const p = tien(f, a + i * Math.max(1, k(0.067, fps)), Math.max(2, k(0.13, fps)));
  return {opacity: p, filter: p < 1 ? `blur(${(6 * (1 - p)).toFixed(2)}px)` : undefined};
};

// Chọn kiểu chữ hiện theo cảnh (cố định theo id → render lại vẫn ra một kiểu, nhưng các cảnh khác nhau thì khác kiểu).
const KIEU = ['mo', 'muc', 'dong'];
export const kieuChu = (id = '', uuTien) => uuTien || KIEU[[...String(id)].reduce((s, c) => (s * 31 + c.charCodeAt(0)) >>> 0, 7) % KIEU.length];

// Thời gian đọc tối thiểu (giây) của một dòng chữ.
export const docDu = (chu = '') => 0.5 + 0.3 * String(chu).trim().split(/\s+/).filter(Boolean).length;
