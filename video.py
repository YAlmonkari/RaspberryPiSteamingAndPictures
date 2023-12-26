# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:20:44 2023

@author: Yrjö Almonkari
"""
from picamera import PiCamera
import subprocess
import time
date = time.strftime("%Y-%m-%d_%H%M%S")
camera = PiCamera()
camera.start_preview()
camera.resolution = (1920, 1080)
camera.start_recording('/home/pi/Pictures/' + date + '.h264')
i = input()
camera.stop_recording()
camera.stop_preview()
render = "ffmpeg -i /home/pi/Pictures/" + date + ".h264 -vcodec copy /home/pi/Pictures/" + date + ".mp4"
i = subprocess.call(render, shell=True)
remove = "rm /home/pi/Pictures/" + date + ".h264"
j = subprocess.call(remove, shell=True)