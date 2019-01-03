import unittest
from gol import *

class TestRandomGameCreation(unittest.TestCase):

  def test_randomization(self):
    g = Game()
    self.assertEqual(g.grid.state[4][4],0)

class TestConwaysGameOfLife(unittest.TestCase):

  def setUp(self):
    self.r = Rules({'rules': [
      Rule({'alive': False,
      'transitions': [0,0,0,1,0,0,0,0,0]}),
      Rule({'alive': True,
      'transitions': [0,0,1,1,0,0,0,0,0]})
      ]})
  
  def test_stable_square(self):
    state = \
    [
      [0,0,0,0],
      [0,1,1,0],
      [0,1,1,0],
      [0,0,0,0]
    ]
    g = Game(self.r,Grid({'state': state}))
    self.assertEqual(g.find_alive(1,1),3)
    g.tick()
    self.assertEqual(g.grid.state,state)

  def test_corners(self):
    state = \
    [
      [1,0,0,1],
      [0,0,0,0],
      [0,0,0,0],
      [1,0,0,1]
    ]
    state_next = \
    [
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]
    ]
    g = Game(self.r,Grid({'state': state}))
    g.tick()
    self.assertEqual(g.grid.state,state_next)
  
  def test_toad(self):
    state = \
    [
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,1,1,1,0],
      [0,1,1,1,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0]
    ]
    state_next = \
    [
      [0,0,0,0,0,0],
      [0,0,0,1,0,0],
      [0,1,0,0,1,0],
      [0,1,0,0,1,0],
      [0,0,1,0,0,0],
      [0,0,0,0,0,0]
    ]
    g = Game(self.r,Grid({'state': state}))
    g.tick()
    self.assertEqual(g.grid.state,state_next)

class TestGridCreation(unittest.TestCase):

  def test_random_size(self):
    self.g = Grid()
    self.assertTrue(self.g.x > 4)
    self.assertTrue(self.g.x < 11)
    self.assertTrue(self.g.y > 4)
    self.assertTrue(self.g.y < 11)
  
  def test_random_state(self):
    self.g = Grid()
    self.assertEqual(self.g.state[4][4],0)

  def test_set_state(self):
    state = [[0,0,0],[0,0,0]]
    self.g = Grid({'state': state})
    self.assertEqual(self.g.x,2)
    self.assertEqual(self.g.y,3)
    self.assertEqual(self.g.state,state)
  
  def test_set_x_y(self):
    self.g = Grid({'x': 2, 'y': 1})
    self.assertEqual(self.g.state,[[0],[0]])

class TestRuleCreation(unittest.TestCase):

  def test_random_alive(self):
    self.r = Rule({'rule_amount': 2})
    self.assertTrue(self.r.alive in [True, False])
  
  def test_random_rule(self):
    self.r = Rule({'rule_amount': 3})
    self.assertTrue(max(self.r.transitions) < 3)

class TestRulesCreation(unittest.TestCase):
  
  def test_random_rules(self):
    r = Rules()
    rules_out = []
    for x in r.rules:
      rules_out += x.transitions
    self.assertTrue(max(rules_out) < r.amount)

if __name__ == '__main__':
    unittest.main()
