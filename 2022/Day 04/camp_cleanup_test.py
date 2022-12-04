"""Day 4: tests"""
from camp_cleanup import DATA, part1, part2

EXAMPLE = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 2
    assert part1(DATA) == 431


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 4
    assert part2(DATA) == 823
