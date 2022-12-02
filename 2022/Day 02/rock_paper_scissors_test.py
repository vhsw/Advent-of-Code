"""Day 2: tests"""
from rock_paper_scissors import DATA, part1, part2

EXAMPLE = """
A Y
B X
C Z
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 15
    assert part1(DATA) == 12740


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 12
    assert part2(DATA) == 11980
