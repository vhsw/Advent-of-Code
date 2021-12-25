"""Day 24: tests"""
from arithmetic_logic_unit import DATA, part1, part2

EXAMPLE = """

""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(DATA) == "96929994293996"


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == "41811761181141"
