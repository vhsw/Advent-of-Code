"""Day 22: Sand Slabs"""
from copy import deepcopy
from dataclasses import dataclass
from string import ascii_uppercase
from typing import NamedTuple

with open("2023/Day 22/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    snapshot = Snapshot.from_str(data)
    # draw(snapshot.slabs)
    snapshot.fall_down()
    slabs = snapshot.slabs
    stable_slabs = 0
    for idx in range(len(slabs)):
        new_slabs = slabs[:idx] + slabs[idx + 1 :]
        snapshot.slabs = deepcopy(new_slabs)
        if snapshot.fall_down() > 0:
            continue
        stable_slabs += 1
    return stable_slabs


def part2(data: str):
    """Part 2 solution"""
    snapshot = Snapshot.from_str(data)
    snapshot.fall_down()
    slabs = sorted(snapshot.slabs, key=lambda slab: slab.end.z)
    fallen_slabs = 0
    for idx in range(len(slabs)):
        print(idx)
        new_slabs = slabs[:idx] + slabs[idx + 1 :]
        snapshot.slabs = deepcopy(new_slabs)
        fallen_slabs += snapshot.fall_down()
    return fallen_slabs


class Vec3(NamedTuple):
    x: int
    y: int
    z: int

    @classmethod
    def from_str(cls, line: str):
        return cls(*map(int, line.split(",")))

    def __add__(self, other: object):
        if not isinstance(other, Vec3):
            return NotImplemented
        return Vec3(*map(sum, zip(self, other)))


@dataclass
class Slab:
    start: Vec3
    end: Vec3
    row: int | None = None

    @classmethod
    def from_str(cls, line: str, row: int):
        start, end = line.split("~")
        return cls(Vec3.from_str(start), Vec3.from_str(end), row)

    def __contains__(self, point: Vec3) -> bool:
        return all(
            self.start[idx] <= val <= self.end[idx] for idx, val in enumerate(point)
        )

    def __str__(self) -> str:
        start = ",".join(map(str, self.start))
        end = ",".join(map(str, self.end))
        return f"{start}~{end}"

    def move(self, offset: Vec3):
        return Slab(self.start + offset, self.end + offset, self.row)


@dataclass
class Snapshot:
    slabs: list[Slab]

    @classmethod
    def from_str(cls, data: str):
        return cls(
            [Slab.from_str(line, row) for row, line in enumerate(data.splitlines())]
        )

    def fall_down(self):
        new_slabs: list[Slab] = []
        total = len(self.slabs)
        fallen = 0
        for idx, slab in enumerate(sorted(self.slabs, key=lambda slab: slab.end.z)):
            # print(f"Drop {idx+1} / {total}")
            moved = False
            while True:
                new_slab = slab.move(Vec3(0, 0, -1))
                if new_slab.end.z < 1 or is_collision(new_slab, new_slabs):
                    break
                slab = new_slab
                moved = True
            if moved:
                fallen += 1
            new_slabs.append(slab)
            # draw(new_slabs)
        self.slabs = new_slabs
        return fallen


def draw(slabs: list[Slab]):
    start = Vec3(
        min(slab.start.x for slab in slabs),
        min(slab.start.y for slab in slabs),
        min(slab.start.z for slab in slabs),
    )
    end = Vec3(
        max(slab.end.x for slab in slabs),
        max(slab.end.y for slab in slabs),
        max(slab.end.z for slab in slabs),
    )
    x_label_pos = (end.x - start.x) // 2
    y_label_pos = (end.x - x_label_pos) + 4 + (end.x - start.x) // 2
    print(" " * x_label_pos + "x" + " " * y_label_pos + "y")
    print(
        "".join(map(str, range(start.x, end.x + 1)))
        + " " * 4
        + "".join(map(str, range(start.y, end.y + 1)))
    )
    for z in range(end.z, 0, -1):
        for x in range(start.x, end.x + 1):
            row = None
            for y in range(start.y, end.y + 1):
                if slab := is_collision(Vec3(x, y, z), slabs):
                    if row == slab.row:
                        continue
                    if row is None:
                        row = slab.row
                    else:
                        row = -1
                        break
            print(row2name(row), end="")
        print(" " * 4, end="")
        for y in range(start.y, end.y + 1):
            row = None
            for x in range(start.x, end.x + 1):
                if slab := is_collision(Vec3(x, y, z), slabs):
                    if row == slab.row:
                        continue
                    if row is None:
                        row = slab.row
                    else:
                        row = -1
                        break
            print(row2name(row), end="")
        z_label = "z" if z == (end.z + 1) // 2 else " "
        print(f" {z} {z_label} ", end="")

        print()
    print("-" * (end.x - start.x + 1) + " " * 4 + "-" * (end.y - start.y + 1) + " 0")


def is_collision(item: Vec3 | Slab, slabs: list[Slab]):
    if isinstance(item, Vec3):
        item = Slab(item, item)
    for slab in slabs:
        start = Vec3(*map(max, zip(item.start, slab.start)))
        end = Vec3(*map(min, zip(item.end, slab.end)))
        # print(item, slab, start, end)
        if all((e_i - s_i) >= 0 for s_i, e_i in zip(start, end)):
            # print("!!!")
            return slab
    # print("Nope")
    return None


def row2name(row: int | None):
    if row is None:
        return "."
    if row == -1:
        return "?"
    return ascii_uppercase[row % len(ascii_uppercase)]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
