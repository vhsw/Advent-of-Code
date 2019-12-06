"""Day 6 Tests"""

import pytest
from orbit import total_orbits, total_transfers, part1, part2


@pytest.mark.parametrize(
    "orbits, result",
    [
        [
            """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""",
            42,
        ],
    ],
)
def test_total_orbits(orbits, result):
    assert total_orbits(orbits) == result


@pytest.mark.parametrize(
    "orbits, result",
    [
        [
            """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
""",
            4,
        ],
    ],
)
def test_total_transfers(orbits, result):
    assert total_transfers(orbits) == result


def test_parts():
    assert part1() == 301100
    assert part2() == 547
