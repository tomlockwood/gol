import random
from lib.rule import *

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
