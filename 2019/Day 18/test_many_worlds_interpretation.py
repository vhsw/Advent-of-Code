"""Day 18 Tests"""

import pytest

from many_worlds_interpretation_part_1 import shortest_path_length as sp1, part1
from many_worlds_interpretation_part_2 import shortest_path_length as sp2, part2


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
    assert sp1(maze) == length


@pytest.mark.parametrize(
    "maze, length",
    [
        [
            """###############
#d.ABC.#.....a#
######...######
######.@.######
######...######
#b.....#.....c#
###############""",
            24,
        ],
        [
            """#############
#DcBa.#.GhKl#
#.###...#I###
#e#d#.@.#j#k#
###C#...###J#
#fEbA.#.FgHi#
#############""",
            32,
        ],
        [
            """#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba...BcIJ#
#####.@.#####
#nK.L...G...#
#M###N#H###.#
#o#m..#i#jk.#
#############""",
            72,
        ],
    ],
)
def test_path_len_2(maze, length):
    assert sp2(maze) == length


def test_parts():
    assert part1() == 0
    assert part2() == 0
