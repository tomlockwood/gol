from gol import *
from lib.display import *
import sys, os

def init(filename,random_grid=True):
  if random_grid:
    r = load_rules(filename)
    g = Game(r,Grid(x=50,y=50))
    g.metadata = load_metadata(filename)
    g.random_grid()
  else:
    g = load_game(filename)
    g.metadata = load_metadata(filename)
    g.metadata['filename'] = filename

  if g.metadata.get('period') not in [None,1,2]:
    d = Display(g)

if __name__ == '__main__':
  for game_file in os.listdir('games/'):
    init('games/' + game_file,random_grid=False)
