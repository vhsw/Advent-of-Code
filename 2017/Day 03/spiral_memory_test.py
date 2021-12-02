"""Day 3: tests"""
from spiral_memory import DATA, part1, part2


def test_part1():
    """Part 1 test"""
    assert part1(1) == 0
    assert part1(12) == 3
    assert part1(23) == 2
    assert part1(1024) == 31
    assert part1(DATA) == 475


def test_part2():
    """Part 2 test"""
    example = """

""".strip().splitlines()
    assert part2(DATA) == 279138
