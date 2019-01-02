import gol
import json

rules = gol.Rules()

grid = gol.Grid({'x': 50, 'y': 50})

g = gol.Game(rules=rules,grid=grid)

g.random_grid()

for x in range(10):
  g.tick()
  g.show()

print(json.dumps(vars(grid)))
for x in rules.rules:
  print(json.dumps(vars(x)))
