import unittest
import numpy
from lib.gol import *

class TestConwaysGameOfLife(unittest.TestCase):

  def setUp(self):
    self.r = Rules(rules=[
      Rule(alive=False,
      transitions=[0,0,0,1,0,0,0,0,0]),
      Rule(alive=True,
      transitions=[0,0,1,1,0,0,0,0,0])
      ])
  
  def test_stable_square(self):
    state = \
    [
      [0,0,0,0],
      [0,1,1,0],
      [0,1,1,0],
      [0,0,0,0]
    ]
    g = Game(self.r,Grid(state=state),period_retention=2)
    self.assertEqual(g.find_alive(1,1),3)
    self.assertEqual(g.find_alive(0,1),2)
    g.tick()
    self.assertTrue(numpy.array_equal(g.grid.state,state))
    self.assertEqual(g.periodic,1)

  def test_corners(self):
    state = \
    [
      [1,0,0,1],
      [0,0,0,0],
      [0,0,0,0],
      [1,0,0,1]
    ]
    state_next = numpy.asarray(
    [
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]
    ])
    g = Game(self.r,Grid(state=state),period_retention=2)
    g.tick()
    self.assertTrue(numpy.array_equal(g.grid.state,state_next))
    self.assertEqual(g.periodic,None)
    g.tick()
    g.tick()
    self.assertEqual(len(g.grid_states),2)
    self.assertEqual(g.periodic,1)
  
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
    g = Game(self.r,Grid(state=state),period_retention=3)
    g.tick()
    self.assertTrue(numpy.array_equal(g.grid.state,state_next))
    self.assertEqual(g.periodic,None)
    g.tick()
    self.assertEqual(g.periodic,2)
    g.tick()
    g.tick()
    self.assertEqual(g.periodic,2)
