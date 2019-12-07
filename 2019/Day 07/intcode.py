"""Day 5 Answers"""


class Intcode:
    """An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong."""

    def __init__(self, code, input_data=None):
        self._ip = 0
        self.mem = code[:]
        if input_data is None:
            self.input_data = []
        else:
            self.input_data = input_data[::-1]
        self.output_data = []
        self.opcodes = {
            1: self._add,
            2: self._mul,
            3: self._input,
            4: self._output,
            5: self._jump_if_true,
            6: self._jump_if_false,
            7: self._less_than,
            8: self._equals,
            99: self._halt,
        }
        self.__mode = 0
        self.__running = True
        self.__evaluate()

    def __evaluate(self):
        """Eval code"""
        while self.__running:
            self.__mode, op = divmod(self.__readimmediate(), 100)
            self.opcodes[op]()

    def __readimmediate(self):
        """read memory at current ip and incrase ip by one"""
        data = self.mem[self._ip]
        self._ip += 1
        return data

    def __readmem(self):
        """read memory with respect of current mode and increase ip by one"""
        mode = self.__mode % 10
        self.__mode //= 10
        data = self.__readimmediate()
        if mode == 0:
            return self.mem[data]
        if mode == 1:
            return data
        raise ValueError(f"Wrong mode {mode}")

    def __memstore(self, value):
        """store value in memory"""
        assert self.__mode == 0
        position = self.__readimmediate()
        self.mem[position] = value

    def _add(self):
        """Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored."""
        a1 = self.__readmem()
        a2 = self.__readmem()
        self.__memstore(a1 + a2)

    def _mul(self):
        """Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values."""
        a1 = self.__readmem()
        a2 = self.__readmem()
        self.__memstore(a1 * a2)

    def _input(self):
        """Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50."""
        value = self.input_data.pop()
        self.__memstore(value)

    def _output(self):
        """Opcode 4 outputs the value of its only parameter."""
        data = self.__readmem()
        self.output_data.append(data)

    def _jump_if_true(self):
        """Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing."""
        param1 = self.__readmem()
        param2 = self.__readmem()
        if param1 != 0:
            self._ip = param2

    def _jump_if_false(self):
        """Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing."""
        param1 = self.__readmem()
        param2 = self.__readmem()
        if param1 == 0:
            self._ip = param2

    def _less_than(self):
        """Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        param1 = self.__readmem()
        param2 = self.__readmem()
        self.__memstore(int(param1 < param2))

    def _equals(self):
        """Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        param1 = self.__readmem()
        param2 = self.__readmem()
        self.__memstore(int(param1 == param2))

    def _halt(self):
        """The opcode 99 means that the program is finished and should immediately halt."""
        self.__running = False


INPUT = "2019/Day 05/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as f:
        code = list(map(int, f.read().split(",")))
    ic = Intcode(code, input_data=[1])
    code, out = ic.mem, ic.output_data
    return out[-1]


def part2():
    """Part 2 answer"""
    with open(INPUT) as f:
        code = list(map(int, f.read().split(",")))
    ic = Intcode(code, input_data=[5])
    code, out = ic.mem, ic.output_data
    return out[0]


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
