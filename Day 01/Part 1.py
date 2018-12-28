#!/usr/bin/env python


def get_first_repeat(path):
    with open(path) as f:
        return sum(int(i) for i in f.read().splitlines())


assert get_first_repeat('Day 01/example.txt') == 0
print(get_first_repeat('Day 01/input.txt'))
