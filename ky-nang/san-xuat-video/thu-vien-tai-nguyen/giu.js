// GIỮ CẢNH SAU CHỮ CUỐI (David chốt 2026-11-05, khối 07): lớp chữ / hình chạy theo lời không được tắt ngay khi chữ cuối vừa hiện —
// mắt chưa đọc kịp (vlog Miếu Bà Cam: "QUAY LẠI" chỉ còn 0,4 s, "ĐẦY ĐỦ" 0,75 s). Chuẩn: Kurzgesagt / Vox giữ đồ hoạ ~1–1,5 s sau
// phần tử cuối; phụ đề Netflix ≥ 0,83 s/dòng, ~17 ký tự/giây.
// Luật: hết = max(hết cũ, mốc phần tử cuối + hiện vào + giữ + mờ ra (+ thêm mỗi chữ vượt 3 chữ)), nhưng không quá `dai_max_s` kể từ
// đầu cảnh, không lấn sang lớp giữ-được kế tiếp, không lấn màn chốt / cuối video (`limit`).
// Tham số: ho-so-thuong-hieu/chung.json → canh_minh_hoa.{giu_sau_s, giu_moi_chu_s, hien_vao_s, mo_ra_s, dai_max_s}. Một bản cho mọi khung dựng:
//   montage-template/Show.jsx (OVERLAYS) · remotion-template/Root.jsx (SCENES, props nằm trong s.props).
const HOLD = new Set(['illus', 'diagram', 'action', 'chips', 'pow', 'listItem', 'kinetic', 'scene']);
const words = (t) => (t || '').replace(/\*\*/g, '').trim().split(/\s+/).filter(Boolean).length;

// mốc phần tử cuối hiện ra + nhãn của nó (giây, cùng hệ giây với start)
const lastOf = (o) => {
  const p = {...o, ...(o.props || {})};
  if (p.type === 'diagram') { const L = p.items || []; const z = L.reduce((m, it) => ((it.at ?? p.start) >= (m.at ?? p.start) ? it : m), L[0] || {});
    return {t: Math.max(p.start, z.at ?? p.start) + (p.mode === 'luoi' ? (z.upto || 0) * 0.04 : 0), w: Math.max((z.label || '').split(/\s+/).length, (p.label || '').split(/\s+/).length)}; }
  if (p.type === 'illus') {
    let t = p.start, lb = p.label || '';
    for (const it of p.items || []) if ((it.at ?? p.start) >= t) { t = it.at ?? p.start; lb = it.label || lb; }
    if (p.num) t = Math.max(t, p.num.at + (p.num.dur || 1.2));
    return {t, w: Math.max(words(lb), words(p.label))};
  }
  if (p.type === 'action') return {t: p.doneAt ?? p.start, w: words(p.label)};
  if (p.type === 'chips') { const L = (p.items || []).map((x) => (Array.isArray(x) ? x : [x.text, x.at])); const z = L[L.length - 1] || ['', p.start];
    return {t: z[1] ?? p.start, w: words(z[0])}; }
  if (p.type === 'scene') return {t: Math.max(p.start, ...(p.icons || []).map((x) => (Array.isArray(x) ? x[1] : x.at) ?? p.start)), w: 0};
  return {t: p.start, w: words(p.text || p.label)};   // pow / listItem / kinetic: hiện một lần lúc start
};

export const holdEnds = (list, limit, HS) => {
  const K = (HS && HS.canh_minh_hoa) || {};
  const giu = K.giu_sau_s ?? 1.2, moi = K.giu_moi_chu_s ?? 0.3, vao = K.hien_vao_s ?? 0.5, ra = K.mo_ra_s ?? 0.3, mx = K.dai_max_s ?? Infinity;   // không trần cứng (2026-11-07)
  const starts = list.filter((o) => HOLD.has(o.type)).map((o) => o.start).sort((a, b) => a - b);
  return list.map((o) => {
    if (!HOLD.has(o.type) || o.keepEnd) return o;
    const {t, w} = lastOf(o);
    const need = t + vao + giu + ra + Math.max(0, w - 3) * moi;
    if (need <= o.end) return o;
    const next = starts.find((s) => s > o.start + 0.01);
    const cap = Math.min(o.start + mx, next != null ? next - 0.1 : Infinity, limit ?? Infinity);
    const end = Math.max(o.end, Math.min(need, cap));
    if (need - end > 0.15 && typeof console !== 'undefined')   // bị trần chặn → báo để dời start (khối 07)
      console.warn(`[giu] ${o.id || o.type} @${o.start}: thiếu ${(need - end).toFixed(1)} s giữ — dời start muộn hơn (phần tử cuối hiện ở giây ${(t - o.start).toFixed(1)} của cảnh)`);
    return end > o.end ? {...o, end, held: +(end - o.end).toFixed(2)} : o;
  });
};
