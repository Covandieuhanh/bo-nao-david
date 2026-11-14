// Màu nhận diện của chế độ ghép — chuong-trinh.jsx và bieu-tuong.jsx (chép từ remotion-template lúc tạo dự án) cùng đọc ở đây.
// Giữ TRÙNG với remotion-template/src/chu-de.js (C) — cùng một bộ nhận diện cho mọi loại video.
import {Easing, interpolate} from 'remotion';

export {C} from './lib/bien-thiet-ke';   // MỘT NGUỒN thư viện hình (khối 10)
export const ease = (f, a, b, o0 = 0, o1 = 1, e = Easing.out(Easing.cubic)) =>
  interpolate(f, [a, b], [o0, o1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: e});
