"""Day 17 Tests"""

import pytest
from set_n_forget import part1, part2


def test_parts():
    assert part1() == 7780
    assert part2() == 1075882
