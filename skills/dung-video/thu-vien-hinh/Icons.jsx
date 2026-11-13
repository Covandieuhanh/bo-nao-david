// Biểu tượng nét có chuyển động — minh hoạ thay ảnh (mặc định: không tải ảnh, xem scene-design.md "Ảnh minh hoạ").
// Mỗi hình vẽ trên lưới 64×64, nét tròn đầu; xuất hiện bằng cách vẽ dần từng nét (stroke-dashoffset), rồi đứng yên.
// Dùng: <Pictogram name="mic" size={420} at={0} /> trong montage (item.icon) và card job (icon). Thêm hình: thêm vào ICONS.
import React from 'react';
import {useCurrentFrame} from 'remotion';
import {C, ease} from './tokens';   // thư viện hình dùng chung

const c = (cx, cy, r) => `M${cx - r} ${cy} a${r} ${r} 0 1 0 ${r * 2} 0 a${r} ${r} 0 1 0 ${-r * 2} 0`;
const rr = (x, y, w, h, r) => `M${x + r} ${y} H${x + w - r} Q${x + w} ${y} ${x + w} ${y + r} V${y + h - r} Q${x + w} ${y + h} ${x + w - r} ${y + h} H${x + r} Q${x} ${y + h} ${x} ${y + h - r} V${y + r} Q${x} ${y} ${x + r} ${y} Z`;

// Mỗi hình = danh sách nét (vẽ lần lượt). Tên tiếng Anh ngắn; đặt tên theo VẬT, không theo nghề, để dùng lại được.
export const ICONS = {
  // nghề / công việc
  sneaker: ['M6 46 L9 30 Q13 26 18 30 L25 36 Q31 40 40 40 L52 41 Q58 42 58 47 V50 H6 Z', 'M6 45 H58', 'M16 32 l4 -3 M21 35 l4 -3 M26 38 l3 -3'],
  tray: ['M8 46 H56', 'M14 46 Q14 26 32 26 Q50 26 50 46', c(32, 22, 2.5), 'M56 46 L60 52'],
  bricks: ['M8 22 H56 V54 H8 Z', 'M8 33 H56 M8 44 H56', 'M24 22 V33 M40 22 V33 M16 33 V44 M32 33 V44 M48 33 V44 M24 44 V54 M40 44 V54', 'M44 6 L56 12 L48 16 Z M50 14 L58 18'],
  welding: ['M8 52 L28 32', 'M28 32 L36 24 L40 28 L32 36 Z', 'M42 20 l6 -7 M43 22 l9 1 M41 19 l1 -10 M44 24 l7 7', 'M14 58 H58'],
  hammer: ['M14 54 L38 30', 'M32 22 L44 34 L52 26 L40 14 Z', 'M48 50 V58 M44 50 H52'],
  mower: ['M12 30 H46 L50 42 H8 Z', c(16, 46, 5), c(42, 46, 5), 'M46 30 L56 10 H60', 'M4 58 l3 -6 l3 6 l3 -6 l3 6 l3 -6 l3 6 l3 -6 l3 6 l3 -6 l3 6 l3 -6 l3 6 l3 -6 l3 6 l3 -6 l3 6 l3 -6 l3 6'],
  golf: ['M24 54 V8', 'M24 8 L48 15 L24 22', 'M12 54 Q24 49 36 54 Q24 59 12 54', c(46, 51, 3)],
  megaphone: ['M10 28 V40 H18 L40 50 V18 L18 28 Z', 'M18 40 L22 52 H28 L25 42', 'M46 26 Q50 34 46 42 M52 21 Q58 34 52 47'],
  guideflag: ['M16 58 V8', 'M16 10 H46 L40 18 L46 26 H16', c(40, 46, 6), 'M40 52 V58 M34 58 H46'],
  mic: [rr(22, 6, 20, 30, 10), 'M14 28 Q14 46 32 46 Q50 46 50 28', 'M32 46 V56 M22 56 H42'],
  tv: ['M8 16 H56 V46 H8 Z', 'M24 54 H40 M32 46 V54', 'M24 6 L32 14 L40 6', 'M14 24 H34 M14 30 H30 M14 36 H26', 'M40 24 H50 V38 H40 Z'],
  briefcase: ['M8 22 H56 V52 H8 Z', 'M24 22 V15 H40 V22', 'M8 34 H56', 'M29 31 H35 V38 H29 Z'],
  laptop: ['M14 14 H50 V40 H14 Z', 'M6 48 H58 L54 40 H10 Z', 'M22 22 H38 M22 28 H32'],
  chart: ['M8 54 H56 M8 54 V10', 'M14 44 L26 32 L36 38 L52 18', 'M44 18 H52 V26'],
  // người / tâm trí
  person: [c(32, 18, 9), 'M14 56 Q14 34 32 34 Q50 34 50 56'],
  people: [c(22, 20, 7), 'M8 52 Q8 34 22 34 Q36 34 36 52', c(44, 22, 6), 'M38 34 Q50 32 56 48'],
  meditate: [c(32, 13, 6), 'M32 21 V36', 'M18 30 L32 26 L46 30', 'M12 48 Q32 36 52 48 Q32 58 12 48'],
  heart: ['M32 54 L12 34 Q4 24 12 16 Q22 8 32 20 Q42 8 52 16 Q60 24 52 34 Z'],
  bulb: ['M24 40 Q14 32 16 22 Q20 8 32 8 Q44 8 48 22 Q50 32 40 40 V46 H24 Z', 'M26 52 H38 M28 58 H36', 'M32 24 V34'],
  target: [c(32, 32, 22), c(32, 32, 13), c(32, 32, 4), 'M32 32 L54 10 M47 10 H54 V17'],
  chat: ['M8 12 H56 V40 H26 L14 50 V40 H8 Z', 'M18 22 H46 M18 30 H38'],
  book: ['M32 16 Q20 10 8 14 V50 Q20 46 32 52 Q44 46 56 50 V14 Q44 10 32 16 Z', 'M32 16 V52'],
  write: [rr(8, 8, 34, 48, 5), 'M15 20 H34 M15 28 H34 M15 36 H26', 'M50 20 L56 26 L38 50 L30 54 L32 46 Z M46 26 L52 32'],   // viết ra giấy
  check: [rr(10, 8, 44, 48, 6), 'M18 22 l4 4 l8 -8 M36 22 H46', 'M18 38 l4 4 l8 -8 M36 38 H46'],
  star: ['M32 6 L39 24 L58 24 L43 36 L49 56 L32 44 L15 56 L21 36 L6 24 L25 24 Z'],
  // vật / nơi chốn
  house: ['M8 30 L32 10 L56 30', 'M14 26 V54 H50 V26', 'M26 54 V40 H38 V54'],
  building: ['M12 56 V18 H34 V56', 'M34 30 H52 V56', 'M6 56 H58', 'M18 26 H22 M26 26 H30 M18 34 H22 M26 34 H30 M18 42 H22 M26 42 H30 M40 38 H46 M40 46 H46'],
  clock: [c(32, 32, 22), 'M32 18 V32 L42 38'],
  calendar: ['M10 14 H54 V54 H10 Z', 'M10 24 H54', 'M22 8 V18 M42 8 V18', 'M18 34 H22 M30 34 H34 M42 34 H46 M18 44 H22 M30 44 H34'],
  money: ['M6 18 H58 V46 H6 Z', c(32, 32, 7), 'M12 24 H16 M48 40 H52'],
  coins: ['M12 20 Q12 14 26 14 Q40 14 40 20 Q40 26 26 26 Q12 26 12 20 Z', 'M12 20 V44 Q12 50 26 50 Q40 50 40 44 V20', 'M12 32 Q12 38 26 38 Q40 38 40 32', 'M40 30 Q54 30 54 36 V52 Q54 58 40 58 Q30 58 28 54'],
  thoi: ['M6 52 L10 42 H30 L34 52 Z', 'M30 52 L34 42 H54 L58 52 Z', 'M18 40 L22 30 H42 L46 40 Z', 'M14 47 H26', 'M38 47 H50', 'M26 35 H38'],   // thỏi kim loại (đồng, nhôm…)
  phone: [rr(18, 6, 28, 52, 5), 'M28 50 H36'],
  car: ['M6 40 V32 L14 20 H44 L54 32 H58 V40 Z', 'M14 20 L18 32 H50', c(18, 42, 5), c(46, 42, 5)],
  globe: [c(32, 32, 24), 'M8 32 H56', 'M32 8 Q18 32 32 56 Q46 32 32 8'],
  pin: ['M32 58 Q14 36 14 24 Q14 8 32 8 Q50 8 50 24 Q50 36 32 58 Z', c(32, 24, 7)],
  mountain: ['M4 52 L22 24 L32 38 L42 20 L60 52 Z', 'M42 20 L47 29 L42 27 L38 31'],
  road: ['M20 58 L28 6 M44 58 L36 6', 'M32 54 V46 M32 38 V32 M32 25 V20 M32 14 V11'],
  stairs: ['M6 56 H18 V44 H30 V32 H42 V20 H54 V8', 'M48 8 H58'],
  chip: ['M18 18 H46 V46 H18 Z', 'M26 26 H38 V38 H26 Z', 'M24 10 V18 M32 10 V18 M40 10 V18 M24 46 V54 M32 46 V54 M40 46 V54 M10 24 H18 M10 32 H18 M10 40 H18 M46 24 H54 M46 32 H54 M46 40 H54'],
  gear: [c(32, 32, 9), c(32, 32, 18), 'M32 6 V14 M32 50 V58 M6 32 H14 M50 32 H58 M14 14 L19 19 M45 45 L50 50 M50 14 L45 19 M19 45 L14 50'],
  leaf: ['M12 52 Q10 14 52 12 Q54 52 12 52 Z', 'M12 52 L40 24'],
  sun: [c(32, 32, 11), 'M32 6 V14 M32 50 V58 M6 32 H14 M50 32 H58 M14 14 L19 19 M45 45 L50 50 M50 14 L45 19 M19 45 L14 50'],
  sweater: ['M22 10 L14 14 L6 30 L14 34 L18 26 V54 H46 V26 L50 34 L58 30 L50 14 L42 10 Q32 18 22 10 Z', 'M18 49 H46', 'M24 10 Q32 16 40 10'],
  fruit: ['M32 20 Q20 10 12 22 Q6 36 16 48 Q24 58 32 52 Q40 58 48 48 Q58 36 52 22 Q44 10 32 20 Z', 'M32 20 Q32 12 36 8', 'M34 12 Q42 6 46 12 Q40 16 34 12 Z'],
  tree: ['M32 34 Q16 36 14 24 Q14 12 26 12 Q30 4 38 8 Q50 8 50 20 Q52 34 32 34 Z', 'M29 34 V46 M35 34 V46', 'M8 46 H56', 'M29 46 L20 56 M31 46 L28 58 M33 46 L36 58 M35 46 L44 56'],
  scooter: [c(14, 46, 7), c(50, 46, 7), 'M14 46 H30 L36 34 H46 L50 46', 'M24 30 H38', 'M46 34 L42 16 H50'],
  bicycle: [c(16, 42, 10), c(48, 42, 10), 'M16 42 L26 24 H42 L48 42 M26 24 L32 42 L42 24 M32 42 H16', 'M22 20 H30', 'M42 24 L40 16 H46'],
  footsteps: ['M20 30 Q13 30 13 21 Q13 11 20 11 Q27 11 27 21 Q27 30 20 30 Z', c(20, 37, 4), 'M44 46 Q37 46 37 37 Q37 27 44 27 Q51 27 51 37 Q51 46 44 46 Z', c(44, 53, 4)],
  coffee: ['M12 24 H44 V40 Q44 52 28 52 Q12 52 12 40 Z', 'M44 28 Q54 28 54 35 Q54 42 44 42', 'M22 8 Q18 12 22 16 Q26 20 22 22 M32 8 Q28 12 32 16 Q36 20 32 22', 'M8 58 H48'],
  backpack: [rr(16, 14, 32, 44, 8), 'M16 28 H48', 'M22 38 H42 V50 H22 Z', 'M26 14 Q26 6 32 6 Q38 6 38 14'],
  moon: ['M44 10 Q24 12 22 32 Q24 52 44 54 Q28 58 18 46 Q8 32 18 18 Q28 6 44 10 Z'],
  // bổ sung 2026-11-04 cho cảnh minh hoạ 2 trạng thái (Illus.jsx)
  brain: ['M30 12 Q20 8 15 16 Q8 18 10 28 Q5 34 11 42 Q12 52 24 52 Q30 56 32 50 V14 Q31 12 30 12 Z', 'M34 12 Q44 8 49 16 Q56 18 54 28 Q59 34 53 42 Q52 52 40 52 Q34 56 32 50', 'M20 26 Q26 26 26 32 M44 26 Q38 26 38 32 M22 40 Q28 38 30 42 M42 40 Q36 38 34 42'],
  water: ['M32 8 Q16 30 16 40 Q16 54 32 56 Q48 54 48 40 Q48 30 32 8 Z', 'M24 42 Q25 48 31 49'],
  plane: ['M8 36 L56 14 L46 50 L32 40 L24 50 L24 38 Z', 'M24 38 L56 14'],
  hourglass: ['M18 8 H46 M18 56 H46', 'M20 8 Q20 26 32 32 Q20 38 20 56 M44 8 Q44 26 32 32 Q44 38 44 56', 'M26 50 Q32 44 38 50'],
  puzzle: ['M12 22 H24 Q22 12 30 12 Q38 12 36 22 H50 V33 Q60 31 60 39 Q60 47 50 45 V56 H12 V44 Q22 46 22 38 Q22 30 12 32 Z'],
  smile: ['M32 8 A24 24 0 1 0 32.01 8 Z', 'M23 26 V27 M41 26 V27', 'M21 38 Q32 48 43 38'],
  sad: ['M32 8 A24 24 0 1 0 32.01 8 Z', 'M23 26 V27 M41 26 V27', 'M21 44 Q32 34 43 44'],
  warning: ['M32 8 L58 54 H6 Z', 'M32 24 V38 M32 46 V47'],
  bed: ['M6 44 V22 M6 36 H58 V50 M58 44 H6', 'M12 36 V30 Q12 26 18 26 H26 Q30 26 30 30 V36', 'M6 50 V54 M58 50 V54'],
  family: ['M18 14 A6 6 0 1 0 18.01 14 Z M46 14 A6 6 0 1 0 46.01 14 Z M32 30 A5 5 0 1 0 32.01 30 Z', 'M8 54 V34 Q8 26 18 26 Q28 26 28 34 V54 M36 54 V34 Q36 26 46 26 Q56 26 56 34 V54', 'M26 54 V44 Q26 38 32 38 Q38 38 38 44 V54'],
  up: ['M8 52 L24 36 L34 44 L56 18', 'M42 18 H56 V32'],
  down: ['M8 14 L24 30 L34 22 L56 48', 'M42 48 H56 V34'],
};

export const ICON_NAMES = Object.keys(ICONS);

// Biểu tượng vẽ dần: mỗi nét bắt đầu sau nét trước 4 khung, vẽ trong 16 khung
export const Icon = ({name, size = 300, at = 0, color = C.accent, stroke = 3.2}) => {
  const f = useCurrentFrame();
  const parts = ICONS[name] || ICONS.star;
  return (
    <svg width={size} height={size} viewBox="0 0 64 64" fill="none" stroke={color} strokeWidth={stroke}
      strokeLinecap="round" strokeLinejoin="round" style={{overflow: 'visible'}}>
      {parts.map((d, i) => {
        const p = ease(f, at + i * 4, at + i * 4 + 16);
        return <path key={i} d={d} pathLength={1} strokeDasharray={1} strokeDashoffset={1 - p} />;
      })}
    </svg>
  );
};

// Ô minh hoạ thay ảnh: nền tối + quầng cam + vòng tròn mảnh + biểu tượng vẽ dần rồi đứng yên
export const Pictogram = ({name, w, h, at = 0}) => {
  const f = useCurrentFrame();
  const s = Math.min(w, h);
  const ring = ease(f, at, at + 24);
  const k = s > 400 ? 0.6 : 0.74;   // ô nhỏ (thẻ) → biểu tượng chiếm nhiều hơn
  return (
    <div style={{position: 'relative', width: w, height: h, background: `radial-gradient(circle at 50% 46%, rgba(255,122,69,0.22), ${C.card} 62%)`}}>
      <svg width={w} height={h} style={{position: 'absolute', inset: 0}}>
        <circle cx={w / 2} cy={h / 2} r={s * 0.42} fill="none" stroke={C.accent} strokeOpacity={0.25} strokeWidth={2}
          strokeDasharray={`${s * 0.06} ${s * 0.05}`} opacity={ring} />
      </svg>
      <div style={{position: 'absolute', left: (w - s * k) / 2, top: (h - s * k) / 2,
        filter: 'drop-shadow(0 0 18px rgba(255,122,69,0.45))'}}>
        <Icon name={name} size={s * k} at={at} stroke={s > 400 ? 2.6 : 3.2} />
      </div>
    </div>
  );
};
