"""Day 21: tests"""
from dirac_dice import DATA, part1, part2

EXAMPLE = """
Player 1 starting position: 4
Player 2 starting position: 8
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 739785
    assert part1(DATA) == 752745


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 444356092776315
    assert part2(DATA) == 309196008717909
