import gol
import copy
from datetime import datetime

for y in range(1000000):
  print('Init game: ' + str(y+1))
  rules = gol.Rules({'randomize': 4})

  grid = gol.Grid({'x': 50, 'y': 50})

  g = gol.Game(rules=rules,grid=grid,period_retention=25)

  g.random_grid()

  for x in range(1000):
    g.tick()
    if g.periodic != None and g.ticks > 10:
      g.seed.output('games/game_ticks{}_period{}_time{}.json'.format(
        g.ticks,g.periodic,datetime.now().isoformat()))
      break

  g.output('games/game.json')
