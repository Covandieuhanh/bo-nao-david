// Thanh thời gian (podcast): đáy vùng an toàn, cho người xem biết video còn bao lâu. Vẽ cùng lớp phụ đề (trên cùng).
// HIGHLIGHT (highlight.js có dữ liệu — skill cat-highlight-video): thanh của CẢ tập gốc — các đoạn được trích tô cam mờ, phần
// đã phát cam đậm, chấm ở vị trí đang phát trong tập gốc (lướt nhanh qua khoảng tua), mốc "3:45 · 7:32".
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import HL from '../highlight.js';
import {BODY, C} from '../theme';
import {POD, PF, PF_W} from '../podframe';
import {STAGE} from '../scenes';
import {ThanhThoiGian} from '../lib/ThanhThoiGian';

const mmss = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

// mốc trong tập gốc tại giây t của dự án này
const srcAt = (t) => {
  const j = HL.jumps.find((x) => t >= x.at && t < x.at + x.dur);
  if (j) { const p = (t - j.at) / j.dur; const e = p * p * (3 - 2 * p); return j.src_from + (j.src_to - j.src_from) * e; }
  let s = HL.segs[0];
  for (const x of HL.segs) if (t >= x.clip_start) s = x;
  return Math.min(s.src_end, s.src_start + Math.max(0, t - s.clip_start));
};

export const Timeline = () => {
  const f = useCurrentFrame();
  const {durationInFrames: d, fps} = useVideoConfig();
  const label = {fontFamily: BODY, fontWeight: 600, fontSize: 24, color: C.muted, fontVariantNumeric: 'tabular-nums', whiteSpace: 'nowrap'};
  const box = {position: 'absolute', left: PF.left, width: PF_W, top: PF.tl.y, height: PF.tl.h, display: 'flex', alignItems: 'center', gap: 18};
  const track = {position: 'relative', flex: 1, height: 8, borderRadius: 4, background: 'rgba(255,255,255,0.18)'};
  const dot = (p) => <div style={{position: 'absolute', left: `${p * 100}%`, top: 4, width: 18, height: 18, borderRadius: 9, background: C.text,
    transform: 'translate(-50%, -50%)', boxShadow: '0 0 12px rgba(255,122,69,0.7)'}} />;
  if (HL && HL.bar !== false) {   // bar: false (mặc định từ 2026-11-04) → thanh thường của clip
    const t = f / fps, T = HL.src_duration, now = srcAt(t);
    const bar = (a, w, op) => <div style={{position: 'absolute', left: `${a / T * 100}%`, width: `${w / T * 100}%`, top: 0, bottom: 0,
      borderRadius: 4, background: C.accent, opacity: op}} />;
    // video người nói: nền hình sáng (trời, tường) làm thanh + mốc khó đọc → dải nền tối mờ phía sau
    const plate = POD ? {} : {background: '#141418', borderRadius: PF.tl.h, padding: '0 16px', boxSizing: 'border-box'};
    return (
      <div style={{...box, ...plate}}>
        <div style={{...label, color: C.text}}>{mmss(now)}</div>
        <div style={track}>
          {HL.segs.map((s, i) => (
            <React.Fragment key={i}>
              {bar(s.src_start, s.src_end - s.src_start, 0.35)}
              {t >= s.clip_start && bar(s.src_start, Math.max(0, Math.min(s.src_end, now) - s.src_start), 1)}
            </React.Fragment>
          ))}
          {dot(now / T)}
        </div>
        <div style={{...label, color: POD ? C.muted : C.text}}>{mmss(T)}</div>
      </div>
    );
  }
  const ep = STAGE && STAGE.episode;   // số tập + ngày (2026-11-05, kiểu "đài phát thanh" Hieu Nguyen): {n, date}
  const truoc = ep && (ep.n != null || ep.date) ? <div style={{...label, color: C.accent, fontWeight: 800}}>{ep.n != null ? `TẬP ${ep.n}` : ''}{ep.date ? <span style={{color: C.muted, fontWeight: 600}}>{ep.n != null ? ' · ' : ''}{ep.date}</span> : null}</div> : null;
  // thanh thường = thành phần chung của mọi khung dựng (thu-vien-hinh/ThanhThoiGian.jsx); vị trí theo PF (= nhan-dien.js)
  return <ThanhThoiGian t={f / fps} T={(d - 1) / fps} k={{tl: {left: PF.left, right: PF.right, y: PF.tl.y, h: PF.tl.h}}} nen={!POD} truoc={truoc} />;
};
