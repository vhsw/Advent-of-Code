#!/usr/bin/python3


def polymerization(path):
    with open(path) as f:
        poly = list(f.read().strip('\n'))
    # print(''.join(poly))
    reaction = True
    while reaction and poly:
        reaction = False
        for i, (a, b) in enumerate(zip(poly, poly[1:])):
            if a != b and a.upper() == b.upper():
                # print(a, b)
                del poly[i]
                del poly[i]
                reaction = True
                break
    # print(''.join(poly))
    return len(poly)


assert(polymerization('Day 5/example.txt') == 10)
print(polymerization('Day 5/input.txt'))
