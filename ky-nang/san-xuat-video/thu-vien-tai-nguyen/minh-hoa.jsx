// CẢNH MINH HOẠ TOÀN MÀN HÌNH — một kiểu của bố cục tự cân (khối 07; "2 trạng thái" 04/11 đã bỏ 07/11). Một bản cho mọi khung dựng.
// Người xem chỉ có MỘT điểm nhìn: hình động minh hoạ đúng ý đang nói + phụ đề vẫn chạy bên dưới (không câu trích dài, không chữ to).
// props:
//   mode : 'single' (1 hình lớn) · 'flow' (A → B → C) · 'vs' (A ✗ | B ✓) · 'count' (số chạy + biểu tượng) · 'list' (2–5 hình hiện dần)
//   items: [{icon: '<tên bieu-tuong.jsx>', at: <giây — cùng hệ giây với `start`>, label?: '≤ 3 chữ', good?: true|false (vs)}]
//   label: nhãn chung ≤ 3 chữ (tên riêng / con số / cụm đắt — TRÍCH lời), hiện dưới hình; bỏ trống được
//   num  : {to: 15, from?: 0, at, unit?: 'PHÚT', dur?: 1.2}  (mode 'count' — đúng con số người nói)
//   start: giây bắt đầu cảnh (cùng hệ giây với items[].at) — khung dựng truyền sẵn
// Vùng vẽ: dọc 10%–56% chiều cao (chừa đáy cho phụ đề + nút nền tảng) · ngang 12%–80% (dưới dấu góc, trên phụ đề); tự cân theo khung dọc / ngang.
import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease} from './bien-thiet-ke';
import {Icon} from './bieu-tuong';
import {NenPhong, usePhong} from './phong';

const cl = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const Arrow = ({s, o, flip}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none" stroke={C.accent} strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"
    style={{opacity: o, transform: flip ? 'scaleX(-1)' : 'none'}}><path d="M4 12h15M13 6l6 6-6 6" strokeDasharray="30" strokeDashoffset={30 * (1 - o)} /></svg>
);
const Mark = ({good, s, o}) => (
  <div style={{position: 'absolute', right: -s * 0.08, top: -s * 0.08, width: s * 0.34, height: s * 0.34, borderRadius: s, opacity: o,
    background: good ? '#3DDC84' : '#FF4D4D', display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${o})`,
    boxShadow: `0 0 30px ${good ? 'rgba(61,220,132,0.5)' : 'rgba(255,77,77,0.5)'}`}}>
    <svg width={s * 0.22} height={s * 0.22} viewBox="0 0 24 24" fill="none" stroke="#0D0D10" strokeWidth="3.4" strokeLinecap="round">
      {good ? <path d="M5 12.5l4.5 4.5L19 7.5" /> : <path d="M6 6l12 12M18 6L6 18" />}</svg>
  </div>
);

// KIỂU VÀO theo ý của câu (khối 07 — không để mọi cảnh cùng "trồi lên"): 1 hình = phóng tại chỗ · nhân quả = đi theo hướng đọc ·
// so sánh = hai phía tiến vào · danh sách = trồi lên lần lượt. Hình đã vào là ĐỨNG YÊN (không lơ lửng, không vòng xoay).
const enter = (mode, i, p, sz) => {
  const d = (1 - p) * sz * 0.22;
  if (mode === 'flow') return `translateX(${-d}px)`;
  if (mode === 'vs') return `translateX(${i === 0 ? -d : d}px)`;
  if (mode === 'list') return `translateY(${d}px)`;
  return `scale(${0.82 + 0.18 * p})`;
};

export const Illus = ({mode = 'single', items = [], label = '', num = null, start = 0, len, compact = false, nen = true}) => {   // nen=false: không vẽ nền (lồng trong bố cục BoCuc)   // compact: chừa giữa khung cho chữ chính
  const f = useCurrentFrame();
  const {fps, width: W, height: H, durationInFrames} = useVideoConfig();
  const L = len || durationInFrames;
  const rel = (t) => Math.round(((t ?? start) - start) * fps);
  const land = W > H, M = Math.min(W, H);
  const {phong} = usePhong();
  const out = interpolate(f, [L - 5, L], [1, 0], cl);   // ra ngắn hơn vào ~40% (vào 8 khung · ra 5 khung)
  const n = Math.max(1, items.length);
  // khung ngang (podcast 1920×1080): hình nhỏ hơn để cả dấu ✓/✗ + nhãn nằm gọn trong vùng vẽ (2026-11-05: bản cũ bị cắt mép trên)
  const sz = compact ? M * 0.36 : mode === 'count' ? M * (land ? 0.22 : 0.5) : mode === 'single' ? M * (land ? 0.34 : 0.5) : n === 2 ? M * (land ? 0.26 : 0.36) : M * (land ? 0.2 : 0.24);
  const icon = (it, i) => {
    const a = rel(it.at), p = spring({frame: f - a, fps, config: {damping: 14, stiffness: 150, mass: 0.7}});
    const dim = mode === 'vs' && it.good === false ? 0.55 : 1;
    return (
      <div key={i} style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: sz * 0.1, opacity: Math.min(1, p * 1.3) * dim,
        transform: enter(mode, i, p, sz)}}>
        <div style={{position: 'relative', width: sz, height: sz}}>
          <svg width={sz} height={sz} style={{position: 'absolute', inset: 0}}>
            <circle cx={sz / 2} cy={sz / 2} r={sz * 0.47} fill="rgba(255,122,69,0.07)" stroke={C.accent} strokeOpacity={0.32} strokeWidth={2}
              strokeDasharray={`${sz * 0.06} ${sz * 0.05}`} />
          </svg>
          <div style={{position: 'absolute', left: sz * 0.18, top: sz * 0.18, filter: 'drop-shadow(0 0 22px rgba(255,122,69,0.45))'}}>
            <Icon name={it.icon} size={sz * 0.64} at={a} stroke={sz > 400 ? 2.6 : 3} />
          </div>
          {mode === 'vs' && typeof it.good === 'boolean' && <Mark good={it.good} s={sz} o={ease(f, a + 14, a + 22)} />}
        </div>
        {it.label && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: Math.round(sz * (n > 2 ? 0.2 : 0.16)), color: C.text,
          textTransform: 'uppercase', letterSpacing: 1, opacity: ease(f, a + 8, a + 16), textAlign: 'center', maxWidth: sz * 1.3}}>{it.label}</div>}
      </div>
    );
  };
  // số chạy (count): đúng con số người nói, chạy trong `dur` giây từ `at`
  let numEl = null;
  if (mode === 'count' && num) {
    const a = rel(num.at), d = Math.round((num.dur || 1.2) * fps);
    const v = Math.round(interpolate(f, [a, a + d], [num.from || 0, num.to], {...cl, easing: (x) => 1 - Math.pow(1 - x, 3)}));
    numEl = (
      <div style={{display: 'flex', alignItems: 'baseline', gap: M * 0.02, opacity: ease(f, a, a + 6)}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: M * (land ? 0.17 : 0.3), lineHeight: 1, color: C.accent,
          fontVariantNumeric: 'tabular-nums', textShadow: '0 0 60px rgba(255,122,69,0.35)'}}>{v.toLocaleString('vi-VN')}</div>
        {num.unit && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: M * (land ? 0.06 : 0.08), color: C.text, textTransform: 'uppercase'}}>{num.unit}</div>}
      </div>
    );
  }
  const first = items.length ? rel(items[0].at) : 0;
  const row = mode === 'flow' || mode === 'vs' || mode === 'list';
  // list 4–5 hình ở khung dọc: lưới 2 cột (một cột tràn khỏi vùng vẽ — vlog VF3 2026-11-05); khung ngang / ≤ 3 hình: một hàng
  const grid = mode === 'list' && !land && n > 3;
  return (
    <AbsoluteFill style={{opacity: Math.min(ease(f, 0, 8), out)}}>
      {nen && phong && <NenPhong />}
      {nen && !phong && <AbsoluteFill style={{background: C.bg}} />}
      {nen && !phong && <AbsoluteFill style={{background: `radial-gradient(circle at 50% ${land ? 42 : 38}%, rgba(255,122,69,0.2), transparent 60%)`}} />}
      <div style={{position: 'absolute', left: W * 0.06, right: W * 0.06, top: compact ? H * 0.115 : H * (land ? 0.12 : 0.1), height: compact ? H * 0.235 : H * (land ? 0.68 : 0.46), display: 'flex', flexDirection: 'column',
        alignItems: 'center', justifyContent: 'center', gap: M * 0.05}}>
        {numEl}
        <div style={{display: 'flex', flexDirection: row ? 'row' : 'column', flexWrap: mode === 'list' ? 'wrap' : 'nowrap', alignItems: 'center',
          justifyContent: 'center', gap: M * 0.035, ...(grid ? {width: sz * 2.7 + M * 0.035, rowGap: M * 0.02} : {})}}>
          {items.map((it, i) => (
            <React.Fragment key={i}>
              {mode === 'flow' && i > 0 && <Arrow s={sz * 0.32} o={ease(f, rel(it.at) - 6, rel(it.at) + 4)} />}
              {mode === 'vs' && i > 0 && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: sz * 0.22, color: C.muted,
                opacity: ease(f, rel(it.at) - 6, rel(it.at))}}>VS</div>}
              {icon(it, i)}
            </React.Fragment>
          ))}
        </div>
        {label && <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: M * 0.018,
          opacity: ease(f, first + 10, first + 20), transform: `translateY(${(1 - ease(f, first + 10, first + 20)) * 20}px)`}}>
          <div style={{width: M * 0.12 * ease(f, first + 12, first + 26), height: 6, borderRadius: 3, background: C.accent}} />
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: M * (land ? 0.07 : 0.085), lineHeight: 1.1, paddingTop: '0.1em', color: C.text,
            textTransform: 'uppercase', textAlign: 'center'}}>{label}</div>
        </div>}
      </div>
    </AbsoluteFill>
  );
};
