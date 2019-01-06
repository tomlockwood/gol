import matplotlib.pyplot as plt
import os
import json

game_files = os.listdir('games/')

end_ticks = []
alive_rule_count = []

alive_group_by = [0,0,0,0]

for game_file in game_files:
  with open('games/' + game_file, 'r') as json_stream:
    json_game = json.load(json_stream)

  end_tick = json_game['metadata']['end_ticks']

  if end_tick < 10: continue

  if end_tick == 1500: continue

  alives = 0

  for rule in json_game['rules']:
    if rule['alive']:
      alives += 1
  
  end_ticks.append(end_tick)
  alive_group_by[alives] += 1
  alive_rule_count.append(alives)

for idx, x in enumerate(alive_group_by):
  print ('{} alive: {}'.format(idx,x))

plt.plot(end_ticks,alive_rule_count,'ro')
plt.show()
