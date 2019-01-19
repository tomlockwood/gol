import pygame
import pygame.freetype
import random
from lib.game import *

class Render:

  def __init__(self,x=50,y=50):
    pygame.init()
    self.x = x
    self.y = y
    infoObject = pygame.display.Info()
    self.w = infoObject.current_w
    self.h = infoObject.current_h
    self.grid_size()
    self.screen = pygame.display.set_mode((self.w, self.h),pygame.FULLSCREEN)
    pygame.font.init()
    self.font = pygame.freetype.Font('assets/slkscr.ttf', 30)
    self.done = False

  def grid_size(self):
    self.cell_edge = int((self.h-200)/self.x)
    cell_height_length = self.cell_edge * self.y
    cell_dist_from_mid = int(cell_height_length/2)
    self.grid_start_x = self.h - cell_dist_from_mid
    self.grid_start_y = self.w - cell_dist_from_mid
    
  def generate_grid(self):
    for x in range(self.x):
      for y in range(self.y):
        colour = self.game.state_rule(x,y).colour
        pygame.draw.rect(self.screen, (int(colour['r']), int(colour['g']), int(colour['b'])), \
          pygame.Rect((x*self.cell_edge)+self.grid_start_x-200, (y*self.cell_edge)+100, self.cell_edge, self.cell_edge))

  def generate_text(self,input,x=0,y=0):
    for idx, line in enumerate(input):
      text, rect = self.font.render(line, (255,255,255))
      self.screen.blit(text,(x,y+(30*idx)))

  def play(self,ticks=0):
    # Determine window size, set up the grid based on the game
    clock = pygame.time.Clock()
    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            return 'Done'
          elif event.key == pygame.K_SPACE:
            return 'Next'
          elif event.key == pygame.K_k:
            return 'Move'

      if self.game.ticks > ticks and ticks != 0:
        return 'TimeOut'
      self.screen.fill((0,0,0))
      out = []
      out.append('Tick:   ' + str(self.game.ticks))
      out.append('FPS:   ' + str(int(clock.get_fps())))
      self.generate_grid()
      for k in self.game.metadata:
        out.append('{}:   {}'.format(k,self.game.metadata[k]))
      self.generate_text(out)
      pygame.display.flip()
      self.game.tick()
      clock.tick(30)
