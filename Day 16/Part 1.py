#!/usr/bin/env python


class InvalidRegister(Exception):
    pass


class Machine:
    def __init__(self, r0=0, r1=0, r2=0, r3=0):
        self.reg = [r0, r1, r2, r3]

    def __repr__(self):
        return f'Machine({", ".join(str(r) for r in self.reg)})'

    def __eq__(self, other):
        return self.reg == other.reg

    def _assure_valid_reg(self, a):
        if not 0 <= a <= len(self.reg):
            raise InvalidRegister(a)
    # Addition:

    def addr(self, a, b, c):
        """
        (add register) stores into register C the result of adding register A and register B.
        """
        map(self._assure_valid_reg, (a, b, c))
        self.reg[c] = self.reg[a] + self.reg[b]

    def addi(self, a, b, c):
        """
        (add immediate) stores into register C the result of adding register A and value B.
        """
        map(self._assure_valid_reg, (a, c))
        self.reg[c] = self.reg[a] + b

    # Multiplication:

    def mulr(self, a, b, c):
        """
        (multiply register) stores into register C the result of multiplying register A and register B.
        """
        map(self._assure_valid_reg, (a, b, c))
        self.reg[c] = self.reg[a] * self.reg[b]

    def muli(self, a, b, c):
        """
        (multiply immediate) stores into register C the result of multiplying register A and value B.
        """
        map(self._assure_valid_reg, (a, c))
        self.reg[c] = self.reg[a] * b

    # Bitwise AND:

    def banr(self, a, b, c):
        """
        (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
        """
        map(self._assure_valid_reg, (a, b, c))
        self.reg[c] = self.reg[a] & self.reg[b]

    def bani(self, a, b, c):
        """
        (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
        """
        map(self._assure_valid_reg, (a, c))
        self.reg[c] = self.reg[a] & b

    # Bitwise OR:

    def borr(self, a, b, c):
        """
        (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
        """
        map(self._assure_valid_reg, (a, b, c))
        self.reg[c] = self.reg[a] | self.reg[b]

    def bori(self, a, b, c):
        """
        (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
        """
        map(self._assure_valid_reg, (a, c))
        self.reg[c] = self.reg[a] | self.reg[b]

    # Assignment:

    def setr(self, a, b, c):
        """
        (set register) copies the contents of register A into register C. (Input B is ignored.)
        """
        map(self._assure_valid_reg, (a, c))
        self.reg[c] = self.reg[a]

    def seti(self, a, b, c):
        """
        (set immediate) stores value A into register C. (Input B is ignored.)
        """
        map(self._assure_valid_reg, (c,))
        self.reg[c] = a

    # Greater-than testing:

    def gtir(self, a, b, c):
        """
        (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        """
        map(self._assure_valid_reg, (b, c))
        self.reg[c] = a > self.reg[b]

    def gtri(self, a, b, c):
        """
        (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
        """
        map(self._assure_valid_reg, (a, c))
        self.reg[c] = self.reg[a] > b

    def gtrr(self, a, b, c):
        """
        (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
        """
        map(self._assure_valid_reg, (a, b, c))
        self.reg[c] = self.reg[a] > self.reg[b]

    # Equality testing:

    def eqir(self, a, b, c):
        """
        (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        """
        map(self._assure_valid_reg, (b, c))
        self.reg[c] = a == self.reg[b]

    def eqri(self, a, b, c):
        """
        (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
        """
        map(self._assure_valid_reg, (a, c))
        self.reg[c] = self.reg[a] == b

    def eqrr(self, a, b, c):
        """
        (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
        """
        map(self._assure_valid_reg, (a, b, c))
        self.reg[c] = self.reg[a] == self.reg[b]


class Test:
    def __init__(self, lines):
        before, instruntion, after = lines.splitlines()

        self.init_state = tuple(map(int, before[9:-1].split(', ')))
        self.opcode, *self.args = map(int, instruntion.split())
        test_state = tuple(map(int, after[9:-1].split(', ')))
        self.test_machine = Machine(*test_state)

    def get_valid_opcodes(self):
        valid_opcodes = []
        method_list = [func for func in dir(Machine) if callable(
            getattr(Machine, func)) and not func.startswith("_")]
        for opcode in method_list:
            m = Machine(*self.init_state)
            getattr(Machine, opcode)(m, *self.args)
            if m == self.test_machine:
                valid_opcodes.append(opcode)
        return valid_opcodes


def madness(path):
    with open(path) as f:
        raw_data = f.read().split('\n\n\n\n')[0]
    commands = [Test(lines) for lines in raw_data.split('\n\n')]

    n = 0
    for c in commands:
        if len(c.get_valid_opcodes()) >= 3:
            n += 1
    return n


assert madness('Day 16/example.0.txt') == 1
# assert madness('Day 15/example.1.txt') == (7, 3)
print(madness('Day 16/input.txt'))
