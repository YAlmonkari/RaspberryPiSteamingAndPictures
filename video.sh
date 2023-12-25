#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M%S")
rpicam-vid -f --saturation 0.0 --width 1920 --height 1080 -t 0  --bitrate 600000 -o /home/pi/Pictures/$DATE.h264
ffmpeg -i /home/pi/Pictures/$DATE.h264 -vcodec copy /home/pi/Pictures/$DATE.mp4
rm /home/pi/Pictures/$DATE.h264