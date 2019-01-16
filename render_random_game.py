import os
from datetime import datetime
from lib.renderer import *
from lib.gol import *

loop = True

r = Render()

filename = 'games/{}/{}.json'

while loop:
    g = Game(grid=Grid(x=50,y=50),rules=Rules())
    g.random_grid()
    r.game = g
    out = r.play()
    if out == 'Done': 
        loop = False
    elif out == 'Next':
        g.output(filename.format('boring',datetime.now().isoformat()),True)
    elif out == 'Move':
        g.output(filename.format('interesting',datetime.now().isoformat()),True)

    