"Day 15 answers"
INPUT = "2020/Day 15/input.txt"


def part1(data):
    "Part 1 answer"
    before = {}
    spoken = {}
    num = None
    for turn in range(1, 2020 + 1):
        idx = turn - 1
        if idx < len(data):
            num = data[idx]
            before[num] = turn
        else:
            if num not in spoken or num not in before:
                nxt = 0
            else:
                nxt = spoken[num] - before[num]
            if nxt in spoken:
                before[nxt] = spoken[nxt]
            spoken[nxt] = turn
            num = nxt
    return num


def part2(data):
    "Part 2 answer"
    before = {}
    spoken = {}
    num = None
    for turn in range(1, 30000000 + 1):
        idx = turn - 1
        if idx < len(data):
            num = data[idx]
            before[num] = turn
        else:
            if num not in spoken or num not in before:
                nxt = 0
            else:
                nxt = spoken[num] - before[num]
            if nxt in spoken:
                before[nxt] = spoken[nxt]
            spoken[nxt] = turn
            num = nxt
    return num


if __name__ == "__main__":
    with open(INPUT) as fp:
        RAW = fp.read()
    # RAW = "0,3,6"
    DATA = list(map(int, RAW.split(",")))
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
