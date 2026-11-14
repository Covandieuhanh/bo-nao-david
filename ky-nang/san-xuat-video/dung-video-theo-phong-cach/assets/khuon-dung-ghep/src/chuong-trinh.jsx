import React, {createContext, useContext, useEffect, useState} from 'react';
import {AbsoluteFill, Audio, Easing, Freeze, OffthreadVideo, Sequence, continueRender, delayRender,
  interpolate, random, spring, staticFile, useCurrentFrame} from 'remotion';
import {FONT_CHECKS} from './phong-chu';
import * as EDL from './danh-sach-cat';
import {CTA, FPS, H, MUSIC, OVERLAYS, SEGS, SFX, SUBS, TOTAL, W, fr} from './danh-sach-cat';
import {SUB, ShortLine, highlight} from './lib/kieu-phu-de';
import LIFT from './nang-lop.js';
import GUARD from './bao-ve.js';
import HS from './hoso.json';
import {Illus} from './lib/minh-hoa';
import {Diagram} from './lib/so-do';   // sơ đồ nói thay lời + ảnh khung bo góc (khối 07)   // cảnh minh hoạ toàn màn hình — 2 trạng thái (khối 07, thư viện dùng chung)
import {holdEnds} from './lib/giu';   // giữ cảnh ≥ 1,2 s sau chữ cuối (khối 07, hồ sơ chung canh_minh_hoa.giu_sau_s)
// 2 TRẠNG THÁI (hồ sơ hai_trang_thai): lớp chữ đè người (pow, chips, location, nameCard, replay, pointer, callout) tự vẽ toàn màn hình
// ≤ toan_man_max_s; ngoại lệ: thẻ tít mở đầu (pow bắt đầu < 0,5 s) và `keep: true`. Tít ghim tắt.
const TWO = !!HS.hai_trang_thai;
const CONV = new Set(['pow', 'chips', 'nameCard', 'replay', 'pointer', 'callout']);   // hồ sơ tham số (tao-dung-ghep.sh / danh-sach-cat-doan-noi-bat.py chép vào)
const PD = HS.phu_de || {};   // lớp phủ tự chuyển toàn màn hình khi che người (bao-ve-lop-phu.py)
import CTA_DEF, {CTA_ICONS, CTA_TICK} from './lib/keu-goi-hanh-dong.js';
import {Icon} from './lib/bieu-tuong';
import BRAND from './lib/brand.json';
import {YtEnd} from './lib/man-ket-youtube';
import {EndCardBody} from './lib/than-man-ket';
import {khung, nganDoc} from './lib/nhan-dien-thuong-hieu';   // bộ nhận diện chung: vùng an toàn, dấu góc, thanh thời gian (David chốt 08/11/2026)
import {DauGoc} from './lib/dau-goc';
import {ThanhThoiGian} from './lib/thanh-thoi-gian';   // ruột thẻ cuối dùng chung (khối 08)   // màn kết YouTube 15–20 s (chép từ remotion-template, một nguồn)   // bộ nhận diện David (một nguồn với chế độ 1 video, podcast, highlight)   // biểu tượng nét vẽ dần — chép từ remotion-template (một nguồn với chế độ 1 video)   // câu màn chốt — chép từ remotion-template (một nguồn với chế độ 1 video)

// ===== Phong cách (token) — mặc định: thẻ tối, nhấn cam, chữ cô đặc in hoa trồi lên (bộ nhận diện đã duyệt).
// Có video mẫu/dự án cũ → đổi C, HEAD, BODY (+ phong-chu.js) theo style.md; component giữ nguyên ngôn ngữ chuyển động. =====
import {C} from './thuong-hieu';   // màu nhận diện chung (thuong-hieu.js) — biểu tượng vẽ (bieu-tuong.jsx) cùng đọc
const HEAD = '"Barlow Condensed", sans-serif';
const BODY = '"Be Vietnam Pro", sans-serif';
const K = khung(W, H);
const SAFE = K.safe;
const SAFE_W = W - SAFE.left - SAFE.right;
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const pop = (f, at = 0, cfg = {damping: 16, stiffness: 140, mass: 0.7}) => spring({frame: f - at, fps: FPS, config: cfg});
const ease = (f, a, b, o0 = 0, o1 = 1, e = Easing.out(Easing.cubic)) => interpolate(f, [a, b], [o0, o1], {...clamp, easing: e});
const inOut = (f, total, inLen = 10, outLen = 8) => Math.min(ease(f, 0, inLen), ease(f, total - outLen, total, 1, 0, Easing.in(Easing.cubic)));
const SHADOW = '0 6px 30px rgba(0,0,0,0.45)';

// ===== HIGHLIGHT (skill cat-doan-noi-bat) — vlog thường không khai báo nên mọi thứ dưới đây tắt =====
// HL = {src_duration}: thanh của CẢ tập gốc ở đáy + chip tua ở các đoạn `jump` (đoạn đứng hình ~0,4 s giữa hai câu trích).
// TONE = [[từ, đến, 'lang' | 'soi']] giây timeline — 'lang' (tâm sự, nỗi đau): không chớp trắng, chuyển cảnh tối dần
// không vệt quét/tiếng vút, chữ to hiện chậm, màu dịu; 'soi' (mặc định): như game show.
const HL = EDL.HL || null;
const TONE = EDL.TONE || [];
const toneAt = (t) => (TONE.find(([a, b]) => t >= a && t < b) || [0, 0, 'soi'])[2];
// THANH THỜI GIAN (David chốt 08/11/2026): mọi loại video đều có, kể cả clip ngắn. HL.bar → thanh của cả tập gốc (SrcBar), còn lại thanh
// thường của chính video (ThanhThoiGian, nhan-dien-thuong-hieu.js). Tắt tay: `export const THANH = false` trong danh-sach-cat.js. Phụ đề lên trên thanh.
const NGAN_DOC = nganDoc(W, H, TOTAL, EDL.SHORT || EDL.HL);   // David chốt 10/11/2026: dọc ngắn → không thanh, không thẻ cuối, màn chốt trên hình
const THANH = EDL.THANH ?? !NGAN_DOC;
const HL_LIFT = HL && HL.bar !== false && THANH ? 56 : THANH ? SAFE.bottom - SUB.bottomGap - K.capBottom : 0;
// SHORT (danh-sach-cat.js, highlight luôn bật): phụ đề 1–3 chữ to mỗi nhịp kiểu kênh lớn (kieu-phu-de.js ShortLine) — vlog dài giữ hộp tối
const SHORT = !!EDL.SHORT;
// DẢI PHỤ ĐỀ (người dùng chỉ ra 2026-11-04: thẻ địa điểm đè phụ đề): phụ đề tối đa 2 dòng ≈ 140 px ở đáy vùng an toàn — giống
// CAP_H của chế độ 1 video (bo-cuc.js). Thẻ thấp (Location, NameCard, Replay) canh ĐÁY vào LOW_Y nên dài/ngắn, có dòng phụ hay
// không cũng không chạm phụ đề; lớp đặt tay (pow y, pointer, chips top) phải có đáy ≤ LOW_Y.
const CAP_H = 140;
const CAP_TOP = SAFE.bottom - SUB.bottomGap - HL_LIFT - CAP_H;
// CHẾ ĐỘ GIỮA (lỗi 09/11/2026, app dựng video): lớp phủ bị đổi sang TOÀN MÀN HÌNH (che người) trước đây chỉ bị đẩy lên + phóng 1,12 —
// chữ neo mép trái vẫn dính mép trái, chữ dài tràn khung. Nay FullOv bật GIUA: nội dung căn giữa trong vùng an toàn, không phóng.
const GiuaCtx = createContext(false);
const useGiua = () => useContext(GiuaCtx);
const KHOI_GIUA = {left: SAFE.left, width: SAFE_W, top: H * 0.46, transform: 'translateY(-50%)', display: 'flex', flexDirection: 'column',
  alignItems: 'center', textAlign: 'center'};
const LOW_Y = CAP_TOP - 20;
const FULLSCREEN = new Set(['action', 'scene', 'outro']);   // lớp toàn màn hình (phụ đề ẩn hoặc không có) — không chặn
const mmss = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

// ===== Hình =====
const zoomAt = (f, seg) => {
  // f: khung trong đoạn → giây trong clip
  const src = seg.from + (f / FPS) * seg.rate;
  let s = 1, x = 0.5, y = 0.5;
  // KHÔNG ZOOM VÀO / RA (13/11/2026 — David: "bỏ hiệu ứng zoom ra zoom vào, không thẩm mỹ"): bỏ qua seg.zoom và zoomIn đổi cỡ; chỉ giữ cỡ tĩnh (zoomIn [a, a, …])
  for (const z of []) {
    const d = src - z.at;
    if (d < 0) continue;
    const k = d < z.len ? spring({frame: d * FPS / seg.rate, fps: FPS, config: {damping: 14, stiffness: 200}}) : 1;
    // hold (danh-sach-cat-vlog.py fx): giữ cú dồn `hold` s rồi nhả về khung gốc trong 0,5 s — không có hold thì giữ tới hết đoạn (như cũ)
    const back = z.hold != null ? interpolate(d, [z.hold, z.hold + 0.5], [1, 0], {...clamp, easing: Easing.inOut(Easing.cubic)}) : 1;
    if (back <= 0) continue;
    s = 1 + (z.s - 1) * k * back; x = z.x; y = z.y;
  }
  if (seg.zoomIn && seg.zoomIn[0] === seg.zoomIn[1]) { const [a, b, zx, zy] = seg.zoomIn; s = interpolate(f, [0, fr(seg.dur)], [a, b], clamp); x = zx; y = zy; }
  return {transform: `scale(${s})`, transformOrigin: `${x * 100}% ${y * 100}%`};
};
const gradeFilter = {lang: 'saturate(0.72) brightness(0.94) contrast(1.03)', replay: 'saturate(0.55) sepia(0.35) contrast(1.05)', dark: 'brightness(0.55) saturate(1.1)', title: 'blur(18px) brightness(0.45) saturate(1.3)'};

// Đoạn TRÍCH DẪN (người dùng chốt): hình minh hoạ từ clip khác nằm trong KHUNG BO GÓC trên nền tối + quầng cam theo
// phong cách — không toàn khung như clip chính, để người xem biết đây là cảnh được nhắc tới. Luôn TẮT tiếng clip minh hoạ;
// tiếng người nói lấy từ clip chính (seg.audio) nên chạy liền mạch. Khung y 300–1240: chừa phụ đề ở đáy vùng an toàn.
const Cite = ({seg, src, common}) => {
  const f = useCurrentFrame();
  const len = fr(seg.dur);
  const p = pop(f, 0, {damping: 18, stiffness: 150, mass: 0.7});
  const out = ease(f, len - 8, len, 0, 1, Easing.in(Easing.cubic));
  const top = 300, h = 940;
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, overflow: 'hidden'}}>
      <AbsoluteFill style={{background: `radial-gradient(circle at 50% 42%, ${C.accentSoft}, transparent 65%)`}} />
      {seg.cite.label && (
        <div style={{position: 'absolute', left: SAFE.left, top: top - 64, opacity: ease(f, 2, 12) * (1 - out)}}>
          <Eyebrow>{seg.cite.label}</Eyebrow>
        </div>
      )}
      <div style={{position: 'absolute', left: SAFE.left, top, width: SAFE_W, height: h, borderRadius: 36, overflow: 'hidden',
        border: `3px solid ${C.accent}`, boxShadow: '0 40px 100px rgba(0,0,0,0.6)', opacity: Math.min(1, p * 1.4) * (1 - out),
        transform: `scale(${0.92 + 0.08 * p - out * 0.04})`}}>
        {seg.freeze
          ? <Freeze frame={0}><OffthreadVideo src={src} trimBefore={fr(seg.from)} muted style={{width: '100%', height: '100%', objectFit: 'cover'}} /></Freeze>
          : <OffthreadVideo src={src} {...common} muted style={{width: '100%', height: '100%', objectFit: seg.cite.fit || 'cover',
            transform: `scale(${1.06 - ease(f, 0, len) * 0.04})`}} />}
      </div>
      {seg.audio && <Audio src={staticFile(`clips/${seg.audio.clip}.mp4`)} trimBefore={fr(seg.audio.from)} volume={seg.audio.vol} />}
    </AbsoluteFill>
  );
};

const Clip = ({seg}) => {
  const f = useCurrentFrame();
  const src = staticFile(`clips/${seg.clip}.mp4`);
  const common = {trimBefore: fr(seg.from), playbackRate: seg.rate, pauseWhenBuffering: false};
  if (seg.cite) return <Cite seg={seg} src={src} common={common} />;
  const vol = seg.audio ? 0 : seg.vol ?? 1;
  const fillStyle = {width: '100%', height: '100%', objectFit: 'cover'};
  let video;
  if (seg.freeze) {
    video = <Freeze frame={0}><OffthreadVideo src={src} trimBefore={fr(seg.from)} muted style={fillStyle} /></Freeze>;
  } else if (seg.fit === 'blur') {
    video = (
      <>
        <OffthreadVideo src={src} {...common} muted style={{...fillStyle, filter: 'blur(40px) brightness(0.55)', transform: 'scale(1.2)'}} />
        <AbsoluteFill style={{justifyContent: 'center'}}>
          <OffthreadVideo src={src} {...common} muted style={{width: '100%', transform: `scale(${1.25 + f * 0.0015})`}} />
        </AbsoluteFill>
      </>
    );
  } else {
    video = <OffthreadVideo src={src} {...common} volume={vol} muted={vol === 0} style={fillStyle} />;
  }
  // NÂNG KHUNG (người dùng chốt): nhân vật/vật chính nằm thấp → đẩy hình lên `y` px (phần trên bị cắt vốn nằm dưới thanh tab
  // nền tảng), đáy hở lấp bằng chính hình đó làm mờ; cần hơn 400 px thì phóng thêm `s` (gốc phóng ở mép trên).
  // Số liệu từ nang-lop.js (scripts/lift_plan.py tự tính theo mặt) hoặc đặt tay `lift: {y, s}` trong đoạn ở danh-sach-cat.js.
  const lift0 = seg.lift || LIFT[seg.id];
  const kc = ctaK(fr(seg.start) + f);   // màn chốt: hình đã lùi vào khung, phụ đề nằm ngoài → nhả dần độ nâng
  const lift = lift0 && {y: (lift0.y || 0) * (1 - kc), s: 1 + ((lift0.s || 1) - 1) * (1 - kc)};
  if (lift && !seg.fit && kc < 1 && (lift.y > 0 || lift.s > 1)) {
    const bg = seg.freeze
      ? <Freeze frame={0}><OffthreadVideo src={src} trimBefore={fr(seg.from)} muted style={{...fillStyle, filter: 'blur(40px) brightness(0.6)', transform: 'scale(1.15)'}} /></Freeze>
      : <OffthreadVideo src={src} {...common} muted style={{...fillStyle, filter: 'blur(40px) brightness(0.6)', transform: 'scale(1.15)'}} />;
    video = (
      <>
        {bg}
        <AbsoluteFill style={{transform: `translateY(${-lift.y}px) scale(${lift.s || 1})`, transformOrigin: '50% 0%',
          WebkitMaskImage: 'linear-gradient(to bottom, #000 calc(100% - 160px), transparent)'}}>{video}</AbsoluteFill>
      </>
    );
  }
  return (
    <AbsoluteFill style={{backgroundColor: '#000', overflow: 'hidden'}}>
      <AbsoluteFill style={{...zoomAt(f, seg), filter: gradeFilter[seg.grade] || 'none'}}>{video}</AbsoluteFill>
      {seg.audio && <Audio src={staticFile(`clips/${seg.audio.clip}.mp4`)} trimBefore={fr(seg.audio.from)} volume={seg.audio.vol} />}
    </AbsoluteFill>
  );
};

// Chớp trắng ở mỗi lần chuyển đoạn
const Flash = () => {
  const f = useCurrentFrame();
  return <AbsoluteFill style={{backgroundColor: '#fff', opacity: interpolate(f, [0, 5], [0.75, 0], clamp)}} />;
};

// ===== Mảnh dùng chung (như video mẫu) =====
const Eyebrow = ({children, style}) => (
  <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 26, letterSpacing: 4, color: C.accent, textShadow: '0 2px 10px rgba(0,0,0,0.7)', ...style}}>{children}</div>
);
// Nền tối mờ dần để chữ trắng dễ đọc
const Scrim = ({from = 'bottom', o = 1}) => (
  <AbsoluteFill style={{opacity: o, background: from === 'bottom'
    ? 'linear-gradient(transparent 45%, rgba(0,0,0,0.55) 65%, rgba(0,0,0,0.7))'
    : 'linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.35) 22%, transparent 36%)'}} />
);
// Một chữ trồi lên khỏi mặt nạ (chừa đệm để không cắt dấu tiếng Việt)
// Chữ trồi lên trong khung cắt: chừa chỗ theo cỡ chữ cho dấu chồng (0,5 em trên) và dấu nặng (0,32 em dưới) — chuẩn chung với
// chế độ 1 video (VN trong khung-podcast.js); khoảng 34/30 px cố định cũ cắt dấu và làm 2 dòng dính nhau.
const Rise = ({children, p, style}) => {
  const fs = style?.fontSize || 100;
  return (
    <div style={{overflow: 'hidden', paddingTop: fs * 0.5, marginTop: -fs * 0.5, paddingBottom: fs * 0.32, marginBottom: -fs * 0.32}}>
      <div style={{transform: `translateY(${(1 - p) * 105}%)`, ...style}}>{children}</div>
    </div>
  );
};
const Bar = ({w, style}) => (
  <div style={{height: 9, borderRadius: 5, background: C.accent, width: w, boxShadow: '0 0 24px rgba(255,122,69,0.55)', ...style}} />
);
const Arrow = ({size = 30, color = C.accent}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="2.4"
    strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
);

// ===== Phụ đề: KIỂU CHUẨN DÙNG CHUNG (kieu-phu-de.js — giống hệt chế độ 1 video): hộp nền tối, đáy vùng an toàn, từ khoá cam =====
const WHO = {1: C.accent, 2: '#4DA3FF'};   // ô phụ đề theo người nói (kiểu hội thoại GaryVee) — chỉ đổi viền
const Caption = ({text, hl, len, who, off = 0}) => {
  const fl = useCurrentFrame(), f = fl + off;
  const o = Math.min(ease(fl, 0, 3), 1 - ease(f, len - 3, len));
  return (
    <AbsoluteFill>
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: SAFE.bottom - SUB.bottomGap - HL_LIFT, transform: 'translateY(-100%)',
        display: 'flex', justifyContent: 'center', opacity: o}}>
        {SHORT
          ? <ShortLine text={text} hl={hl} f={f} len={len} font={BODY} color={C.text} accent={WHO[who] || C.accent} width={SAFE_W} size={PD.ngan_co} maxW={PD.ngan_max_chu} maxC={PD.ngan_max_ky_tu} />
          : <div style={{maxWidth: SAFE_W, ...SUB.box, ...SUB.text, fontFamily: BODY, fontSize: SUB.size, color: C.text,
              ...(WHO[who] ? {border: `3px solid ${WHO[who]}`} : {})}}>
              {highlight(text, hl, C.accent)}</div>}
      </div>
    </AbsoluteFill>
  );
};

// ===== Chữ nhấn kiểu NHÃN DÁN (David 13/11/2026: chữ dính mặt + nền đen mờ là mất thẩm mỹ) =====
// Mỗi dòng một nhãn đặc màu (dòng trước trắng chữ sẫm, dòng cuối cam chữ trắng), không nền mờ phủ hình. Canh ĐÁY vào đáy dải phụ đề
// (phụ đề nhường đúng lúc này) nên khối chữ nằm ngực/bụng, xa cằm. '\n' = chỗ xuống dòng theo cụm nghĩa.
const Pow = ({text, y, len, start = 0}) => {
  const f = useCurrentFrame(); const giua = useGiua();
  const soft = toneAt(start) === 'lang';   // tông lắng: hiện chậm, không nghiêng, không nảy
  const o = soft ? inOut(f, len, 12, 12) : inOut(f, len, 4, 6);
  const dongs = text.split('\n').map((d) => d.trim()).filter(Boolean);
  const dai = Math.max(...dongs.map((d) => d.length));
  const size = Math.max(64, Math.min(104, Math.floor((SAFE_W - 80) / (0.52 * Math.max(dai, 6)))));
  const day = CAP_TOP + CAP_H;   // đáy khối = đáy dải phụ đề
  return (
    <AbsoluteFill style={{opacity: o}}>
      <div style={giua ? {position: 'absolute', ...KHOI_GIUA} : {position: 'absolute', left: SAFE.left, width: SAFE_W,
        ...(y != null && y < 700 ? {top: y} : {top: day, transform: 'translateY(-100%)'}), display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        {dongs.map((d, i) => {
          const cuoi = i === dongs.length - 1 && dongs.length > 1;
          const p = soft ? ease(f, 2 + i * 6, 16 + i * 6) : pop(f, 1 + i * 4, {damping: 15, stiffness: 190, mass: 0.6});
          return (
            <div key={i} style={{marginTop: i ? 14 : 0, padding: `${size * 0.16}px ${size * 0.34}px ${size * 0.1}px`, borderRadius: 14,
              background: cuoi || dongs.length === 1 ? C.accent : '#fff', color: cuoi || dongs.length === 1 ? '#fff' : '#141418',
              fontFamily: HEAD, fontWeight: soft ? 700 : 800, fontSize: size, lineHeight: 1.18, whiteSpace: 'nowrap',
              boxShadow: '0 10px 28px rgba(0,0,0,0.28)', opacity: Math.min(1, p * 1.4),
              transform: `translateY(${(1 - p) * 40}px) scale(${0.85 + 0.15 * p}) rotate(${soft ? 0 : i % 2 ? 1.5 : -2}deg)`}}>{d}</div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// ===== Màn hình tiêu đề (nền toàn màn hình như cảnh FullShell của mẫu) =====
// over: tiêu đề nằm TRÊN đoạn ghép mở đầu của vlog (danh-sach-cat-vlog.py intro) — nền mỏng để cảnh ghép vẫn thấy rõ (kiểu kênh mẫu)
const Title = ({len, eyebrow = 'TẬP ĐẶC BIỆT', l1 = 'NGÀY', l2 = 'NHẬN XE', sub = '', over = false}) => {
  const f = useCurrentFrame();
  const o = inOut(f, len, 4, 6);
  return (
    <AbsoluteFill style={{opacity: o}}>
      <AbsoluteFill style={{background: over ? 'rgba(13,13,16,0.38)' : 'rgba(13,13,16,0.72)'}} />
      {!over && <AbsoluteFill style={{background: 'radial-gradient(circle at 45% 42%, rgba(255,122,69,0.22), transparent 60%)'}} />}
      {!over && <AbsoluteFill style={{backgroundImage: `linear-gradient(${C.line} 2px, transparent 2px), linear-gradient(90deg, ${C.line} 2px, transparent 2px)`,
        backgroundSize: '120px 120px', opacity: 0.5, maskImage: 'radial-gradient(circle at 50% 45%, black, transparent 75%)',
        transform: `scale(${1.04 - 0.04 * ease(f, 0, 14)})`}} />}
      {/* over (trên đoạn ghép): canh ĐÁY vào LOW_Y — mặt người tự quay thường ở nửa trên khung, chữ không che mặt */}
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, ...(over ? {top: LOW_Y, transform: 'translateY(-100%)'} : {top: 640})}}>
        <Eyebrow style={{opacity: ease(f, 2, 12), fontSize: 32}}>{eyebrow}</Eyebrow>
        <Bar w={420 * ease(f, 4, 20)} style={{marginTop: 18, height: 6}} />
        {over ? (   /* trên đoạn ghép: một dòng gọn kiểu thẻ tên chuyến của kênh mẫu — khối thấp, không lên tới mặt */
          <div style={{marginTop: 14, display: 'flex', flexWrap: 'wrap', gap: '0 24px'}}>
            {[[l1, C.text, 5], [l2, C.accent, 9]].filter(([t]) => t).map(([t, col, at]) => (
              <Rise key={at} p={pop(f, at, {damping: 18, stiffness: 170, mass: 0.6})}
                style={{fontFamily: HEAD, fontWeight: 800, fontSize: Math.min(130, Math.floor(SAFE_W / ((l1.length + l2.length + 1) * 0.46))), lineHeight: 1.12,
                  color: col, textShadow: SHADOW}}>{t}</Rise>
            ))}
          </div>
        ) : (
        <div style={{marginTop: 18}}>
          <Rise p={pop(f, 5, {damping: 18, stiffness: 170, mass: 0.6})}
            style={{fontFamily: HEAD, fontWeight: 800, fontSize: Math.min(250, Math.floor(SAFE_W / (l1.length * 0.46))), lineHeight: 1.12,   /* co cho vừa 1 dòng; giãn đủ chỗ dấu tiếng Việt */ color: C.text, textShadow: SHADOW}}>{l1}</Rise>
          <Rise p={pop(f, 9, {damping: 18, stiffness: 170, mass: 0.6})}
            style={{fontFamily: HEAD, fontWeight: 800, fontSize: Math.min(250, Math.floor(SAFE_W / (l2.length * 0.46))), lineHeight: 1.12, marginTop: 18, color: C.accent, textShadow: SHADOW}}>{l2}</Rise>
        </div>
        )}
        {sub && <div style={{fontFamily: BODY, fontWeight: 500, fontSize: 44, color: C.muted, marginTop: over ? 8 : 26,
          opacity: ease(f, 18, 30), transform: `translateX(${(1 - ease(f, 18, 32)) * -30}px)`}}>{sub}</div>}
      </div>
    </AbsoluteFill>
  );
};

const TeaserTag = ({len}) => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity: inOut(f, len, 8, 4)}}>
      <Scrim from="top" o={0.7} />
      <div style={{position: 'absolute', left: SAFE.left, top: 250}}>
        <Bar w={260 * ease(f, 2, 16)} style={{height: 6}} />
        <div style={{marginTop: 14}}>
          <Rise p={pop(f, 4)} style={{fontFamily: HEAD, fontWeight: 800, fontSize: 72, color: C.text, textShadow: SHADOW, letterSpacing: 1}}>
            TẬP NÀY CÓ GÌ?</Rise>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// Nhãn chương trình nhỏ ở góc
const Hud = ({len, name = ''}) => {
  const f = useCurrentFrame();
  const o = inOut(f, len, 10, 6);
  return (
    <DauGoc topic={name} style={{position: 'absolute', top: K.brand.top, left: K.brand.left, opacity: o * 0.95,
      transform: `translateX(${(1 - ease(f, 0, 12)) * -24}px)`}} />
  );
};

// TÍT GHIM (highlight, David duyệt 2026-11-04 — học 5/20 highlight Việt: Pháp Hoà, Dat Bike, Vũ Linh…): sau thẻ tít mở đầu, tít thu
// nhỏ thành dải 1–2 dòng ngay dưới dấu kênh, giữ tới trước màn chốt — người lướt vào giữa clip vẫn biết clip nói gì. Không che mặt
// (mặt được nâng về ~y 800). text = tít của clip (luật 7 cat-doan-noi-bat).
const PinTitle = ({text = '', len}) => {
  const f = useCurrentFrame();
  const o = inOut(f, len, 10, 8);
  const size = text.length > 30 ? 46 : 54;
  return (
    <div style={{position: 'absolute', top: 284, left: SAFE.left, width: SAFE_W, opacity: o, transform: `translateY(${(1 - ease(f, 0, 12)) * -16}px)`}}>
      <div style={{display: 'inline-block', maxWidth: SAFE_W, padding: '8px 18px 10px', borderRadius: 14, background: 'rgba(13,13,16,0.72)',
        borderLeft: `6px solid ${C.accent}`}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: 1.12, paddingTop: '0.08em', textTransform: 'uppercase',
          color: C.text, textWrap: 'balance'}}>{text}</div>
      </div>
    </div>
  );
};

// Thẻ vòng: số viền cam như montage của mẫu
const Round = ({n, of = 3, text, len}) => {
  const f = useCurrentFrame();
  const o = inOut(f, len, 6, 8);
  const p = pop(f, 0, {damping: 20, stiffness: 160, mass: 0.7});
  return (
    <AbsoluteFill style={{opacity: o}}>
      <Scrim from="top" o={0.9} />
      <div style={{position: 'absolute', top: 300, left: SAFE.left, width: SAFE_W}}>
        <Eyebrow style={{opacity: ease(f, 2, 12)}}>VÒNG</Eyebrow>
        <div style={{display: 'flex', alignItems: 'baseline', gap: 14, transform: `translateY(${(1 - p) * 60}px)`}}>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 150, lineHeight: 1, color: 'transparent', WebkitTextStroke: `4px ${C.accent}`}}>
            {String(n).padStart(2, '0')}</div>
          <div style={{fontFamily: HEAD, fontWeight: 700, fontSize: 56, color: C.muted}}>/ {String(of).padStart(2, '0')}</div>
        </div>
        <div style={{marginTop: 4}}>
          <Rise p={pop(f, 4)} style={{fontFamily: HEAD, fontWeight: 800, fontSize: text.length > 14 ? 92 : 110, lineHeight: 1,
            color: C.text, textShadow: SHADOW}}>{text}</Rise>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// Nhãn chỉ vào xe: thẻ tối + mũi tên cam
const Pointer = ({text, x, y, len}) => {
  const f = useCurrentFrame();
  const p = pop(f, 0);
  const draw = ease(f, 4, 16);
  return (
    <div style={{position: 'absolute', left: x, top: y, transform: 'translate(-100%, -100%)', opacity: Math.min(1, p * 1.4) * ease(f, len - 8, len, 1, 0),
      display: 'flex', flexDirection: 'column', alignItems: 'flex-end'}}>
      <div style={{background: C.card, border: `2px solid ${C.line}`, borderRadius: 24, padding: '16px 28px', boxShadow: '0 20px 50px rgba(0,0,0,0.45)',
        transform: `translateY(${(1 - p) * 30}px) scale(${0.94 + 0.06 * p})`}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 62, lineHeight: 1, color: C.text, whiteSpace: 'nowrap'}}>{text}</div>
      </div>
      <svg width="110" height="100" viewBox="0 0 110 100" style={{marginRight: -16}}>
        <path d="M14 6 C 56 18, 84 44, 98 88" stroke={C.accent} strokeWidth="7" fill="none" strokeLinecap="round"
          strokeDasharray="130" strokeDashoffset={130 * (1 - draw)} />
        <circle cx="98" cy="88" r={9 * ease(f, 14, 20)} fill={C.accent} />
      </svg>
    </div>
  );
};

// Giới thiệu nhân vật: đúng kiểu LowerThird của mẫu
const NameCard = ({tag, name, sub, len}) => {
  const f = useCurrentFrame(); const giua = useGiua();
  const o = inOut(f, len, 8, 8);
  return (
    <AbsoluteFill style={{opacity: o}}>
      {!giua && <Scrim o={1} />}
      <AbsoluteFill style={{border: `6px solid ${C.accent}`, opacity: ease(f, 0, 6) * 0.9}} />
      <div style={giua ? {position: 'absolute', ...KHOI_GIUA} : {position: 'absolute', left: SAFE.left, top: LOW_Y, transform: 'translateY(-100%)'}}>
        <Eyebrow style={{opacity: ease(f, 2, 12)}}>{tag}</Eyebrow>
        <Bar w={420 * ease(f, 4, 22)} style={{height: 6, marginTop: 14}} />
        <div style={{marginTop: 16}}>
          <Rise p={pop(f, 6)} style={{fontFamily: HEAD, fontWeight: 800, fontSize: 150, lineHeight: 1, color: C.text, letterSpacing: 4, textShadow: SHADOW}}>{name}</Rise>
        </div>
        <div style={{fontFamily: BODY, fontWeight: 500, fontSize: 42, color: C.muted, marginTop: 10,
          opacity: ease(f, 16, 28), transform: `translateX(${(1 - ease(f, 16, 30)) * -30}px)`}}>{sub}</div>
      </div>
    </AbsoluteFill>
  );
};

// Danh sách hiện theo lời (1–2–3 năm sau, các nước…): dòng bắt đầu bằng số → số viền cam; hiện đúng mốc được nói
const Chips = ({items, start, len, top}) => {
  const f = useCurrentFrame(); const giua = useGiua();
  const o = inOut(f, len, 4, 6);
  const n = items.length;
  // cỡ chữ tự thu cho mục DÀI NHẤT vẫn một dòng (người dùng chỉ ra 2026-11-04: "KHÔNG BỆNH TẬT NHIỀU" xuống 2 dòng → tràn đè phụ đề)
  const longest = Math.max(...items.map(([t]) => t.replace(/^\d+\s+/, '').length + (/^\d+\s/.test(t) ? 4 : 0)));
  const size = Math.min(n > 3 ? 92 : 110, Math.floor(SAFE_W / (longest * 0.46)));
  return (
    <AbsoluteFill style={{opacity: o}}>
      {!giua && <Scrim o={0.9} />}
      {/* neo ĐÁY vào LOW_Y: khối mọc LÊN, không bao giờ xuống dải phụ đề (không ước chiều cao) */}
      <div style={giua ? {position: 'absolute', ...KHOI_GIUA, alignItems: 'stretch'} : {position: 'absolute', left: SAFE.left, width: SAFE_W, ...(top != null ? {top} : {top: LOW_Y, transform: 'translateY(-100%)'})}}>
        {items.map(([t, at], i) => {
          const p = pop(f, fr(at - start), {damping: 18, stiffness: 170, mass: 0.6});
          const parts = t.split(' ');
          const num = /^\d+$/.test(parts[0]) ? parts.shift() : null;
          const last = i === n - 1;
          return (
            <div key={i} style={{display: 'flex', alignItems: 'baseline', justifyContent: giua ? 'center' : 'flex-start', gap: 26, padding: '6px 0', borderBottom: !last ? `2px solid ${C.line}` : 'none',
              opacity: Math.min(1, p * 1.5)}}>
              {num && <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: size * 1.18, lineHeight: 1, width: 90, color: 'transparent',
                WebkitTextStroke: `4px ${C.accent}`, transform: `translateY(${(1 - p) * 40}px)`}}>{num}</div>}
              <Rise p={p} style={{fontFamily: HEAD, fontWeight: 800, fontSize: size, lineHeight: 1, color: C.text, textShadow: SHADOW, whiteSpace: 'nowrap'}}>{parts.join(' ')}</Rise>
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// Thẻ địa điểm: ghim cam + tên nơi chốn (kiểu LowerThird)
const Location = ({eyebrow = 'ĐỊA ĐIỂM', place, sub, len}) => {
  const f = useCurrentFrame(); const giua = useGiua();
  const o = inOut(f, len, 8, 8);
  const p = pop(f, 0);
  return (
    <AbsoluteFill style={{opacity: o}}>
      {!giua && <Scrim o={1} />}
      <div style={giua ? {position: 'absolute', ...KHOI_GIUA} : {position: 'absolute', left: SAFE.left, top: LOW_Y, transform: 'translateY(-100%)', width: SAFE_W}}>
        <div style={{display: 'flex', alignItems: 'center', justifyContent: giua ? 'center' : 'flex-start', gap: 14}}>
          <svg width="40" height="40" viewBox="0 0 24 24" style={{transform: `translateY(${(1 - p) * -30}px)`, opacity: p}}>
            <path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z" fill={C.accent} />
            <circle cx="12" cy="10" r="2.6" fill={C.bg} />
          </svg>
          <Eyebrow style={{opacity: ease(f, 2, 12)}}>{eyebrow}</Eyebrow>
        </div>
        <Bar w={420 * ease(f, 4, 22)} style={{height: 6, marginTop: 14}} />
        <div style={{marginTop: 16}}>
          <Rise p={pop(f, 6)} style={{fontFamily: HEAD, fontWeight: 800, fontSize: Math.max(84, Math.min(150, Math.floor(SAFE_W / (0.5 * Math.max(place.length, 6))))), lineHeight: 1.05, color: C.text, textShadow: SHADOW, textWrap: 'balance'}}>{place}</Rise>
        </div>
        {sub && <div style={{fontFamily: BODY, fontWeight: 500, fontSize: 42, color: C.muted, marginTop: 10,
          opacity: ease(f, 16, 28), transform: `translateX(${(1 - ease(f, 16, 30)) * -30}px)`}}>{sub}</div>}
      </div>
    </AbsoluteFill>
  );
};

// Chú thích bám theo xe: chấm cam + đường mảnh + thẻ tối
const Callout = ({text, dx, dy, track, start, len}) => {
  const f = useCurrentFrame();
  const t = start + f / FPS, ts = track.map((k) => k[0]);
  const x = interpolate(t, ts, track.map((k) => k[1]), clamp), y = interpolate(t, ts, track.map((k) => k[2]), clamp);
  const d = ease(f, 0, 10), p = pop(f, 6);
  const lx = x + dx * d, ly = y + dy * d;
  return (
    <AbsoluteFill style={{opacity: ease(f, len - 8, len, 1, 0)}}>
      <svg width={W} height={H} style={{position: 'absolute'}}>
        <line x1={x} y1={y} x2={lx} y2={ly} stroke={C.text} strokeWidth="3" opacity="0.9" />
        <circle cx={x} cy={y} r={22 * ease(f, 0, 6)} fill="none" stroke={C.accent} strokeWidth="3" opacity="0.6" />
        <circle cx={x} cy={y} r={10 * ease(f, 0, 6)} fill={C.accent} />
      </svg>
      <div style={{position: 'absolute', left: lx, top: ly, transform: `translate(-50%, -100%) translateY(${(1 - p) * 20}px)`,
        opacity: Math.min(1, p * 1.4), background: C.card, border: `2px solid ${C.line}`, borderRadius: 20, padding: '12px 22px',
        boxShadow: '0 20px 50px rgba(0,0,0,0.45)', whiteSpace: 'nowrap'}}>
        <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: 50, lineHeight: 1, color: C.text}}>{text}</div>
      </div>
    </AbsoluteFill>
  );
};

const Replay = ({text, len, eyebrow = 'KHOẢNH KHẮC'}) => {
  const f = useCurrentFrame();
  const o = inOut(f, len, 6, 8);
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{background: 'radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,0.7) 100%)'}} />
      <div style={{position: 'absolute', left: 0, width: W, height: 4, top: (f * 37) % H, background: 'rgba(255,255,255,0.18)'}} />
      <div style={{position: 'absolute', top: K.brand.top, left: SAFE.left, display: 'flex', alignItems: 'center', gap: 16, opacity: o}}>
        <div style={{display: 'inline-flex', alignItems: 'center', gap: 10, padding: '10px 22px', borderRadius: 999,
          background: C.accentSoft, border: `2px solid ${C.accent}`}}>
          <div style={{width: 12, height: 12, borderRadius: 6, background: C.accent, opacity: 0.4 + 0.6 * Math.abs(Math.sin(f / 8))}} />
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 30, letterSpacing: 4, color: C.accent}}>REPLAY</div>
        </div>
      </div>
      <AbsoluteFill style={{opacity: Math.min(ease(f, 12, 22), o)}}>
        <Scrim o={0.9} />
        <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: LOW_Y, transform: 'translateY(-100%)'}}>
          <Eyebrow>{eyebrow}</Eyebrow>
          <div style={{fontFamily: BODY, fontWeight: 700, fontSize: 62, lineHeight: 1.15, color: C.text, marginTop: 10, textShadow: SHADOW}}>{text}</div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Outro = ({len, eyebrow = 'CHÚC MỪNG', lines = ['CHỊ CÓ', 'XE MỚI.'], cta = 'Theo dõi để xem tập sau'}) => {
  const f = useCurrentFrame();
  const colors = [C.accent, C.text, '#FFB38F', C.muted];
  const done = 22;
  return (
    <AbsoluteFill>
      {Array.from({length: 70}).map((_, i) => {
        const x0 = random(`x${i}`) * W, sp = 6 + random(`s${i}`) * 8, delay = random(`d${i}`) * 25;
        const t = Math.max(0, f - delay);
        return <div key={i} style={{position: 'absolute', left: x0 + Math.sin(t / 8 + i) * 40, top: -60 + t * sp, width: 14, height: 26,
          background: colors[i % 4], opacity: 0.85, transform: `rotate(${t * (6 + i % 7)}deg) scaleX(${Math.cos(t / 5 + i)})`, borderRadius: 3}} />;
      })}
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 720}}>
        <Eyebrow style={{opacity: ease(f, 2, 12), fontSize: 32}}>{eyebrow}</Eyebrow>
        <div style={{marginTop: 14, display: 'flex', flexDirection: 'column', gap: 190 * 0.24}}>
          {lines.map((l, i) => (
            <Rise key={i} p={pop(f, 5 + i * 5, {damping: 18, stiffness: 170, mass: 0.6})}
              style={{fontFamily: HEAD, fontWeight: 800, fontSize: 190, lineHeight: 1.14, color: i ? C.accent : C.text, textShadow: SHADOW}}>{l}</Rise>
          ))}
        </div>
        <Bar w={`${ease(f, done, done + 14) * 80}%`} style={{marginTop: 28}} />
        <div style={{display: 'flex', alignItems: 'center', gap: 12, marginTop: 30, opacity: ease(f, 34, 46),
          transform: `translateX(${(1 - ease(f, 34, 48)) * -24}px)`}}>
          <Arrow size={36} /><div style={{fontFamily: BODY, fontWeight: 600, fontSize: 42, color: C.accent}}>{cta}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ===== MÀN HÀNH ĐỘNG (người dùng chốt): người nói nêu việc người xem làm được → toàn cảnh: vòng tick + NGUYÊN VĂN câu nói
// ({type: 'action', start, end, quote: 'câu đúng từng chữ, **cụm nhấn**', doneAt?}); phụ đề tạm ẩn (câu to = phụ đề) =====
const hiWords = (text, f, a0, step = 2) => {
  let k = 0;
  return text.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((part, i) => {
    const hi = part.startsWith('**');
    const ws = part.replace(/\*\*/g, '').split(/(\s+)/).map((w, j) => {
      if (/^\s+$/.test(w)) return w;
      const a = a0 + (k++) * step;
      return <span key={`${i}-${j}`} style={{opacity: 0.12 + 0.88 * ease(f, a, a + 6), color: hi ? C.accent : C.text}}>{w}</span>;
    });
    return hi && part.length <= 30 ? <span key={i} style={{whiteSpace: 'nowrap'}}>{ws}</span> : ws;
  });
};
const Action = ({len, quote, doneAt, start}) => {
  const f = useCurrentFrame();
  const done = pop(f, doneAt != null ? fr(doneAt) - fr(start) : Math.round(len * 0.55));
  const size = quote.replace(/\*\*/g, '').length <= 60 ? 58 : quote.length <= 110 ? 50 : 44;
  return (
    <AbsoluteFill style={{opacity: inOut(f, len, 8, 8), background: C.bg}}>
      <AbsoluteFill style={{background: 'radial-gradient(circle at 45% 38%, rgba(255,122,69,0.16), transparent 60%)'}} />
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 250, height: 1000, display: 'flex', flexDirection: 'column',
        justifyContent: 'center', gap: 56}}>
        <div style={{width: 260, height: 260, borderRadius: '50%', border: `3px solid ${C.accent}`, background: C.accentSoft,
          display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${0.85 + 0.15 * pop(f, 2)})`}}>
          <svg width={150} height={150} viewBox="0 0 24 24" fill="none" stroke="#30A46C" strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round">
            <path d="M5 12.5l4.5 4.5L19 7.5" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - Math.min(1, done)} />
          </svg>
        </div>
        <div style={{fontFamily: BODY, fontWeight: 700, fontSize: size, lineHeight: 1.36, color: C.text, textWrap: 'balance'}}>{hiWords(quote, f, 8)}</div>
      </div>
    </AbsoluteFill>
  );
};

// ===== MÀN CHỐT (người dùng chốt — MỌI video): ~4 s cuối, cả hình lùi vào khung bo góc phía trên (Show co lớp hình), câu chốt
// bên dưới — câu Claude TỰ SÁNG TẠO theo nội dung: CTA = {text, kind} trong danh-sach-cat.js (null = không có màn chốt). Phụ đề vẫn chạy ở đáy. =====
const CTA_LEN = 4;
const OVS = holdEnds(OVERLAYS, CTA ? TOTAL - CTA_LEN : TOTAL, HS);   // lớp phủ đã kéo dài theo luật giữ (giu.js)
const ctaK = (f) => !CTA || NGAN_DOC ? 0 : ease(f, fr(TOTAL - CTA_LEN), fr(TOTAL - CTA_LEN) + 14);
const WIN = {w: 400, h: Math.round(400 * 16 / 9), y: 240};
const ctaFrame = (k) => k <= 0 ? {} : {transform: `translate(${(W - WIN.w) / 2 * k}px, ${WIN.y * k}px) scale(${1 + (WIN.w / W - 1) * k})`,
  transformOrigin: '0 0', borderRadius: 36 / (WIN.w / W) * k, overflow: 'hidden', border: k > 0.5 ? `${3 / (WIN.w / W)}px solid ${C.accent}` : 'none'};
const CtaEnd = ({text, kind}) => {
  const f = useCurrentFrame();
  const t = text || CTA_DEF.text;
  const kd = kind || (text ? 'comment' : CTA_DEF.kind);
  const tk = pop(f, fr(CTA_TICK), {damping: 9, stiffness: 220, mass: 0.6});   // tick nhỏ + tiếng ting (Audio trong Show)
  return (
    <div style={{position: 'absolute', left: SAFE.left, top: NGAN_DOC ? SAFE.bottom - 330 : WIN.y + WIN.h + 30, width: SAFE_W, padding: '30px 34px', boxSizing: 'border-box',
      borderRadius: 36, background: C.card, border: `2px solid ${C.line}`, boxShadow: '0 30px 80px rgba(0,0,0,0.45)', display: 'flex',
      alignItems: 'center', gap: 30, opacity: ease(f, 10, 18), transform: `translateY(${(1 - pop(f, 12)) * 40}px)`}}>
      <div style={{position: 'relative', flexShrink: 0, width: 140, height: 140, borderRadius: '50%', background: C.accent, display: 'flex',
        alignItems: 'center', justifyContent: 'center', boxShadow: '0 0 60px rgba(255,122,69,0.45)', transform: `scale(${1 + 0.04 * Math.sin(f / 6)})`}}>
        <svg width={82} height={82} viewBox="0 0 24 24" fill="none" stroke={C.bg} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">{(CTA_ICONS[kd] || CTA_ICONS.comment).map((d, i) => <path key={i} d={d} />)}</svg>
        {kd === 'comment' && <div style={{position: 'absolute', top: 55, display: 'flex', gap: 9}}>
          {[0, 1, 2].map((i) => <div key={i} style={{width: 10, height: 10, borderRadius: '50%', background: C.bg, opacity: 0.35 + 0.65 * Math.max(0, Math.sin((f - i * 5) / 5))}} />)}
        </div>}
        <div style={{position: 'absolute', right: -6, top: -6, width: 54, height: 54, borderRadius: '50%', background: '#30A46C', border: `4px solid ${C.bg}`,
          display: 'flex', alignItems: 'center', justifyContent: 'center', transform: `scale(${tk})`, boxShadow: `0 0 ${24 * Math.min(1, tk)}px rgba(48,164,108,0.8)`}}>
          <svg width={28} height={28} viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth="3.8" strokeLinecap="round" strokeLinejoin="round">
            <path d="M5 12.5l4.5 4.5L19 7.5" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - Math.min(1, tk)} />
          </svg>
        </div>
      </div>
      <div style={{fontFamily: BODY, fontWeight: 700, fontSize: ((n) => n <= 45 ? 50 : n <= 60 ? 46 : 42)(t.replace(/\*\*/g, '').length), lineHeight: 1.3, color: C.text,
        textWrap: 'balance'}}>{hiWords(t, f, 18)}</div>
    </div>
  );
};

// ===== THẺ CUỐI (highlight, người dùng chốt 2026-11-03): ~1,8 s SAU màn chốt, dẫn về bản đầy đủ — kiểu thẻ cuối Have A Sip.
// ENDCARD = {title, speaker, clip, at, len} trong danh-sach-cat.js (null = không có). CHỈ chữ của bản gốc: title = tên tập gốc, speaker = tên
// người nói gốc — không nhãn tự viết ("BẢN ĐẦY ĐỦ", "XEM NGAY"…). Ảnh = khung đứng hình của người nói (clip, at = giây trong clip). =====
const ENDCARD = (EDL.THE_CUOI ?? !NGAN_DOC) ? (EDL.ENDCARD || null) : null;   // dọc ngắn: không thẻ cuối (10/11/2026)
const EndCard = ({title, speaker, clip, at, play = true, yt = 0, schedule = ''}) => {   // schedule: lịch phát David đưa (PO-6)   // play: nhãn "Bản đầy đủ trên kênh …"; false = thẻ nhận diện (vlog)
  const f = useCurrentFrame();
  // yt (giây, plan.json "ytEnd"): sau thẻ nhận diện là MÀN KẾT YOUTUBE (khung chừa 2 video + nút đăng ký), có nhạc kênh nhỏ
  if (yt > 5 && f >= fr(BRAND.endcardLen)) return (
    <AbsoluteFill><YtEnd name={BRAND.name} topic={title} schedule={schedule} start={fr(BRAND.endcardLen)} />
      {MUSIC.tracks?.[0] && <Audio src={staticFile(`hieu-ung-am-thanh/${MUSIC.tracks[0].f}.mp3`)} loop
        volume={(k) => 0.16 * Math.min(1, k / 20) * Math.min(1, Math.max(0, (fr(yt) - k) / 40))} />}</AbsoluteFill>);
  const p = pop(f, 0, {damping: 15, stiffness: 160, mass: 0.7});
  const pb = pop(f, 8, {damping: 10, stiffness: 220, mass: 0.6});
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, opacity: ease(f, 0, 6)}}>
      {clip && <Freeze frame={0}><OffthreadVideo src={staticFile(`clips/${clip}.mp4`)} trimBefore={fr(at || 0)} muted
        style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'brightness(0.42) saturate(1.1)', transform: `scale(${1.06 + f * 0.0012})`}} /></Freeze>}
      <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(13,13,16,0.1) 30%, rgba(13,13,16,0.92) 78%)'}} />
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 1000, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 34,
        transform: `translateY(${(1 - p) * 60}px)`}}>
        <EndCardBody title={title} speaker={speaker} play={play} schedule={schedule} kenh={HS.man_cuoi_kenh || ''} big={96} gap={34} shadow={SHADOW} />
      </div>
    </AbsoluteFill>
  );
};

// ===== CHUYỂN CẢNH HIGHLIGHT: đoạn `jump` (đứng hình) — tối dần + chip ⏩/⏪ + mốc phút của câu kế trong tập gốc =====
const STREAKS = Array.from({length: 16}, (_, i) => ({y: (i * 137) % 100, h: 2 + (i * 7) % 6, w: 18 + (i * 29) % 40, ph: (i * 0.37) % 1}));
const Tua = ({seg}) => {
  const f = useCurrentFrame();
  const p = Math.min(1, f / Math.max(1, fr(seg.dur)));
  const o = Math.sin(Math.PI * p);
  const soft = toneAt(seg.start) === 'lang';
  const back = seg.jump.to < seg.jump.from;
  const s = 54;
  return (
    <AbsoluteFill style={{background: `rgba(10,10,12,${(soft ? 0.78 : 0.62) * o})`}}>
      {!soft && STREAKS.map((k, i) => {
        const q = ((p * 2.2 + k.ph) % 1.4) - 0.4;
        const x = back ? 1 - q - k.w / 100 : q;
        return <div key={i} style={{position: 'absolute', top: `${k.y}%`, left: `${x * 100}%`, width: `${k.w}%`, height: k.h,
          borderRadius: k.h, opacity: 0.55 * o, background: `linear-gradient(90deg, transparent, ${i % 3 ? C.text : C.accent})`}} />;
      })}
      <div style={{position: 'absolute', left: 0, right: 0, top: H * 0.42, display: 'flex', justifyContent: 'center',
        opacity: Math.min(1, o * (soft ? 1.2 : 1.6)), transform: soft ? 'none' : `translateX(${(back ? 0.5 - p : p - 0.5) * 60}px) scale(${0.92 + 0.12 * o})`}}>
        <div style={{display: 'flex', alignItems: 'center', gap: s * 0.5, padding: `${s * 0.3}px ${s * 0.6}px`, borderRadius: s,
          background: soft ? 'rgba(24,24,28,0.9)' : C.accent, border: soft ? `2px solid ${C.accent}` : 'none',
          boxShadow: soft ? 'none' : '0 0 60px rgba(255,122,69,0.55)'}}>
          <svg width={s * 1.3} height={s} viewBox="0 0 26 20" fill={soft ? C.accent : C.bg} style={{transform: back ? 'scaleX(-1)' : 'none'}}>
            <path d="M1 1 L12 10 L1 19 Z M13 1 L24 10 L13 19 Z" /></svg>
          <div style={{fontFamily: HEAD, fontWeight: 800, fontSize: s * 1.25, lineHeight: 1, color: soft ? C.text : C.bg, fontVariantNumeric: 'tabular-nums'}}>
            {mmss(seg.jump.to)}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ===== THANH TẬP GỐC (highlight): các câu được trích tô cam mờ, phần đã phát cam đậm, chấm = vị trí đang phát trong tập gốc =====
const srcAt = (t) => {
  let s = SEGS[0];
  for (const x of SEGS) if (t >= x.start) s = x;
  if (s.jump) { const p = Math.min(1, (t - s.start) / s.dur); const e = p * p * (3 - 2 * p); return s.jump.from + (s.jump.to - s.jump.from) * e; }
  return Math.min(s.to, s.from + Math.max(0, t - s.start) * s.rate);
};
const ThanhGoc = () => { const f = useCurrentFrame(); return <ThanhThoiGian t={f / FPS} T={TOTAL} k={K} />; };
const SrcBar = () => {
  const f = useCurrentFrame();
  if (!HL || HL.bar === false) return null;
  const t = f / FPS, T = HL.src_duration, now = srcAt(t);
  const parts = SEGS.filter((s) => !s.jump && !s.freeze);
  const bar = (a, w, op) => <div style={{position: 'absolute', left: `${a / T * 100}%`, width: `${w / T * 100}%`, top: 0, bottom: 0,
    borderRadius: 4, background: C.accent, opacity: op}} />;
  const label = {fontFamily: BODY, fontWeight: 600, fontSize: 24, color: C.text, fontVariantNumeric: 'tabular-nums', whiteSpace: 'nowrap'};
  return (
    <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: SAFE.bottom - 40, height: 40, display: 'flex', alignItems: 'center',
      gap: 18, padding: '0 16px', boxSizing: 'border-box', borderRadius: 40, background: 'rgba(0,0,0,0.5)', opacity: 1 - ctaK(f)}}>
      <div style={label}>{mmss(now)}</div>
      <div style={{position: 'relative', flex: 1, height: 8, borderRadius: 4, background: 'rgba(255,255,255,0.18)'}}>
        {parts.map((s, i) => (
          <React.Fragment key={i}>
            {bar(s.from, s.to - s.from, 0.35)}
            {t >= s.start && bar(s.from, Math.max(0, Math.min(s.to, now) - s.from), 1)}
          </React.Fragment>
        ))}
        <div style={{position: 'absolute', left: `${now / T * 100}%`, top: 4, width: 18, height: 18, borderRadius: 9, background: C.text,
          transform: 'translate(-50%, -50%)', boxShadow: '0 0 12px rgba(255,122,69,0.7)'}} />
      </div>
      <div style={label}>{mmss(T)}</div>
    </div>
  );
};

// ===== CẢNH MINH HOẠ VẼ (người dùng chốt 2026-11-04 — như thẻ toàn cảnh của chế độ 1 video): nền tối + 1–3 biểu tượng nét vẽ dần
// ĐÚNG LÚC lời nhắc tới (icons: [[tên, giây timeline]]), mũi tên nối khi `flow`, bên dưới NGUYÊN VĂN câu nói sáng dần theo lời.
// 4–8 s / cảnh, 3–4 cảnh / video; phụ đề tạm ẩn (câu to giữa màn là phụ đề). Biểu tượng: bieu-tuong.jsx (một nguồn với chế độ 1 video). =====
const Scene = ({len, start, icons, quote, flow = true}) => {
  const f = useCurrentFrame();
  const n = icons.length, sz = n === 1 ? 520 : n === 2 ? 360 : 230;
  const plain = quote.replace(/\*\*/g, '');
  const size = plain.length <= 60 ? 58 : plain.length <= 110 ? 50 : plain.length <= 170 ? 44 : 38;
  const words = []; quote.split(/(\*\*[^*]+\*\*)/).filter(Boolean).forEach((part) => {
    const hi = part.startsWith('**'); part.replace(/\*\*/g, '').split(/\s+/).filter(Boolean).forEach((w) => words.push([w, hi]));
  });
  const span = Math.max(1, len - fr(0.8));   // chữ sáng dần đều theo thời lượng cảnh (≈ nhịp nói)
  return (
    <AbsoluteFill style={{opacity: inOut(f, len, 8, 5), background: C.bg}}>
      <AbsoluteFill style={{background: 'radial-gradient(circle at 50% 30%, rgba(255,122,69,0.18), transparent 60%)'}} />
      <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: 250, height: 1000, display: 'flex', flexDirection: 'column',
        justifyContent: 'center', gap: 64}}>
        <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 18}}>
          {icons.map(([name, at], i) => {
            const a = fr(at - start), p = pop(f, a, {damping: 15, stiffness: 150, mass: 0.7});
            return (
              <React.Fragment key={i}>
                {flow && i > 0 && <div style={{opacity: ease(f, a - 4, a + 4)}}><Arrow size={46} /></div>}
                <div style={{position: 'relative', width: sz, height: sz, opacity: Math.min(1, p * 1.4), transform: `translateY(${(1 - p) * 40}px)`}}>
                  <svg width={sz} height={sz} style={{position: 'absolute', inset: 0}}>
                    <circle cx={sz / 2} cy={sz / 2} r={sz * 0.46} fill="rgba(255,122,69,0.07)" stroke={C.accent} strokeOpacity={0.3} strokeWidth={2}
                      strokeDasharray={`${sz * 0.06} ${sz * 0.05}`} />
                  </svg>
                  <div style={{position: 'absolute', left: sz * 0.18, top: sz * 0.18, filter: 'drop-shadow(0 0 18px rgba(255,122,69,0.45))'}}>
                    <Icon name={name} size={sz * 0.64} at={a} stroke={2.8} />
                  </div>
                </div>
              </React.Fragment>
            );
          })}
        </div>
        <div style={{fontFamily: BODY, fontWeight: 700, fontSize: size, lineHeight: 1.36, color: C.text, textWrap: 'balance', textAlign: 'center'}}>
          {words.map(([w, hi], i) => {
            const o = ease(f, 6 + (span * i) / words.length, 6 + (span * i) / words.length + 8);
            return <span key={i} style={{opacity: 0.18 + 0.82 * o, color: hi ? C.accent : C.text}}>{w}{i < words.length - 1 ? ' ' : ''}</span>;
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// Nền của lớp tự chuyển toàn màn hình: hiện/ẩn mềm 6 khung, nền tối + quầng cam (như cảnh toàn màn hình của bộ nhận diện)
const FullOv = ({children}) => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity: ease(f, 0, 6)}}>
      <AbsoluteFill style={{backgroundColor: C.bg}} />
      <AbsoluteFill style={{background: 'radial-gradient(circle at 50% 44%, rgba(255,122,69,0.2), transparent 60%)'}} />
      {children}
    </AbsoluteFill>
  );
};

const IllusOv = ({start, len, ...o}) => <Illus {...o} start={start} len={len} />;
const DiagramOv = ({start, len, ...o}) => <Diagram {...o} start={start} len={len} />;
// MỖI LÚC MỘT CHỖ CHỮ (David chốt 2026-11-08): lớp motion graphic có chữ đang hiện → phụ đề nhường (ẩn đúng khoảng đó, phần
// còn lại của dòng vẫn hiện). Không tính lớp chạy suốt clip (dấu góc, tít ghim, nhãn teaser).
const KHONG_CHU = new Set(['pinTitle', 'hud', 'teaserTag']);
const nhuong = (s) => {
  let parts = [{...s, s0: s.start, s1: s.end}];
  const lop = CTA ? [...OVS, {type: 'cta', start: TOTAL - CTA_LEN, end: TOTAL}] : OVS;   // màn chốt cũng là một chỗ chữ   // s0/s1: mốc gốc của dòng → phần sau tiếp đúng cụm chữ đang nói
  for (const o of lop) {
    if (KHONG_CHU.has(o.type) || o.end == null) continue;
    parts = parts.flatMap((p) => {
      if (o.end <= p.start + 0.1 || o.start >= p.end - 0.1) return [p];
      const r = [];
      if (o.start - p.start >= 0.6) r.push({...p, end: o.start});
      if (p.end - o.end >= 0.6) r.push({...p, start: o.end});
      return r;
    });
  }
  return parts;
};
const TYPES = {illus: IllusOv, diagram: DiagramOv, pinTitle: PinTitle, action: Action, pow: Pow, title: Title, teaserTag: TeaserTag, hud: Hud, round: Round, pointer: Pointer,
  nameCard: NameCard, chips: Chips, callout: Callout, replay: Replay, outro: Outro, location: Location, scene: Scene};

// ===== Nhạc nền có hạ âm khi có lời =====
const musicVol = (f) => {
  const t = f / FPS;
  const fadeIn = interpolate(t, [0, 0.6], [0, 1], clamp), fadeOut = interpolate(t, [TOTAL - 1.5, TOTAL], [1, 0], clamp);
  let v = MUSIC.base;
  if (SUBS.some((s) => t > s.start - 0.15 && t < s.end + 0.15)) v = MUSIC.duck;
  if (MUSIC.loudRanges.some(([a, b]) => t >= a && t < b)) v = MUSIC.loud;
  return v * fadeIn * fadeOut;
};
// MUSIC.tracks = [{f: 'soi-1', a, b, gain}] (highlight): mỗi bài một khoảng timeline, chồng mờ 0,8 s ở mối; không có → music.wav
const XF = 0.8;
// gain không ghi → mức cân của bài ở hồ sơ chung nhac.muc (một nguồn), rồi mới tới 1
const Track = ({tr}) => {
  const a0 = Math.max(0, tr.a - XF);
  const fadeIn = (t) => tr.a <= 0 ? 1 : interpolate(t, [tr.a - XF, tr.a + XF], [0, 1], clamp);
  const fadeOut = (t) => tr.b >= TOTAL ? 1 : interpolate(t, [tr.b - XF, tr.b + XF], [1, 0], clamp);
  return (
    <Sequence from={fr(a0)} durationInFrames={fr(Math.min(TOTAL, tr.b + XF) - a0)} name={`nhac ${tr.f}`} layout="none">
      <Audio src={staticFile(`hieu-ung-am-thanh/${tr.f}.mp3`)} trimBefore={fr(tr.from || 0)} loop
        volume={(k) => { const t = a0 + k / FPS; return musicVol(fr(t)) * (tr.gain ?? HS.nhac?.muc?.[tr.f] ?? 1) * fadeIn(t) * fadeOut(t); }} />
    </Sequence>
  );
};

export const Show = () => {
  const f = useCurrentFrame();
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    Promise.all(FONT_CHECKS.map((x) => document.fonts.load(x, 'Tiếng Việt ĐẾN ĐÂU'))).then(() => continueRender(handle));
  }, [handle]);
  return (
    <AbsoluteFill style={{backgroundColor: C.bg}}>
      <AbsoluteFill style={{background: 'radial-gradient(circle at 45% 38%, rgba(255,122,69,0.16), transparent 60%)'}} />
      <AbsoluteFill style={ctaFrame(ctaK(f))}>
        {SEGS.map((s, i) => (
          <Sequence key={s.id} from={fr(s.start)} durationInFrames={fr(s.dur)} name={s.id}>
            <Clip seg={s} />
            {s.jump && <Tua seg={s} />}
            {i > 0 && !SHORT && !s.jump && !SEGS[i - 1].jump && toneAt(s.start) !== 'lang' && <Flash />}
          </Sequence>
        ))}
      </AbsoluteFill>
      {CTA && (
        <Sequence from={fr(TOTAL - CTA_LEN)} name="chot" layout="none"><AbsoluteFill><CtaEnd text={CTA.text} kind={CTA.kind} /></AbsoluteFill></Sequence>
      )}
      {CTA && (
        <Sequence from={fr(TOTAL - CTA_LEN + CTA_TICK)} name="ting" layout="none"><Audio src={staticFile('hieu-ung-am-thanh/ting.wav')} volume={0.55} /></Sequence>
      )}
      {OVS.map((o, i) => {
        const Comp = TYPES[o.type];
        let g = GUARD[String(i)];
        if (!g && TWO && !o.keep && o.type === 'pinTitle') g = {off: true};
        if (!g && TWO && !o.keep && CONV.has(o.type) && !(o.type === 'pow' && o.start < 0.5))
          g = {full: true, end: o.held ? o.end : Math.min(o.end, o.start + (HS.toan_man_max_s ?? Infinity)), dy: o.y != null ? Math.round(H * 0.44 - (o.y + 120)) : -260};
        if (g?.off) return null;   // tít ghim che đầu người nói / tắt theo 2 trạng thái → ẩn
        // TỰ CHUYỂN TOÀN MÀN HÌNH (David chốt 2026-11-04): lớp này sẽ che mặt / thân trên → nền tối che hình, nội dung dời ra giữa
        // khung + phóng nhẹ, dài tối đa 4 s (guard.end); phụ đề vẫn chạy
        if (g?.full) {
          const lenF = fr(g.end) - fr(o.start);
          return (
            <Sequence key={i} from={fr(o.start)} durationInFrames={lenF} name={`${o.type} (toàn màn hình)`} layout="none">
              <FullOv><GiuaCtx.Provider value={true}><AbsoluteFill>
                <Comp {...o} len={lenF} /></AbsoluteFill></GiuaCtx.Provider></FullOv>
            </Sequence>
          );
        }
        const len = fr(o.end) - fr(o.start);
        // CHẶN CỨNG (người dùng chỉ ra nhiều lần: thẻ / chữ đè phụ đề): mọi lớp không toàn màn hình bị cắt ở mép trên dải phụ đề —
        // lưới an toàn như bo-cuc.js của chế độ 1 video; component vẫn phải tự neo đáy LOW_Y (cắt chữ = lỗi bố cục, chụp soát phải thấy)
        const guard = !FULLSCREEN.has(o.type) && o.type !== 'pow' && o.type !== 'illus' && o.type !== 'diagram' && !(o.type === 'title' && !o.over);
        return (
          <Sequence key={i} from={fr(o.start)} durationInFrames={len} name={o.type} layout="none">
            {guard
              ? <AbsoluteFill><div style={{position: 'absolute', left: 0, top: 0, width: W, height: CAP_TOP - 6, overflow: 'hidden'}}>
                  <AbsoluteFill style={{height: H}}><Comp {...o} len={len} /></AbsoluteFill></div></AbsoluteFill>
              : <AbsoluteFill><Comp {...o} len={len} /></AbsoluteFill>}
          </Sequence>
        );
      })}
      {SUBS.flatMap((s) => nhuong(s)).map((s, i) => {
        const len = fr(s.end) - fr(s.start);
        return (
          <Sequence key={`s${i}`} from={fr(s.start)} durationInFrames={len} name="sub" layout="none">
            <AbsoluteFill><Caption {...s} len={fr(s.s1) - fr(s.s0)} off={fr(s.start) - fr(s.s0)} /></AbsoluteFill>
          </Sequence>
        );
      })}
      {THANH && <SrcBar />}
      {THANH && !(HL && HL.bar !== false) && <Sequence from={0} durationInFrames={fr(TOTAL)} name="thanh-thoi-gian" layout="none"><ThanhGoc /></Sequence>}
      {ENDCARD && (
        <Sequence from={fr(TOTAL)} name="the-cuoi" layout="none"><EndCard {...ENDCARD} /></Sequence>
      )}
      {SEGS.filter((s) => s.jump && toneAt(s.start) !== 'lang').map((s) => (
        <Sequence key={`tua${s.id}`} from={Math.max(0, fr(s.start + s.dur / 2 - 0.21))} name="tua" layout="none">
          <Audio src={staticFile('hieu-ung-am-thanh/tua.wav')} volume={0.32} />
        </Sequence>
      ))}
      {SFX.map((s, i) => (
        <Sequence key={`x${i}`} from={Math.max(0, fr(s.at))} name={s.f} layout="none">
          <Audio src={staticFile(`hieu-ung-am-thanh/${s.f}.wav`)} volume={s.v} />
        </Sequence>
      ))}
      {MUSIC.tracks ? MUSIC.tracks.map((tr, i) => <Track key={`m${i}`} tr={tr} />)
        : <Audio src={staticFile('hieu-ung-am-thanh/music.wav')} volume={musicVol} />}
    </AbsoluteFill>
  );
};
