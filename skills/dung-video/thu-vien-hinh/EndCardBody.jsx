// RUỘT THẺ CUỐI — một bản cho mọi khung dựng (khối 08). Khung dựng lo nền (ảnh đứng hình / nền tối / sóng âm) và vị trí;
// thành phần này lo chữ: nút phát (highlight) hoặc gạch nhận diện, nhãn "XEM BẢN ĐẦY ĐỦ" (highlight), tên, người nói, lịch phát.
import React from 'react';
import {spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease} from './tokens';

export const EndCardBody = ({title = '', speaker = '', play = false, schedule = '', big = 120, gap = 40, shadow, tease = '', kenh = ''}) => {   // tease: câu gợi tò mò của màn hình cuối clip ngắn
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pb = spring({frame: f - 6, fps, config: {damping: 10, stiffness: 220, mass: 0.6}});
  const size = tease ? big * 0.5 : ((k) => (k <= 24 ? big : k <= 44 ? big * 0.8 : big * 0.65))(title.length);
  return (
    <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap}}>
      {tease && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: big * 0.95, lineHeight: 1.15, paddingTop: '0.1em', textTransform: 'uppercase',
        color: C.text, textAlign: 'center', textWrap: 'balance', marginBottom: gap * 0.5}}>{tease}</div>}
      {play && !tease && <div style={{width: big * 1.45, height: big * 1.02, borderRadius: big * 0.3, background: '#FF0033', display: 'flex', alignItems: 'center',
        justifyContent: 'center', transform: `scale(${pb})`, boxShadow: '0 0 80px rgba(255,0,51,0.45)'}}>
        <svg width={big * 0.55} height={big * 0.55} viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z" fill="#fff" /></svg></div>}
      {play && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: big * 0.35, letterSpacing: 2, color: C.accent, textAlign: 'center', textWrap: 'balance', opacity: ease(f, 6, 14)}}>{tease ? `BẢN ĐẦY ĐỦ TRÊN KÊNH ${kenh}`.toUpperCase() : 'XEM BẢN ĐẦY ĐỦ'}</div>}
      {(!play || tease) && <div style={{width: 420 * ease(f, 2, 16), height: 6, borderRadius: 3, background: C.accent}} />}
      <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: 1.05, paddingTop: '0.12em', textTransform: 'uppercase',
        color: C.text, textAlign: 'center', textWrap: 'balance', textShadow: shadow}}>{title}</div>
      {speaker && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: big * 0.38, color: C.accent, opacity: ease(f, 8, 16)}}>{speaker}</div>}
      {schedule && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: big * 0.33, color: C.text, padding: '8px 24px', borderRadius: 12,
        border: `2px solid ${C.accent}`, opacity: ease(f, 12, 20)}}>{schedule}</div>}
    </div>
  );
};
