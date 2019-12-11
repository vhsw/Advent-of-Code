"""Intcode interpreter v11"""


class InputError(Exception):
    pass


class Intcode:
    """An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong."""

    def __init__(self, code):
        self._ip = 0
        self.mem = dict(enumerate(code))
        self.input_data = []
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
            9: self._relative_base_offset,
            99: self._halt,
        }
        self.__mode = 0
        self.__relative_base = 0
        self.__running = True

    @property
    def running(self):
        """running or halt"""
        return self.__running

    def provide_input(self, data):
        """send input"""
        self.input_data.append(data)
        self._input()

    def evaluate(self):
        """Eval code"""
        while self.__running:
            self.__mode, op = divmod(self.__readimmediate(), 100)
            self.opcodes[op]()

    def __readimmediate(self):
        """read memory at current ip and incrase ip by one"""
        data = self.mem.get(self._ip, 0)
        self._ip += 1
        return data

    def __memread(self):
        """read memory with respect of current mode and increase ip by one"""
        mode = self.__mode % 10
        self.__mode //= 10
        data = self.__readimmediate()
        if mode == 0:
            return self.mem.get(data, 0)
        if mode == 1:
            return data
        if mode == 2:
            position = self.__relative_base + data
            return self.mem.get(position, 0)
        raise ValueError(f"Wrong mode {mode}")

    def __memstore(self, value):
        """store value in memory"""
        position = self.__readimmediate()
        if self.__mode == 0:
            self.mem[position] = value
            return
        if self.__mode == 2:
            position += self.__relative_base
            self.mem[position] = value
            return
        raise ValueError(f"Wrong mode {self.__mode}")

    def _add(self):
        """Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored."""
        a1 = self.__memread()
        a2 = self.__memread()
        self.__memstore(a1 + a2)

    def _mul(self):
        """Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values."""
        a1 = self.__memread()
        a2 = self.__memread()
        self.__memstore(a1 * a2)

    def _input(self):
        """Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50."""
        if not self.input_data:
            raise InputError
        value = self.input_data.pop()
        self.__memstore(value)

    def _output(self):
        """Opcode 4 outputs the value of its only parameter."""
        data = self.__memread()
        self.output_data.append(data)

    def _jump_if_true(self):
        """Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing."""
        param1 = self.__memread()
        param2 = self.__memread()
        if param1 != 0:
            self._ip = param2

    def _jump_if_false(self):
        """Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing."""
        param1 = self.__memread()
        param2 = self.__memread()
        if param1 == 0:
            self._ip = param2

    def _less_than(self):
        """Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        param1 = self.__memread()
        param2 = self.__memread()
        self.__memstore(int(param1 < param2))

    def _equals(self):
        """Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        param1 = self.__memread()
        param2 = self.__memread()
        self.__memstore(int(param1 == param2))

    def _relative_base_offset(self):
        """Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter"""
        param1 = self.__memread()
        self.__relative_base += param1

    def _halt(self):
        """The opcode 99 means that the program is finished and should immediately halt."""
        self.__running = False
