// Hai bên khung ngang (chế độ pillar), chạy suốt video, nền đặc — cột giữa để trống cho video dọc.
// Trái: chủ đề + người nói, rồi từ khoá của ý đang nói (ẩn khi có thẻ/chữ to chiếm ô SLOT).
// Phải: danh sách ý — chưa tới thì mờ, đang nói thì nhấn màu, nói xong thì tích.
// Dữ liệu: SIDES trong scenes.js — {eyebrow, title, speaker, keywords: [{at, text}], points: [{at, label}]}
import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import {BODY, C, HEAD, ease, pop} from '../theme';
import {FPS, SCENES, SIDES, fr} from '../scenes';
import {CENTER, FULL, LEFT, RIGHT, SLOT, SLOT_H, TOP} from '../layout';
import {Eyebrow} from './Overlays';

const Tick = ({on, active}) => (
  <div style={{width: 40, height: 40, borderRadius: 20, flexShrink: 0, display: 'flex', alignItems: 'center',
    justifyContent: 'center', background: on ? C.accent : 'transparent', border: `3px solid ${on || active ? C.accent : C.dim}`}}>
    {on && <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={C.bg} strokeWidth="3.4"
      strokeLinecap="round" strokeLinejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5" /></svg>}
  </div>
);

// Mục cuối cùng đã tới mốc
const current = (list, f) => {
  let i = -1;
  list.forEach((x, k) => { if (f >= fr(x.at)) i = k; });
  return i;
};

export const Sides = () => {
  const f = useCurrentFrame();
  const {eyebrow = 'CHỦ ĐỀ', title = '', speaker = '', keywords = [], points = []} = SIDES || {};
  // Ô SLOT đang có lớp phủ → ẩn từ khoá (mờ ra/vào 6 khung)
  const busy = SCENES.some((s) => !FULL.has(s.type) && f >= fr(s.start) - 6 && f < fr(s.end) + 6);
  const kOpacity = busy ? 0 : 1;
  const ki = current(keywords, f);
  const kw = ki >= 0 ? keywords[ki] : null;
  const kIn = kw ? pop(f, fr(kw.at)) : 0;
  const pi = current(points, f);
  const size = points.length <= 6 ? 34 : points.length <= 9 ? 28 : 23;
  return (
    <AbsoluteFill style={{background: C.bg}}>
      <AbsoluteFill style={{background: `radial-gradient(circle at 18% 30%, ${C.accentSoft}, transparent 45%)`}} />
      <div style={{position: 'absolute', left: CENTER.x, width: CENTER.w, top: 0, bottom: 0, background: '#000'}} />
      <div style={{position: 'absolute', left: CENTER.x - 6, width: 6, top: 0, bottom: 0, background: C.accent}} />

      <div style={{position: 'absolute', left: LEFT.x, width: LEFT.w, top: TOP}}>
        <Eyebrow>{eyebrow}</Eyebrow>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: title.length > 40 ? 54 : 66, lineHeight: 1.02,
          color: C.text, textTransform: 'uppercase', marginTop: 10, paddingBottom: 6}}>{title}</div>
        {speaker && <div style={{fontFamily: BODY, fontWeight: 600, fontSize: 26, color: C.muted, marginTop: 14}}>{speaker}</div>}
      </div>
      {kw && (
        <div style={{position: 'absolute', left: SLOT.x, width: SLOT.w, top: SLOT.y, height: SLOT_H,
          opacity: kOpacity * ease(f, fr(kw.at), fr(kw.at) + 8), transform: `translateY(${(1 - kIn) * 24}px)`}}>
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 22, letterSpacing: 4, color: C.muted}}>ĐANG NÓI VỀ</div>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: kw.text.length > 18 ? 58 : 76, lineHeight: 1.02,
            color: C.accent, textTransform: 'uppercase', marginTop: 8, paddingBottom: 8}}>{kw.text}</div>
        </div>
      )}

      {points.length > 0 && (
        <div style={{position: 'absolute', left: RIGHT.x, width: RIGHT.w, top: TOP}}>
          <Eyebrow>NỘI DUNG</Eyebrow>
          <div style={{display: 'flex', flexDirection: 'column', gap: size * 0.75, marginTop: 26}}>
            {points.map((p, k) => {
              const done = k < pi, active = k === pi;
              return (
                <div key={k} style={{display: 'flex', alignItems: 'center', gap: 18,
                  opacity: done ? 0.72 : active ? 1 : 0.38}}>
                  <Tick on={done} active={active} />
                  <div style={{fontFamily: BODY, fontWeight: active ? 700 : 600, fontSize: size, lineHeight: 1.2,
                    color: active ? C.text : C.muted, paddingBottom: 4}}>{p.label}</div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};
