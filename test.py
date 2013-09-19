#!/usr/bin/python
import os
import time
import math
import pygame, sys
from pygame.locals import *
from bikecomputer import *

# set up pygame
pygame.init()

# set up the window
VIEW_WIDTH = 0
VIEW_HEIGHT = 0
pygame.display.set_caption('BIKE COMPUTER')

# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)

windowSurface = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32) 
FONTSIZE = 48
LINEHEIGHT = 52
basicFont = pygame.font.SysFont(None, FONTSIZE)

def renderThings(myBikeComputer, windowSurface, basicFont):
  # Clear the screen
  windowSurface.fill(BLACK)
  
  # Draw readings
  string = "Readings: " + myBikeComputer.getReadings()
  text = basicFont.render(string, True, WHITE, BLACK)
  textRect = text.get_rect()
  windowSurface.blit(text, (40,1*LINEHEIGHT))
  
  # Draw clicks
  string = "Clicks: " + myBikeComputer.getClicks()
  text = basicFont.render(string, True, WHITE, BLACK)
  textRect = text.get_rect()
  windowSurface.blit(text, (40,2*LINEHEIGHT))
   
  # Draw wheel size
  string = "Wheel Size: " + myBikeComputer.getFormattedWheelSize()
  text = basicFont.render(string, True, WHITE, BLACK)
  textRect = text.get_rect()
  windowSurface.blit(text, (40,3*LINEHEIGHT))
  
  # Draw velocity
  string = "Velocity: " + myBikeComputer.getFormattedVelocity()
  text = basicFont.render(string, True, WHITE, BLACK)
  textRect = text.get_rect()
  windowSurface.blit(text, (40,4*LINEHEIGHT))
  
  # Draw avg velocity
  string = "Avg Velocity: " + myBikeComputer.getFormattedAvgVelocity()
  text = basicFont.render(string, True, WHITE, BLACK)
  textRect = text.get_rect()
  windowSurface.blit(text, (40,5*LINEHEIGHT))

  # Draw distance
  string = "Distance: " + myBikeComputer.getFormattedDistance()
  text = basicFont.render(string, True, WHITE, BLACK)
  textRect = text.get_rect()
  windowSurface.blit(text, (40,6*LINEHEIGHT))

  # Display everything
  pygame.display.flip()

myBikeComputer = BikeComputer('imperial');
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
    myBikeComputer.update(currentTime)
  
  renderThings(myBikeComputer, windowSurface, basicFont)
  prevPinState = pinState
