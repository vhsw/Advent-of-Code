#!/usr/bin/env python
import functools
from collections import namedtuple

@functools.lru_cache(maxsize=None)
def get_index(pos, target, depth):
    if pos == target:
        return 0
    x, y = pos
    if x == y == 0:
        return 0
    elif y == 0:
        index = x * 16807
    elif x == 0:
        index = y * 48271
    else:
        index = get_erosion((x-1, y), target, depth) * \
            get_erosion((x, y-1), target, depth)
    return index


def get_erosion(pos, target, depth):
    return (get_index(pos, target, depth) + depth) % 20183


def madness(depth, target):
    index = {}
    region_type = {}
    for x in range(target[0] + 1):
        for y in range(target[1] + 1):
            pos = (x, y)
            index[pos] = get_index(pos, target, depth)
            region_type[pos] = get_erosion(pos, target, depth) % 3    
    
    return sum(region_type.values())


assert madness(depth=510, target=(10, 10)) == 114
print(madness(depth=4080, target=(14, 785)))
