// Hình học khung PODCAST (skill dung-podcast) — dọc 1080×1920 hoặc NGANG 1920×1080 thiết kế toàn khung (không chia cột).
// Component lớp phủ (thẻ, chữ to, hook) vẫn vẽ trên dải dọc 830×435 của theme (SAFE) — Place phóng/đặt dải đó vào `ov`.
// Phụ đề + thanh thời gian vẽ ở lớp trên cùng (phu-de) → cảnh toàn màn hình không che được.
import project from './project.js';

export const POD = !!project.podcast;
export const LAND = project.width > project.height;
export const PF = LAND ? {
  W: 1920, H: 1080, left: 96, right: 1824, top: 54, bottom: 1026,     // vùng an toàn ngang: lề 5% mọi phía (title safe 90%)
  tl: {y: 996, h: 30},                                                 // thanh thời gian = đáy vùng an toàn (= nhan-dien.js)
  capBottom: 982, capSize: 36, capW: 1240,                              // phụ đề ngay trên thanh thời gian
  ov: {scale: 1.08, top: 175},                                         // dải lớp phủ 830×435 → 896×470, canh trái (x 96–992)
  contentBottom: 900,                                                  // cảnh toàn màn hình: nội dung kết thúc trước dải phụ đề
} : {
  W: 1080, H: 1920, left: 70, right: 900, top: 210, bottom: 1420,
  tl: {y: 1386, h: 30},
  capBottom: 1374, capSize: 38, capW: 830,
  ov: {scale: 0.88, top: 480},
  contentBottom: 1240,
};
export const PF_W = PF.right - PF.left;

// Chữ to tiếng Việt (CẢ HAI skill — người dùng chốt 2026-11-02): dấu chồng (Ầ Ễ Ỗ) cao ~0,45 em trên chữ hoa, dấu nặng ~0,22 em dưới chân → giãn dòng + chừa chỗ
// trong khung overflow theo cỡ chữ. Người dùng chốt: không thiếu dấu, dòng trên dòng dưới không chồng nhau.
export const VN = {lh: 1.14, top: 0.5, bot: 0.32, gap: 0.24, above: 0.4};
// gap: khoảng thêm giữa 2 DÒNG chữ to xếp chồng (dấu nặng dòng trên + dấu chồng dòng dưới) — 0,1 làm "MỘT" chạm "RẤT" (người dùng chỉ ra)
// above: chữ to đứng NGAY SAU một dòng/khối khác (chữ nhỏ, vạch màu, "BƯỚC n", khung ảnh) phải chừa phía trên ≥ 0,4 cỡ chữ cho
// dấu chồng (Ố Ễ Ỗ) — đã gặp: "GỐC RỄ" đè lên dòng "Phải nuôi đến cả năm trời" ngay trên nó. Dùng aboveGap(size).
export const aboveGap = (size) => Math.round(size * VN.above);
// Cảnh toàn màn hình podcast: thu cả nội dung (không thu nền) quanh tâm vùng nội dung
export const FULL_SCALE = 0.88;
export const FULL_ORIGIN = LAND ? '960px 420px' : '540px 725px';
