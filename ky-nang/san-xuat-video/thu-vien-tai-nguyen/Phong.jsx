// PHÔNG NỀN CẢNH TOÀN MÀN HÌNH (David chốt 10/11/2026, học từ Joseph Video Editing): mặc định nền tối của kênh. Cảnh có props.phong:
//   'nguoi-mo'  nền = chính video người nói, làm mờ + tối — đồ hoạ nổi trên người, mạch hình ảnh không đứt (thay vì cắt hẳn sang nền tối)
//   'hat'       nền tối + hạt nhiễu nhẹ như giấy ảnh (cảnh lắng, trích câu)
// Root.jsx bọc mỗi cảnh bằng PhongCtx; FullShell, Illus, Diagram gọi <NenPhong /> thay nền riêng khi có phong.
import React, {createContext, useContext} from 'react';
import {AbsoluteFill, OffthreadVideo, staticFile} from 'remotion';
import {C} from './tokens';

export const PhongCtx = createContext({phong: null, khungDau: 0});
export const usePhong = () => useContext(PhongCtx);
const HAT = `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.22 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")`;

export const NenPhong = ({glow = true}) => {
  const {phong, khungDau} = usePhong();
  return (
    <>
      <AbsoluteFill style={{background: C.bg}} />
      {phong === 'nguoi-mo' && (
        <AbsoluteFill style={{overflow: 'hidden'}}>
          <OffthreadVideo src={staticFile('goc.mp4')} trimBefore={khungDau} muted
            style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(28px) brightness(0.42) saturate(0.8)', transform: 'scale(1.08)'}} />
        </AbsoluteFill>
      )}
      {glow && <AbsoluteFill style={{background: `radial-gradient(circle at 45% 38%, rgba(255,122,69,${phong === 'nguoi-mo' ? 0.1 : 0.16}), transparent 60%)`}} />}
      {phong === 'hat' && <AbsoluteFill style={{backgroundImage: HAT, opacity: 0.6, mixBlendMode: 'overlay'}} />}
    </>
  );
};
