#!/usr/bin/python3
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(True, True, True) #turn IMU sensors on  

def door_state():
    #global orientation
    state=0
    while True:
        orientation = sense.get_orientation()
        if orientation["roll"] > 355.0  or orientation["roll"] < 5.0 :
            state=0
        else:
            state=1
        print(state)
        time.sleep(.1)

if __name__ == "__main__":
    door_state()
