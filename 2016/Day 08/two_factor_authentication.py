"Day 08 answers"
import re

INPUT = "2016/Day 08/input.txt"


def redner(matrix):
    lines = []
    lines.append(f"\n+{'-' * len(matrix[0])}+")
    for line in matrix:
        line = "".join(line)
        lines.append(f"|{line}|")
    lines.append(f"+{'-' * len(matrix[0])}+\n")
    return "\n".join(lines)


def run(data):
    matrix = [[" "] * 50 for i in range(6)]
    for line in data:
        if m := re.match(r"rect (\d+)x(\d+)", line):
            y, x = m.groups()
            y = int(y)
            x = int(x)
            for row in range(x):
                for col in range(y):
                    matrix[row][col] = "#"
        elif m := re.match(r"rotate row y=(\d+) by (\d+)", line):
            y, val = m.groups()
            y = int(y)
            val = int(val)
            matrix[y] = matrix[y][-val:] + matrix[y][:-val]
        elif m := re.match(r"rotate column x=(\d+) by (\d+)", line):
            x, val = m.groups()
            x = int(x)
            val = int(val)
            column = [line[x] for line in matrix]
            column = column[-val:] + column[:-val]
            for row, val in zip(matrix, column):
                row[x] = val
    return matrix


def part1(data):
    "Part 1 answer"
    matrix = run(data)
    return sum(line.count("#") for line in matrix)


def part2(data):
    "Part 2 answer"
    matrix = run(data)
    return redner(matrix)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split("\n")

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
