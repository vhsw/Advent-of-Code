#!/usr/bin/python3
# this code will run basically forever
# disassembled elven code in disass.py

class Machine:
    def __init__(self, reg=None):
        if not reg:
            reg = [0]*6
        self.reg = reg

    def __repr__(self):
        reg_str = ", ".join([str(int(i)) for i in self.reg])
        return f'Machine([{reg_str}])'

    def __eq__(self, other):
        return self.reg == other.reg

    # Addition:
    def addr(self, a, b, c):
        """
        (add register) stores into register C
        the result of adding register A and register B.
        """
        self.reg[c] = self.reg[a] + self.reg[b]

    def addi(self, a, b, c):
        """
        (add immediate) stores into register C
        the result of adding register A and value B.
        """
        self.reg[c] = self.reg[a] + b

    # Multiplication:
    def mulr(self, a, b, c):
        """
        (multiply register) stores into register C
        the result of multiplying register A and register B.
        """
        self.reg[c] = self.reg[a] * self.reg[b]

    def muli(self, a, b, c):
        """
        (multiply immediate) stores into register C
        the result of multiplying register A and value B.
        """
        self.reg[c] = self.reg[a] * b

    # Bitwise AND:
    def banr(self, a, b, c):
        """
        (bitwise AND register) stores into register C
        the result of the bitwise AND of register A and register B.
        """
        self.reg[c] = self.reg[a] & self.reg[b]

    def bani(self, a, b, c):
        """
        (bitwise AND immediate) stores into register C
        the result of the bitwise AND of register A and value B.
        """
        self.reg[c] = self.reg[a] & b

    # Bitwise OR:
    def borr(self, a, b, c):
        """
        (bitwise OR register) stores into register C
        the result of the bitwise OR of register A and register B.
        """
        self.reg[c] = self.reg[a] | self.reg[b]

    def bori(self, a, b, c):
        """
        (bitwise OR immediate) stores into register C
        the result of the bitwise OR of register A and value B.
        """
        self.reg[c] = self.reg[a] | b

    # Assignment:
    def setr(self, a, b, c):
        """
        (set register) copies the contents of register A
        into register C. (Input B is ignored.)
        """
        self.reg[c] = self.reg[a]

    def seti(self, a, b, c):
        """
        (set immediate) stores value A into register C. (Input B is ignored.)
        """
        self.reg[c] = a

    # Greater-than testing:
    def gtir(self, a, b, c):
        """
        (greater-than immediate/register)
        sets register C to 1 if value A is greater than register B.
        Otherwise, register C is set to 0.
        """
        self.reg[c] = a > self.reg[b]

    def gtri(self, a, b, c):
        """
        (greater-than register/immediate)
        sets register C to 1 if register A is greater than value B.
        Otherwise, register C is set to 0.
        """
        self.reg[c] = self.reg[a] > b

    def gtrr(self, a, b, c):
        """
        (greater-than register/register)
        sets register C to 1 if register A is greater than register B.
        Otherwise, register C is set to 0.
        """
        self.reg[c] = self.reg[a] > self.reg[b]

    # Equality testing:
    def eqir(self, a, b, c):
        """
        (equal immediate/register)
        sets register C to 1 if value A is equal to register B.
        Otherwise, register C is set to 0.
        """
        self.reg[c] = a == self.reg[b]

    def eqri(self, a, b, c):
        """
        (equal register/immediate)
        sets register C to 1 if register A is equal to value B.
        Otherwise, register C is set to 0.
        """
        self.reg[c] = self.reg[a] == b

    def eqrr(self, a, b, c):
        """
        (equal register/register)
        sets register C to 1 if register A is equal to register B.
        Otherwise, register C is set to 0.
        """
        self.reg[c] = self.reg[a] == self.reg[b]


def madness(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    ip_reg_str, *program = raw_data
    ip_reg = int(ip_reg_str[4:])
    m = Machine([1, 0, 0, 0, 0, 0])
    
    while True:     
        instr = program[m.reg[ip_reg]]
        print(instr, m)
        func, *args = instr.split()
        getattr(m, func)(*map(int, args))
        
        if m.reg[ip_reg] + 1 < len(program):
            m.reg[ip_reg] += 1
        else:
            return m.reg[0]

print(madness('Day 19/input.txt'))
