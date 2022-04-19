import airsim
import numpy
import Swarmer
import time
import CollisionDetection
import WaypointList
import SwarmPathing
import Vector3D 
import threading

client1 = airsim.MultirotorClient()
client2 = airsim.MultirotorClient()
client1.confirmConnection()
client2.confirmConnection()
d = len(client1.simListSceneObjects(name_regex= 'Drone.*')) + len(client2.simListSceneObjects(name_regex= 'Drone.*'))

#client = airsim.MultirotorClient()
#client.confirmConnection()
Swarming = Swarmer.Swarmer()
cd = CollisionDetection.CollisionDetection()
wpl1 = WaypointList.WaypointList()
wpl2 = WaypointList.WaypointList()
SwarmPathing = SwarmPathing.SwarmPathing()
v3d = Vector3D.Vector3D()
#d = len(client.simListSceneObjects(name_regex = 'Drone.*'))
print("Number of drones: ", d)
wpl1.addWayPoint([-200,0,-100],4)
wpl2.addWayPoint([200,0,-100],4)


if d == 0:

    client1.enableApiControl(True, "Lead")
    client1.armDisarm(True, "Lead")
    client1.takeoffAsync(vehicle_name="Lead").join()
    client1.moveToZAsync(-50, 10, vehicle_name="Lead").join()

    while True:
        droneState = client1.getMultirotorState(vehicle_name = "Lead").kinematics_estimated
        drone_pos = []
        drone_pos.append(droneState.position.x_val)
        drone_pos.append(droneState.position.y_val)
        drone_pos.append(droneState.position.z_val)
        drone_velocity = droneState.linear_velocity.to_numpy_array()
        drone_pos.append(drone_velocity[0])
        drone_pos.append(drone_velocity[1])

        avoid_state1 = cd.collisionDetection("Lead", wpl1, client1, drone_pos)
        if avoid_state1 is not None:
            client1.moveToPositionAsync(avoid_state1[0], avoid_state1[1], avoid_state1[2], avoid_state1[3], vehicle_name= "Lead")
        SwarmPathing.pathCheck(wpl1, "Lead", drone_pos)
        SwarmPathing.pathTo(wpl1, "Lead", drone_pos)
        time.sleep(0.1)

    

if d == 2:
    client1.enableApiControl(True, "Lead")
    client1.armDisarm(True, "Lead")
    client2.enableApiControl(True, "Drone1")
    client2.armDisarm(True, "Drone1")

    client1.takeoffAsync(vehicle_name="Lead")
    client2.takeoffAsync(vehicle_name="Drone1").join()

    client1.moveToZAsync(-100, 10,vehicle_name="Lead")
    client2.moveToZAsync(-102, 10,vehicle_name="Drone1").join()

    while True:

        droneState2 = client2.getMultirotorState(vehicle_name = "Drone1").kinematics_estimated
        drone_pos2 = []
        drone_pos2.append(droneState2.position.x_val)
        drone_pos2.append(droneState2.position.y_val)
        drone_pos2.append(droneState2.position.z_val)
        drone_velocity2 = droneState2.linear_velocity.to_numpy_array()
        drone_pos2.append(drone_velocity2[0])
        drone_pos2.append(drone_velocity2[1])

        droneState1 = client1.getMultirotorState(vehicle_name = "Lead").kinematics_estimated
        drone_pos1 = []
        drone_pos1.append(droneState1.position.x_val)
        drone_pos1.append(droneState1.position.y_val)
        drone_pos1.append(droneState1.position.z_val)
        drone_velocity1 = droneState1.linear_velocity.to_numpy_array()
        drone_pos1.append(drone_velocity1[0])
        drone_pos1.append(drone_velocity1[1])

        print("Drone1 ", droneState1)
        print("Drone2 ", droneState2)

        th1 = threading.Thread(target = cd.collisionDetection,args = ["Lead", wpl1,client1,drone_pos1,"MyLidar1"])
        th2 = threading.Thread(target = cd.collisionDetection,args = ["Lead", wpl2,client2,drone_pos2,"MyLidar2"])
        th1.start()
        th2.start()

        avoid_state1 = th1.run()
        #avoid_state1 = cd.collisionDetection("Lead", wpl1,client1,drone_pos1,"MyLidar1")
        print("Drone1 ", avoid_state1)

        avoid_state2 = th2.run()
        #avoid_state2 = cd.collisionDetection("Drone1", wpl2, client2,drone_pos2,"MyLidar2")
        print("Drone2 ", avoid_state2)
        

        
        if ((bool(avoid_state1) is not False) and (bool(avoid_state2) is not False)):
            print("Drones 1 and 2 avoiding")
            f1 = client1.moveToPositionAsync(avoid_state1[0], avoid_state1[1], avoid_state1[2], avoid_state1[3], vehicle_name= "Lead")
            f2 = client2.moveToPositionAsync(avoid_state2[0], avoid_state2[1], avoid_state2[2], avoid_state2[3], vehicle_name= "Drone1")
            f1.join()
            f2.join()
        elif bool(avoid_state2) is not False:
            print("Drone 2 avoiding")
            f1 = client2.moveToPositionAsync(avoid_state2[0], avoid_state2[1], avoid_state2[2], avoid_state2[3], vehicle_name= "Drone1")
            f1.join()
        elif bool(avoid_state1) is not False:
            print("Drone 1 avoiding")
            f1 = client1.moveToPositionAsync(avoid_state1[0], avoid_state1[1], avoid_state1[2], avoid_state1[3], vehicle_name= "Lead")
            f1.join()

        time.sleep(1)
        SwarmPathing.pathCheck(wpl1, "Lead", client1)
        SwarmPathing.pathCheck(wpl2, "Drone1", client2)
        SwarmPathing.pathTo(wpl1,"Lead",client1,v3d,drone_pos1)
        SwarmPathing.pathTo(wpl2,"Drone1",client2,v3d,drone_pos2)
        
        th1._stop 
        th2._stop
        


    f1 = client1.moveToZAsync(-0.1, 5,vehicle_name="Lead")
    f2 = client2.moveToZAsync(-0.1, 5,vehicle_name="Drone1")
    f1.join()
    f2.join()
    f1 = client1.landAsync(vehicle_name="Lead")
    f2 = client2.landAsync(vehicle_name="Drone1")
    f1.join()
    f2.join()
    client1.armDisarm(False, "Lead")
    client2.armDisarm(False, "Drone1")
    client1.enableApiControl(False, "Lead")
    client2.enableApiControl(False, "Drone1")





#
#
#
# BELOW CODE DOES NOT HAVE CORRECT CLIENT1/ CLIENT2 REFERENCES!!
#
#
#




if d == 20:
    client.enableApiControl(True, "Lead")
    client.enableApiControl(True, "Drone1")
    client.enableApiControl(True, "Drone2")
    client.armDisarm(True, "Lead")
    client.armDisarm(True, "Drone1")
    client.armDisarm(True, "Drone2")


    Swarming.formSwarm(d)
    
   
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


    Swarming.formSwarm(d)


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


    Swarming.formSwarm(d)


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


    Swarming.formSwarm(d)


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


    Swarming.formSwarm(d)


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


    Swarming.formSwarm(d)


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


    Swarming.formSwarm(d)


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