// Dùng bởi chup-anh-mau.sh. // sinh canh.js cho khuôn thử danh mục: mỗi kiểu một khe 6 s
const K = [
 ['illus-single', 'illus', {mode: 'single', items: [{icon: 'bulb', at: 0.3}], label: 'Ý TƯỞNG'}],
 ['illus-flow', 'illus', {mode: 'flow', items: [{icon: 'write', at: 0.3, label: 'GHI'}, {icon: 'chart', at: 1, label: 'ĐO'}, {icon: 'target', at: 1.7, label: 'SỬA'}]}],
 ['illus-vs', 'illus', {mode: 'vs', items: [{icon: 'phone', at: 0.3, label: 'LƯỚT', good: false}, {icon: 'book', at: 1, label: 'ĐỌC', good: true}]}],
 ['illus-count', 'illus', {mode: 'count', items: [{icon: 'clock', at: 0.3}], num: {to: 15, at: 0.5, unit: 'PHÚT'}, label: 'MỖI NGÀY'}],
 ['illus-list', 'illus', {mode: 'list', items: [{icon: 'heart', at: 0.3, label: 'SỨC KHOẺ'}, {icon: 'money', at: 0.9, label: 'TIỀN'}, {icon: 'people', at: 1.5, label: 'CON NGƯỜI'}]}],
 ['diagram-tang', 'diagram', {mode: 'tang', items: [{at: 0.3, label: 'LÃNH ĐẠO'}, {at: 0.8, label: 'QUẢN LÝ'}, {at: 1.3, label: 'NHÂN VIÊN'}]}],
 ['diagram-xay-tang', 'diagram', {mode: 'xay-tang', items: [{at: 0.3, label: 'BẢN THÂN'}, {at: 1, label: 'CÔNG VIỆC'}, {at: 1.7, label: 'MỐI QUAN HỆ'}]}],
 ['diagram-vong', 'diagram', {mode: 'vong', items: [{at: 0.3, label: 'BÊN TRONG'}, {at: 0.9, label: 'GIA ĐÌNH'}, {at: 1.5, label: 'XÃ HỘI'}]}],
 ['diagram-moc', 'diagram', {mode: 'moc', items: [{at: 0.3, value: '2016', label: 'BẮT ĐẦU'}, {at: 0.9, value: '2020', label: 'ĐỔI NGHỀ'}, {at: 1.5, value: '2026', label: 'TRAINER'}]}],
 ['diagram-cot', 'diagram', {mode: 'cot', items: [{at: 0.3, value: 10, label: 'THÁNG 1'}, {at: 0.8, value: 40, label: 'THÁNG 3'}, {at: 1.3, value: 120, label: 'THÁNG 6'}]}],
 ['diagram-luoi', 'diagram', {mode: 'luoi', total: 80, items: [{at: 0.3, upto: 30, label: '30 NĂM'}]}],
 ['diagram-tu-thanh', 'diagram', {mode: 'tu-thanh', items: [{at: 0.3, label: 'LÀM GIỎI'}, {at: 1, label: 'DẪN ĐỘI'}]}],
 ['diagram-doi-trang-thai', 'diagram', {mode: 'doi-trang-thai', items: [{at: 0.3, label: 'RỐI', icon: 'chat'}, {at: 1.2, label: 'RÕ'}]}],
 ['diagram-chuyen-giao', 'diagram', {mode: 'chuyen-giao', items: [{at: 0.3, label: 'CHỦ', icon: 'person'}, {at: 0.9, label: 'BÁO CÁO', icon: 'write'}, {at: 1.5, label: 'ĐỘI', icon: 'people'}]}],
 ['diagram-chuoi', 'diagram', {mode: 'chuoi', items: [{at: 0.3, label: 'CÂU LỆNH'}, {at: 0.9, label: 'VIẾT CODE'}, {at: 1.5, label: 'CHỤP KHUNG'}, {at: 2.1, label: 'GHÉP VIDEO'}]}],
 ['bocuc-o-nguoi', 'bocuc', {kieu: 'o-nguoi', noi_dung: {type: 'the', props: {tieu_de: 'Ba việc', dong: [{text: 'nhìn lại tuần', at: 0.4}, {text: 'chia việc', at: 1, to: true}]}}}],
 ['bocuc-o-nguoi-duoi', 'bocuc', {kieu: 'o-nguoi', nguoi_duoi: true, noi_dung: {type: 'diagram', props: {mode: 'chuoi', items: [{at: 0.3, label: 'GHI'}, {at: 0.9, label: 'ĐO'}, {at: 1.5, label: 'SỬA'}]}}}],
 ['bocuc-the-canh', 'bocuc', {kieu: 'the-canh', tieu_de: 'Không cần', dong: [{text: 'biết code', at: 0.4, gach: 1.2}, {text: 'chỉ cần prompt', at: 1.5, to: true}]}],
 ['bocuc-the-canh-so', 'bocuc', {kieu: 'the-canh', so: 1, tieu_de: 'yếu tố', dong: [{text: 'khuôn mặt', at: 0.5, to: true}]}],
 ['bocuc-muc-luc', 'bocuc', {kieu: 'muc-luc', tieu_de: 'Trong video', muc: [{text: 'vì sao cần', at: 0.4}, {text: 'cách làm', at: 1}, {text: 'lỗi hay gặp', at: 1.6}]}],
 ['bocuc-tien-trinh', 'bocuc', {kieu: 'tien-trinh', so: 2, tong: 4, nhan: 'Mẹo', ten: 'ghi việc trước khi ngủ'}],
 ['bocuc-chuong', 'bocuc', {kieu: 'chuong', so: 2, nhan: 'Phần', ten: 'Giải pháp\ncho người bận'}],
 ['bocuc-canh-nguoi', 'bocuc', {kieu: 'canh-nguoi', noi_dung: {type: 'illus', props: {mode: 'flow', items: [{icon: 'write', at: 0.3, label: 'GHI'}, {icon: 'target', at: 1, label: 'LÀM'}]}}}],
 ['bocuc-dung-hay', 'bocuc', {kieu: 'dung-hay', cap: [{nhan: 'Giao việc', at: 0.3, at_hay: 1.2, dung: {text: 'giao miệng rồi quên'}, hay: {photo: 'anh1.jpg'}}, {nhan: 'Theo dõi', at: 4.5, dung: {photo: 'anh2.jpg'}, hay: {text: 'bảng việc'}}]}],
 ['bocuc-tren-duoi', 'bocuc', {kieu: 'tren-duoi', giuPhuDe: true, tren: {photo: 'anh1.jpg', nhan: 'Trước'}, duoi: {photo: 'anh2.jpg', nhan: 'Sau'}}],
 ['bocuc-o-tron', 'bocuc', {kieu: 'o-tron', hinh: {photo: 'anh2.jpg'}}],
 ['bocuc-cau-hoi', 'bocuc', {kieu: 'cau-hoi', nhan: 'Câu hỏi', cau: 'Lý do nào khiến anh chọn khoá học này?', at: 0.3}],
];
const out = K.map(([id, type, props], i) => ({id, type, start: 1 + i * 6, end: 6 + i * 6, props: shift(props, 1 + i * 6)}));
function shift(o, t0) { if (Array.isArray(o)) return o.map((x) => shift(x, t0)); if (o && typeof o === 'object') return Object.fromEntries(Object.entries(o).map(([k, v]) => [k, ['at', 'at_hay', 'gach'].includes(k) && typeof v === 'number' ? +(v + t0).toFixed(2) : shift(v, t0)])); return o; }
const caps = [];
console.log(`import project from './du-an.js';
export const FPS = project.fpsNum / project.fpsDen; export const W = project.width; export const H = project.height;
export const fr = (sec) => Math.round(sec * FPS);
export const SCENES = ${JSON.stringify(out)};
export const COVER = null; export const STAGE = null; export const TOPICS = []; export const CHAPTERS = []; export const GHI_CHU = []; export const GHI_CHU_O = null; export const SIDES = null;
//PHUDE ${JSON.stringify(caps)}`);
