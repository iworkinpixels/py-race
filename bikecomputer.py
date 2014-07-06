import time
import math
class BikeComputer():
  MM_IN_AN_INCH = 25.4 
  MM_IN_A_MILE = 1609344
  MM_IN_A_KILOMETER = 1000000
  SECONDS_IN_AN_HOUR = 3600
  SECONDS_IN_A_MINUTE = 60
  MS_IN_A_SECOND = 1000.0000
  displayFormat = 'metric'
  displayInterval = 1000 # Update display every 1 second
  boxUnit = 1.0 # How many mph/kph each box on the graph represents.  We start out at 1.0, and up it as your max velocity goes over 10
  clicks = 0
  tripBegin = 0
  lastClick = 0
  lastDisplay = 0
  hertz = 0.0
  displayVelocity = 0.0
  velocity = 0.0
  avgVelocity = 0.0
  maxVelocity = 0.0
  distance = 0.0
  wheelCircumference = 2136.0
  wheelDiameter = 680.0

  def __init__(self, displayFormat):
    self.displayFormat = displayFormat
    self.clicks = 0
    self.lastDisplay = int(time.time() * BikeComputer.MS_IN_A_SECOND)
    self.lastClick = int(time.time() * BikeComputer.MS_IN_A_SECOND)
    self.tripBegin = int(time.time() * BikeComputer.MS_IN_A_SECOND)
    self.hertz = 0.0
    
    self.index = 0
    self.displayVelocity = 0.0
    self.boxtUnit = 1.0
    self.velocity = 0.0
    self.avgVelocity = 0.0
    self.maxVelocity = 0.0
    self.distance = 0.0
    self.wheelCircumference = 2136.0 # 700c x 28 according to a Bell cycling computer chart
    self.wheelDiameter = self.wheelCircumference / math.pi

  def update(self, currentTime, pinState):
    # get the delta from our last click
    clickDelta = max((currentTime - self.lastClick), 1)
    # get the delta from our last display
    displayDelta = max((currentTime - self.lastDisplay), 1)
    if(pinState == True):
      self.clicks += 1  
      # calculate the instantaneous speed
      self.hertz = BikeComputer.MS_IN_A_SECOND / clickDelta
      # Velocity = hertz * wheel circumference, in mm/s
      self.velocity = (self.hertz * self.wheelCircumference)
      self.maxVelocity = max(self.velocity,self.maxVelocity)
      # Adjust the bar graph to make the red bar barely attainable
      if(self.displayFormat == 'metric'):
        self.boxUnit = (self.maxVelocity / BikeComputer.MM_IN_A_KILOMETER * BikeComputer.SECONDS_IN_AN_HOUR) / 11
      if(self.displayFormat == 'imperial'):
        self.boxUnit = (self.maxVelocity / BikeComputer.MM_IN_A_MILE * BikeComputer.SECONDS_IN_AN_HOUR) / 11
      # Distance travelled = clicks * wheel circumference, in mm
      self.distance = self.clicks * self.wheelCircumference    
      # Update the last click
      self.lastClick = currentTime
    else:
      # decay the speed.  We know that you aren't going fast enough to have done the next click yet
      self.hertz = min((BikeComputer.MS_IN_A_SECOND / clickDelta), self.hertz)
      self.velocity = self.hertz * self.wheelCircumference
      # Distance travelled = clicks * wheel circumference, in mm
      self.distance = self.clicks * self.wheelCircumference
    # If we haven't updated the display in a while, do that now  
    if(displayDelta > self.displayInterval):
      self.updateDisplayVelocity(currentTime);
      self.lastDisplay = currentTime

  def updateDisplayVelocity(self,currentTime):
    self.displayVelocity = self.velocity
    self.avgVelocity = self.distance / (((currentTime-self.tripBegin)+1)/1000.00)
    if(self.displayFormat == 'metric' and (self.displayVelocity / BikeComputer.MM_IN_A_KILOMETER * BikeComputer.SECONDS_IN_AN_HOUR) < 1.0):
      self.displayVelocity = 0.0
    if(self.displayFormat == 'imperial' and (self.displayVelocity / BikeComputer.MM_IN_A_MILE * BikeComputer.SECONDS_IN_AN_HOUR) < 1.0):
      self.displayVelocity = 0.0
    
  def getClicks(self):
    return str(self.clicks)

  def getVelocity(self):
    if(self.displayFormat == 'metric'):
      return (self.velocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR
    else:
      return (self.velocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR
  
  def getDisplayVelocity(self):
    if(self.displayFormat == 'metric'):
      return (self.displayVelocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR
    else:
      return (self.displayVelocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR
   
  def getAverageVelocity(self):
    if(self.displayFormat == 'metric'):
      return (self.avgVelocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR
    else:
      return (self.avgVelocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR
  
  def getMaxVelocity(self):
    if(self.displayFormat == 'metric'):
      return (self.maxVelocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR
    else:
      return (self.maxVelocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR
  
  def getDistance(self):
    if(self.displayFormat == 'metric'):
      return (self.distance / BikeComputer.MM_IN_A_KILOMETER)
    else:
      return (self.distance / BikeComputer.MM_IN_A_MILE)
  
  def getFormattedWheelCircumference(self):
    if(self.displayFormat == 'metric'):
      return str(self.wheelCircumference) + ' mm'
    else:
      return str(round(self.wheelCircumference / BikeComputer.MM_IN_AN_INCH,3)) + ' in'

  def getFormattedWheelDiameter(self):
    if(self.displayFormat == 'metric'):
      return str(self.wheelDiameter) + ' mm'
    else:
      return str(round(self.wheelDiameter / BikeComputer.MM_IN_AN_INCH,3)) + ' in'

  def getFormattedVelocity(self):
    if(self.displayFormat == 'metric'):
      return str(round((self.velocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR, 1)) + 'kmph'
    else:
      return str(round((self.velocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR, 1)) + 'mph'
  
  def getFormattedDisplayVelocity(self):
    if(self.displayFormat == 'metric'):
      return str(round((self.displayVelocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR, 1)) + 'kmph'
    else:
      return str(round((self.displayVelocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR, 1)) + 'mph'
  
  def getFormattedAvgVelocity(self):
    if(self.displayFormat == 'metric'):
      return str(round((self.avgVelocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR, 1)) + 'kmph'
    else:
      return str(round((self.avgVelocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR, 1)) + 'mph'
  
  def getFormattedDistance(self):
    if(self.displayFormat == 'metric'):
      return str(round((self.distance / BikeComputer.MM_IN_A_KILOMETER),1))+'km'
    else:
      return str(round((self.distance / BikeComputer.MM_IN_A_MILE),3))+'mi'

