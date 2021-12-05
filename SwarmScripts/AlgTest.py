import airsim
import pprint
import setup_path 
import sys
import time
import random
import math

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Lead")
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.enableApiControl(True, "Drone3")
client.enableApiControl(True, "Drone4")
client.enableApiControl(True, "Drone5")
client.armDisarm(True, "Lead")
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")
client.armDisarm(True, "Drone3")
client.armDisarm(True, "Drone4")
client.armDisarm(True, "Drone5")

f1 = client.takeoffAsync(vehicle_name="Lead")
f2 = client.takeoffAsync(vehicle_name="Drone1")
f3 = client.takeoffAsync(vehicle_name="Drone2")
f4 = client.takeoffAsync(vehicle_name="Drone3")
f5 = client.takeoffAsync(vehicle_name="Drone4")
f6 = client.takeoffAsync(vehicle_name="Drone5")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()

f1 = client.moveToZAsync(-50, 5,vehicle_name="Lead")
f2 = client.moveToZAsync(-50, 5,vehicle_name="Drone1")
f3 = client.moveToZAsync(-50, 5,vehicle_name="Drone2")
f4 = client.moveToZAsync(-40, 5,vehicle_name="Drone3")
f5 = client.moveToZAsync(-50, 5,vehicle_name="Drone4")
f6 = client.moveToZAsync(-50, 5,vehicle_name="Drone5")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()

r = 4
a = math.sin((109.5*math.pi/180))*math.sin(math.pi/6)
b = math.sin((109.5*math.pi/180))*math.cos(math.pi/6)
c = math.sin((109.5*math.pi/180))

airsim.wait_key('Press any key to takeoff')
kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
client.moveToPositionAsync(((kinematics.x_val)+(4)), (kinematics.y_val), (kinematics.z_val), 4, vehicle_name="Drone1")
client.moveToPositionAsync(((kinematics.x_val)-(r/2)), (kinematics.y_val-(r*(math.sqrt(3)/2))), (kinematics.z_val), 4, vehicle_name="Drone2")
client.moveToPositionAsync(((kinematics.x_val)-(r/2)), (kinematics.y_val+(r*(math.sqrt(3)/2))), (kinematics.z_val), 4, vehicle_name="Drone4")
client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val), ((kinematics.z_val)+r), 3.25, vehicle_name="Drone3")
client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val), ((kinematics.z_val)-r), 3.25, vehicle_name="Drone5")