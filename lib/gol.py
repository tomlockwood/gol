import random
import time
import json
from lib.rule import *
from lib.rules import *
from lib.grid import *
from lib.game import *

def load_rules(file=None,json_game=None):
  if file != None:
    with open(file,'r') as infile:
      json_game = json.load(infile)
  rules = []
  for rule in json_game['rules']:
    rules.append(Rule(**rule))
  return Rules(rules=rules)

def load_grid(file=None,json_game=None):
  if file != None:
    with open(file,'r') as infile:
      json_game = json.load(infile)
  return Grid(**json_game['grid'])

def load_metadata(file=None,json_game=None):
  if file != None:
    with open(file,'r') as infile:
      json_game = json.load(infile)
  return json_game['metadata']

def load_game(file):
  with open(file,'r') as infile:
    json_game = json.load(infile)
  grid = load_grid(json_game=json_game)
  ruleset = load_rules(json_game=json_game)
  game = Game(rules=ruleset,grid=grid)
  game.init_alives()
  game.ticks = json_game.get('ticks',0)
  game.metadata = load_metadata(json_game=json_game)

  return game
