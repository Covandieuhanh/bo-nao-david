// NỀN + HÌNH ẢNH BÌA PODCAST KHÔNG MẶT (khối 14, David duyệt 2026-11-06, mẫu: mau-chuan/anh-thu-nho-podcast/chuan.jpg).
// Nền hoạ tiết: lưới chấm mờ + quầng cam + sóng âm mờ ở đáy. Một hình đại diện cho ý của tập, KHÔNG chữ, không lộ các bước giải pháp.
// hinh: 'danh-sach' (hình riêng) hoặc tên bất kỳ trong ICONS của thư viện hình (puzzle, target, people, tree, mountain, ...).
import React from 'react';
import {Icon} from './bieu-tuong';

const A = '#FF7A45';
const CX = 945, CY = 372;

const Bars = () => Array.from({length: 64}, (_, i) => {
  const h = 14 + 70 * Math.abs(Math.sin(i * 0.55) * Math.cos(i * 0.17));
  return <rect key={i} x={20 + i * 20} y={640 - h / 2} width={9} height={h} rx={4.5} fill={A} opacity={0.13} />;
});

const Dong = ({y, w, tich}) => (
  <g>
    <circle cx={CX - 95} cy={y} r={24} fill={tich ? A : 'none'} stroke={A} strokeWidth={7} />
    {tich && <path d={`M${CX - 107} ${y} l9 10 l17 -21`} fill="none" stroke="#0D0D10" strokeWidth={7} strokeLinecap="round" strokeLinejoin="round" />}
    <rect x={CX - 52} y={y - 7} width={w} height={14} rx={7} fill={A} />
  </g>
);

// Hai dòng đã tích, một dòng còn trống: gợi "vẫn còn điều chưa tìm ra", không lộ nội dung danh sách.
const DanhSach = () => (
  <g>
    <g filter="url(#phat-sang)">
      <rect x={CX - 140} y={CY - 165} width={280} height={340} rx={30} fill="#17120F" stroke={A} strokeWidth={10} />
      <rect x={CX - 60} y={CY - 192} width={120} height={54} rx={16} fill="#17120F" stroke={A} strokeWidth={10} />
    </g>
    <Dong y={CY - 70} w={160} tich />
    <Dong y={CY + 15} w={125} tich />
    <Dong y={CY + 100} w={145} />
  </g>
);

export const HinhPodcast = ({hinh}) => (
  <div style={{position: 'absolute', inset: 0, filter: 'saturate(1.25) contrast(1.12) brightness(1.04)'}}>
    <svg width={1280} height={720} viewBox="0 0 1280 720" style={{position: 'absolute', inset: 0}}>
      <defs>
        <radialGradient id="quang" cx={CX / 1280} cy={CY / 720} r={0.55}>
          <stop offset={0} stopColor={A} stopOpacity={0.34} />
          <stop offset={0.6} stopColor={A} stopOpacity={0.07} />
          <stop offset={1} stopColor={A} stopOpacity={0} />
        </radialGradient>
        <pattern id="cham" width={32} height={32} patternUnits="userSpaceOnUse">
          <circle cx={4} cy={4} r={2.2} fill="#fff" opacity={0.09} />
        </pattern>
        <filter id="phat-sang" x="-40%" y="-40%" width="180%" height="180%">
          <feGaussianBlur stdDeviation={9} result="b" />
          <feMerge><feMergeNode in="b" /><feMergeNode in="SourceGraphic" /></feMerge>
        </filter>
      </defs>
      <rect width={1280} height={720} fill="#0D0D10" />
      <rect width={1280} height={720} fill="url(#cham)" />
      <rect width={1280} height={720} fill="url(#quang)" />
      <Bars />
      <circle cx={CX} cy={CY} r={262} fill="none" stroke={A} strokeOpacity={0.35} strokeWidth={3} strokeDasharray="20 16" />
      {hinh === 'danh-sach' && <DanhSach />}
    </svg>
    {hinh !== 'danh-sach' && (
      <div style={{position: 'absolute', left: CX - 200, top: CY - 200, filter: 'drop-shadow(0 0 14px rgba(255,122,69,0.75))'}}>
        <Icon name={hinh} size={400} at={-1000} stroke={3.4} />
      </div>
    )}
  </div>
);
