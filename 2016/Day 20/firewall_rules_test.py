"""Day 20: tests"""
from firewall_rules import DATA, merge, parse, part1, part2

EXAMPLE = """
5-8
0-2
4-7
""".strip()


def test_merge():
    assert merge([(6, 8), (1, 9), (2, 4), (4, 7)]) == [(1, 9)]
    assert merge([(1, 3), (2, 4), (6, 8), (9, 10)]) == [(1, 4), (6, 8), (9, 10)]
    assert merge(parse(EXAMPLE)) == [(0, 2), (4, 8)]


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, max_num=9) == 3
    assert part1(DATA) == 4793564


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE, max_num=9) == 2
    assert part2(DATA) == 146
