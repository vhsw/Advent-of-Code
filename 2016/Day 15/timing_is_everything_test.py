"""Day 15: tests"""
from timing_is_everything import DATA, part1, part2

EXAMPLE = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 5
    assert part1(DATA) == 121834


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 3208099
