// ĐIỂM NHẤN TRÊN NGƯỜI (type 'nhan' — David chốt 2026-11-07): làm nổi người đang nói ở câu đắt, KHÔNG che mặt.
// props: text ('CHỮ NHẤN', '\n' xuống dòng, ≤ 4 chữ, trích lời) · icon (tên trong lib/Icons) · at (giây tuyệt đối lúc bật)
//        zoom (vd 1.15 — zoom dồn vào mặt, render_preview.py làm trên video gốc) · toi (true = làm tối viền quanh người)
// Vị trí mặt: mat.js (scripts/nhan_place.py). Chữ / biểu tượng đặt bên phía còn trống cạnh mặt; khung dọc hẹp → dưới cằm.
import React from 'react';
import {AbsoluteFill, Easing, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, SAFE, BRAND_BOT, ease, pop, rel} from '../theme';
import {Icon} from '../lib/Icons';
import project from '../project.js';
import MAT from '../mat.js';

const W = project.width, H = project.height;
// Vị trí mặt SAU zoom (cùng công thức với render_preview.py: khung zoom canh giữa mặt, kẹp trong khung hình)
export const zoomed = (m, Z) => {
  const x0 = Math.max(0, Math.min(1 - 1 / Z, m.cx - 0.5 / Z)), y0 = Math.max(0, Math.min(1 - 1 / Z, m.cy - 0.5 / Z));
  return {cx: (m.cx - x0) * Z, cy: (m.cy - y0) * Z, w: m.w * Z, h: m.h * Z,
    l: ((m.l ?? m.cx - m.w / 2) - x0) * Z, r: ((m.r ?? m.cx + m.w / 2) - x0) * Z};
};

export const Nhan = ({sceneId, start, text, icon, at, zoom = 1, toi = false}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d} = useVideoConfig();
  const m = zoomed(MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18, h: 0.3}, zoom || 1);
  const a = at != null ? rel(at, start) : 6;
  const out = ease(f, d - 8, d, 1, 0, Easing.in(Easing.cubic));
  const p = pop(f, a);
  const V = H > W;
  // phía trống: mặt lệch phải → đặt bên trái và ngược lại
  const fx = m.cx * W, fy = m.cy * H, padX = m.w * 0.3 * W;              // chừa tai + tóc + khoảng thở
  const fl = m.l * W - padX, fr_ = m.r * W + padX;
  const leftRoom = fl - SAFE.left, rightRoom = W - SAFE.right - fr_;
  const side = rightRoom >= leftRoom ? 'right' : 'left';
  const room = Math.max(leftRoom, rightRoom);
  const lines = (text || '').split('\n');
  // Cỡ chữ tự thu cho vừa khoảng trống bên cạnh mặt (chữ cô đặc ~0,52 cỡ / ký tự + đệm ô nền). Khung ngang KHÔNG bao giờ xuống
  // dưới cằm (đè miệng + phụ đề — lỗi 07/11/2026); khung dọc hẹp mới đặt dưới cằm.
  const base = (V ? 0.05 : 0.075) * H, minS = (V ? 0.038 : 0.042) * H;
  const chars = Math.max(1, ...lines.map((l) => l.length), icon && !text ? 4 : 1);
  const fit = (room - 0.9 * base) / (0.52 * chars + 0.8);
  const under = V && fit < minS;
  const size = Math.round(under ? base : Math.max(minS, Math.min(base, fit)));
  const box = under
    ? {left: W / 2, maxWidth: W - SAFE.left - SAFE.right, top: Math.min(fy + m.h * 0.75 * H, SAFE.bottom - 140 - size * lines.length * 1.2 - 40), textAlign: 'center', alignItems: 'center'}
    : side === 'right'
      ? {left: fr_, maxWidth: room, top: Math.max(BRAND_BOT + 24, fy - size * lines.length * 0.6), alignItems: 'flex-start', textAlign: 'left'}
      : {right: W - fl, maxWidth: room, top: Math.max(BRAND_BOT + 24, fy - size * lines.length * 0.6), alignItems: 'flex-end', textAlign: 'right'};
  const dx = under ? 0 : (side === 'right' ? -1 : 1) * (1 - p) * 60;
  const cxT = under ? 'translateX(-50%) ' : '';
  return (
    <AbsoluteFill style={{opacity: out}}>
      {toi && <AbsoluteFill style={{opacity: ease(f, 0, 8) * 0.9,
        background: `radial-gradient(ellipse ${m.w * 190}% ${m.h * 160}% at ${m.cx * 100}% ${m.cy * 100}%, transparent 30%, rgba(0,0,0,0.8) 100%)`}} />}
      {(text || icon) && (
        <div style={{position: 'absolute', display: 'flex', flexDirection: 'column', gap: size * 0.18, ...box,
          padding: `${size * 0.28}px ${size * 0.4}px`, borderRadius: size * 0.22,
          background: 'rgba(13,13,16,0.55)', backdropFilter: 'blur(6px)',
          opacity: Math.min(1, p * 1.4), transform: `${cxT}translateX(${dx}px) scale(${0.85 + 0.15 * p})`,
          transformOrigin: side === 'right' ? 'left center' : under ? 'center top' : 'right center'}}>
          {icon && <div style={{filter: 'drop-shadow(0 0 18px rgba(255,122,69,0.55)) drop-shadow(0 4px 14px rgba(0,0,0,0.6))'}}>
            <Icon name={icon} size={size * 2.1} at={a} stroke={3} /></div>}
          {text && lines.map((l, i) => (
            <div key={i} style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: 1.12, letterSpacing: 2,
              color: lines.length > 1 && i === lines.length - 1 ? C.accent : C.text, whiteSpace: 'nowrap',
              textShadow: '0 4px 24px rgba(0,0,0,0.75), 0 0 2px rgba(0,0,0,0.9)'}}>{l}</div>
          ))}
          {text && <div style={{height: Math.max(4, size * 0.07), borderRadius: 4, background: C.accent,
            width: ease(f, a + 6, a + 18) * size * 0.5 * Math.max(...lines.map((l) => l.length)),
            boxShadow: '0 0 14px rgba(255,122,69,0.7)', alignSelf: box.alignItems}} />}
        </div>
      )}
    </AbsoluteFill>
  );
};
