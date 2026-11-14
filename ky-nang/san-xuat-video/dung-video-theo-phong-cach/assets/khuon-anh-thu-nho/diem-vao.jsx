import React from 'react';
import {Composition, registerRoot} from 'remotion';
import {Thumb} from './anh-thu-nho';

registerRoot(() => <Composition id="anh-thu-nho" component={Thumb} fps={30} width={1280} height={720} durationInFrames={1}
  defaultProps={{bg: 'nen-1.jpg', l1: '', l2: ''}} />);
