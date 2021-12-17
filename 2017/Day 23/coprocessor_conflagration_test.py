"""Day 23: tests"""
from coprocessor_conflagration import DATA, part1, part2

EXAMPLE = """

""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(DATA) == 4225


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 905
