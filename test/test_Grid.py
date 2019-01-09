import unittest
import numpy
from lib.gol import *

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
    self.g = Grid(state=state)
    self.assertEqual(self.g.x,2)
    self.assertEqual(self.g.y,3)
    self.assertTrue(numpy.array_equal(self.g.state,state))
  
  def test_set_x_y(self):
    self.g = Grid(x=2,y=1)
    self.assertTrue(numpy.array_equal(self.g.state,[[0],[0]]))
