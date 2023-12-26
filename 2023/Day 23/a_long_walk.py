"""Day 23: A Long Walk"""
import re
from dataclasses import dataclass
from typing import NamedTuple

import networkx as nx

with open("2023/Day 23/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    maze = Maze.from_str(data)
    G = maze.to_graph()
    return longest_path(G, maze.src.pos, maze.dst.pos)


def part2(data: str):
    """Part 2 solution"""
    return part1(re.sub(r"[<>v\^]", ".", data))


class State(NamedTuple):
    pos: complex
    dir: complex


@dataclass
class Maze:
    src: State
    dst: State
    maze: dict[complex, str]

    slides_dir = {
        ">": 1,
        "<": -1,
        "^": -1j,
        "v": 1j,
    }

    @classmethod
    def from_str(cls, data: str):
        lines = data.splitlines()
        maze: dict[complex, str] = {}
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "#":
                    continue
                pos = complex(col, row)
                if row == 0:
                    src = pos
                if row == len(lines) - 1:
                    dst = pos
                maze[pos] = char
        return cls(State(src, 1j), State(dst, 1j), maze)

    def neighbors(self, item: State):
        for rot in (1, 1j, -1j):
            new_dir = item.dir * rot
            new_pos = item.pos + new_dir
            if char := self.maze.get(new_pos):
                if slide_dir := self.slides_dir.get(char):
                    if slide_dir != new_dir:
                        continue
                    new_pos += slide_dir
                yield State(new_pos, new_dir)

    def cost(self, src: State, dst: State):
        return len(list(crange(src.pos, dst.pos))) - 1

    def to_graph(self):
        graph = nx.DiGraph()
        todo = [(self.src, self.src, 0)]
        seen = set()
        while todo:
            src, dst, weight = todo.pop()
            if (src, dst) in seen:
                continue
            seen.add((src, dst))

            neighbors = list(self.neighbors(dst))
            if len(neighbors) == 1:
                todo.append((src, neighbors[0], weight + self.cost(dst, neighbors[0])))
                continue
            if not neighbors:
                if dst.pos == self.dst.pos:
                    if data := graph.get_edge_data(src.pos, dst.pos):
                        weight = max(weight, data["weight"])

                    graph.add_edge(src.pos, dst.pos, weight=weight)
                continue

            graph.add_edge(src.pos, dst.pos, weight=weight)
            todo.extend(
                (dst, neighbor, self.cost(dst, neighbor)) for neighbor in neighbors
            )
        return graph


def longest_path(graph: nx.DiGraph, src: complex, dst: complex):
    best = 0
    path = set[complex]()

    def dfs(cur, total_len=0):
        if cur == dst:
            nonlocal best
            best = max(best, total_len)
        for neigh, data in graph[cur].items():
            if neigh not in path:
                path.add(neigh)
                dfs(neigh, total_len + data["weight"])
                path.remove(neigh)

    dfs(src)
    return best


def crange(start: complex, end: complex):
    min_r, max_r = sorted(map(int, (start.real, end.real)))
    min_i, max_i = sorted(map(int, (start.imag, end.imag)))
    for real in range(min_r, max_r + 1):
        for imag in range(min_i, max_i + 1):
            yield complex(real, imag)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
