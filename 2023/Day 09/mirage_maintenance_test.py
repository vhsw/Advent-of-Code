"""Day 9: tests"""
from mirage_maintenance import DATA, part1, part2

EXAMPLE = """
10 13 16 21 30 45
1 3 6 10 15 21
0 3 6 9 12 15
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 114
    assert part1(DATA) == 1806615041


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 2
    assert part2(DATA) == 1211
