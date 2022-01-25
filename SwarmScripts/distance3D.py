import airsim
import math

class distance3D:

    # Something, something, something Dark Side.
    # Something, something, something complete.
    def calcDistance(coordinate1, coordinate2):
        
        # Split coordinates into dimensional components
        c1_x = coordinate1.x_val
        c1_y = coordinate1.y_val
        c1_z = coordinate1.z_val

        c2_x = coordinate2.x_val
        c2_y = coordinate2.y_val
        c2_z = coordinate2.z_val
        
        # 3D distance between two coordinates
        return math.sqrt((c2_x - c1_x)**2 + (c2_y - c1_y)**2 + (c2_z - c1_z)**2)

