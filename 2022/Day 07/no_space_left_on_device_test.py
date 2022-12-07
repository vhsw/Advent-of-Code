"""Day 7: tests"""
from no_space_left_on_device import DATA, part1, part2

EXAMPLE = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 95437
    assert part1(DATA) == 1367870


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 24933642
    assert part2(DATA) == 549173
