"""Day 17: tests"""
from two_steps_forward import DATA, get_allowed_moves, part1, part2


def test_get_allowed_moves():
    assert get_allowed_moves("hijkl", "") == set("UDL")
    assert get_allowed_moves("hijkl", "D") == set("URL")
    assert get_allowed_moves("hijkl", "DR") == set()
    assert get_allowed_moves("hijkl", "DU") == set("R")
    assert get_allowed_moves("hijkl", "DUR") == set()


def test_part1():
    """Part 1 test"""
    assert part1("ihgpwlah") == "DDRRRD"
    assert part1("kglvqrro") == "DDUDRLRRUDRD"
    assert part1("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"
    assert part1(DATA) == "DRDRULRDRD"


def test_part2():
    """Part 2 test"""
    assert part2("ihgpwlah") == 370
    assert part2("kglvqrro") == 492
    assert part2("ulqzkmiv") == 830
    assert part2(DATA) == 384
