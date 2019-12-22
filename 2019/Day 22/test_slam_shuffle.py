"""Day N Tests"""

import pytest
from collections import deque
from slam_shuffle import part1, part2, shuffle


@pytest.mark.parametrize(
    "example",
    [
        """deal with increment 7
deal into new stack
deal into new stack
Result: 0 3 6 9 2 5 8 1 4 7""",
        """cut 6
deal with increment 7
deal into new stack
Result: 3 0 7 4 1 8 5 2 9 6""",
        """deal with increment 7
deal with increment 9
cut -2
Result: 6 3 0 7 4 1 8 5 2 9""",
        """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
Result: 9 2 5 8 1 4 7 0 3 6""",
    ],
)
def test_shuffle(example):
    *commands, res = example.splitlines()
    res = res[8:]
    test_deq = deque(int(i) for i in res.split())
    assert shuffle(commands, deck_size=10) == test_deq


def test_parts():
    assert part1() == 0
    assert part2() == 0
