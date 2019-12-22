"""Day 18 Tests"""

import pytest
from many_worlds_interpretation import shortest_path_length, part1, part2


@pytest.mark.parametrize(
    "maze, length",
    [
        [
            """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################""",
            81,
        ],
    ],
)
def test_path_len(maze, length):
    assert shortest_path_length(maze) == length


def test_parts():
    assert part1() == 0
    assert part2() == 0
