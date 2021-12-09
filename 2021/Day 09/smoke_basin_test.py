"""Day 9: tests"""
from smoke_basin import DATA, part1, part2

EXAMPLE = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 15
    assert part1(DATA) == 494


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 1134
    assert part2(DATA) == 1048128
