// Kịch bản dựng (EDL) — Claude viết lại cho từng dự án. Ví dụ đầy đủ đã duyệt: references/vi-du-danh-sach-cat.js
// Mọi mốc theo giây trong clip gốc (src); T(id, src) tự quy đổi sang giây trên timeline.
export const FPS = 30;
export const W = 1080;
export const H = 1920;
export const fr = (s) => Math.round(s * FPS);

// ===== Các đoạn hình, theo thứ tự phát =====
// clip: file trong public/clips (c1, c2, … do tao-dung-ghep.sh đặt tên) · from/to: giây trong clip
// rate: tốc độ (1.5 = tua nhanh, 0.4 = phát chậm) · freeze: giữ 1 khung tại `from` trong N giây
// vol: âm lượng tiếng gốc (0 = tắt) · audio: {clip, from, vol} lấy tiếng chỗ khác (hình vẫn của clip này)
// fit: 'blur' cho hình ngang đặt trên nền mờ · zoom: [{at (src), s, x, y, len}] cú zoom dồn
// zoomIn: [từ, đến, x, y] zoom chậm suốt đoạn · grade: 'title' | 'replay' | 'dark'
// cite: {label?, fit?} đoạn TRÍCH DẪN — viết bằng hàm cite() bên dưới, đừng tự ghép tay
//
// cite({id, clip, from, over: [clipChính, a, b], label}) — chèn hình clip minh hoạ `clip` (từ giây `from`) đúng lúc người
// nói ở clipChính nói câu [a, b]: hình nằm trong khung bo góc, tắt tiếng; tiếng clipChính chạy tiếp. Đoạn clip chính
// trước/sau tách ở đúng a và b (mốc từ words.srt). Minh hoạ ngắn hơn câu nói → rate < 1 (≥ 0,6) hoặc freeze.
// label: chữ nhỏ trên khung, TRÍCH từ câu nói (vd. 'MỖI NGÀY 15 PHÚT ĐỂ VIẾT'); bỏ trống nếu không cần.
const cite = ({id, clip, from, over: [main, a, b], label, rate = 1, fit}) =>
  ({id, clip, from, to: from + (b - a) * rate, rate, audio: {clip: main, from: a, vol: 1}, cite: {label, fit}});

const RAW = [
  {id: 'teaser', clip: 'c1', from: 0, to: 3, vol: 1},
  {id: 'title', clip: 'c1', from: 0, to: 2.8, vol: 0, grade: 'title'},
  {id: 'r1a', clip: 'c1', from: 3, to: 8, vol: 1},
  {id: 'outro', clip: 'c1', from: 8, to: 11, vol: 0, grade: 'dark'},
];

let acc = 0;
export const SEGS = RAW.map((s) => {
  const rate = s.rate || 1;
  const dur = s.freeze || (s.to - s.from) / rate;
  const seg = {...s, rate, start: acc, dur};
  acc += fr(dur) / FPS;
  return seg;
});
export const TOTAL = acc;
const byId = Object.fromEntries(SEGS.map((s) => [s.id, s]));
// Đoạn trích dẫn: `src` tính theo giây của clip CHÍNH đang nói (phụ đề/lớp phủ gắn vào lời nói, không vào hình minh hoạ)
export const T = (id, src) => {
  const s = byId[id];
  if (s.cite) return s.start + (src - s.audio.from);
  return s.start + (s.freeze ? 0 : (src - s.from) / s.rate);
};
export const segStart = (id) => byId[id].start;
export const segEnd = (id) => byId[id].start + byId[id].dur;

// ===== Phụ đề: [đoạn, từ (src), đến (src), chữ, [từ khoá tô màu nhấn]] =====
const SUB = [
  // ['r1a', 3.2, 5.0, 'Câu nói đã sửa chính tả', ['khoá']],
];
// who (tuỳ chọn, cảnh hội thoại): 1 | 2 = viền ô phụ đề theo người nói (cam / xanh) — vị trí, cỡ chữ giữ chuẩn kieu-phu-de.js
export const SUBS = SUB.map(([id, a, b, text, hl, who]) => ({start: T(id, a), end: T(id, b), text, hl, who}));

// ===== Lớp đồ hoạ (type xem TYPES trong chuong-trinh.jsx) =====
export const OVERLAYS = [
  {type: 'teaserTag', start: 0, end: segEnd('teaser')},
  {type: 'title', start: segStart('title'), end: segEnd('title')},
  {type: 'hud', start: segEnd('title'), end: segStart('outro')},
  {type: 'round', start: segStart('r1a'), end: segStart('r1a') + 2.3, n: 1, text: 'TÊN VÒNG'},
  {type: 'outro', start: segStart('outro'), end: TOTAL},
];

// ===== Hiệu ứng âm thanh (file trong public/sfx, tạo bởi tao-am-thanh.mjs) =====
export const SFX = [
  {f: 'whoosh', at: segStart('title') - 0.25, v: 0.8},
  {f: 'boom', at: segStart('title'), v: 0.9},
  {f: 'sting', at: segStart('title') + 0.05, v: 0.55},
  {f: 'tada', at: segStart('outro') + 0.1, v: 0.6},
];

// Nhạc nền: base bình thường · duck khi có phụ đề · loud ở tiêu đề/replay/kết
export const MUSIC = {base: 0.2, duck: 0.08, loud: 0.34, loudRanges: [[segStart('title'), segEnd('title')], [segStart('outro'), TOTAL]]};

// MÀN CHỐT ~4 s cuối (mọi video — người dùng chốt): câu chốt Claude TỰ SÁNG TẠO sau khi nắm toàn bộ nội dung (luật trong
// SKILL.md). kind: 'comment' | 'save' | 'follow' | 'share' (biểu tượng); '**…**' = tô nhấn.
export const CTA = {text: 'David rất mong có được sự góp ý của bạn **tại phần bình luận**!', kind: 'comment'};

// HIGHLIGHT (skill cat-doan-noi-bat — scripts/danh-sach-cat-doan-noi-bat.py viết sẵn cả file): vlog thường để null / [].
// HL = {src_duration}: bật thanh của CẢ tập gốc ở đáy + chip tua ở đoạn `jump` ({id, clip, from, freeze: 0.4, vol: 0, jump: {from, to}}).
// TONE = [[từ, đến, 'lang' | 'soi']] giây timeline. MUSIC.tracks = [{f, a, b, gain}] — f là file public/hieu-ung-am-thanh/<f>.mp3.
export const HL = null;
export const TONE = [];
// Thẻ cuối dẫn về bản đầy đủ (highlight): {title: '<tên tập gốc>', speaker: '<tên người nói gốc>', clip: 'c1', at: <giây>, len: 1.8} — null = không có
export const ENDCARD = null;
