import random

class Rule:
  def __init__(self,defintion={}):
    self.definition = definition
    self.alive = definition.get('alive')
    if self.alive == None:
      self.alive = random.choice([True,False],1)

    self.transitions = []
    if definition.get('transitions') == None:
      for x in definition['rule_amount']:
        self.transitions.append(random.choice(definition['rule_amount']))
    else:
      self.transitions = definition['transitions']
      
class Rules:
  def __init__(self,definition={}):
    self.definition = definition
    self.rules = definition.get('rules')
    if definition.get('randomize') != None:
      if self.rules != None: raise ValueError('Passed both randomize integer and preset rules.')
      rule_amount = range(int(definition['randomize']))
    elif self.rules = None:
      rule_amount = range(random.randint(2,5))
    
    if self.rules = None:
      class_init = {}
      class_init['rule_amount'] = rule_amount 
      for x in rule_amount:
        self.rules.append(Rule(class_init))


class Grid:
  def __init__(self,definition={}):
    self.definition = definition
    self.grid = definition.get('state')
    if self.state == None:
      self.x = definition.get('x',random.randint(5,10))
      self.y = definition.get('y',random.randint(5,10))
    else:
      pass
      # Set x and y from loaded grid
      # self.x =
      # self.y =

class Game:
  def __init__(self,rules=Rules(),grid=Grid()):
    pass
