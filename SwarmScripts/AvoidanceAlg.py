# Written by Dillon Mead
import math
import numpy
import airsim
import WaypointList

class AvoidanceAlg:
    # basic avoidance. drone travels at 90 deg right for X distance.
    def rightTurnAvoid(self, wpl, drone, client):
    
        radius = 5 # constraint for vector distance
        new_speed = 5 # drone velocity

        # determine drone position/ heading
        droneState = client.getMultirotorState(vehicle_name = drone).kinematics_estimated
        velocity = droneState.linear_velocity.to_numpy_array()   
        drone_ypos = droneState.position.y_val
        drone_xpos = droneState.position.x_val
        drone_zpos = droneState.position.z_val
        
        # Calculate orthagonal vector. Avoids arithmatic error
        if velocity[0] == 0:                                    # case if x component is zero
            orthagonal_heading = -1 * velocity[1]              
        elif velocity[1] == 0:                                  # case if y component is zero
            orthagonal_heading = velocity[0]
        else:
            orthagonal_heading = -1 * velocity[0]/velocity[1]

        # find x, y coordinate ahead of drone constrained with designated radius
        intercept_x = radius * math.sin(math.asin(velocity[0]/radius)) + drone_xpos
        intercept_y = radius * math.cos(math.acos(velocity[1]/radius)) + drone_ypos
        
        # find right turn waypoint with orthagonal vector constrained with designated radius
        orthagonal_x = radius * math.sin(math.atan(orthagonal_heading)) + intercept_x
        orthagonal_y = orthagonal_heading * (orthagonal_x - intercept_x) + intercept_y

        # insert avoidance WayPoint as first waypoint
        #client.moveToPositionAsync(orthagonal_x, orthagonal_y, drone_zpos, new_speed, vehicle_name = drone).join()
        wpl.insertWayPoint([orthagonal_x, orthagonal_y, drone_zpos], new_speed)