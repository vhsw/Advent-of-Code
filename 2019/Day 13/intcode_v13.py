"""Intcode interpreter v13"""

import time
from curses import error


class InputError(Exception):
    pass


class Intcode:
    """An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong."""

    def __init__(self, code, stdscr=None):
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
        self.__stdscr = stdscr
        self.__ball = None
        self.__bar = None
        self.score = 0
        self.__skip_frames = 0

    @property
    def running(self):
        """running or halt"""
        return self.__running

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

    @property
    def parsed_output(self):
        """dict with output instructions"""
        data = self.output_data
        args = [iter(data)] * 3
        return zip(*args)

    def _display(self):
        """The arcade cabinet runs Intcode software like the game the Elves sent (your puzzle input). It has a primitive screen capable of drawing square tiles on a grid. The software draws tiles to the screen with output instructions: every three output instructions specify the x position (distance from the left), y position (distance from the top), and tile id. The tile id is interpreted as follows:
        0 is an empty tile. No game object appears in this tile.
        1 is a wall tile. Walls are indestructible barriers.
        2 is a block tile. Blocks can be broken by the ball.
        3 is a horizontal paddle tile. The paddle is indestructible.
        4 is a ball tile. The ball moves diagonally and bounces off objects."""
        stdscr = self.__stdscr
        if stdscr is None:
            return
        for col, row, tile in self.parsed_output:
            if col == -1 and row == 0:
                self.score = tile
                stdscr.addstr(0, 0, f"Score: {tile}")
                continue
            try:
                stdscr.addch(row, col, " #*_O"[tile])
            except error:
                pass
            if tile == 3:
                self.__bar = col
            if tile == 4:
                self.__ball = col
        if self.score < 8000 or self.__skip_frames > 20:
            stdscr.refresh()
            self.__skip_frames = 0
        self.__skip_frames += 1

    def _input(self):
        """Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50."""

        self._display()
        if self.__ball > self.__bar:
            value = 1
        elif self.__ball < self.__bar:
            value = -1
        else:
            value = 0

        self.__memstore(value)
        if self.score < 3000:
            time.sleep(1 / 30)

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
        self._display()
