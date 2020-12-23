"Day 21 answers"
from typing import Dict, FrozenSet, List, Set

INPUT = "2020/Day 21/input.txt"


def part1(data: List[str]):
    "Part 1 answer"
    vocab: Dict[str, FrozenSet[str]] = {}
    all_ingredients = []
    for line in data:
        food, allergens = line.split(" (contains ")
        if not allergens:
            continue
        allergens = allergens[:-1]
        ingredients = frozenset(food.split(" "))
        all_ingredients.extend(food.split(" "))
        for allergen in allergens.split(", "):
            if allergen in vocab:
                vocab[allergen] &= ingredients
            else:
                vocab[allergen] = ingredients
    possible_allergens: Set[str] = set()
    for value in vocab.values():
        possible_allergens |= value
    return len([i for i in all_ingredients if i not in possible_allergens])


def part2(data):
    "Part 2 answer"
    vocab: Dict[str, FrozenSet[str]] = {}
    for line in data:
        food, allergens = line.split(" (contains ")
        if not allergens:
            continue
        allergens = allergens[:-1]
        ingredients = frozenset(food.split(" "))
        for allergen in allergens.split(", "):
            if allergen in vocab:
                vocab[allergen] &= ingredients
            else:
                vocab[allergen] = ingredients
    while any(len(vocab[k]) > 1 for k in vocab):
        for k in vocab:
            if len(vocab[k]) == 1:
                for i in vocab:
                    if i == k:
                        continue
                    vocab[i] -= vocab[k]

    return ",".join(next(iter(vocab[k])) for k in sorted(vocab))


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split("\n")

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
