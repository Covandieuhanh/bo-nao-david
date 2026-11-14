// Màn hình BÌA (podcast): ~1 giây ghép TRƯỚC video (xem-truoc-ban-dung.py) để mạng xã hội lấy làm ảnh bìa. Đứng yên (ảnh bìa = khung đầu).
// Tiêu đề do NGƯỜI DÙNG đưa (mỗi video hỏi lại) → COVER.title trong canh.js; '\n' = xuống dòng bắt buộc, dòng cuối tô màu nhấn.
// Tự chia dòng cho chữ to nhất có thể (≤ 4 dòng), giãn dòng tiếng Việt (VN). Trang trí: quầng cam, lưới, vòng micro, sóng âm.
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {BODY, C, HEAD} from '../chu-de';
import {COVER, STAGE} from '../canh';
import {LAND, PF, PF_W, VN} from '../khung-podcast';

const G = LAND
  ? {box: {x: PF.left, y: 150, w: 1160, h: 600}, max: 168, ring: {x: 1530, y: 450, r: 190}, wave: {y: 800, h: 80}}
  : {box: {x: PF.left, y: 800, w: PF_W, h: 440}, max: 150, ring: {x: 485, y: 530, r: 170}, wave: {y: 1290, h: 80}};

// Chia một đoạn chữ thành k dòng cân nhất (dòng dài nhất ngắn nhất)
const splitK = (words, k) => {
  if (k <= 1 || words.length <= 1) return [words.join(' ')];
  let best = null;
  for (let i = 1; i < words.length; i++) {
    const rest = splitK(words.slice(i), k - 1);
    const lines = [words.slice(0, i).join(' '), ...rest];
    const m = Math.max(...lines.map((l) => l.length));
    if (!best || m < best.m) best = {m, lines};
  }
  return best.lines;
};

// Chọn cách chia (mỗi đoạn 1–3 dòng, tổng ≤ 4) cho cỡ chữ lớn nhất vừa khung
const layout = (title) => {
  const segs = title.toUpperCase().split('\n').map((s) => s.trim()).filter(Boolean);
  const combos = segs.reduce((acc) => acc.flatMap((c) => [1, 2, 3].map((k) => [...c, k])), [[]]);
  let best = null;
  for (const ks of combos) {
    const n = ks.reduce((a, b) => a + b, 0);
    if (n > 4) continue;
    const lines = segs.flatMap((s, i) => splitK(s.split(' '), ks[i]).map((t) => ({t, accent: i === segs.length - 1 && segs.length > 1})));
    const longest = Math.max(...lines.map((l) => l.t.length));
    const size = Math.min(G.max, G.box.w / (longest * 0.46), G.box.h / (n * VN.lh + (n - 1) * VN.gap + VN.bot));
    if (!best || size > best.size + 0.5) best = {size: Math.floor(size), lines};
  }
  return best;
};

export const Cover = () => {
  const {title = '', eyebrow} = COVER || {};
  const {show = '', speakers = []} = STAGE || {};
  const tag = eyebrow ?? show;
  const {size, lines} = layout(title || ' ');
  const names = speakers.filter((s) => s && s.name).map((s) => s.name).join(' · ');
  const n = LAND ? 72 : 40, gap = 8, bw = (PF_W - gap * (n - 1)) / n;
  return (
    <AbsoluteFill style={{background: C.bg}}>
      <AbsoluteFill style={{background: `radial-gradient(circle at ${LAND ? '78% 40%' : '50% 28%'}, rgba(255,122,69,0.30), transparent 55%)`}} />
      <AbsoluteFill style={{backgroundImage: `linear-gradient(${C.line} 2px, transparent 2px), linear-gradient(90deg, ${C.line} 2px, transparent 2px)`,
        backgroundSize: '120px 120px', opacity: 0.35, maskImage: 'radial-gradient(circle at 60% 40%, black, transparent 80%)'}} />
      {/* Vòng micro */}
      {[1.55, 1.3, 1.08].map((k, i) => (
        <div key={i} style={{position: 'absolute', left: G.ring.x - G.ring.r * k, top: G.ring.y - G.ring.r * k, width: G.ring.r * 2 * k, height: G.ring.r * 2 * k,
          borderRadius: '50%', border: `${i === 2 ? 4 : 2}px solid ${C.accent}`, opacity: 0.18 + i * 0.16}} />
      ))}
      <div style={{position: 'absolute', left: G.ring.x - G.ring.r * 0.8, top: G.ring.y - G.ring.r * 0.8, width: G.ring.r * 1.6, height: G.ring.r * 1.6,
        borderRadius: '50%', background: C.accent, boxShadow: '0 0 120px rgba(255,122,69,0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <svg width={G.ring.r * 0.85} height={G.ring.r * 0.85} viewBox="0 0 24 24" fill="none" stroke={C.bg} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
          <rect x="9" y="3" width="6" height="11" rx="3" /><path d="M5 11a7 7 0 0 0 14 0M12 18v3" />
        </svg>
      </div>
      {/* Tiêu đề */}
      <div style={{position: 'absolute', left: G.box.x, top: G.box.y, width: G.box.w, height: G.box.h, display: 'flex', flexDirection: 'column',
        justifyContent: LAND ? 'center' : 'flex-start'}}>
        {tag && <div style={{alignSelf: 'flex-start', padding: '8px 18px 9px', borderRadius: 10, background: C.accent, marginBottom: 22,
          fontFamily: BODY, fontWeight: 700, fontSize: 28, letterSpacing: 3, color: C.bg}}>{tag.toUpperCase()}</div>}
        {lines.map((l, i) => (
          <div key={i} style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: VN.lh, marginTop: i ? size * VN.gap : 0,
            paddingTop: i ? 0 : size * 0.04, color: l.accent ? C.accent : C.text, whiteSpace: 'nowrap', textShadow: '0 8px 40px rgba(0,0,0,0.5)'}}>{l.t}</div>
        ))}
        <div style={{width: '32%', height: 10, borderRadius: 5, background: C.accent, marginTop: size * 0.3}} />
        {names && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 34, color: C.muted, marginTop: 22}}>{names}</div>}
      </div>
      {/* Sóng âm tĩnh */}
      <div style={{position: 'absolute', left: PF.left, top: G.wave.y, width: PF_W, height: G.wave.h, display: 'flex', alignItems: 'center', gap}}>
        {Array.from({length: n}).map((_, i) => {
          const v = (0.25 + 0.75 * Math.sin(Math.PI * (i + 0.5) / n)) * (0.55 + 0.45 * Math.abs(Math.sin(i * 1.7)));
          return <div key={i} style={{width: bw, height: Math.max(6, v * G.wave.h), borderRadius: bw / 2, background: C.accent, opacity: 0.35 + 0.5 * v}} />;
        })}
      </div>
    </AbsoluteFill>
  );
};
