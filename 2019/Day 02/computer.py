def evaluate(code, noun, verb):
    code = code[:]
    code[1] = noun
    code[2] = verb
    pos = 0
    while True:
        opcode = code[pos]
        if opcode == 1:
            arg1 = code[pos + 1]
            arg2 = code[pos + 2]
            store = code[pos + 3]
            code[store] = code[arg1] + code[arg2]
        elif opcode == 2:
            arg1 = code[pos + 1]
            arg2 = code[pos + 2]
            store = code[pos + 3]
            code[store] = code[arg1] * code[arg2]
        elif opcode == 99:
            return code
        else:
            raise ValueError("Wrong opcode", opcode)
        pos += 4


if __name__ == "__main__":
    with open("input", "r") as f:
        code = list(map(int, f.read().split(",")))
    print(code)
    result = evaluate(code, 12, 2)
    print(code)
    print(f"Part 1: {code[0]}")

    for noun in range(100):
        for verb in range(100):
            result = evaluate(code, noun, verb)
            if result[0] == 19690720:
                print(f"Noun = {noun}, Verb = {verb}")
                print(f"Part 2: {noun * 100 + verb}")
