// DẤU GÓC ● DAVID │ chủ đề — một bản cho mọi khung dựng (vị trí: nhan-dien.js → brand).
import React from 'react';
import {C, HEAD} from './tokens';
import BRAND from './brand.json';
const SHADOW = '0 6px 30px rgba(0,0,0,0.45)';
export const DauGoc = ({topic = '', style}) => (
  <div style={{display: 'flex', alignItems: 'center', gap: 14, ...style}}>
    <div style={{width: 12, height: 12, borderRadius: 6, background: C.accent, boxShadow: '0 0 14px rgba(255,122,69,0.8)'}} />
    <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 38, color: C.accent, letterSpacing: 3, textShadow: SHADOW}}>{BRAND.name}</div>
    {topic && <div style={{width: 2, height: 30, background: C.line}} />}
    {topic && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 38, color: C.text, letterSpacing: 2, textShadow: SHADOW,
      whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: 640}}>{topic}</div>}
  </div>
);
