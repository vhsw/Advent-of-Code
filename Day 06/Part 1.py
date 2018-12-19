#!/usr/bin/python3

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
                if self.grid[i][j] != '.':
                    continue
                current = Point(j, i)
                distances = [current - p for p in points]
                min_dist = min(distances)
                if distances.count(min_dist) == 1:
                    self.grid[i][j] = string.ascii_letters[distances.index(
                        min_dist)]

        self.corners = []
        for i in self.grid[0]:
            if i != '.':
                self.corners.append(i)
        for i in self.grid[-1]:
            if i != '.':
                self.corners.append(i)
        for i in [j[0] for j in self.grid]:
            if i != '.':
                self.corners.append(i)
        for i in [j[-1] for j in self.grid]:
            if i != '.': 
                self.corners.append(i)
        
        print(self.corners)

    def max_area(self):
        res = []
        for letter in string.ascii_letters:
            if letter not in self.corners:
                res.append(sum(row.count(letter) for row in self.grid))
        return max(res)

    def __repr__(self):
        lines = [''.join(line) for line in self.grid]
        return '\n'.join(lines) + '\n'

    def plot(self):
        import matplotlib.pyplot as plt
        import numpy as np
        grid = np.zeros((len(self.grid),len(self.grid[0]))) 
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '.':
                    grid[i][j] = 100
                else:    
                    grid[i][j] = string.ascii_letters.index(self.grid[i][j])
        plt.imshow(grid)
        plt.show()

def area(path):
    with open(path) as f:
        raw = list(f.read().splitlines())
    data = [Point.from_str(line) for line in raw]
    grid = Grid(data)
    #grid.plot()
    return grid.max_area()


#assert(area('Day 6/example.txt') == 17)
print(area('Day 6/input.txt'))
