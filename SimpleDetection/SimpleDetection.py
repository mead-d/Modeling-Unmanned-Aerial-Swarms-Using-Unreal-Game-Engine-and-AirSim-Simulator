# Purpose: Detect Objects Utilizing Lidar

# Created by John Mueller

import setup_path 
import airsim

import sys
import math
import time
import argparse
import pprint
import numpy

class simpleDetection:

#Used for testing
 #def __init__(self):

        # connect to the AirSim simulator
        #self.client = airsim.MultirotorClient()
        #self.client.confirmConnection()
        #self.client.enableApiControl(True)

 def detectObject(self,client):
      
        objectDetected = False 

        #while objectDetected == False:

        lidarData = client.getLidarData()
        if (len(lidarData.point_cloud) >= 3):
            print("\tObject Detected!")
            objectDetected = True
                
        return objectDetected


#Used for testing
 def stop(self):

    airsim.wait_key('Press any key to reset to original state')

    self.client.armDisarm(False)
    self.client.reset()

    self.client.enableApiControl(False)
    print("Done!\n")

# main used for testing
if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
 
    #SD = simpleDetection()
    #try:
    #    SD.execute()
    #finally:
    #    SD.stop()



