import time
class BikeComputer():
  MM_IN_AN_INCH = 25.4 
  MM_IN_A_MILE = 1609344
  MM_IN_A_KILOMETER = 1000000
  SECONDS_IN_AN_HOUR = 3600
  SECONDS_IN_A_MINUTE = 60
  MS_IN_A_SECOND = 1000.0000
  displayFormat = 'metric'
  clicks = 0
  lastClick = 0
  hertz = 0.0
  readings = [ ] 
  index = 0
  velocity = 0
  avgVelocity = 0
  distance = 0.0
  wheelSize = 2136.0

  def __init__(self, displayFormat):
    self.displayFormat = displayFormat
    self.clicks = 0
    self.lastClick = int(time.time() * BikeComputer.MS_IN_A_SECOND)
    self.hertz = 0.0
    
    self.readings = []
    for i in range(10):
      self.readings.append(0)

    self.index = 0
    self.velocity = 0.0
    self.avgVelocity = 0.0
    self.distance = 0.0
    self.wheelSize = 2136.0 # 700c x 28 according to a Bell cycling computer chart

  def update(self, currentTime):
    # get the time delta
    delta = currentTime - self.lastClick
    self.clicks += 1  
    clickDelta = delta
    # We're not going to punish you for long periods of inactivity
    self.readings[self.index] = min(clickDelta, 3000)
    
    # Increment the index
    self.index += 1
    # wrap around when we get to the end of the list
    if(self.index > (len(self.readings) - 1)):
      self.index = 0   
      
    # Avg all the last 10 readings to get the velocity
    clickDelta = max((sum(self.readings) / len(self.readings)),1)
    
    # calculate the instantaneous speed
    self.hertz = BikeComputer.MS_IN_A_SECOND / clickDelta
    # Velocity = hertz * wheel circumference, in mm/s
    self.velocity = (self.hertz * self.wheelSize)
    self.avgVelocity = (self.velocity + self.avgVelocity) / 2.0
    # Distance travelled = clicks * wheel circumference, in mm
    self.distance = self.clicks * self.wheelSize    
    # Update the last click
    self.lastClick = currentTime

  def getReadings(self):
    return str(self.readings)

  def getClicks(self):
    return str(self.clicks)

  def getVelocity(self):
    if(self.displayFormat == 'metric'):
      return (self.velocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR
    else:
      return (self.velocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR
  
  def getAvgVelocity(self):
    if(self.displayFormat == 'metric'):
      return (self.avgVelocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR
    else:
      return (self.avgVelocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR
  
  def getDistance(self):
    if(self.displayFormat == 'metric'):
      return (self.distance / BikeComputer.MM_IN_A_KILOMETER)
    else:
      return (self.distance / BikeComputer.MM_IN_A_MILE)
  
  def getFormattedWheelSize(self):
    if(self.displayFormat == 'metric'):
      return str(self.wheelSize) + ' mm'
    else:
      return str(round(self.wheelSize / BikeComputer.MM_IN_AN_INCH,3)) + ' in'

  def getFormattedVelocity(self):
    if(self.displayFormat == 'metric'):
      return str(round((self.velocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR, 3)) + 'kmph'
    else:
      return str(round((self.velocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR, 3)) + 'mph'
  
  def getFormattedAvgVelocity(self):
    if(self.displayFormat == 'metric'):
      return str(round((self.avgVelocity / BikeComputer.MM_IN_A_KILOMETER) * BikeComputer.SECONDS_IN_AN_HOUR, 3)) + 'kmph'
    else:
      return str(round((self.avgVelocity / BikeComputer.MM_IN_A_MILE) * BikeComputer.SECONDS_IN_AN_HOUR, 3)) + 'mph'
  
  def getFormattedDistance(self):
    if(self.displayFormat == 'metric'):
      return str(round((self.distance / BikeComputer.MM_IN_A_KILOMETER),3))+'km'
    else:
      return str(round((self.distance / BikeComputer.MM_IN_A_MILE),3))+'mi'

