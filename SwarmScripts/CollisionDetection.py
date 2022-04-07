from re import X
import airsim
import math
import time
import SimpleDetection
import AvoidanceAlg
import Vector3D

class CollisionDetection:

    def collisionDetection(self,drone,wpl,client):
        sd = SimpleDetection.simpleDetection()
        AA = AvoidanceAlg.AvoidanceAlg()
        v3D = Vector3D.Vector3D()
        distanceArray= []
        vectorArray = []
        standOff = 20

        droneState = client.getMultirotorState(vehicle_name = drone).kinematics_estimated
        velocity = droneState.linear_velocity.to_numpy_array()   
        drone_ypos = droneState.position.y_val
        drone_xpos = droneState.position.x_val
        drone_zpos = droneState.position.z_val


#        while True:
        #if (sd.detectObject(client)):
            #intiate avoidance
            #AA.rightTurnAvoid(wpl, drone, client)
            #print ("Collision Detected")
        #time.sleep(0.1)

            #if(sd.detectObject(client) == False):
               # break

        # while True:
        lidarArray = sd.execute(client)
        if (lidarArray is not None):
            for i in lidarArray:
                lidarPt = lidarArray
                distanceArray.append(v3D.calcDistance(lidarPt[0], lidarPt[1], lidarPt[2], drone_xpos, drone_ypos, drone_zpos))
                # vector components from UAV to obstacle
                objVector = v3D.vectorize(drone_xpos, drone_ypos, drone_zpos, lidarPt[0], lidarPt[1], lidarPt[2])
                objVector = v3D.vectorize(drone_xpos, drone_ypos, drone_zpos, lidarPt[0], lidarPt[1], lidarPt[2])
                vectorArray.append(objVector)

        for i in distanceArray:
            vector = vectorArray[0]
            # check if obstacle is within range and converging from the left, with a reduction of 5 degrees to the left.
            #and (v3D.vectorAngle(vector[0], vector[1]) > 95 * math.pi / 180)
            if ((i-200) < standOff):
                AA.rightTurnAvoid(wpl, [drone_xpos, drone_ypos, drone_zpos, velocity[0], velocity[1]],client,drone)
                print("Possible Collision Detected")
                break
            # time.sleep(0.1)