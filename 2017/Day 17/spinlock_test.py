"""Day 17: tests"""
from spinlock import DATA, part1, part2

EXAMPLE = "3"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 638
    assert part1(DATA) == 355


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 6154117
