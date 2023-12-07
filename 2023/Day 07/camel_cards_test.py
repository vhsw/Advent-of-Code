"""Day 7: tests"""
from camel_cards import DATA, part1, part2

EXAMPLE = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 6440
    assert part1(DATA) == 251545216


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 5905
    assert part2(DATA) == 250384185
