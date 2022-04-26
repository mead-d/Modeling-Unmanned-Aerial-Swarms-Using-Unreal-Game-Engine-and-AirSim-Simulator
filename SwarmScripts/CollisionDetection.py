from re import X
import airsim
import math
import time
import SimpleDetection
import AvoidanceAlg
import Vector3D

class CollisionDetection:

    # Includes FAA Right-of-Way measures
    #
    #
    def collisionDetection(self, drone_name, wpl, client, drone_pos, lidarName):
        sd = SimpleDetection.simpleDetection()
        AA = AvoidanceAlg.AvoidanceAlg()
        v3D = Vector3D.Vector3D()
        distanceArray= []
        vectorArray = []
        standOff = 20
        collidedDist = 10
        avoid_state = []



#        while True:
        #if (sd.detectObject(client)):
            #intiate avoidance
            #AA.rightTurnAvoid(wpl, drone_name, client)
            #print ("Collision Detected")
        #time.sleep(0.1)

            #if(sd.detectObject(client) == False):
               # break

        # while True:
        lidarArray = sd.execute(client, lidarName, drone_name)
        if (lidarArray is not None):
            for i in lidarArray:
                lidarPt = lidarArray
                distanceArray.append(v3D.calcDistance(lidarPt[0], lidarPt[1], lidarPt[2], drone_pos[0], drone_pos[1], drone_pos[2]))
                # vector components from UAV to obstacle
                vectorArray.append(v3D.vectorize(drone_pos[0], drone_pos[1], drone_pos[2], lidarPt[0], lidarPt[1], lidarPt[2]))
        print(drone_name, " received sensor data.")

        print("DistanceArray: ", distanceArray)
        # Is obstacle distance less than avoidance range?
        for i in distanceArray:
            # vector = vectorArray[0]
            # check if obstacle is within range and converging from the left, with a reduction of 5 degrees to the left.
            # and (v3D.vectorAngle(vectorArray[0], vectorArray[1]) > 95 * math.pi / 180)
            distance = i-200
            if ((distance) <= standOff):
                print(drone_name, "'s obstacle distance: ", distance)
                if ((distance) <= collidedDist):
                    print("-----VEHICLE COLLISION!!!-----")

                print("Possible Collision Detected.")
                AA.rightTurnAvoid(wpl, client, drone_pos, drone_name)

        
        # time.sleep(0.1)