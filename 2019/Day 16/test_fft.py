"""Day 16 Tests"""

import pytest
from fft import part1, part2


def test_parts():
    assert part1() == 11833188
    assert part2() == 55005000
