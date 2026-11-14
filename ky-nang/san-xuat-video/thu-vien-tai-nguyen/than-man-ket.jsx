// RUỘT THẺ CUỐI — một bản cho mọi khung dựng (khối 08). Khung dựng lo nền (ảnh đứng hình / nền tối / sóng âm) và vị trí;
// thành phần này lo chữ: gạch nhận diện (không nút phát, không logo nền tảng), nhãn "Bản đầy đủ trên kênh …" (highlight), tên, người nói, lịch phát.
import React from 'react';
import {spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease} from './bien-thiet-ke';

export const EndCardBody = ({title = '', speaker = '', play = false, schedule = '', big = 120, gap = 40, shadow, kenh = ''}) => {   // play = hiện nhãn dẫn bản đầy đủ (không phải nút phát)
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pb = spring({frame: f - 6, fps, config: {damping: 10, stiffness: 220, mass: 0.6}});
  const size = ((k) => (k <= 24 ? big : k <= 44 ? big * 0.8 : big * 0.65))(title.length);
  return (
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap}}>
      {/* Không nút phát đỏ / logo nền tảng (David chốt 06/11/2026, áp mọi khung dựng 08/11/2026): video đăng Reels + TikTok, nút không bấm được */}
      {play && kenh && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: big * 0.35, letterSpacing: 2, color: C.accent, textAlign: 'center', textWrap: 'balance', opacity: ease(f, 6, 14)}}>{`BẢN ĐẦY ĐỦ TRÊN KÊNH ${kenh}`.toUpperCase()}</div>}
      {<div style={{width: 420 * ease(f, 2, 16), height: 6, borderRadius: 3, background: C.accent}} />}
      <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: 1.05, paddingTop: '0.12em', textTransform: 'uppercase',
        color: C.text, textAlign: 'center', textWrap: 'balance', textShadow: shadow}}>{title}</div>
      {speaker && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: big * 0.38, color: C.accent, opacity: ease(f, 8, 16)}}>{speaker}</div>}
      {schedule && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: big * 0.33, color: C.text, padding: '8px 24px', borderRadius: 12,
        border: `2px solid ${C.accent}`, opacity: ease(f, 12, 20)}}>{schedule}</div>}
    </div>
  );
};
