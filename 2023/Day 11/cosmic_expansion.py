"""Day 11: Cosmic Expansion"""
from itertools import combinations

with open("2023/Day 11/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""

    return find_distances(expand(data))


def part2(data: str, expansion_rate=1_000_000):
    """Part 2 solution"""

    return find_distances(expand(data, expansion_rate))


def parse_galaxies(data: str):
    return {
        complex(col, row)
        for row, line in enumerate(data.splitlines())
        for col, char in enumerate(line)
        if char == "#"
    }


def parse_voids(data: str):
    no_galaxies_rows = [
        row
        for row, line in enumerate(data.splitlines())
        if all(char == "." for char in line)
    ]
    no_galaxies_cols = [
        col
        for col, line in enumerate(zip(*data.splitlines()))
        if all(char == "." for char in line)
    ]
    return no_galaxies_rows, no_galaxies_cols


def expand(data: str, expansion_rate=2):
    galaxies = parse_galaxies(data)
    no_galaxies_rows, no_galaxies_cols = parse_voids(data)
    new_galaxies: set[complex] = set()
    for galaxy in galaxies:
        new_galaxy = galaxy
        for row in no_galaxies_rows:
            if galaxy.imag > row:
                new_galaxy += (expansion_rate - 1) * 1j
        for col in no_galaxies_cols:
            if galaxy.real > col:
                new_galaxy += expansion_rate - 1

        new_galaxies.add(new_galaxy)
    return new_galaxies


def find_distances(galaxies: set[complex]):
    return sum(distance(a, b) for a, b in combinations(galaxies, r=2))


def distance(a: complex, b: complex):
    return int(abs(b.real - a.real) + abs(b.imag - a.imag))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
