from gol import *
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
    g.show(1)

    period_even = (g.metadata['period'] % 2) == 0

    tick_amt = g.metadata['end_ticks'] + g.metadata['period']
    if period_even:
      tick_rng = range(int(tick_amt / 2))
    else:
      tick_rng = range(tick_amt)
      

    for x in tick_rng:
      if period_even:
        g.tick(2)
      else:
        g.tick()
      g.show()

if __name__ == '__main__':
  for game_file in os.listdir('games/'):
    print (game_file)
    init('games/' + game_file,random_grid=False)
