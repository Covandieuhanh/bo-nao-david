// MẪU cảnh tự vẽ có mạch hình — chỉ để AI tham khảo cách dùng (xoá / thay bằng hình riêng của video).
// Ý: một con đường đi từ "trước" tới "sau"; cảnh đầu vẽ đoạn đầu, cảnh sau (khi người nói quay lại ý) vẽ tiếp đoạn kế.
// scenes.js: {id:'m1', type:'ve', start, end, props:{ve:'MauMach', buoc:1, tu_buoc:0, moc_buoc:[giây], label:['CHỮ NGUYÊN VĂN']}}
//            {id:'m2', type:'ve', start, end, props:{ve:'MauMach', buoc:2, tu_buoc:1, moc_buoc:[giây], label:['…','…']}}
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {C, HEAD} from '../lib/tokens';
import {mach, net} from '../lib/mach';
import {vaoRa} from '../lib/chuyen-dong';
import {ChuHien} from '../lib/ChuHien';

export const MauMach = ({start, buoc, tu_buoc, moc_buoc, label = []}) => {
  const f = useCurrentFrame(); const {fps, width: W, height: H, durationInFrames: d} = useVideoConfig();
  const m = mach(f, fps, start, {buoc, tu_buoc, moc_buoc});
  const v = vaoRa(f, d);
  const doan = [`M ${W * 0.12} ${H * 0.62} C ${W * 0.3} ${H * 0.4}, ${W * 0.4} ${H * 0.7}, ${W * 0.52} ${H * 0.5}`,
    `M ${W * 0.52} ${H * 0.5} C ${W * 0.64} ${H * 0.32}, ${W * 0.76} ${H * 0.56}, ${W * 0.88} ${H * 0.36}`];
  return (
    <AbsoluteFill style={{background: C.bg, opacity: v.opacity, filter: v.filter}}>
      <svg width={W} height={H}>
        {doan.map((p, i) => <path key={i} d={p} fill="none" stroke={i === buoc - 1 ? C.accent : C.muted} strokeWidth={10}
          strokeLinecap="round" style={net(m.p(i), 1400)} />)}
      </svg>
      {label.map((t, i) => m.p(i) > 0 && <div key={i} style={{position: 'absolute', left: W * (0.16 + i * 0.4), top: H * 0.22,
        fontFamily: HEAD, fontWeight: 800, fontSize: H * 0.06, color: i === buoc - 1 ? C.text : C.muted}}>
        <ChuHien text={t} a={m.moi(i) ? Math.round(((moc_buoc[i - tu_buoc] ?? start) - start) * fps) : 0} kieu={m.moi(i) ? 'mo' : 'dong'} /></div>)}
    </AbsoluteFill>
  );
};
