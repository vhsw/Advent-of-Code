#!/usr/bin/env python


def asleep_guards(path):
    with open(path) as f:
        lines = [line for line in f.read().splitlines()]

    lines.sort()

    guards = {}
    current_gurad = None
    sleep_begin = None
    sleep_end = None
    for line in lines:
        if 'Guard' in line:
            current_gurad = int(line.split('#')[1].split()[0])
            if current_gurad not in guards:
                guards[current_gurad] = [0]*60
            sleep_begin = None
            sleep_end = None
        elif 'falls' in line:
            sleep_begin = int(line[15:17])
        else:
            sleep_end = int(line[15:17])
            for i in range(sleep_begin, sleep_end):
                guards[current_gurad][i] += 1
    # for g in guards:
    #   print(' '.join(str(i) for i in guards[g]))
    best_sleeper_id, data = max(guards.items(), key=lambda i: max(i[1]))
    most_asleep_minute, _ = max(enumerate(data), key=lambda i: i[1])
    # print(best_sleeper_id, most_asleep_minute, data)
    return best_sleeper_id * most_asleep_minute


assert asleep_guards('Day 04/example.txt') == 4455
print(asleep_guards('Day 04/input.txt'))
