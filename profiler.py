from lib.gol import *
from lib.renderer import *
import cProfile
import pstats
import io
import subprocess
from datetime import datetime
import socket


def init(filename):
  g = load_game(filename)
  g.metadata = load_metadata(filename)
  g.metadata['filename'] = filename

  return g

def gliders_unrendered_test(last_commit,hostname):
  g = init('examples/shteve/gliderserrywhere.json')
  pr = cProfile.Profile()
  pr.enable()
  for x in range(1500): g.tick()
  pr.disable()
  s = io.StringIO()
  ps = pstats.Stats(pr,stream=s).sort_stats('tottime')
  ps.print_stats()
  with open('performance/gliders_unrendered/{}-{}-{}.txt'.format(datetime.now().isoformat(),last_commit,hostname),'w+') as f:
    f.write(s.getvalue())

def masses_unrendered_test(last_commit,hostname):
  g = init('examples/shteve/longlivedmasses1.json')
  pr = cProfile.Profile()
  pr.enable()
  for x in range(1500): g.tick()
  pr.disable()
  s = io.StringIO()
  ps = pstats.Stats(pr,stream=s).sort_stats('tottime')
  ps.print_stats()
  with open('performance/masses_unrendered/{}-{}-{}.txt'.format(datetime.now().isoformat(),last_commit,hostname),'w+') as f:
    f.write(s.getvalue())

def gliders_rendered_test(last_commit,hostname):
  g = init('examples/shteve/gliderserrywhere.json')
  r = Render()
  r.game = g
  pr = cProfile.Profile()
  pr.enable()
  r.play(1500)
  pr.disable()
  s = io.StringIO()
  ps = pstats.Stats(pr,stream=s).sort_stats('tottime')
  ps.print_stats()
  with open('performance/gliders_rendered/{}-{}-{}.txt'.format(datetime.now().isoformat(),last_commit,hostname),'w+') as f:
    f.write(s.getvalue())

if __name__ == '__main__':
  last_commit = subprocess.check_output(["git", "describe","--always"]).strip().decode()
  hostname = socket.gethostname()

  gliders_unrendered_test(last_commit,hostname)
  masses_unrendered_test(last_commit,hostname)
  gliders_rendered_test(last_commit,hostname)