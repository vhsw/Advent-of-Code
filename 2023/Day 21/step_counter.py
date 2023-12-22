"""Day 21: Step Counter"""
from dataclasses import dataclass

import numpy as np

with open("2023/Day 21/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, steps=64):
    """Part 1 solution"""
    maze = Maze.from_str(data)
    return count_reachable(maze, steps)


def part2(data: str, steps=26501365):
    """Part 2 solution"""
    maze = Maze.from_str(data, repeats_infinitely=True)
    if steps <= 5000:
        return count_reachable(maze, steps)
    X = [int(maze.start.real) + maze.side * i for i in range(3)]
    Y = [count_reachable(maze, x) for x in X]
    poly = np.polyfit(X, Y, deg=2)
    return int(np.polyval(poly, steps))


@dataclass
class Maze:
    start: complex
    side: int
    _maze: set[complex]
    _repeats_infinitely: bool

    @classmethod
    def from_str(cls, data: str, repeats_infinitely=False):
        maze: set[complex] = set()
        for row, line in enumerate(data.splitlines()):
            for col, char in enumerate(line):
                pos = complex(col, row)
                if char != "#":
                    maze.add(pos)
                if char == "S":
                    start = pos
        return cls(
            start,
            row + 1,  # pylint: disable=undefined-loop-variable
            maze,
            repeats_infinitely,
        )

    def __contains__(self, item: complex):
        if self._repeats_infinitely:
            item = complex(item.real % self.side, item.imag % self.side)
        return item in self._maze


def count_reachable(maze: Maze, steps: int):
    positions = {maze.start}
    for _ in range(steps):
        new_positions: set[complex] = set()
        for pos in positions:
            for d_pos in (1, -1, 1j, -1j):
                new_pos = pos + d_pos
                if new_pos in maze:
                    new_positions.add(new_pos)
        positions = new_positions
    return len(positions)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
