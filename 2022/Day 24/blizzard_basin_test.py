"""Day 24: tests"""
import pytest
from blizzard_basin import DATA, part1, part2

EXAMPLE = """
#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#
""".strip()

EXAMPLE_2 = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
""".strip()


@pytest.mark.parametrize(
    "data,expected",
    [
        (EXAMPLE, 10),
        (EXAMPLE_2, 18),
        (DATA, 238),
    ],
)
def test_part1(data, expected):
    """Part 1 test"""
    assert part1(data) == expected


@pytest.mark.parametrize(
    "data,expected",
    [
        (EXAMPLE_2, 54),
        (DATA, 751),
    ],
)
def test_part2(data, expected):
    """Part 2 test"""
    assert part2(data) == expected
