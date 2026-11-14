// Kịch bản dựng "NGÀY NHẬN XE" — mọi mốc theo giây trong clip gốc (src), tự quy đổi sang giây trên timeline.
export const FPS = 30;
export const W = 1080;
export const H = 1920;
export const fr = (s) => Math.round(s * FPS);

// ===== Các đoạn hình, theo thứ tự phát =====
// clip: file trong public/clips · from/to: giây trong clip · rate: tốc độ · freeze: giữ 1 khung (giây)
// vol: âm lượng tiếng gốc · audio: lấy tiếng từ chỗ khác · fit 'blur': hình ngang đặt trên nền mờ
// zoom: [{at (src), s, x, y}] cú zoom dồn · grade: 'replay' | 'dark' | 'title'
const RAW = [
  {id: 'teaser', clip: 'c2497', from: 4.9, to: 8.7, vol: 1, zoom: [{at: 5.35, s: 1.18, x: 0.47, y: 0.43, len: 1.0}]},
  {id: 'title', clip: 'c2496', from: 0, to: 2.8, vol: 0, grade: 'title'},
  {id: 'r1a', clip: 'c2495', from: 0.4, to: 3.0, rate: 1.7, vol: 0.5},
  {id: 'r1b', clip: 'c2495', from: 3.0, to: 7.6, rate: 1.5, vol: 0.5},
  {id: 'r1c', clip: 'c2495', from: 7.6, to: 10.3, vol: 0.8, zoom: [{at: 8.05, s: 1.22, x: 0.6, y: 0.28, len: 1.6}]},
  {id: 'r2a', clip: 'c2496', from: 0, to: 4.1, vol: 0.6},
  {id: 'r2b', clip: 'c2497', from: 0, to: 6.45, vol: 1, zoom: [{at: 5.15, s: 1.15, x: 0.47, y: 0.43, len: 1.3}]},
  {id: 'freeze', clip: 'c2497', from: 5.9, to: 5.9, freeze: 2.0, zoomIn: [1.06, 1.14, 0.47, 0.43]},
  {id: 'r2c', clip: 'c2497', from: 6.45, to: 8.6, vol: 1},
  {id: 'r2d', clip: 'c2497', from: 8.6, to: 14.3, vol: 1, zoom: [{at: 13.4, s: 1.16, x: 0.3, y: 0.4, len: 0.9}]},
  {id: 'r2e', clip: 'c2497', from: 14.3, to: 17.9, rate: 1.8, vol: 0},
  {id: 'r3a', clip: 'c2497', from: 17.9, to: 24.4, vol: 1},
  {id: 'replay', clip: 'c2497', from: 4.9, to: 6.3, rate: 0.4, vol: 0, grade: 'replay'},
  {id: 'r3c', clip: 'c2497', from: 24.4, to: 29.6, vol: 1},
  {id: 'outro', clip: 'c2497', from: 29.6, to: 33.0, rate: 0.85, vol: 0, grade: 'dark'},
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
// Giây trong clip của đoạn `id` → giây trên timeline
export const T = (id, src) => {
  const s = byId[id];
  return s.start + (s.freeze ? 0 : (src - s.from) / s.rate);
};
export const segStart = (id) => byId[id].start;
export const segEnd = (id) => byId[id].start + byId[id].dur;

// ===== Phụ đề (chữ trắng viền đen, từ khoá vàng) =====
// Viết lại gọn và đúng chính tả từ transcript Whisper
const SUB = [
  ['teaser', 5.25, 6.45, 'Đã mua được', []],
  ['teaser', 6.45, 8.4, 'con VF3 này, quá đẹp!', ['VF3', 'quá', 'đẹp!']],
  ['r2b', 0.15, 2.7, 'Chị mình là…', []],
  ['r2b', 2.7, 5.25, 'sau khoảng thời gian rất cố gắng', ['rất', 'cố', 'gắng']],
  ['r2b', 5.25, 6.45, 'đã mua được', []],
  ['r2c', 6.45, 8.5, 'con VF3 này, quá đẹp!', ['VF3', 'quá', 'đẹp!']],
  ['r2d', 8.6, 10.5, 'Em quay lại làm kỷ niệm đây', ['kỷ', 'niệm']],
  ['r2d', 10.5, 11.25, 'sau này còn có…', []],
  ['r3a', 18.2, 20.1, 'Nhìn tổng quan con này', []],
  ['r3a', 20.1, 21.7, 'nó cứ đẹp hơn', ['đẹp', 'hơn']],
  ['r3a', 21.7, 24.4, 'con VF3 bình thường nhỉ?', ['VF3']],
  ['r3c', 24.5, 26.6, 'Thật không biết', []],
  ['r3c', 26.6, 29.6, 'tả như thế nào luôn!', ['tả']],
];
export const SUBS = SUB.map(([id, a, b, text, hl]) => ({start: T(id, a), end: T(id, b), text, hl}));

// ===== Lớp đồ hoạ =====
export const OVERLAYS = [
  {type: 'teaserTag', start: 0, end: T('teaser', 7.5)},
  {type: 'pow', start: T('teaser', 7.5), end: segEnd('teaser'), text: 'QUÁ ĐẸP.', y: 300},
  {type: 'title', start: segStart('title'), end: segEnd('title')},
  {type: 'hud', start: segEnd('title'), end: segStart('replay')},
  {type: 'hud', start: segEnd('replay'), end: segStart('outro')},
  {type: 'round', start: segStart('r1a'), end: segStart('r1a') + 2.3, n: 1, text: 'ĐƯỜNG TỚI SHOWROOM'},
  {type: 'pow', start: T('r1c', 8.15), end: segEnd('r1c'), text: 'PHẤN KHÍCH.', y: 1060},
  {type: 'round', start: segStart('r2a'), end: segStart('r2a') + 2.3, n: 2, text: 'GẶP CHỦ XE'},
  {type: 'pointer', start: segStart('r2a') + 1.6, end: segEnd('r2a'), text: 'XE ĐÂY RỒI!', x: 860, y: 900, side: 'left'},
  {type: 'nameCard', start: segStart('freeze'), end: segEnd('freeze'), tag: 'NHÂN VẬT CHÍNH', name: 'CHỊ GÁI', sub: 'Chủ nhân VF3 mới tinh'},
  {type: 'pointer', start: T('r2c', 7.45), end: segEnd('r2c'), text: 'VF3', x: 740, y: 900, side: 'left'},
  {type: 'chips', start: T('r2d', 11.25), end: T('r2d', 13.35), items: [['1 NĂM SAU', T('r2d', 11.33)], ['2 NĂM SAU', T('r2d', 11.93)], ['3 NĂM SAU', T('r2d', 12.53)]]},
  {type: 'pow', start: T('r2d', 13.35), end: segEnd('r2d'), text: 'CÒN LÊN ĐỜI NỮA.', y: 960},
  {type: 'round', start: segStart('r3a'), end: segStart('r3a') + 2.3, n: 3, text: 'SOI XE'},
  {type: 'callout', start: T('r3a', 19.2), end: T('r3a', 21.3), text: 'NƠ SIÊU TO', dx: -250, dy: -270,
    track: [[19.2, 615, 1005], [19.8, 660, 960], [20.4, 480, 990], [21.0, 480, 960]].map(([t, x, y]) => [T('r3a', t), x, y])},
  {type: 'callout', start: T('r3a', 19.6), end: T('r3a', 21.3), text: 'BIỂN SỐ MỚI', dx: 250, dy: -40,
    track: [[19.2, 465, 1230], [19.8, 525, 1185], [20.4, 345, 1230], [21.0, 315, 1195]].map(([t, x, y]) => [T('r3a', t), x, y])},
  {type: 'replay', start: segStart('replay'), end: segEnd('replay'), text: 'Nụ cười của chủ xe mới'},
  {type: 'pow', start: T('r3c', 26.7), end: segEnd('r3c'), text: 'ĐẸP KHÔNG TẢ NỔI.', y: 300},
  {type: 'outro', start: segStart('outro'), end: TOTAL},
];

// ===== Hiệu ứng âm thanh =====
export const SFX = [
  {f: 'pop', at: 0.05, v: 0.5},
  {f: 'ding2', at: T('teaser', 7.5), v: 0.6},
  {f: 'whoosh', at: segStart('title') - 0.25, v: 0.8},
  {f: 'boom', at: segStart('title'), v: 0.9},
  {f: 'sting', at: segStart('title') + 0.05, v: 0.55},
  {f: 'whoosh', at: segStart('r1a') - 0.2, v: 0.7},
  {f: 'pop', at: segStart('r1a') + 0.15, v: 0.5},
  {f: 'pop', at: T('r1c', 8.15), v: 0.6},
  {f: 'ding1', at: T('r1c', 8.2), v: 0.45},
  {f: 'whoosh', at: segStart('r2a') - 0.2, v: 0.7},
  {f: 'pop', at: segStart('r2a') + 0.15, v: 0.5},
  {f: 'pop', at: segStart('r2a') + 1.6, v: 0.45},
  {f: 'shutter', at: segStart('freeze'), v: 0.8},
  {f: 'ding4', at: segStart('freeze') + 0.35, v: 0.45},
  {f: 'pop', at: T('r2c', 7.45), v: 0.45},
  {f: 'ding1', at: T('r2d', 11.33), v: 0.55},
  {f: 'ding2', at: T('r2d', 11.93), v: 0.55},
  {f: 'ding3', at: T('r2d', 12.53), v: 0.55},
  {f: 'boom', at: T('r2d', 13.35), v: 0.75},
  {f: 'whoosh', at: segStart('r2e'), v: 0.6},
  {f: 'whoosh', at: segStart('r3a') - 0.15, v: 0.6},
  {f: 'pop', at: segStart('r3a') + 0.15, v: 0.5},
  {f: 'pop', at: T('r3a', 19.2), v: 0.4},
  {f: 'pop', at: T('r3a', 19.6), v: 0.4},
  {f: 'rewind', at: segStart('replay') - 0.1, v: 0.6},
  {f: 'pop', at: T('r3c', 26.7), v: 0.55},
  {f: 'ding2', at: T('r3c', 26.75), v: 0.45},
  {f: 'whoosh', at: segStart('outro') - 0.2, v: 0.6},
  {f: 'tada', at: segStart('outro') + 0.1, v: 0.6},
];

// Nhạc nền: âm lượng theo đoạn, tự hạ khi có lời nói
export const MUSIC = {base: 0.2, duck: 0.08, loud: 0.34, loudRanges: [[segStart('title'), segEnd('title')], [segStart('replay'), segEnd('replay')], [segStart('outro'), TOTAL]]};
