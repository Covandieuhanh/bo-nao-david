// MÀN KẾT YOUTUBE 15–20 s (David chốt 2026-11-04, học 80 video Việt: 11/30 video dài có màn kết 2 video + nút đăng ký).
// Chỉ vẽ NỀN + KHUNG CHỪA CHỖ cho phần tử màn kết mà David gắn trong YouTube Studio (2 video + đăng ký) — không chữ tự viết ngoài
// tên kênh + chủ đề (bộ nhận diện). Tự cân theo khung ngang / dọc. Một nguồn: remotion-template; new_montage.sh chép sang dự án ghép.
// Vị trí ô theo lưới màn kết của YouTube (phần tử video 16:9 ~ 1/3 bề ngang; nút đăng ký tròn).
import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';

const K = {bg: '#0D0D10', text: '#F4F4F5', accent: '#FF7A45', line: 'rgba(255,255,255,0.14)'};
const HEAD = '"Barlow Condensed", sans-serif';
const cl = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};

// Toạ độ ô (để David gắn khớp trong YouTube Studio — ghi cùng vào phat-hanh.md)
export const ytSlots = (W, H) => W > H
  ? {v1: {x: 0.08, y: 0.33, w: 0.38}, v2: {x: 0.54, y: 0.33, w: 0.38}, sub: {x: 0.5, y: 0.83, r: 0.06}}
  : {v1: {x: 0.12, y: 0.26, w: 0.76}, v2: {x: 0.12, y: 0.51, w: 0.76}, sub: {x: 0.5, y: 0.85, r: 0.11}};

export const YtEnd = ({name = 'DAVID', topic = '', schedule = '', start = 0}) => {
  const f = useCurrentFrame() - start;
  const {width: W, height: H} = useVideoConfig();
  const s = ytSlots(W, H);
  const a = interpolate(f, [0, 14], [0, 1], cl);
  const box = (v, k) => {
    const w = v.w * W, h = w * 9 / 16;
    const d = interpolate(f, [6 + k * 5, 20 + k * 5], [0, 1], cl);
    return <div key={k} style={{position: 'absolute', left: v.x * W, top: v.y * H, width: w, height: h, borderRadius: w * 0.03,
      border: `3px solid ${K.line}`, background: 'rgba(255,255,255,0.04)', opacity: d, transform: `scale(${0.94 + 0.06 * d})`,
      boxShadow: '0 30px 80px rgba(0,0,0,0.45)'}} />;
  };
  const r = s.sub.r * Math.min(W, H) * 1.6;
  const pulse = 1 + 0.04 * Math.sin(f / 9);
  const big = Math.round(Math.min(W, H) * 0.075);
  return (
    <AbsoluteFill style={{background: K.bg, opacity: a}}>
      <AbsoluteFill style={{background: 'radial-gradient(circle at 50% 20%, rgba(255,122,69,0.22), transparent 55%)'}} />
      <div style={{position: 'absolute', left: 0, right: 0, top: H * (W > H ? 0.09 : 0.12), display: 'flex', flexDirection: 'column',
        alignItems: 'center', gap: big * 0.25}}>
        <div style={{display: 'flex', alignItems: 'center', gap: big * 0.3}}>
          <div style={{width: big * 0.22, height: big * 0.22, borderRadius: big, background: K.accent}} />
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: big, letterSpacing: 4, color: K.accent}}>{name}</div>
        </div>
        {topic && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: big * 0.62, color: K.text, textTransform: 'uppercase',
          letterSpacing: 2}}>{topic}</div>}
        {schedule && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: big * 0.42, color: K.accent, letterSpacing: 2,
          textTransform: 'uppercase'}}>{schedule}</div>}
      </div>
      {box(s.v1, 0)}{box(s.v2, 1)}
      <div style={{position: 'absolute', left: s.sub.x * W - r / 2, top: s.sub.y * H - r / 2, width: r, height: r, borderRadius: r,
        border: `4px solid ${K.accent}`, opacity: interpolate(f, [16, 30], [0, 1], cl), transform: `scale(${pulse})`,
        boxShadow: '0 0 60px rgba(255,122,69,0.35)'}} />
    </AbsoluteFill>
  );
};
