import airsim
import math

class distance3D:

    # @Param: {x,y,x} coordinate set 1 and coordinate set 2.
    # @Return: 3 Dimensional distance between coordinate pair.
    def calcDistance(x1, y1, z1, x2, y2, z2):

        # 3D distance between two coordinates
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    # Function to separate Lidar coordinates into single dimension variables


    # Function to separate drone kinematic coordinates into single dimension variables
    