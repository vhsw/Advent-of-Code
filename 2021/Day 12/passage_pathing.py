"""Day 12: Passage Pathing"""
from collections import defaultdict

with open("2021/Day 12/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    graph = parse(data)

    def traverse(src: str, path: frozenset[str] = frozenset()):
        if src == "END":
            yield path
            return
        for node in graph[src]:
            if node.isupper():
                yield from traverse(node, path)
                continue
            if node in path:
                continue
            yield from traverse(node, path | {node})

    return len(list(traverse("START")))


def part2(data: str):
    """Part 2 solution"""
    graph = parse(data)

    def traverse(src: str, path: frozenset[str] = frozenset(), bonus: str = ""):
        if src == "END":
            yield path
            return
        for node in graph[src]:
            if node.isupper():
                yield from traverse(node, path, bonus)
                continue
            if node in path:
                if not bonus:
                    yield from traverse(node, path, node)
                continue
            yield from traverse(node, path | {node}, bonus)

    return len(list(traverse("START")))


def parse(data: str):
    data = data.replace("start", "START").replace("end", "END")
    graph: dict[str, set[str]] = defaultdict(set)
    for line in data.splitlines():
        src, dst = line.split("-")
        if src != "END" and dst != "START":
            graph[src].add(dst)
        if dst != "END" and src != "START":
            graph[dst].add(src)
    return dict(graph)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
