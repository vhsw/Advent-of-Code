#!/usr/bin/python3

class Claim:
    def __init__(self, claim_str):
        idx, _,  pos, dim = claim_str.split()
        self.id = int(idx[1:])
        self.x, self.y = (int(p) for p in pos[:-1].split(','))
        self.w, self.h = (int(p) for p in dim.split('x'))

    def __repr__(self):
        return f'Claim {self.id} @({self.x}, {self.y}), {self.w}x{self.h}'


def overlaps(path):
    with open(path) as f:
        claims = [Claim(line) for line in f.read().splitlines()]
    len_x = max(c.x+c.w for c in claims) + 1
    len_y = max(c.y+c.h for c in claims) + 1
    canvas = [[0]*len_y for _ in range(len_x)]
    for c in claims:
        for x in range(c.x, c.x + c.w):
            for y in range(c.y, c.y + c.h):
                canvas[x][y] += 1
    overlap_area = 0
    for row in canvas:
        for itm in row:
            if itm > 1:
                overlap_area += 1

    return overlap_area

assert(overlaps('Day 3/example.txt') == 4)
print(overlaps('Day 3/input.txt'))
