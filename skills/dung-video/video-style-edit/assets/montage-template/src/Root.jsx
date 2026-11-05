import React from 'react';
import {Composition} from 'remotion';
import {Show} from './Show';
import * as EDL from './edl';
import {FPS, H, TOTAL, W, fr} from './edl';

// Thẻ cuối dẫn về bản đầy đủ (ENDCARD trong edl.js) nối thêm sau TOTAL
const END = EDL.ENDCARD ? (EDL.ENDCARD.len || 1.8) : 0;

export const Root = () => <Composition id="show" component={Show} fps={FPS} width={W} height={H} durationInFrames={fr(TOTAL + END)} />;
