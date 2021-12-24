"""Day 23: Amphipod"""
from dataclasses import dataclass, field
from heapq import heappop, heappush

with open("2021/Day 23/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    val: complex = field(compare=False)


WEIGHT = {"A": 1, "B": 10, "C": 100, "D": 1000}
TARGET = dict(enumerate("ABCD"))
ORDER = {k: v for v, k in enumerate("ABCD")}
ROOM_DOORS = {2, 4, 6, 8}


def part1(data: str):
    """Part 1 solution"""
    rooms = parse(data)
    return move(rooms)


def part2(data: str):
    """Part 2 solution"""
    rooms = parse(data)
    rooms = tuple(
        (r[0], (1, c[0]), (2, c[1]), (3, r[1][1]))
        for r, c in zip(rooms, ("DD", "CB", "BA", "AC"))
    )
    return move(rooms)


# @cache
def move(rooms):
    MAX_DEPTH = len(rooms[0])
    FINAL = tuple(tuple((pos, letter) for pos in range(MAX_DEPTH)) for letter in "ABCD")

    todo = [PrioritizedItem(0, ((), rooms))]
    todo_lookup = {((), rooms)}
    energy = {((), rooms): 0}
    while todo:
        node = heappop(todo).val
        todo_lookup.remove(node)

        hall = dict(node[0])
        rooms = node[1]
        if rooms == FINAL:
            return energy[node]

        for hall_pos, char in hall.items():
            target_hall_pos = (ORDER[char] + 1) * 2
            if no_move(hall, hall_pos, target_hall_pos):
                continue
            new_hall = hall.copy()
            new_hall.pop(hall_pos)
            room_idx = ORDER[char]
            room = rooms[room_idx]
            if not room:
                room = ((MAX_DEPTH - 1, char),)
                steps = abs(hall_pos - target_hall_pos) + MAX_DEPTH

            elif all(c == char for _, c in room):
                target_depth = room[0][0]
                room = ((target_depth - 1, char),) + room
                steps = abs(hall_pos - target_hall_pos) + target_depth
            else:
                continue
            new_rooms = rooms[:room_idx] + (room,) + rooms[room_idx + 1 :]
            new_node = (tuple(new_hall.items()), new_rooms)
            new_energy = energy[node] + steps * WEIGHT[char]
            if new_node in energy and new_energy >= energy[new_node]:
                continue
            energy[new_node] = new_energy
            if new_node not in todo_lookup:
                todo_lookup.add(new_node)
                heappush(
                    todo, PrioritizedItem(heuristic(new_node) + new_energy, new_node)
                )

        for room_idx, room in enumerate(rooms):
            if all(c == "ABCD"[room_idx] for _, c in room):
                continue
            place_idx, char = room[0]
            new_rooms = rooms[:room_idx] + (room[1:],) + rooms[room_idx + 1 :]
            hall_idx = (room_idx + 1) * 2
            for pos in get_placements(hall, hall_idx):
                new_hall = hall.copy()
                new_hall[pos] = char
                steps = abs(pos - hall_idx) + 1 + place_idx

                new_node = (tuple(new_hall.items()), new_rooms)
                new_energy = energy[node] + steps * WEIGHT[char]
                if new_node in energy and new_energy >= energy[new_node]:
                    continue
                energy[new_node] = new_energy
                if new_node not in todo_lookup:
                    todo_lookup.add(new_node)
                    heappush(
                        todo,
                        PrioritizedItem(heuristic(new_node) + new_energy, new_node),
                    )
    return energy[((), FINAL)]


def no_move(hall, src, dst):
    if src < dst:
        return any(p in hall for p in range(src + 1, dst + 1))
    return any(p in hall for p in range(dst, src))


def heuristic(new_node):
    hall, rooms = new_node
    score = 0
    for pos, char in hall:
        target_pos = (ORDER[char] + 1) * 2
        score += abs(pos - target_pos) * WEIGHT[char]
    for room_idx, room in enumerate(rooms):
        for pos, char in room:
            dist = abs(ORDER[char] - room_idx)
            if dist == 0:
                continue
            score += (dist + pos) * WEIGHT[char]
    return score


def get_placements(hall, hall_idx):
    for pos in range(hall_idx - 1, -1, -1):
        if pos in hall:
            break
        if pos in ROOM_DOORS:
            continue
        yield pos
    for pos in range(hall_idx + 1, 11):
        if pos in hall:
            break
        if pos in ROOM_DOORS:
            continue
        yield pos


def parse(data: str):
    lines = data.splitlines()
    rooms = tuple(zip(lines[2][2:-2].split("#"), lines[3].split("#")))
    rooms = rooms[1:-1]

    return tuple(tuple(enumerate(room)) for room in rooms)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
