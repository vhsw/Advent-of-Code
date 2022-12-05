"""Day 5: Supply Stacks"""
from collections import defaultdict

with open("2022/Day 05/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    stacks, moves = parse(data)
    for n, x, y in moves:
        for _ in range(n):
            payload = stacks[x - 1].pop()
            stacks[y - 1].append(payload)
    return "".join(s[-1] for s in stacks)


def part2(data: str):
    """Part 2 solution"""
    stacks, moves = parse(data)
    for n, x, y in moves:
        payload = [stacks[x - 1].pop() for _ in range(n)]
        stacks[y - 1].extend(reversed(payload))
    return "".join(s[-1] for s in stacks)


def parse(data: str):
    stacks, moves = data.split("\n\n")
    return parse_stacks(stacks), parse_moves(moves)


def parse_stacks(data: str):
    lines = data.splitlines()
    pos = [i for i, v in enumerate(lines[-1]) if v.isdigit()]
    stacks = defaultdict(list)
    for line in lines[:-1]:
        for p in pos:
            if p < len(line) and (char := line[p]) != " ":
                stacks[p].append(char)
    return [stacks[k][::-1] for k in sorted(stacks)]


def parse_moves(data: str):
    moves = []
    for line in data.splitlines():
        _, N, _, X, _, Y = line.split()
        moves.append((int(N), int(X), int(Y)))
    return moves


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
