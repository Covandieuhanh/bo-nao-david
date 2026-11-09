// CẢNH TỰ VẼ CỦA VIDEO NÀY (type 've' · khối 07, David chốt 09/11/2026). AI viết component riêng cho từng video ở thư mục này —
// motion graphic kể chuyện, không bắt buộc theo danh mục kiểu cảnh. Đăng ký mỗi component vào VE; cảnh trong scenes.js:
//   {id, type: 've', start, end, props: {ve: 'TenComponent', ...dữ liệu, chữ trên màn hình đặt ở khoá text/label/lines/quote/title}}
// Giữ cố định: nền + màu chủ đạo (lib/tokens: C, HEAD, BODY), biểu tượng cùng kiểu vẽ (lib/Icons), bộ nhận diện chung.
// Tự do: bố cục, chuyển động, hình kể chuyện, mạch hình xuyên nhiều cảnh (lib/mach.js), chuyển cảnh (lib/chuyen-dong.js).
// Thư mục này là DỮ LIỆU RIÊNG của video: cập nhật khung dựng không ghi đè.
import {MauMach} from './MauMach';
export const VE = {MauMach};
