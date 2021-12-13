"""Day 13: tests"""
from transparent_origami import DATA, part1, part2

EXAMPLE = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 17
    assert part1(DATA) == 602


def test_part2():
    """Part 2 test"""
    example = """
#####
#...#
#...#
#...#
#####
""".strip()
    assert part2(EXAMPLE) == example

    ans = """
.##...##..####...##.#..#.####..##..#..#
#..#.#..#.#.......#.#..#....#.#..#.#.#.
#....#..#.###.....#.####...#..#....##..
#....####.#.......#.#..#..#...#....#.#.
#..#.#..#.#....#..#.#..#.#....#..#.#.#.
.##..#..#.#.....##..#..#.####..##..#..#
""".strip()
    assert part2(DATA) == ans
