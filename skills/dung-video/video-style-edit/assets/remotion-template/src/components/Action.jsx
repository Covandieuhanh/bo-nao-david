// MÀN HÀNH ĐỘNG + MÀN CHỐT (người dùng chốt 2026-11-02): mục tiêu video = người xem HIỂU ý chính rồi LÀM theo.
//
// action — người nói nêu một việc người xem có thể làm ("ra tắm nắng một tí", "tìm hiểu thêm về Haruku và áp dụng") →
//   màn toàn cảnh: biểu tượng của việc đó vẽ dần trong vòng tròn, ô tick bật lên lúc `doneAt` (= "làm được"), bên dưới NGUYÊN VĂN
//   câu nói (`quote`, `**từ**` tô nhấn). Phụ đề tạm ẩn (câu to = phụ đề). props: {icon, quote, quoteAt?, doneAt?, eyebrow?}
//   eyebrow chỉ khi trích được từ lời (vd. 'MỖI NGÀY'); không có thì bỏ.
// cta — MÀN CHỐT ở ~4 s cuối mọi video: câu chốt Claude TỰ SÁNG TẠO theo nội dung từng video (props {text, kind}; kind chọn
//   biểu tượng: comment | save | follow | share — cta.js). Thiếu props → câu dự phòng trong cta.js. Màn toàn cảnh: video gốc vẫn chạy trong khung bo góc
//   phía trên (vẫn thấy vẫy tay/like chào — public/goc.mp4, render.mjs tự nối), câu chốt to bên dưới, phụ đề vẫn chạy ở đáy.
//   Podcast (không có hình): chỉ ô câu chốt, Place đặt giữa sân khấu. props: {text?} ghi đè câu mặc định cho riêng video đó.
import React from 'react';
import {AbsoluteFill, OffthreadVideo, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, SAFE, SAFE_W, ease, inOut, pop, rel} from '../theme';
import {Eyebrow} from './Overlays';
import {FullShell} from './FullScreen';
import {Icon} from '../lib/Icons';
import {Quote} from './CardFull';
import CTA, {CTA_ICONS, CTA_TICK} from '../lib/cta.js';
import project from '../project.js';
import {fr} from '../scenes';

const Tick = ({p, size}) => (
  <div style={{position: 'absolute', right: -size * 0.02, bottom: -size * 0.02, width: size * 0.34, height: size * 0.34, borderRadius: '50%',
    background: '#30A46C', boxShadow: '0 8px 30px rgba(48,164,108,0.55)', display: 'flex', alignItems: 'center', justifyContent: 'center',
    transform: `scale(${p})`}}>
    <svg width={size * 0.2} height={size * 0.2} viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="3.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12.5l4.5 4.5L19 7.5" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - Math.min(1, p)} />
    </svg>
  </div>
);

import HS from '../hoso.json';
// 2 trạng thái: không câu trích dài — chỉ biểu tượng + tick + nhãn ngắn `label` (≤ 4 chữ, cụm việc nguyên văn); phụ đề vẫn chạy
export const Action = ({start, icon = 'check', quote: q0, quoteAt, doneAt, eyebrow, label}) => {
  // 2 trạng thái: nhãn = `label`, không có thì lấy cụm **nhấn** trong câu (cụm việc nguyên văn), tối đa 5 chữ
  const auto = q0 && (q0.match(/\*\*([^*]+)\*\*/) || [])[1];
  const quote = HS.hai_trang_thai ? (label || (auto ? `**${auto.split(/\s+/).slice(0, 5).join(' ')}**` : null)) : q0;
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const size = 300;
  const done = pop(f, doneAt != null ? rel(doneAt, start) : Math.round(d * 0.55));
  return (
    <FullShell>
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 250, height: 1000, display: 'flex', flexDirection: 'column',
        justifyContent: 'center', alignItems: 'flex-start', gap: 56}}>
        <div style={{position: 'relative', width: size, height: size, borderRadius: '50%', border: `3px solid ${C.accent}`,
          background: C.accentSoft, display: 'flex', alignItems: 'center', justifyContent: 'center',
          transform: `scale(${0.85 + 0.15 * pop(f, 2)})`, boxShadow: '0 0 50px rgba(255,122,69,0.25)'}}>
          <Icon name={icon} size={size * 0.62} at={4} stroke={2.8} />
          <Tick p={done} size={size} />
        </div>
        {eyebrow && <Eyebrow style={{marginBottom: -30}}>{eyebrow}</Eyebrow>}
        {quote && <Quote text={quote} start={start} at={quoteAt} />}
      </div>
    </FullShell>
  );
};

// Dấu tick nhỏ ở góc biểu tượng (bật nảy đúng lúc tiếng "ting")
const MiniTick = ({p}) => (
  <div style={{position: 'absolute', right: -6, top: -6, width: 54, height: 54, borderRadius: '50%', background: '#30A46C',
    border: `4px solid ${C.bg}`, display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${p})`,
    boxShadow: `0 0 ${24 * Math.min(1, p)}px rgba(48,164,108,0.8)`}}>
    <svg width={28} height={28} viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="3.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12.5l4.5 4.5L19 7.5" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - Math.min(1, p)} />
    </svg>
  </div>
);

// Ô câu chốt: bong bóng bình luận + ba chấm "đang gõ" → câu hiện từng từ (`**…**` tô nhấn)
const CtaBox = ({text, kind, top, f, tickF}) => {
  const t = text || CTA.text;
  const kd = kind || (text ? 'comment' : CTA.kind);
  const parts = t.split(/(\*\*[^*]+\*\*)/).filter(Boolean);
  const n = t.replace(/\*\*/g, '').length, size = n <= 45 ? 50 : n <= 60 ? 46 : 42;   // ≤ 3 dòng, đáy ô trên dải phụ đề
  let k = 0;
  return (
    <div style={{position: 'absolute', left: SAFE.left, top, width: SAFE_W, padding: '30px 34px', boxSizing: 'border-box',
      borderRadius: 36, background: C.card, border: `2px solid ${C.line}`, boxShadow: '0 30px 80px rgba(0,0,0,0.45)',
      display: 'flex', alignItems: 'center', gap: 30, transform: `translateY(${(1 - pop(f, 4)) * 40}px)`, opacity: ease(f, 2, 10)}}>
      <div style={{position: 'relative', flexShrink: 0, width: 140, height: 140, borderRadius: '50%', background: C.accent,
        display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${1 + 0.04 * Math.sin(f / 6)})`,
        boxShadow: '0 0 60px rgba(255,122,69,0.45)'}}>
        <svg width={82} height={82} viewBox="0 0 24 24" fill="none" stroke={C.bg} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
          {(CTA_ICONS[kd] || CTA_ICONS.comment).map((d, i) => <path key={i} d={d} />)}
        </svg>
        {kd === 'comment' && <div style={{position: 'absolute', top: 55, display: 'flex', gap: 9}}>
          {[0, 1, 2].map((i) => (
            <div key={i} style={{width: 10, height: 10, borderRadius: '50%', background: C.bg,
              opacity: 0.35 + 0.65 * Math.max(0, Math.sin((f - i * 5) / 5))}} />
          ))}
        </div>}
        <MiniTick p={pop(f, tickF, {damping: 9, stiffness: 220, mass: 0.6})} />
      </div>
      <div style={{fontFamily: BODY, fontWeight: 700, fontSize: size, lineHeight: 1.3, color: C.text, textWrap: 'balance'}}>
        {parts.map((part, i) => {
          const hi = part.startsWith('**');
          const ws = part.replace(/\*\*/g, '').split(/(\s+)/).map((w, j) => {
            if (/^\s+$/.test(w)) return w;
            const a = 10 + (k++) * 2;
            return <span key={`${i}-${j}`} style={{opacity: 0.12 + 0.88 * ease(f, a, a + 6), color: hi ? C.accent : C.text}}>{w}</span>;
          });
          return hi && part.length <= 30 ? <span key={i} style={{whiteSpace: 'nowrap'}}>{ws}</span> : ws;
        })}
      </div>
    </div>
  );
};

export const Cta = ({start, text, kind}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  if (project.podcast) {
    return <AbsoluteFill style={{opacity: inOut(f, d, 10, 10)}}><CtaBox text={text} kind={kind} top={SAFE.overlayTop + 10} f={f} tickF={fr(start + CTA_TICK) - fr(start)} /></AbsoluteFill>;
  }
  // khung video: 9:16 thu nhỏ, co dần từ toàn khung vào chỗ (người xem thấy "video lùi lại nhường chỗ cho lời chốt")
  const k = ease(f, 0, 14);
  const w0 = 1080, h0 = 1920, w1 = 400, h1 = Math.round(400 * 16 / 9), x1 = (1080 - w1) / 2, y1 = 240;
  const w = w0 + (w1 - w0) * k, h = h0 + (h1 - h0) * k, x = x1 * k, y = y1 * k;
  return (
    <FullShell hold>
      <div style={{position: 'absolute', left: x, top: y, width: w, height: h, borderRadius: 36 * k, overflow: 'hidden',
        border: k > 0.5 ? `3px solid ${C.accent}` : 'none', boxShadow: '0 30px 90px rgba(0,0,0,0.6)'}}>
        <OffthreadVideo src={staticFile('goc.mp4')} trimBefore={fr(start)} muted style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      </div>
      <CtaBox text={text} kind={kind} top={y1 + h1 + 30} f={f - 8} tickF={fr(start + CTA_TICK) - fr(start) - 8} />
    </FullShell>
  );
};
