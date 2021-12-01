"""Day 01 tests"""
from sonar_sweep import DATA, part1, part2


def test_part1():
    """Part 1 test"""
    example = """
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
""".strip().splitlines()
    assert part1(example) == 7
    assert part1(DATA) == 1696


def test_part2():
    """Part 2 test"""
    example = """
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
""".strip().splitlines()
    assert part2(example) == 5
    assert part2(DATA) == 1737
