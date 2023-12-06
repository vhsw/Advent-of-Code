"""Day 2: Cube Conundrum"""
from math import prod
from typing import NamedTuple

with open("2023/Day 02/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    games = (Game.from_str(line) for line in data.splitlines())
    return sum(game.id for game in games if game.is_valid)


def part2(data: str):
    """Part 2 solution"""
    games = (Game.from_str(line) for line in data.splitlines())

    return sum(game.power for game in games)


class CubeSet(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_str(cls, line: str):
        kwargs = {}
        for set_ in line.split(", "):
            num, color = set_.split(" ")
            kwargs[color] = int(num)
        return cls(**kwargs)

    @property
    def is_valid(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14


class Game(NamedTuple):
    id: int
    cube_sets: tuple[CubeSet, ...]

    @classmethod
    def from_str(cls, line: str):
        game_id, str_sets = line.split(": ")
        id_ = int(game_id.removeprefix("Game "))
        sets = tuple(CubeSet.from_str(line) for line in str_sets.split("; "))
        return cls(id_, sets)

    @property
    def is_valid(self):
        return all(cube_set.is_valid for cube_set in self.cube_sets)

    @property
    def power(self):
        return prod(
            max(cube_set[idx] for cube_set in self.cube_sets) for idx in range(3)
        )


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
