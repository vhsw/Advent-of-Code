"""Day 6 Answers"""
import networkx as nx


def total_orbits(orbs: str):
    """The total number of direct and indirect orbits"""
    graph = nx.DiGraph()
    for line in orbs.splitlines():
        src, dst = line.split(")")
        graph.add_edge(src, dst)
    paths_length = nx.single_source_shortest_path_length(graph, "COM")
    return sum(paths_length.values())


def total_transfers(orbs: str):
    """How many orbital transfers you (YOU) need to take to get to Santa (SAN)"""
    graph = nx.DiGraph()
    for line in orbs.splitlines():
        src, dst = line.split(")")
        graph.add_edge(src, dst)
    src, *_ = graph.predecessors("YOU")
    dst, *_ = graph.predecessors("SAN")
    print(src, dst)
    return nx.shortest_path_length(graph.to_undirected(), src, dst)


INPUT = "2019/Day 06/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        result = total_orbits(data.read())
    return result


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        result = total_transfers(data.read())
    return result


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
