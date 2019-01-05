import gol
import copy
from datetime import datetime

for y in range(1000000):
  print('Init game: ' + str(y+1))
  rules = gol.Rules({'randomize': 3})

  grid = gol.Grid({'x': 50, 'y': 50})

  g = gol.Game(rules=rules,grid=grid,period_retention=50)

  g.random_grid()

  for x in range(5000):
    g.tick()
    if g.periodic != None:
      if g.ticks > 10:
        g.seed.output('games/ticks{}_period{}_time{}.json'.format(
          g.ticks,g.periodic,datetime.now().isoformat()))
      break

  g.output('games/game.json')
