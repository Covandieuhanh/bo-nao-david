// THẺ CUỐI (highlight podcast — skill cat-highlight-video, người dùng chốt 2026-11-03): ~1,8 s ghép SAU video (render_preview.py),
// dẫn về bản đầy đủ kiểu thẻ cuối Have A Sip. CHỈ chữ của bản gốc: tên tập gốc + tên người nói — không "BẢN ĐẦY ĐỦ"/"XEM NGAY".
// Dữ liệu: highlight.js → endcard {title?, speaker?}; thiếu thì lấy STAGE.title / STAGE.speakers (tên tập, người nói của bản gốc).
import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import {BODY, C, HEAD, ease, pop} from '../theme';
import {STAGE} from '../scenes';
import HL from '../highlight.js';
import project from '../project.js';
import BRAND from '../lib/brand.json';
import {LAND, PF, PF_W} from '../podframe';
import {YtEnd} from '../lib/YtEnd';
import {EndCardBody} from '../lib/EndCardBody';   // ruột thẻ cuối dùng chung (khối 08)
import {fr} from '../scenes';

export const EndCard = () => {
  const f = useCurrentFrame();
  // thẻ cuối NHẬN DIỆN (không phải highlight): chủ đề + tên kênh, không nút phát (người dùng chốt 2026-11-04)
  const brandOnly = !(HL && HL.endcard);
  const ec = (HL && HL.endcard) || {};
  const title = ec.title || project.topic || (STAGE && STAGE.title) || '';
  const speaker = brandOnly ? BRAND.name : ec.speaker || ((STAGE && STAGE.speakers) || []).filter((s) => s && s.name).map((s) => s.name).join(' · ');
  const p = pop(f, 0, {damping: 15, stiffness: 160, mass: 0.7});
  const pb = pop(f, 6, {damping: 10, stiffness: 220, mass: 0.6});
  const n = LAND ? 56 : 32, gap = 10, bw = (PF_W - gap * (n - 1)) / n;
  const size = ((k) => k <= 24 ? (LAND ? 150 : 120) : k <= 44 ? (LAND ? 120 : 96) : (LAND ? 96 : 78))(title.length);
  // Màn kết YouTube (project.ytEnd = 15–20 s, chỉ video đăng YouTube > 3 phút): thẻ nhận diện như cũ rồi chuyển sang khung chừa chỗ
  // 2 video + nút đăng ký (YtEnd.jsx). Highlight / video ngắn không dùng.
  const yt = brandOnly && project.ytEnd > 5;
  // PO-6: lịch phát David đưa (project.schedule hoặc STAGE.schedule, vd 'Tập mới mỗi thứ 6') — không tự đặt
  const schedule = (!brandOnly && ec.schedule) || project.schedule || (STAGE && STAGE.schedule) || '';
  if (yt && f >= fr(BRAND.endcardLen)) return <YtEnd name={BRAND.name} topic={title} schedule={schedule} start={fr(BRAND.endcardLen)} />;
  return (
    <AbsoluteFill style={{background: C.bg}}>
      <AbsoluteFill style={{background: `radial-gradient(circle at 50% ${LAND ? '42%' : '40%'}, rgba(255,122,69,0.28), transparent 58%)`}} />
      <div style={{position: 'absolute', left: PF.left, width: PF_W, top: LAND ? 180 : (ec.tease ? 400 : 560), display: 'flex', flexDirection: 'column',
        alignItems: 'center', gap: LAND ? 36 : 44, transform: `translateY(${(1 - p) * 60}px)`, opacity: ease(f, 0, 6)}}>
        <EndCardBody tease={ec.tease || ''} kenh={ec.kenh || ''} title={title} speaker={ec.tease ? '' : speaker} play={!brandOnly} schedule={schedule} big={LAND ? 150 : 120} gap={LAND ? 36 : 44} />
      </div>
      {/* sóng âm lặng dần — nối mạch với sân khấu podcast (chỉ podcast) */}
      {project.podcast && <div style={{position: 'absolute', left: PF.left, width: PF_W, top: LAND ? 900 : 1380, height: 90, display: 'flex', alignItems: 'center', gap}}>
        {Array.from({length: n}, (_, i) => {
          const h = 10 + 70 * Math.abs(Math.sin(i * 0.7 + f / 5)) * Math.max(0.08, 1 - f / 50);
          return <div key={i} style={{width: bw, height: h, borderRadius: bw, background: C.accent, opacity: 0.55}} />;
        })}
      </div>}
    </AbsoluteFill>
  );
};
