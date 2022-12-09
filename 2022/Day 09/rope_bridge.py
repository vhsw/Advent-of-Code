"""Day 9: Rope Bridge"""
from math import copysign

with open("2022/Day 09/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    head = 0j
    tail = 0j
    seen = {tail}
    for d_pos, n in parse(data):
        for _ in range(n):
            head += d_pos
            tail = update_tail(head, tail)
            seen.add(tail)

    return len(seen)


def part2(data: str):
    """Part 2 solution"""
    rope = [0j] * 10
    seen = {rope[-1]}
    for d_pos, n in parse(data):
        for _ in range(n):
            rope[0] += d_pos
            for i in range(len(rope) - 1):
                tail = update_tail(rope[i], rope[i + 1])
                rope[i + 1] = tail
            seen.add(rope[-1])

    return len(seen)


def parse(data: str):
    directions = {"R": 1j, "L": -1j, "U": -1, "D": 1}
    moves: list[tuple[complex, int]] = []
    for line in data.splitlines():
        move, length = line.split()
        moves.append((directions[move], int(length)))
    return moves


def update_tail(head: complex, tail: complex):
    dif = head - tail

    if abs(dif) < 1.5:
        return tail

    real_mag = min(1, abs(dif.real))
    imag_mag = min(1, abs(dif.imag))
    return tail + copysign(real_mag, dif.real) + copysign(imag_mag, dif.imag) * 1j


def sign(n: float):
    if n == 0:
        return 0
    return 1 if n > 0 else -1


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
