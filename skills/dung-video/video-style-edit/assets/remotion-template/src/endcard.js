// Có thẻ cuối hay không (Root.jsx + render.mjs cùng đọc): highlight podcast → thẻ dẫn về bản đầy đủ (highlight.js endcard);
// mọi video khác → thẻ cuối NHẬN DIỆN (chủ đề + tên kênh brand.json), cần project.topic hoặc STAGE.title (người dùng chốt 2026-11-04)
import project from './project.js';
import HL from './highlight.js';
import {STAGE} from './scenes.js';
import {NGAN_DOC} from './thanh.js';   // video dọc ngắn: không thẻ cuối (David chốt 10/11/2026) — ép tay project.theCuoi = true

export const ENDCARD_ON = (project.theCuoi ?? !NGAN_DOC) && (HL ? !!(project.podcast && HL.endcard) : !!(project.topic || (STAGE && STAGE.title)));
