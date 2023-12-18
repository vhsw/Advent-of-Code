"""Day 18: tests"""
from lavaduct_lagoon import DATA, part1, part2

EXAMPLE = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 62
    assert part1(DATA) == 52035


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 952408144115
    assert part2(DATA) == 60612092439765
