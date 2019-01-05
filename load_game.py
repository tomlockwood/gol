from gol import *
import sys

def init(filename,random_grid=True):
  if random_grid:
    r = load_rules(filename)
    g = Game(r,Grid(definition={'x':60,'y':100}))
    g.random_grid()
  else:
    g = load_game(filename)

  g.show(1)

  for x in range(1000):
    g.tick()
    g.show()

if __name__ == '__main__':
  init(sys.argv[1])
