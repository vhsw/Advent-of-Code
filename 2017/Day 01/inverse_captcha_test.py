"""Day 1: tests"""
from inverse_captcha import DATA, part1, part2


def test_part1():
    """Part 1 test"""
    assert part1(DATA) == 1343


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 1274
