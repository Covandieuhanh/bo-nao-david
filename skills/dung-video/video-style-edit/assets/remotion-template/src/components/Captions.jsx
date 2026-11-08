// Phụ đề đầy đủ lời nói, chạy suốt video (nền trong suốt), nằm TRÊN mọi lớp khác.
// Vị trí: luôn ở ĐÁY vùng an toàn (dải CAP_H = 140 px). Lớp phủ được thu nhỏ và đặt ngay trên dải này (layout.js);
// cảnh toàn màn hình phải chừa trống ~140 px cuối vùng an toàn khi có phụ đề.
// Dữ liệu: captions.js — [{start, end, text}]
import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import CAPTIONS from '../captions.js';
import {BODY, C, HEAD, SAFE, SAFE_W, BRAND_TOP, ease} from '../theme';
import {SCENES, fr} from '../scenes';
import project from '../project.js';
import {POD, PF} from '../podframe';
import {Timeline} from './Timeline';
import {Tua} from './Tua';
import HL from '../highlight.js';
import {DauGoc} from '../lib/DauGoc';   // dấu góc chung (thu-vien-hinh)
import {SUB, ShortLine, highlight} from '../lib/subStyle';
import HS from '../hoso.json';   // hồ sơ tham số (chép lúc tạo dự án — khoi/hoso.py)
const PD = HS.phu_de || {};
import {holdEnds} from '../lib/giu';
// MỖI LÚC MỘT CHỖ CHỮ (David chốt 2026-11-08, thay luật 02/11 chỉ ẩn khi thẻ có quote): cảnh motion graphic nào đang hiện (chữ to,
// thẻ, nhãn, sơ đồ, màn hành động…) thì phụ đề nhường — chữ trên hình là lời nguyên văn của đúng lúc đó. Phần còn lại của dòng hiện
// tiếp đúng cụm đang nói. Cảnh không có chữ: props.giuPhuDe = true để giữ phụ đề. Áp cho mọi khung (dọc, ngang, podcast).
const _cta0 = SCENES.find((s) => s.type === 'cta');
const LOP = holdEnds(SCENES, _cta0 ? _cta0.start : project.duration, HS).filter((s) => !s.props?.giuPhuDe && s.type !== 'endcard' && s.type !== 'cover');

// Video ngắn (David chốt 2026-11-08, thay 1–3 chữ ngày 04/11): phụ đề cụm 5–8 chữ, cỡ bằng chữ thẻ (subStyle.js ShortLine). Tự bật: highlight, podcast dọc (mọi độ dài, 08/11), hoặc video dọc ≤ 90 s
// (video ngang / video dọc dài không phải podcast giữ hộp tối). Ép tay: project.short = true | false.
import {SHORT, TL_ON} from '../thanh';

// CHỮ CHÍNH (David chốt 2026-11-06, podcast đồ hoạ dọc trích ngắn): cả câu đang nói hiện to giữa khung, thay dải phụ đề và dòng chủ đề —
// mỗi lúc chỉ một lớp chữ. Ẩn khi thẻ tít mở đầu / màn chốt đang hiện (hai màn đó là chữ của đoạn ấy).
const CHU = !!(HL && HL.chu_chinh);
const ChuChinh = ({cap, f}) => {
  if (!cap || SCENES.some((s) => (s.type === 'hook' || s.type === 'cta') && f >= fr(s.start) && f < fr(s.end))) return null;
  const a = ease(f, fr(cap.start), fr(cap.start) + 4);
  return (
    <div style={{position: 'absolute', left: PF.left + 24, width: PF.right - PF.left - 48, top: 660, height: 330, display: 'flex', alignItems: 'center', justifyContent: 'center',
      opacity: a, transform: `translateY(${(1 - a) * 14}px)`}}>
      <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: cap.text.length > 42 ? 84 : 96, lineHeight: 1.18, paddingTop: '0.1em', color: C.text, textTransform: 'uppercase', textAlign: 'center', textWrap: 'balance'}}>
        {highlight(cap.text, cap.hl, C.accent)}</div>
    </div>
  );
};

export const Captions = () => {
  const f = useCurrentFrame();
  // Thẻ toàn cảnh đang hiện NGUYÊN VĂN câu nói (quote) → ẩn phụ đề: câu to giữa màn chính là phụ đề đoạn đó, không đọc 2 lần
  const quoted = !CHU && LOP.some((s) => f >= fr(s.start) && f < fr(s.end));   // tên cũ giữ lại: có lớp chữ đang hiện → ẩn phụ đề
  const jumping = HL && HL.jumps.some((j) => f >= fr(j.at) && f < fr(j.at + j.dur));   // highlight: đang tua → không phụ đề
  const cap = quoted || jumping ? null : CAPTIONS.find((c) => f >= fr(c.start) && f < fr(c.end));
  // Podcast: phụ đề ngay trên thanh thời gian (đáy vùng an toàn), khung dọc hoặc ngang toàn khung
  // Highlight (highlight.js) ở video người nói: thanh tập gốc chiếm đáy vùng an toàn → phụ đề lên ngay trên nó như podcast
  const box = POD ? {left: (PF.W - PF.capW) / 2, width: PF.capW, bottom: PF.capBottom, size: PF.capSize}
    : {left: SAFE.left, width: SAFE_W, bottom: TL_ON ? PF.capBottom : SAFE.bottom - SUB.bottomGap, size: SUB.size};   // luôn ở đáy vùng an toàn (người dùng chốt)
  const a = cap ? ease(f, fr(cap.start), fr(cap.start) + 3) : 0;
  // màn chốt khung ngang: ô video to chiếm nửa trên → ẩn dấu góc (lỗi 08/11/2026: dấu góc đè lên ô video)
  const ctaNgang = project.width > project.height && SCENES.some((s) => s.type === 'cta' && f >= fr(s.start) && f < fr(s.end));
  return (
    <AbsoluteFill>
      {CHU && <ChuChinh cap={cap} f={f} />}
      {cap && !CHU && <div style={{position: 'absolute', left: box.left, width: box.width, top: box.bottom, transform: 'translateY(-100%)',
        display: 'flex', justifyContent: 'center', opacity: a}}>
        {SHORT
          ? <ShortLine text={cap.text} hl={cap.hl} f={f - fr(cap.start)} len={fr(cap.end) - fr(cap.start)} font={BODY}
              color={C.text} accent={C.accent} width={box.width} size={PD.ngan_co} maxW={PD.ngan_max_chu} maxC={PD.ngan_max_ky_tu} />
          : <div style={{maxWidth: box.width, ...SUB.box, ...SUB.text, fontFamily: BODY, fontSize: box.size, color: C.text}}>
              {highlight(cap.text, cap.hl, C.accent)}</div>}
      </div>}
      {/* dấu kênh ● DAVID │ chủ đề (project.topic) — podcast đã có ở đầu sân khấu (Stage.jsx) */}
      {!POD && !ctaNgang && <DauGoc topic={project.topic || ''} style={{position: 'absolute', left: SAFE.left, top: BRAND_TOP}} />}
      {TL_ON && <Timeline />}
      {HL && <Tua />}
    </AbsoluteFill>
  );
};
