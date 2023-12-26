#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M%S")
rpicam-still -q 100 -r --shutter 1000000--saturation 0.0 -o /home/pi/Pictures/$DATE.jpg --width 3280 --height 2464
