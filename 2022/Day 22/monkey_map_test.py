"""Day 22: tests"""
from monkey_map import DATA, part1, part2

EXAMPLE = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".strip(
    "\n"
)


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 6032
    assert part1(DATA) == 20494


def test_part2():
    """Part 2 test"""
    # assert part2(EXAMPLE) == 5031
    assert part2(DATA) == 55343
