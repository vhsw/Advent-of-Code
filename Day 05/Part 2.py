#!/usr/bin/env python
import string


def shortest_polymer(path):
    with open(path) as f:
        orig_poly = list(f.read().strip('\n'))
    res = {}
    for unit in string.ascii_lowercase:
        reaction = True
        poly = [p for p in orig_poly if p.lower() != unit]
        while reaction and poly:
            reaction = False
            for i in range(len(poly) - 1):
                a = poly[i]
                b = poly[i+1]
                if a != b and a.upper() == b.upper():
                    reaction = True
                    poly[i] = '_'
                    poly[i+1] = '_'

            poly = [p for p in poly if p != '_']
        res[unit] = len(poly)
    return min(res.values())


assert shortest_polymer('Day 05/example.txt') == 4
print(shortest_polymer('Day 05/input.txt'))
