"""Day 6: tests"""
from memory_reallocation import DATA, part1, part2, redistribute


def test_redistribute():
    assert redistribute([0, 2, 7, 0]) == [2, 4, 1, 2]
    assert redistribute([2, 4, 1, 2]) == [3, 1, 2, 3]
    assert redistribute([3, 1, 2, 3]) == [0, 2, 3, 4]


def test_part1():
    """Part 1 test"""
    assert part1([0, 2, 7, 0]) == 5
    assert part1(DATA) == 12841


def test_part2():
    """Part 2 test"""
    assert part2([0, 2, 7, 0]) == 4
    assert part2(DATA) == 8038
