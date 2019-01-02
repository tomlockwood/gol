import gol
import copy
from datetime import datetime

for y in range(1000):
  rules = gol.Rules({'randomize': 3})

  grid = gol.Grid({'x': 25, 'y': 50})

  g = gol.Game(rules=rules,grid=grid)

  g.random_grid()
  g_start = copy.deepcopy(g)
  grid_state = g.grid.state

  for x in range(1000):
    g.tick()
    if g.grid.state == grid_state: 
      g_start.output('games/game_{}_{}.json'.format(g.ticks,datetime.now().isoformat()))
      break
    grid_state = g.grid.state

  g.output('games/game.json')
