import unittest
import numpy
from lib.gol import *

class TestRandomGameCreation(unittest.TestCase):

  def test_randomization(self):
    g = Game()
    self.assertEqual(g.grid.state[4][4],0)
