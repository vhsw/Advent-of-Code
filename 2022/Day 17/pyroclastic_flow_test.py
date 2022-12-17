"""Day 17: tests"""
from pyroclastic_flow import DATA, part1, part2

EXAMPLE = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 3068
    assert part1(DATA) == 3127


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 1514285714288
    assert part2(DATA) == 1542941176480
