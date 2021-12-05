"""Day 7: Recursive Circus"""
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Optional


@dataclass
class Node:
    """Graph node"""

    weight: int = 0
    children: tuple[str, ...] = ()
    parent: Optional[str] = None


Graph = dict[str, Node]

with open("2017/Day 07/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    graph = create_graph(data)
    return get_root(graph)


def part2(data: str):
    """Part 2 solution"""
    graph = create_graph(data)
    root = get_root(graph)
    return balance_dfs(graph, root)


def create_graph(data: str):
    graph: DefaultDict[str, Node] = defaultdict(Node)
    regex = r"(\w+) \((\d+)\)(?: -> )?([\w, ]+)?"
    for line in data.splitlines():
        match = re.match(regex, line)
        if not match:
            raise ValueError(line)
        vertex, weight, children = match.groups()
        graph[vertex].weight = int(weight)
        if children:
            graph[vertex].children = tuple(children.split(", "))
            for child in graph[vertex].children:
                graph[child].parent = vertex

    return dict(graph)


def get_root(graph: Graph):
    for name, node in graph.items():
        if not node.parent:
            return name
    raise KeyError


def balance_dfs(graph: Graph, vertex: str):
    weights: dict[str, int] = {}
    todo = [vertex]
    while todo:
        vertex = todo[-1]
        try:
            children_weights = [weights[c] for c in graph[vertex].children]
            if len(set(children_weights)) > 1:
                unbalanced_weight, other_weight = get_balance(children_weights)
                unbalanced_name = graph[vertex].children[
                    children_weights.index(unbalanced_weight)
                ]
                unbalanced_node = graph[unbalanced_name]
                return unbalanced_node.weight - (unbalanced_weight - other_weight)
            weights[vertex] = graph[vertex].weight + sum(children_weights)
            todo.pop()
        except KeyError:
            todo.extend(c for c in graph[vertex].children if c not in todo)


def get_balance(weights):
    """return (wrong weight, other weight)"""
    most_common = Counter(weights).most_common()
    assert len(most_common) == 2
    assert most_common[1][1] == 1
    return most_common[1][0], most_common[0][0]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
