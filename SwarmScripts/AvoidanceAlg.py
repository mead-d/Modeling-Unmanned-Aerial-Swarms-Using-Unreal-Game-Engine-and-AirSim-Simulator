# Written by Dillon Mead
import numpy
import airsim
import msgpackrpc

class AvoidanceAlg:
    # basic avoidance. drone travels at 90 deg right for X distance.
    def rightTurnAvoid(self, drone,client):
        
        detour = 5 # avoidance distance

        # determine drone position/ heading
        droneState = client.getMultirotorState(vehicle_name = drone).kinematics_estimated
        velocity = droneState.linear_velocity.to_numpy_array()   

         #select new coordinates at 90deg
         #velocity vector is in the 1st quadrant
        if velocity[0] > 0 and velocity[1] > 0:
            new_x = droneState.position.x_val - detour
            new_y = droneState.position.y_val
            new_z = droneState.position.z_val
         #velocity vector is in the 4th quadrant
        elif velocity[0] < 0 and velocity[1] > 0:
            new_x = droneState.position.x_val
            new_y = droneState.position.y_val - detour
            new_z = droneState.position.z_val
            #velocity vector is in the 3rd quadrant
        elif velocity[0] < 0 and velocity[1] < 0:
            new_x = droneState.position.x_val + detour
            new_y = droneState.position.y_val
            new_z = droneState.position.z_val
         #velocity vector is in the 2nd quadrant
        elif velocity[0] > 0 and velocity[1] < 0:
            new_x = droneState.position.x_val
            new_y = droneState.position.y_val + detour
            new_z = droneState.position.z_val


        coords = [new_x, new_y, new_z]
        newx = coords[0]
        newy = coords[1]
        newz = coords[2]
        # insert avoidance WayPoint as first unvisited location
        client.moveToPositionAsync(newx,newy,newz-30,10,vehicle_name = drone).join()
        #wpl.insertWayPoint(coord, 5)