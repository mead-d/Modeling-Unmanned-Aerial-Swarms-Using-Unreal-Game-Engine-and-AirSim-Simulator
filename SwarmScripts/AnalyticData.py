class AnalyticData:
    
    #Test main
	#def __init__(self):
	    #self._position = 0;
	    #self._speed = 0;
	    #self._heading = 0;
	    #self._avoidancePoint = 0;
	    #self._objDist = 0;
	    #self._objHeading = 0;
	    #self._sensorRange = 0;
	    #self._standoffRange = 0;

    
    #what position the drone is at
	
    def get_position(self):
        return self._position

    def set_position(self, x):
	    self._position = x
	

    #what speed the drone has

    def get_speed(self):
       return self._speed

    def set_speed(self, x):
       self._speed = x

    #what heading the drone is moving on
     
    def get_heading(self):
       return self._heading

    def set_heading(self, x):
	   self._heading = x

    #what point at which the avoidance manuver was initiated
    
    def get_avoidancePoint(self):
       return self._avoidancePoint
    
    def set_avoidancePoint(self, x):
	   self._avoidancePoint = x

    #detected obstacle distance from drone POV
  

    def get_objDist(self):
      return self.objDist

    def set_objDist(self, x):
	  self._objDist = x

    #obstacle heading from the drone to the obstacle

	def get_objHeading(self):
      return self._objHeading

    def set_objHeading(self, x):
	  self._objHeading = x

    #sensor Range

    def get_sensorRange(self):
      return self._sensorRange

    def set_sensorRange(self, x):
	  self._sensorRange = x

    #Standoff range

    def get_standoffRange(self):
      return self._standoffRange

    def set_standoffRange(self, x):
	  self._standoffRange = x




    #what avoidance rules were used
    def get_rules(self):
      return self._rules

    def set_rules(self, x):
	  self._rules = x


    #used to repeat and identify randomized scenarios
    
    def get_seed(self):
      return self._seed

    def set_seed(self, x):
	  self._seed = x


    #time used for simulation
    
    def get_simTime(self):
      return self._simTime

    def set_simTime(self, x):
	  self._simTime = x


    #time used for avoidance
    
    def get_avoidanceTime(self):
      return self._avoidanceTime

    def set_avoidanceTime(self, x):
	  self._advoidanceTime= x
