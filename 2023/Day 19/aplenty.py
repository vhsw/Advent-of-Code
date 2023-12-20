"""Day 19: Aplenty"""
from dataclasses import dataclass
from math import prod
from typing import NamedTuple

with open("2023/Day 19/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()

MIN_ATTR = 1
MAX_ATTR = 4000


def part1(data: str):
    """Part 1 solution"""
    workflows, parts = parse(data)
    accepted: set[Part] = set()
    for part in parts:
        accepted.update(execute(workflows, part))
    return sum(interval.start for part in accepted for interval in part)


def part2(data: str):
    """Part 2 solution"""
    workflows, _ = parse(data)
    part = Part(*(Interval(MIN_ATTR, MAX_ATTR) for _ in "xmas"))
    parts = execute(workflows, part)
    return sum(
        prod(interval.end - interval.start + 1 for interval in part) for part in parts
    )


def parse(data: str):
    workflows, parts = data.split("\n\n")
    return parse_workflows(workflows), parse_parts(parts)


class Interval(NamedTuple):
    start: int
    end: int

    def __and__(self, other: "Interval"):
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        if (end - start) < 0:
            return None
        return self.__class__(start, end)


class Part(NamedTuple):
    x: Interval
    m: Interval
    a: Interval
    s: Interval

    @classmethod
    def from_str(cls, line: str):
        items: dict[str, Interval] = {}
        for item in line.strip(r"{}").split(","):
            k, v = item.split("=")
            value = int(v)
            items[k] = Interval(value, value)
        return cls(**items)

    def __or__(self, new_data: dict[str, Interval]):
        data = self._asdict()  # pylint: disable=no-member
        return self.__class__(**(data | new_data))


def parse_parts(data: str):
    return list(map(Part.from_str, data.splitlines()))


class Rule(NamedTuple):
    attr: str
    interval: Interval
    step: str

    @classmethod
    def from_str(cls, rule: str):
        condition, step = rule.split(":")
        value = int(condition[2:])
        interval = (
            Interval(value + 1, MAX_ATTR)
            if condition[1] == ">"
            else Interval(MIN_ATTR, value - 1)
        )
        return cls(
            attr=condition[0],
            interval=interval,
            step=step,
        )


@dataclass
class Rules:
    name: str
    rules: list[Rule]
    default: str
    raw: str

    @classmethod
    def from_str(cls, line: str):
        name, rules_str = line.split("{")
        rules_str = rules_str.removesuffix("}")
        *rules, default = rules_str.split(",")
        return cls(name, list(map(Rule.from_str, rules)), default, line)

    def apply(self, part: Part):
        for rule in self.rules:
            interval: Interval = getattr(part, rule.attr)
            if overlap := rule.interval & interval:
                yield rule.step, part | {rule.attr: overlap}
                if interval.start < overlap.start:
                    yield self.name, part | {
                        rule.attr: Interval(interval.start, overlap.start - 1)
                    }
                if interval.end > overlap.end:
                    yield self.name, part | {
                        rule.attr: Interval(overlap.end + 1, interval.end)
                    }
                break
        else:
            yield self.default, part


def parse_workflows(data: str):
    workflows: dict[str, Rules] = {}
    for line in data.splitlines():
        rule = Rules.from_str(line)
        workflows[rule.name] = rule
    return workflows


def execute(workflows: dict[str, Rules], part: Part):
    accepted: set[Part] = set()
    todo = [("in", part)]
    while todo:
        step, part = todo.pop()
        if step == "R":
            continue
        if step == "A":
            accepted.add(part)
            continue
        todo.extend(workflows[step].apply(part))

    return accepted


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
