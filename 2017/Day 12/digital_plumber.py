"""Day 12: Digital Plumber"""
import re

with open("2017/Day 12/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()

REGEX = r"(\d+) <-> ([\d, ]+)"


def part1(data: str):
    """Part 1 solution"""
    graph = create_graph(data)
    todo = graph["0"]
    seen = set()
    while todo:
        node = todo.pop()
        if node in seen:
            continue
        seen.add(node)
        todo.extend(graph[node])
    return len(seen)


def part2(data: str):
    """Part 2 solution"""
    graph = create_graph(data)
    components = 0
    while graph:
        todo = [next(iter(graph))]
        components += 1
        while todo:
            node = todo.pop()
            if node not in graph:
                continue
            todo.extend(graph[node])
            del graph[node]
    return components


def create_graph(data: str):
    graph: dict[str, list[str]] = {}
    for line in data.splitlines():
        match = re.match(REGEX, line)
        if not match:
            raise ValueError(line)
        src, dsts = match.groups()
        graph[src] = dsts.split(", ")
    return graph


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
