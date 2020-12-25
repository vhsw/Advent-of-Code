"Day 25 answers"
INPUT = "2020/Day 25/input.txt"


def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value


def find_loop_size(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value *= 7
        value %= 20201227
        loop_size += 1
    return loop_size


def part1(data):
    "Part 1 answer"
    card_loop_size = find_loop_size(data[0])
    door_loop_size = find_loop_size(data[1])
    key = transform(data[1], card_loop_size)
    assert key == transform(data[0], door_loop_size)
    return key


def part2(data):
    "Part 2 answer"


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = list(map(int, fp.read().strip().split()))
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
