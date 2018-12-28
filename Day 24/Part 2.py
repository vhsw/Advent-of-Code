#!/usr/bin/env python
import re
import operator


class Group:
    def __init__(self, n_units: int, hp: int, weak: set,
                 immune: set, attak: int, attak_type: str, initiative: int):
        self.n_units = n_units
        self.hp = hp
        self.weak = weak
        self.immune = immune
        self.attak = attak
        self.attak_type = attak_type
        self.initiative = initiative
        self.id = None

    @classmethod
    def from_str(cls, line):
        regex = r'^(\d+) units each with (\d+) hit points (\(.*\) )*with an attack that does (\d+) (\w+) damage at initiative (\d+)$'
        matchhes = re.match(regex, line)
        _n_units, hp, specs, attak, attak_type, initiative = matchhes.groups()
        n_units, hp, attak, initiative = map(
            int, (_n_units, hp, attak, initiative))
        weak = set()
        immune = set()
        if specs:
            specs = specs.replace('(', '').replace(')', '')
            for s in specs.split('; '):
                if s.startswith('weak'):
                    for t in s[7:].split(', '):
                        weak.add(t.strip())
                elif s.startswith('immune'):
                    for t in s[9:].split(', '):
                        immune.add(t.strip())
                else:
                    raise Exception('Wrong spec!')

        return cls(n_units, hp, weak, immune, attak, attak_type, initiative)

    def __str__(self):
        return f'{self.__class__.__name__} contains {self.n_units} units'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.n_units, self.hp, self.weak, self.immune, self.attak, self.attak_type, self.initiative }'

    def __lt__(self, other):
        return (self.effective_power, self.initiative) < (other.effective_power, other.initiative)

    @property
    def effective_power(self) -> int:
        return self.n_units * self.attak

    def estimate_damage(self, other) -> int:
        if self.attak_type in other.immune:
            return 0
        elif self.attak_type in other.weak:
            return self.effective_power * 2
        else:
            return self.effective_power


class Immune(Group):
    pass


class Infection(Group):
    pass


def madness(path, boost):
    with open(path) as f:
        immune_raw, infection_raw = f.read().split('\n\n')
        immune_raw = immune_raw[1:]
        infection_raw = infection_raw[1:]
    immune = [Immune.from_str(line) for line in immune_raw.splitlines()[1:]]
    
    for g in immune:
        g.attak += boost

    infection = [Infection.from_str(line)
                 for line in infection_raw.splitlines()[1:]]

    groups = infection + immune

    for idx, group in enumerate(groups):
        group.id = idx

    def alive(groups):
        immune = sum(1 for group in groups
                     if not isinstance(group, Immune) and group.hp > 0)

        infection = sum(1 for group in groups
                        if not isinstance(group, Infection) and group.hp > 0)
        return immune > 0 and infection > 0

    while alive(groups):
        # print('New round')
        choosen = set()
        pairs = []
        for attaker in sorted(groups, reverse=True):
            enemies = (group for group in groups
                       if not isinstance(group, attaker.__class__)
                       and group.id not in choosen)
            targets = []
            for enemy in enemies:
                damage = attaker.estimate_damage(enemy)
                if damage > 0:
                    targets.append([damage, enemy.effective_power, enemy.initiative, enemy])
            try:
                target = max(targets)[-1]
                pairs.append([attaker, target])
                choosen.add(target.id)
            except ValueError:
                pass
        pairs.sort(reverse=True, key=lambda p: p[0].initiative)
        
        
        total_kills = 0
        for attaker, target in pairs:
            # print(f'{repr(attaker)} attaks {repr(target)}', end='')
            killed = attaker.estimate_damage(target) // target.hp
            if target.n_units < killed:
                killed = target.n_units
            target.n_units -= killed
            total_kills += killed
            # print(f' kills {killed} units')
        if total_kills == 0:
            return -float('inf')
        groups = [g for g in groups if g.n_units > 0]
        
    if all(isinstance(g, Immune) for g in groups):
        return sum(g.n_units for g in groups)
    return -sum(g.n_units for g in groups)


assert madness('Day 24/example.0.txt',1570) == 51

boost = 0
while True:
    res = madness('Day 24/input.txt', boost)
    print(boost, res)
    if res > 0:
        print(boost)
        break
    else:
        boost += 1    