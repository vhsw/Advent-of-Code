"""Day 24: Electromagnetic Moat"""
from functools import cache

with open("2017/Day 24/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    graph = parse(data)
    max_w = 0

    @cache
    def search(cur, graph, w=0):
        for i in range(len(graph)):
            a, b = graph[i]
            if a == cur:
                sub_g = graph[:i] + graph[i + 1 :]
                search(b, sub_g, w + a + b)
            if b == cur:
                sub_g = graph[:i] + graph[i + 1 :]
                search(a, sub_g, w + a + b)
        nonlocal max_w
        max_w = max(max_w, w)

    search(0, graph)
    return max_w


def part2(data: str):
    """Part 2 solution"""
    graph = parse(data)
    max_w = 0
    max_l = 0

    @cache
    def search(cur, graph, w=0, l=0):
        for i in range(len(graph)):
            a, b = graph[i]
            if a == cur:
                sub_g = graph[:i] + graph[i + 1 :]
                search(b, sub_g, w + a + b, l + 1)
            if b == cur:
                sub_g = graph[:i] + graph[i + 1 :]
                search(a, sub_g, w + a + b, l + 1)
        nonlocal max_w, max_l
        if l >= max_l:
            max_l = l
            max_w = max(max_w, w)

    search(0, graph)
    return max_w


def parse(data: str):
    graph = []
    for line in data.splitlines():
        port_a, port_b = map(int, line.split("/"))
        graph.append((port_a, port_b))
    return tuple(graph)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
