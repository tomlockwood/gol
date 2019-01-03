from gol import *
import sys

def init(filename):
  g = load_game(filename)

  for x in range(1000):
    g.tick()
    g.show()

if __name__ == '__main__':
  init(sys.argv[1])
