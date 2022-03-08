import airsim
import WaypointList as wpl



class SwarmPathing(object):
    def pathTo(self,wpl,drone,client,v3d):
        vNode = wpl.validWayPoint()
        coords = vNode.coord
        speed = vNode.speed

        droneState = client.getMultirotorState(vehicle_name = drone).kinematics_estimated
        velocity = droneState.linear_velocity.to_numpy_array()   
        drone_ypos = droneState.position.y_val
        drone_xpos = droneState.position.x_val
        drone_zpos = droneState.position.z_val

        vect = v3d.vectorize(drone_xpos,drone_ypos,drone_zpos,coords[0],coords[1],coords[2])
        ang = v3d.vectorAngle(vect[0],vect[1])

        client.rotateToYawAsync(ang)
        client.moveToPositionAsync(coords[0], coords[1], coords[2], speed, vehicle_name= drone)

    def pathCheck(self,wpl,drone,client):
        vNode = wpl.validWayPoint()
        coords = vNode.coord
        kinematics = client.simGetGroundTruthKinematics(vehicle_name = drone)
        if ((abs(abs(kinematics.position.x_val)-abs(coords[0])) < 1) and (abs(abs(kinematics.position.y_val)-abs(coords[1])) < 1) and (abs(abs(kinematics.position.z_val)-abs(coords[2])) < 1)):
            wpl.visitWayPoint()
            print("Waypoint Reached")
            return True
