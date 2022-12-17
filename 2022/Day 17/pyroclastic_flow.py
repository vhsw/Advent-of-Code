"""Day 17: Pyroclastic Flow"""
from itertools import cycle, islice

with open("2022/Day 17/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    moves = cycle(parse(data))
    pool = figures()
    field = {complex(0, i) for i in range(7)}
    max_height = 0
    for figure in islice(cycle(pool), 0, 2022):
        drop_height = max_height + 4
        figure = move(figure, complex(drop_height, 2))
        for d_pos in moves:
            new_figure = move(figure, d_pos)
            if (not is_wall_collision(new_figure)) and (
                not is_field_collision(new_figure, field)
            ):
                figure = new_figure

            new_figure = drop(figure)
            if is_field_collision(new_figure, field):
                break
            figure = new_figure

        field.update(figure)
        max_height = max(max_height, max(int(pos.real) for pos in figure))
    return max_height


def part2(data: str, size=1000000000000):
    """Part 2 solution"""
    moves = parse(data)
    moves_cycle = cycle(moves)
    pool = figures()
    field = {complex(0, i) for i in range(7)}
    max_height = 0
    history = []
    for figure in cycle(pool):
        drop_height = max_height + 4
        figure = move(figure, complex(drop_height, 2))
        for d_pos in moves_cycle:
            new_figure = move(figure, d_pos)
            if (not is_wall_collision(new_figure)) and (
                not is_field_collision(new_figure, field)
            ):
                figure = new_figure

            new_figure = drop(figure)
            if is_field_collision(new_figure, field):
                break
            figure = new_figure

        field.update(figure)
        delta = max(max_height, max(int(pos.real) for pos in figure)) - max_height
        history.append(delta)
        for period in range(2, len(history) // 3):
            slices = [
                history[offset : offset + period]
                for offset in range(0, len(history) - period, period)
            ]
            if all(len(set(values)) == 1 for values in zip(*slices[1:])):
                step = sum(history[period : 2 * period])
                full_steps, remain = divmod(size, period)
                return (
                    sum(history[:period])
                    + step * (full_steps - 1)
                    + sum(history[period : period + remain])
                )
        max_height = max(max_height, max(int(pos.real) for pos in figure))


def parse(data: str):
    moves = {
        ">": 1j,
        "<": -1j,
    }
    return [moves[char] for char in data]


def figures():
    h_bar = (0 + 0j, 0 + 1j, 0 + 2j, 0 + 3j)
    cross = (2 + 1j, 1 + 0j, 1 + 1j, 1 + 2j, 0 + 1j)
    l_shape = (2 + 2j, 1 + 2j, 0 + 0j, 0 + 1j, 0 + 2j)
    v_bar = (0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j)
    box = (0 + 0j, 0 + 1j, 1 + 0j, 1 + 1j)
    return (h_bar, cross, l_shape, v_bar, box)


def move(figure, d_pos):
    return tuple(pos + d_pos for pos in figure)


def drop(figure):
    return tuple(pos - 1 for pos in figure)


def is_wall_collision(figure):
    return any(pos.imag < 0 or pos.imag >= 7 for pos in figure)


def is_field_collision(figure, field):
    return any(pos in field for pos in figure)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
