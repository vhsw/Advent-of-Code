"""Day 6: tests"""
import pytest
from wait_for_it import DATA, part1, part2

EXAMPLE = """
Time:      7  15   30
Distance:  9  40  200
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 288
    assert part1(DATA) == 1312850


@pytest.mark.skip  # slow
def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 71503
    assert part2(DATA) == 36749103
