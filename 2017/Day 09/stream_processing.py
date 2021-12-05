"""Day 9: Stream Processing"""
with open("2017/Day 09/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data):
    """Part 1 solution"""
    score = 0
    level = 0
    skip = False
    garbage = False
    for char in data:
        if skip:
            skip = False
            continue
        if garbage:
            match char:
                case "!":
                    skip = True
                case ">":
                    garbage = False
        else:
            match char:
                case "<":
                    garbage = True
                case "{":
                    level += 1
                    score += level
                case "}" :
                    assert level > 0
                    level -= 1
    return score


def part2(data):
    """Part 2 solution"""
    characters = 0
    level = 0
    skip = False
    garbage = False
    for char in data:
        if skip:
            skip = False
            continue
        if garbage:
            match char:
                case "!":
                    skip = True
                case ">":
                    garbage = False
                case _:
                    characters += 1
        else:
            match char:
                case "<":
                    garbage = True
                case "{":
                    level += 1
                case "}" :
                    assert level > 0
                    level -= 1
    return characters

if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
