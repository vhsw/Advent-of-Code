"""Day 22: tests"""
from wizard_simulator_20xx import DATA, part1, part2

EXAMPLE = """
Hit Points: 13
Damage: 8
""".strip()

EXAMPLE_2 = """
Hit Points: 14
Damage: 8
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, hp=10, mana=250) == 173 + 53
    assert part1(EXAMPLE_2, hp=10, mana=250) == 229 + 113 + 73 + 173 + 53
    assert part1(DATA) == 953


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 1289
