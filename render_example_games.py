from lib.gol import *
import sys, os
import random
from lib.renderer import *

def init(filename):
  g = load_game(filename)
  g.metadata = load_metadata(filename)
  g.metadata['filename'] = filename

  return g

if __name__ == '__main__':
  file_list = os.listdir('examples/')
  random.shuffle(file_list)
  r = Render()
  for game_file in file_list:
    if os.path.isdir('examples/' + game_file): continue
    g = init('examples/' + game_file)
    r.game = g
    out = r.play()
    if out == 'Done': break
    if out == 'Move':
      os.rename('examples/' + game_file, 'examples/shteve/' + game_file)
