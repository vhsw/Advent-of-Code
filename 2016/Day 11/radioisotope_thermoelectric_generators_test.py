"""Day 11: tests"""
from radioisotope_thermoelectric_generators import DATA, part1, part2

EXAMPLE = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 11
    assert part1(DATA) == 37


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 61
