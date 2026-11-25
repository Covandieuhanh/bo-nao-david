// Phụ đề đầy đủ lời nói, chạy suốt video (nền trong suốt), nằm TRÊN mọi lớp khác.
// Vị trí: luôn ở ĐÁY vùng an toàn (dải CAP_H = 140 px). Lớp phủ được thu nhỏ và đặt ngay trên dải này (bo-cuc.js);
// cảnh toàn màn hình phải chừa trống ~140 px cuối vùng an toàn khi có phụ đề.
// Dữ liệu: phu-de.js — [{start, end, text}]
import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import CAPTIONS from '../phu-de.js';
import {BODY, C, HEAD, SAFE, SAFE_W, BRAND_TOP, ease} from '../chu-de';
import {SCENES, fr} from '../canh';
import project from '../du-an.js';
import {POD, PF, LAND} from '../khung-podcast';
import {Timeline} from './dong-thoi-gian';
import {Tua} from './tua';
import HL from '../doan-noi-bat.js';
import {DauGoc} from '../thu-vien/dau-goc';   // dấu góc chung (thu-vien-tai-nguyen)
import {SUB, ShortLine, highlight} from '../thu-vien/kieu-phu-de';
import HS from '../ho-so.json';   // hồ sơ tham số (chép lúc tạo dự án — mo-dun/ho_so.py)
const PD = HS.phu_de || {};
import {holdEnds} from '../thu-vien/giu';
import * as SC from '../canh';
import KHUNG from '../khung.js';   // khung chủ thể (khung-chu-the.py) → phụ đề + bảng ghi chú ở phần khung còn lại
import {BangGhiChu, bangO} from './bang-ghi-chu';
// MỖI LÚC MỘT CHỖ CHỮ (David chốt 2026-11-08, thay luật 02/11 chỉ ẩn khi thẻ có quote): cảnh motion graphic nào đang hiện (chữ to,
// thẻ, nhãn, sơ đồ, màn hành động…) thì phụ đề nhường — chữ trên hình là lời nguyên văn của đúng lúc đó. Phần còn lại của dòng hiện
// tiếp đúng cụm đang nói. Cảnh không có chữ: props.giuPhuDe = true để giữ phụ đề. Áp cho mọi khung (dọc, ngang, podcast).
const _cta0 = SCENES.find((s) => s.type === 'cta');
const LOP = holdEnds(SCENES, _cta0 ? _cta0.start : project.duration, HS).filter((s) => !s.props?.giuPhuDe && s.type !== 'endcard' && s.type !== 'cover');

// Video ngắn (David chốt 2026-11-08, thay 1–3 chữ ngày 04/11): phụ đề cụm 5–8 chữ, cỡ bằng chữ thẻ (kieu-phu-de.js ShortLine). Tự bật: highlight, podcast dọc (mọi độ dài, 08/11), hoặc video dọc ≤ 90 s
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
  // Highlight (doan-noi-bat.js) ở video người nói: thanh tập gốc chiếm đáy vùng an toàn → phụ đề lên ngay trên nó như podcast
  // podcast dọc: canh theo vùng an toàn (lề phải chừa cột nút nền tảng) — canh giữa khung 1080 làm phụ đề lấn vùng đỏ bên phải
  // (AI bắt ở chụp thử podcast 10/11/2026). Ngang giữ canh giữa.
  let box = POD ? {left: LAND ? (PF.W - PF.capW) / 2 : PF.left, width: PF.capW, bottom: PF.capBottom, size: PF.capSize}
    : {left: SAFE.left, width: SAFE_W, bottom: TL_ON ? PF.capBottom : SAFE.bottom - SUB.bottomGap, size: SUB.size};   // luôn ở đáy vùng an toàn (người dùng chốt)
  // Bảng ghi chú chạy + khung chủ thể (11/11/2026): phụ đề vào cột cạnh khung, bảng ngay trên phụ đề; cảnh đang hiện → bảng nhường
  const GC = !POD && SC.GHI_CHU && SC.GHI_CHU.length ? SC.GHI_CHU : null;
  const capTop = box.bottom - box.size * 3.4;
  const bo = (GC || KHUNG) && !POD ? bangO(KHUNG, SC.GHI_CHU_O, capTop) : null;
  if (bo && KHUNG && !POD) { box.left = bo.x; box.width = bo.w; }
  const gan = LOP.reduce((m, s) => Math.min(m, f < fr(s.start) ? fr(s.start) - f : f >= fr(s.end) ? f - fr(s.end) + 1 : 0), Infinity);
  const vis = Math.max(0, Math.min(1, gan / 8));
  const a = cap ? ease(f, fr(cap.start), fr(cap.start) + 3) : 0;
  // màn chốt khung ngang: ô video to chiếm nửa trên → ẩn dấu góc (lỗi 08/11/2026: dấu góc đè lên ô video)
  const ctaNgang = project.width > project.height && SCENES.some((s) => s.type === 'cta' && f >= fr(s.start) && f < fr(s.end));
  return (
    <AbsoluteFill>
      {CHU && <ChuChinh cap={cap} f={f} />}
      {GC && bo && <BangGhiChu data={GC} o={bo} vis={vis} />}
      {cap && !CHU && <div style={{position: 'absolute', left: box.left, width: box.width, top: box.bottom, transform: 'translateY(-100%)',
        display: 'flex', justifyContent: 'center', opacity: a}}>
        {SHORT
          ? <ShortLine text={cap.text} hl={cap.hl} f={f - fr(cap.start)} len={fr(cap.end) - fr(cap.start)} font={BODY}
              color={C.text} accent={C.accent} width={box.width} size={PD.ngan_co} maxW={PD.ngan_max_chu} maxC={PD.ngan_max_ky_tu} />
          : <div style={{maxWidth: box.width, ...SUB.box, ...SUB.text, fontFamily: BODY, fontSize: box.size, color: C.text}}>
              {highlight(cap.text, cap.hl, C.accent)}</div>}
      </div>}
      {/* dấu kênh ● DAVID │ chủ đề (project.topic) — podcast đã có ở đầu sân khấu (san-khau.jsx) */}
      {!POD && !ctaNgang && <DauGoc topic={project.topic || ''} style={{position: 'absolute', left: SAFE.left, top: BRAND_TOP}} />}
      {TL_ON && <Timeline />}
      {HL && <Tua />}
    </AbsoluteFill>
  );
};
