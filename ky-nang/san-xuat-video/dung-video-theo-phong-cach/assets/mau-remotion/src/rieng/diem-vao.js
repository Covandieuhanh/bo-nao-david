// CẢNH TỰ VẼ CỦA VIDEO NÀY (type 've' · khối 07, David chốt 09/11/2026). AI viết component riêng cho từng video ở thư mục này —
// motion graphic kể chuyện, không bắt buộc theo danh mục kiểu cảnh. Đăng ký mỗi component vào VE; cảnh trong canh.js:
//   {id, type: 've', start, end, props: {ve: 'TenComponent', ...dữ liệu, chữ trên màn hình đặt ở khoá text/label/lines/quote/title}}
// Giữ cố định: chữ ký nhận diện (lib/nhan-dien-chung.md mục 0: bộ nhận diện chung, màu nhấn cam, HEAD/BODY; một từ nhấn dùng NHAN).
// Tự do (David 10/11/2026): nền, kết cấu, kiểu hình, bố cục, chuyển động, hình kể chuyện, mạch hình xuyên nhiều cảnh (lib/mach.js), chuyển cảnh (lib/chuyen-dong.js).
// Thư mục này là DỮ LIỆU RIÊNG của video: cập nhật khung dựng không ghi đè.
import {MauMach} from './mau-mach';
// Mẫu dùng lại được (22/11/2026): nhãn ở chỗ trống thật (tập tham quan, David duyệt 21/11) · đường may vẽ tiếp, không che ai
import {NhanTram} from './nhan-tram';
import {DuongMay} from './duong-may';
// Intro tiêu đề trên cảnh không lời (việc #39, 22/11): dòng nhỏ + tên rơi từng chữ + chữ to đập, quét sáng — chỉ khi David yêu cầu intro
import {IntroTieuDe} from './intro-tieu-de';
// 10 cách học từ Sang Huỳnh + kho aislop (27/11/2026, thiet-ke-bo-cuc/README.md mục 4a): toả nhánh, hội tụ, số vang, soi sáng, gõ lệnh,
// hàng thẻ, hai thẻ, thẻ chào, người trong thẻ, thẻ dọc tối
import {ToaNhanh, HoiTu, SoVang, SoiSang, GoLenh, HangThe, HaiThe, TheChao, NguoiTrongThe, TheDocToi} from './mau-sang-huynh';
export const VE = {MauMach, NhanTram, DuongMay, IntroTieuDe,
  ToaNhanh, HoiTu, SoVang, SoiSang, GoLenh, HangThe, HaiThe, TheChao, NguoiTrongThe, TheDocToi};
