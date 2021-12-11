"""Day 11: tests"""
from dumbo_octopus import DATA, part1, part2

EXAMPLE = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 1656
    assert part1(DATA) == 1601


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 195
    assert part2(DATA) == 368
