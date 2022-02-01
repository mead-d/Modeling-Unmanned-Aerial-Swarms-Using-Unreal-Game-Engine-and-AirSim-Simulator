# Purpose:Get Lidar information from drones

# Created by John Mueller

import setup_path 
import airsim

import sys
import math
import time
import argparse
import pprint
import numpy


client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")


airsim.wait_key('Press any key to takeoff')
f1 = client.takeoffAsync(vehicle_name="Drone1")
f2 = client.takeoffAsync(vehicle_name="Drone2")
f1.join()
f2.join()

f1 = client.moveToZAsync(-10, 5,vehicle_name="Drone1")
f2 = client.moveToZAsync(-9, 5,vehicle_name="Drone2")
f1.join()
f2.join()

state1 = client.getMultirotorState(vehicle_name="Drone1")
s = pprint.pformat(state1)
print("state: %s" % s)
state2 = client.getMultirotorState(vehicle_name="Drone2")
s = pprint.pformat(state2)
print("state: %s" % s)

airsim.wait_key('Press any key to get Lidar readings')
        
for i in range(1,5):
            lidarData = client.getLidarData();
            if (len(lidarData.point_cloud) < 3):
                print("\tNo points received from Lidar data")
            else:
                points = parse_lidarData(lidarData)
                print("\tReading %d: time_stamp: %d number_of_points: %d" % (i, lidarData.time_stamp, len(points)))
                print("\t\tlidar position: %s" % (pprint.pformat(lidarData.pose.position)))
                print("\t\tlidar orientation: %s" % (pprint.pformat(lidarData.pose.orientation)))
            time.sleep(5)

client.armDisarm(False, "Drone1")
client.armDisarm(False, "Drone2")
client.enableApiControl(False, "Drone1")
client.enableApiControl(False, "Drone2")
