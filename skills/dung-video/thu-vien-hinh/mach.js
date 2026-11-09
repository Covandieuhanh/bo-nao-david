// MẠCH HÌNH (khối 07 · David chốt 09/11/2026): một hình kể chuyện sống qua nhiều cảnh. Khi người nói quay lại ý cũ, cảnh sau
// VẼ TIẾP lên hình đã có (thêm nét, đổi trạng thái), không vẽ hình mới rời rạc.
// Cách dùng trong một cảnh tự vẽ (type 've', motion/src/rieng/): props.buoc = số bước của mạch mà cảnh này vẽ tới, props.moc_buoc =
// [giây tuyệt đối lúc mỗi bước MỚI của cảnh này bắt đầu]. Bước < bước đầu của cảnh = đã vẽ ở cảnh trước → hiện ngay trạng thái
// xong (chỉ hiện lại nhẹ trong ~0,3 s); bước mới → vẽ dần theo mốc lời.
//   const m = mach(f, fps, start, props)   →   m.p(i) = tiến độ 0..1 của bước i · m.moi(i) = bước i là bước mới của cảnh này
import {interpolate, Easing} from 'remotion';

export const mach = (f, fps, start, {buoc = 1, tu_buoc = 0, moc_buoc = [], dai = 0.9} = {}) => {
  const hienLai = interpolate(f, [0, Math.round(0.3 * fps)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
    easing: Easing.out(Easing.exp)});
  const p = (i) => {
    if (i >= buoc) return 0;                       // chưa tới
    if (i < tu_buoc) return hienLai;               // đã vẽ ở cảnh trước: hiện lại trạng thái xong
    const t = moc_buoc[i - tu_buoc];
    if (t == null) return hienLai;
    const a = Math.round((t - start) * fps);
    return interpolate(f, [a, a + Math.round(dai * fps)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
      easing: Easing.out(Easing.exp)});
  };
  return {p, moi: (i) => i >= tu_buoc && i < buoc};
};

// Nét vẽ dần cho đường SVG có độ dài L: style={nét(p, L)}
export const net = (p, L) => ({strokeDasharray: L, strokeDashoffset: L * (1 - p)});
