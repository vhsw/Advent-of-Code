"""Day 20: Pulse Propagation"""
from collections import deque
from dataclasses import dataclass, field
from functools import cached_property
from math import lcm

with open("2023/Day 20/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    network = Network.from_str(data)
    for _ in range(1000):
        network.press_the_button()
    return network.pulses[True] * network.pulses[False]


def part2(data: str):
    """Part 2 solution"""
    network = Network.from_str(data)
    step = 0
    while not all(network.loops.values()):
        step += 1
        network.press_the_button(step)
        if network.modules["rx"].got_low:
            return step

    return lcm(*network.loops.values())


@dataclass
class Module:
    destinations: list[str]

    def process(self, sender: str, signal: bool):
        return signal


@dataclass
class Rx(Module):
    destinations: list[str]
    got_low = False

    def process(self, sender: str, signal: bool):
        if not signal:
            self.got_low = True
        return signal


@dataclass
class FlipFlop(Module):
    state: bool = False

    def process(self, sender, signal):
        if signal:
            return

        self.state = not self.state
        return self.state


@dataclass
class Conjunction(Module):
    state: dict[str, bool] = field(default_factory=dict)

    def process(self, sender, signal):
        self.state[sender] = signal
        return not all(self.state.values())


def make_module(line: str) -> tuple[str, Module]:
    name, connections_str = line.split(" -> ")
    connections = connections_str.split(", ")
    prefix = name[0]
    module: type[Module]
    if prefix in "%&":
        name = name[1:]
        if prefix == "%":
            module = FlipFlop
        else:
            module = Conjunction
    else:
        module = Module
    return name, module(connections)


@dataclass
class Network:
    modules: dict[str, Module]
    pulses: dict[bool, int] = field(default_factory=lambda: {True: 0, False: 0})
    _history: dict[str, list[int]] = field(init=False)

    def __post_init__(self):
        self._history = {key: [] for key in self.loop_nand_names}

    @classmethod
    def from_str(cls, data: str):
        modules: dict[str, Module] = {}
        destinations: set[str] = set()
        for line in data.splitlines():
            name, module = make_module(line)
            modules[name] = module
            destinations.update(module.destinations)
        modules["rx"] = Rx([])
        for dst in destinations:
            modules.setdefault(dst, Module([]))
        for name, module in modules.items():
            for dst in module.destinations:
                dst_module = modules[dst]
                if isinstance(dst_module, Conjunction):
                    dst_module.state[name] = False

        return cls(modules)

    @cached_property
    def loop_nand_names(self):
        for module in self.modules.values():
            if "rx" in module.destinations:
                last_nand = module
                break
        else:
            return set()
        assert isinstance(last_nand, Conjunction)
        nands: set[str] = set()
        for name in last_nand.state:
            inverter = self.modules[name]
            assert isinstance(inverter, Conjunction)
            nands.update(inverter.state)
        return nands

    @property
    def loops(self):
        loops: dict[str, int | None] = {}
        for name in self.loop_nand_names:
            history = self._history[name]
            if len(history) < 2:
                loops[name] = None
                continue
            loops[name] = history[1] - history[0]
        return loops

    def press_the_button(self, step=0):
        self.send("button", "broadcaster", False, step)

    def send(self, src: str, dst: str, signal: bool, step):
        todo = deque([(src, dst, signal)])
        while todo:
            src, dst, signal = todo.popleft()
            # print(f"{src} -{['low', 'high'][signal]}-> {dst}")
            self.pulses[signal] += 1
            result = self.modules[dst].process(src, signal)
            if dst in self.loop_nand_names and result is False:
                self._history[dst].append(step)

            if result is None:
                continue
            for dst_name in self.modules[dst].destinations:
                todo.append((dst, dst_name, result))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
