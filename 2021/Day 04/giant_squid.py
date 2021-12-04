"""Day 4: Giant Squid"""
import re
from typing import Iterable

with open("2021/Day 04/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    nums, boards = parse(data)
    for num in nums:
        for board in boards:
            for line in board:
                replace(line, num)
            if check(board):
                return num * score(board)
    raise ValueError(data)


def part2(data):
    """Part 2 solution"""
    nums, boards = parse(data)
    board_finished = [False] * len(boards)
    for num in nums:
        for idx, board in enumerate(boards):
            if board_finished[idx]:
                continue
            for line in board:
                replace(line, num)
            if check(board):
                board_finished[idx] = True
                if all(board_finished):
                    return num * score(board)
    raise ValueError(data)


def parse(data: str):
    nums, *boards = data.split("\n\n")
    return parse_nums(nums), parse_boards(boards)


def parse_nums(nums: str):
    return list(map(int, nums.split(",")))


def parse_boards(boards: list[str]):
    return [
        [
            [int(num) for num in re.split(r"\s+", line.strip())]
            for line in board.splitlines()
        ]
        for board in boards
    ]


def replace(line: list[int | None], value: int):
    for idx, _ in enumerate(line):
        if line[idx] == value:
            line[idx] = None


def check(board: list[list[str]]):
    return check_lines(board) or check_lines(zip(*board))


def check_lines(board: Iterable[Iterable[str]]):
    return any(all(num is None for num in line) for line in board)


def score(board):
    return sum(num for line in board for num in line if num)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
