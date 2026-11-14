import React, {useEffect, useState} from 'react';
import {Composition, continueRender, delayRender} from 'remotion';
import {FONT_CHECKS} from './phong-chu';
import project from './du-an.js';
import {COVER, FPS, SCENES, fr} from './canh';
import {FULL, OUT, PILLAR, Place} from './bo-cuc';
import {Card, Hook, Kinetic, ListItem, LowerThird} from './components/lop-phu';
import {CardFull} from './components/the-toan-man';
import {Action, Cta} from './components/hanh-dong';
import {Build, Converge, Gens, Master, Montage, Recap} from './components/toan-man-hinh';
import {Sides} from './components/hai-ben';
import {Stage} from './components/san-khau';
import {Cover} from './components/anh-bia';
import {EndCard} from './components/man-ket';
import HL from './doan-noi-bat.js';
import {BuildL, GensL, MontageL} from './components/toan-man-hinh-ngang';
import {LAND, POD} from './khung-podcast';
import {Captions} from './components/phu-de';
import {Nhan} from './components/nhan';
import {BoCuc} from './components/bo-cuc';   // lớp trình bày: người vào ô / thẻ cạnh mặt / màn chương (2026-11-07)   // điểm nhấn trên người (2026-11-07)
import CAPTIONS from './phu-de.js';
import PLACEMENT from './vi-tri.js';
import {ENDCARD_ON} from './man-ket.js';
import BRAND from './lib/brand.json';
import {Illus} from './lib/minh-hoa';
import {VE} from './rieng/diem-vao';
import {PhongCtx} from './lib/phong';   // cảnh tự vẽ riêng của video (type 've', khối 07 — 2026-11-09)
import {Diagram} from './lib/so-do';   // sơ đồ nói thay lời + ảnh khung bo góc (khối 07, 2026-11-05)   // cảnh minh hoạ toàn màn hình — 2 trạng thái (khối 07)
import HS from './hoso.json';
import {holdEnds} from './lib/giu';   // giữ cảnh ≥ 1,2 s sau chữ cuối (khối 07)
const _cta = SCENES.find((s) => s.type === 'cta');
const HELD = Object.fromEntries(holdEnds(SCENES, _cta ? _cta.start : project.duration, HS).map((s) => [s.id, s]));
import {TWO, TWO_KEEP} from './bo-cuc';

// Thêm loại cảnh mới: viết component rồi đăng ký ở đây (loại toàn màn hình: thêm cả vào FULL trong bo-cuc.js)
const TYPES = {illus: Illus, diagram: Diagram, hook: Hook, lower: LowerThird, kinetic: Kinetic, listItem: ListItem, card: project.podcast ? Card : CardFull,   // thẻ = toàn cảnh (trừ podcast)
  montage: Montage, recap: Recap, converge: Converge, master: Master, gens: Gens, build: Build,
  ...(POD && LAND ? {montage: MontageL, gens: GensL, build: BuildL} : {}),   // podcast ngang: bản thiết kế toàn khung 16:9
  ve: ({ve, ...p}) => { const V = VE[ve]; if (!V) throw new Error(`cảnh tự vẽ '${ve}' chưa đăng ký trong rieng/diem-vao.js`); return <V {...p} />; },
  action: Action, cta: Cta, nhan: Nhan, bocuc: BoCuc,   // màn hành động (toàn cảnh) · màn chốt bình luận cuối video
  sides: Sides, captions: Captions, stage: Stage, cover: Cover, endcard: EndCard};

// Chờ font tải xong rồi mới chụp khung, tránh chữ bị font dự phòng. Props phải là dữ liệu thuần (không truyền hàm/component).
const WithFonts = ({type, id, place, ...props}) => {
  const Comp = TYPES[type];
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    Promise.all(FONT_CHECKS.map((f) => document.fonts.load(f, 'Tiếng Việt ĐẾN ĐÂU'))).then(() => continueRender(handle));
  }, [handle]);
  return <PhongCtx.Provider value={{phong: props.phong || null, khungDau: fr(props.start || 0)}}>
    <Place type={type} id={id} place={place}><Comp sceneId={id} {...props} /></Place></PhongCtx.Provider>;
};

export const Root = () => (
  <>
    {SCENES.map((s) => (
      <Composition key={s.id} id={s.id} component={WithFonts} fps={FPS} width={OUT.W} height={OUT.H}
        durationInFrames={fr(PLACEMENT[s.id]?.full && !s.place ? Math.max(PLACEMENT[s.id].end, HELD[s.id].held ? HELD[s.id].end : 0)
          : TWO && !FULL.has(s.type) && !TWO_KEEP.has(s.type) && !s.place && !HELD[s.id].held ? Math.min(s.end, s.start + (HS.toan_man_max_s ?? Infinity)) : HELD[s.id].end) - fr(s.start)}   // toàn màn hình (tự chuyển / 2 trạng thái): tối đa 4 s
        defaultProps={{type: s.type, start: s.start, id: s.id, place: s.place ?? null, ...s.props}} />
    ))}
    {CAPTIONS.length > 0 && (
      <Composition id="phu-de" component={WithFonts} fps={FPS} width={OUT.W} height={OUT.H}
        durationInFrames={fr(project.duration)} defaultProps={{type: 'captions', start: 0}} />
    )}
    {COVER && (   // màn hình bìa 1 s (ghép trước video bởi xem-truoc-ban-dung.py)
      <Composition id="bia" component={WithFonts} fps={FPS} width={project.width} height={project.height}
        durationInFrames={fr(1.0)} defaultProps={{type: 'cover', start: 0}} />
    )}
    {ENDCARD_ON && (   // thẻ cuối (ghép SAU video bởi xem-truoc-ban-dung.py): highlight podcast → dẫn về bản đầy đủ; còn lại → thẻ nhận diện
      <Composition id="the-cuoi" component={WithFonts} fps={FPS} width={project.width} height={project.height}
        durationInFrames={fr((HL && HL.endcard && HL.endcard.len) || (!HL && project.ytEnd > 5 ? BRAND.endcardLen + project.ytEnd : BRAND.endcardLen))} defaultProps={{type: 'endcard', start: 0}} />
    )}
    {project.podcast && (   // podcast: sân khấu nền luôn vẽ theo khung dọc thiết kế (khung ngang thì ghép kiểu pillar như video dọc)
      <Composition id="nen" component={WithFonts} fps={FPS} width={project.width} height={project.height}
        durationInFrames={fr(project.duration)} defaultProps={{type: 'stage', start: 0}} />
    )}
    {PILLAR && (
      <Composition id="hai-ben" component={WithFonts} fps={FPS} width={OUT.W} height={OUT.H}
        durationInFrames={fr(project.duration)} defaultProps={{type: 'sides', start: 0}} />
    )}
  </>
);
