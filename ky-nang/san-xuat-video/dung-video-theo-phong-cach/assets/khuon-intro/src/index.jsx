import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Intro, TONG } from './Intro';

const Root = () => (
  <>
    <Composition id="IntroNgang" component={Intro} durationInFrames={TONG} fps={30} width={1920} height={1080} />
  </>
);
registerRoot(Root);
