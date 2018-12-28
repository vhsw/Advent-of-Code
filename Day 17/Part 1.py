#!/usr/bin/env python
import sys
sys.setrecursionlimit(1500)


class Soil:
    def __init__(self, raw_data):
        self.grid = {}

        def parce(d):
            a, a_val, b, b_range = d.replace('=', ', ').split(', ')
            b_start, b_end = map(int, b_range.split('..'))
            b_range = range(b_start, b_end + 1)
            return a, int(a_val), b, b_range
        data = [parce(d) for d in raw_data]
        for a, a_val, b, b_range in data:
            for b_val in b_range:
                if a == 'x' and b == 'y':
                    t = (a_val, b_val)
                else:
                    t = (b_val, a_val)
                self.grid[t] = '#'
        self.min_x = min(k[0] for k in self.grid) - 1
        self.max_x = max(k[0] for k in self.grid) + 1
        self.min_y = min(k[1] for k in self.grid)
        self.max_y = max(k[1] for k in self.grid) + 1

    def __repr__(self):

        res = []
        for y in range(self.min_y, self.max_y):
            row = []
            for x in range(self.min_x, self.max_x):
                row.append(self.grid.get((x, y), '.'))
            res.append(''.join(row))
        return '\n'.join(res) + '\n'

    def draw(self, x=None, y=None):
        import matplotlib.pyplot as plt
        d = {'#': 0, '|': 50, '~': 100, '.': 255}
        res = []
        for y in range(self.min_y, self.max_y):
            row = []
            for x in range(self.min_x, self.max_x):
                row.append(d[self.grid.get((x, y), '.')])
            res.append(row)
        plt.imshow(res)

        plt.show()

    def try_fill(self, source_x, source_y):
        left_bound = None
        right_bound = None

        for x in range(source_x, self.min_x - 1, -1):
            if (x, source_y+1) in self.grid and self.grid[(x, source_y+1)] != '|':
                if self.grid.get((x, source_y), '.') == '#':
                    left_bound = x+1
                    break
                else:
                    self.grid[(x, source_y)] = '|'

            else:
                self.flow(x, source_y)
                break
        for x in range(source_x, self.max_x):
            if (x, source_y+1) in self.grid and self.grid[(x, source_y+1)] != '|':
                if self.grid.get((x, source_y), '.') == '#':
                    right_bound = x
                    break
                else:
                    self.grid[(x, source_y)] = '|'

            else:
                self.flow(x, source_y)
                break

        if left_bound and right_bound:
            for x in range(left_bound, right_bound):
                self.grid[(x, source_y)] = '~'
            self.try_fill(source_x, source_y - 1)

    def flow(self, source_x, source_y):
        for y in range(source_y, self.max_y):
            if (source_x, y) in self.grid and self.grid[(source_x, y)] != '|':
                self.try_fill(source_x, y-1)
                break
            else:
                self.grid[(source_x, y)] = '|'

        else:
            return


def madness(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    soil = Soil(raw_data)
    # soil.draw()
    # print(soil)
    soil.flow(500, 0)
    # soil.draw()
    # print(soil)
    return sum(1 for ((x, y), val) in soil.grid.items() if val in '~|' and soil.min_y <= y < soil.max_y)


assert madness('Day 17/example.0.txt') == 57
print(madness('Day 17/input.txt'))
