"""Day 5: A Maze of Twisty Trampolines, All Alike"""
with open("2017/Day 05/input.txt", encoding="utf-8") as fp:
    DATA = [int(line) for line in fp.read().strip().splitlines()]


def part1(data: list[int]):
    """Part 1 solution"""
    offsets = data.copy()
    ip = 0
    step = 0
    while ip < len(offsets):
        offset = offsets[ip]
        offsets[ip] += 1
        ip += offset
        step += 1
    return step


def part2(data: list[int]):
    """Part 2 solution"""
    offsets = data.copy()
    ip = 0
    step = 0
    while ip < len(offsets):
        offset = offsets[ip]
        if offset >= 3:
            offsets[ip] -= 1
        else:
            offsets[ip] += 1
        ip += offset
        step += 1
    return step


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
