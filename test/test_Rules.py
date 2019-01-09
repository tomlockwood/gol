import unittest
import numpy
from lib.gol import *

class TestRulesCreation(unittest.TestCase):
  
  def test_random_rules(self):
    r = Rules()
    rules_out = []
    for x in r.rules:
      rules_out += x.transitions
    self.assertTrue(max(rules_out) < r.amount)
