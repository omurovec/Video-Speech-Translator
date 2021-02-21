import sys
import os
import subprocess


def get_length(input_video):
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            input_video,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return float(result.stdout)


def slow_video(adj, input_vid):
    os.system(
        "ffmpeg -i "
        + input_vid
        + ' -filter:v "setpts='
        + str(adj)
        + '*PTS" temp/adjusted.mp4'
    )


def get_slow_adj(audio_len, vid_len):
    return audio_len / vid_len


def adj_vid(audio, video):
    adj_amt = get_slow_adj(get_length(audio), get_length(video))
    slow_video(adj_amt, video)
