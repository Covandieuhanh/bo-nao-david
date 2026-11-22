// INTRO TIÊU ĐỀ (mẫu dùng lại, từ việc #39 22/11 — David: "làm cả intro ấn tượng") — chỉ dùng khi David yêu cầu intro (khối 06), chữ nguyên văn lời David.
// Chữ nguyên văn lời David trong video: "địa điểm để tổ chức cái sự kiện chữa lành doanh nhân số đầu tiên".
// Nhịp: chớp sáng → dòng nhỏ → từng chữ của tên chương trình rơi vào → "SỐ ĐẦU TIÊN" đập to, quét sáng → nhoè ra nhường lời David.
// Khung ngang: căn giữa; khung dọc: cỡ chữ tự co theo bề rộng.
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {C, HEAD, BODY} from '../thu-vien/bien-thiet-ke';
import {EASE, k, tien} from '../thu-vien/chuyen-dong';
import {VN} from '../khung-podcast';

const kep = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};

export const IntroTieuDe = ({eyebrow, eyebrowAt = 0.15, title, titleAt = 0.45, big, bigAt = 1.25}) => {
  const f = useCurrentFrame(); const {fps, width: W, height: H, durationInFrames: d} = useVideoConfig();
  const g = (s) => k(s, fps);
  const safeW = W * 0.86;
  const sT = Math.min(124, Math.floor(safeW / (title.length * 0.5)));
  const sB = Math.min(250, Math.floor(safeW / (big.length * 0.52)));
  const out = interpolate(f, [d - 10, d], [0, 1], {...kep, easing: EASE.ra});
  const flash = interpolate(f, [0, 6], [0.5, 0], kep) + interpolate(f, [g(bigAt), g(bigAt) + 3, g(bigAt) + 12], [0, 0.45, 0], kep);
  const nen = tien(f, 0, 10);
  // chữ to: đập từ 1,7 xuống 1, rung nhẹ khi chạm
  const pB = tien(f, g(bigAt), 9, EASE.vao);
  const rung = f >= g(bigAt) + 9 ? Math.sin((f - g(bigAt) - 9) * 1.9) * 6 * Math.max(0, 1 - (f - g(bigAt) - 9) / 14) : 0;
  const quet = interpolate(f, [g(bigAt) + 8, g(bigAt) + 26], [-0.3, 1.3], kep);
  const vach = tien(f, g(eyebrowAt), 16);
  const words = title.split(' ');
  const stB = {fontFamily: HEAD, fontWeight: 800, fontSize: sB, lineHeight: VN.lh, whiteSpace: 'nowrap', letterSpacing: 2,
    padding: `${sB * VN.top * 0.5}px 0.1em ${sB * VN.bot}px`};
  return (
    <AbsoluteFill style={{opacity: 1 - out, filter: out ? `blur(${out * 10}px)` : undefined, transform: `scale(${1 + out * 0.08})`}}>
      <AbsoluteFill style={{opacity: nen, background:
        'radial-gradient(ellipse 70% 62% at 50% 52%, rgba(13,13,16,0.52) 0%, rgba(13,13,16,0.72) 60%, rgba(13,13,16,0.9) 100%)'}} />
      <AbsoluteFill style={{background: '#fff', opacity: flash}} />
      <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', flexDirection: 'column'}}>
        {/* dòng nhỏ + hai vạch cam chạy ra hai bên */}
        <div style={{display: 'flex', alignItems: 'center', gap: 26, opacity: tien(f, g(eyebrowAt), 8)}}>
          <div style={{width: 160 * vach, height: 5, borderRadius: 3, background: C.accent}} />
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 36, color: C.accent, textShadow: '0 4px 20px rgba(0,0,0,0.6)',
            letterSpacing: 4 + 10 * (1 - vach)}}>{eyebrow}</div>
          <div style={{width: 160 * vach, height: 5, borderRadius: 3, background: C.accent}} />
        </div>
        {/* tên chương trình: từng chữ rơi vào */}
        <div style={{display: 'flex', gap: sT * 0.26, marginTop: sT * 0.25}}>
          {words.map((w, i) => {
            const a = g(titleAt) + i * 3; const p = tien(f, a, 10, EASE.vao);
            return <div key={i} style={{fontFamily: HEAD, fontWeight: 800, fontSize: sT, lineHeight: VN.lh, color: C.text, whiteSpace: 'nowrap',
              padding: `${sT * VN.top * 0.5}px 0 ${sT * VN.bot}px`, textShadow: '0 8px 36px rgba(0,0,0,0.7)', opacity: p,
              transform: `translateY(${(1 - p) * -sT * 0.6}px)`, filter: p < 1 ? `blur(${(1 - p) * 8}px)` : undefined}}>{w}</div>;
          })}
        </div>
        {/* SỐ ĐẦU TIÊN: đập to + quét sáng */}
        {/* luôn giữ chỗ để khối chữ không nhảy khi chữ to vào */}
        {(
          <div style={{position: 'relative', marginTop: -sB * 0.12, opacity: f >= g(bigAt) ? Math.min(1, pB * 1.6) : 0,
            transform: `scale(${1.7 - 0.7 * pB}) translateX(${rung}px)`}}>
            <div style={{...stB, color: C.accent, textShadow: '0 10px 50px rgba(0,0,0,0.6), 0 0 60px rgba(255,122,69,0.35)'}}>{big}</div>
            <div style={{...stB, position: 'absolute', inset: 0, color: 'transparent',
              backgroundImage: `linear-gradient(105deg, transparent ${quet * 100 - 12}%, rgba(255,255,255,0.95) ${quet * 100}%, transparent ${quet * 100 + 12}%)`,
              WebkitBackgroundClip: 'text', backgroundClip: 'text'}}>{big}</div>
          </div>
        )}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
