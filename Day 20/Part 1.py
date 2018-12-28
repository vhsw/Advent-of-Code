#!/usr/bin/env python


def madness(path):
    with open(path) as f:
        raw_data = f.read().strip()
    return

assert madness('Day 20/example.0.txt') == 6
assert madness('Day 20/example.1.txt') == 6
print(madness('Day 20/input.txt'))
