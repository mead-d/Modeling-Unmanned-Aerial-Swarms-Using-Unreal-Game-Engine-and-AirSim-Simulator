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
client.enableApiControl(True, "Drone3")
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")
client.armDisarm(True, "Drone3")
d = len(client.simListSceneObjects(name_regex = 'Drone.*'))
print("Number of drones: ", d)

#Add cases for formations here

#if (d ==2):

airsim.wait_key('Press any key to takeoff')
f1 = client.takeoffAsync(vehicle_name="Lead")
f2 = client.takeoffAsync(vehicle_name="Drone2")
f3 = client.takeoffAsync(vehicle_name="Drone3")
f1.join()
f2.join()
f3.join()

f1 = client.moveToZAsync(-50, 5,vehicle_name="Lead")
f2 = client.moveToZAsync(-50, 5,vehicle_name="Drone2")
f3 = client.moveToZAsync(-50, 5,vehicle_name="Drone3")
f1.join()
f2.join()
f3.join()

airsim.wait_key('Press any key to begin drone movement')
z = 50
#x = random.randrange(-10,10,1)
#y = random.randrange(-10,10,1)
x = 50
y = 50
client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
print("before loop")
while True:
    kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
    client.moveToPositionAsync((kinematics.x_val)+4, kinematics.y_val, -z, 3.5, vehicle_name="Drone2")
    client.moveToPositionAsync((kinematics.x_val)-4, kinematics.y_val, -z, 3.5, vehicle_name="Drone3")
    if ((abs(abs(kinematics.x_val)-abs(x)) < 3) and (abs(abs(kinematics.y_val)-abs(y)) < 3)):
        print("hit break")
        break
    time.sleep(0.1)

print("after loop")
airsim.wait_key('Press any key to reset to original state')


f1 = client.landAsync(vehicle_name="Lead")
f2 = client.landAsync(vehicle_name="Drone2")
f3 = client.landAsync(vehicle_name="Drone3")
f1.join()
f2.join()
f3.join()

client.armDisarm(False, "Lead")
client.armDisarm(False, "Drone2")
client.armDisarm(False, "Drone3")
client.enableApiControl(False, "Lead")
client.enableApiControl(False, "Drone2")
client.enableApiControl(False, "Drone3")