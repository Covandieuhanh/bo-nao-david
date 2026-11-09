// CHỮ HIỆN TỪNG TỪ (khối 07 · luật ở chuyen-dong.js): một dòng chữ hiện theo kiểu 'mo' | 'muc' | 'dong', không dịch chỗ — chữ đã vào
// là đứng yên. Giữ '\n' (xuống dòng theo cụm nghĩa) và khoảng trắng; style của dòng (font, cỡ, màu) do nơi gọi đặt như cũ.
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {tu} from './chuyen-dong';

export const ChuHien = ({text = '', a = 0, kieu = 'mo', style}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  let i = 0;
  return (
    <span style={style}>
      {String(text).split(/(\s+)/).map((w, j) => (/^\s*$/.test(w) ? w
        : <span key={j} style={{display: 'inline-block', whiteSpace: 'pre', ...tu(f, a, i++, fps, kieu)}}>{w}</span>))}
    </span>
  );
};
