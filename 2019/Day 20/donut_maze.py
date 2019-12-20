"""Day 20 Answers"""
from typing import NamedTuple, Dict, List, Tuple, Optional, Set
from collections import deque
import networkx as nx


class Vec(NamedTuple):
    """2D Vec"""

    line: int
    col: int

    def __add__(self, other):
        return Vec(self.line + other.line, self.col + other.col)


DPOS = (
    Vec(1, 0),
    Vec(-1, 0),
    Vec(0, 1),
    Vec(0, -1),
)


def parse_grid(lines: List[str]) -> Dict[Vec, str]:
    """coordinates of points"""
    grid = {}
    for line, row in enumerate(lines):
        for col, char in enumerate(row):
            if char not in " #":
                src = Vec(line, col)
                grid[src] = char
    return grid


def check_portal(pos: Vec, grid: Dict[Vec, str]) -> Optional[str]:
    """check if this point is portal"""
    for dp in DPOS:
        p1 = pos + dp
        p2 = p1 + dp
        try:
            ch1 = grid[p1]
            ch2 = grid[p2]
            if ch1.isupper() and ch2.isupper():
                return min(ch1, ch2) + max(ch1, ch2)
        except KeyError:
            continue
    return None


def parse_special(
    points: Set[Vec], grid: Dict[Vec, str]
) -> Tuple[Vec, Vec, Dict[str, List[Vec]]]:
    """find entrance, exit and portals in grid"""
    portals: Dict[str, List[Vec]] = {}
    for p in points:
        portal_name = check_portal(p, grid)
        if portal_name:
            if portal_name == "AA":
                start = p
            elif portal_name == "ZZ":
                end = p
            else:
                portals.setdefault(portal_name, []).append(p)
    return start, end, portals


def neighbors(pos):
    """neighbors points"""
    for dp in DPOS:
        dst = pos + dp
        yield dst


def build_graph(points, portals):
    """build nx.Grapg for given points and portals"""
    graph = nx.Graph()
    for src in points:
        for dst in neighbors(src):
            if dst in points:
                graph.add_edge(src, dst)
    for src, dst in portals.values():
        graph.add_edge(src, dst)
    return graph


INPUT = "2019/Day 20/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read()
    lines = data.splitlines()
    grid = parse_grid(lines)
    points = {k for k, v in grid.items() if v == "."}
    entrance, end, portals = parse_special(points, grid)
    graph = build_graph(points, portals)

    return nx.shortest_path_length(graph, entrance, end)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read()
    lines = data.splitlines()
    grid = parse_grid(lines)
    points = {k: v for k, v in grid.items() if v == "."}
    entrance, end, portals = parse_special(points, grid)
    rportals: Dict[Vec, str] = {}
    for name, (p1, p2) in portals.items():
        rportals[p1] = name
        rportals[p2] = name
    max_line = max(p.line for p in rportals)
    max_col = max(p.col for p in rportals)

    queue = deque([(entrance, 0, 0)])  # type: deque[Tuple[Vec, int, int]]
    visited = set([(entrance, 0)])
    while queue:
        pos, distance, lvl = queue.popleft()
        if lvl == 0 and pos == end:
            return distance
        if pos not in points or lvl < 0:
            continue
        for dst in neighbors(pos):
            sl = lvl
            add_dist = 0
            if dst in rportals:
                add_dist += 1
                name = rportals[dst]
                portal_dsts = portals[name]
                if (
                    dst.line == 2
                    or dst.line == max_line
                    or dst.col == 2
                    or dst.col == max_col
                ):
                    sl -= 1
                else:
                    sl += 1
                if portal_dsts[0] == dst:
                    dst = portal_dsts[1]
                else:
                    dst = portal_dsts[0]

            if (dst, sl) not in visited:
                visited.add((dst, sl))
                queue.append((dst, distance + add_dist + 1, sl))


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
