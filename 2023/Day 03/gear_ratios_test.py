"""Day 3: tests"""
from gear_ratios import DATA, part1, part2

EXAMPLE = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 4361
    assert part1(DATA) == 509115


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 467835
    assert part2(DATA) == 75220503
