"""Day 12: tests"""
from hill_climbing_algorithm import DATA, part1, part2

EXAMPLE = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 31
    assert part1(DATA) == 408


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 29
    assert part2(DATA) == 399
