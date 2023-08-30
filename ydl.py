#!/usr/bin/python3

#
# yt-dlp with time specification using ffmpeg
# requires yt-dlp, ffmpeg
#
# Example: python3 ydl.py ytLink 96 125
#
# 96 is start second, 125 is length of clip in seconds
# cuts out a clip of the video from 1:36 to 3:41
#


# imports
from sys import argv
from os import system as sc

# sec to min
def secToMin(secs):
    min = str(int(secs) // 60).zfill(2)
    sec = str(int(secs) % 60).zfill(2)
    return f'{min}:{sec}'

# download
sc(f'yt-dlp --no-mtime {argv[1]}')

# cut to specified time
if len(argv) == 4:
    sc(f"""
    echo executing ffmpeg... &&
    fileName=$(ls -t | head -n 1 | sed -e 's/\.[^.]*$//') &&
    ffmpeg -hide_banner -loglevel error -ss 0:{secToMin(argv[2])}.00 -i "$(ls -t | head -n 1)" -t 0:{secToMin(argv[3])}.00 -c copy temp.mp4 &&
    rm "$(ls -t | head -n 2 | tail -n 1)" &&
    mv temp.mp4 "$fileName".mp4 &&
    echo Done
    """)

