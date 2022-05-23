#!/usr/bin/python3

import random
import itertools

class Player:
    alive = True
    def __init__(self, name):
        self.name = name

class Event:
    def __init__(self, name, text, num_participants, participants, p_action):
        self.name = name
        self.text = text
        self.num_participants = num_participants
        self.participants = participants
        self.p_action = p_action
    def action(participants):
        p_action(*participants)

num_players = int(input("How many players? "))

player_list = []

for i in range(num_players):
    t_name = input(f"Name of player {i}: ")
    player_list.append(Player(t_name))

event_list = []
add = event_list.append
def kill(p1, p2):
    p2.alive = False
def nothing(*args):
    pass

add(Event("stab", "$1 stabs $2 in the back", 2, [], kill))
add(Event("shoot", "$1 shoots $2 in the head", 2, [], kill))

add(Event("stab", "$1 and $2 hold hands", 2, [], nothing))
add(Event("fishing", "$1 fishes in the river", 1, [], nothing))
add(Event("cliff fall", "$1 slips and falls off a cliff", 1, [], nothing))
add(Event("search water", "$1 searches for water", 1, [], nothing))

def partition(lst, n):
    return [lst[i::n] for i in range(n)]

dead_players = []

while True:
    for i,p in enumerate(player_list):
        if not p.alive:
            dead_players.append(p)
            player_list[i] = None
    player_list = [p for p in player_list if p is not None]
    random.shuffle(player_list)
    random.shuffle(event_list)
    player_list = partition(player_list, 2)
    print(player_list)
    player_list = itertools.chain(*player_list)
    for p in player_list:
        print(p.name, end=' ')
    print()
    input()