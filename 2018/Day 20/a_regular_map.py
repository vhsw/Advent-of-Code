"""Day 20: A Regular Map"""
import networkx as nx

with open("2018/Day 20/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    G = parse(data)
    pathes = nx.single_source_shortest_path(G, 0)
    return max(map(len, pathes.values())) - 1


def part2(data: str):
    """Part 2 solution"""
    G = parse(data)
    pathes = nx.single_source_shortest_path(G, 0)
    return sum(len(p) > 1000 for p in pathes.values())


def parse(data: str):
    lookup = {
        "N": -2,
        "S": 2,
        "W": -2j,
        "E": 2j,
    }
    G = nx.Graph()
    # ^N(W|E)S$
    stack = [(0j, data)]
    level_starts = []
    while stack:
        # print(stack)
        (src, data) = stack.pop()
        head, tail = data[0], data[1:]
        if head == "$":
            return G
        if head == "^":
            stack.append((src, tail))
            continue
        if head in lookup:
            dst = src + lookup[head]
            G.add_edge(src, dst)
            stack.append((dst, tail))
            continue
        if head == "(":
            level_starts.append(src)
            stack.append((src, tail))
            continue
        if head == "|":
            src = level_starts[-1]
            stack.append((src, tail))
            continue
        if head == ")":
            level_starts.pop()
            stack.append((src, tail))
            continue


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
