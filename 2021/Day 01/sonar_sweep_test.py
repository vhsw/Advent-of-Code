"""Day 01: tests"""
from sonar_sweep import DATA, part1, part2

EXAMPLE = """
199
200
208
210
200
207
240
269
260
263
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 7
    assert part1(DATA) == 1696


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 5
    assert part2(DATA) == 1737
