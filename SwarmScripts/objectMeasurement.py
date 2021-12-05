# Written by Dillon Mead

import airsim
import math

# assumptions: swarm finished moving to object - swarm consists of 3 drone
# Orient drone pair (2) at bottom of object at closest end along one dimension. (ex: y1 = y2, z1 = z2, x1 = 0 x2 = 10)

class objectMeasurement:

    def measureVol():
        # define volume
        volume = 0

        # create stack for each horizontal pass
        sliceStack = StackList()

        # loop drone pair for height of object. 
        while(True):
            # loop drone pair for length of object.
            # add slice values to stack for each horizontal plane

            # retreive current drone coordinates
            state1 = client.getMultirotorState(vehicle_name = 'Drone1')
            state2 = client.getMultirotorState(vehicle_name = 'Drone2')

            x1 = state1.kinematics_estimated.position.x_val
            y1 = state1.kinematics_estimated.position.y_val
            z1 = state1.kinematics_estimated.position.z_val

            x2 = state2.kinematics_estimated.position.x_val
            y2 = state2.kinematics_estimated.position.y_val
            z2 = state2.kinematics_estimated.position.z_val

            while(True):
                sliceStack.push(getSlice())
                # move drone pair for next slice
                f1 = client.moveToPositionAsync(x1 +1, y1, -z1, 2, vehicle_name = 'Drone1')
                f2 = client.moveToPositionAsync(x2 +1, y2, -z2, 2, vehicle_name = 'Drone2')

                # exit test evaluates last 5 stack indeces. if <= 0, exit
                if(horzCheck(sliceStack) <= 0): break

            # retreive current drone coordinates
            state1 = client.getMultirotorState(vehicle_name = 'Drone1')
            state2 = client.getMultirotorState(vehicle_name = 'Drone2')

            x1 = state1.kinematics_estimated.position.x_val
            y1 = state1.kinematics_estimated.position.y_val
            z1 = state1.kinematics_estimated.position.z_val

            x2 = state2.kinematics_estimated.position.x_val
            y2 = state2.kinematics_estimated.position.y_val
            z2 = state2.kinematics_estimated.position.z_val
            
            # move drone pair vertically
            f1 = client.moveToPositionAsync(x1, y1 +1, z1, 2, vehicle_name = 'Drone1')
            f2 = client.moveToPositionAsync(x2, y2 +1, z2, 2, vehicle_name = 'Drone2')

            # exit test evaluates sum of stack content. if <= 0, exit
            if(volumeSum(sliceStack) <= 0): break

            # sum stack and add to volume
            volume += volumeSum(sliceStack)

        return volume

    # horizontal movement end check
    @staticmethod
    def horzCheck(sliceStack):
        # check last 5 slices
        val1 = sliceStack.pop()
        val2 = sliceStack.pop()
        val3 = sliceStack.pop()
        val4 = sliceStack.pop()
        val5 = sliceStack.pop()

        # push to maintain stack integrity
        sliceStack.push(val1)
        sliceStack.push(val2)
        sliceStack.push(val3)
        sliceStack.push(val4)
        sliceStack.push(val5)

        return val1+val2+val3+val4+val5

    # sum function for stack
    @staticmethod
    def volumeSum(sliceStack):
        volume = 0

        for i in range(sliceStack.getSize()):
            volume += sliceStack.pop()
        return volume

    # End writing by Dillon Mead

    # Written by John Mueller - edited by Dillon Mead
    # function to get slice of object being measured 
    # utilizing distance sensors and distance formula
    @staticmethod
    def getSlice(drone1,drone2):

	    d1_pos = drone1.getMultirotorState().kinematics_estimated.position
	    d2_pos = drone2.getMultirotorState().kinematics_estimated.position

	    d1_x = d1_pos.x_val
	    d1_y = d1_pos.y_val
	    d1_z = d1_pos.z_val

	    d2_x = d2_pos.x_val
	    d2_y = d2_pos.y_val
	    d2_z = d2_pos.z_val

        # distance between drone pair
	    totalDistance = sqrt((d2_x - d1_x)**2 + (d2_y - d1_y)**2 + (d2_z - d1_z)**2)

	    dSensor1 = getDistanceSensorData(distance_sensor_name = "MyDistance1", vehicle_name = "Drone1")
	    dSensor2 = getDistanceSensorData(distance_sensor_name = "MyDistance2", vehicle_name = "Drone2")
	    
        slice = totalDistance - dSensor1 - dSensor2

	    if slice < 0:
		    slice = 0

	    return slice