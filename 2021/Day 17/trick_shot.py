"""Day 17: Trick Shot"""
import re

with open("2021/Day 17/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    bounds = parse(data)
    dist = -bounds[2] - 1
    return dist * (dist + 1) // 2


def part2(data: str):
    """Part 2 solution"""
    bounds = parse(data)
    vels = set()
    for x in range(bounds[1] + 1):
        for y in range(bounds[2], -bounds[2] + 1):
            pos = complex(x, y)
            if not check(pos, bounds):
                continue
            vels.add(pos)
    return len(vels)


def check(vel: complex, bounds: list[int]):
    lo_x, hi_x, lo_y, hi_y = bounds
    pos = 0j
    while pos.imag > lo_y:
        pos += vel
        if lo_y <= pos.imag <= hi_y and lo_x <= pos.real <= hi_x:
            return True
        if vel.real > 0:
            vel -= 1

        elif vel.real < 0:
            vel += 1
        vel -= 1j
    return False


def parse(data: str):
    match = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", data)
    if not match:
        raise ValueError(data)
    return list(map(int, match.groups()))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
