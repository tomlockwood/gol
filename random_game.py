import gol

rules = gol.Rules()

grid = gol.Grid({'x': 50, 'y': 50})

g = gol.Game(rules=rules,grid=grid)

g.random_grid()

for x in range(50):
  g.tick()
  g.show()
