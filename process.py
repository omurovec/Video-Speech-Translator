import sys
import argparse
import os
import adjuster

if not os.path.exists("./dependencies/"):
    print("You must run init.py before using this tool")
    sys.exit()

parser = argparse.ArgumentParser(
    description="Translate your speech to another language"
)

parser.add_argument("Video", metavar="video_path", type=str, help="path to mp4")
parser.add_argument("Audio", metavar="audio_path", type=str, help="path to wav/mp3")

args = parser.parse_args()

video = args.Video
audio = args.Audio

if not os.path.exists(video):
    print("The specified Video Path does not exist.")
    sys.exit()

if not os.path.exists(audio):
    print("The specified Audio Path does not exist.")
    sys.exit()

# Adjust length of video
adjuster.adj_vid(audio, video)

# Run Wav2Lip model
# os.system("python ./dependencies/Wav2Lip/inference.py --checkpoint_path ./dependencies/Wav2Lip/checkpoints/wav2lip.pth --face ./temp/adjusted.mp4 --audio " + audio)

# move to results folder
os.system("mv -f ./dependencies/Wav2Lip/results/result_voice.mp4 ./results/result.mp4")
