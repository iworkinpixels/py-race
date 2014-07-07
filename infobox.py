#!/usr/bin/python
import os
import time
import pygame, sys
from pygame.locals import *

pygame.init()

class InfoBox():
  x = 0
  y = 0
  w = 0
  h = 0
  bgColor = (0,0,0)
  labelColor = (255,255,255)
  textColor = (127,127,127)
  padding = 5
  text = ''
  label = ''
  units = ''
  surface = pygame.Surface((0,0), pygame.SRCALPHA, 32)
  smallFont = pygame.font.SysFont(None, 16)
  largeFont = pygame.font.SysFont(None, 52)

  def __init__(self,x,y,w,h,bgColor,labelColor,textColor,padding,text,label,units):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.text = text
    self.label = label
    self.units = units
    self.bgColor = bgColor
    self.labelColor = labelColor
    self.textColor = textColor
    smallFont = pygame.font.SysFont(None, 16)
    largeFont = pygame.font.SysFont(None, 52)
    self.surface = pygame.Surface((self.w, self.h), pygame.SRCALPHA, 32)

  def update(self,sometext):
    # update the text
    self.text = sometext
    # fill the box with background color
    self.surface.fill(self.bgColor)
    # draw on the label
    text = self.smallFont.render(self.label, True, self.labelColor, self.bgColor)
    textRect = text.get_rect()
    self.surface.blit(text, (self.padding,self.padding))
    # draw on the units
    text = self.smallFont.render(self.units, True, self.labelColor, self.bgColor)
    textRect = text.get_rect()
    self.surface.blit(text, (self.w - textRect.width - self.padding,self.h - textRect.height-self.padding))
    # draw on the text
    text = self.largeFont.render(self.text, True, self.textColor, self.bgColor)
    textRect = text.get_rect()
    self.surface.blit(text, (self.padding, self.h - textRect.height))
