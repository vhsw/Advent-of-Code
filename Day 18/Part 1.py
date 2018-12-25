#!/usr/bin/python3


def step(area):
    mem = area.copy()
    for (x, y), letter in mem.items():
        neighbours = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                pos = x + dx, y + dy
                neighbour = mem.get(pos, None)
                if neighbour:
                    neighbours.append(neighbour)
        if letter == '.':
            if neighbours.count('|') >= 3:
                area[(x, y)] = '|'
        elif letter == '|':
            if neighbours.count('#') >= 3:
                area[(x, y)] = '#'
        elif letter == '#':
            if neighbours.count('|') >= 1 and neighbours.count('#') >= 1:
                area[(x, y)] = '#'
            else:
                area[(x, y)] = '.'
    # for i in range(50):
    #     for j in range(50):
    #         pos = i, j
    #         print(area[pos], end='')
    #     print()
    # print()

    return area


def madness(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    area = {}
    for i, line in enumerate(raw_data):
        for j, letter in enumerate(line):
            pos = i, j
            area[pos] = letter
    for i in range(10):
        area = step(area)
      
    trees = tuple(area.values()).count('|')
    lumberyards = tuple(area.values()).count('#')

    return trees * lumberyards


assert madness('Day 18/example.0.txt') == 1147
print(madness('Day 18/input.txt'))
