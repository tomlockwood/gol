import random
import time
import json
import copy
from lib.rules import *
from lib.grid import *

class Game:
  def __init__(self,rules=Rules(),grid=Grid(),period_retention=0):
    self.rules = rules
    self.grid = grid
    self.ticks = 0
    self.period_retention = period_retention
    if period_retention > 0:
      self.grid_states = [self.grid.state]

    self.seed = copy.deepcopy(self)

    self.metadata = {}
  
  def random_grid(self,reset_seed=True):
    for x in range(self.grid.x):
      for y in range(self.grid.y):
        self.grid.state[x][y] = random.choice(range(self.rules.amount))
    if reset_seed:
      self.seed = copy.deepcopy(self)

  def get_state(self,x,y):
    return self.grid.state[x][y]
  
  def state_rule(self,x,y):
    return self.rules.rules[self.get_state(x,y)]

  def find_alive(self,x,y):
    alive = 0
    for x_relative in range(-1,2):
      for y_relative in range(-1,2):
        if (x_relative != 0 or y_relative != 0) \
          and x+x_relative > -1 and x+x_relative < self.grid.x \
          and y+y_relative > -1 and y+y_relative < self.grid.y:
          if self.state_rule(x+x_relative,y+y_relative).alive:
            alive += 1
    return alive

  def tick(self,amount=1):
    for i in range(amount):
      self.next_state = []
      for x in range(self.grid.x):
        self.next_state.append([])
        for y in range(self.grid.y):
          adjacent = self.find_alive(x,y)
          self.next_state[x].append(self.state_rule(x,y).transitions[adjacent])
      self.grid.state = self.next_state
      if self.period_retention > 0:
        if len(self.grid_states) >= self.period_retention:
          self.grid_states.pop(0)
        self.grid_states.append(self.grid.state)
    self.ticks += amount
  
  @property
  def periodic(self):
    if self.period_retention == 0: raise ValueError('No period_retention set for this game.')
    state = self.grid.state
    # Removes last grid_state after tick, because it represents current state
    if state in self.grid_states[:-1]:
      return len(self.grid_states)-(self.grid_states.index(state)+1)
    else:
      return

  def show(self,wait=0.3):
    TEXT = '\033[38;2;'
    COLOUR_TEXT = "{r};{g};{b}m"
    WHITE_TEXT = TEXT + '255;255;255m'

    print(chr(27) + "[2J")
    print('\033[H')
    print (WHITE_TEXT + 'At tick number ' + str(self.ticks))
    for k in self.metadata:
      print('{}: {}'.format(k,self.metadata[k]))
    out = ''
    for x in range(self.grid.x):
      out += '\n'
      for y in self.grid.state[x]:
        colour = self.rules.rules[y].colour
        text_colour = TEXT + COLOUR_TEXT.format(**colour)
        out += text_colour + str(y)
    print(out + WHITE_TEXT)
    time.sleep(wait)
  
  def output(self,file,seed=False):
    json_dict = {}
    json_dict['metadata'] = self.metadata
    if seed == False:
      game = self
    elif seed == True:
      game = self.seed
    json_dict['ticks'] = game.ticks
    json_dict['rules'] = []
    for x in game.rules.rules:
      json_dict['rules'].append(vars(x))
    json_dict['grid'] = vars(game.grid)

    with open(file,'w') as outfile:
      json.dump(json_dict, outfile)
