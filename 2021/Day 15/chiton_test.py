"""Day 15: tests"""
from chiton import DATA, part1, part2

EXAMPLE = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 40
    assert part1(DATA) == 361


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 315
    assert part2(DATA) == 2838
