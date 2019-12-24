"""Day 24 Tests"""

import pytest
from planet_of_discord import part1, part2


def test_parts():
    assert part1() == 23846449
    assert part2() == 1934
