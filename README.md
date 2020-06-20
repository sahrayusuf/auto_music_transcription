# auto_music_transcription: Using recurrent neural networks, long short-term memory, and borrowed digital signal processing techniques to transcribe musical audio.

### Based on work by Jonathan Sleep at CalPoly

## Abstract / Intro
There has been a multitude of recent research on using deep learning for music & audio generation and classification. In this paper, we plan to build on these works by implementing a novel system to automatically transcribe polyphonic music with an artificial neural network model. We show that by treating the transcription problem as an image classification problem we can use transformed audio data to predict the group of notes currently being played.

## Concepts explored:
Digital Signal Processing: Fast Fourier Transform, Constant-Q Transform, Beat Tracking
Machine Learning: CNNs versus RNNs

## Related work
https://magenta.tensorflow.org/

## Technique
* Pre-process audio using FFT and constant-Q transform to convert to midi files.
* Design a deep learning model to recognize and separate instruments
* Train on several audio samples, increasing in polyphonic complexity
* Evaluate performance

## Things used
* Python, C
* Tensorflow
* librosa - for DSP
* modern-midi for manipulating MIDI

## Data
* http://www.tsi.telecom-paristech.fr/aao/en/2010/07/08/maps-database-a-piano-database-for-multipitch-estimation-and-automatic-transcription-of-music/
