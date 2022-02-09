import airsim
import math
import time
import SimpleDetection
import AvoidanceAlg

class CollisionDetection:

    def collisionDetection(drone):

        standOff = 10

        while True:
            if (simpleDetection()):
                #intiate avoidance
                rightTurnAvoid(drone)
                print ("Collision Detected")
     
            time.sleep(0.1)

        # while True:
            # distanceArray = simpleDetection()
            # for i in distanceArray:
                # if distanceArray[i] < standOff:
                    # call avoidance algorithm
                    # print("Collision Detected")
                    # break
            # time.sleep(0.1)