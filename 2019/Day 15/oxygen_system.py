"""Day 15 Answers"""
from typing import Dict, NamedTuple
import networkx as nx
from intcode_v15 import Intcode


INPUT = "2019/Day 15/input"


class Point(NamedTuple):
    """2D Point"""

    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Maze:
    def __init__(self, robot: Intcode):
        self.robot = robot
        self.pos = Point(0, 0)
        self.ship: Dict[Point, int] = {}
        self.graph = nx.Graph()
        self.graph.add_node(self.pos)
        dpos = {
            Point(-1, 0): 1,
            Point(1, 0): 2,
            Point(0, -1): 3,
            Point(0, 1): 4,
        }
        self.dpos: Dict[Point, int] = dpos
        self.rdpos: Dict[int, Point] = {v: k for k, v in dpos.items()}

    def move(self, direction):
        res = self.robot.evaluate(direction)
        new_pos = self.pos + self.rdpos[direction]
        assert new_pos not in self.ship
        self.ship[new_pos] = res
        if res > 0:
            self.graph.add_edge(self.pos, new_pos)
            self.pos = new_pos
            self.ship[new_pos] = 2 + direction
        return res

    def search(self, pos: Point, state):
        oxy = None
        for direction in (1, 2, 3, 4):
            new_pos = pos + self.rdpos[direction]
            if new_pos in self.ship:
                continue
            self.pos = pos
            self.robot = state.save_state()
            result = self.move(direction)
            if result == 2:
                return self.pos
            if result == 1:
                if not oxy:
                    oxy = self.search(new_pos, self.robot.save_state())
        return oxy

    def findall(self, pos: Point, state):
        for direction in (1, 2, 3, 4):
            new_pos = pos + self.rdpos[direction]
            if new_pos in self.ship:
                continue
            self.pos = pos
            self.robot = state.save_state()
            result = self.move(direction)
            if result > 0:
                self.findall(new_pos, self.robot.save_state())

    def __str__(self):
        minx = min((k.x for k in self.ship), default=0)
        maxx = max((k.x for k in self.ship), default=0)
        miny = min((k.y for k in self.ship), default=0)
        maxy = max((k.y for k in self.ship), default=0)
        result = []
        for x in range(minx, maxx + 1):
            line = []
            for y in range(miny, maxy + 1):
                tile = "#.O^v<> "[self.ship.get((x, y), 7)]
                if (x, y) == (0, 0):
                    tile = "X"
                if (x, y) == self.pos:
                    tile = "D"
                line.append(tile)
            result.append("".join(line))
        return "\n".join(result)


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    robot = Intcode(code)
    maze = Maze(robot)
    oxy = maze.search(Point(0, 0), maze.robot.save_state())
    return nx.shortest_path_length(maze.graph, Point(0, 0), oxy)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    robot = Intcode(code)
    maze = Maze(robot)
    oxy = maze.search(Point(0, 0), maze.robot.save_state())
    robot = Intcode(code)
    maze = Maze(robot)
    maze.findall(Point(0, 0), maze.robot.save_state())

    return max(nx.single_source_shortest_path_length(maze.graph, oxy).values())


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
