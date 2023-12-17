"""Day 17: tests"""
from clumsy_crucible import DATA, part1, part2

EXAMPLE = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""".strip()

ANOTHER_EXAMPLE = """
111111111111
999999999991
999999999991
999999999991
999999999991
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 102
    assert part1(DATA) == 791


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 94
    assert part2(ANOTHER_EXAMPLE) == 71
    assert part2(DATA) == 900
