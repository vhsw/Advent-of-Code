"""Day 24: tests"""

from never_tell_me_the_odds import DATA, part1, part2

EXAMPLE = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, bounds=(7, 27)) == 2
    assert part1(DATA) == 26611


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 47
    assert part2(DATA) == 0
