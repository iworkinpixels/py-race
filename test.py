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
SPEED_BOX_WIDTH = 40
SPEED_BOX_HEIGHT = 16
BOX_SPACING = 5
SPEED_BOX_X = VIEW_WIDTH - SPEED_BOX_WIDTH - BOX_SPACING

windowSurface = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32) 
FONTSIZE = 16
LINEHEIGHT = int(FONTSIZE * 1.05)
smallFont = pygame.font.SysFont(None, 16)
mediumFont = pygame.font.SysFont(None, 32)
largeFont = pygame.font.SysFont(None, 52)

def renderThings(myBikeComputer, windowSurface, smallFont, pinstate):
  # Clear the screen
  windowSurface.fill(BG)
  
  # Draw Boxes For Instantaneous Speed
  if(myBikeComputer.getVelocity() > 1*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,BLUE,(SPEED_BOX_X, (VIEW_HEIGHT-1*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-1*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 2*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,BLUE,(SPEED_BOX_X, (VIEW_HEIGHT-2*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-2*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 3*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,BLUE,(SPEED_BOX_X, (VIEW_HEIGHT-3*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-3*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 4*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,BLUE,(SPEED_BOX_X, (VIEW_HEIGHT-4*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-4*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 5*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,GREEN,(SPEED_BOX_X, (VIEW_HEIGHT-5*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-5*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 6*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,GREEN,(SPEED_BOX_X, (VIEW_HEIGHT-6*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-6*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 7*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,GREEN,(SPEED_BOX_X, (VIEW_HEIGHT-7*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-7*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 8*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,YELLOW,(SPEED_BOX_X, (VIEW_HEIGHT-8*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-8*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 9*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,YELLOW,(SPEED_BOX_X, (VIEW_HEIGHT-9*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-9*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  if(myBikeComputer.getVelocity() > 10*myBikeComputer.boxUnit):
    pygame.draw.rect(windowSurface,RED,(SPEED_BOX_X, (VIEW_HEIGHT-10*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))
  else:
    pygame.draw.rect(windowSurface,LIGHT_BG,(SPEED_BOX_X, (VIEW_HEIGHT-10*(SPEED_BOX_HEIGHT+BOX_SPACING)), SPEED_BOX_WIDTH, SPEED_BOX_HEIGHT))

  # Draw the header
  pygame.draw.rect(windowSurface,BLUE,(0, 0, VIEW_WIDTH, HEADER_HEIGHT))
  string = time.strftime("%I:%M:%S %p")
  text = mediumFont.render(string, True, LIGHT_TEXT, BLUE)
  textRect = text.get_rect()
  windowSurface.blit(text, (VIEW_WIDTH-BOX_SPACING-textRect.width, BOX_SPACING/2))
  
  # Draw the current speed box
  pygame.draw.rect(windowSurface,LIGHT_BG,(BOX_SPACING, HEADER_HEIGHT+BOX_SPACING, INFO_BOX_WIDTH, INFO_BOX_HEIGHT))
  string = "CURRENT SPEED"
  text = smallFont.render(string, True, LIGHT_TEXT, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (2*BOX_SPACING, HEADER_HEIGHT+2*BOX_SPACING))
  string = str(round(myBikeComputer.getDisplayVelocity(),1))
  text = largeFont.render(string, True, YELLOW, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (INFO_BOX_WIDTH - textRect.width, HEADER_HEIGHT+INFO_BOX_HEIGHT + BOX_SPACING-textRect.height))

  # Draw the average speed box
  pygame.draw.rect(windowSurface,LIGHT_BG,(2*BOX_SPACING+INFO_BOX_WIDTH, HEADER_HEIGHT+BOX_SPACING, INFO_BOX_WIDTH, INFO_BOX_HEIGHT))
  string = "AVERAGE SPEED"
  text = smallFont.render(string, True, LIGHT_TEXT, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (3*BOX_SPACING+INFO_BOX_WIDTH, HEADER_HEIGHT+2*BOX_SPACING))
  string = str(round(myBikeComputer.getAverageVelocity(),1))
  text = largeFont.render(string, True, RED, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (2*INFO_BOX_WIDTH+BOX_SPACING-textRect.width, HEADER_HEIGHT+INFO_BOX_HEIGHT + BOX_SPACING-textRect.height))
  
  # Draw the max speed box
  pygame.draw.rect(windowSurface,LIGHT_BG,(BOX_SPACING, HEADER_HEIGHT+2*BOX_SPACING+INFO_BOX_HEIGHT, INFO_BOX_WIDTH, INFO_BOX_HEIGHT))
  string = "MAX SPEED"
  text = smallFont.render(string, True, LIGHT_TEXT, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (2*BOX_SPACING, HEADER_HEIGHT+3*BOX_SPACING+INFO_BOX_HEIGHT))
  string = str(round(myBikeComputer.getMaxVelocity(),1))
  text = largeFont.render(string, True, GREEN, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (INFO_BOX_WIDTH - textRect.width, HEADER_HEIGHT+2*INFO_BOX_HEIGHT + 2*BOX_SPACING-textRect.height))

  # Draw the distance box
  pygame.draw.rect(windowSurface,LIGHT_BG,(2*BOX_SPACING+INFO_BOX_WIDTH, HEADER_HEIGHT+2*BOX_SPACING+INFO_BOX_HEIGHT, INFO_BOX_WIDTH, INFO_BOX_HEIGHT))
  string = "DISTANCE"
  text = smallFont.render(string, True, LIGHT_TEXT, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (3*BOX_SPACING+INFO_BOX_WIDTH, HEADER_HEIGHT+3*BOX_SPACING+INFO_BOX_HEIGHT))
  string = str(round(myBikeComputer.getDistance(),2))
  text = largeFont.render(string, True, BLUE, LIGHT_BG)
  textRect = text.get_rect()
  windowSurface.blit(text, (2*INFO_BOX_WIDTH+BOX_SPACING-textRect.width, HEADER_HEIGHT+2*INFO_BOX_HEIGHT + 2*BOX_SPACING-textRect.height))

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
    myBikeComputer.update(currentTime, pinState)
  else:
    myBikeComputer.update(currentTime, False)
  
  renderThings(myBikeComputer, windowSurface, smallFont, pinState)
  prevPinState = pinState
