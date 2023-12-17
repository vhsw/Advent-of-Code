"""Day 17: Clumsy Crucible"""
from dataclasses import dataclass, field
from queue import PriorityQueue

with open("2023/Day 17/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, ultra=False):
    """Part 1 solution"""
    graph = Graph.from_str(data)
    src = 0j
    start = UltraCrucible(src) if ultra else Crucible(src)
    dst = complex(len(graph.map[0]) - 1, len(graph.map) - 1)
    _, costs = a_star_search(graph, start, dst)
    # draw(graph, _, costs, src, dst)
    return min_cost(costs, dst)


def part2(data: str):
    """Part 2 solution"""
    return part1(data, ultra=True)


@dataclass(frozen=True)
class Crucible:
    pos: complex
    dir: complex = 1
    straight_steps: int = 0
    min_straight_steps = 1
    max_straight_steps = 3

    def forward(self, steps: int):
        return self.__class__(
            self.pos + self.dir * steps,
            self.dir,
            self.straight_steps + steps,
        )

    def left(self):
        return self.__class__(self.pos, self.dir * 1j, 0)

    def right(self):
        return self.__class__(self.pos, self.dir * -1j, 0)

    def possible_moves(self):
        lo = max(1, self.min_straight_steps - self.straight_steps)
        hi = self.max_straight_steps - self.straight_steps + 1
        for steps in range(lo, hi):
            yield self.forward(steps)
        yield self.left().forward(self.min_straight_steps)
        yield self.right().forward(self.min_straight_steps)


class UltraCrucible(Crucible):
    min_straight_steps = 4
    max_straight_steps = 10


@dataclass
class Graph:
    map: list[list[int]]

    @classmethod
    def from_str(cls, data: str):
        return cls([[int(char) for char in line] for line in data.splitlines()])

    def __contains__(self, point: complex):
        return 0 <= point.imag < len(self.map) and 0 <= point.real < len(self.map[0])

    def neighbors(self, crucible: Crucible):
        for new_crucible in crucible.possible_moves():
            if new_crucible.pos in self:
                yield new_crucible

    def cost(self, src: complex, dst: complex):
        return sum(
            self.map[int(pos.imag)][int(pos.real)]
            for pos in crange(src, dst)
            if pos != src
        )


@dataclass(order=True)
class PrioritizedCrucible:
    priority: int
    item: Crucible = field(compare=False)


def heuristic(a: complex, b: complex):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


def a_star_search(graph: Graph, start: Crucible, dst: complex):
    queue: PriorityQueue[PrioritizedCrucible] = PriorityQueue()
    queue.put(PrioritizedCrucible(0, start))
    came_from: dict[Crucible, Crucible | None] = {start: None}
    cost_so_far = {start: 0}
    while not queue.empty():
        current = queue.get().item
        if current.pos == dst:
            break

        for next_crus in current.possible_moves():
            if next_crus.pos not in graph:
                continue
            new_cost = cost_so_far[current] + graph.cost(current.pos, next_crus.pos)
            if next_crus not in cost_so_far or new_cost < cost_so_far[next_crus]:
                cost_so_far[next_crus] = new_cost
                priority = new_cost + heuristic(next_crus.pos, dst)
                queue.put(PrioritizedCrucible(priority, next_crus))
                came_from[next_crus] = current

    return came_from, cost_so_far


def min_cost(costs: dict[Crucible, int], pos: complex):
    return min(v for k, v in costs.items() if k.pos == pos)


def draw(
    graph: Graph,
    came_from: dict[Crucible, Crucible],
    costs: dict[Crucible, int],
    src: complex,
    dst: complex,
):
    mc = min_cost(costs, dst)
    goal = next(k for k, v in costs.items() if k.pos == dst and v == mc)
    path = reconstruct_path(came_from, Crucible(src), goal)
    dirs = {
        1: ">",
        -1: "<",
        1j: "v",
        -1j: "^",
    }
    carts = {
        item: dirs[src.dir]
        for src, dst in zip(path, path[1:])
        for item in crange(src.pos, dst.pos)
    }
    for row, line in enumerate(graph.map):
        for col, cost in enumerate(line):
            pos = complex(col, row)
            if cart := carts.get(pos):
                print(cart, end="")
                continue
            print(cost, end="")
        print()
    print()


def crange(start: complex, end: complex):
    min_r, max_r = sorted(map(int, (start.real, end.real)))
    min_i, max_i = sorted(map(int, (start.imag, end.imag)))
    for real in range(min_r, max_r + 1):
        for imag in range(min_i, max_i + 1):
            yield complex(real, imag)


def reconstruct_path(came_from: dict[Crucible, Crucible], src: Crucible, dst: Crucible):
    path: list[Crucible] = []
    while dst != src:
        path.append(dst)
        dst = came_from[dst]
    path.append(src)
    path.reverse()
    return path


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
