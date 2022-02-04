import airsim
import math
import time

from .simpleDetection import *

class collisionDetection:

    standOff = 10

    while True:
        if (simpleDetection < standOff):
            #intiate avoidence/break iteration
            print ("Collision Detected")
        else:
                #do nothing
                print ("Safe")
     
        time.sleep(1)
