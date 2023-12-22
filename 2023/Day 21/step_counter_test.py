"""Day 21: tests"""
import pytest
from step_counter import DATA, part1, part2

EXAMPLE = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, steps=6) == 16
    assert part1(DATA) == 3746


@pytest.mark.slow
def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE, steps=6) == 16
    assert part2(EXAMPLE, steps=10) == 50
    assert part2(EXAMPLE, steps=50) == 1594
    assert part2(EXAMPLE, steps=100) == 6536
    assert part2(EXAMPLE, steps=500) == 167004
    assert part2(EXAMPLE, steps=1000) == 668697
    assert part2(EXAMPLE, steps=5000) == 16733044
    assert part2(DATA) == 623540829615589
