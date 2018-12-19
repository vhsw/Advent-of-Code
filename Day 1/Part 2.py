#!/usr/bin/python3

def get_first_repeat(path):
    freq = 0
    history = set()
    with open(path) as f:
        arr = [int(i) for i in f.readlines()]
    while True:
        for i in arr:
            if freq in history:
                return freq
            else:
                history.add(freq)
                freq += i
assert(get_first_repeat('Day 1/example.txt') == 0)
print(get_first_repeat('Day 1/input.txt'))