"""Day 23: tests"""
from unstable_diffusion import DATA, part1, part2

SMALL_EXAMPLE = """
.....
..##.
..#..
.....
..##.
.....
""".strip()
EXAMPLE = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(SMALL_EXAMPLE) == 5 * 6 - 5
    assert part1(EXAMPLE) == 110
    assert part1(DATA) == 3788


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 20
    assert part2(DATA) == 921
