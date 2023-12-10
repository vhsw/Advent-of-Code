"""Day 10: Pipe Maze"""

with open("2023/Day 10/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    maze, start, _ = parse(data)
    return len(dfs(start, maze)) // 2


def part2(data: str):
    """Part 2 solution"""
    maze, start, start_char = parse(data)
    data = data.replace("S", start_char)
    visited = dfs(start, maze)
    area = 0
    for row, line in enumerate(data.splitlines()):
        inside = False
        for col, char in enumerate(line):
            pos = complex(col, row)
            if pos in visited:
                if char in "|LJ":
                    inside = not inside
                continue
            area += inside

    return area


Maze = dict[complex, tuple[complex, ...]]


def parse(data: str):
    maze: Maze = {}
    start = None
    for row, line in enumerate(data.splitlines()):
        for col, char in enumerate(line):
            pos = complex(col, row)
            if char == "S":
                start = pos
                continue
            tiles = parse_tile(char)
            maze[pos] = tuple(tile + pos for tile in tiles)
    if start is None:
        raise ValueError(data)
    start_char, tiles = guess_start(start, maze)
    maze[start] = tiles
    return maze, start, start_char


def parse_tile(char: str) -> tuple[complex, ...]:
    #   -1j
    # -1    1
    #    1j
    return {
        "|": (-1j, 1j),
        "-": (-1, 1),
        "L": (-1j, 1),
        "J": (-1j, -1),
        "7": (-1, 1j),
        "F": (1j, 1),
    }.get(char, ())


def guess_start(pos: complex, maze: Maze):
    for char in "|-LJ7F":
        tiles = tuple(tile + pos for tile in parse_tile(char))
        if all(pos in maze.get(tile, ()) for tile in tiles):
            return char, tiles
    raise ValueError(pos, maze)


def dfs(src: complex, maze: Maze):
    stack = [src]
    visited = {src}

    while stack:
        src = stack.pop()
        visited.add(src)
        stack.extend(neighbour for neighbour in maze[src] if neighbour not in visited)
    return visited


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
