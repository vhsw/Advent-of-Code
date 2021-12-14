"""Day 20: Particle Swarm"""
import re

import numpy as np

with open("2017/Day 20/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    pos, vel, acc = parse(data)
    acc_vel_pos = np.stack((acc, vel, pos), axis=1)
    scores = abs(acc_vel_pos).sum(axis=2)
    base = scores.max()

    # lexicographical ordering emulation
    def key_func(arr):
        return sum(base ** i * val for i, val in enumerate(reversed(arr)))

    return np.apply_along_axis(key_func, 1, scores).argmin()


def part2(data: str):
    """Part 2 solution"""
    pos, vel, acc = parse(data)

    for _ in range(100):
        vel += acc
        pos += vel
        unique, counts = np.unique(pos, return_counts=True, axis=0)
        if np.any(counts > 1):
            collided = set(map(tuple, unique[counts > 1]))
            mask = [tuple(coords) not in collided for coords in pos]
            pos = pos[mask]
            vel = vel[mask]
            acc = acc[mask]

    return len(pos)


def parse(data: str):
    poss = []
    vels = []
    accs = []
    for line in data.splitlines():
        match = re.match(r"p=<(.*)>, v=<(.*)>, a=<(.*)>", line)
        if not match:
            raise ValueError(line)
        pos, vel, acc = match.groups()
        poss.append(list(map(int, pos.split(","))))
        vels.append(list(map(int, vel.split(","))))
        accs.append(list(map(int, acc.split(","))))
    return map(np.array, (poss, vels, accs))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
