"""Day 20: tests"""
from particle_swarm import DATA, part1, part2

EXAMPLE = """
p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 0
    assert part1(DATA) == 243


EXAMPLE_2 = """
p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
""".strip()


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE_2) == 1
    assert part2(DATA) == 648
