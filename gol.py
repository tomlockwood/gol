import random
import time
import json

class Rule:
  def __init__(self,definition={}):
    self.alive = definition.get('alive')
    self.rule_amount = definition.get('rule_amount')
    self.colour = definition.get('colour')
    self.transitions = definition.get('transitions')

    # Set the alive status if it is ambiguous
    if self.alive == None:
      self.alive = random.choice([True,False])

    # Set or generate transitions
    if self.transitions == None:
      self.transitions = []
      for x in range(9):
        self.transitions.append(random.choice(range(definition['rule_amount'])))

    if self.colour == None:
      self.colour = {}
      self.colour['r'] = str(random.randint(0,255))
      self.colour['g'] = str(random.randint(0,255))
      self.colour['b'] = str(random.randint(0,255))
      
class Rules:
  def __init__(self,definition={}):
    self.definition = definition
    self.rules = definition.get('rules')

    # Set the amount of rules to be generated, or that exist
    if definition.get('randomize') != None:
      if self.rules != None: raise ValueError('Passed both randomize integer and preset rules.')
      rule_amount = int(definition['randomize'])
    elif self.rules != None:
      rule_amount = len(self.rules)
    else:
      rule_amount = random.randint(2,5)

    # Generate rules if they don't exist yet
    if self.rules == None:
      self.rules = []
      class_init = {}
      class_init['rule_amount'] = rule_amount 
      for x in range(rule_amount):
        self.rules.append(Rule(class_init))
    
    self.amount = rule_amount

class Grid:
  def __init__(self,definition={}):
    self.state = []
    self.state = definition.get('state')
    if self.state == None:
      self.state = []
      self.x = definition.get('x',random.randint(5,10))
      self.y = definition.get('y',random.randint(5,10))
      for x in range(self.x):
        self.state.append([])
        for y in range(self.y):
          self.state[x].append(0)
    else:
      self.x = len(self.state)
      self.y = len(self.state[0])

class Game:
  def __init__(self,rules=Rules(),grid=Grid()):
    self.rules = rules
    self.grid = grid
    self.ticks = 0
  
  def random_grid(self):
    for x in range(self.grid.x):
      for y in range(self.grid.y):
        self.grid.state[x][y] = random.choice(range(self.rules.amount))

  def get_state(self,x,y):
    return self.grid.state[x][y]

  def find_alive(self,x,y):
    alive = 0
    for x_relative in range(-1,2):
      for y_relative in range(-1,2):
        if (x_relative != 0 or y_relative != 0) \
          and x+x_relative > -1 and x+x_relative < self.grid.x \
          and y+y_relative > -1 and y+y_relative < self.grid.y:
          state = self.get_state(x+x_relative,y+y_relative)
          if self.rules.rules[state].alive:
            alive += 1
    return alive

  def tick(self,amount=1):
    for i in range(amount):
      self.next_state = []
      for x in range(self.grid.x):
        self.next_state.append([])
        for y in range(self.grid.y):
          adjacent = self.find_alive(x,y)
          state = self.get_state(x,y)
          self.next_state[x].append(self.rules.rules[state].transitions[adjacent])
    self.grid.state = self.next_state
    self.ticks += amount

  def show(self,wait=0.3):
    TEXT = '\033[38;2;'
    COLOUR_TEXT = "{r};{g};{b}m"
    WHITE_TEXT = TEXT + '255;255;255m'

    print(chr(27) + "[2J")
    print (WHITE_TEXT + 'At tick number ' + str(self.ticks))
    for x in range(self.grid.x):
      print()
      for y in self.grid.state[x]:
        colour = self.rules.rules[y].colour
        text_colour = TEXT + COLOUR_TEXT.format(**colour)
        print(text_colour + str(y), end='')
    print()
    time.sleep(wait)
  
  def output(self,file):
    json_dict = {}
    json_dict['ticks'] = self.ticks
    json_dict['rules'] = []
    for x in self.rules.rules:
      json_dict['rules'].append(vars(x))
    json_dict['grid'] = vars(self.grid)

    with open(file,'w') as outfile:
      json.dump(json_dict, outfile)

def load_rules(file=None,json_game=None):
  if file != None:
    with open(file,'r') as infile:
      json_game = json.load(infile)
  rules = []
  for rule in json_game['rules']:
    rules.append(Rule(definition=rule))
  return Rules(definition={'rules': rules})

def load_grid(file=None,json_game=None):
  if file != None:
    with open(file,'r') as infile:
      json_game = json.load(infile)
  return Grid(definition=json_game['grid'])

def load_game(file):
  with open(file,'r') as infile:
    json_game = json.load(infile)
  grid = load_grid(json_game=json_game)
  ruleset = load_rules(json_game=json_game)
  g = Game(rules=ruleset,grid=grid)
  g.ticks = json_game.get('ticks',0)

  return g
