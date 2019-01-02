import random

class Rule:
  def __init__(self,definition={}):
    self.definition = definition
    self.alive = definition.get('alive')
    if self.alive == None:
      self.alive = random.choice([True,False])

    self.transitions = []
    if definition.get('transitions') == None:
      for x in range(definition['rule_amount']):
        self.transitions.append(random.choice(range(definition['rule_amount'])))
    else:
      self.transitions = definition['transitions']
      
class Rules:
  def __init__(self,definition={}):
    self.definition = definition
    self.rules = definition.get('rules')
    if definition.get('randomize') != None:
      if self.rules != None: raise ValueError('Passed both randomize integer and preset rules.')
      rule_amount = int(definition['randomize'])
    else:
      rule_amount = random.randint(2,5)

    if self.rules == None:
      self.rules = []
      class_init = {}
      class_init['rule_amount'] = rule_amount 
      for x in range(rule_amount):
        self.rules.append(Rule(class_init))

class Grid:
  def __init__(self,definition={}):
    self.definition = definition
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

  def show(self):
    for x in self.grid.state:
      print(x)
