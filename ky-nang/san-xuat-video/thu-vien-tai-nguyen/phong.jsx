// PHÔNG NỀN CẢNH TOÀN MÀN HÌNH (David chốt 10/11/2026, học từ Joseph Video Editing): mặc định nền tối của kênh. Cảnh có props.phong:
//   'nguoi-mo'  nền = chính video người nói, làm mờ + tối — đồ hoạ nổi trên người, mạch hình ảnh không đứt (thay vì cắt hẳn sang nền tối)
//   'hat'       nền tối + hạt nhiễu nhẹ như giấy ảnh (cảnh lắng, trích câu)
// goc.jsx bọc mỗi cảnh bằng PhongCtx; FullShell, Illus, Diagram gọi <NenPhong /> thay nền riêng khi có phong.
import React, {createContext, useContext} from 'react';
import {AbsoluteFill, OffthreadVideo, staticFile} from 'remotion';
import {C} from './bien-thiet-ke';

export const PhongCtx = createContext({phong: null, khungDau: 0});
export const usePhong = () => useContext(PhongCtx);
const HAT = `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.22 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")`;

const HAT_SAM = `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='320' height='320'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.25  0 0 0 0 0.24  0 0 0 0 0.23  0 0 0 9 -5.2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")`;

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
      {glow && <AbsoluteFill style={{background: `radial-gradient(circle at 45% 38%, rgba(${C.accentRgb},${phong === 'nguoi-mo' ? 0.1 : C.giay === 'hat' ? 0 : 0.16}), transparent 60%)`}} />}
      {phong === 'hat' && (C.giay === 'hat'
        // giấy Joseph minimal: lấm tấm hạt sẫm trên giấy xám (đo khung 4:34)
        ? <AbsoluteFill style={{backgroundImage: HAT_SAM, backgroundSize: '320px 320px'}} />
        : <AbsoluteFill style={{backgroundImage: HAT, opacity: 0.6, mixBlendMode: 'overlay'}} />)}
    </>
  );
};
