import sys
import argparse
import os
import adjuster


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

adjuster.adj_vid(audio, video)
