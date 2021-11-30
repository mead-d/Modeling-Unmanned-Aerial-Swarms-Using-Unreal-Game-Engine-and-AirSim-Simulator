
import math

# function to get slice of object being measured 
# utilizing distance sensors and distance formula

def getSlice(drone1,drone2):

	int slice 

	d1_pos = drone1.getMultirotorState().kinematics_estimated.position
	d2_pos = drone2.getMultirotorState().kinematics_estimated.position

	d1_x = d1_pos.x_val
	d1_y = d1_pos.y_val
	d1_z = d1_pos.z_val

	d2_x = d2_pos.x_val
	d2_y = d2_pos.y_val
	d2_z = d2_pos.z_val

	dSensor1 = getDistanceSensorData(distance_sensor_name = "MyDistance1", vehicle_name = "Drone1")
	dSensor2 = getDistanceSensorData(distance_sensor_name = "MyDistance2", vehicle_name = "Drone2")

	if dSensor1 or dSensor2 == 0:
		slice = 0;
	else:

	totalDistance = sqrt((d2_x - d1_x)**2 + (d2_y - d1_y)**2 + (d2_z - d1_z)**2)

	slice = totalDistance - dSensor1 - dSensor2

	return slice
