"""Day 12: tests"""
from digital_plumber import DATA, part1, part2

EXAMPLE = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 6
    assert part1(DATA) == 141


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 2
    assert part2(DATA) == 171
