[logo](https://github.com/omurovec/Video-Speech-Translator/blob/master/logo.png)
# About

This idea stemmed from the recent popularity of deep fakes and the goal of this project was to apply this type of technology in a beneficial way rather than the harmful ways it could potenetially be used. This tool allows the user to process a video clip with an audio or text file of an alternate language and lipsync the video to that language.

This could be used in a real life situation where a political figure is delivering a speech and convert that to any native language for a wider reach or even be used to fix poor audio dubbing in movies and TV. Example [here.](https://youtu.be/SpxiFlRgTxg)

If a translated audio source is not available, the user could also provide a `.txt` file of the translated text and specify the language to generate an artifical voice. Although the artificial voice is not ideal, with enough data, the voice could be trained to mimic the original speaker. Example of generated voice [here.](https://youtu.be/BpzdlwWc8GU)

Since this project was limited to 24 hours, I was only able to generate <5sec clips as examples.

# Disclaimer

This tool is for research purposes only, please see the following dependencies for information on licensing:

[Wav2Lip](https://github.com/Rudrabha/Wav2Lip)
[Multilingual_Text_to_Speech](https://github.com/Tomiinek/Multilingual_Text_to_Speech)
[WaveRNN](https://github.com/Tomiinek/WaveRNN)

# Usage

## Dependancies

- Python 3.6
- ffmpeg

## Getting started

_This will take up a fair amount of space on your machine since it automatically downloads multiple pretrained models_

1. Run `python init.py`
2. Download these [weights](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIY27JZg80f7V9jtMfbNDaQ?e=TBFBVW) and place `wav2lip.pth` in `./dependencies/Wav2Lip/checkpoints/`

## Process a Video

_This can take quite a bit of time, with an integrated graphics chip it took me almost an hour to process a 5 second clip_

- To process a clip with a pre-existing audio clip run:
  ```bash
      python process.py --video <video-path> --audio <audio-path>
  ```
- To process a clip with a translated txt file run:
  ```bash
      python process.py --video <video-path> --text <txt-path>
  ```

Results will be saved to the results file
