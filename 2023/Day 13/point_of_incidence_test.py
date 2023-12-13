"""Day 13: tests"""
from point_of_incidence import DATA, part1, part2

EXAMPLE = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 405
    assert part1(DATA) == 30518


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 400
    assert part2(DATA) == 36735
