#!/usr/bin/python
import os
import time
import pygame, sys
from pygame.locals import *

pygame.init()

class EffortScale():
  x = 0
  y = 0
  w = 0
  h = 0
  boxWidth = 0
  boxHeight = 0
  bgColor = (0,0,0)
  emptyColor = (0,0,0)
  lowColor = (0,0,0)
  medColor = (0,0,0)
  highColor = (0,0,0)
  topColor = (0,0,0)
  padding = 5
  surface = pygame.Surface((0,0), pygame.SRCALPHA, 32)
  value = 0.0
  unit = 2.5

  def __init__(self,x,y,w,h,boxHeight,bgColor,emptyColor,lowColor,medColor,highColor,topColor,padding,unit):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.boxHeight = boxHeight
    self.bgColor = bgColor
    self.emptyColor = emptyColor
    self.lowColor = lowColor
    self.medColor = medColor
    self.highColor = highColor
    self.topColor = topColor
    self.surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA, 32)
    self.padding = padding
    self.unit = unit

  def update(self,somevalue):
    # update the text
    self.value = somevalue
    # fill the box with background color
    self.surface.fill(self.bgColor)
    if(self.value > 1*self.unit):
      pygame.draw.rect(self.surface,self.lowColor,(0, (self.h-1*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-1*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 2*self.unit):
      pygame.draw.rect(self.surface,self.lowColor,(0, (self.h-2*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-2*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 3*self.unit):
      pygame.draw.rect(self.surface,self.lowColor,(0, (self.h-3*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-3*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 4*self.unit):
      pygame.draw.rect(self.surface,self.lowColor,(0, (self.h-4*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-4*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 5*self.unit):
      pygame.draw.rect(self.surface,self.medColor,(0, (self.h-5*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-5*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 6*self.unit):
      pygame.draw.rect(self.surface,self.medColor,(0, (self.h-6*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-6*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 7*self.unit):
      pygame.draw.rect(self.surface,self.medColor,(0, (self.h-7*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-7*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 8*self.unit):
      pygame.draw.rect(self.surface,self.highColor,(0, (self.h-8*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-8*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 9*self.unit):
      pygame.draw.rect(self.surface,self.highColor,(0, (self.h-9*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-9*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    if(self.value > 10*self.unit):
      pygame.draw.rect(self.surface,self.topColor,(0, (self.h-10*(self.boxHeight+self.padding)), self.w, self.boxHeight))
    else:
      pygame.draw.rect(self.surface,self.emptyColor,(0, (self.h-10*(self.boxHeight+self.padding)), self.w, self.boxHeight))

