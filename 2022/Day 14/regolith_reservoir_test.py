"""Day 14: tests"""
from regolith_reservoir import DATA, part1, part2

EXAMPLE = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 24
    assert part1(DATA) == 665


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 93
    assert part2(DATA) == 25434
