"""Day 14: Parabolic Reflector Dish"""
from dataclasses import dataclass

with open("2023/Day 14/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    reflector = Reflector.from_str(data)
    reflector.fall()
    return reflector.load_on_north


def part2(data: str):
    """Part 2 solution"""
    reflector = Reflector.from_str(data)
    history: dict[frozenset, int] = {}
    total = 1000000000
    for cycle in range(total):
        frozen_rocks = frozenset(reflector.rocks)
        if prev := history.get(frozen_rocks):
            remain = (total - cycle) % (cycle - prev)
            final_cycle = prev + remain
            for rocks, cycle_no in history.items():
                if cycle_no == final_cycle:
                    reflector.rocks = rocks
                    return reflector.load_on_north
        history[frozen_rocks] = cycle
        reflector.cycle()
    return reflector.load_on_north


@dataclass
class Reflector:
    rows: int
    cols: int
    walls: set[complex]
    rocks: set[complex]

    @classmethod
    def from_str(cls, data: str):
        lines = data.splitlines()
        walls: set[complex] = set()
        rocks: set[complex] = set()
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                pos = complex(col, row)
                match char:
                    case "#":
                        walls.add(pos)
                    case "O":
                        rocks.add(pos)
        return cls(len(lines), len(lines[0]), walls, rocks)

    def fall(self, direction=-1j):
        new_rocks: set[complex] = set()
        for pos in sorted(self.rocks, key=sorter(direction)):
            while True:
                new_pos = pos + direction
                if (
                    new_pos in self.walls
                    or new_pos in new_rocks
                    or not self.in_bounds(new_pos)
                ):
                    new_rocks.add(pos)
                    break
                pos = new_pos

        self.rocks = new_rocks

    def cycle(self):
        for direction in (-1j, -1, 1j, 1):
            self.fall(direction)

    def in_bounds(self, rock: complex):
        return 0 <= rock.real < self.cols and 0 <= rock.imag < self.rows

    @property
    def load_on_north(self):
        return sum(self.rows - int(pos.imag) for pos in self.rocks)

    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pos = complex(col, row)
                if pos in self.walls:
                    print("#", end="")
                    assert pos not in self.rocks
                    continue
                if pos in self.rocks:
                    print("O", end="")
                    continue
                print(".", end="")
            print()
        print()


def sorter(direction: complex):
    def func(val: complex):
        match direction:
            case -1j:
                return val.imag, val.real
            case 1j:
                return -val.imag, val.real
            case -1:
                return val.real, val.imag
            case 1:
                return -val.real, val.imag

    return func


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
