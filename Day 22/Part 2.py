#!/usr/bin/python3
import functools
from collections import namedtuple, deque
import networkx as nx

@functools.lru_cache(maxsize=None)
def get_index(pos, target, depth):
    if pos == target:
        return 0
    x, y = pos
    if x == y == 0:
        return 0
    elif y == 0:
        index = x * 16807
    elif x == 0:
        index = y * 48271
    else:
        index = get_erosion((x-1, y), target, depth) * \
            get_erosion((x, y-1), target, depth)
    return index


def get_erosion(pos, target, depth):
    return (get_index(pos, target, depth) + depth) % 20183


def get_region(pos, target, depth):
    return get_erosion(pos, target, depth) % 3


def dijkstra(source, dest,  target, depth, margin=100):
    Edge = namedtuple('Edge', ('start', 'end', 'weight'))
    graph = nx.Graph()
    # tools: 0 - 👋, 1 - 🔦, 2 - 🔨
    for x in range(dest[0] + margin):
        for y in range(dest[1] + margin):
            region = get_region((x, y), target, depth)
            region_tools = (1, 2), (0, 2), (0, 1)
            allowed_tools = region_tools[region]
            for start_tool in allowed_tools:
                start = x, y, start_tool
                if start_tool == allowed_tools[0]:
                    end_tool = allowed_tools[1]
                else:
                    end_tool = allowed_tools[0]
                end = x, y, end_tool
                graph.add_edge(start, end, weight=7)

                for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    end_x = x + dx
                    end_y = y + dy

                    if 0 <= end_x < dest[0] + margin and 0 <= end_y < dest[1] + margin:
                        end_region = get_region((end_x, end_y), target, depth)
                        if start_tool in region_tools[end_region]:
                            end = end_x, end_y, start_tool
                            graph.add_edge(start, end, weight=1)



    return nx.shortest_path_length(graph, source, dest, 'weight')



def madness(depth, target):
    weight = dijkstra((0, 0, 1), (*target, 1), target, depth, margin=100)
    return weight


assert madness(depth=510, target=(10, 10)) == 45
print(madness(depth=4080, target=(14, 785)))
