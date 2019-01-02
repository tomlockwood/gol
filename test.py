import unittest
import gol

class TestRandomGameCreation(unittest.TestCase):

  def test_randomization(self):
    g = gol.Game()
    self.assertEqual(g.grid.state[4][4],0)

class TestGridCreation(unittest.TestCase):

  def test_random_size(self):
    self.g = gol.Grid()
    self.assertTrue(self.g.x > 4)
    self.assertTrue(self.g.x < 11)
    self.assertTrue(self.g.y > 4)
    self.assertTrue(self.g.y < 11)
  
  def test_random_state(self):
    self.g = gol.Grid()
    self.assertEqual(self.g.state[4][4],0)

  def test_set_state(self):
    state = [[0,0,0],[0,0,0]]
    self.g = gol.Grid({'state': state})
    self.assertEqual(self.g.x,2)
    self.assertEqual(self.g.y,3)
    self.assertEqual(self.g.state,state)
  
  def test_set_x_y(self):
    self.g = gol.Grid({'x': 2, 'y': 1})
    self.assertEqual(self.g.state,[[0],[0]])

class TestRuleCreation(unittest.TestCase):

  def test_random_alive(self):
    self.g = gol.Rule({'rule_amount': 2})
    self.assertTrue(self.g.alive in [True, False])

if __name__ == '__main__':
    unittest.main()
