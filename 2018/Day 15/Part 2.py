#!/usr/bin/env python
from collections import deque

class UnitDied(Exception):
    pass

class ElfDied(UnitDied):
    pass

class Unit:
    def __init__(self, x, y, attack_power=3, health=200):
        self.x = x
        self.y = y
        self.attack_power = attack_power
        self._health = health
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value <= 0:
            self._health = 0
            raise UnitDied(self)
        else:
            self._health = value

    @property
    def coords(self):
        return self.x, self.y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.attack_power}, {self.health})'

    def __eq__(self, other):
        return self.coords == other.coords

    def move(self, x, y):
        self.x = x
        self.y = y

    def attack(self, other):
        other.health = other.health - self.attack_power

    def __sub__(self, other):
        return (abs(self.x - other.x) + abs(self.y - other.y))


class Elf(Unit):
    pass
    def __str__(self):
        return f'E({self.health})'



class Goblin(Unit):
    pass

    def __str__(self):
        return f'G({self.health})'

class Board:
    def __init__(self, data, elf_power):
        self.grid = []
        self._units = []
        for i in range(len(data)):
            row = []
            for j in range(len(data[0])):
                if data[i][j] == 'E':
                    self._units.append(Elf(i, j, elf_power))
                elif data[i][j] == 'G':
                    self._units.append(Goblin(i, j))

                if data[i][j] == '#':
                    row.append('#')
                else:
                    row.append('.')
            self.grid.append(row)

        walls = []
        for i, line in enumerate(self.grid):
            for j, element in enumerate(line):
                if element == '#':
                    walls.append((i, j))
        self.walls = set(walls)

    @property
    def units(self):
        units = (u for u in self._units if u.health > 0)
        return sorted(units, key=lambda u: (u.x, u.y))

    def get_targets(self, unit):
        return set(other.coords for other in self.units if type(unit) != type(other))

    def obstacles(self, unit):
        other_units = set(
            other.coords for other in self.units if other != unit)
        return self.walls.union(other_units)

    def __repr__(self):
        res = []
        units = {(u.x, u.y): ('G' if isinstance(u, Goblin)
                              else 'E') + f'({u.health})' for u in self.units}
        for i in range(len(self.grid)):
            row = []
            stats = []
            for j in range(len(self.grid[0])):
                if (i, j) in units:
                    row.append(units[(i, j)][0])
                    stats.append(units[(i, j)])
                else:
                    row.append(self.grid[i][j])
            res.append(''.join(row) + '   ' + ', '.join(stats))
        return '\n'.join(res) + '\n'

    def get_closest(self, u):
        targets = self.get_targets(u)
        obstacles = self.obstacles(u)
        previous = {}
        distance = {}

        to_visit = deque()
        for (dx, dy) in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            new_coords = u.coords[0] + dx, u.coords[1] + dy
            # if new_coords not in self.walls:
            to_visit.append(new_coords)
            previous[new_coords] = u.coords
            distance[new_coords] = 1

        closest = None
        while to_visit:
            coords = to_visit.popleft()

            if coords in targets:
                closest = coords
                break

            if coords in obstacles:
                continue

            for (dx, dy) in ((-1, 0), (0, -1), (0, +1), (+1, 0)):
                new_coords = coords[0] + dx, coords[1] + dy
                if new_coords == (3, 15):
                    pass
                if new_coords not in previous:
                    previous[new_coords] = coords
                    distance[new_coords] = distance[coords] + 1
                    to_visit.append(new_coords)

        if closest is None:
            return None, -1

        position = closest
        next_move = previous[closest]
        # _dist = 0
        trace = [next_move]
        while next_move != u.coords:
            # _dist += 1
            trace.append(next_move)
            position = next_move
            next_move = previous[position]
        # print(trace)
        # print(u, distance[closest], closest)
        return position, distance[closest]

    def get_neighbour_enemies(self, unit):
        x, y = unit.coords
        neighbours = []
        for (dx, dy) in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            new_coord = x + dx, y + dy
            for other in self.units:
                if new_coord == other.coords:
                    if not isinstance(other, unit.__class__):
                        neighbours.append(other)
        return neighbours

    def step(self):
        move_success = False
        for u in self.units:
            if u.health <= 0:
                continue
            coord, distance = self.get_closest(u)
            if distance > 1:
                u.move(*coord)
                distance -= 1
            if distance == 1:
                targets = self.get_neighbour_enemies(u)
                selected_target = min(targets, key=lambda t: t.health)
                try:
                    u.attack(selected_target)
                except UnitDied as e:
                    unit = e.args[0]
                    if isinstance(unit, Elf):
                        raise ElfDied
            move_success = move_success or coord is not None
        return move_success

def madness(path, elf_power):
    with open(path) as f:
        raw_data = f.read().splitlines()
    board = Board(raw_data, elf_power)
    step = -1
    while board.step():
        step += 1
        # print(step)
        # print(board)
        # import time
        # time.sleep(0.05)

    return sum(u.health for u in board.units) * step


elf_power = 4
while True:
    try:
        print(madness('Day 15/input.txt', elf_power))
        break
    except ElfDied:
        elf_power += 1
        print(f'Elf died, setting power to {elf_power}')