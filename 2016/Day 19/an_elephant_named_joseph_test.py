"""Day 19: tests"""
from an_elephant_named_joseph import DATA, part1, part2


def test_part1():
    """Part 1 test"""
    assert part1("5") == 3
    assert part1(DATA) == 1834903


def test_part2():
    """Part 2 test"""
    assert part2("5") == 2
    assert part2(DATA) == 1420280
