# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:20:44 2023
@author: Yrjö Almonkari
"""
from picamera import PiCamera
import time
from fractions import Fraction
date = time.strftime("%Y-%m-%d_%H%M%S")
camera = PiCamera(
    resolution=(2592, 1944),
    framerate=Fraction(1, 6),
    sensor_mode=3)
camera.shutter_speed = 6000000
camera.iso = 800
time.sleep(30)
camera.exposure_mode = 'off'
camera.capture('/home/pi/Pictures/' + date + '.jpg')