# Written by Dillon Mead
import math
import numpy
#import airsim
import WaypointList
import Vector3D

class AvoidanceAlg:

    # UAV avoids by right turn with set radius. Includes FAA Right-of-Way measures
    # @Param: waypointlist of acting drone, the drone object, obstacle to avoid as array of coordinates, and client object
    # @Return: void
    def rightTurnAvoid(self, wpl, drone, client,droneName):
        print("avoiding")
        # vector3D module constructor
        #v3D = Vector3D.Vector3D()

        radius = 10 # constraint for vector distance
        new_speed = 5 # drone velocity during avoidance

        # determine drone position/ heading from AirSim client
        #droneState = client.getMultirotorState(vehicle_name = drone).kinematics_estimated
        #velocity = droneState.linear_velocity.to_numpy_array()   
        #drone_ypos = droneState.position.y_val
        #drone_xpos = droneState.position.x_val
        #drone_zpos = droneState.position.z_val
        
        # vector components from UAV to obstacle
        #objVector = v3D.vectorize(drone_xpos, drone_ypos, drone_zpos, obstacle[0], obstacle[1], obstacle[2])

        # boolean condition if x xor y component is negative
        # negVector = objVector[0] < 0 != objVector[1] < 0

        # check if obstacle is converging from the left, with a bias of 5 degrees to the left.
        #if (objVector[0] < 0 != objVector[1] < 0) and (v3D.vectorAngle(objVector[0], objVector[1]) > 95 * math.pi / 180):
            # don't avoid for convergence from left
            #dummy = 0 # dummy var. python is dumb and won't recognize "do nothing" statement
        #else:
        # Calculate orthagonal vector. Avoids arithmatic error
        if ((drone[3] == 0) or ((drone[3] < 0.1) and (drone[3] > -0.1))):                                    # case if x component is zero
            orthagonal_heading = -1 * drone[4]              
        elif ((drone[4] == 0) or ((drone[4] < 0.1) and (drone[4] > -0.1))):                                  # case if y component is zero
            orthagonal_heading = drone[3]
        else:
            orthagonal_heading = -1 * drone[3]/drone[4]

        # find x, y coordinate ahead of drone constrained with designated radius
        intercept_x = 2 * radius * math.sin(math.asin(drone[3]/radius)) + drone[0]
        intercept_y = 2 * radius * math.cos(math.acos(drone[4]/radius)) + drone[1]
        
        # find right turn waypoint with orthagonal vector constrained with designated radius
        orthagonal_x = radius * math.sin(math.atan(orthagonal_heading)) + intercept_x
        orthagonal_y = orthagonal_heading * (orthagonal_x - intercept_x) + intercept_y

        # insert avoidance WayPoint as first waypoint
        client.moveToPositionAsync(orthagonal_x, orthagonal_y, drone[2], new_speed, vehicle_name = droneName)
        #wpl.insertWayPoint([orthagonal_x, orthagonal_y, drone[2]], new_speed)