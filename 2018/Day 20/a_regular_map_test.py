"""Day 20: tests"""
from a_regular_map import DATA, part1, part2

EXAMPLE = """

""".strip()


def test_part1():
    """Part 1 test"""
    assert part1("^WNE$") == 3
    assert part1("^ENWWW(NEEE|SSE(EE|N))$") == 10
    assert part1("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$") == 18
    assert part1("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$") == 23
    assert (
        part1("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$") == 31
    )
    assert part1(DATA) == 4432


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 8681
