"""Day 16: The Floor Will Be Lava"""
from dataclasses import dataclass
from typing import Iterable, NamedTuple

with open("2023/Day 16/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""

    return Contraption.from_str(data).bounce()


def part2(data: str):
    """Part 2 solution"""
    contraption = Contraption.from_str(data)
    return max(contraption.bounce(ray) for ray in contraption.edge_rays())


class Ray(NamedTuple):
    pos: complex
    dir: complex


@dataclass
class Item:
    type: str

    def interact(self, ray_dir: complex) -> Iterable[complex]:
        raise NotImplementedError


class Empty(Item):
    def interact(self, ray_dir: complex):
        yield ray_dir


class Mirror(Item):
    def interact(self, ray_dir: complex):
        #     -1j
        #      ^
        #      |
        # 1 -> /

        #     1j
        #      |
        #      v
        # -1 <-/

        #      /-> 1
        #      ^
        #      |
        #     -1j

        #      /<- -1
        #      |
        #      v
        #     1j

        if (self.type == "/" and ray_dir in {1j, -1j}) or (
            self.type == "\\" and ray_dir in {1, -1}
        ):
            yield ray_dir * 1j
        else:
            yield ray_dir * -1j


class Splitter(Item):
    def interact(self, ray_dir: complex):
        if (self.type == "|" and ray_dir in {1, -1}) or (
            self.type == "-" and ray_dir in {1j, -1j}
        ):
            yield ray_dir * 1j
            yield ray_dir * -1j
        else:
            yield ray_dir


@dataclass
class Contraption:
    rows: int
    cols: int
    items: dict[complex, Item]

    @classmethod
    def from_str(cls, data: str):
        lines = data.splitlines()
        items: dict[complex, Item] = {}
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                pos = complex(col, row)
                match char:
                    case ".":
                        items[pos] = Empty(char)
                    case "\\" | "/":
                        items[pos] = Mirror(char)
                    case "|" | "-":
                        items[pos] = Splitter(char)
                    case _:
                        raise ValueError(char)
        return cls(len(lines), len(lines[0]), items)

    def bounce(self, ray=Ray(0 + 0j, 1 + 0j)):
        todo = [ray]
        seen: set[Ray] = set()
        while todo:
            ray = todo.pop()
            if ray in seen:
                continue
            item = self.items.get(ray.pos)
            if item is None:
                continue
            seen.add(ray)
            for new_dir in item.interact(ray.dir):
                new_ray = Ray(ray.pos + new_dir, new_dir)
                todo.append(new_ray)
        return len({ray.pos for ray in seen})

    def edge_rays(self):
        for col in range(self.cols):
            yield Ray(complex(col, 0), 1j)
            yield Ray(complex(col, self.rows - 1), -1j)
        for row in range(self.rows):
            yield Ray(complex(0, row), 1)
            yield Ray(complex(self.cols - 1, row), -1)

    def draw(self, rays_: set[Ray], cur: complex):
        rays: dict[complex, set[complex]] = {}
        for ray in rays_:
            rays.setdefault(ray.pos, set()).add(ray.dir)

        for row in range(self.rows):
            for col in range(self.cols):
                pos = complex(col, row)
                if pos == cur:
                    print("\033[1m", end="")
                try:
                    if item := self.items.get(pos):
                        if item.type != ".":
                            print(item.type, end="")
                            continue
                    if ray_dirs := rays.get(pos):
                        if len(ray_dirs) == 1:
                            char = {1: ">", -1: "<", -1j: "^", 1j: "v"}[ray_dirs.pop()]
                            print(char, end="")
                        else:
                            print(len(ray_dirs), end="")
                        continue
                    print(".", end="")
                finally:
                    if pos == cur:
                        print("\033[0m", end="")

            print()
        print()


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
