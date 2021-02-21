import sys
import argparse
import os
import adjuster
from voice_generator import synthesize

if not os.path.exists("./dependencies/"):
    print("You must run init.py before using this tool")
    sys.exit()

parser = argparse.ArgumentParser(
    description="Translate your speech to another language"
)

parser.add_argument("--video", type=str, help="path to mp4")
parser.add_argument("--audio", type=str, help="path to wav/mp3")
parser.add_argument("--text", type=str, help="path to txt")
parser.add_argument("--lang", type=str, help="language (one of de, fr, nl, ru, zh)")

args = parser.parse_args()

video = args.video
audio = args.audio
text = args.text
lang = args.lang

if video is None:
    print("please specify a path to the video file")
    sys.exit()

if not os.path.exists(video):
    print("The specified Video Path does not exist.")
    sys.exit()

if audio is None and text is None:
    print("please specify either a text file or an audio file")
    sys.exit()

if text is None:
    if not os.path.exists(audio):
        print("The specified Audio Path does not exist.")
        sys.exit()

    # Adjust length of video
    adjuster.adj_vid(audio, video)

    # Run Wav2Lip model
    os.system("python ./dependencies/Wav2Lip/inference.py --checkpoint_path ./dependencies/Wav2Lip/checkpoints/wav2lip.pth --face ./temp/adjusted.mp4 --audio " + audio)

    # move to results folder
    os.system("mv -f ./dependencies/Wav2Lip/results/result_voice.mp4 ./results/result.mp4")

else:
    if not os.path.exists(text):
        print("The specified Audio Path does not exist.")
        sys.exit()

    if lang is None:
        print("Must sepicify target language")
        sys.exit()

    # Synthesize voice
    f = open(text, "r")
    text = f.read()
    synthesize(text, lang)

    # Adjust length of video
    adjuster.adj_vid("./temp/result.wav", video)

    # Run Wav2Lip model
    os.system("python ./dependencies/Wav2Lip/inference.py --checkpoint_path ./dependencies/Wav2Lip/checkpoints/wav2lip.pth --face ./temp/adjusted.mp4 --audio ./temp/result.wav")

    # move to results folder
    os.system("mv -f ./dependencies/Wav2Lip/results/result_voice.mp4 ./results/result.mp4")
