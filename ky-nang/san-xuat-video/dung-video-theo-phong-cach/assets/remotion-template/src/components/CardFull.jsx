// THẺ TOÀN CẢNH (người dùng chốt 2026-11-02): mọi ô thẻ (`card`) không còn đặt nhỏ trên video mà thành một màn hình toàn cảnh —
// hình động của loại thẻ (số chạy, danh sách tick, đồng hồ, biểu đồ, biểu tượng vẽ…) to ở giữa + NGUYÊN VĂN câu người nói (`quote`)
// bên dưới: đầy đủ ý, đúng từng chữ (chỉ sửa chính tả Whisper), KHÔNG tóm tắt. `**từ**` trong quote = tô màu nhấn.
// Mỗi cảnh 4–8 s quanh ý chính (mặt người nói vẫn hiện ~60% video). TỐI GIẢN: một ý · một hình · một câu — có quote thì khung
// thẻ chỉ còn hình động + nhãn, và phụ đề tạm ẩn (Captions.jsx) vì câu to giữa màn chính là phụ đề. Podcast: thẻ vẫn ở giữa sân khấu (không dùng file này).
import React from 'react';
import {useCurrentFrame} from 'remotion';
import {BODY, C, SAFE, SAFE_W, ease, rel} from '../theme';
import {Card, CardInline} from './Overlays';
import {FullShell} from './FullScreen';

const TOP = 250, BOTTOM = 1250;   // nội dung toàn cảnh: dưới thanh trên của nền tảng, trên dải phụ đề

export const Quote = ({text, start, at}) => {
  const f = useCurrentFrame();
  const plain = text.replace(/\*\*/g, '');
  const size = plain.length <= 60 ? 58 : plain.length <= 110 ? 50 : plain.length <= 170 ? 44 : 38;
  const a = at != null ? rel(at, start) : 8;
  // tách theo **…**: phần nhấn tô màu; từng từ hiện nối tiếp nhanh (2 khung/từ)
  const parts = text.split(/(\*\*[^*]+\*\*)/).filter(Boolean);
  let k = 0;
  return (
    <div style={{width: SAFE_W, fontFamily: BODY, fontWeight: 700, fontSize: size, lineHeight: 1.36, color: C.text, textWrap: 'balance'}}>
      {parts.map((part, i) => {
        const hi = part.startsWith('**');
        const words = part.replace(/\*\*/g, '').split(/(\s+)/).map((w, j) => {
          if (/^\s+$/.test(w)) return w;
          const o = ease(f, a + (k++) * 2, a + k * 2 + 6);
          return <span key={`${i}-${j}`} style={{opacity: 0.15 + 0.85 * o, color: hi ? C.accent : C.text}}>{w}</span>;
        });
        // cụm nhấn ngắn (≤ 24 ký tự) không bị xuống dòng giữa chừng ("23 | giờ 22 phút")
        return hi && part.length <= 28 ? <span key={i} style={{whiteSpace: 'nowrap'}}>{words}</span> : words;
      })}
    </div>
  );
};

import HS from '../hoso.json';
// 2 trạng thái: bỏ câu trích dài (phụ đề đã chạy bên dưới) — thẻ chỉ còn hình động + nhãn ngắn
export const CardFull = ({start, quote: q0, quoteAt, ...p}) => { const quote = HS.hai_trang_thai ? null : q0; return (
  <FullShell>
    <div style={{position: 'absolute', left: SAFE.left, width: SAFE_W, top: TOP, height: BOTTOM - TOP, display: 'flex',
      flexDirection: 'column', justifyContent: 'center', gap: 56}}>
      {/* có quote → khung thẻ tối giản: chỉ hình động + nhãn (bỏ tiêu đề/dòng phụ lặp lại câu); variant 'quote' không có hình → bỏ khung */}
      {!(quote && p.variant === 'quote' && !p.icon) && (
        <CardInline.Provider value={quote ? 'min' : true}><Card start={start} {...p} /></CardInline.Provider>
      )}
      {quote && <Quote text={quote} start={start} at={quoteAt} />}
    </div>
  </FullShell>
); };
