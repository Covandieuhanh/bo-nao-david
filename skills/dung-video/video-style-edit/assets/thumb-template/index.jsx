import React from 'react';
import {Composition, registerRoot} from 'remotion';
import {Thumb} from './Thumb';

registerRoot(() => <Composition id="thumb" component={Thumb} fps={30} width={1280} height={720} durationInFrames={1}
  defaultProps={{bg: 'bg-1.jpg', l1: '', l2: ''}} />);
