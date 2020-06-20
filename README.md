## auto_music_transcription: Using recurrent neural networks, LSTM, and borrowed DSP techniques to transcribe musical audio.

### Based on work by Jonathan Sleep at CalPoly

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
