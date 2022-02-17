import airsim
import math
import time
import SimpleDetection
import AvoidanceAlg

class CollisionDetection:

    def collisionDetection(self,drone,wpl,client):
        sd = SimpleDetection.simpleDetection()
        AA = AvoidanceAlg.AvoidanceAlg()
        standOff = 10

#        while True:
        if (sd.detectObject(client)):
            #intiate avoidance
            AA.rightTurnAvoid(wpl,drone,client)
            print ("Collision Detected")
        #time.sleep(0.1)

            #if(sd.detectObject(client) == False):
               # break
        # while True:
            # distanceArray = simpleDetection()
            # for i in distanceArray:
                # if distanceArray[i] < standOff:
                    # call avoidance algorithm
                    # print("Collision Detected")
                    # break
            # time.sleep(0.1)