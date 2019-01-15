import pygame

class Render:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((400, 300))
    self.done = False

  def play(self):
    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True
        else:
          print(event)
      pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(0, 30, 60, 60))
      pygame.display.flip()
  
r = Render()
r.play()
