#!/usr/bin/python3


class Rule:
    def __init__(self, line):
        self.pattern, self.result = line.split(' => ')
        self.pattern = list(self.pattern)

    def __repr__(self):
        return f'''Rule('{''.join(self.pattern)} => {self.result}')'''


def plants(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    init_state = list(raw_data[0][15:])
    rules = tuple(map(Rule, raw_data[2:]))
    state_str = ''.join(init_state)
    width = 80
    print(' 0', state_str.center(width))
    state_pad = 0
    for gen in range(20):
        while init_state[:5] != ['.']*5:
            init_state.insert(0, '.')
            state_pad += 1
        while init_state[-5:] != ['.']*5:
            init_state.append('.')

        state = init_state[:2]
        for i in range(len(init_state)-5):
            group = init_state[i:i+5]
            for rule in rules:
                if group == rule.pattern:
                    state.append(rule.result)
                    break
            else:
                state.append('.')            
        state.extend(init_state[-3:])
        state_str = ''.join(state)
        print(f'{gen + 1:2d}', state_str.center(width))
        init_state = state
    total = 0
    for i, p in enumerate(init_state):
        if p == '#':
            total += i-state_pad
    return total


assert plants('Day 12/example.txt') == 325
print(plants('Day 12/input.txt'))
