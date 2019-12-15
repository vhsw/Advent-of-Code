"""Day 15 Tests"""

import pytest
from oxygen_system import part1, part2


def test_parts():
    assert part1() == 412
    assert part2() == 418
