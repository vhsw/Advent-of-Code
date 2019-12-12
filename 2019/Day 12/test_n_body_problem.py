"""Day N Tests"""

import pytest
from n_body_problem import parse_input, step, period_all, part1, part2


def test_energy():
    data = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
    bodies = parse_input(data)
    for _ in range(10):
        step(bodies)
    assert sum(b.total_energy for b in bodies) == 179


def test_period():
    data = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""
    bodies = parse_input(data)
    period = period_all(bodies)

    assert period == 4686774924


def test_parts():
    assert part1() == 6678
    assert part2() == 496734501382552
