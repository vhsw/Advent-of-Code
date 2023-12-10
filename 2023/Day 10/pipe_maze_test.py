"""Day 10: tests"""
from pipe_maze import DATA, part1, part2

EXAMPLE_4_1 = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip()
EXAMPLE_4_2 = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
""".strip()
EXAMPLE_8_1 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip()
EXAMPLE_8_2 = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE_4_1) == 4
    assert part1(EXAMPLE_4_2) == 4
    assert part1(EXAMPLE_8_1) == 8
    assert part1(EXAMPLE_8_2) == 8
    assert part1(DATA) == 6613


AREA_EXAMPLE_4_1 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""".strip()

AREA_EXAMPLE_4_2 = """
..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
""".strip()

AREA_EXAMPLE_8 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip()

AREA_EXAMPLE_10 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip()


def test_part2():
    """Part 2 test"""
    assert part2(AREA_EXAMPLE_4_1) == 4
    assert part2(AREA_EXAMPLE_4_2) == 4
    assert part2(AREA_EXAMPLE_8) == 8
    assert part2(AREA_EXAMPLE_10) == 10
    assert part2(DATA) == 511
