#!/usr/bin/env python


class Cart:
    n_carts = 0

    @classmethod
    def get_cart_id(cls):
        cls.n_carts += 1
        return cls.n_carts - 1

    def __init__(self, direction, x, y):
        self.id = self.__class__.get_cart_id()
        self.direction = direction
        self.x = x
        self.y = y
        self.n_turns = 0

    def left_turn(self):
        dirs = '^<v>^'
        idx = dirs.index(self.direction)
        self.direction = dirs[idx + 1]

    def right_turn(self):
        dirs = '^>v<^'
        idx = dirs.index(self.direction)
        self.direction = dirs[idx + 1]

    def go_straight(self):
        pass

    def move(self, point):
        if self.direction == '>':
            self.y += 1
        if self.direction == '<':
            self.y -= 1
        if self.direction == '^':
            self.x -= 1
        if self.direction == 'v':
            self.x += 1
        if point == '/':
            if self.direction in '<>':
                self.left_turn()
            else:
                self.right_turn()
        elif point == '\\':
            if self.direction in '^v':
                self.left_turn()
            else:
                self.right_turn()
        elif point == '+':
            [self.left_turn, self.go_straight, self.right_turn][self.n_turns % 3]()
            self.n_turns += 1

    def __repr__(self):
        return f'''Cart('{self.direction}', {self.x}, {self.y}')'''


class Board:
    def __init__(self, lines):
        self.grid = [[' ' for l in line] for line in lines]
        self.carts = []
        self.crash = None
        for i in range(len(lines)):
            for j in range(len(list(lines[0]))):
                point = lines[i][j]
                if point in '<>^v':
                    self.carts.append(Cart(point, i, j))
                    point = {'<': '-', '>': '-', '^': '|', 'v': '|'}[point]
                self.grid[i][j] = point

    def __str__(self):
        grid = []
        for i in range(len(self.grid)):
            row = []
            for j in range(len(self.grid[0])):
                char = self.grid[i][j]
                for cart in self.carts:
                    if cart.x == i and cart.y == j:
                        char = cart.direction
                        break
                if self.crash and self.crash == (i, j):
                    char = 'X'
                row.append(char)
            grid.append(row)
        return '\n'.join(''.join(line) for line in grid[:35]) + '\n'

    def get(self, x, y, direction):
        if direction == '>':
            try:
                return self.grid[x][y+1]
            except:
                return
        if direction == '<':
            try:
                return self.grid[x][y-1]
            except:
                return

        if direction == '^':
            try:
                return self.grid[x-1][y]
            except:
                return

        if direction == 'v':
            try:
                return self.grid[x+1][y]
            except:
                return

    def step(self):
        self.carts.sort(key=lambda c: (c.x, c.y))
        cart_positions = []
        for cart in self.carts:
            cart_positions.append((cart.id, cart.x, cart.y))
        crashed_carts = []
        for cart in self.carts:
            point = self.get(cart.x, cart.y, cart.direction)
            cart.move(point)
            cart_positions.pop(0)
            for other_cart_pos in cart_positions:
                if cart.x == other_cart_pos[1] and cart.y == other_cart_pos[2]:
                    crashed_carts.extend((cart.id, other_cart_pos[0]))
            cart_positions.append((cart.id, cart.x, cart.y))
        self.carts = [
            cart for cart in self.carts if cart.id not in crashed_carts]


def madness(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    board = Board(raw_data)
    while len(board.carts) > 1:
        # print(board)
        board.step()
        # import time; time.sleep(.5)
    last_cart = board.carts[0]
    return last_cart.y, last_cart.x


assert madness('Day 13/example.2.txt') == (6, 4)
print(madness('Day 13/input.txt'))
