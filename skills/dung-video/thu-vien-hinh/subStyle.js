// PHỤ ĐỀ CHUẨN — MỘT NGUỒN DUY NHẤT cho mọi chế độ (1 video, ghép nhiều clip, podcast). Người dùng chốt: phụ đề hai chế độ
// phải khớp 100% (hộp nền tối bo góc, chữ đậm, giãn dòng đủ cho dấu, đáy vùng an toàn). new_montage.sh chép file này sang
// dự án ghép — sửa kiểu phụ đề CHỈ ở đây.
import React from 'react';

export const SUB = {
  size: 42,                 // dọc 1080×1920 (podcast tự đổi cỡ qua podframe)
  bottomGap: 6,             // đáy hộp cách đáy vùng an toàn
  box: {padding: '10px 22px 13px', borderRadius: 16, background: 'rgba(0,0,0,0.58)'},
  text: {fontWeight: 700, lineHeight: 1.28, textAlign: 'center', textWrap: 'balance',   // dòng dài chia đều, không rơi 1 chữ
    textShadow: '0 2px 8px rgba(0,0,0,0.5)'},
};

// ===== PHỤ ĐỀ VIDEO NGẮN (David chốt 2026-11-04: "người xem là trung tâm — sao chép chuẩn kênh lớn") =====
// 1–3 chữ to mỗi nhịp, in hoa, viền đen dày, không hộp nền, từ khoá cam — kiểu Hormozi / DOAC / Jay Shetty. Bật cho highlight
// (luôn) và video 1 người dọc ≤ 90 s (project.short). Nằm ngang ngực / dưới cằm, trong dải phụ đề cũ → lớp phủ, nâng khung,
// face_place không đổi. Video dài, vlog ghép, podcast giữ phụ đề hộp tối ở trên (SUB).
export const SHORT_SUB = {
  size: 84,
  text: {fontWeight: 800, lineHeight: 1.18, textAlign: 'center', textTransform: 'uppercase', letterSpacing: 0.5,
    WebkitTextStroke: '12px #000', paintOrder: 'stroke fill', textShadow: '0 6px 18px rgba(0,0,0,0.55)'},
};
// Chia một dòng phụ đề thành các nhịp ≤ 3 chữ (≤ 16 ký tự — dài hơn sẽ rớt dòng ở cỡ 84); CỤM TỪ KHOÁ trong `hl` (kể cả +/-)
// được giữ liền trong một nhịp (không tách "TỎ / RÕ"). Thời gian chia theo độ dài chữ → [{a, b, text}] (khung, từ đầu dòng)
const norm = (w) => w.toLowerCase().replace(/[.,!?…:;"“”]/g, '');
export const chunks = (text, len, hl = [], maxW = 3, maxC = 16) => {   // maxW / maxC: hồ sơ phu_de.ngan_max_chu / ngan_max_ky_tu
  const w = text.split(/\s+/).filter(Boolean);
  const toks = [];   // mỗi token = 1 từ, hoặc cả cụm từ khoá
  const phrases = hl.map((h) => h.replace(/^[+-]/, '').toLowerCase().split(/\s+/).filter(Boolean)).filter((p) => p.length > 1);
  for (let i = 0; i < w.length;) {
    const ph = phrases.find((p) => p.every((x, k) => w[i + k] && norm(w[i + k]) === norm(x)));
    if (ph) { toks.push(w.slice(i, i + ph.length).join(' ')); i += ph.length; } else { toks.push(w[i]); i += 1; }
  }
  const out = [];
  let cur = [];
  const words = (arr) => arr.join(' ').split(' ').length;
  for (const t of toks) {
    if (cur.length && (words(cur) + t.split(' ').length > maxW || (cur.join(' ') + ' ' + t).length > maxC)) { out.push(cur.join(' ')); cur = []; }
    cur.push(t);
  }
  if (cur.length) out.push(cur.join(' '));
  const n = out.length;   // chữ lẻ 1 từ ngắn ở cuối → gộp vào nhịp trước nếu vẫn ≤ 16 ký tự
  if (n > 1 && !out[n - 1].includes(' ') && out[n - 1].length <= 3 && (out[n - 2] + ' ' + out[n - 1]).length <= maxC) out.splice(n - 2, 2, `${out[n - 2]} ${out[n - 1]}`);
  const tot = out.reduce((s, c) => s + c.length + 1, 0);
  let acc = 0;
  return out.map((c) => { const a = Math.round(acc / tot * len); acc += c.length + 1; return {a, b: Math.round(acc / tot * len), text: c}; });
};
// Nhịp đang hiện ở khung f (tính từ đầu dòng) — từ thuộc cụm `hl` tô màu nhấn
export const ShortLine = ({text, hl = [], f, len, font, color, accent, width, size = SHORT_SUB.size, maxW = 3, maxC = 16}) => {   // size/maxW/maxC: hồ sơ phu_de.*
  const ck = chunks(text, len, hl, maxW, maxC);
  const c = ck.find((k) => f >= k.a && f < k.b) || ck[ck.length - 1];
  // MÀU THEO NGHĨA (David duyệt 2026-11-04, học Huỳnh Duy Khương): mục hl bắt đầu "+" = nên làm (xanh lá), "-" = tránh (đỏ),
  // còn lại = cam nhận diện. Vd hl: ['+tỏ rõ', '-nói vòng vo', 'bộ não']
  const words = (arr) => new Set(arr.join(' ').toLowerCase().split(/\s+/).filter(Boolean));
  const good = words(hl.filter((h) => h.startsWith('+')).map((h) => h.slice(1)));
  const bad = words(hl.filter((h) => h.startsWith('-')).map((h) => h.slice(1)));
  const hw = words(hl.filter((h) => !/^[+-]/.test(h)));
  const colorOf = (w) => good.has(w) ? '#3DDC84' : bad.has(w) ? '#FF4D4D' : hw.has(w) ? accent : null;
  const pop = Math.min(1, (f - c.a + 1) / 3);   // bật nhẹ mỗi nhịp
  return (
    <div style={{maxWidth: width, ...SHORT_SUB.text, fontFamily: font, fontSize: size, color,
      transform: `scale(${0.9 + 0.1 * pop})`, transformOrigin: '50% 100%'}}>
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
