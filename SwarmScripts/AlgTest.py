import airsim
import pprint
import setup_path 
import sys
import time
import random
import math

client = airsim.MultirotorClient()
client.confirmConnection()

# connect to the AirSim simulator
client.enableApiControl(True, "Lead")
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.armDisarm(True, "Lead")
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")

airsim.wait_key('Press any key to takeoff')
f1 = client.takeoffAsync(vehicle_name="Lead")
f2 = client.takeoffAsync(vehicle_name="Drone1")
f3 = client.takeoffAsync(vehicle_name="Drone2")
f1.join()
f2.join()
f3.join()

f1 = client.moveToZAsync(-10, 5,vehicle_name="Lead")
f2 = client.moveToZAsync(-10, 5,vehicle_name="Drone1")
f3 = client.moveToZAsync(-10, 5,vehicle_name="Drone2")
f1.join()
f2.join()
f3.join()

airsim.wait_key('Press any key to begin drone movement')
z = 2.2
x = -40
y = 11
r = 2
kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val)+4, (kinematics.z_val), 3.25, vehicle_name="Drone1")
client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val)-4, (kinematics.z_val), 3.25, vehicle_name="Drone2")
time.sleep(5)
client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position

while True:
    kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
    client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val)+r, (kinematics.z_val), 3.25, vehicle_name="Drone1")
    client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val)-r, (kinematics.z_val), 3.25, vehicle_name="Drone2")
    if ((abs(abs(kinematics.x_val)-abs(x)) < 3) and (abs(abs(kinematics.y_val)-abs(y)) < 3)):
        print("hit break")
        break
time.sleep(5)
kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val)+2, (kinematics.z_val), 3.25, vehicle_name="Drone1")
client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val)-2, (kinematics.z_val), 3.25, vehicle_name="Drone2")
time.sleep(5)
kinematics = client.getMultirotorState(vehicle_name="Drone1").kinematics_estimated.position
kinematics1 = client.getMultirotorState(vehicle_name="Drone2").kinematics_estimated.position
f1 = client.moveToPositionAsync((kinematics.x_val)-1.8, (kinematics.y_val), (kinematics.z_val)+0.2, 1, vehicle_name="Drone1")
f2 = client.moveToPositionAsync((kinematics1.x_val)-1.8, (kinematics1.y_val), (kinematics1.z_val)+0.2, 1, vehicle_name="Drone2")
f1.join()
f2.join()
time.sleep(5)
client.rotateToYawAsync(90,vehicle_name="Drone1")
client.rotateToYawAsync(-90,vehicle_name="Drone1")