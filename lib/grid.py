import random

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
