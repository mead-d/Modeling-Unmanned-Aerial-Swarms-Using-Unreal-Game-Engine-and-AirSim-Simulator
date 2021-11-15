# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 03:44:47 2021

@author: elija
"""

import airsim
import pprint
import setup_path 
import sys
import time
import random

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
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

airsim.wait_key('Press any key to begin drone movement')
z = 10
x = random.randrange(-10,10,1)
y = random.randrange(-10,10,1)
f1 = client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Drone1")
f1.join()
time.sleep(5)
state1 = client.getMultirotorState(vehicle_name="Drone1")
x1 = state1.kinematics_estimated.position.x_val
y1 = state1.kinematics_estimated.position.y_val
f2 = client.moveToPositionAsync((x1+4), y1, (-z +1), 3, vehicle_name="Drone2")
f2.join()
time.sleep(5)

x = random.randrange(-10,10,1)
y = random.randrange(-10,10,1)
f1 = client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Drone1")
f1.join()
time.sleep(5)
state1 = client.getMultirotorState(vehicle_name="Drone1")
x1 = state1.kinematics_estimated.position.x_val
y1 = state1.kinematics_estimated.position.y_val
f2 = client.moveToPositionAsync((x1+4), y1, (-z +1), 3, vehicle_name="Drone2")
f2.join()
time.sleep(5)

x = random.randrange(-10,10,1)
y = random.randrange(-10,10,1)
f1 = client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Drone1")
f1.join()
time.sleep(5)
state1 = client.getMultirotorState(vehicle_name="Drone1")
x1 = state1.kinematics_estimated.position.x_val
y1 = state1.kinematics_estimated.position.y_val
f2 = client.moveToPositionAsync((x1+4), y1, (-z +1), 3, vehicle_name="Drone2")
f2.join()
time.sleep(5)

x = random.randrange(-10,10,1)
y = random.randrange(-10,10,1)
f1 = client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Drone1")
f1.join()
time.sleep(5)
state1 = client.getMultirotorState(vehicle_name="Drone1")
x1 = state1.kinematics_estimated.position.x_val
y1 = state1.kinematics_estimated.position.y_val
f2 = client.moveToPositionAsync((x1+4), y1, (-z +1), 3, vehicle_name="Drone2")
f2.join()
time.sleep(5)


airsim.wait_key('Press any key to reset to original state')
f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
f1.join()
f2.join()

f1 = client.landAsync(vehicle_name="Drone1")
f2 = client.landAsync(vehicle_name="Drone2")
f1.join()
f2.join()

client.armDisarm(False, "Drone1")
client.armDisarm(False, "Drone2")
client.enableApiControl(False, "Drone1")
client.enableApiControl(False, "Drone2")