from lib.gol import *
import copy
import random
from datetime import datetime

PERIOD_RETENTION = 250
GRID_X = 50
GRID_Y = 50
TICK_LIMIT = 3000

for y in range(1000000):
  rule_amount = random.randint(2,9)
  print('Init game: ' + str(y+1))

  rules_unsatisfying = True

  while rules_unsatisfying:
    alives = 0
    rules = Rules(randomize=rule_amount)
    for rule in rules.rules:
      if rule.alive: alives += 1
    if alives not in [0,rule_amount]:
      rules_unsatisfying = False

  grid = Grid(x=GRID_X,y=GRID_Y)

  g = Game(rules=rules,grid=grid,period_retention=PERIOD_RETENTION)

  g.random_grid()

  for x in range(TICK_LIMIT):
    g.tick()
    if g.periodic != None:
      break

  g.metadata['period'] = g.periodic
  g.metadata['end_ticks'] = g.ticks
  g.metadata['max_cycle'] = PERIOD_RETENTION
  g.metadata['max_ticks'] = TICK_LIMIT
  g.metadata['rules'] = g.rules.amount
  filename = 'games/{}.json'.format(datetime.now().isoformat())
  print ('{}: {}'.format(filename,g.metadata))
  g.output(filename,seed=True)
