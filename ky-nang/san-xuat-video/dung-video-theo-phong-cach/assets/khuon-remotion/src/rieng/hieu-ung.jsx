// HIỆU ỨNG VÀO / RA + QUÉT SÁNG dùng chung cho cảnh tự vẽ (22/11/2026 — David: "những hiệu ứng hay là 3D để chuyển cảnh … từ những cái
// mà bạn học được ấy, thì nó có thể linh động và áp dụng bất kỳ cái nào … đa dạng những cái thẩm mỹ để gây ấn tượng … gọn gàng thôi").
// Đổi kiểu qua các cảnh để video không lặp một hiệu ứng; mỗi cảnh chỉ một kiểu vào + một kiểu ra.
//   vao / ra: 'truot' (trượt từ trên) · 'lat-3d' (lật xuống quanh mép trên) · 'xoay-3d' (xoay vào quanh mép trái) · 'mo-man' (mở màn
//             trái → phải) · 'phong' (phóng nhẹ từ nhỏ) · 'nhoe' (mờ nhoè → nét)
//   const v = vaoRaKieu(f, d, {vao: 'lat-3d', ra: 'nhoe'})  →  <div style={{...v.boc}}><div style={{...v.khoi}}>…</div></div>
//   <QuetSang a={khung bắt đầu} w h r />  → vệt sáng chéo quét qua một lần (nhấn câu đắt / lúc tấm vừa vào)
import React from 'react';
import {Easing, interpolate, useCurrentFrame} from 'remotion';

const kep = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const len = (f, a, b, e = Easing.out(Easing.cubic)) => interpolate(f, [a, b], [0, 1], {...kep, easing: e});

const mot = (kieu, p) => {          // p = 0 (chưa vào / đã ra) → 1 (đứng yên)
  const q = 1 - p;
  switch (kieu) {
    case 'lat-3d': return {transform: `rotateX(${-82 * q}deg)`, transformOrigin: '50% 0%', opacity: Math.min(1, p * 1.6)};
    case 'xoay-3d': return {transform: `rotateY(${70 * q}deg) translateX(${-30 * q}px)`, transformOrigin: '0% 50%', opacity: Math.min(1, p * 1.6)};
    case 'mo-man': return {clipPath: `inset(0 ${100 * q}% 0 0 round 22px)`, opacity: 1};
    case 'phong': return {transform: `scale(${0.82 + 0.18 * p})`, transformOrigin: '50% 40%', opacity: p};
    case 'nhoe': return {filter: q > 0.01 ? `blur(${(12 * q).toFixed(2)}px)` : undefined, opacity: p};
    case 'truot': default: return {transform: `translateY(${-16 * q}px)`, opacity: p};
  }
};

export const vaoRaKieu = (f, d, {vao = 'truot', ra = 'nhoe', dVao = 14, dRa = 9} = {}) => {
  const pv = len(f, 0, dVao, vao === 'phong' ? Easing.out(Easing.back(1.6)) : Easing.out(Easing.exp));
  const pr = 1 - len(f, d - dRa, d, Easing.in(Easing.cubic));
  const st = f < d - dRa ? mot(vao, pv) : mot(ra, pr);
  return {boc: {perspective: 1100, position: 'absolute', inset: 0}, khoi: {position: 'absolute', inset: 0, ...st}};
};

export const QuetSang = ({a = 0, dai = 22, w, h, r = 0}) => {
  const f = useCurrentFrame();
  const p = len(f, a, a + dai, Easing.inOut(Easing.cubic));
  if (p <= 0 || p >= 1) return null;
  const x = -0.4 * w + p * 1.8 * w;
  return (
    <div style={{position: 'absolute', inset: 0, borderRadius: r, overflow: 'hidden', pointerEvents: 'none'}}>
      <div style={{position: 'absolute', top: -h, left: x, width: w * 0.22, height: h * 3, transform: 'rotate(18deg)',
        background: 'linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.22), rgba(255,255,255,0))', mixBlendMode: 'screen'}} />
    </div>
  );
};
