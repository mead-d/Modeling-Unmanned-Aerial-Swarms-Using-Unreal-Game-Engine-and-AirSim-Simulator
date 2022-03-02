# Equation originally developed by John Mueller.
# Modular form and generalized function developed by Dillon Mead.

import airsim
import math

class Vector3D:

    # Calculates distance between two coordinates in 3 dimensional space
    # @Param: {x,y,z} coordinate set 1 and coordinate set 2.
    # @Return: 3 Dimensional distance between coordinate pair.
    def calcDistance(x1, y1, z1, x2, y2, z2):

        # 3D distance between two coordinates
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    # Calculates the vector decomposition of the vector between an origin and second coordinate
    # @Param: {x,y,z} coordinate set 1 and set 2
    # @Return: {x vector, y vector, z vector}
    def vectorize(origin_x, origin_y, origin_z, x2, y2, z2):
        x_vector = x2 - origin_x
        y_vector = y2 - origin_y
        z_vector = z2 - origin_z

        return [x_vector, y_vector, z_vector]

    # Determines the angle of a 2D x-y vector
    # @Param: {x,y,z} coordinate set 1 and set 2
    # @Return: angle of vector in radians
    def vectorAngle(x_vector, y_vector):

        return math.atan2(x_vector, y_vector) # Because of N.E.D. system in AirSim, x and y parameter is swapped.