import pygame
from game import *

class Render:

  def __init__(self,game=None,x=300,y=400):
    pygame.init()
    self.game = game
    infoObject = pygame.display.Info()
    self.screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    self.done = False

  def cell_size(self):
    pass
  
  def generate_grid(self):
    for x in range(self.game.grid.x):
      for y in range(self.game.grid.y):
        colour = self.game.state_rule(x,y).colour
        pygame.draw.rect(self.screen, (int(colour['r']), int(colour['g']), int(colour['b'])), pygame.Rect(x*20, y*20, 20, 20))


  def play(self):
    # Determine window size, set up the grid based on the game
    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.done = True
      self.generate_grid()
      pygame.display.flip()
      self.game.tick()

g = Game()
r = Render(g)
r.play()
