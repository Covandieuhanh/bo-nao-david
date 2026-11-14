// DẤU GÓC ● DAVID │ chủ đề — một bản cho mọi khung dựng (vị trí: nhan-dien-thuong-hieu.js → brand).
// Nền sẫm đặc (C.nen) như phụ đề: chữ trắng / cam đọc được trên mọi nền sáng; không nền đen mờ.
import React from 'react';
import {C, HEAD} from './bien-thiet-ke';
import BRAND from './brand.json';
const SHADOW = '0 6px 30px rgba(0,0,0,0.45)';
export const DauGoc = ({topic = '', style}) => (
  <div style={{display: 'flex', alignItems: 'center', gap: 14, background: C.nen, borderRadius: 14, padding: '6px 18px 8px 16px', ...style}}>
    <div style={{width: 12, height: 12, borderRadius: 6, background: C.accent, boxShadow: '0 0 14px rgba(255,122,69,0.8)'}} />
    <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 38, color: C.accent, letterSpacing: 3, textShadow: SHADOW}}>{BRAND.name}</div>
    {topic && <div style={{width: 2, height: 30, background: C.line}} />}
    {topic && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 38, color: C.text, letterSpacing: 2, textShadow: SHADOW,
      whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: 640}}>{topic}</div>}
  </div>
);
