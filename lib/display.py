import pyxel

class Display:
  def __init__(self,game,ticks=1500):
    self.game = game
    self.ticks = ticks
    pyxel.init(game.grid.x,game.grid.y)
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

  def draw(self):
    pyxel.image(0).set(0, 0, self.game.grid.state)
    for x in range(self.ticks):
      self.game.tick()
      pyxel.image(0).set(0, 0, self.game.grid.state)
