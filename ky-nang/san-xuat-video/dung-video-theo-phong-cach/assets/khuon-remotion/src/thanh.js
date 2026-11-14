// THANH THỜI GIAN ở đáy (David chốt 08/11/2026): người xem biết video đang ở phút nào, còn bao lâu.
// Video DỌC NGẮN thì TẮT (David chốt 10/11/2026: nền tảng đã có thanh riêng, "còn 0:20" khiến người xem lướt đi). Ép tay: project.thanh = true|false.
import project from './du-an.js';
import HL from './doan-noi-bat.js';
import HS from './ho-so.json' with {type: 'json'};   // có `with`: xuat-video.mjs (Node 24) nạp được qua man-ket.js, webpack cũng nhận
import {POD} from './khung-podcast.js';
const PD = HS.phu_de || {};
export const SHORT = project.short ?? (!!HL || (project.height > project.width && (POD || (project.duration > 0 && project.duration <= (PD.ngan_max_s ?? 90)))));
export const NGAN_DOC = project.height > project.width && SHORT;   // video dọc ngắn: không thanh, không thẻ cuối, màn chốt trên hình
export const TL_ON = project.thanh ?? !NGAN_DOC;
