"""Day 4: High-Entropy Passphrases"""
from collections import Counter

with open("2017/Day 04/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    return sum(map(no_duplicates, data.splitlines()))


def no_duplicates(line: str):
    return Counter(line.split()).most_common(1)[0][1] == 1


def part2(data: str):
    """Part 2 solution"""
    return sum(map(no_anagrams, data.splitlines()))


def no_anagrams(line: str):
    sorted_phrasaes = map(lambda s: "".join(sorted(s)), line.split())
    return Counter(sorted_phrasaes).most_common(1)[0][1] == 1


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
