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

def glider_test(last_commit,hostname):
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

if __name__ == '__main__':
  last_commit = subprocess.check_output(["git", "describe","--always"]).strip().decode()
  hostname = socket.gethostname()

  glider_test(last_commit,hostname)