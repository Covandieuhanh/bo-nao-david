// ẢNH THUMBNAIL YOUTUBE 1280×720 (David chốt 2026-11-04: bước phát hành — "sao chép chuẩn kênh lớn"). Theo chuẩn MrBeast /
// Paddy Galloway / Ali Abdaal: MỘT khuôn mặt to có cảm xúc, ≤ 4 chữ cực to tương phản cao, một ý duy nhất, không lặp tiêu đề,
// đọc được ở cỡ điện thoại (~160 px). Nhận diện David: chữ cô đặc in hoa, dòng nhấn cam, chấm cam + DAVID góc trên.
// props: {bg: 'bg-1.jpg' (thumb/public), pos: '60% 30%' (object-position — đặt mặt về phía đối diện chữ), side: 'left'|'right'
//         (phía đặt chữ), l1: 'DÒNG TRẮNG', l2: 'DÒNG CAM', zoom: 1.0–1.4, panel: true khi nguồn quay dọc (thumbnail.sh tự đặt),
//         l3: 'DÒNG 3 TRẮNG' (tuỳ chọn), num: '5' (con số khổng lồ riêng 1 khối, cam), badge: 'HAVE A SIP · TẬP 12' (nhãn series)}
// KIỂU VIỆT (học 10/10 video dài Việt, 2026-11-04): 3 tầng chữ, tới ~8 chữ, con số khổng lồ, từ khoá (dòng cam) to nhất.
import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, continueRender, delayRender, staticFile} from 'remotion';
import '@fontsource/barlow-condensed/vietnamese-800.css';
import '@fontsource/barlow-condensed/800.css';
import BRAND from './brand.json';   // thumbnail.sh chép từ remotion-template (một nguồn)

const C = {bg: '#0D0D10', text: '#F4F4F5', accent: '#FF7A45'};
const HEAD = '"Barlow Condensed", sans-serif';

export const Thumb = ({bg, pos = '50% 35%', side = 'left', l1 = '', l2 = '', l3 = '', num = '', badge = '', zoom = 1.1, panel = false}) => {
  const [h] = useState(() => delayRender('font'));
  useEffect(() => { document.fonts.load(`800 100px ${HEAD}`, 'ĐẾN ĐÂU Ầ Ễ').then(() => continueRender(h)); }, [h]);
  const W0 = num ? 560 : 720;   // bề ngang cho chữ (chừa khối số)
  const fit = (t, cap) => Math.min(cap, Math.round(W0 / Math.max(t.length, 1) * 1.9));   // cỡ theo độ dài từng dòng
  const nLines = [l1, l2, l3].filter(Boolean).length;
  const cap = nLines >= 3 ? 130 : 190;
  const L = side === 'left';
  const line = (t, color, boost = 1) => t && (
    <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: Math.round(fit(t, cap) * boost), lineHeight: 1.02, color, textTransform: 'uppercase',
      WebkitTextStroke: '14px #000', paintOrder: 'stroke fill', textShadow: '0 10px 40px rgba(0,0,0,0.7)', whiteSpace: 'nowrap'}}>{t}</div>);
  return (
    <AbsoluteFill style={{background: C.bg, overflow: 'hidden'}}>
      {/* panel (nguồn quay dọc): ảnh chiếm 58% phía đối diện chữ, mép mờ dần — mặt không bị phóng quá khổ, không chạm chữ */}
      <div style={{position: 'absolute', top: 0, bottom: 0, width: panel ? '58%' : '100%', [L ? 'right' : 'left']: 0, overflow: 'hidden',
        ...(panel ? {WebkitMaskImage: `linear-gradient(${L ? 90 : 270}deg, transparent 0%, #000 22%)`} : {})}}>
        <Img src={staticFile(bg)} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', objectPosition: pos,
          transform: `scale(${zoom})`, transformOrigin: pos, filter: 'saturate(1.25) contrast(1.12) brightness(1.04)'}} />
      </div>
      <AbsoluteFill style={{background: `linear-gradient(${L ? 90 : 270}deg, rgba(13,13,16,0.92) 0%, rgba(13,13,16,0.55) 38%, transparent 62%)`}} />
      <div style={{position: 'absolute', top: 0, bottom: 0, [L ? 'left' : 'right']: 64, maxWidth: 820, display: 'flex', flexDirection: 'column',
        justifyContent: 'center', alignItems: L ? 'flex-start' : 'flex-end', textAlign: L ? 'left' : 'right'}}>
        {badge && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 38, letterSpacing: 2, color: C.bg, background: C.accent,
          padding: '4px 16px', borderRadius: 8, marginBottom: 18, textTransform: 'uppercase'}}>{badge}</div>}
        {!badge && <div style={{width: 120, height: 12, borderRadius: 6, background: C.accent, marginBottom: 22}} />}
        <div style={{display: 'flex', alignItems: 'center', gap: 18, flexDirection: L ? 'row' : 'row-reverse'}}>
          {num && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: nLines >= 2 ? 300 : 260, lineHeight: 0.9, color: C.accent,
            WebkitTextStroke: '16px #000', paintOrder: 'stroke fill', textShadow: '0 10px 40px rgba(0,0,0,0.7)'}}>{num}</div>}
          <div style={{display: 'flex', flexDirection: 'column', alignItems: L ? 'flex-start' : 'flex-end'}}>
            {line(l1, C.text)}{line(l2, C.accent, 1.12)}{line(l3, C.text)}
          </div>
        </div>
      </div>
      <div style={{position: 'absolute', top: 36, [L ? 'left' : 'right']: 64, display: 'flex', alignItems: 'center', gap: 12}}>
        <div style={{width: 14, height: 14, borderRadius: 7, background: C.accent}} />
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 40, letterSpacing: 3, color: C.text, WebkitTextStroke: '6px #000', paintOrder: 'stroke fill'}}>{BRAND.name}</div>
      </div>
    </AbsoluteFill>
  );
};
