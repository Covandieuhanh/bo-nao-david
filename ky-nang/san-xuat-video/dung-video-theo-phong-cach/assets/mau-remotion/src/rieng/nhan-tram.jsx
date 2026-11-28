// NHÃN TRẠM — cảnh tự vẽ riêng của video tham quan (David 20/11/2026: "các sản phẩm là giải pháp công nghệ được thể hiện chính trên
// các màn hình máy tính … cần motion graphics phù hợp để không bị che đi các nội dung chính").
// Vì sao tự vẽ: the-canh đặt thẻ theo khoảng trống NGANG quanh người (cho.js), không biết màn hình; thiếu chỗ thì thu cả khung vào ô người
// → che sản phẩm. Ở đây người dựng chọn vị trí `o` từ ảnh đầu / giữa / cuối cảnh (chỗ trống thật: kệ, trần, cửa sổ — không màn hình, không mặt).
// Hai dạng:
//   nhãn trạm  : {so, tong, ten}          → dải mảnh "1/8 │ TÊN DỰ ÁN" (Chia đoạn + Báo hiệu)
//   thẻ ý      : {tieu_de?, dong:[{text, at, to?, gach?}]} → thẻ nhỏ, dòng hiện đúng lúc nói (Đúng lúc), dòng `to` = câu đắt
// o = {x, y, w} theo phần khung (0–1), neo góc trên trái; `phai: true` = trượt vào từ phải.
import React from 'react';
import {AbsoluteFill, Easing, useCurrentFrame, useVideoConfig} from 'remotion';
import {BODY, C, HEAD, ease, pop, rel} from '../chu-de';
import {ChuHien} from '../thu-vien/chu-hien';
import {kieuChu} from '../thu-vien/chuyen-dong';

export const NhanTram = ({sceneId, start, so, tong, ten, tieu_de, dong = [], o = {x: 0.68, y: 0.04, w: 0.3}, phai = true}) => {
  const f = useCurrentFrame();
  const {durationInFrames: d, width: W, height: H} = useVideoConfig();
  const vao = ease(f, 0, 12), ra = ease(f, d - 8, d, 1, 0, Easing.in(Easing.cubic));
  const op = Math.min(vao, ra);
  const dx = (1 - vao) * 50 * (phai ? 1 : -1);
  const blur = ra < 1 ? `blur(${(6 * (1 - ra)).toFixed(2)}px)` : undefined;
  const x = o.x * W, y = o.y * H, w = o.w * W;
  const kc = kieuChu(sceneId);

  if (so != null) {   // dải nhãn trạm — chữ co cho vừa bề rộng `o.w` (tên dài không tràn mép)
    const fs = Math.min(H * 0.032, (w - H * 0.032 * 3.2) / (String(ten).length * 0.7 + 1.6));
    return (
      <AbsoluteFill style={{opacity: op, filter: blur}}>
        <div style={{position: 'absolute', left: x, top: y, width: w, display: 'flex', justifyContent: phai ? 'flex-end' : 'flex-start',
          transform: `translateX(${dx}px)`}}>
          <div style={{display: 'flex', alignItems: 'stretch', borderRadius: fs * 0.5, overflow: 'hidden', background: C.card,
            border: `2px solid ${C.line}`, boxShadow: `0 16px 40px rgba(${C.bongRgb},${C.bongDo})`}}>
            <div style={{background: C.accent, color: C.trenNhan, fontFamily: HEAD, fontWeight: 800, fontSize: fs * 1.05,
              padding: `${fs * 0.32}px ${fs * 0.55}px`, display: 'flex', alignItems: 'center', letterSpacing: 1}}>
              {so}<span style={{opacity: 0.6, fontSize: fs * 0.75, marginLeft: 2}}>/{tong}</span></div>
            <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs, color: C.text, textTransform: 'uppercase', letterSpacing: 2,
              padding: `${fs * 0.32}px ${fs * 0.7}px`, display: 'flex', alignItems: 'center', whiteSpace: 'nowrap'}}>
              <ChuHien text={ten} a={6} kieu={kc} /></div>
          </div>
        </div>
      </AbsoluteFill>
    );
  }

  const fs = Math.min(H * 0.04, w / 10);   // thẻ ý — khung ôm chữ (không rộng thừa), neo về phía trượt vào
  return (
    <AbsoluteFill style={{opacity: op, filter: blur}}>
      <div style={{position: 'absolute', left: x, top: y, width: w, display: 'flex', justifyContent: phai ? 'flex-end' : 'flex-start',
        transform: `translateX(${dx}px)`}}>
      <div style={{width: 'fit-content', maxWidth: '100%', padding: fs * 0.7,
        borderRadius: fs * 0.6, background: C.card, border: `2px solid ${C.line}`, boxShadow: `0 20px 60px rgba(${C.bongRgb},${C.bongDo})`,
        display: 'flex', flexDirection: 'column', gap: fs * 0.72, boxSizing: 'border-box'}}>
        {tieu_de && <div style={{fontFamily: BODY, fontWeight: 700, fontSize: fs * 0.62, letterSpacing: 2.5, color: C.accent,
          textTransform: 'uppercase', textWrap: 'balance'}}><ChuHien text={tieu_de} a={4} kieu={kc} /></div>}
        {dong.map((dg, i) => {
          const a = rel(dg.at ?? start, start);
          if (f < a - 1) return null;
          const p = pop(f, a);
          const g = dg.gach != null ? ease(f, rel(dg.gach, start), rel(dg.gach, start) + 8) : 0;
          const to = !!dg.to;
          const cw = w - fs * 2.4;
          const size = to ? Math.max(fs * 1.05, Math.min(fs * 1.7, cw / (0.56 * Math.max(5, Math.max(...dg.text.split('\n').map((l) => l.length)))))) : fs;
          // Trình bày ý (David góp ý 26/11/2026): mỗi ý có gạch đầu dòng, viết hoa chữ đầu, các ý cách nhau rõ;
          // dòng xuống hàng thụt theo chữ, không chạy dưới gạch
          const chu = dg.text.replace(/^([^\p{L}\p{N}]*)(\p{L})/u, (_, a, b) => a + b.toLocaleUpperCase('vi'));
          const lh = 1.18;
          return (
            <div key={i} style={{alignSelf: 'flex-start', display: 'flex', alignItems: 'flex-start', gap: fs * 0.45,
              opacity: (1 - 0.45 * g) * Math.min(1, p * 1.3), transform: `translateY(${(1 - p) * 14}px)`}}>
              {dong.length > 1 && <div style={{flex: 'none', width: fs * 0.48, height: Math.max(4, fs * 0.12), borderRadius: 4, background: C.accent,
                marginTop: size * lh / 2 - Math.max(4, fs * 0.12) / 2}} />}
              <div style={{position: 'relative', minWidth: 0}}>
                <div style={{fontFamily: to ? HEAD : BODY, fontWeight: to ? 800 : 600, fontSize: size, lineHeight: lh,
                  color: to ? C.accent : C.text, textTransform: to ? 'uppercase' : 'none', whiteSpace: 'pre-line', textWrap: 'pretty'}}>
                  <ChuHien text={chu} a={a} kieu={kc} /></div>
                {g > 0 && <div style={{position: 'absolute', left: 0, top: '52%', height: Math.max(3, fs * 0.09), width: `${g * 100}%`, background: C.accent}} />}
              </div>
            </div>
          );
        })}
      </div>
      </div>
    </AbsoluteFill>
  );
};
