"Day 09 answers"
import re

INPUT = "2016/Day 09/input.txt"


def decompress(data):
    i = 0
    result = ""
    while i < len(data):
        # print(f"{i=}")
        if data[i] == "(":
            buf = ""
            i += 1
            while data[i] != ")":
                buf += data[i]
                i += 1
            i += 1
            length, times = map(int, re.match("(\d+)x(\d+)", buf).groups())
            result += data[i : i + length] * times
            i += length
        else:
            result += data[i]
            i += 1

    # print(f"{result=}")
    return result


def decomp_rec(data):
    i = 0
    result_length = 0
    while i < len(data):
        if data[i] == "(":
            buf = ""
            i += 1
            while data[i] != ")":
                buf += data[i]
                i += 1
            i += 1
            length, times = map(int, re.match("(\d+)x(\d+)", buf).groups())
            result_length += decomp_rec(data[i : i + length]) * times
            i += length
        else:
            result_length += 1
            i += 1

    return result_length


def part1(data):
    "Part 1 answer"
    return len(decompress(data))


def part2(data):
    "Part 2 answer"
    return decomp_rec(data)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()

    # DATA = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
