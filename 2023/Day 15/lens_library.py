"""Day 15: Lens Library"""


with open("2023/Day 15/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    return sum(map(hash_algorithm, parse(data)))


def part2(data: str):
    """Part 2 solution"""
    boxes: list[list[tuple[str, int]]] = [[] for _ in range(256)]
    for step in parse(data):
        box_idx, label, focal_length = split(step)
        if focal_length:
            already_in_box = False
            for lens in boxes[box_idx]:
                if lens[0] == label:
                    lens[1] = focal_length
                    already_in_box = True
            if not already_in_box:
                boxes[box_idx].append([label, focal_length])
        else:
            boxes[box_idx] = [lens for lens in boxes[box_idx] if lens[0] != label]
    return sum(
        box_no * slot_no * focal_length
        for box_no, box in enumerate(boxes, start=1)
        for slot_no, (_, focal_length) in enumerate(box, start=1)
    )


def parse(data: str):
    return data.split(",")


def hash_algorithm(data: str):
    current_value = 0
    for char in data:
        code = ord(char)
        current_value += code
        current_value *= 17
        current_value %= 256
    return current_value


def split(step: str):
    match step.split("="):
        case [label, focal_length]:
            return hash_algorithm(label), label, int(focal_length)
        case [label]:
            label = label.removesuffix("-")
            return hash_algorithm(label), label, 0
    raise ValueError(step)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
