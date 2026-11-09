// ĐIỂM NHẤN TRÊN NGƯỜI (type 'nhan' — David chốt 2026-11-07): làm nổi người đang nói ở câu đắt, KHÔNG che mặt.
// props: text ('CHỮ NHẤN', '\n' xuống dòng, ≤ 4 chữ, trích lời) · icon (tên trong lib/Icons) · at (giây tuyệt đối lúc bật)
//        zoom (vd 1.15 — zoom dồn vào mặt, render_preview.py làm trên video gốc) · toi (true = làm tối viền quanh người)
// bam ('trai' | 'phai' | số thứ tự — graphic nói về một người cụ thể, vd thẻ tên khách; mặc định người đang nói)
// Vị trí: mat.js (scripts/nhan_place.py — mọi người trong khung + người đang nói). Zoom dồn vào người đang nói; chữ / biểu tượng vào
// khoảng trống sát người đó (lib/cho.js), co cỡ theo khoảng trống, KHÔNG đè ai; khung dọc hẹp → dưới cằm. Không con số vị trí cố định.
import React from 'react';
import {AbsoluteFill, Easing, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, SAFE, BRAND_BOT, ease, pop, rel} from '../theme';
import {Icon} from '../lib/Icons';
import project from '../project.js';
import MAT from '../mat.js';
import {nguoi, chonCho, nguoiBam} from '../lib/cho';
import {ChuHien} from '../lib/ChuHien';
import {kieuChu, k as khung} from '../lib/chuyen-dong';

const W = project.width, H = project.height;
// Vị trí mặt SAU zoom (cùng công thức với render_preview.py: khung zoom canh giữa mặt, kẹp trong khung hình)
export const zoomed = (m, Z) => {
  const x0 = Math.max(0, Math.min(1 - 1 / Z, m.cx - 0.5 / Z)), y0 = Math.max(0, Math.min(1 - 1 / Z, m.cy - 0.5 / Z));
  return {cx: (m.cx - x0) * Z, cy: (m.cy - y0) * Z, w: m.w * Z, h: m.h * Z,
    l: ((m.l ?? m.cx - m.w / 2) - x0) * Z, r: ((m.r ?? m.cx + m.w / 2) - x0) * Z};
};

export const Nhan = ({sceneId, start, text, icon, at, zoom = 1, toi = false, bam}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, fps} = useVideoConfig();
  const a = at != null ? rel(at, start) : 6;
  const out = ease(f, d - 6, d, 1, 0, Easing.in(Easing.cubic));   // ra gọn hơn vào (chuyen-dong.js luật 2)
  const kc = kieuChu(sceneId);
  const p = pop(f, a);
  const V = H > W;
  // Mọi người trong khung (sau zoom) — chữ đặt vào khoảng trống sát NGƯỜI ĐANG NÓI (hoặc người được bám), không đè ai
  const ps = nguoi(MAT[sceneId] || {cx: 0.5, cy: 0.42, w: 0.18, h: 0.3}, zoom || 1);
  const t = nguoiBam(ps, bam);
  const fy = t.cy * H;
  const lines = (text || '').split('\n');
  const base = (V ? 0.05 : 0.075) * H, minS = (V ? 0.038 : 0.042) * H;
  const chars = Math.max(1, ...lines.map((l) => l.length), icon && !text ? 4 : 1);
  const need = (s) => s * (0.52 * chars + 0.8) + 0.9 * base;          // bề rộng ô chữ ở cỡ s
  const k = chonCho(ps, need(base * 0.8), t, need(minS * 0.8));
  const fit = (k.w - 0.9 * base) / (0.52 * chars + 0.8);
  const under = V && fit < minS;
  const size = Math.round(under ? base : Math.max(minS * 0.8, Math.min(base, fit)));
  const side = k.ke === 'phai' ? 'right' : 'left';
  const top = Math.max(BRAND_BOT + 24, fy - size * lines.length * 0.6);
  const box = under
    ? {left: W / 2, maxWidth: W - SAFE.left - SAFE.right, top: Math.min(fy + t.h * 0.75 * H, SAFE.bottom - 140 - size * lines.length * 1.2 - 40), textAlign: 'center', alignItems: 'center'}
    : side === 'right'
      ? {left: k.x0, maxWidth: k.w, top, alignItems: 'flex-start', textAlign: 'left'}
      : {right: W - k.x1, maxWidth: k.w, top, alignItems: 'flex-end', textAlign: 'right'};
  const m = t;
  const dx = under ? 0 : (side === 'right' ? -1 : 1) * (1 - p) * 60;
  const cxT = under ? 'translateX(-50%) ' : '';
  return (
    <AbsoluteFill style={{opacity: out, filter: out < 1 ? `blur(${(8 * (1 - out)).toFixed(2)}px)` : undefined}}>
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
              textShadow: '0 4px 24px rgba(0,0,0,0.75), 0 0 2px rgba(0,0,0,0.9)'}}><ChuHien text={l} a={a + 3 + i * khung(0.15, fps)} kieu={kc} /></div>
          ))}
          {text && <div style={{height: Math.max(4, size * 0.07), borderRadius: 4, background: C.accent,
            width: ease(f, a + 6, a + 18) * size * 0.5 * Math.max(...lines.map((l) => l.length)),
            boxShadow: '0 0 14px rgba(255,122,69,0.7)', alignSelf: box.alignItems}} />}
        </div>
      )}
    </AbsoluteFill>
  );
};
