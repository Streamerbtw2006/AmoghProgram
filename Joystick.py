#!/usr/bin/env/ python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button
import time
import logging

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(levelname)5s: %(message)s')
log = logging.getLogger(__name__)

tp = MoveTank(OUTPUT_A, OUTPUT_D)
butt = Button()


try:
    while not butt.any():  
        time.sleep(0.5)
        press = input("w to go forward, s to go backward, a to go right, d to go left, x to stop, t to end program")
        if press == "w":
            tp.on(left_speed = 50, right_speed = 50)
            print("going forward") 

        elif press == "s":
            tp.on(left_speed = -50, right_speed = -50)
            print("going backward") 
            
        elif press == "a":
            tp.on(left_speed = -50, right_speed = 50)
            print("going right") 

        elif press == "d":
            tp.on(left_speed = 50, right_speed = -50)
            print("going right")     

        elif press == "x":
            tp.on(left_speed = 0, right_speed = 0)
            print("stopping")
        
        elif press == "t":
            break

    tp.on(left_speed = 0, right_speed = 0)

except(KeyboardInterrupt):
    print('interrupt')
    tp.on(left_speed = 0, right_speed = 0)
        
