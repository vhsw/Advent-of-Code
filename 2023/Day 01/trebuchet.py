"""Day 1: Trebuchet?!"""
import re

with open("2023/Day 01/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""

    return sum(num_iterator(data))


def part2(data: str):
    """Part 2 solution"""
    return sum(spelled_num_iterator(data))


def num_iterator(data: str):
    for line in data.splitlines():
        first: str | None = None
        last: str | None = None
        for char in line:
            if not char.isnumeric():
                continue
            last = char
            if first:
                continue
            first = char
        assert first and last
        yield int(first + last)


SPELLS = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"


def spelled_num_iterator(data: str):
    pattern = rf"({'|'.join(SPELLS)}|\d)"
    for line in data.splitlines():
        match = re.search(pattern, line)
        if match is None:
            raise ValueError(line)
        first = match[1]
        match = re.search(rf".*{pattern}", line)
        if match is None:
            raise ValueError(line)
        last = match[1]
        yield int(unspell(first) + unspell(last))


def unspell(num: str):
    if num.isnumeric():
        return num
    return str(SPELLS.index(num) + 1)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
