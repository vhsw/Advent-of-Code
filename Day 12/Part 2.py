#!/usr/bin/env python


class Rule:
    def __init__(self, line):
        self.pattern, self.result = line.split(' => ')
        self.pattern = list(self.pattern)

    def __repr__(self):
        return f'''Rule('{''.join(self.pattern)} => {self.result}')'''


def plants(path, max_gen):
    with open(path) as f:
        raw_data = f.read().splitlines()
    init_state = list(raw_data[0][15:])
    rules = tuple(map(Rule, raw_data[2:]))
    state_pad = 0
    growth_rate = [0]*10
    prev_total = 0
    for gen in range(max_gen):
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
        init_state = state
        total = 0
        for i, p in enumerate(init_state):
            if p == '#':
                total += i-state_pad
        del growth_rate[0]
        growth_rate.append(total-prev_total)
        prev_total = total
        if all(growth_rate[0] == g for g in growth_rate):
            return growth_rate[0] * (max_gen - gen -1) + total
    return total


assert plants('Day 12/example.txt', 20) == 325
assert plants('Day 12/example.txt', 477) == 8914
print(plants('Day 12/input.txt', 50000000000))

 
