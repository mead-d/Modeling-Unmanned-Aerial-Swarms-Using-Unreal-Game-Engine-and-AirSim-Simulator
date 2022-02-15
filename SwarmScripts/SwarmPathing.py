import airsim
import WaypointList as wpl


class SwarmPathing(object):
    def pathTo(self,wpl,drone):
        client = airsim.MultirotorClient()
        vNode = wpl.validWayPoint()
        coords = vNode.coord
        speed = vNode.speed
        client.moveToPositionAsync(coords[0], coords[1], coords[2], speed, vehicle_name= drone)
        print("pathing")

    def pathCheck(self,wpl,drone):
        client = airsim.MultirotorClient()
        vNode = wpl.validWayPoint()
        coords = vNode.coord
        kinematics = client.simGetGroundTruthKinematics(vehicle_name = drone)
        if ((abs(abs(kinematics.position.x_val)-abs(coords[0])) < 1) and (abs(abs(kinematics.position.y_val)-abs(coords[1])) < 1) and (abs(abs(kinematics.position.z_val)-abs(coords[2])) < 1)):
            wpl.visitWayPoint()
            return True
