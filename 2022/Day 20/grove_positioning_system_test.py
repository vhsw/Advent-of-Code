"""Day 20: tests"""
from grove_positioning_system import DATA, part1, part2

EXAMPLE = """
1
2
-3
3
-2
0
4
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 3
    assert part1(DATA) == 7278


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 1623178306
    assert part2(DATA) == 0
