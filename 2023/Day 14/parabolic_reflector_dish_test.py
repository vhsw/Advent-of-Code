"""Day 14: tests"""
from parabolic_reflector_dish import DATA, part1, part2

EXAMPLE = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 136
    assert part1(DATA) == 109424


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 64
    assert part2(DATA) == 102509
