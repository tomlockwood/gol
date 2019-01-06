import gol
import copy
from datetime import datetime

PERIOD_RETENTION = 150
GRID_X = 50
GRID_Y = 50
TICK_LIMIT = 1500
RULES = 3

for y in range(1000000):
  print('Init game: ' + str(y+1))

  rules_unsatisfying = True

  while rules_unsatisfying:
    alives = 0
    rules = gol.Rules(randomize=RULES)
    for rule in rules.rules:
      if rule.alive: alives += 1
    if alives in [1,2]:
      rules_unsatisfying = False

  grid = gol.Grid(x=GRID_X,y=GRID_Y)

  g = gol.Game(rules=rules,grid=grid,period_retention=PERIOD_RETENTION)

  g.random_grid()

  for x in range(TICK_LIMIT):
    g.tick()
    if g.periodic != None:
      break

  g.seed.output('games/{}.json'.format(datetime.now().isoformat()),
  metadata={
    'period': g.periodic,
    'end_ticks': g.ticks,
    'max_cycle': PERIOD_RETENTION,
    'x': GRID_X,
    'y': GRID_Y,
    'max_ticks': TICK_LIMIT,
    'rules': RULES
    }
  )
