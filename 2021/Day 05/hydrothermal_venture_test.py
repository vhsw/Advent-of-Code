"""Day 5: tests"""
from hydrothermal_venture import DATA, create_diag_grid, create_grid, draw, part1, part2

EXAMPLE = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip()


def test_part1():
    """Part 1 test"""
    diagram = """
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
""".strip()

    assert draw(create_grid(EXAMPLE)) == diagram
    assert part1(EXAMPLE) == 5
    assert part1(DATA) == 6007


def test_part2():
    """Part 2 test"""
    diagram = """
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
""".strip()
    assert draw(create_diag_grid(EXAMPLE)) == diagram
    assert part2(EXAMPLE) == 12
    assert part2(DATA) == 19349
