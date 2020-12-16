"Day 04 answers"
import re
from collections import Counter

INPUT = "2016/Day 04/input.txt"


def part1(data):
    "Part 1 answer"
    s = 0
    for line in data:
        name, sector, checksum = re.match(r"((?:\w+-)+)(\d+)\[(\w+)\]", line).groups()
        letters = {i for i, _ in Counter(sorted(name.replace("-", ""))).most_common(5)}
        if letters == set(checksum):
            s += int(sector)
    return s


def part2(data):
    "Part 2 answer"
    for line in data:
        name, sector, checksum = re.match(r"((?:\w+-)+)(\d+)\[(\w+)\]", line).groups()
        letters = {i for i, _ in Counter(sorted(name.replace("-", ""))).most_common(5)}
        if letters == set(checksum):
            decrypted = ""
            for letter in name:
                if letter != "-":
                    idx = (ord(letter) - ord("a") + int(sector)) % 26 + ord("a")
                    letter = chr(idx)
                decrypted += letter
            if "north" in decrypted:
                return sector


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split("\n")
    DATA1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]""".split()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
