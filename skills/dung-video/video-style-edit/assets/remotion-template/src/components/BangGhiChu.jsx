// BẢNG GHI CHÚ CHẠY (khối 07, David chốt 11/11/2026): video dày thông tin (cuộc gọi, hướng dẫn, giải thích dài) — một bảng luôn hiện
// ở phần khung trống, như có người ghi chép hộ người xem: tên phần đang nói + các ý chính cộng dồn theo lời (ý mới sáng cam, ý cũ mờ dần,
// đầy bảng thì ý cũ nhất trôi ra). Chữ là NGUYÊN VĂN cụm lời (luat-chung mục 1). Nằm trong lớp phụ đề (không thêm lớp render).
// Cảnh motion graphic đang hiện → bảng nhường (mỗi lúc một chỗ chữ). Dữ liệu scenes.js:
//   export const GHI_CHU = [{phan: 'Tự ra quyết định', at: 0, y: [{text: 'một tuần đào tạo từ A đến Z', at: 12.4}, …]}, …];
//   export const GHI_CHU_O = {x: .6, y: .11, w: .35, h: .55};   // tuỳ chọn (0–1); có khung chủ thể (khung.js) thì tự đặt cạnh khung
import React from 'react';
import {useCurrentFrame} from 'remotion';
import {BODY, C, HEAD, ease} from '../theme';
import {fr} from '../scenes';
import project from '../project.js';

export const bangO = (KHUNG, O, capTop) => {
  const W = project.width, H = project.height;
  if (O) return {x: O.x * W, y: O.y * H, w: O.w * W, h: O.h * H};
  if (KHUNG) {
    const gap = W * 0.035, x = KHUNG.phia === 'phai' ? W * 0.05 : (KHUNG.x + KHUNG.w) * W + gap;
    const w = KHUNG.phia === 'phai' ? KHUNG.x * W - gap - W * 0.05 : W * 0.95 - x;
    return {x, y: KHUNG.y * H, w, h: capTop - KHUNG.y * H - H * 0.03};
  }
  return {x: W * 0.6, y: H * 0.11, w: W * 0.35, h: H * 0.55};
};

export const BangGhiChu = ({data, o, vis}) => {
  const f = useCurrentFrame();
  const pi = data.reduce((k, p, i) => (f >= fr(p.at) ? i : k), -1);
  if (pi < 0 || vis <= 0.01) return null;
  const p = data[pi], ph = ease(f, fr(p.at), fr(p.at) + 12);
  const co = Math.max(30, Math.min(50, o.w / 21));   // cỡ chữ theo bề rộng bảng (11/11/2026: 36 quá nhỏ, bảng trống nửa dưới)
  const MAX = Math.max(3, Math.floor((o.h - co * 4.6) / (co * 2.9)));   // số ý vừa bảng (ý dài 2 dòng)
  const shown = (p.y || []).filter((y) => f >= fr(y.at));
  const ds = shown.slice(-MAX), moi = shown.length - 1;
  return (
    <div style={{position: 'absolute', left: o.x, top: o.y, width: o.w, opacity: vis, display: 'flex', flexDirection: 'column', gap: co * 0.5}}>
      <div style={{opacity: ph, transform: `translateY(${(1 - ph) * 10}px)`}}>
        <div style={{fontFamily: HEAD, fontWeight: 700, fontSize: co * 0.78, letterSpacing: '0.14em', color: C.accent}}>
          {data.length > 1 ? `PHẦN ${pi + 1}/${data.length}` : 'GHI CHÚ'}</div>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: co * 1.7, lineHeight: 1.08, paddingTop: '0.08em', color: C.text,
          textTransform: 'uppercase', textWrap: 'balance'}}>{p.phan}</div>
        <div style={{height: 3, width: o.w * 0.18 * ph, background: C.accent, marginTop: co * 0.45, borderRadius: 2}} />
      </div>
      {ds.map((y, i) => {
        const k = shown.length - ds.length + i, a = ease(f, fr(y.at), fr(y.at) + 9), la = k === moi;
        return (
          <div key={y.at} style={{display: 'flex', gap: co * 0.5, alignItems: 'flex-start', opacity: a * (la ? 1 : 0.62),
            transform: `translateX(${(1 - a) * 18}px)`}}>
            <div style={{flex: 'none', width: co * 0.36, height: co * 0.36, borderRadius: '50%', marginTop: co * 0.48,
              background: la ? C.accent : C.dim}} />
            <div style={{fontFamily: BODY, fontWeight: la ? 600 : 500, fontSize: co, lineHeight: 1.32, color: la ? C.text : C.muted}}>{y.text}</div>
          </div>
        );
      })}
    </div>
  );
};
