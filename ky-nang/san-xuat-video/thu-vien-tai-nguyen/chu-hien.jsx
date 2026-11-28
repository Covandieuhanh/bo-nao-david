// CHỮ HIỆN TỪNG TỪ (khối 07 · luật ở chuyen-dong.js): một dòng chữ hiện theo kiểu 'mo' | 'muc' | 'dong', không dịch chỗ — chữ đã vào
// là đứng yên. Giữ '\n' (xuống dòng theo cụm nghĩa) và khoảng trắng; style của dòng (font, cỡ, màu) do nơi gọi đặt như cũ.
// TỪ NHẤN (David chốt 10/11/2026, học từ Joseph Video Editing): `*từ*` hoặc `*cụm từ*` → font phụ NHAN (chữ có chân, nghiêng),
// màu nhấn cam, giữ chữ thường. Mỗi cụm tối đa MỘT chỗ nhấn. Chữ vẫn nguyên văn — dấu * chỉ đánh dấu, không hiện.
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {tu} from './chuyen-dong';
import {C, NHAN} from './bien-thiet-ke';

// màu đọc lúc vẽ (không lúc nạp mã) để theo giao diện của cảnh; C.nhanMau ghi đè khi màu nhấn của mẫu không đọc được trên nền đó
export const nhanStyle = () => ({fontFamily: NHAN, fontStyle: 'italic', fontWeight: 700, color: C.nhanMau || C.accent, textTransform: 'none', letterSpacing: 0});
export const boSao = (t) => String(t ?? '').replace(/\*/g, '');

export const ChuHien = ({text = '', a = 0, kieu = 'mo', style}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  let i = 0, nhan = false;
  return (
    <span style={style}>
      {String(text).split(/(\s+)/).map((w, j) => {
        if (/^\s*$/.test(w)) return w;
        const mo = w.startsWith('*'), dong = w.replace(/[.,!?;:…"'”)]+$/, '').endsWith('*');
        if (mo) nhan = true;
        const st = nhan ? nhanStyle() : null;
        if (dong) nhan = false;
        return <span key={j} style={{display: 'inline-block', whiteSpace: 'pre', ...st, ...tu(f, a, i++, fps, kieu)}}>{w.replace(/\*/g, '')}</span>;
      })}
    </span>
  );
};
