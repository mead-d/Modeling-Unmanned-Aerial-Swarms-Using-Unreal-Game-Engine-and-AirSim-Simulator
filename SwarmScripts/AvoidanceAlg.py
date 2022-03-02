# Written by Dillon Mead
import math
import numpy
import airsim
import WaypointList
import Vector3D

class AvoidanceAlg:

    # UAV avoids by right turn with set radius. Includes FAA Right-of-Way measures
    # @Param: waypointlist of acting drone, the drone object, obstacle to avoid as array of coordinates, and client object
    # @Return: void
    def rightTurnAvoid(self, wpl, drone, obstacle, client):
    
        # vector3D module constructor
        v3D = Vector3D.Vector3D()

        radius = 5 # constraint for vector distance
        new_speed = 5 # drone velocity during avoidance

        # determine drone position/ heading from AirSim client
        droneState = client.getMultirotorState(vehicle_name = drone).kinematics_estimated
        velocity = droneState.linear_velocity.to_numpy_array()   
        drone_ypos = droneState.position.y_val
        drone_xpos = droneState.position.x_val
        drone_zpos = droneState.position.z_val
        
        # vector components from UAV to obstacle
        objVector = v3D.vectorize(drone_xpos, drone_ypos, drone_zpos, obstacle[0], obstacle[1], obstacle[2])

        # boolean condition if x xor y component is negative
        # negVector = objVector[0] < 0 != objVector[1] < 0

        # check if obstacle is converging from the left, with a bias of 5 degrees to the left.
        if (objVector[0] < 0 != objVector[1] < 0) and (v3D.vectorAngle(objVector[0], objVector[1]) > 95 * math.pi / 180):
            # don't avoid for convergence from left
            dummy = 0 # dummy var. python is dumb and won't recognize "do nothing" statement
        else:
            # Calculate orthagonal vector. Avoids arithmatic error
            if velocity[0] == 0:                                    # case if x component is zero
                orthagonal_heading = -1 * velocity[1]              
            elif velocity[1] == 0:                                  # case if y component is zero
                orthagonal_heading = velocity[0]
            else:
                orthagonal_heading = -1 * velocity[0]/velocity[1]

            # find x, y coordinate ahead of drone constrained with designated radius
            intercept_x = 2 * radius * math.sin(math.asin(velocity[0]/radius)) + drone_xpos
            intercept_y = 2 * radius * math.cos(math.acos(velocity[1]/radius)) + drone_ypos
        
            # find right turn waypoint with orthagonal vector constrained with designated radius
            orthagonal_x = radius * math.sin(math.atan(orthagonal_heading)) + intercept_x
            orthagonal_y = orthagonal_heading * (orthagonal_x - intercept_x) + intercept_y

            # insert avoidance WayPoint as first waypoint
            #client.moveToPositionAsync(orthagonal_x, orthagonal_y, drone_zpos, new_speed, vehicle_name = drone).join()
            wpl.insertWayPoint([orthagonal_x, orthagonal_y, drone_zpos], new_speed)