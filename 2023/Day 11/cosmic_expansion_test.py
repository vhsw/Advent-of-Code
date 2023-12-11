"""Day 11: tests"""
from cosmic_expansion import DATA, distance, part1, part2

EXAMPLE = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip()


def test_distance():
    assert distance(4 + 0j, 9 + 10j) == 15
    assert distance(0 + 2j, 12 + 7j) == 17


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 374
    assert part1(DATA) == 10276166


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE, 10) == 1030
    assert part2(EXAMPLE, 100) == 8410
    assert part2(DATA) == 598693078798
