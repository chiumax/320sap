"""
Goals
- figure out how to use sapai
- generate data
    - randomized teams against other randomized teams
        - team 1
            - list of the 5 animals
        - team 2
            - list of the 5 animals
        - which team won
    - randomized pet against other randomized pet
    - round based random matchups

possible analysis
- if we see a pet that has bad performance but 
  good performance in team environment - good support animal
- if we see a pet that has good performance (1v1) but
  bad performance in team environment - bad support animal

- pet positioning make s a difference

- common pets in teams that win
- what sort of ability is best ?
"""


from sapai.pets import Pet
from sapai.teams import Team
from sapai.battle import Battle
from sapai.data import data

import random
import csv

# pet = Pet("ant")

pets = list(data["pets"].keys())
print(pets)

count = 500

team_header = ['team1', 'team2', 'win', 'team1_tier', 'team2_tier']

# def gen_one():
#   # one v one random pet data
#   f = open('data/gen_one.csv', 'w')
#   writer = csv.writer(f)
#   writer.writerow(team_header)
#   i = 0
#   while i < count:
#     t1 = random.choice(pets)
#     t2 = random.choice(pets)
#     try:
#       writer.writerow([t1,t2,str(Battle(Team([t1]),Team([t2])).battle())])
#       i+=1
#     except:
#       pass

def gen_allOneCombs():
  # one v one pet data
  f = open('data/gen_one.csv', 'w')
  writer = csv.writer(f)
  writer.writerow(team_header)
  for idx, x in enumerate(pets):
    for z in range(idx, len(pets)):
        # print(x, pets[z])
      # tier
      tier1 = data["pets"][x]["tier"]
      tier2 = data["pets"][pets[z]]["tier"]
      try:
        writer.writerow([x,pets[z],str(Battle(Team([x]),Team([pets[z]])).battle()), tier1, tier2])
      except:
        pass


def gen_two():
  # two v two random pet data
  f = open('data/gen_two.csv', 'w')
  writer = csv.writer(f)
  writer.writerow(team_header)
  i = 0
  while i < count:
    t1=[]
    tier1 = 0
    for _ in range(2):
      t = random.choice(pets)
      try:
        tier1 += int(data["pets"][t]["tier"])
      except:
        pass
      t1.append(t)
    t2 = []
    tier2 = 0
    for _ in range(2):
      t = random.choice(pets)
      try:
        tier2 += int(data["pets"][t]["tier"])
      except:
        pass
      t2.append(t)
    try:
      writer.writerow(['.'.join(t1),'.'.join(t2),str(Battle(Team(t1),Team(t2)).battle()), tier1, tier2])
      i+=1
    except:
      pass

def gen_three():
  # three v three random pet data
  f = open('data/gen_three.csv', 'w')
  writer = csv.writer(f)
  writer.writerow(team_header)
  i = 0
  while i < count:
    t1=[]
    tier1 = 0
    for _ in range(3):
      t = random.choice(pets)
      try:
        tier1 += int(data["pets"][t]["tier"])
      except:
        pass
      t1.append(t)
    t2 = []
    tier2 = 0
    for _ in range(3):
      t = random.choice(pets)
      try:
        tier2 += int(data["pets"][t]["tier"])
      except:
        pass
      t2.append(t)
    try:
      writer.writerow(['.'.join(t1),'.'.join(t2),str(Battle(Team(t1),Team(t2)).battle()), tier1, tier2])
      i+=1
    except:
      pass

def gen_four():
  # four v four random pet data
  f = open('data/gen_four.csv', 'w')
  writer = csv.writer(f)
  writer.writerow(team_header)
  i = 0
  while i < count:
    t1=[]
    tier1 = 0
    for _ in range(4):
      t = random.choice(pets)
      try:
        tier1 += int(data["pets"][t]["tier"])
      except:
        pass
      t1.append(t)
    t2 = []
    tier2 = 0
    for _ in range(4):
      t = random.choice(pets)
      try:
        tier2 += int(data["pets"][t]["tier"])
      except:
        pass
      t2.append(t)
    try:
      writer.writerow(['.'.join(t1),'.'.join(t2),str(Battle(Team(t1),Team(t2)).battle()), tier1, tier2])
      i+=1
    except:
      pass

def gen_five():
  # five v five random pet data
  f = open('data/gen_five.csv', 'w')
  writer = csv.writer(f)
  writer.writerow(team_header)
  i = 0
  while i < count:
    t1=[]
    tier1 = 0
    for _ in range(5):
      t = random.choice(pets)
      try:
        tier1 += int(data["pets"][t]["tier"])
      except:
        pass
      t1.append(t)
    t2 = []
    tier2 = 0
    for _ in range(5):
      t = random.choice(pets)
      try:
        tier2 += int(data["pets"][t]["tier"])
      except:
        pass
      t2.append(t)
    try:
      writer.writerow(['.'.join(t1),'.'.join(t2),str(Battle(Team(t1),Team(t2)).battle()), tier1, tier2])
      i+=1
    except:
      pass

def find_issue():
  fault = []
  for pet in pets:
    try:
      Battle(Team([pet]), Team([pet])).battle()
    except:
      fault.append(pet)
      print(pet)
  return [x for x in pets if x not in fault]

pets = find_issue()
gen_two()
gen_three()
gen_four()
gen_five()
# print(pet)
# keys = data.keys()
# for key in keys:
#   print(data[key].keys())