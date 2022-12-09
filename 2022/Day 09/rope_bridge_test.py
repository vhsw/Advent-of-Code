"""Day 9: tests"""
from rope_bridge import DATA, part1, part2

EXAMPLE = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()

EXAMPLE_2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 13
    assert part1(DATA) == 6522


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 1
    assert part2(EXAMPLE_2) == 36
    assert part2(DATA) == 2717
