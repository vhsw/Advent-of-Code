"""Day 2 Answers"""


def evaluate(code, noun=None, verb=None):
    """An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.
    Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.
    For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.
    Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
    Once you're done processing an opcode, move to the next one by stepping forward 4 positions."""
    code = code[:]
    if noun is not None:
        code[1] = noun
    if verb is not None:
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


def part1():
    with open("2019/Day 02/input", "r") as f:
        code = list(map(int, f.read().split(",")))
    result = evaluate(code, 12, 2)
    return result[0]


def part2():
    with open("2019/Day 02/input") as f:
        code = list(map(int, f.read().split(",")))
    for noun in range(100):
        for verb in range(100):
            result = evaluate(code, noun, verb)
            if result[0] == 19690720:
                answer = noun * 100 + verb
                return answer
    raise ValueError


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
