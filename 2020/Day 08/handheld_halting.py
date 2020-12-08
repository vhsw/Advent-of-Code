"Day 08 answers"
INPUT = "2020/Day 08/input.txt"


def run(code):
    acc = 0
    ip = 0
    seen = set()

    while ip < len(code):
        if ip in seen:
            raise RuntimeError(acc)
        seen.add(ip)
        ins, val = code[ip]
        if ins == "acc":
            acc += val
            ip += 1
            continue
        if ins == "nop":
            ip += 1
            continue
        if ins == "jmp":
            ip += val

    return acc


def part1(data):
    "Part 1 answer"
    code = []
    for line in data:
        ins, val = line.split(" ")
        val = int(val)
        code.append((ins, val))
    try:
        run(code)
    except RuntimeError as e:
        return e.args[0]


def part2(data):
    "Part 2 answer"
    code = []
    for line in data:
        ins, val = line.split(" ")
        val = int(val)
        code.append((ins, val))
    for i in range(len(code)):
        ins, val = code[i]
        if ins == "acc":
            continue
        ins = {"nop": "jmp", "jmp": "nop"}[ins]
        new_code = code[:i] + [(ins, val)] + code[i + 1 :]
        try:
            acc = run(new_code)
        except RuntimeError:
            continue
        else:
            return acc


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
