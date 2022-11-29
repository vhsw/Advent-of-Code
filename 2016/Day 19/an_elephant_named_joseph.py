"""Day 19: An Elephant Named Joseph"""


with open("2016/Day 19/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    #  https://oeis.org/A006257
    n = int(data)
    a = bin(n)[2:]
    a = a[1:] + a[0]
    return int(a, 2)


# def helper(data)
#     num_elfs = int(data)
#     elfs = {i: 1 for i in range(num_elfs)}
#     # print(elfs)
#     go = True
#     while go:
#         for elf in elfs:
#             if sum(v > 0 for v in elfs.values()) == 1:
#                 go = False
#                 break
#             if elfs[elf] == 0:
#                 continue
#             start = elf + 1
#             if elf == num_elfs:
#                 start = 0
#             for i in range(num_elfs):
#                 v = (start + i) % (num_elfs)
#                 if elfs[v] > 0:
#                     elfs[elf] += elfs[v]
#                     elfs[v] = 0
#                     # print(f"{elf=} takes from {v}")
#                     break
#     for k, v in elfs.items():
#         if v > 0:
#             return k + 1

# >> 1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11,
# >> https://oeis.org/A006257


def part2(data: str):
    """Part 2 solution"""
    # https://oeis.org/A334473

    n = int(data)
    x = highest_power_of_3(n)
    if x == n:
        return x
    return n % x if n < 2 * x else x + 2 * (n % x)


def highest_power_of_3(n: int):
    option = 0
    while 3**option <= n:
        option += 1
    return 3 ** (option - 1)


# def helper2(n):
#     elfs = deque(range(1, n + 1))
#     while len(elfs) > 1:
#         elim = len(elfs) // 2
#         elfs.rotate(-elim)
#         elfs.popleft()
#         elfs.rotate(elim - 1)
#     return elfs[0]

# >> 1 1 3 1 2 3 5 7 9 1 2 3 4 5 6 7 8 9 11 13 15 17 19
# >> https://oeis.org/A334473


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
