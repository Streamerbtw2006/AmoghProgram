#!/usr/bin/env/ python3

from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button
import time
from ev3dev2.sensor.lego import ColorSensor
import logging

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

cs = ColorSensor()
us = UltrasonicSensor()
tp = MoveTank(OUTPUT_A, OUTPUT_D)
button = Button()

try:
    while not button.any():
        
            #white line and turn
        tp.on(left_speed = 50, right_speed = 50)
        time.sleep(1.5)
        while not button.any():
            CS = cs.reflected_light_intensity 
            log.info(CS)
            if CS > 15:
                break
        tp.on_for_rotations(-50, 50, 0.65)
            
            #yellow line and turn
        tp.on(left_speed = 50, right_speed = 50)
        time.sleep(1.5)
        while not button.any():    
            if cs.reflected_light_intensity > 15:
                break
        tp.on_for_rotations(50, -50, 0.65)

            #Cabinet obstruction
        while not button.any():    
            tp.on(left_speed = 50, right_speed = 50)
            dist = int( us.distance_centimeters_continuous)
            log.info(dist)
            if dist < 33:
                break
        tp.on_for_rotations(-50, 50, 0.65)

            #Finish line      
        tp.on(left_speed = 50, right_speed = 50)
        time.sleep(1)
        while not button.any():    
            if cs.reflected_light_intensity > 15:
                break
        
        tp.on(left_speed = 0, right_speed = 0)
        log.info("Done")
        break
    log.info("Complete")


except(KeyboardInterrupt):
    print('interrupt')
    tp.on(left_speed = 0, right_speed = 0)
        

