// THANH THỜI GIAN ở đáy (David chốt 08/11/2026): người xem biết video đang ở phút nào, còn bao lâu.
// Bật: podcast · highlight có thanh tập gốc · MỌI video dài (không phải clip ngắn). Tắt tay: project.thanh = false.
import project from './project.js';
import HL from './highlight.js';
import HS from './hoso.json';
import {POD} from './podframe';
const PD = HS.phu_de || {};
export const SHORT = project.short ?? (!!HL || (project.height > project.width && project.duration > 0 && project.duration <= (PD.ngan_max_s ?? 90)));
export const TL_ON = project.thanh ?? (POD || (HL ? HL.bar !== false : !SHORT));
