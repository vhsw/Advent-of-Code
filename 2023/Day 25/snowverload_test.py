"""Day 25: tests"""

from snowverload import DATA, part1

EXAMPLE = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 54
    assert part1(DATA) == 562912
