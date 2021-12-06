"""Day 02: tests"""
from corruption_checksum import DATA, part1, part2


def test_part1():
    """Part 1 test"""
    assert part1(DATA) == 21845


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 191
