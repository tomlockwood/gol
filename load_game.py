import gol

g = gol.load_game(
  '/Users/tom/Documents/scratch/gol/games/game_ticks26_period6_time2019-01-03T12:11:39.754669.json'
  )

# gr = gol.Grid(definition={'x':25,'y':150})

# g = gol.Game(r,gr)
# g.random_grid()

for x in range(1000):
  g.tick()
  g.show()
