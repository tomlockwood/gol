import unittest
import numpy
from lib.gol import *

class TestRuleCreation(unittest.TestCase):

  def test_random_alive(self):
    self.r = Rule(rule_amount=2)
    self.assertTrue(self.r.alive in [True, False])
  
  def test_random_rule(self):
    self.r = Rule(rule_amount=3)
    self.assertTrue(max(self.r.transitions) < 3)
