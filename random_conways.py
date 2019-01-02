import gol

rules = gol.Rules({'rules': [
  gol.Rule({'alive': False,
  'transitions': [0,0,0,1,0,0,0,0,0]}),
  gol.Rule({'alive': True,
  'transitions': [0,0,1,1,0,0,0,0,0]})
  ]})

grid = gol.Grid({'x': 50, 'y': 50})

g = gol.Game(rules=rules,grid=grid)

g.random_grid()

for x in range(50):
  g.tick()
  g.show()
