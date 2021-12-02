import airsim
import pprint
import setup_path 
import sys
import time
import random

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

d = len(client.simListSceneObjects(name_regex = 'Drone.*'))
print("Number of drones: ", d)

if d == 2:
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

    f1 = client.moveToZAsync(-50, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-50, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-50, 5,vehicle_name="Drone2")
    f1.join()
    f2.join()
    f3.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 50
    x = 50
    y = 50
    client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
    kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
    while True:
        kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
        client.moveToPositionAsync((kinematics.x_val)+4, kinematics.y_val, -z, 3.25, vehicle_name="Drone1")
        client.moveToPositionAsync((kinematics.x_val)-4, kinematics.y_val, -z, 3.25, vehicle_name="Drone2")
        if ((abs(abs(kinematics.x_val)-abs(x)) < 3) and (abs(abs(kinematics.y_val)-abs(y)) < 3)):
            print("hit break")
            break
        time.sleep(0.1)

    airsim.wait_key('Press any key to reset to original state')

    f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
    f3.join()
    f2.join()
    f1.join()

    f1 = client.landAsync(vehicle_name="Lead")
    f2 = client.landAsync(vehicle_name="Drone1")
    f3 = client.landAsync(vehicle_name="Drone2")
    f3.join()
    f2.join()
    f1.join()

    client.armDisarm(False, "Lead")
    client.armDisarm(False, "Drone1")
    client.armDisarm(False, "Drone2")
    client.enableApiControl(False, "Lead")
    client.enableApiControl(False, "Drone1")
    client.enableApiControl(False, "Drone2")


#if d == 3:
#
#if d == 4:
#
#if d == 5:
#
#if d == 6:
#
#if d == 7:
#
#if d == 8:
#