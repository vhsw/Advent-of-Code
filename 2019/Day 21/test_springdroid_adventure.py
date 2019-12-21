"""Day 21 Tests"""

import pytest
from springdroid_adventure import part1, part2


def test_parts():
    assert part1() == 19358416
    assert part2() == 1144641747
