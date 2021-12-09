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

d = len(client.simListSceneObjects(name_regex = 'Drone.*'))
print("Number of drones: ", d)
client.enableApiControl(True, "Lead")
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.enableApiControl(True, "Drone3")
client.enableApiControl(True, "Drone4")
client.enableApiControl(True, "Drone5")
client.enableApiControl(True, "Drone6")
client.armDisarm(True, "Lead")
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")
client.armDisarm(True, "Drone3")
client.armDisarm(True, "Drone4")
client.armDisarm(True, "Drone5")
client.armDisarm(True, "Drone6")

airsim.wait_key('Press any key to takeoff')
f1 = client.takeoffAsync(vehicle_name="Lead")
f2 = client.takeoffAsync(vehicle_name="Drone1")
f3 = client.takeoffAsync(vehicle_name="Drone2")
f4 = client.takeoffAsync(vehicle_name="Drone3")
f5 = client.takeoffAsync(vehicle_name="Drone4")
f6 = client.takeoffAsync(vehicle_name="Drone5")
f7 = client.takeoffAsync(vehicle_name="Drone6")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()
f7.join()

f1 = client.moveToZAsync(-50, 5,vehicle_name="Lead")
f2 = client.moveToZAsync(-50, 5,vehicle_name="Drone1")
f3 = client.moveToZAsync(-50, 5,vehicle_name="Drone2")
f4 = client.moveToZAsync(-50, 5,vehicle_name="Drone3")
f5 = client.moveToZAsync(-50, 5,vehicle_name="Drone4")
f6 = client.moveToZAsync(-50, 5,vehicle_name="Drone5")
f7 = client.moveToZAsync(-50, 5,vehicle_name="Drone6")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()
f7.join()

airsim.wait_key('Press any key to begin drone movement')
z = 50
x = 500
y = 500
r = 4


kinematics = client.simGetGroundTruthKinematics(vehicle_name="Lead")
f1 = client.moveToPositionAsync((-4 + kinematics.position.x_val)+r, -4 + kinematics.position.y_val, (kinematics.position.z_val), 3.25, vehicle_name="Drone1")
f2 = client.moveToPositionAsync((4 + kinematics.position.x_val), 4 + kinematics.position.y_val+r, (kinematics.position.z_val), 3.25, vehicle_name="Drone6")
f3 = client.moveToPositionAsync((4 + kinematics.position.x_val)-r, -4 + kinematics.position.y_val, (kinematics.position.z_val), 3.25, vehicle_name="Drone3")
f4 = client.moveToPositionAsync((-4 + kinematics.position.x_val), 4 + kinematics.position.y_val-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone4")
f5 = client.moveToPositionAsync((8 + kinematics.position.x_val), kinematics.position.y_val, (kinematics.position.z_val+r), 3.25, vehicle_name="Drone5")
f6 = client.moveToPositionAsync((-8 + kinematics.position.x_val), kinematics.position.y_val, (kinematics.position.z_val-r), 3.25, vehicle_name="Drone2")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()

time.sleep(10)
numb = 0
client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
while (d == 6):
    kinematics = client.simGetGroundTruthKinematics(vehicle_name="Lead")
    client.moveToPositionAsync((-4 + kinematics.position.x_val)+r, -4 + kinematics.position.y_val, (kinematics.position.z_val), 3.25, vehicle_name="Drone1")
    client.moveToPositionAsync((4 + kinematics.position.x_val), 4 + kinematics.position.y_val+r, (kinematics.position.z_val), 3.25, vehicle_name="Drone6")
    client.moveToPositionAsync((4 + kinematics.position.x_val)-r, -4 + kinematics.position.y_val, (kinematics.position.z_val), 3.25, vehicle_name="Drone3")
    client.moveToPositionAsync((-4 + kinematics.position.x_val), 4 + kinematics.position.y_val-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone4")
    client.moveToPositionAsync((8 + kinematics.position.x_val), kinematics.position.y_val, (kinematics.position.z_val+r), 3.25, vehicle_name="Drone5")
    client.moveToPositionAsync((-8 + kinematics.position.x_val), kinematics.position.y_val, (kinematics.position.z_val-r), 3.25, vehicle_name="Drone2")
    numb+=1
    if (numb==300):
        time.sleep(1)
        client.armDisarm(False, "Drone6")
        client.enableApiControl(False, "Drone6")
    d = 0
    for i in client.simListSceneObjects(name_regex = 'Drone.*'):
        if (client.isApiControlEnabled(i)==True):
            d=d+1
    time.sleep(0.05)




while (d == 5):
    kinematics = client.simGetGroundTruthKinematics(vehicle_name="Lead")
    client.moveToPositionAsync(((-4 + kinematics.position.x_val)+(4)), (-4 + kinematics.position.y_val), (kinematics.position.z_val), 3.75, vehicle_name="Drone1")
    client.moveToPositionAsync(((-8 + kinematics.position.x_val)-(r/2)), (kinematics.position.y_val-(r*(math.sqrt(3)/2))), (kinematics.position.z_val), 3.75, vehicle_name="Drone2")
    client.moveToPositionAsync(((4 + kinematics.position.x_val)-(r/2)), (-4 + kinematics.position.y_val+(r*(math.sqrt(3)/2))), (kinematics.position.z_val), 3.75, vehicle_name="Drone3")
    client.moveToPositionAsync((-4 + kinematics.position.x_val), (4 + kinematics.position.y_val), ((kinematics.position.z_val)+r), 3.75, vehicle_name="Drone4")
    client.moveToPositionAsync((8 + kinematics.position.x_val), (kinematics.position.y_val), ((kinematics.position.z_val)-r), 3.75, vehicle_name="Drone5")
    time.sleep(0.05)