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
    cache = set()
    results = []
    repeat_pos = 0
    repeat_area = None
    in_repeat = False
    not_first_repeat = False
    last_step = 1000000000
    for i in range(last_step):
        area = step(area)
        if in_repeat:
            trees = tuple(area.values()).count('|')
            lumberyards = tuple(area.values()).count('#')
            result = trees*lumberyards
            results.append(result)
            print(i, result)
            if area == repeat_area and not_first_repeat:
                break
            not_first_repeat = True

        else:
            frozen_area = tuple(area.items())
            if frozen_area in cache:
                in_repeat = True
                repeat_area = area.copy()
                repeat_pos = i
            else:
                cache.add(frozen_area)

    
    period = len(results)
    end = (last_step - repeat_pos)%period -2
    print('per', last_step, repeat_pos, period, end)
    return results[end]


# assert madness('Day 18/example.0.txt') == 1147
print(madness('Day 18/input.txt'))
