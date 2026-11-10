// THANH THỜI GIAN ở đáy (David chốt 08/11/2026): người xem biết video đang ở phút nào, còn bao lâu.
// Video DỌC NGẮN thì TẮT (David chốt 10/11/2026: nền tảng đã có thanh riêng, "còn 0:20" khiến người xem lướt đi). Ép tay: project.thanh = true|false.
import project from './project.js';
import HL from './highlight.js';
import HS from './hoso.json' with {type: 'json'};   // có `with`: render.mjs (Node 24) nạp được qua endcard.js, webpack cũng nhận
import {POD} from './podframe.js';
const PD = HS.phu_de || {};
export const SHORT = project.short ?? (!!HL || (project.height > project.width && (POD || (project.duration > 0 && project.duration <= (PD.ngan_max_s ?? 90)))));
export const NGAN_DOC = project.height > project.width && SHORT;   // video dọc ngắn: không thanh, không thẻ cuối, màn chốt trên hình
export const TL_ON = project.thanh ?? !NGAN_DOC;
