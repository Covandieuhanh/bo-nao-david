// THANH THỜI GIAN ở đáy — một bản cho mọi khung dựng (vị trí: nhan-dien-thuong-hieu.js → tl). Hiện "đã chạy · thanh · còn m:ss".
// nen: true → dải tối mờ phía sau (video có người nói, nền sáng); podcast nền tối thì false.
import React from 'react';
import {BODY, C} from './bien-thiet-ke';
import {mmss} from './nhan-dien-thuong-hieu';
export const ThanhThoiGian = ({t, T, k, nen = true, truoc = null, opacity = 1}) => {
  const p = Math.min(1, Math.max(0, t / Math.max(0.001, T)));
  const label = {fontFamily: BODY, fontWeight: 600, fontSize: 24, color: nen ? C.text : C.muted, fontVariantNumeric: 'tabular-nums', whiteSpace: 'nowrap'};
  return (
    <div style={{position: 'absolute', left: k.tl.left, width: k.tl.right - k.tl.left, top: k.tl.y, height: k.tl.h, display: 'flex', alignItems: 'center',
      gap: 18, opacity, ...(nen ? {background: C.nen, borderRadius: k.tl.h, padding: '0 16px', boxSizing: 'border-box'} : {})}}>
      {truoc}
      <div style={label}>{mmss(t)}</div>
      <div style={{position: 'relative', flex: 1, height: 8, borderRadius: 4, background: 'rgba(255,255,255,0.18)'}}>
        <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, width: `${p * 100}%`, borderRadius: 4, background: C.accent}} />
        <div style={{position: 'absolute', left: `${p * 100}%`, top: 4, width: 18, height: 18, borderRadius: 9, background: C.text,
          transform: 'translate(-50%, -50%)', boxShadow: '0 0 12px rgba(255,122,69,0.7)'}} />
      </div>
      <div style={label}>còn {mmss(Math.max(0, T - t))}</div>
    </div>
  );
};
