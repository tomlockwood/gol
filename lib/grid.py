import random

class Grid:
  def __init__(self,**kwargs):
    self.state = []
    self.state = kwargs.get('state')
    if self.state == None:
      self.state = []
      self.x = kwargs.get('x',random.randint(5,10))
      self.y = kwargs.get('y',random.randint(5,10))
      for x in range(self.x):
        self.state.append([])
        for y in range(self.y):
          self.state[x].append(0)
    else:
      self.x = len(self.state)
      self.y = len(self.state[0])
