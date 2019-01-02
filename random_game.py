import gol

for y in range(1000):
  rules = gol.Rules({'randomize': 3})

  grid = gol.Grid({'x': 25, 'y': 50})

  g = gol.Game(rules=rules,grid=grid)

  g.random_grid()

  for x in range(100):
    g.tick()
    g.show()

  g.output('game.json')
