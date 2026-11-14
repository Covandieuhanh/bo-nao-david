// Font của phong cách hiện tại. Đổi theo style mẫu: cài gói @fontsource/<tên> (bản có subset vietnamese)
// rồi sửa import + FONT_CHECKS + HEAD/BODY trong chu-de.js.
import '@fontsource/barlow-condensed/vietnamese-700.css';
import '@fontsource/barlow-condensed/vietnamese-800.css';
import '@fontsource/barlow-condensed/700.css';
import '@fontsource/barlow-condensed/800.css';
import '@fontsource/be-vietnam-pro/vietnamese-500.css';
import '@fontsource/be-vietnam-pro/vietnamese-600.css';
import '@fontsource/be-vietnam-pro/vietnamese-700.css';
import '@fontsource/be-vietnam-pro/500.css';
import '@fontsource/be-vietnam-pro/600.css';
import '@fontsource/be-vietnam-pro/700.css';
import './thu-vien/phong-chu-nhan.css';   // font phụ: một từ nhấn (bien-thiet-ke.js NHAN) — file font nằm trong thư viện hình, không cần cài gói

export const FONT_CHECKS = [
  '800 100px "Barlow Condensed"', '700 100px "Barlow Condensed"',
  '500 40px "Be Vietnam Pro"', '600 40px "Be Vietnam Pro"', '700 40px "Be Vietnam Pro"', 'italic 700 40px "Playfair Display"',
];
