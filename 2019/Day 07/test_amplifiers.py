"""Day N Tests"""

import pytest
from amplifiers import part1, part2


def test_parts():
    assert part1() == 116680
    assert part2() == 89603079
