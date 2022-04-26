# Written by Dillon Mead
import math
import numpy
#import airsim
import WaypointList
import Vector3D

class AvoidanceAlg:

    # UAV avoids by right turn with set radius.
    # @Param: waypointlist of acting drone, the drone object, obstacle to avoid as array of coordinates, and client object
    # @Return: void
    def rightTurnAvoid(self, wpl, client, drone_pos, drone_name):
        radius = 10 # constraint for vector distance
        new_speed = 5 # drone velocity during avoidance

        # Calculate orthagonal vector. Avoids arithmatic error
        if ((drone_pos[3] == 0) or ((drone_pos[3] < 0.1) and (drone_pos[3] > -0.1))):       # case if x component is zero
            orthagonal_heading = drone_pos[4]              
        elif ((drone_pos[4] == 0) or ((drone_pos[4] < 0.1) and (drone_pos[4] > -0.1))):     # case if y component is zero
            orthagonal_heading = drone_pos[3]
        else:
            orthagonal_heading = -1 * drone_pos[3]/drone_pos[4]

        # find x, y coordinate ahead of drone constrained with designated radius
        intercept_x = 2 * radius * math.cos(math.acos(drone_pos[3]/radius)) + drone_pos[0]
        intercept_y = 2 * radius * math.sin(math.asin(drone_pos[4]/radius)) + drone_pos[1]
        
        # find right turn waypoint with orthagonal vector constrained with designated radius
        orthagonal_x = radius * math.cos(math.atan2(drone_pos[4],drone_pos[3])) + intercept_x
        orthagonal_y = orthagonal_heading * (orthagonal_x - intercept_x) + intercept_y

        #print(drone_name, "'s avoidance information.")
        #print("Original path")
        #print("X: ", drone_pos[0], ", Y: ", drone_pos[1], ", Z: ", drone_pos[2], ", Heading: (", drone_pos[3], ",", drone_pos[4], ")")
        #print("Avoidance path")
        #print("X: ", intercept_x, ", Y: ", intercept_y, ", Z: ", drone_pos[2], ", Heading: (", orthagonal_x, ",", orthagonal_y, ")")

        client.moveToPositionAsync(orthagonal_x, orthagonal_y, drone_pos[2], new_speed, vehicle_name= drone_name).join()
        print(drone_name, " uav avoiding.")

        # insert avoidance WayPoint as first waypoint
        #wpl.insertWayPoint([orthagonal_x, orthagonal_y, drone_pos[2]], new_speed)

        # for return data
        #return [orthagonal_x, orthagonal_y, drone_pos[2], new_speed]