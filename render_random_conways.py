from lib.gol import *


rules = Rules(rules=[
  Rule(alive=False,transitions=[0,0,0,1,0,0,0,0,0]),
  Rule(alive=True,transitions=[0,0,1,1,0,0,0,0,0])
  ])

grid = Grid(x=50,y=50)

g = Game(rules=rules,grid=grid)

g.random_grid()

for x in range(1000):
  g.tick()
  g.show()
