import matplotlib.pyplot as plt
import os
import json

game_files = os.listdir('games/')

end_ticks = []
alive_rule_count = []
period_spread = {}
rule_amounts = []

alive_group_by = [0,0,0,0,0,0,0,0,0,0]

for game_file in game_files:
  with open('games/' + game_file, 'r') as json_stream:
    json_game = json.load(json_stream)
  
  metadata = json_game.get('metadata')
  if metadata in [{},None]: continue

  end_tick = metadata['end_ticks']
  max_ticks = metadata['max_ticks']

  period = metadata['period']

  rule_amount = metadata['rules']

  if period != None:
    if period_spread.get(period) == None:
      period_spread[period] = 1
    else:
      period_spread[period] += 1

  if end_tick < 10: continue

  if end_tick == max_ticks: continue

  if max_ticks != 3000: continue

  alives = 0

  for rule in json_game['rules']:
    if rule['alive']:
      alives += 1
  
  end_ticks.append(end_tick)
  rule_amounts.append(rule_amount)
  alive_group_by[alives] += 1
  alive_rule_count.append(alives)

for idx, x in enumerate(alive_group_by):
  print ('{} alive: {}'.format(idx,x))

for k in period_spread:
  print("{}: {}".format(k,period_spread[k]))

plt.plot(end_ticks,alive_rule_count,'ro')
plt.plot(end_ticks,rule_amounts,'b^')
plt.xlabel('ticks iteration ended')
plt.ylabel('alives/rules')
plt.title('Game of Life')
plt.show()
