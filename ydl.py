#!/usr/bin/python3

#
# yt-dlp with time specification using ffmpeg
#

# imports
from sys import argv
from os import system as sc

# time format
def tf(time):
    if len(time) == 1: return f'00:00:0{time}'
    elif len(time) == 2: return f'00:00:{time}'
    elif len(time) == 3: return f'00:0{time[0]}:{time[1:3]}'
    elif len(time) == 4: return f'00:{time[0:2]}:{time[2:4]}'
    elif len(time) == 5: return f'0{time[0]}:{time[1:3]}:{time[3:5]}'
    elif len(time) == 6: return f'{time[0:2]}:{time[2:4]}:{time[4:6]}'

# set time selection
if len(argv) > 2:
    startTime = tf(argv[2])
    endTime = '12:00:00'
    if len(argv) > 3:
        endTime = tf(argv[3])
        print(f"dl from {startTime} to {endTime}")
    else: print(f"dl from {startTime} to end")


# download
sc(f'yt-dlp --no-mtime {argv[1]}')

# cut to specified time
if len(argv) > 2:
    sc(f"""
    echo running ffmpeg... &&
    fileName=$(ls -t | head -n 1 | sed -e 's/\.[^.]*$//') &&
    ffmpeg -hide_banner -loglevel error -i "$(ls -t | head -n 1)" -ss {startTime} -to {endTime} -c copy temp.mp4 &&
    rm "$(ls -t | head -n 2 | tail -n 1)" &&
    mv temp.mp4 "$fileName".mp4 &&
    echo Done
    """)


