// Chuyển cảnh HIGHLIGHT (skill cat-highlight-video): ở mỗi mối nhảy sang đoạn khác của tập gốc, ~0,4 s "tua nhanh" —
// tối dần, vệt sáng quét ngang, biểu tượng ⏩ (⏪ khi đoạn kế nằm TRƯỚC trong tập gốc) + mốc phút của đoạn kế trong tập gốc. Người xem thấy ngay đây là đoạn
// trích từ video dài. Vẽ trong lớp phụ đề (trên cùng). Dữ liệu: highlight.js (jumps). Tiếng "vút tua": render_preview.py.
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import HL from '../highlight.js';
import {C, HEAD} from '../theme';

const mmss = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
// vệt quét: vị trí dọc, dày, dài, lệch pha — cố định để mọi lần render giống nhau
const STREAKS = Array.from({length: 16}, (_, i) => ({y: (i * 137) % 100, h: 2 + (i * 7) % 6, w: 18 + (i * 29) % 40, ph: (i * 0.37) % 1}));

export const Tua = () => {
  const f = useCurrentFrame();
  const {fps, width: W, height: H} = useVideoConfig();
  const t = f / fps;
  const j = HL?.jumps?.find((x) => t >= x.at && t < x.at + x.dur);
  if (!j) return null;
  const p = (t - j.at) / j.dur;                      // 0 → 1 trong khoảng chuyển
  const o = Math.sin(Math.PI * p);                   // hiện nhanh, tắt nhanh
  const s = Math.min(54, Math.round(W * 0.05));
  const back = j.src_to < j.src_from;               // nhảy lùi trong tập gốc → tua lùi
  const soft = j.tone === 'lang';                    // tông lắng: tối dần, không vệt quét, chip viền cam (không tiếng vút — render_preview)
  return (
    <AbsoluteFill style={{background: `rgba(10,10,12,${(soft ? 0.78 : 0.62) * o})`}}>
      {!soft && STREAKS.map((k, i) => {
        const q = ((p * 2.2 + k.ph) % 1.4) - 0.4;      // quét trái → phải (tua tới), phải → trái (tua lùi)
        const x = back ? 1 - q - k.w / 100 : q;
        return <div key={i} style={{position: 'absolute', top: `${k.y}%`, left: `${x * 100}%`, width: `${k.w}%`, height: k.h,
          borderRadius: k.h, opacity: 0.55 * o, background: `linear-gradient(90deg, transparent, ${i % 3 ? C.text : C.accent})`}} />;
      })}
      <div style={{position: 'absolute', left: 0, right: 0, top: H * 0.42, display: 'flex', justifyContent: 'center',
        opacity: Math.min(1, o * (soft ? 1.2 : 1.6)), transform: soft ? 'none' : `translateX(${(back ? 0.5 - p : p - 0.5) * 60}px) scale(${0.92 + 0.12 * o})`}}>
        <div style={{display: 'flex', alignItems: 'center', gap: s * 0.5, padding: `${s * 0.3}px ${s * 0.6}px`, borderRadius: s,
          background: soft ? 'rgba(24,24,28,0.9)' : C.accent, border: soft ? `2px solid ${C.accent}` : 'none',
          boxShadow: soft ? 'none' : '0 0 60px rgba(255,122,69,0.55)'}}>
          <svg width={s * 1.3} height={s} viewBox="0 0 26 20" fill={soft ? C.accent : C.bg} style={{transform: back ? 'scaleX(-1)' : 'none'}}>
            <path d="M1 1 L12 10 L1 19 Z M13 1 L24 10 L13 19 Z" /></svg>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: s * 1.25, lineHeight: 1, color: soft ? C.text : C.bg, fontVariantNumeric: 'tabular-nums'}}>
            {mmss(j.src_to)}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};
