"Day 16 answers"
INPUT = "2015/Day 16/input.txt"


def part1(data):
    "Part 1 answer"
    known = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".splitlines()
    for line in data:
        n, props = line.strip().split(": ", 1)
        if all(p in known for p in props.split(", ")):
            return n


def cmp(prop, known):
    name, val = prop.split(": ")
    val = int(val)
    if name in ("cats", "trees"):
        return val > known[name]
    if name in ("pomeranians", "goldfish"):
        return val < known[name]
    return known[name] == val


def part2(data):
    "Part 2 answer"
    known = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    for line in data:
        n, props = line.strip().split(": ", 1)
        if all(cmp(prop, known) for prop in props.split(", ")):
            return n


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
