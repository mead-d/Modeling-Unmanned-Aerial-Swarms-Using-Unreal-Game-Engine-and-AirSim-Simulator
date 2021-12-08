# Written by Dillon Mead -----------------------------------------------------------------------------------------------------------------------------------

import airsim
import math
import numpy


# assumptions: swarm finished moving to object - swarm consists of 3+ drone
# Orient drone pair at bottom of object at closest end along one dimension. (ex: y1 = y2, z1 = z2, x1 = 0 x2 = 10)

class objectMeasurement:

    def measureVol():

        # drone movement variables
        velocity = 1.0
        x_mov = 0.2
        y_mov = 0.2
        z_mov = 0.0

        # create stack for each horizontal collection and final vertical integration
        sliceStack = StackList()
        vertStack = StackList()

        # loop drone pair for height of object. 
        while(True):
            # add slice values for each horizontal plane to stack

            # set access to drone state
            state1 = client.getMultirotorState(vehicle_name = 'Drone1')
            state2 = client.getMultirotorState(vehicle_name = 'Drone2')

            # set up data history for inner loop break statement (first 7 slices of horizontal)
            for i in range(10):
                # measure before movement.
                sliceStack.push(getSlice())

                # retreive current drone coordinates
                x1 = state1.kinematics_estimated.position.x_val
                y1 = state1.kinematics_estimated.position.y_val
                z1 = state1.kinematics_estimated.position.z_val

                x2 = state2.kinematics_estimated.position.x_val
                y2 = state2.kinematics_estimated.position.y_val
                z2 = state2.kinematics_estimated.position.z_val

                # move drone pair for next slice
                f1 = client.moveToPositionAsync(x1 +x_mov, y1, -z1, velocity, vehicle_name = 'Drone1')
                f2 = client.moveToPositionAsync(x2 +x_mov, y2, -z2, velocity, vehicle_name = 'Drone2') 

            # loop drone pair for remaining length of object.
            while(True):
                # measure before movement.
                sliceStack.push(getSlice())

                # retreive current drone coordinates
                x1 = state1.kinematics_estimated.position.x_val
                y1 = state1.kinematics_estimated.position.y_val
                z1 = state1.kinematics_estimated.position.z_val

                x2 = state2.kinematics_estimated.position.x_val
                y2 = state2.kinematics_estimated.position.y_val
                z2 = state2.kinematics_estimated.position.z_val

                # move drone pair for next slice
                f1 = client.moveToPositionAsync(x1 +x_mov, y1, -z1, velocity, vehicle_name = 'Drone1')
                f2 = client.moveToPositionAsync(x2 +x_mov, y2, -z2, velocity, vehicle_name = 'Drone2')

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
            f1 = client.moveToPositionAsync(x1, y1 +y_mov, z1, velocity, vehicle_name = 'Drone1')
            f2 = client.moveToPositionAsync(x2, y2 +y_mov, z2, velocity, vehicle_name = 'Drone2')

            # add integrated horizontal slice to vertical stack
            vertStack.push(integrate1D(sliceStack))

            # exit test evaluates sum of stack content. if <= 0, exit
            if(vertStack.top() <= 0): break

        return integrate1D(vertStack)

    # horizontal movement end check
    @staticmethod
    def horzCheck(sliceStack):
        # check last 5 slices
        val1 = sliceStack.pop()
        val2 = sliceStack.pop()
        val3 = sliceStack.pop()
        val4 = sliceStack.pop()

        # push to maintain stack integrity
        sliceStack.push(val1)
        sliceStack.push(val2)
        sliceStack.push(val3)
        sliceStack.push(val4)

        return val1+val2+val3+val4

    # integration with numpy trapezoidal for single dimension using stack as input.
    @staticmethod
    def integrate1D(stack):
        # instantiate array
        arr = [0.0]
        # overwrite single item with top of stack
        arr[0] = stack.pop()

        # convert stack(data) into array(data) for integration
        for i in range(stack.getSize()):
            arr.append(stack.pop())

        # integrate over array and return
        return numpy.trapz(arr)

    # End writing by Dillon Mead ---------------------------------------------------------------------------------------------------------------------------



    # Written by John Mueller - edited by Dillon Mead ------------------------------------------------------------------------------------------------------
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