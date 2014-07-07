#!/usr/bin/python
import os
import time
import math
import pygame, sys
from pygame.locals import *
from bikecomputer import *
from infobox import *
from headerbox import *
from effortscale import *

# set up pygame
pygame.init()

# set up the window
VIEW_WIDTH = 320
VIEW_HEIGHT = 240
pygame.display.set_caption('BIKE COMPUTER')

# set up the colors
BG = (18,18,18)
LIGHT_BG = (36,36,36)
LIGHT_TEXT = (255,255,255)
GREEN = (0,127,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

# Set up the box for the header
HEADER_HEIGHT = 25

# Set up the info boxes
INFO_BOX_WIDTH = 129
INFO_BOX_HEIGHT = 55

# Set up the boxes for the main speed chart
EFFORT_BOX_WIDTH = 40
EFFORT_BOX_HEIGHT = 16
BOX_SPACING = 5
EFFORT_BOX_X = VIEW_WIDTH - EFFORT_BOX_WIDTH - BOX_SPACING

windowSurface = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32) 

FONTSIZE = 16
LINEHEIGHT = int(FONTSIZE * 1.05)

smallFont = pygame.font.SysFont(None, 16)
mediumFont = pygame.font.SysFont(None, 32)
largeFont = pygame.font.SysFont(None, 52)

def renderThings(myBikeComputer, windowSurface, smallFont, pinstate):
  # Clear the screen
  windowSurface.fill(BG)
  
  # Draw Effort Scale
  windowSurface.blit(effortScaleBox.surface,(effortScaleBox.x, effortScaleBox.y))
  # Display the header
  windowSurface.blit(header.surface,(header.x, header.y))
  # Display the current speed info box
  windowSurface.blit(currentSpeedInfoBox.surface,(currentSpeedInfoBox.x, currentSpeedInfoBox.y))
  # Display the average speed info box
  windowSurface.blit(averageSpeedInfoBox.surface,(averageSpeedInfoBox.x, averageSpeedInfoBox.y))
  # Display the max speed info box
  windowSurface.blit(maxSpeedInfoBox.surface,(maxSpeedInfoBox.x, maxSpeedInfoBox.y))
  # Display the distance info box
  windowSurface.blit(distanceInfoBox.surface,(distanceInfoBox.x, distanceInfoBox.y))

  # Display everything
  pygame.display.flip()

myBikeComputer = BikeComputer('imperial');
header = HeaderBox(0,0,VIEW_WIDTH,HEADER_HEIGHT,BLUE,LIGHT_TEXT,BOX_SPACING,'');
effortScaleBox = EffortScale(EFFORT_BOX_X,HEADER_HEIGHT+BOX_SPACING,EFFORT_BOX_WIDTH,(10*EFFORT_BOX_HEIGHT)+(10*BOX_SPACING),EFFORT_BOX_HEIGHT,BG,LIGHT_BG,BLUE,GREEN,YELLOW,RED,BOX_SPACING,2.5);
currentSpeedInfoBox = InfoBox(BOX_SPACING,HEADER_HEIGHT+BOX_SPACING,INFO_BOX_WIDTH,INFO_BOX_HEIGHT,LIGHT_BG,LIGHT_TEXT,YELLOW,BOX_SPACING/2,'0.0','CURRENT SPEED','MPH');
averageSpeedInfoBox = InfoBox(INFO_BOX_WIDTH+2*BOX_SPACING,HEADER_HEIGHT+BOX_SPACING,INFO_BOX_WIDTH,INFO_BOX_HEIGHT,LIGHT_BG,LIGHT_TEXT,RED,BOX_SPACING/2,'0.0','AVERAGE SPEED','MPH');
maxSpeedInfoBox = InfoBox(BOX_SPACING,HEADER_HEIGHT+2*BOX_SPACING+INFO_BOX_HEIGHT,INFO_BOX_WIDTH,INFO_BOX_HEIGHT,LIGHT_BG,LIGHT_TEXT,GREEN,BOX_SPACING/2,'0.0','MAX SPEED','MPH');
distanceInfoBox = InfoBox(INFO_BOX_WIDTH+2*BOX_SPACING,HEADER_HEIGHT+2*BOX_SPACING+INFO_BOX_HEIGHT,INFO_BOX_WIDTH,INFO_BOX_HEIGHT,LIGHT_BG,LIGHT_TEXT,BLUE,BOX_SPACING/2,'0.0','DISTANCE','MI');
prevPinState = False

# main loop
while True:
  # Handle keyboard events
  for event in pygame.event.get():
    pinState = False
    if(event.type == KEYDOWN and event.key == K_SPACE):
      pinState = True
    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
      pygame.quit()
      sys.exit()
    
  currentTime = int(time.time() * 1000)
  
  if(pinState == True and prevPinState == False):
    myBikeComputer.update(currentTime, pinState)
  else:
    myBikeComputer.update(currentTime, False)
 
  header.update(time.strftime("%I:%M:%S %p"))
  effortScaleBox.update(myBikeComputer.getDisplayVelocity())
  currentSpeedInfoBox.update(str(round(myBikeComputer.getDisplayVelocity(),1)))
  averageSpeedInfoBox.update(str(round(myBikeComputer.getAverageVelocity(),1)))
  maxSpeedInfoBox.update(str(round(myBikeComputer.getMaxVelocity(),1)))
  distanceInfoBox.update(str(round(myBikeComputer.getDistance(),2)))
  renderThings(myBikeComputer, windowSurface, smallFont, pinState)
  prevPinState = pinState
