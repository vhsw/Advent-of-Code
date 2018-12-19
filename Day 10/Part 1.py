#!/usr/bin/python3
import re
import pprint


class Point:
    def __init__(self, data):
        regex = 'position=<([ -]*\d+), ([ -]*\d+)> velocity=<([ -]*\d+), ([ -]*\d+)>'
        matches = re.match(regex, data)
        self.x, self.y, self.dx, self.dy = map(int, matches.groups())

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy})'


class Canvas:
    def __init__(self, points):
        self.points = points

    def get_size(self, step):
        data = [(p.x + p.dx * step, p.y + p.dy * step) for p in self.points]
        min_x = min(p[0] for p in data)
        min_y = min(p[1] for p in data)
        max_x = max(p[0] for p in data) + 1
        max_y = max(p[1] for p in data) + 1
        return min_x, max_x, min_y, max_y

    def draw(self, step):
        data = [(p.x + p.dx * step, p.y + p.dy * step) for p in self.points]
        min_x, max_x, min_y, max_y = self.get_size(step)
        canvas = [[' ' for i in range(min_x, max_x)]
                  for j in range(min_y, max_y)]
        for x, y in data:
            #print(x-min_x, y - min_y, len(canvas), len(canvas[0]))
            canvas[y-min_y][x-min_x] = '#'
        pprint.pprint([''.join(line) for line in canvas])


def message(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    points = [Point(line) for line in raw_data]
    canvas = Canvas(points)
    # canvas.draw(3)
    canvas.draw(10418)
    return 0


# message('Day 10/example.txt')
message('Day 10/input.txt')
