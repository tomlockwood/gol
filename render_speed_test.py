from lib.renderer import *
import random
import pygame

r = Render()

clock = pygame.time.Clock()

for i in range(100):
    r.clear()
    for x in range(50):
        for y in range(50):
            r.draw_cell(random.randint(0,255),random.randint(0,255),random.randint(0,255),x,y)
    r.generate_text(['FPS:   ' + str(int(clock.get_fps()))])
    r.display()
    clock.tick(30)