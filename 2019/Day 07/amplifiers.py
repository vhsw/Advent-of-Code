"""Day 07 Answers"""
from itertools import permutations
from intcode import Intcode
from intcode_generator import Intcode as Intcode_generator


INPUT = "2019/Day 07/input"


def amps_chain(code):
    """Your job is to find the largest output signal that can be sent to the thrusters by trying every possible combination of phase settings on the amplifiers."""
    max_signal = None
    for phases in permutations(range(5)):
        signal = 0
        for phase in phases:
            amp = Intcode(code, input_data=[phase, signal])
            assert len(amp.output_data) == 1
            signal = amp.output_data[0]
        if max_signal is None or signal > max_signal:
            max_signal = signal
    return max_signal


def feedback(code):
    """Your job is to find the largest output signal that can be sent to the thrusters using the new phase settings and feedback loop arrangement."""
    max_signal = None
    for phases in permutations(range(5, 10)):
        signal = 0
        amps = []
        for phase in phases:
            amp = Intcode_generator(code, [phase])
            amps.append(amp)
        run = True
        while run:
            for amp in amps:
                amp.input_data.append(signal)
                out = amp.evaluate()
                if out is None:
                    assert amp == amps[0]
                    run = False
                    break
                signal = out

        if max_signal is None or signal > max_signal:
            max_signal = signal
    return max_signal


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        code = list(map(int, data.read().split(",")))

    return amps_chain(code)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        code = list(map(int, data.read().split(",")))

    return feedback(code)


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
