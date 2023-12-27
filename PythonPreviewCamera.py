# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:20:44 2023
@author: Yrjö Almonkari
"""
from picamera import PiCamera
import time
date = time.strftime("%Y-%m-%d_%H%M%S")
camera = PiCamera()
camera.iso = 800
#0,6s exposure
camera.shutter_speed = 600000
camera.start_preview()
time.sleep(5)
camera.resolution = (2592, 1944)
camera.capture('/home/pi/Pictures/' + date + '.jpg')
camera.stop_preview()
