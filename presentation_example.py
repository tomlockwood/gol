from lib.gol import *
from lib.renderer import *
import os

def progressive_slide(text):
    disp = []

    for line in text:
        disp.append(line)
        r.display_slide(disp,100,250,300)


title = ["CELLULAR AUTOMATA"]

r = Render(50,50)

# text, size, x, y

r.display_slide(title,300,250,300)

slide01 = [
    "What is a cellular automata?",
    " * Not enough time",
    "Well, can you give us an example?!?!?",
    " * 2d grid",
    " * Cells can be alive or dead",
    " * If a cell is dead...",
    " and has 3 live neighbours it becomes alive",
    " * If a cell is alive",
    " and it has 2 or 3 live neighbours it remains alive",
    " Otherwise it [DIES]",
    "Show us the pretty thing already",
    " * Ok",
    " * Here u go"
]

progressive_slide(slide01)

rules = Rules(rules=[
  Rule(alive=False,transitions=[0,0,0,1,0,0,0,0,0],colour={'r':0,'g':0,'b':0}),
  Rule(alive=True,transitions=[0,0,1,1,0,0,0,0,0],colour={'r':255,'g':255,'b':255})
  ])

grid = Grid(x=50,y=50)

r.game = Game(grid=grid,rules=rules)
r.game.random_grid()
r.play()

slide02 = [
    "That's Conway's game of life",
    " * But I want to have my own game named after me",
    " * Ok so, I implemented some machine learning",
    " * Not really",
    " * I'm a total dumbass",
    " * Like, a real dum dum",
    " * I bruteforced random rule and colour combos",
    "Show us the thing already",
    " * Ok",
    " * Fine",
    " * Here u go"
]

progressive_slide(slide02)

def init(filename):
  g = load_game(filename)
  g.metadata = load_metadata(filename)
  g.metadata['filename'] = filename

  return g

file_path = 'games/interesting/'

if __name__ == '__main__':
  file_list = os.listdir(file_path)
  random.shuffle(file_list)
  for game_file in file_list:
    if os.path.isdir(file_path + game_file): continue
    g = init(file_path + game_file)
    r.game = g
    out = r.play()
    if out == 'Done': break