"""Day 6 Tests"""

import pytest
from puzzle import func, part1, part2


@pytest.mark.parametrize(
    "param1, result", [["", ""],],
)
def test_func(param1, result):
    assert func(param1) == result


def test_parts():
    assert part1() == 0
    assert part2() == 0
