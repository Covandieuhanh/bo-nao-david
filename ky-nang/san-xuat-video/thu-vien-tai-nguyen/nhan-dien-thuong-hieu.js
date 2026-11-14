// BỘ NHẬN DIỆN CHUNG — vị trí cố định của kênh cho MỌI loại video (David chốt 08/11/2026: "các loại có những tiêu chuẩn giống nhau,
// chỉ motion graphics là tuỳ loại, tuỳ cảnh"). Một nguồn: khuôn 1 video, podcast, ghép vlog, highlight đều đọc ở đây.
// Bảng giải thích: nhan-dien-chung.md. Sửa vị trí → sửa ở đây, rồi chụp kiểm cả khung ngang lẫn dọc.
export const khung = (W, H) => {
  const V = H > W;
  const safe = V
    ? {left: 70, right: 180, top: 210, bottom: 1420}                  // dọc 1080×1920: chừa nút + chữ của Reels/TikTok
    : {left: Math.round(W * 0.05), right: Math.round(W * 0.05), top: Math.round(H * 0.05), bottom: Math.round(H * 0.95)};   // ngang: title safe SMPTE 90 % (lề 5 %)
  const brandTop = V ? 228 : safe.top;                                // dấu góc ● DAVID │ chủ đề, góc trên trái
  const tl = V ? {y: 1386, h: 30} : {y: Math.round(H * 0.95) - 30, h: 30}; // thanh thời gian = đáy vùng an toàn (ngang: sát đáy, 92–95 %)
  return {
    V, W, H, safe,
    brand: {left: safe.left, top: brandTop, bottom: brandTop + 64},   // mọi lớp phủ góc trên phải nằm dưới brand.bottom
    tl: {...tl, left: safe.left, right: W - safe.right},
    capBottom: V ? 1374 : tl.y - 14,                                    // đáy phụ đề ngay trên thanh thời gian (= khung-podcast.js PF.capBottom)
  };
};
// VIDEO DỌC NGẮN (Reels / TikTok / Shorts — David chốt 10/11/2026): KHÔNG thanh thời gian, KHÔNG thẻ cuối, màn chốt hiện chữ trên khung hình
// (không thu nhỏ video) để video kết ở chữ cuối và tự lặp. Dọc + (ép ngắn | ≤ 90 s). Video ngang / dọc dài giữ nguyên bộ nhận diện.
export const nganDoc = (W, H, dur, ep) => H > W && (!!ep || (dur > 0 && dur <= 90));
export const mmss = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
