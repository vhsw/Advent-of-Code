"""Day 16: Packet Decoder"""
from math import prod

with open("2021/Day 16/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()

version_sum = 0


def part1(data: str):
    """Part 1 solution"""
    global version_sum
    version_sum = 0
    val = bin(int(data, 16))[2:].rjust(len(data) * 4, "0")
    read_packet(val)
    return version_sum


def part2(data: str):
    """Part 2 solution"""
    val = bin(int(data, 16))[2:].rjust(len(data) * 4, "0")
    value, _ = read_packet(val)
    return value


def read_packet(val: str):
    version = int(val[:3], 2)
    global version_sum
    version_sum += version
    type_id = int(val[3:6], 2)
    if type_id == 4:
        value, consumed = get_liteal(val[6:])
        return value, 6 + consumed

    operands, consumed = get_operands(val[6:])
    match type_id:
        case 0:
            value = sum(operands)
        case 1:
            value = prod(operands)
        case 2:
            value = min(operands)
        case 3:
            value = max(operands)
        case 5:
            value = int(operands[0] > operands[1])
        case 6:
            value = int(operands[0] < operands[1])
        case 7:
            value = int(operands[0] == operands[1])
    return value, 6 + consumed


def get_operands(val: str):
    length_type_id = val[0]
    val = val[1:]
    match length_type_id:
        case "0":
            total_length = int(val[:15], 2)
            operands, consumed = read_length(val[15:], total_length)
            return operands, 16 + consumed
        case "1":
            n_sub_packets = int(val[:11], 2)
            operands, consumed = read_sub_packets(val[11:], n_sub_packets)
            return operands, 12 + consumed
    raise ValueError(length_type_id)


def read_length(val: str, length: int):
    consumed = 0
    operands = []
    while consumed < length:
        value, cons = read_packet(val[consumed:])
        operands.append(value)
        consumed += cons
    return operands, consumed


def read_sub_packets(val: str, n_packets: int):
    consumed = 0
    operands = []
    for _ in range(n_packets):
        value, cons = read_packet(val[consumed:])
        operands.append(value)
        consumed += cons
    return operands, consumed


def get_liteal(val: str):
    """return liteal, consumed"""
    pos = 0
    packet = []
    while True:
        packet.extend(val[pos + 1 : pos + 5])
        if val[pos] == "0":
            break
        pos += 5
    return int("".join(packet), 2), pos + 5


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
