#!/usr/bin/env python


def checksum(path):
    num_2 = 0
    num_3 = 0
    with open(path) as f:
        for line in f.read().splitlines():
            was_2 = False
            was_3 = False
            for letter in set(line):
                count = line.count(letter)
                if not was_2 and count == 2:
                    num_2 += 1
                    was_2 = True
                elif not was_3 and count == 3:
                    num_3 += 1
                    was_3 = True
    return num_2 * num_3


assert checksum('Day 02/example.1.txt') == 12
print(checksum('Day 02/input.txt'))
