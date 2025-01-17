import airsim
import pprint
import setup_path 
import sys
import time
import random
import math
import objectMeasurement as om

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

d = len(client.simListSceneObjects(name_regex = 'Drone.*'))
print("Number of drones: ", d)
#ALL MOVEMENT COORDINATES NEED TO BE ADJUSTED FOR SPAWN LOCATION IN SETTINGS.JSON (spawned at x: -4 position needs to be +4)
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

    f1 = client.moveToZAsync(-10, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-10, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-10, 5,vehicle_name="Drone2")
    f1.join()
    f2.join()
    f3.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 10
    x = 30
    y = 30
    r = 4
    kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
    f1 = client.moveToPositionAsync((kinematics.position.x_val)-r, (kinematics.position.y_val)-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone1")
    f2 = client.moveToPositionAsync((kinematics.position.x_val)+r, (kinematics.position.y_val)+r, (kinematics.position.z_val), 3.25, vehicle_name="Drone2")
    f1.join()
    f2.join()
    time.sleep(2)
    client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
    kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
    while True:
        kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
        client.moveToPositionAsync((kinematics.position.x_val)-4, (kinematics.position.y_val)-r, (kinematics.position.z_val), 3.5, vehicle_name="Drone1")
        client.moveToPositionAsync((kinematics.position.x_val)+4, (kinematics.position.y_val)+r, (kinematics.position.z_val), 3.5, vehicle_name="Drone2")
        if ((abs(abs(kinematics.position.x_val)-abs(x)) < 1) and (abs(abs(kinematics.position.y_val)-abs(y)) < 1)):
            print("hit break")
            break
        

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


if d == 3:
    client.enableApiControl(True, "Lead")
    client.enableApiControl(True, "Drone1")
    client.enableApiControl(True, "Drone2")
    client.enableApiControl(True, "Drone3")
    client.armDisarm(True, "Lead")
    client.armDisarm(True, "Drone1")
    client.armDisarm(True, "Drone2")
    client.armDisarm(True, "Drone3")

    airsim.wait_key('Press any key to takeoff')
    f1 = client.takeoffAsync(vehicle_name="Lead")
    f2 = client.takeoffAsync(vehicle_name="Drone1")
    f3 = client.takeoffAsync(vehicle_name="Drone2")
    f4 = client.takeoffAsync(vehicle_name="Drone3")
    f1.join()
    f2.join()
    f3.join()
    f4.join()

    f1 = client.moveToZAsync(-10, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-10, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-10, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-10, 5,vehicle_name="Drone3")
    f1.join()
    f2.join()
    f3.join()
    f4.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 10
    x = 30
    y = 30
    r = 4

    kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
    f1 = client.moveToPositionAsync(((kinematics.position.x_val)+(4)), (kinematics.position.y_val)-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone1")
    f2 = client.moveToPositionAsync(((kinematics.position.x_val)-(r/2)), (kinematics.position.y_val+(r*(math.sqrt(3)/2)))+r, (kinematics.position.z_val), 3.25, vehicle_name="Drone2")
    f3 = client.moveToPositionAsync(((kinematics.position.x_val)-(r/2))-r, (kinematics.position.y_val-(r*(math.sqrt(3)/2))), (kinematics.position.z_val), 3.25, vehicle_name="Drone3")
    f1.join()
    f2.join()
    f3.join()
    time.sleep(5)
    client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
    kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
    while True:
        kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
        client.moveToPositionAsync(((kinematics.position.x_val)+(4)), (kinematics.position.y_val)-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone1")
        client.moveToPositionAsync(((kinematics.position.x_val)-(r/2)), (kinematics.position.y_val+(r*(math.sqrt(3)/2)))+r, (kinematics.position.z_val), 3.25, vehicle_name="Drone2")
        client.moveToPositionAsync(((kinematics.position.x_val)-(r/2))-r, (kinematics.position.y_val-(r*(math.sqrt(3)/2))), (kinematics.position.z_val), 3.25, vehicle_name="Drone3")
        if ((abs(abs(kinematics.position.x_val)-abs(x)) < 1) and (abs(abs(kinematics.position.y_val)-abs(y)) < 1) and (abs(abs(kinematics.position.z_val)-abs(z)) < 1)):
            print("hit break")
            break
        time.sleep(0.1)

    airsim.wait_key('Press any key to reset to original state')

    f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone3")
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    f1 = client.landAsync(vehicle_name="Lead")
    f2 = client.landAsync(vehicle_name="Drone1")
    f3 = client.landAsync(vehicle_name="Drone2")
    f4 = client.landAsync(vehicle_name="Drone3")
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    client.armDisarm(False, "Lead")
    client.armDisarm(False, "Drone1")
    client.armDisarm(False, "Drone2")
    client.armDisarm(False, "Drone3")
    client.enableApiControl(False, "Lead")
    client.enableApiControl(False, "Drone1")
    client.enableApiControl(False, "Drone2")
    client.enableApiControl(False, "Drone3")


if d == 4:
    client.enableApiControl(True, "Lead")
    client.enableApiControl(True, "Drone1")
    client.enableApiControl(True, "Drone2")
    client.enableApiControl(True, "Drone3")
    client.enableApiControl(True, "Drone4")
    client.armDisarm(True, "Lead")
    client.armDisarm(True, "Drone1")
    client.armDisarm(True, "Drone2")
    client.armDisarm(True, "Drone3")
    client.armDisarm(True, "Drone4")

    airsim.wait_key('Press any key to takeoff')
    f1 = client.takeoffAsync(vehicle_name="Lead")
    f2 = client.takeoffAsync(vehicle_name="Drone1")
    f3 = client.takeoffAsync(vehicle_name="Drone2")
    f4 = client.takeoffAsync(vehicle_name="Drone3")
    f5 = client.takeoffAsync(vehicle_name="Drone4")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()

    f1 = client.moveToZAsync(-50, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-50, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-50, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-50, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-50, 5,vehicle_name="Drone4")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 50
    x = 50
    y = 50
    r = 4
    a = math.sin((109.5*math.pi/180))*math.sin(math.pi/6)
    b = math.sin((109.5*math.pi/180))*math.cos(math.pi/6)
    c = math.cos((109.5*math.pi/180))

    kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
    f1 = client.moveToPositionAsync((kinematics.position.x_val), (kinematics.position.y_val)-r, ((kinematics.position.z_val)-r), 3.25, vehicle_name="Drone1")
    f2 = client.moveToPositionAsync(((kinematics.position.x_val)-(r*a)), ((kinematics.position.y_val-(r*b)))+r, (kinematics.position.z_val - (r*c)), 3.25, vehicle_name="Drone2")
    f3 = client.moveToPositionAsync(((kinematics.position.x_val)-(r*c))-r, ((kinematics.position.y_val)), (kinematics.position.z_val - (r*c)), 3.25, vehicle_name="Drone3")
    f4 = client.moveToPositionAsync(((kinematics.position.x_val)-(r*a))+r, (kinematics.position.y_val+(r*b)), (kinematics.position.z_val - (r*c)), 3.25, vehicle_name="Drone4")

    f1.join()
    f2.join()
    f3.join()
    f4.join()

    time.sleep(10)

    client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
    kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
    while True:
        kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
        client.moveToPositionAsync((kinematics.position.x_val), (kinematics.position.y_val)-r, ((kinematics.position.z_val)-r), 3.25, vehicle_name="Drone1")
        client.moveToPositionAsync(((kinematics.position.x_val)-(r*a)), ((kinematics.position.y_val-(r*b)))+r, (kinematics.position.z_val - (r*c)), 3.25, vehicle_name="Drone2")
        client.moveToPositionAsync(((kinematics.position.x_val)-(r*c))-r, ((kinematics.position.y_val)), (kinematics.position.z_val - (r*c)), 3.25, vehicle_name="Drone3")
        client.moveToPositionAsync(((kinematics.position.x_val)-(r*a))+r, (kinematics.position.y_val+(r*b)), (kinematics.position.z_val - (r*c)), 3.25, vehicle_name="Drone4")
        if ((abs(abs(kinematics.position.x_val)-abs(x)) < 1) and (abs(abs(kinematics.position.y_val)-abs(y)) < 1)):
            print("hit break")
            break

    airsim.wait_key('Press any key to reset to original state')

    f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone4")
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    f1 = client.landAsync(vehicle_name="Lead")
    f2 = client.landAsync(vehicle_name="Drone1")
    f3 = client.landAsync(vehicle_name="Drone2")
    f4 = client.landAsync(vehicle_name="Drone3")
    f5 = client.landAsync(vehicle_name="Drone4")
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    client.armDisarm(False, "Lead")
    client.armDisarm(False, "Drone1")
    client.armDisarm(False, "Drone2")
    client.armDisarm(False, "Drone3")
    client.armDisarm(False, "Drone4")
    client.enableApiControl(False, "Lead")
    client.enableApiControl(False, "Drone1")
    client.enableApiControl(False, "Drone2")
    client.enableApiControl(False, "Drone3")
    client.enableApiControl(False, "Drone4")
if d == 5:
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

    airsim.wait_key('Press any key to takeoff')
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
    f4 = client.moveToZAsync(-50, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-50, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-50, 5,vehicle_name="Drone5")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 60
    x = 50
    y = 50
    r = 4
    a = math.sin((109.5*math.pi/180))*math.sin(math.pi/6)
    b = math.sin((109.5*math.pi/180))*math.cos(math.pi/6)
    beep = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
    f1 = client.moveToPositionAsync(((beep.position.x_val)+(4)), (beep.position.y_val)-r, (beep.position.z_val), 2.1, vehicle_name="Drone1")
    f2 = client.moveToPositionAsync(((beep.position.x_val)-(r/2)), (beep.position.y_val-(r*(math.sqrt(3)/2)))+r, (beep.position.z_val), 2.1, vehicle_name="Drone2")
    f3 = client.moveToPositionAsync(((beep.position.x_val)-(r/2))-r, (beep.position.y_val+(r*(math.sqrt(3)/2))), (beep.position.z_val), 2.1, vehicle_name="Drone3")
    f4 = client.moveToPositionAsync((beep.position.x_val)+r, (beep.position.y_val), ((beep.position.z_val)+r), 2.1, vehicle_name="Drone4")
    f5 = client.moveToPositionAsync((beep.position.x_val)-r, (beep.position.y_val)-r, ((beep.position.z_val)-r), 2.1, vehicle_name="Drone5")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    time.sleep(5)
    client.moveToPositionAsync(x, y, -z, 2, vehicle_name="Lead")
    kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
    while True:
        kinematics = client.simGetGroundTruthKinematics(vehicle_name="Lead")
        client.moveToPositionAsync(((kinematics.position.x_val)+(4)), (kinematics.position.y_val)-r, (kinematics.position.z_val), 2.1, vehicle_name="Drone1")
        client.moveToPositionAsync(((kinematics.position.x_val)-(r/2)), (kinematics.position.y_val-(r*(math.sqrt(3)/2)))+r, (kinematics.position.z_val), 2.1, vehicle_name="Drone2")
        client.moveToPositionAsync(((kinematics.position.x_val)-(r/2))-r, (kinematics.position.y_val+(r*(math.sqrt(3)/2))), (kinematics.position.z_val), 2.1, vehicle_name="Drone3")
        client.moveToPositionAsync((kinematics.position.x_val)+r, (kinematics.position.y_val), ((kinematics.position.z_val)+r), 2.1, vehicle_name="Drone4")
        client.moveToPositionAsync((kinematics.position.x_val)-r, (kinematics.position.y_val)-r, ((kinematics.position.z_val)-r), 2.1, vehicle_name="Drone5")
        if ((abs(abs(kinematics.position.x_val)-abs(x)) < 3) and (abs(abs(kinematics.position.y_val)-abs(y)) < 3)):
            print("hit break")
            break
        time.sleep(0.1)

    airsim.wait_key('Press any key to reset to original state')

    f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone5")
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    f1 = client.landAsync(vehicle_name="Lead")
    f2 = client.landAsync(vehicle_name="Drone1")
    f3 = client.landAsync(vehicle_name="Drone2")
    f4 = client.landAsync(vehicle_name="Drone3")
    f5 = client.landAsync(vehicle_name="Drone4")
    f6 = client.landAsync(vehicle_name="Drone5")
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    client.armDisarm(False, "Lead")
    client.armDisarm(False, "Drone1")
    client.armDisarm(False, "Drone2")
    client.armDisarm(False, "Drone3")
    client.armDisarm(False, "Drone4")
    client.armDisarm(False, "Drone5")
    client.enableApiControl(False, "Lead")
    client.enableApiControl(False, "Drone1")
    client.enableApiControl(False, "Drone2")
    client.enableApiControl(False, "Drone3")
    client.enableApiControl(False, "Drone4")
    client.enableApiControl(False, "Drone5")


if d == 6:
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
    f2 = client.moveToZAsync(-53, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-47, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-46, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-48, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-54, 5,vehicle_name="Drone5")
    f7 = client.moveToZAsync(-52, 5,vehicle_name="Drone6")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()
    f7.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 50
    x = 50
    y = 50
    r = 4
    a = math.sin((109.5*math.pi/180))*math.sin(math.pi/6)
    b = math.sin((109.5*math.pi/180))*math.cos(math.pi/6)

    kinematics = client.simGetGroundTruthKinematics(vehicle_name="Lead")
    f1 = client.moveToPositionAsync((kinematics.position.x_val)+r, (kinematics.position.y_val)-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone1")
    f2 = client.moveToPositionAsync((kinematics.position.x_val), (kinematics.position.y_val+r)+r, (kinematics.position.z_val), 3.25, vehicle_name="Drone2")
    f3 = client.moveToPositionAsync(((kinematics.position.x_val)-r)-r, (kinematics.position.y_val), (kinematics.position.z_val), 3.25, vehicle_name="Drone3")
    f4 = client.moveToPositionAsync((kinematics.position.x_val)+r, kinematics.position.y_val-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone4")
    f5 = client.moveToPositionAsync((kinematics.position.x_val+r)-r, (kinematics.position.y_val)-r, (kinematics.position.z_val+r), 3.25, vehicle_name="Drone5")
    f6 = client.moveToPositionAsync((kinematics.position.x_val)+r, (kinematics.position.y_val)-r, (kinematics.position.z_val-r), 3.25, vehicle_name="Drone6")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()

    time.sleep(10)
    
    
    client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
    kinematics = client.simGetGroundTruthKinematics(vehicle_name="Lead")
    while True:
        kinematics = client.simGetGroundTruthKinematics(vehicle_name="Lead")
        client.moveToPositionAsync((kinematics.position.x_val)+r, (kinematics.position.y_val)-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone1")
        client.moveToPositionAsync((kinematics.position.x_val), (kinematics.position.y_val+r)+r, (kinematics.position.z_val), 3.25, vehicle_name="Drone2")
        client.moveToPositionAsync(((kinematics.position.x_val)-r)-r, (kinematics.position.y_val), (kinematics.position.z_val), 3.25, vehicle_name="Drone3")
        client.moveToPositionAsync((kinematics.position.x_val)+r, kinematics.position.y_val-r, (kinematics.position.z_val), 3.25, vehicle_name="Drone4")
        client.moveToPositionAsync((kinematics.position.x_val+r)-r, (kinematics.position.y_val)-r, (kinematics.position.z_val+r), 3.25, vehicle_name="Drone5")
        client.moveToPositionAsync((kinematics.position.x_val)+r, (kinematics.position.y_val)-r, (kinematics.position.z_val-r), 3.25, vehicle_name="Drone6")
        if ((abs(abs(kinematics.position.x_val)-abs(x)) < 3) and (abs(abs(kinematics.position.y_val)-abs(y)) < 3)):
            print("hit break")
            break
        time.sleep(0.1)

    airsim.wait_key('Press any key to reset to original state')

    f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone5")
    f7 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone6")
    f7.join()
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    f1 = client.landAsync(vehicle_name="Lead")
    f2 = client.landAsync(vehicle_name="Drone1")
    f3 = client.landAsync(vehicle_name="Drone2")
    f4 = client.landAsync(vehicle_name="Drone3")
    f5 = client.landAsync(vehicle_name="Drone4")
    f6 = client.landAsync(vehicle_name="Drone5")
    f7 = client.landAsync(vehicle_name="Drone6")
    f7.join()
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    client.armDisarm(False, "Lead")
    client.armDisarm(False, "Drone1")
    client.armDisarm(False, "Drone2")
    client.armDisarm(False, "Drone3")
    client.armDisarm(False, "Drone4")
    client.armDisarm(False, "Drone5")
    client.armDisarm(False, "Drone6")
    client.enableApiControl(False, "Lead")
    client.enableApiControl(False, "Drone1")
    client.enableApiControl(False, "Drone2")
    client.enableApiControl(False, "Drone3")
    client.enableApiControl(False, "Drone4")
    client.enableApiControl(False, "Drone5")
    client.enableApiControl(False, "Drone6")


if d == 7:
    client.enableApiControl(True, "Lead")
    client.enableApiControl(True, "Drone1")
    client.enableApiControl(True, "Drone2")
    client.enableApiControl(True, "Drone3")
    client.enableApiControl(True, "Drone4")
    client.enableApiControl(True, "Drone5")
    client.enableApiControl(True, "Drone6")
    client.enableApiControl(True, "Drone7")
    client.armDisarm(True, "Lead")
    client.armDisarm(True, "Drone1")
    client.armDisarm(True, "Drone2")
    client.armDisarm(True, "Drone3")
    client.armDisarm(True, "Drone4")
    client.armDisarm(True, "Drone5")
    client.armDisarm(True, "Drone6")
    client.armDisarm(True, "Drone7")

    airsim.wait_key('Press any key to takeoff')
    f1 = client.takeoffAsync(vehicle_name="Lead")
    f2 = client.takeoffAsync(vehicle_name="Drone1")
    f3 = client.takeoffAsync(vehicle_name="Drone2")
    f4 = client.takeoffAsync(vehicle_name="Drone3")
    f5 = client.takeoffAsync(vehicle_name="Drone4")
    f6 = client.takeoffAsync(vehicle_name="Drone5")
    f7 = client.takeoffAsync(vehicle_name="Drone6")
    f8 = client.takeoffAsync(vehicle_name="Drone7")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()
    f7.join()
    f8.join()

    f1 = client.moveToZAsync(-50, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-50, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-50, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-50, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-50, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-50, 5,vehicle_name="Drone5")
    f7 = client.moveToZAsync(-50, 5,vehicle_name="Drone6")
    f8 = client.moveToZAsync(-50, 5,vehicle_name="Drone7")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()
    f7.join()
    f8.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 50
    x = 50
    y = 50
    r = 4
    h = 0.5237 #h/2 constant
    a = math.sin((109.5*math.pi/180))*math.sin(math.pi/6)
    b = math.sin((109.5*math.pi/180))*math.cos(math.pi/6)
    client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
    kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
    while True:
        kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
        client.moveToPositionAsync((kinematics.x_val)+r, (kinematics.y_val)-r, -(z), 3.25, vehicle_name="Drone1")
        client.moveToPositionAsync((kinematics.x_val)+r*math.cos((72*math.pi/180)), (kinematics.y_val+r*math.sin((72*math.pi/180)))+r, -(z), 3.25, vehicle_name="Drone2")
        client.moveToPositionAsync(((kinematics.x_val)-r*math.cos((36*math.pi/180)))-r, kinematics.y_val+r*math.sin((36*math.pi/180)), -(z), 3.25, vehicle_name="Drone3")
        client.moveToPositionAsync((kinematics.x_val)+r, kinematics.y_val, -(z+r), 3.25, vehicle_name="Drone4")
        client.moveToPositionAsync(((kinematics.x_val)+r*math.cos((72*math.pi/180)))-r, (kinematics.y_val-r*math.sin((72*math.pi/180)))-r, -(z), 3.25, vehicle_name="Drone5")
        client.moveToPositionAsync(((kinematics.x_val)-r*math.cos((36*math.pi/180)))+r, (kinematics.y_val-r*math.sin((36*math.pi/180)))-r, -(z), 3.25, vehicle_name="Drone6")
        client.moveToPositionAsync((kinematics.x_val)-r, (kinematics.y_val)+r, -(z-r), 3.25, vehicle_name="Drone7")
        if ((abs(abs(kinematics.x_val)-abs(x)) < 3) and (abs(abs(kinematics.y_val)-abs(y)) < 3)):
            print("hit break")
            break
        time.sleep(0.1)

    airsim.wait_key('Press any key to reset to original state')

    f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone5")
    f7 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone6")
    f8 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone7")
    f8.join()
    f7.join()
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    f1 = client.landAsync(vehicle_name="Lead")
    f2 = client.landAsync(vehicle_name="Drone1")
    f3 = client.landAsync(vehicle_name="Drone2")
    f4 = client.landAsync(vehicle_name="Drone3")
    f5 = client.landAsync(vehicle_name="Drone4")
    f6 = client.landAsync(vehicle_name="Drone5")
    f7 = client.landAsync(vehicle_name="Drone6")
    f8 = client.landAsync(vehicle_name="Drone7")
    f8.join()
    f7.join()
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    client.armDisarm(False, "Lead")
    client.armDisarm(False, "Drone1")
    client.armDisarm(False, "Drone2")
    client.armDisarm(False, "Drone3")
    client.armDisarm(False, "Drone4")
    client.armDisarm(False, "Drone5")
    client.armDisarm(False, "Drone6")
    client.armDisarm(False, "Drone7")
    client.enableApiControl(False, "Lead")
    client.enableApiControl(False, "Drone1")
    client.enableApiControl(False, "Drone2")
    client.enableApiControl(False, "Drone3")
    client.enableApiControl(False, "Drone4")
    client.enableApiControl(False, "Drone5")
    client.enableApiControl(False, "Drone6")
    client.enableApiControl(False, "Drone7")


if d == 8:
    client.enableApiControl(True, "Lead")
    client.enableApiControl(True, "Drone1")
    client.enableApiControl(True, "Drone2")
    client.enableApiControl(True, "Drone3")
    client.enableApiControl(True, "Drone4")
    client.enableApiControl(True, "Drone5")
    client.enableApiControl(True, "Drone6")
    client.enableApiControl(True, "Drone7")
    client.enableApiControl(True, "Drone8")
    client.armDisarm(True, "Lead")
    client.armDisarm(True, "Drone1")
    client.armDisarm(True, "Drone2")
    client.armDisarm(True, "Drone3")
    client.armDisarm(True, "Drone4")
    client.armDisarm(True, "Drone5")
    client.armDisarm(True, "Drone6")
    client.armDisarm(True, "Drone7")
    client.armDisarm(True, "Drone8")

    airsim.wait_key('Press any key to takeoff')
    f1 = client.takeoffAsync(vehicle_name="Lead")
    f2 = client.takeoffAsync(vehicle_name="Drone1")
    f3 = client.takeoffAsync(vehicle_name="Drone2")
    f4 = client.takeoffAsync(vehicle_name="Drone3")
    f5 = client.takeoffAsync(vehicle_name="Drone4")
    f6 = client.takeoffAsync(vehicle_name="Drone5")
    f7 = client.takeoffAsync(vehicle_name="Drone6")
    f8 = client.takeoffAsync(vehicle_name="Drone7")
    f9 = client.takeoffAsync(vehicle_name="Drone8")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()
    f7.join()
    f8.join()
    f9.join()

    f1 = client.moveToZAsync(-50, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-50, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-50, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-50, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-50, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-50, 5,vehicle_name="Drone5")
    f7 = client.moveToZAsync(-50, 5,vehicle_name="Drone6")
    f8 = client.moveToZAsync(-50, 5,vehicle_name="Drone7")
    f9 = client.moveToZAsync(-50, 5,vehicle_name="Drone8")
    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()
    f7.join()
    f8.join()
    f9.join()

    airsim.wait_key('Press any key to begin drone movement')
    z = 50
    x = 50
    y = 50
    r = 4
    h = 0.5237 #h/2 constant
    a = math.sin((109.5*math.pi/180))*math.sin(math.pi/6)
    b = math.sin((109.5*math.pi/180))*math.cos(math.pi/6)
    client.moveToPositionAsync(x, y, -z, 3, vehicle_name="Lead")
    kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
    while True:
        kinematics = client.getMultirotorState(vehicle_name="Lead").kinematics_estimated.position
        client.moveToPositionAsync((kinematics.x_val)+r*a*(math.sqrt(2))/2, kinematics.y_val-r, -(z+r*h), 3.25, vehicle_name="Drone1")
        client.moveToPositionAsync((kinematics.x_val), (kinematics.y_val+r*a*(math.sqrt(2))/2)+r, -(z+r*h), 3.25, vehicle_name="Drone2")
        client.moveToPositionAsync(((kinematics.x_val)-r*a*(math.sqrt(2))/2)-r, kinematics.y_val, -(z+r*h), 3.25, vehicle_name="Drone3")
        client.moveToPositionAsync((kinematics.x_val)+r, kinematics.y_val-r*a*(math.sqrt(2))/2, -(z+r*h), 3.25, vehicle_name="Drone4")
        client.moveToPositionAsync(((kinematics.x_val)+r*a)-r, (kinematics.y_val+r*a)-r, -(z-r*h), 3.25, vehicle_name="Drone5")
        client.moveToPositionAsync(((kinematics.x_val)-r*a)+r, (kinematics.y_val+r*a)-r, -(z-r*h), 3.25, vehicle_name="Drone6")
        client.moveToPositionAsync(((kinematics.x_val)-r*a)-r, (kinematics.y_val-r*a)+r, -(z-r*h), 3.25, vehicle_name="Drone7")
        client.moveToPositionAsync(((kinematics.x_val)+r*a)+r, (kinematics.y_val-r*a, -(z-r*h))+r, 3.25, vehicle_name="Drone8")
        if ((abs(abs(kinematics.x_val)-abs(x)) < 3) and (abs(abs(kinematics.y_val)-abs(y)) < 3)):
            print("hit break")
            break
        time.sleep(0.1)

    airsim.wait_key('Press any key to reset to original state')

    f1 = client.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f3 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone2")
    f4 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone3")
    f5 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone4")
    f6 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone5")
    f7 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone6")
    f8 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone7")
    f9 = client.moveToZAsync(-0.1, 5,vehicle_name="Drone8")
    f9.join()
    f8.join()
    f7.join()
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    f1 = client.landAsync(vehicle_name="Lead")
    f2 = client.landAsync(vehicle_name="Drone1")
    f3 = client.landAsync(vehicle_name="Drone2")
    f4 = client.landAsync(vehicle_name="Drone3")
    f5 = client.landAsync(vehicle_name="Drone4")
    f6 = client.landAsync(vehicle_name="Drone5")
    f7 = client.landAsync(vehicle_name="Drone6")
    f8 = client.landAsync(vehicle_name="Drone7")
    f9 = client.landAsync(vehicle_name="Drone8")
    f9.join()
    f8.join()
    f7.join()
    f6.join()
    f5.join()
    f4.join()
    f3.join()
    f2.join()
    f1.join()

    client.armDisarm(False, "Lead")
    client.armDisarm(False, "Drone1")
    client.armDisarm(False, "Drone2")
    client.armDisarm(False, "Drone3")
    client.armDisarm(False, "Drone4")
    client.armDisarm(False, "Drone5")
    client.armDisarm(False, "Drone6")
    client.armDisarm(False, "Drone7")
    client.armDisarm(False, "Drone8")
    client.enableApiControl(False, "Lead")
    client.enableApiControl(False, "Drone1")
    client.enableApiControl(False, "Drone2")
    client.enableApiControl(False, "Drone3")
    client.enableApiControl(False, "Drone4")
    client.enableApiControl(False, "Drone5")
    client.enableApiControl(False, "Drone6")
    client.enableApiControl(False, "Drone7")
    client.enableApiControl(False, "Drone8")