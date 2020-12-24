"Day 24 answers"
INPUT = "2020/Day 24/input.txt"


def parse(line):
    idx = 0
    directions = []
    while idx < len(line):
        a = line[idx]
        b = " "
        if idx < len(line) - 1:
            b = line[idx + 1]
        if a + b in ["se", "sw", "nw", "ne"]:
            directions.append(a + b)
            idx += 2
        else:
            directions.append(a)
            idx += 1
    return directions


#   _____         _____         _____
#  /     \       /     \       /     \
# /       \_____/  1,-1 \_____/       \
# \       /     \  nw   /     \       /
#  \_____/  0,-1 \_____/  1, 0 \_____/
#  /     \   w   /     \  ne   /     \
# /       \_____/  0,0  \_____/       \
# \       /     \   #   /     \       /
#  \_____/ -1, 0 \_____/  0, 1 \_____/
#  /     \  se   /     \   e   /     \
# /       \_____/ -1, 1 \_____/       \
# \       /     \  se   /     \       /
#  \_____/       \_____/       \_____/
#        \       /     \       /
#         \_____/       \_____/

MOVES = {
    "nw": (1, -1),
    "ne": (1, 0),
    "w": (0, -1),
    "e": (0, 1),
    "sw": (-1, 0),
    "se": (-1, 1),
}


def move(directions):
    x, y = 0, 0
    for direction in directions:
        dx, dy = MOVES[direction]
        x += dx
        y += dy
    return x, y


def part1(data):
    "Part 1 answer"
    tiles = {}
    for line in data:
        directions = parse(line)
        x, y = move(directions)
        tiles[x, y] = not tiles.setdefault((x, y), True)
    return sum(not t for t in tiles.values())


def part2(data):
    "Part 2 answer"


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split()
    DATA1 = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".strip().split()
    # DATA = ["esenee"]
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
