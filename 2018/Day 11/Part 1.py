#!/usr/bin/env python


def power(x, y, serial):
    rack_id = x+10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_str = str(power_level).zfill(3)
    power_level = int(power_str[-3])
    power_level -= 5
    return power_level

def largest_total_power(serial):
    grid = []
    for i in range(300):
        row = []
        for j in range(300):
            row.append(power(i,j, serial))
        grid.append(row)
    powers = {}
    for i in range(300-2):
        for j in range(300-2):
            res = sum(grid[i][j:j+3])
            res += sum(grid[i+1][j:j+3])
            res += sum(grid[i+2][j:j+3])
            powers[(i,j)] = res
    pos, _ = max(powers.items(), key=lambda i: i[1])
    return pos

assert power(3, 5, 8) == 4
assert power(122, 79, 57) == -5
assert power(217, 196, 39) == 0
assert power(101, 153, 71) == 4
assert largest_total_power(18) == (33,45)
print(largest_total_power(5093))
