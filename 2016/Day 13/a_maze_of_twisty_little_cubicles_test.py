"""Day 13: tests"""
from a_maze_of_twisty_little_cubicles import DATA, part1, part2

EXAMPLE = "10"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, target=7 + 4j) == 11
    assert part1(DATA) == 0


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 124
