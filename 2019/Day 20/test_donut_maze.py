"""Day 20 Tests"""

import pytest
from donut_maze import part1, part2


def test_parts():
    assert part1() == 620
    assert part2() == 7366
