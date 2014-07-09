#!/usr/bin/python
import time
import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
VIEW_WIDTH = 320
VIEW_HEIGHT = 240
pygame.display.set_caption('BIKE MATE')

# set up the bike computer
last_click = 0
update_counter = 0

# set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
SKY = (0,0,255)
GRASS = (0,162,0)
ASPHALT = (50,50,50)

class YellowStripes():
  def __init__(self, xpos, ypos, width, height, color, bg_color, stripe_width, stripe_length, stripe_space, velocity):
    self.xpos = xpos
    self.ypos = ypos
    self.height = height
    self.color = color
    self.bg_color = bg_color
    self.velocity = velocity
    self.offset = 0
    self.stripe_length = stripe_length
    self.stripe_width = stripe_width
    self.stripe_space = stripe_space
    self.stripe_period = stripe_length + stripe_space
    # set up a surface
    surface_width = 0
    periods = 0
    while surface_width < width + self.stripe_period:
      surface_width += self.stripe_period
      periods += 1
   
    self.width = surface_width
    self.surface = pygame.Surface((surface_width , self.height))
    self.surface.fill(self.bg_color)
    for x in range(0,periods):
      pygame.draw.rect(self.surface, self.color, (x * self.stripe_period, 0, self.stripe_length, self.stripe_width))
 
  def update(self, delta, new_velocity):
      self.velocity = new_velocity
      limit = 0 - self.stripe_period
      self.xpos -= int(delta * self.velocity)
      while self.xpos < 0 - self.stripe_period:
        self.xpos += self.stripe_period

class Topbar():
  def __init__(self, xpos, ypos, width, height, color, bg_color, font_size, text, velocity):
    self.xpos = xpos
    self.ypos = ypos
    self.width = width
    self.height = height
    self.color = color
    self.bg_color = bg_color
    self.font_size = font_size
    self.text = text
    self.velocity = velocity
    self.offset = self.width
    
    # set up font
    self.basicFont = pygame.font.SysFont(None, self.font_size)
    # set up a surface 
    self.surface = pygame.Surface((self.width, self.height))
  
  def update(self, delta):
    # black everything out
    self.surface.fill(self.bg_color)
    # draw the text onto the topbar
    text = self.basicFont.render(self.text, True, self.color, self.bg_color)
    textRect = text.get_rect()
    # calculate the padding
    text_padding = int((self.height - textRect.height) / 2) 
    textRect.topleft = (self.offset, text_padding) 
    # draw the text onto the surface
    self.surface.blit(text, textRect)
    # update the text of the topbar
    if(self.offset > 0 - textRect.width):
      self.offset -= delta * self.velocity
    else:
      self.offset = self.surface.get_rect().width  

class Console():
  def __init__(self, xpos, ypos, width, height, color, bg_color, font_size, text, velocity):
    self.xpos = xpos
    self.ypos = ypos
    self.width = width
    self.height = height
    self.color = color
    self.bg_color = bg_color
    self.font_size = font_size
    self.text = text
    self.velocity = velocity
    self.offset = 20
    
    # set up font
    self.basicFont = pygame.font.SysFont(None, self.font_size)
    # set up a surface 
    self.surface = pygame.Surface((self.width, self.height))
  
  def update(self, delta):
    # black everything out
    self.surface.fill(self.bg_color)
    # draw the text onto the topbar
    text = self.basicFont.render(self.text, True, self.color, self.bg_color)
    textRect = text.get_rect()
    # calculate the padding
    text_padding = int((self.height - textRect.height) / 2) 
    textRect.topleft = (self.offset, text_padding) 
    # draw the text onto the surface
    self.surface.blit(text, textRect)

class World():
  def __init__(self):
    # Rock some tunes, yo! (make sure you have the appropriate mp3 in the directory)
    # pygame.mixer.music.load('thtf.mp3')
    # pygame.mixer.music.play()

    # make a surface 
    self.width = VIEW_WIDTH
    self.height = VIEW_HEIGHT
    # always start at 0 velocity
    self.velocity = 0
    self.max_v = 0
    self.avg_v = 0
    self.worldx = 0
    self.stable_velocity = False
    self.windowSurface = pygame.display.set_mode((VIEW_WIDTH,VIEW_HEIGHT), FULLSCREEN, 32) 
    self.background = pygame.Surface((VIEW_WIDTH, VIEW_HEIGHT))
    
    # We are going to need to calculate some heights and positions
    grass_top = self.height * 0.45
    grass_height = self.height - grass_top
    asphalt_top = grass_top + (grass_height * 0.15)
    asphalt_height = grass_height * 0.65
    stripe_height = asphalt_height / 30
    top_stripe_top = asphalt_top + asphalt_height / 20
    bottom_stripe_top = asphalt_top + asphalt_height - (asphalt_height / 10)
    stripe_length = self.width / 20 
    yellow_stripe_top = int( (top_stripe_top + bottom_stripe_top) / 2)
    
    # make the topbar
    self.topbar = Topbar(0, 0, self.width, self.height/10, WHITE, BLACK, 16, 'Nine Inch Nails - The Hand That Feeds', 200)
    # make the yellow stripes
    self.yellow_stripes = YellowStripes(0, yellow_stripe_top, self.width, stripe_height, YELLOW, ASPHALT, stripe_height, stripe_length, stripe_length * 2, 400)

    # make the console
    self.console = Console(0, int(self.height * 0.9), self.width, self.height/10, WHITE, BLACK, 16, 'This is the console...', 200)

    # draw the sky layer onto the background surface
    self.background.fill(SKY) 
    # draw the ground rectangle onto the background surface
    pygame.draw.rect(self.background, GRASS, (0, grass_top, self.background.get_rect().width, grass_height))
    # draw the asphalt onto the background surface
    pygame.draw.rect(self.background, ASPHALT, (0, asphalt_top, self.background.get_rect().width, asphalt_height))
    # draw the white stripes onto the background surface
    pygame.draw.rect(self.background, WHITE, (0, top_stripe_top, self.background.get_rect().width, stripe_height))
    pygame.draw.rect(self.background, WHITE, (0, bottom_stripe_top, self.background.get_rect().width, stripe_height))
    
    # there... now we have a non-animated background that we can use to cover everything up during update()

  def update(self, delta, update_console):
    # update all the sub-objects
    self.console.update(delta)
    self.topbar.update(delta)
    self.yellow_stripes.update(delta, self.velocity)
    self.worldx += int(delta * self.velocity)
    if(update_console):
      self.console.text = 'DIST: ' + str(self.worldx)
      self.console.text = self.console.text + ' SPEED: ' + str(self.velocity)
      self.console.text = self.console.text + ' MAX: ' + str(self.max_v)
      self.console.text = self.console.text + ' AVG: ' + str(self.avg_v)
    # Reset the window surface to the standard background
    self.windowSurface.blit(self.background, (0,0))
    # draw the console surface to the window surface
    self.windowSurface.blit(self.console.surface, (self.console.xpos,self.console.ypos))
    # draw the topbar surface to the window surface
    self.windowSurface.blit(self.topbar.surface, (self.topbar.xpos,self.topbar.ypos))
    # draw the yellow stripe surface to the window surface
    self.windowSurface.blit(self.yellow_stripes.surface, (self.yellow_stripes.xpos,self.yellow_stripes.ypos))
    # draw the window surface to the screen
    pygame.display.flip()

myWorld = World()
clock = pygame.time.Clock()


# THE MAIN LOOP!
while True: 
  update_counter += 1
  current_time = int(time.time() * 1000)
  delta = clock.tick(60) / 1000.0 
  target_velocity = int(60000 / int (current_time - last_click))
  if (target_velocity > myWorld.velocity and last_click > 0 and myWorld.stable_velocity == False):
    myWorld.velocity += 20
  else:
    if (myWorld.velocity > 0 and myWorld.stable_velocity == False):
      myWorld.velocity -= 20
  myWorld.max_v = max(myWorld.velocity, myWorld.max_v)
  myWorld.avg_v = int((myWorld.avg_v + myWorld.velocity) / 2)
  if (update_counter == 50):
    update_counter = 0

  for event in pygame.event.get():
    if(event.type == KEYDOWN and event.key == K_SPACE):
      myWorld.stable_velocity = False
      last_click = current_time
    if(event.type == KEYDOWN and event.key == K_UP and myWorld.velocity <= 1000):
      myWorld.stable_velocity = True
      myWorld.velocity += 50
    if(event.type == KEYDOWN and event.key == K_DOWN and myWorld.velocity >= 0):
      myWorld.stable_velocity = True
      myWorld.velocity -= 50
    if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
      pygame.quit()
      sys.exit()

  if (myWorld.velocity < 0):
      myWorld.velocity = 0

  if (update_counter == 0):
    myWorld.update(delta, True)
  else:
    myWorld.update(delta, False)
