#!/usr/bin/env python


class Nanobot:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius

    @staticmethod
    def from_str(line):
        pos, rad = line.split(', ')
        pos_start = pos.index('<')+1
        pos_end = pos.index('>')
        pos = list(map(int, pos[pos_start:pos_end].split(',')))
        _, rad = rad.split('=')
        rad = int(rad)
        return Nanobot(pos, rad)

    def __repr__(self):
        return f'Nanobot({self.pos}, {self.radius})'

    def get_distance(self, other):
        return sum(abs(s - o) for (s, o) in zip(self.pos, other.pos))

    def in_radius(self, other):
        return self.get_distance(other) <= self.radius

def madness(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    bots = [Nanobot.from_str(line) for line in raw_data]

    bot_w_max_radius = max(bots, key=lambda b: b.radius)
  
    return sum(1 for b in bots if bot_w_max_radius.in_radius(b))


print(madness('Day 23/example.0.txt') )
assert madness('Day 23/example.0.txt') == 7
print(madness('Day 23/input.txt'))
