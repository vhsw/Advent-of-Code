"Day 09 answers"
import re

INPUT = "2016/Day 09/input.txt"


def decompress(data):
    idx = 0
    result = ""
    while idx < len(data):
        # print(f"{i=}")
        if data[idx] == "(":
            buf = ""
            idx += 1
            while data[idx] != ")":
                buf += data[idx]
                idx += 1
            idx += 1
            length, times = map(int, re.match(r"(\d+)x(\d+)", buf).groups())
            result += data[idx : idx + length] * times
            idx += length
        else:
            result += data[idx]
            idx += 1

    # print(f"{result=}")
    return result


def decompress_rec(data):
    idx = 0
    result_length = 0
    while idx < len(data):
        if data[idx] == "(":
            buf = ""
            idx += 1
            while data[idx] != ")":
                buf += data[idx]
                idx += 1
            idx += 1
            length, times = map(int, re.match(r"(\d+)x(\d+)", buf).groups())
            result_length += decompress_rec(data[idx : idx + length]) * times
            idx += length
        else:
            result_length += 1
            idx += 1

    return result_length


def part1(data):
    "Part 1 answer"
    return len(decompress(data))


def part2(data):
    "Part 2 answer"
    return decompress_rec(data)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
