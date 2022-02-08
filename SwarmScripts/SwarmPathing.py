import airsim
import WaypointList as wpl


class SwarmPathing(wp1):
    def pathTo(wpl):
        vNode = wpl.validWaypoint()
        coords = vNode.coord
        speed = vNode.speed
        client.moveToPositionAsync(coords[0], coords[1], coords[2], speed, vehicle_name="Lead")

    def pathCheck(self,wpl):
        vNode = wpl.validWaypoint()
        coords = vNode.coord
        kinematics = client.simGetGroundTruthKinematics(vehicle_name = "Lead")
        if ((abs(abs(kinematics.position.x_val)-abs(coords[0])) < 1) and (abs(abs(kinematics.position.y_val)-abs(coords[1])) < 1) and (abs(abs(kinematics.position.z_val)-abs(coords[2])) < 1)):
            wpl.visitWayPoint()
