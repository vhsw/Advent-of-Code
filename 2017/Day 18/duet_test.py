"""Day 18: tests"""
from duet import DATA, part1, part2

EXAMPLE = """
set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
""".strip()
EXAMPLE_2 = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 4
    assert part1(DATA) == 8600


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE_2) == 3
    assert part2(DATA) == 7239
