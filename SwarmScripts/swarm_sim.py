# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:09:14 2021

@author: elija
"""
import setup_path
import airsim
import sys
import time
import pprint

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)

imu_data = client.getImuData()
s = pprint.pformat(imu_data)
print("imu_data: %s" % s)

barometer_data = client.getBarometerData()
s = pprint.pformat(barometer_data)
print("barometer_data: %s" % s)

magnetometer_data = client.getMagnetometerData()
s = pprint.pformat(magnetometer_data)
print("magnetometer_data: %s" % s)

gps_data = client.getGpsData()
s = pprint.pformat(gps_data)
print("gps_data: %s" % s)

airsim.wait_key('Press any key to takeoff')
print("Taking off...")
client.armDisarm(True)
client.takeoffAsync().join()
client.moveToZAsync(-10, 5).join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to move vehicle')
client.moveToPositionAsync(-10, 10, -10, 5).join()
client.hoverAsync().join()
time.sleep(5)

client.moveToPositionAsync(-20, 10, -10, 5).join()
client.hoverAsync().join()
time.sleep(5)

client.moveToPositionAsync(-20, 0, -10, 5).join()
client.hoverAsync().join()
time.sleep(5)

client.moveToPositionAsync(-10, 0, -10, 5).join()
client.hoverAsync().join()
time.sleep(5)

client.moveToPositionAsync(-10, 10, -10, 5).join()
client.hoverAsync().join()
time.sleep(5)

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to reset to original state')
client.moveToZAsync(-0.1, 5).join()
client.landAsync().join()
client.armDisarm(False)
# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)