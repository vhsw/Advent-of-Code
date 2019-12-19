"""Day 17 Tests"""

import pytest
from tractor_beam import part1, part2


def test_parts():
    assert part1() == 176
    assert part2() == 6751081
