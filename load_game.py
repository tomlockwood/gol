from lib.gol import *
import sys, os
import random

def play(g,game_file):
  g.show(1)

  tick_amt = g.metadata['end_ticks'] + g.metadata['period']

  opt = None
  while opt != '':
    for x in range(tick_amt):
      g.tick()
      g.show(0.1)

    print('r=replay, rg=random grid replay, f=change filename')
    print('enter nothing for next')
    opt = input('Option?: ')

    if opt == 'r':
      g.ticks = 0
      g.grid.state = g.seed.grid.state
    elif opt == 'rg':
      g.random_grid()
    elif opt == 'f':
      os.rename('games/' + game_file,'games/'+ input('Filename:'))
      return
    elif opt == '':
      return

def init(filename,random_grid=False):
  if random_grid:
    r = load_rules(filename)
    g = Game(r,Grid(x=50,y=50))
    g.metadata = load_metadata(filename)
    g.random_grid()
  else:
    g = load_game(filename)
    g.metadata = load_metadata(filename)
  
  g.metadata['filename'] = filename

  return g

if __name__ == '__main__':
  if sys.argv[1] == 'loop':
    file_list = os.listdir('games/')
    random.shuffle(file_list)
    for game_file in file_list:
      g = init('games/' + game_file,random_grid=True)
      if g.metadata.get('period') not in [None,1,2] and \
        g.metadata.get('end_ticks') > 10:
        play(g,game_file)
  else:
    g = init(sys.argv[1],random_grid=False)
    play(g,sys.argv[1])
