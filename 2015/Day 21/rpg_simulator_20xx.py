"Day 21 answers"
from itertools import combinations
from math import ceil

INPUT = "2015/Day 21/input.txt"

# Name, Cost, Damage, Armor
weapons = (
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
)

armors = (
    ("No armor", 0, 0, 0),
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
)
rings = (
    ("No ring 1", 0, 0, 0),
    ("No ring 2", 0, 0, 0),
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
)


def fight(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    player_turns = ceil(player_hp / max(boss_damage - player_armor, 1))
    boss_turns = ceil(boss_hp / max(player_damage - boss_armor, 1))
    return player_turns >= boss_turns


def part1(data):
    "Part 1 answer"
    boss_hp, boss_damage, boss_armor = data
    min_cost = 1000000
    for w in weapons:
        for a in armors:
            for r1, r2 in combinations(rings, 2):
                if fight(
                    player_hp=100,
                    player_damage=w[2] + a[2] + r1[2] + r2[2],
                    player_armor=w[3] + a[3] + r1[3] + r2[3],
                    boss_hp=boss_hp,
                    boss_armor=boss_armor,
                    boss_damage=boss_damage,
                ):
                    min_cost = min(min_cost, w[1] + a[1] + r1[1] + r2[1])
    return min_cost


def part2(data):
    "Part 2 answer"
    boss_hp, boss_damage, boss_armor = data
    max_cost = 0
    for w in weapons:
        for a in armors:
            for r1, r2 in combinations(rings, 2):
                if not fight(
                    player_hp=100,
                    player_damage=w[2] + a[2] + r1[2] + r2[2],
                    player_armor=w[3] + a[3] + r1[3] + r2[3],
                    boss_hp=boss_hp,
                    boss_armor=boss_armor,
                    boss_damage=boss_damage,
                ):
                    max_cost = max(max_cost, w[1] + a[1] + r1[1] + r2[1])
    return max_cost


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = [int(line.split(": ")[1]) for line in fp.read().strip().split("\n")]
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
