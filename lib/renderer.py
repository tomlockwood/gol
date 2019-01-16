import pygame
import pygame.freetype
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
    self.pixel = pygame.freetype.Font('assets/pixel.ttf', 30)
    self.done = False

  def grid_size(self):
    self.cell_edge = int((self.h-200)/self.x)
    cell_height_length = self.cell_edge * self.y
    cell_dist_from_mid = int(cell_height_length/2)
    self.grid_start_x = self.h - cell_dist_from_mid
    
  def generate_grid(self):
    for x in range(self.x):
      for y in range(self.y):
        colour = self.game.state_rule(x,y).colour
        pygame.draw.rect(self.screen, (int(colour['r']), int(colour['g']), int(colour['b'])), \
          pygame.Rect((x*self.cell_edge)+self.grid_start_x-100, (y*self.cell_edge)+100, self.cell_edge, self.cell_edge))

  def generate_text(self,input):
    text, rect = self.pixel.render(input, (255,255,255))
    return text

  def play(self):
    self.game = Game(grid=Grid(x=50,y=50),rules=Rules())
    # Determine window size, set up the grid based on the game
    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.done = True
          elif event.key == pygame.K_SPACE:
            self.game = Game(grid=Grid(x=50,y=50),rules=Rules())
            self.game.random_grid()
      self.screen.fill((0,0,0))
      self.generate_grid()
      text = self.generate_text(str(self.game.ticks))
      self.screen.blit(text,(0,0))
      pygame.display.flip()
      self.game.tick()