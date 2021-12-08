"""Day 8: Seven Segment Search"""
from collections import Counter

with open("2021/Day 08/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    total = 0
    for line in data.splitlines():
        _, output = line.split(" | ")
        total += sum(len(digit) in {2, 3, 4, 7} for digit in output.split())
    return total


SEG_DIG = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


def part2(data: str):
    """Part 2 solution"""
    total = 0
    for line in data.splitlines():
        header, output = line.split(" | ")
        trans = str.maketrans(decode(header))
        digits = ["".join(sorted(dig.translate(trans))) for dig in output.split()]
        num = int("".join(str(SEG_DIG.index(dig)) for dig in digits))
        total += num
    return total


def decode(header: str):
    len_dig = {len(dig): dig for dig in header.split()}
    res = {"a": (set(len_dig[3]) - set(len_dig[2])).pop()}
    header = header.replace(res["a"], "")
    freq = {v: k for k, v in Counter(header.replace(" ", "")).items()}
    res["b"] = freq[6]
    res["c"] = freq[8]
    res["e"] = freq[4]
    res["f"] = freq[9]
    res["d"] = (set(len_dig[4]) - set((res["b"], res["c"], res["f"]))).pop()
    res["g"] = (set(header.replace(" ", "")) - set(res.values())).pop()
    return {v: k for k, v in res.items()}


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
