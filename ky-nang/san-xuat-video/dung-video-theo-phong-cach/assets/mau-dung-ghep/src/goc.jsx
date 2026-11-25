import React from 'react';
import {Composition} from 'remotion';
import {Show} from './chuong-trinh';
import * as EDL from './danh-sach-cat';
import {FPS, H, TOTAL, W, fr} from './danh-sach-cat';
import {nganDoc} from './thu-vien/nhan-dien-thuong-hieu';

// Thẻ cuối dẫn về bản đầy đủ (ENDCARD trong danh-sach-cat.js) nối thêm sau TOTAL
const END = EDL.ENDCARD && (EDL.THE_CUOI ?? !nganDoc(W, H, TOTAL, EDL.SHORT || EDL.HL)) ? (EDL.ENDCARD.len || 1.8) : 0;

export const Root = () => <Composition id="show" component={Show} fps={FPS} width={W} height={H} durationInFrames={fr(TOTAL + END)} />;
