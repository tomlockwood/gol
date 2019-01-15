import random
from rule import *

class Rules:
  def __init__(self,**kwargs):
    self.rules = kwargs.get('rules')

    # Set the amount of rules to be generated, or that exist
    if kwargs.get('randomize') != None:
      if self.rules != None: raise ValueError('Passed both randomize integer and preset rules.')
      rule_amount = int(kwargs['randomize'])
    elif self.rules != None:
      rule_amount = len(self.rules)
    else:
      rule_amount = random.randint(2,5)

    # Generate rules if they don't exist yet
    if self.rules == None:
      self.rules = []
      for x in range(rule_amount):
        self.rules.append(Rule(rule_amount=rule_amount))
    
    self.amount = rule_amount
