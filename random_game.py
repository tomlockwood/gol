import gol
import copy
from datetime import datetime

for y in range(1000000):
  print('Init game: ' + str(y+1))
  rules = gol.Rules({'randomize': 3})

  grid = gol.Grid({'x': 25, 'y': 50})

  g = gol.Game(rules=rules,grid=grid)

  g.random_grid()
  g_start = copy.deepcopy(g)
  grid_states = [g.grid.state]

  for x in range(1000):
    g.tick()
    if g.grid.state in grid_states:
      if g.ticks > 10:
        g_start.output('games/game_ticks{}_period{}_time{}.json'.format(
          g.ticks,grid_states.index(g.grid.state)+1,datetime.now().isoformat()))
      break
    
    grid_states.append(g.grid.state)
    if len(grid_states) > 25:
      grid_states.pop(0)

  g.output('games/game.json')
