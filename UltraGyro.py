#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button
import logging

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

gs = GyroSensor()
us = UltrasonicSensor()
tp = MoveTank(OUTPUT_A, OUTPUT_D)
button = Button()

try:
    while not button.any():
        while not button.any():
            tp.on(left_speed = 50, right_speed = 50)
            dist = int( us.distance_centimeters_continuous)
            log.info(dist)
            if dist < 60:
                break
        
        tp.on_for_rotations(50, -50, 1.15)


except(KeyboardInterrupt):
    print('interrupt')
    tp.on(left_speed = 0, right_speed = 0)


