class AnalyticData:
    #what position the drone is at
    position = None

    #what speed the drone has
    speed = None

    #what heading the drone is moving on
    heading = None

    #what point at which the avoidance manuver was initiated
    avoidancePoint = None

    #detected obstacle distance from drone POV
    objDist = None

    #obstacle heading from the drone to the obstacle
    objHeading = None

    #sensor Range
    sensorRange = None

    #Standoff range
    standoffRange = None




    #what avoidance rules were used
    #avoidanceRules = None

    #used to repeat and identify randomized scenarios
    #seed = None

    #time used for simulation
    #simTime = None

    #time used for avoidance
    #avoidanceTime = None