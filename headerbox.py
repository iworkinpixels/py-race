#!/usr/bin/python
import os
import time
import pygame, sys
from pygame.locals import *

pygame.init()

class HeaderBox():
  x = 0
  y = 0
  w = 0
  h = 0
  bgColor = (0,0,0)
  textColor = (127,127,127)
  padding = 5
  text = ''
  surface = pygame.Surface((0,0), pygame.SRCALPHA, 32)
  mediumFont = pygame.font.SysFont(None, 32)

  def __init__(self,x,y,w,h,bgColor,textColor,padding,text):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.text = text
    self.bgColor = bgColor
    self.textColor = textColor
    self.surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA, 32)
    mediumFont = pygame.font.SysFont(None, 32)

  def update(self,sometext):
    # update the text
    self.text = sometext
    # fill the box with background color
    self.surface.fill(self.bgColor)
    # draw on the text
    text = self.mediumFont.render(self.text, True, self.textColor, self.bgColor)
    textRect = text.get_rect()
    self.surface.blit(text, (self.w - textRect.width-self.padding/2, self.padding/2))
