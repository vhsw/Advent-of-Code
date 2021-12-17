"""Day 24: tests"""
from electromagnetic_moat import DATA, part1, part2

EXAMPLE = """
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 31
    assert part1(DATA) == 1859


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 19
    assert part2(DATA) == 1799
