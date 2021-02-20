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
        "ffmpeg -i " + input_vid + ' -filter:v "setpts=' + str(adj) + '*PTS" output.mp4'
    )


def get_slow_adj(audio_len, vid_len):
    return audio_len / vid_len


adj_amt = get_slow_adj(get_length("french.mp3"), get_length("input.mov"))
print(adj_amt)
slow_video(adj_amt, "input.mov")
print("Done.")
