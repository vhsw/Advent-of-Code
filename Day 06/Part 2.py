#!/usr/bin/env python

import string


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def from_str(line):
        x, y = map(int, line.split(', '))
        return Point(x, y)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __sub__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class Grid:
    def __init__(self, points):
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)

        self.grid = [['.' for i in range(0, max_x + 10)]
                     for j in range(0, max_y + 10)]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                current = Point(j, i)
                distances = [current - p for p in points]
                total = sum(distances)
                self.grid[i][j] = total

    def max_area(self, lim):
        res = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] < lim:
                    res += 1
        return res

    def __repr__(self):
        lines = [''.join(line) for line in self.grid]
        return '\n'.join(lines) + '\n'

    def plot(self):
        import matplotlib.pyplot as plt
        import numpy as np
        grid = np.zeros((len(self.grid), len(self.grid[0])))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '.':
                    grid[i][j] = 100
                else:
                    grid[i][j] = string.ascii_letters.index(self.grid[i][j])
        plt.imshow(grid)
        plt.show()


def area(path, lim):
    with open(path) as f:
        raw = list(f.read().splitlines())
    data = [Point.from_str(line) for line in raw]
    grid = Grid(data)
    # grid.plot()
    return grid.max_area(lim)


assert area('Day 06/example.txt', 32) == 16
print(area('Day 06/input.txt', 10000))
