#!/usr/bin/python3

def distance(str1, str2):
    dist = 0
    # assume that len str1 == len str2
    for idx in range(len(str1)):
        if str1[idx] != str2[idx]:
            dist += 1
    return dist


def find_box(path):
    with open(path) as f:
        boxes = [line for line in f.read().splitlines()]
    for idx, b1 in enumerate(boxes):
        for b2 in boxes[idx+1:]:
            if distance(b1, b2) == 1:
                return ''.join([a for a, b in zip(b1, b2) if a == b])


assert(find_box('Day 2/example.2.txt') == 'fgij')
print(find_box('Day 2/input.txt'))
