#!/usr/bin/python3


def puzzle(path):
    with open(path) as f:
        data = tuple(f.read().split())
    n_players, last_marble = map(int, (data[0], data[6]))
    marbles = [0]
    prev_idx = 0
    current = 0
    players = [0]*n_players
    while True:
        for i in range(n_players):
            current += 1
            if current > last_marble:
                return max(players)

            if current % 23 == 0:
                players[i] += current
                new_idx = (prev_idx - 7) % (len(marbles))
                players[i] += marbles.pop(new_idx)
            else:
                new_idx = (prev_idx + 2) % (len(marbles))
                if new_idx == 0:
                    new_idx = len(marbles)
                marbles.insert(new_idx, current)
            prev_idx = new_idx
    return


assert(puzzle('Day 9/example.0.txt') == 32)
assert(puzzle('Day 9/example.1.txt') == 8317)
assert(puzzle('Day 9/example.2.txt') == 146373)
assert(puzzle('Day 9/example.3.txt') == 2764)
assert(puzzle('Day 9/example.4.txt') == 54718)
assert(puzzle('Day 9/example.5.txt') == 37305)
print(puzzle('Day 9/input.txt'))
