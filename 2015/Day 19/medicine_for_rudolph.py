"""Day 19: Medicine for Rudolph"""
import re
from collections import defaultdict

with open("2015/Day 19/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    repls, molecule = parse(data)
    s = set()
    for idx, atom in enumerate(molecule):
        for dst in repls.get(atom, ()):
            new_molecule = molecule[:idx] + dst + molecule[idx + 1 :]
            s.add(new_molecule)
    return len(s)


# Not with 2022 PC
#
# def part2(data: str):
#     """Part 2 solution"""
#     repls, target = parse(data)
#     todo = deque([(("e",), 0)])
#     seen = set()
#     while todo:
#         molecule, steps = todo.popleft()
#         if molecule == target:
#             return steps
#         if molecule in seen:
#             continue
#         seen.add(molecule)
#         for idx, atom in enumerate(molecule):
#             for dst in repls.get(atom, ()):
#                 new_molecule = molecule[:idx] + dst + molecule[idx + 1 :]
#                 todo.append((new_molecule, steps + 1))


def part2(data: str):
    """Part 2 solution"""
    repls, target = parse(data)
    sources = {"".join(s) for s in repls["e"]}
    r_repls = reverse_repls(repls)
    target = "".join(target)
    pair_rules, other_rules = split_rules(r_repls)
    todo = [(target, 0)]
    while todo:
        molecule, steps = todo.pop()
        if molecule in sources:
            return steps + 1
        for src, dst in pair_rules.items():
            new_molecule = molecule.replace(src, dst, 1)
            if new_molecule != molecule:
                todo.append((new_molecule, steps + 1))
        for src, dst in other_rules.items():
            new_molecules = []
            for idx in find_all(molecule, src):
                new_molecule = molecule[:idx] + dst + molecule[idx + len(src) :]
                new_molecules.append((new_molecule, steps + 1))
            new_molecules.sort(key=lambda i: len(i[0]))
            todo.extend(new_molecules)


def split_rules(rules):
    pair_rules = {}
    other = {}
    for k, v in rules.items():
        if len(split_atoms(k)) == 2:
            pair_rules[k] = v
            continue
        other[k] = v
    return pair_rules, other


def parse(data: str):
    repls, molecule = data.split("\n\n")
    return parse_repls(repls), split_atoms(molecule)


def parse_repls(data: str):
    repls = defaultdict(list)
    for line in data.splitlines():
        src, dst = line.split(" => ")
        atoms = split_atoms(dst)
        repls[src].append(atoms)
    return {k: tuple(v) for k, v in repls.items()}


def split_atoms(data: str):
    return tuple(re.findall(r"([A-Z][a-z]?|e)", data))


def reverse_repls(repls: dict[str, tuple[str, ...]]):
    r_repls = {}
    for src, dsts in repls.items():
        for dst in dsts:
            if src != "e":
                k = "".join(dst)
                r_repls[k] = src
    return {k: r_repls[k] for k in sorted(r_repls, key=len, reverse=True)}


def find_all(haystack: str, needle: str):
    start = 0
    while True:
        start = haystack.find(needle, start)
        if start == -1:
            return
        yield start
        start += 1


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
