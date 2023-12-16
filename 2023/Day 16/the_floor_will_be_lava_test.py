"""Day 16: tests"""
from the_floor_will_be_lava import DATA, part1, part2

EXAMPLE = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 46
    assert part1(DATA) == 7562


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 51
    assert part2(DATA) == 7793
