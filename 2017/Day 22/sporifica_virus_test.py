"""Day 22: tests"""
from sporifica_virus import DATA, part1, part2

EXAMPLE = """
..#
#..
...
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, steps=70) == 41
    assert part1(EXAMPLE) == 5587
    assert part1(DATA) == 5462


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE, steps=100) == 26
    assert part2(EXAMPLE) == 2511944
    assert part2(DATA) == 2512135
