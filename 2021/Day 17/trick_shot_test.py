"""Day 17: tests"""
from trick_shot import DATA, part1, part2

EXAMPLE = "target area: x=20..30, y=-10..-5"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 45
    assert part1(DATA) == 3003


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 112
    assert part2(DATA) == 940
