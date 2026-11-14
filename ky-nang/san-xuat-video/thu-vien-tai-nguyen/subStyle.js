// PHỤ ĐỀ CHUẨN — MỘT NGUỒN DUY NHẤT cho mọi chế độ (1 video, ghép nhiều clip, podcast). Người dùng chốt: phụ đề hai chế độ
// phải khớp 100% (hộp nền tối bo góc, chữ đậm, giãn dòng đủ cho dấu, đáy vùng an toàn). new_montage.sh chép file này sang
// dự án ghép — sửa kiểu phụ đề CHỈ ở đây.
import React from 'react';

export const SUB = {
  size: 42,                 // dọc 1080×1920 (podcast tự đổi cỡ qua podframe)
  bottomGap: 6,             // đáy hộp cách đáy vùng an toàn
  box: {padding: '10px 22px 13px', borderRadius: 16, background: '#141418'},
  text: {fontWeight: 700, lineHeight: 1.28, textAlign: 'center', textWrap: 'balance',   // dòng dài chia đều, không rơi 1 chữ
    textShadow: '0 2px 8px rgba(0,0,0,0.5)'},
};

// ===== PHỤ ĐỀ VIDEO NGẮN (David chốt 2026-11-04: "người xem là trung tâm — sao chép chuẩn kênh lớn") =====
// PHỤ ĐỀ CLIP DỌC (David chốt 2026-11-08, thay kiểu 1–3 chữ to in hoa của Hormozi/DOAC): mỗi lần hiện MỘT CỤM TRỌN Ý ~5–8 chữ,
// tối đa 2 dòng, cỡ BẰNG chữ trong thẻ motion graphic (58), chữ thường, viền đen mảnh để đọc được trên hình, từ khoá cam.
// Bật cho highlight (luôn) và video 1 người dọc ≤ 90 s (project.short). Video dài, vlog ghép, podcast giữ phụ đề hộp tối (SUB).
// Mỗi lúc chỉ MỘT chỗ chữ: lớp motion graphic có chữ đang hiện → phụ đề ẩn (Captions.jsx / Show.jsx).
export const SHORT_SUB = {
  size: 58,
  text: {fontWeight: 800, lineHeight: 1.24, textAlign: 'center', letterSpacing: 0.2, textWrap: 'balance',
    WebkitTextStroke: '7px #000', paintOrder: 'stroke fill', textShadow: '0 4px 14px rgba(0,0,0,0.6)'},
};
// Chia một dòng phụ đề thành các cụm ≤ maxW chữ / ≤ maxC ký tự (hồ sơ phu_de.ngan_max_chu / ngan_max_ky_tu), CHIA ĐỀU (không để
// cụm cuối lẻ loi), ưu tiên ngắt sau dấu phẩy; CỤM TỪ KHOÁ trong `hl` (kể cả +/-) giữ liền một cụm. Thời gian chia theo độ dài chữ → [{a, b, text}]
const norm = (w) => w.toLowerCase().replace(/[.,!?…:;"“”]/g, '');
export const chunks = (text, len, hl = [], maxW = 10, maxC = 52) => {
  const w = text.split(/\s+/).filter(Boolean);
  const toks = [];   // mỗi token = 1 từ, hoặc cả cụm từ khoá
  const phrases = hl.map((h) => h.replace(/^[+-]/, '').toLowerCase().split(/\s+/).filter(Boolean)).filter((p) => p.length > 1);
  for (let i = 0; i < w.length;) {
    const ph = phrases.find((p) => p.every((x, k) => w[i + k] && norm(w[i + k]) === norm(x)));
    if (ph) { toks.push(w.slice(i, i + ph.length).join(' ')); i += ph.length; } else { toks.push(w[i]); i += 1; }
  }
  const nW = w.length, nC = text.length;
  const n = Math.max(1, Math.ceil(nW / maxW), Math.ceil(nC / maxC));
  const out = [];
  let cur = [], done = 0;   // done = số chữ đã xếp
  toks.forEach((t, i) => {
    cur.push(t);
    const cw = cur.join(' ').split(' ').length;
    const target = Math.round((out.length + 1) * nW / n);   // mốc chia đều
    const next = toks[i + 1];
    const comma = /[,;:]$/.test(t) && done + cw >= target - 2;
    if (next && out.length < n - 1 && (done + cw >= target || comma)) { out.push(cur.join(' ')); done += cw; cur = []; }
  });
  if (cur.length) out.push(cur.join(' '));
  const tot = out.reduce((s, c) => s + c.length + 1, 0);
  let acc = 0;
  return out.map((c) => { const a = Math.round(acc / tot * len); acc += c.length + 1; return {a, b: Math.round(acc / tot * len), text: c}; });
};
// Nhịp đang hiện ở khung f (tính từ đầu dòng) — từ thuộc cụm `hl` tô màu nhấn
export const ShortLine = ({text, hl = [], f, len, font, color, accent, width, size = SHORT_SUB.size, maxW = 10, maxC = 52}) => {   // size/maxW/maxC: hồ sơ phu_de.*
  const ck = chunks(text, len, hl, maxW, maxC);
  const c = ck.find((k) => f >= k.a && f < k.b) || ck[ck.length - 1];
  // MÀU THEO NGHĨA (David duyệt 2026-11-04, học Huỳnh Duy Khương): mục hl bắt đầu "+" = nên làm (xanh lá), "-" = tránh (đỏ),
  // còn lại = cam nhận diện. Vd hl: ['+tỏ rõ', '-nói vòng vo', 'bộ não']
  const words = (arr) => new Set(arr.join(' ').toLowerCase().split(/\s+/).filter(Boolean));
  const good = words(hl.filter((h) => h.startsWith('+')).map((h) => h.slice(1)));
  const bad = words(hl.filter((h) => h.startsWith('-')).map((h) => h.slice(1)));
  const hw = words(hl.filter((h) => !/^[+-]/.test(h)));
  const colorOf = (w) => good.has(w) ? '#3DDC84' : bad.has(w) ? '#FF4D4D' : hw.has(w) ? accent : null;
  const pop = Math.min(1, (f - c.a + 1) / 4);   // hiện nhẹ mỗi cụm
  return (
    <div style={{maxWidth: width, ...SHORT_SUB.text, fontFamily: font, fontSize: size, color,
      opacity: 0.4 + 0.6 * pop, transform: `translateY(${(1 - pop) * 6}px)`}}>
      {c.text.split(' ').map((x, i) => (
        <React.Fragment key={i}>{i > 0 && ' '}
          <span style={colorOf(x.toLowerCase().replace(/[.,!?…:;]/g, '')) ? {color: colorOf(x.toLowerCase().replace(/[.,!?…:;]/g, ''))} : null}>{x}</span></React.Fragment>))}
    </div>
  );
};

// Tô màu nhấn các cụm trong `hl` (cụm nhiều chữ được) — trả về mảng phần tử React
export const highlight = (text, hl0 = [], color) => {
  const tone = Object.fromEntries(hl0.map((h) => [h.replace(/^[+-]/, ''), h[0] === '+' ? '#3DDC84' : h[0] === '-' ? '#FF4D4D' : color]));
  const hl = Object.keys(tone);
  if (!hl.length) return text;
  const re = new RegExp(`(${hl.map((h) => h.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})`, 'g');
  return text.split(re).map((p, i) => (hl.includes(p) ? <span key={i} style={{color: tone[p]}}>{p}</span> : p));
};
