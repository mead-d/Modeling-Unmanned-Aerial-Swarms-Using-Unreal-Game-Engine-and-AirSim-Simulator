class AnalyticData:

    #Initialize data variables
    def __init__(self):
        self._position = []
        self._speed = []
        self._heading = []
        self._avoidancePoint = []
        self._objDistance = []
        self._objVector = []
        self._sensorRange = []
        self._avoidanceRange = []
        self._rule = []
        self._seed = []
        self._simTime = []
        self._avoidanceTime = []

    #drone position
    def get_position(self):
        return self._position

    def set_position(self, x):
        self._position = x

    #drone speed
    def get_speed(self):
        return self._speed

    def set_speed(self, x):
        self._speed = x

    #drone heading
    def get_heading(self):
        return self._heading

    def set_heading(self, x):
        self._heading = x

    #coordinate of avoidance start
    def get_avoidancePoint(self):
        return self._avoidancePoint

    def set_avoidancePoint(self, x):
        self._avoidancePoint = x

    #distance of avoided obstacle from vehicle
    def get_objDist(self):
        return self._objDistance

    def set_objDist(self, x):
        self._objDist = x
    
    #Obstacle vector from vehicle
    def get_objVector(self):
        return self._objVector

    def set_objVector(self, x):
        self._objVector = x

    #Sensor range
    def get_sensorRange(self):
        return self._sensorRange

    def set_sensorRange(self, x):
        self._sensorRange = x

    #avoidance range
    def get_avoidanceRange(self):
        return self._avoidanceRange

    def set_avoidanceRange(self, x):
        self._avoidanceRange = x

    #avoidance rule (behavior)
    def get_rule(self):
        return self._rule

    def set_rule(self, x):
        self._rule = x
    
    #Seed of scenario
    def get_seed(self):
        return self._speed

    def set_seed(self, x):
        self._seed = x

    #scenario execution time
    def get_simTime(self):
        return self._simTime

    def set_simTime(self, x):
        self._simTime = x

    #completion time for avoidance maneuver
    def get_avoidanceTime(self):
        return self._avoidanceTime

    def set_avoidanceTime(self, x):
        self._avoidanceTime = x