"""Day 16: tests"""
from proboscidea_volcanium import DATA, part1, part2

EXAMPLE = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 1651
    assert part1(DATA) == 2114


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 1707
    assert part2(DATA) == 2666
