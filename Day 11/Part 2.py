#!/usr/bin/python3


def power(x, y, serial):
    rack_id = x+10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_str = str(power_level).zfill(3)
    power_level = int(power_str[-3])
    power_level -= 5
    return power_level


def create_grid(serial, size=300):
    grid = []
    for i in range(300):
        row = []
        for j in range(size):
            row.append(power(i, j, serial))
        grid.append(row)
    return grid


def largest_power_cell(grid, c_size):
    powers = {}
    g_size = len(grid)

    powers = {}
    for i in range(g_size - c_size + 1):
        for j in range(g_size - c_size + 1):
            cell = [row[j:j+c_size] for row in grid[i:i+c_size]]
            powers[(i, j)] = sum(sum(row) for row in cell)
    pos, val = max(powers.items(), key=lambda i: i[1])
    return pos, val


def largest_total_power(grid):
    powers = {}
    for size in range(1, 300):
        max_cell, val = largest_power_cell(grid, size)
        print(size, val)
        # dirty!
        if val < 0:
            break
        x, y = max_cell
        powers[(x, y, size)] = val
    cell, val = max(powers.items(), key=lambda i: i[1])
    return cell


grid = create_grid(18)
assert(largest_power_cell(grid, 3) == ((33, 45), 29))
assert(largest_total_power(grid) == (90, 269, 16))
grid = create_grid(42)
assert(largest_total_power(grid) == (232, 251, 12))
grid = create_grid(5093)

print(largest_total_power(grid))
