import random
import numpy
# np.uint8 - 0 to 255

class Grid:
  def __init__(self,**kwargs):
    self.state = kwargs.get('state')
    if self.state == None:
      self.x = kwargs.get('x',random.randint(5,10))
      self.y = kwargs.get('y',random.randint(5,10))
      self.state = numpy.zeros([self.x,self.y],numpy.uint8)
    else:
      self.state = numpy.asarray(self.state,numpy.uint8)
      self.x = numpy.size(self.state,0)
      self.y = numpy.size(self.state,1)
