#!/usr/bin/env python
from collections import deque


def puzzle(path):
    with open(path) as f:
        data = tuple(f.read().split())
    n_players, last_marble = map(int, (data[0], data[6]))
    last_marble *= 100
    marbles = deque([0])
    current = 0
    players = [0]*n_players
    while True:
        for i in range(n_players):
            current += 1
            if current > last_marble:
                return max(players)

            if current % 23 == 0:
                players[i] += current
                marbles.rotate(7)
                players[i] += marbles.pop()
                marbles.rotate(-1)
            else:
                marbles.rotate(-1)
                marbles.append(current)


print(puzzle('Day 09/input.txt'))
