import random

class Rule:
  def __init__(self,**kwargs):
    self.alive = kwargs.get('alive')
    self.rule_amount = kwargs.get('rule_amount')
    self.colour = kwargs.get('colour')
    self.transitions = kwargs.get('transitions')

    # Set the alive status if it is ambiguous
    if self.alive == None:
      self.alive = random.choice([True,False])

    # Set or generate transitions
    if self.transitions == None:
      self.transitions = []
      for x in range(9):
        self.transitions.append(random.choice(range(kwargs['rule_amount'])))

    if self.colour == None:
      self.colour = {}
      self.colour['r'] = str(random.randint(0,255))
      self.colour['g'] = str(random.randint(0,255))
      self.colour['b'] = str(random.randint(0,255))
