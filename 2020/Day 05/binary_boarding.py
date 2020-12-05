"Day 05 answers"
INPUT = "2020/Day 05/input.txt"


def decode(line):
    rows = line[:7]
    cols = line[7:]
    row = list(range(128))
    for c in rows:
        l = len(row)
        if c == "F":
            row = row[: l // 2]
        else:
            row = row[l // 2 :]
    col = list(range(8))
    for c in cols:
        l = len(col)
        if c == "L":
            col = col[: l // 2]
        else:
            col = col[l // 2 :]
    return row[0] * 8 + col[0]


def part1(data):
    "Part 1 answer"
    return max(decode(l.strip()) for l in data)


def part2(data):
    "Part 2 answer"
    s = {decode(l.strip()) for l in data}
    for i in range(max(s)):
        if i not in s and (i + 1) in s and (i - 1) in s:
            return i


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    # DATA = ["FBFBBFFRLR"]
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
