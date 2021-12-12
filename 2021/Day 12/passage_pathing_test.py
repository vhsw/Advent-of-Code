"""Day 12: tests"""
from passage_pathing import DATA, part1, part2

EXAMPLE = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip()

SLIGHTLY_LARGER_EXAMPLE = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip()

EVEN_LARGER_EXAMPLE = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 10
    assert part1(SLIGHTLY_LARGER_EXAMPLE) == 19
    assert part1(EVEN_LARGER_EXAMPLE) == 226
    assert part1(DATA) == 3576


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 36
    assert part2(SLIGHTLY_LARGER_EXAMPLE) == 103
    assert part2(EVEN_LARGER_EXAMPLE) == 3509
    assert part2(DATA) == 84271
