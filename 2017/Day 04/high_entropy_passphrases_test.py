"""Day 4: tests"""
from high_entropy_passphrases import DATA, no_anagrams, no_duplicates, part1, part2


def test_no_duplicates():
    assert no_duplicates("aa bb cc dd ee")
    assert not no_duplicates("aa bb cc dd aa")
    assert no_duplicates("aa bb cc dd aaa")


def test_part1():
    """Part 1 test"""
    assert part1(DATA) == 386


def test_no_anagrams():
    assert no_anagrams("abcde fghij")
    assert not no_anagrams("abcde xyz ecdab")
    assert no_anagrams("a ab abc abd abf abj")
    assert no_anagrams("iiii oiii ooii oooi oooo")
    assert not no_anagrams("oiii ioii iioi iiio")


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 208
