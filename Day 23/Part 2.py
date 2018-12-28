#!/usr/bin/env python
import heapq


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

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def z(self):
        return self.pos[2]


class Volume:
    def __init__(self, top, bottom):     
        min_ = min(top, bottom)
        max_ = max(top, bottom)
        length = (max_ - min_)
        round_l = 2**(length - 1).bit_length()   
        self.min = min_
        self.max = min_ + round_l

    def __repr__(self):
        return f'Volume({self.min}, {self.max})'

    @property
    def size(self):
        length = (self.max - self.min)**3
        return length
    @property
    def sub_volumes(self):
        half = (self.max - self.min)//2
        for i in range(3):
            for coord in range(self.min[i], self.max[i], half[i]):
                pass
                



def madness(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    bots = [Nanobot.from_str(line) for line in raw_data]

    min_ = min(min(bot.pos[i] - bot.radius for bot in bots) for i in range(3))
    max_ = max(max(bot.pos[i] + bot.radius for bot in bots) for i in range(3))
    print(min_, max_)

    return

# v = Volume((-1,-1,-1), (3,2,1))
# print(v, v.size)
v = Volume((0,0,0), (3,2,1))
print(v, v.sub_volumes)

# print(madness('Day 23/example.0.txt'))
# assert madness('Day 23/example.1.txt') == 36
# print(madness('Day 23/input.txt'))
