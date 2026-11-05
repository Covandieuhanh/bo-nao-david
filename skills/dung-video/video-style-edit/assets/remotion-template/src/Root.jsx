import React, {useEffect, useState} from 'react';
import {Composition, continueRender, delayRender} from 'remotion';
import {FONT_CHECKS} from './fonts';
import project from './project.js';
import {COVER, FPS, SCENES, fr} from './scenes';
import {FULL, OUT, PILLAR, Place} from './layout';
import {Card, Hook, Kinetic, ListItem, LowerThird} from './components/Overlays';
import {CardFull} from './components/CardFull';
import {Action, Cta} from './components/Action';
import {Build, Converge, Gens, Master, Montage, Recap} from './components/FullScreen';
import {Sides} from './components/Sides';
import {Stage} from './components/Stage';
import {Cover} from './components/Cover';
import {EndCard} from './components/EndCard';
import HL from './highlight.js';
import {BuildL, GensL, MontageL} from './components/FullScreenLand';
import {LAND, POD} from './podframe';
import {Captions} from './components/Captions';
import CAPTIONS from './captions.js';
import PLACEMENT from './placement.js';
import {ENDCARD_ON} from './endcard.js';
import BRAND from './lib/brand.json';
import {Illus} from './lib/Illus';
import {Diagram} from './lib/Diagram';   // sơ đồ nói thay lời + ảnh khung bo góc (khối 07, 2026-11-05)   // cảnh minh hoạ toàn màn hình — 2 trạng thái (khối 07)
import HS from './hoso.json';
import {holdEnds} from './lib/giu';   // giữ cảnh ≥ 1,2 s sau chữ cuối (khối 07)
const _cta = SCENES.find((s) => s.type === 'cta');
const HELD = Object.fromEntries(holdEnds(SCENES, _cta ? _cta.start : project.duration, HS).map((s) => [s.id, s]));
import {TWO, TWO_KEEP} from './layout';

// Thêm loại cảnh mới: viết component rồi đăng ký ở đây (loại toàn màn hình: thêm cả vào FULL trong layout.js)
const TYPES = {illus: Illus, diagram: Diagram, hook: Hook, lower: LowerThird, kinetic: Kinetic, listItem: ListItem, card: project.podcast ? Card : CardFull,   // thẻ = toàn cảnh (trừ podcast)
  montage: Montage, recap: Recap, converge: Converge, master: Master, gens: Gens, build: Build,
  ...(POD && LAND ? {montage: MontageL, gens: GensL, build: BuildL} : {}),   // podcast ngang: bản thiết kế toàn khung 16:9
  action: Action, cta: Cta,   // màn hành động (toàn cảnh) · màn chốt bình luận cuối video
  sides: Sides, captions: Captions, stage: Stage, cover: Cover, endcard: EndCard};

// Chờ font tải xong rồi mới chụp khung, tránh chữ bị font dự phòng. Props phải là dữ liệu thuần (không truyền hàm/component).
const WithFonts = ({type, id, place, ...props}) => {
  const Comp = TYPES[type];
  const [handle] = useState(() => delayRender('fonts'));
  useEffect(() => {
    Promise.all(FONT_CHECKS.map((f) => document.fonts.load(f, 'Tiếng Việt ĐẾN ĐÂU'))).then(() => continueRender(handle));
  }, [handle]);
  return <Place type={type} id={id} place={place}><Comp {...props} /></Place>;
};

export const Root = () => (
  <>
    {SCENES.map((s) => (
      <Composition key={s.id} id={s.id} component={WithFonts} fps={FPS} width={OUT.W} height={OUT.H}
        durationInFrames={fr(PLACEMENT[s.id]?.full && !s.place ? Math.max(PLACEMENT[s.id].end, HELD[s.id].held ? HELD[s.id].end : 0)
          : TWO && !FULL.has(s.type) && !TWO_KEEP.has(s.type) && !s.place && !HELD[s.id].held ? Math.min(s.end, s.start + (HS.toan_man_max_s || 4)) : HELD[s.id].end) - fr(s.start)}   // toàn màn hình (tự chuyển / 2 trạng thái): tối đa 4 s
        defaultProps={{type: s.type, start: s.start, id: s.id, place: s.place ?? null, ...s.props}} />
    ))}
    {CAPTIONS.length > 0 && (
      <Composition id="phu-de" component={WithFonts} fps={FPS} width={OUT.W} height={OUT.H}
        durationInFrames={fr(project.duration)} defaultProps={{type: 'captions', start: 0}} />
    )}
    {COVER && (   // màn hình bìa 1 s (ghép trước video bởi render_preview.py)
      <Composition id="bia" component={WithFonts} fps={FPS} width={project.width} height={project.height}
        durationInFrames={fr(1.0)} defaultProps={{type: 'cover', start: 0}} />
    )}
    {ENDCARD_ON && (   // thẻ cuối (ghép SAU video bởi render_preview.py): highlight podcast → dẫn về bản đầy đủ; còn lại → thẻ nhận diện
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
