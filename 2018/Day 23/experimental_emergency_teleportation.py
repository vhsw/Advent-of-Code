"""Day 23: Experimental Emergency Teleportation"""
import re
from dataclasses import dataclass


@dataclass
class Vec:
    x: int
    y: int
    z: int

    def __sub__(self, other: "Vec"):
        return Vec(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )

    def __abs__(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


with open("2018/Day 23/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    bots = parse(data)
    strongest = max(bots, key=lambda bot: bot["r"])
    return sum(abs(strongest["pos"] - bot["pos"]) <= strongest["r"] for bot in bots)


def part2(data: str):
    """Part 2 solution"""
    bots = parse(data)

    # kinda works, fails if any bots with same distance are present
    q = []
    for bot in bots:
        q.append((abs(bot["pos"]) - bot["r"] + 1, 1))
        q.append((abs(bot["pos"]) + bot["r"] + 1, -1))
    count = 0
    max_count = 0
    result = 0
    q.sort(reverse=True)
    while q:
        dist, end = q.pop()
        count += end
        if count > max_count:
            result = dist
            max_count = count

    return result


def parse(data: str):
    bots = []
    for line in data.splitlines():
        match = re.match(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)", line)
        if not match:
            raise ValueError(line)
        x, y, z, r = map(int, match.groups())
        bot = {"pos": Vec(x, y, z), "r": r}
        bots.append(bot)
    return bots


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
