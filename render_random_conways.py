from lib.gol import *
from lib.renderer import *
import time

rules = Rules(rules=[
  Rule(alive=False,transitions=[0,0,0,1,0,0,0,0,0]),
  Rule(alive=True,transitions=[0,0,1,1,0,0,0,0,0])
  ])

r = Render()

for x in range(100):
  start = time.time()
  
  grid = Grid(x=50,y=50)

  g = Game(rules=rules,grid=grid)

  g.random_grid()

  r.game = g
  r.play(100)

  end = time.time()

  runtime = end - start

  print("Runtime: {}".format(runtime))
