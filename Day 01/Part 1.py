#!/usr/bin/python3

def get_first_repeat(path):
    with open(path) as f:
        return sum(int(i) for i in f.read().splitlines())

assert(get_first_repeat('Day 1/example.txt') == 0)
print(get_first_repeat('Day 1/input.txt'))