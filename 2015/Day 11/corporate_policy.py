"Day 11 answers"
import re
from string import ascii_lowercase

INPUT = "2015/Day 11/input.txt"


def to_int(s):
    acc = 0
    off = ord("a")
    for c in s:
        acc *= 26
        acc += ord(c) - off
    # acc %= 26 ^ 9
    return acc


def to_s(i):
    acc = ""
    off = ord("a")
    while i:
        d, m = divmod(i, 26)
        i = d
        acc = chr(off + m) + acc
    return acc.rjust(8, "a")


tri = [ascii_lowercase[i : i + 3] for i in range(24)]


def check(s):
    if not any(t in s for t in tri):
        return False
    if any(l in s for l in ("i", "o", "l")):
        return False
    return bool(re.match(r".*(\w)\1.*(\w)\2", s))


def part1(data, offest=0):
    "Part 1 answer"
    i = to_int(data) + offest
    print(data, i, to_s(i))

    while not check(to_s(i)):
        i += 1
    return to_s(i)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part1('cqjxxyzz', 1) }")
