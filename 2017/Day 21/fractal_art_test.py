"""Day 21: tests"""
from fractal_art import DATA, part1, part2

EXAMPLE = """
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, 2) == 12
    assert part1(DATA) == 160


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 2271537
