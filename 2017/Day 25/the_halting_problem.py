"""Day 25: The Halting Problem"""
import re
from collections import defaultdict

with open("2017/Day 25/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    head, *text_states = data.split("\n\n")
    states = dict(parse_state(state) for state in text_states)
    state, diagnostic_steps = parse_head(head)
    tape = defaultdict(int)
    cursor = 0
    for _ in range(diagnostic_steps):
        write, move, state = states[state][tape[cursor]]
        tape[cursor] = write
        cursor += move
    return sum(tape.values())


def parse_head(data: str):
    lines = data.splitlines()
    state = s_match(r"Begin in state ([A-Z]).", lines[0])[1]
    steps = s_match(r"Perform a diagnostic checksum after (\d+) steps.", lines[1])[1]

    return state, int(steps)


def parse_state(data: str):
    lines = data.splitlines()
    name = s_match(r"In state ([A-Z]):", lines[0])[1]
    return name, dict(parse_instr("\n".join(lines[i : i + 4])) for i in range(1, 9, 4))


def parse_instr(lines: str):
    regex = r"""
  If the current value is (\d):
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state ([A-Z])."""
    match = s_match(regex.strip("\n"), lines)
    condition, write_val, text_move, next_state = match.groups()
    move = 1 if text_move == "right" else -1
    return int(condition), (int(write_val), move, next_state)


def s_match(regex: str, data: str):
    match = re.match(regex, data)
    if not match:
        raise ValueError(regex, data)
    return match


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
