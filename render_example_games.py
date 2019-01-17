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
  EXAMPLE_PATH = 'games/interesting/'

  file_list = os.listdir(EXAMPLE_PATH)
  random.shuffle(file_list)
  r = Render()
  for game_file in file_list:
    if os.path.isdir(EXAMPLE_PATH + game_file): continue
    g = init(EXAMPLE_PATH + game_file)
    r.game = g
    out = r.play()
    if out == 'Done': break
    if out == 'Move':
      os.rename(EXAMPLE_PATH + game_file, EXAMPLE_PATH + 'shteve/' + game_file)
