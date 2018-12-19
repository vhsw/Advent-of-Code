#!/usr/bin/python3

class Claim:
    def __init__(self, claim_str):
        idx, _,  pos, dim = claim_str.split()
        self.id = int(idx[1:])
        self.x, self.y = (int(p) for p in pos[:-1].split(','))
        self.w, self.h = (int(p) for p in dim.split('x'))

    def __repr__(self):
        return f'Claim {self.id} @({self.x}, {self.y}), {self.w}x{self.h}'


def no_overlaps(path):
    with open(path) as f:
        claims = [Claim(line) for line in f.read().splitlines()]
    len_x = max(c.x+c.w for c in claims) + 1
    len_y = max(c.y+c.h for c in claims) + 1
    canvas = [[0]*len_y for _ in range(len_x)]
    for c in claims:
        for x in range(c.x, c.x + c.w):
            for y in range(c.y, c.y + c.h):
                if canvas[x][y] == 0:
                    canvas[x][y] = c.id
                else:
                    canvas[x][y] = -1
    #import pprint
    #pprint.pprint(canvas)
    for c in claims:
        area = 0
        for x in range(c.x, c.x + c.w):
            for y in range(c.y, c.y + c.h):
                if canvas[x][y] == c.id:
                    area += 1

        if area == c.w * c.h:
            return c.id

assert(no_overlaps('Day 3/example.txt') == 3)
print(no_overlaps('Day 3/input.txt'))
